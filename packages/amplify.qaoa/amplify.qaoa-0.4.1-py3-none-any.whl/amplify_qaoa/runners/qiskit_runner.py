from __future__ import annotations

import time
import datetime
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.opflow import EvolutionFactory, X, Z, H, I
from qiskit.opflow.primitive_ops.pauli_op import PauliOp
from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp
from qiskit_aer import AerSimulator
from qiskit_ibm_provider import IBMProvider, least_busy
from scipy.optimize import minimize
from random import sample

from .core import AbstractQAOARunner, decode_solutions, IsingDict


def _get_time_from_result(result_date: str | datetime.datetime) -> datetime.datetime:
    if type(result_date) is str:
        try:
            timestamp = datetime.datetime.strptime(result_date, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            timestamp = datetime.datetime.strptime(result_date, "%Y-%m-%dT%H:%M:%S")

        return timestamp
    else:
        return result_date


def PauliZ(n_qubit: int, i: int) -> PauliOp:
    return (I ^ (n_qubit - i - 1)) ^ Z ^ (I ^ i)


def PauliX(n_qubit: int, i: int) -> PauliOp:
    return (I ^ (n_qubit - i - 1)) ^ X ^ (I ^ i)


def generate_hamiltonian(
    f_dict: IsingDict,
    wires: int,
) -> PauliSumOp:
    op_f = 0 * (I ^ wires)
    for key, value in f_dict.items():
        op_tmp = I ^ wires
        key = set(key)
        if len(key) > 0:
            for i in key:
                op_tmp = op_tmp.compose(PauliZ(wires, i))
        op_f += value * op_tmp
    return op_f


def compute_function_value(
    f_dict: IsingDict,
    counts: List[Tuple[List[int], int]],
) -> float:
    f_val = 0
    stat_sum = 0
    for count in counts:
        sol, stat = count
        stat_sum += stat
        for key, val in f_dict.items():
            tmp = val
            for i in key:
                tmp *= sol[i]
            f_val += tmp * stat
    return f_val / stat_sum


def qaoa_ansatz(
    op_f: PauliSumOp,
    wires: int,
    parameters: List[float],
    reps: int,
) -> QuantumCircuit:
    # Generate mixer
    op_mixer = 0 * (I ^ wires)
    for i in range(wires):
        op_mixer += PauliX(wires, i)

    # Generate whole circuit
    op_circuit = H ^ wires
    for idx in range(reps):
        op_circuit = (op_f * parameters[idx]).exp_i().compose(op_circuit)
        op_circuit = (op_mixer * parameters[reps + idx]).exp_i().compose(op_circuit)
    evolution = EvolutionFactory.build(op_f)
    op_circuit = evolution.convert(op_circuit)
    circuit = op_circuit.to_circuit()

    return circuit


def constrained_ansatz(
    wires: int,
    parameters: List[float],
    reps: int,
    group_list: List[List[int]],
    init_ones: List[int] = [],
) -> QuantumCircuit:
    # Prepare group
    not_grouped = set(range(wires))
    for group in group_list:
        not_grouped -= set(group)

    k = 0
    circuit = QuantumCircuit(wires)
    for i in init_ones:
        circuit.x(i)
    for i in not_grouped:
        circuit.rx(parameters[k], i)
        k += 1

    for _ in range(reps):
        for group in group_list:
            m = len(group)
            for i in range(m // 2):
                a = 2 * i
                b = 2 * i + 1
                circuit.cx(group[a], group[b])
                circuit.ry(parameters[k], group[a])
                circuit.cx(group[b], group[a])
                circuit.ry(-parameters[k], group[a])
                circuit.cx(group[a], group[b])
                k += 1
            for i in range((m - 1) // 2):
                a = 2 * i + 1
                b = 2 * i + 2
                circuit.cx(group[a], group[b])
                circuit.ry(parameters[k], group[a])
                circuit.cx(group[b], group[a])
                circuit.ry(-parameters[k], group[a])
                circuit.cx(group[a], group[b])
                k += 1

    return circuit


Device_Type = ["CPU", "GPU", "QPU"]


class QiskitRunner(AbstractQAOARunner):
    __token: Optional[str] = None
    __provider: Any = None
    __device: str = "CPU"
    __backend_name: Optional[str] = None
    __backend: Any = None

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        if not self.__token == value:
            self.__provider = IBMProvider(token=value) if value is not None else None

            # Reset backend
            self.__backend = None

        self.__token = value

    @property
    def provider(self):
        return self.__provider

    @property
    def device(self):
        return self.__device

    @device.setter
    def device(self, value):
        if value not in Device_Type:
            raise RuntimeError("Specified device type is not supported.")

        if not self.__device == value:
            # Reset backend
            self.__backend = None

        self.__device = value

    @AbstractQAOARunner.shots.setter
    def shots(self, value):
        if self.__backend is not None and not self._shots == value:
            self.__backend.set_options(shots=value)

        self._shots = value

    @property
    def backend_name(self):
        return self.__backend_name

    @backend_name.setter
    def backend_name(self, value):
        if not self.__backend_name == value:
            # Reset backend
            self.__backend = None

        self.__backend_name = value

    @property
    def backend(self):
        return self.__backend

    def __init__(
        self,
        reps: int = 10,
        shots: Optional[int] = 1024,
        backend_name: Optional[str] = None,
        device: str = "CPU",
        token: Optional[str] = None,
    ) -> None:
        super().__init__(reps, shots)

        if device not in Device_Type:
            raise RuntimeError("Specified device type is not supported.")

        self.backend_name = backend_name
        self.device = device
        self.token = token

    def _load_backend(self, wires: int) -> None:
        # If backend is None, must load backend.
        # If wires is larger than the number of qubits of the current backend, the backend can't be applied to the problem.
        # If token is available or backend is not specified, must update the least busy backend.
        # Otherwise, the current backend is also available to the Ising model.
        if (
            self.__backend is not None
            and wires <= self.__backend.configuration().n_qubits
            and (self.__token is None or not self.__backend_name is None)
        ):
            return

        if self.__device in ["CPU", "GPU"]:
            if self.__backend_name is not None:
                # Simulation of ideal machine with specified backend
                if self.__provider is not None:
                    if self.__backend_name in AerSimulator().available_methods():
                        self.__backend = AerSimulator(method=self.backend_name)
                    else:
                        # Simulation of actual machine with specified backend
                        self.__backend = AerSimulator.from_backend(
                            self.provider.get_backend(self.backend_name)
                        )
                else:
                    # Simulation of ideal machine with specified backend
                    self.__backend = AerSimulator(method=self.backend_name)
            else:
                if self.provider is not None:
                    # Simulation of actual machine with least busy backend
                    backend_list = self.provider.backends(
                        filters=lambda x: x.configuration().n_qubits >= wires
                        and not x.configuration().simulator
                    )
                    if backend_list == []:
                        raise RuntimeError("Available backend is not found.")
                    self.__backend = AerSimulator.from_backend(
                        least_busy((backend_list))
                    )
                else:
                    # Simulation of ideal machine with default simulator
                    self.__backend = AerSimulator(
                        method="automatic", device=self.device
                    )
        elif self.device == "QPU":
            if self.provider is not None:
                if self.backend_name is not None:
                    # Run an actual machine with specified backend
                    self.__backend = self.__provider.get_backend(self.__backend_name)
                else:
                    # Run an actual machine with least busy backend
                    backend_list = self.provider.backends(
                        filters=lambda x: x.configuration().n_qubits >= wires
                        and not x.configuration().simulator
                    )
                    if backend_list == []:
                        raise RuntimeError("Available backend is not found.")
                    self.__backend = least_busy(backend_list)
            else:
                raise RuntimeError('Specified device is "QPU", but a token is not set.')
        else:
            raise NotImplementedError("Invalid device is specified.")

        self.__backend.set_options(shots=self.shots)

        if self.__device in ["CPU", "GPU"]:
            self.__backend.set_options(device=self.device)

    def tune(
        self,
        f_dict: IsingDict,
        wires: int,
        optimizer: str = "COBYLA",
        group_list: List[List[int]] = [],
        init_ones: List[int] = [],
        initial_parameters: Optional[List[float]] = None,
    ) -> Dict[str, Any]:
        # Time count for tune function
        init_tune_total_time = time.perf_counter()

        # Set shots to backend engine
        self._load_backend(wires)

        # Create init_one list
        if group_list != [] and init_ones == []:
            for group in group_list:
                init_ones += sample(group, 1)

        # Prepare parameters
        if group_list == []:
            k = 2 * self.reps
        else:
            k = 0
            not_grouped = set(range(wires))
            for group in group_list:
                m = len(group)
                k += m // 2 + (m - 1) // 2
                not_grouped -= set(group)
            k *= self.reps
            k += len(not_grouped)

        if initial_parameters is None:
            initial_parameters = np.random.rand(k).tolist()

        parameter_values_history = list()

        # Time count for qiskit
        tune_qiskit_time = 0.0
        tune_total_machine_time = 0.0
        tune_machine_job_time = 0.0

        def cost_function(params_val):
            parameter_values_history.append(params_val)
            # Time count for cost function
            init_time_cf = time.perf_counter()

            if group_list == []:
                qc = qaoa_ansatz(
                    generate_hamiltonian(f_dict, wires), wires, params_val, self.reps
                )
            else:
                qc = constrained_ansatz(
                    wires, params_val, self.reps, group_list, init_ones
                )
            qc.measure_all()
            qc = transpile(qc, self.backend)
            init_tune_total_machine_time = datetime.datetime.now()
            job = self.backend.run(qc)
            result = job.result().to_dict()
            value = compute_function_value(
                f_dict, decode_solutions(job.result().get_counts())
            )

            nonlocal tune_qiskit_time
            tune_qiskit_time += time.perf_counter() - init_time_cf
            nonlocal tune_machine_job_time
            tune_machine_job_time += result["time_taken"]

            if hasattr(job, "time_per_step"):
                time_stamp = job.time_per_step()
                if "CREATED" in time_stamp:
                    init_tune_total_machine_time = time_stamp["CREATED"]

            end_tune_total_machine_time = _get_time_from_result(result["date"])

            nonlocal tune_total_machine_time
            tune_total_machine_time += (
                end_tune_total_machine_time - init_tune_total_machine_time
            ).total_seconds()
            return value

        # Time count for minimize
        init_tune_minimize_time = time.perf_counter()
        res = minimize(
            cost_function,
            initial_parameters,
            method=optimizer,
        )
        tune_minimize_time = time.perf_counter() - init_tune_minimize_time

        self._f_dict = f_dict
        self._wires = wires
        self._opt_params = res["x"]
        self._group_list = group_list
        self._init_ones = init_ones

        tune_total_time = time.perf_counter() - init_tune_total_time

        # The dictionary of time counts
        # tune_total_time: the total time taken by tune function
        # tune_qiskit_running_time: the total qiskit running time
        # tune_total_machine_time: the total time taken by the IBMQ machine (including waiting time)
        # tune_machine_running_time: the actual machine running time
        # tune_minimize_time: the time taken by the scipy minimize function
        # tune_classical_opt_time: the time taken for classical optimization
        tune_time_taken = {
            "tune_total_time": tune_total_time,
            "tune_qiskit_running_time": tune_qiskit_time,
            "tune_total_machine_time": tune_total_machine_time,
            "tune_machine_running_time": tune_machine_job_time,
            "tune_minimize_time": tune_minimize_time,
            "tune_classical_opt_time": tune_minimize_time - tune_qiskit_time,
        }

        result = {
            "evals": res["nfev"],
            "eval_time": tune_minimize_time,  # Deprecated
            "tune_time_taken": tune_time_taken,
            "opt_val": res["fun"],
            "opt_params": res["x"],
            "group_list": group_list,
            "init_ones": init_ones,
            "params_history": parameter_values_history,
        }
        return result

    def measure(
        self,
        f_dict: IsingDict,
        wires: int,
        parameters: List[float],
        group_list: List[List[int]],
        init_ones: List[int],
    ) -> Tuple[Dict[str, int], Dict[str, float]]:
        # Time count for tune function
        init_meas_total_time = time.perf_counter()

        self._load_backend(wires)

        op_f = generate_hamiltonian(f_dict, wires)

        # Time count for qulacs
        init_meas_qiskit_time = time.perf_counter()
        if group_list == []:
            qc = qaoa_ansatz(op_f, wires, parameters, self.reps)
        else:
            qc = constrained_ansatz(wires, parameters, self.reps, group_list, init_ones)
        qc.measure_all()

        qc = transpile(qc, self.backend)
        init_meas_total_machine_time = datetime.datetime.now()
        job = self.backend.run(qc)
        meas_qiskit_time = time.perf_counter() - init_meas_qiskit_time
        counts = job.result().get_counts()
        result = job.result().to_dict()
        meas_total_time = time.perf_counter() - init_meas_total_time

        if hasattr(job, "time_per_step"):
            time_stamp = job.time_per_step()
            if "CREATED" in time_stamp:
                init_meas_total_machine_time = time_stamp["CREATED"]

        end_meas_total_machine_time = _get_time_from_result(result["date"])

        # The dictionary of time counts
        # measure_total_time: the total time taken by measure function
        # measure_qiskit_running_time: the total qiskit running time
        # measure_total_machine_time: the total time taken by the IBMQ machine (including waiting time)
        # measure_machine_running_time: the actual machine running time
        meas_time_taken = {
            "measure_total_time": meas_total_time,
            "measure_qiskit_running_time": meas_qiskit_time,
            "measure_total_machine_time": (
                (
                    end_meas_total_machine_time - init_meas_total_machine_time
                ).total_seconds()
            ),
            "measure_machine_running_time": result["time_taken"],
            "time_taken": result["time_taken"],  # Deprecated
        }

        return counts, meas_time_taken
