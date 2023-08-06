from __future__ import annotations

import time
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from qulacs import Observable, PauliOperator, QuantumCircuit, QuantumState
from scipy.optimize import minimize
from random import sample
from collections import Counter

from .core import AbstractQAOARunner, IsingDict


def generate_hamiltonian(
    f_dict: IsingDict,
    wires: int,
) -> Observable:
    op_f = Observable(wires)
    for key, value in f_dict.items():
        Paulistring = ""
        key = set(key)
        if len(key) > 0:
            for i in key:
                if Paulistring != "":
                    Paulistring += " "
                Paulistring += f"Z {i}"
            op_f.add_operator(PauliOperator(Paulistring, value))
    return op_f


def qaoa_ansatz(
    op_f: Observable,
    wires: int,
    parameters: List[float],
    reps: int,
) -> QuantumCircuit:
    k = 0
    circuit = QuantumCircuit(wires)
    op_mixer = Observable(wires)
    for i in range(wires):
        Paulistring = f"X {i}"
        op_mixer.add_operator(PauliOperator(Paulistring, 1.0))
        circuit.add_H_gate(i)
    for _ in range(reps):
        circuit.add_observable_rotation_gate(op_f, parameters[k], 1)
        k += 1
        circuit.add_observable_rotation_gate(op_mixer, parameters[k], 1)
        k += 1

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
        circuit.add_X_gate(i)
    for i in not_grouped:
        op_x = Observable(wires)
        Paulistring_x = f"X {i}"
        op_x.add_operator(PauliOperator(Paulistring_x, 1.0))
        circuit.add_observable_rotation_gate(op_x, parameters[k], 1)
        k += 1
    for _ in range(reps):
        for group in group_list:
            m = len(group)
            for i in range(m // 2):
                a = 2 * i
                b = 2 * i + 1
                circuit.add_CNOT_gate(group[a], group[b])
                circuit.add_RY_gate(group[a], parameters[k])
                circuit.add_CNOT_gate(group[b], group[a])
                circuit.add_RY_gate(group[a], -parameters[k])
                circuit.add_CNOT_gate(group[a], group[b])
                k += 1
            for i in range((m - 1) // 2):
                a = 2 * i + 1
                b = 2 * i + 2
                circuit.add_CNOT_gate(group[a], group[b])
                circuit.add_RY_gate(group[a], parameters[k])
                circuit.add_CNOT_gate(group[b], group[a])
                circuit.add_RY_gate(group[a], -parameters[k])
                circuit.add_CNOT_gate(group[a], group[b])
                k += 1

    return circuit


class QulacsRunner(AbstractQAOARunner):
    def __init__(
        self,
        reps: int = 10,
        shots: Optional[int] = None,
    ) -> None:
        super().__init__(reps, shots)

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

        # Prepare Hamiltonian
        op_f = generate_hamiltonian(f_dict, wires)

        # Create init_one list
        if group_list != [] and init_ones == []:
            for group in group_list:
                init_ones += sample(group, 1)

        # Prepare parameters
        if initial_parameters is None:
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
            initial_parameters = np.random.rand(k)

        # Define cost function
        parameter_values_history = list()

        # Time count for qulacs
        tune_qulacs_time = 0.0

        def cost_function(params_val):
            parameter_values_history.append(params_val)

            # Time count for cost function
            init_time_cf = time.perf_counter()

            if group_list == []:
                circuit = qaoa_ansatz(
                    op_f,
                    wires,
                    params_val,
                    self.reps,
                )
            else:
                circuit = constrained_ansatz(
                    wires,
                    params_val,
                    self.reps,
                    group_list,
                    init_ones,
                )
            state = QuantumState(wires)
            circuit.update_quantum_state(state)

            nonlocal tune_qulacs_time
            tune_qulacs_time += time.perf_counter() - init_time_cf
            return op_f.get_expectation_value(state)

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
        # tune_qulacs_running_time: the total qulacs running time
        # tune_minimize_time: the time taken by the scipy minimize function
        # tune_classical_opt_time: the time taken for classical optimization
        tune_time_taken = {
            "tune_total_time": tune_total_time,
            "tune_qulacs_running_time": tune_qulacs_time,
            "tune_minimize_time": tune_minimize_time,
            "tune_classical_opt_time": tune_minimize_time - tune_qulacs_time,
        }

        # Form result
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
        # Time count for measure function
        init_meas_total_time = time.perf_counter()

        op_f = generate_hamiltonian(f_dict, wires)

        # Time count for qiskit
        init_meas_qulacs_time = time.perf_counter()
        if group_list == []:
            circuit = qaoa_ansatz(
                op_f,
                wires,
                parameters,
                self.reps,
            )
        else:
            circuit = constrained_ansatz(
                wires,
                parameters,
                self.reps,
                group_list,
                init_ones,
            )
        state = QuantumState(wires)
        circuit.update_quantum_state(state)
        samples = Counter(
            state.sampling(self.shots if self.shots is not None else 1024)
        )
        meas_qulacs_time = time.perf_counter() - init_meas_qulacs_time
        z_basis = [format(i, "b").zfill(wires) for i in range(2**wires)]
        counts = {z_basis[i]: samples[i] for i in range(2**wires) if i in samples}
        meas_total_time = time.perf_counter() - init_meas_total_time

        # The dictionary of time counts
        # measure_total_time: the total time taken by measure function
        # measure_qiskit_running_time: the total qulacs running time
        meas_time_taken = {
            "measure_total_time": meas_total_time,
            "measure_qulacs_running_time": meas_qulacs_time,
            "time_taken": meas_total_time,  # Deprecated
        }

        return counts, meas_time_taken
