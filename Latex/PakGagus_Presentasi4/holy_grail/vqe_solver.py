import pennylane as qml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_vqe_spsa_pennylane(H, n_qubits, K=2, depth=1, maxiter=100, seed=42, export_convergence=False):
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def cost_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits - 1):
                    qml.CNOT(wires=[q, q + 1])
                qml.CNOT(wires=[n_qubits - 1, 0])
        return qml.expval(H)

    rng = np.random.default_rng(seed)
    n_params = n_qubits * 2 * (depth + 1)
    params = rng.uniform(0, 2 * np.pi, n_params)
    
    a = 0.1 
    c = 0.1
    A = maxiter * 0.1
    alpha = 0.602
    gamma = 0.101
    
    cost_history = []
    theta_history = []
    
    for k in range(maxiter):
        a_k = a / (A + k + 1) ** alpha
        c_k = c / (k + 1) ** gamma
        delta = 2 * rng.integers(0, 2, size=n_params) - 1
        
        cost_plus = float(cost_circuit(params + c_k * delta))
        cost_minus = float(cost_circuit(params - c_k * delta))
        grad = (cost_plus - cost_minus) / (2 * c_k * delta)
        params = params - a_k * grad
        
        if export_convergence:
            cost_history.append(cost_plus)
            theta_history.append(params.copy())

    if export_convergence:
        pd.DataFrame({'Iteration': range(1, maxiter + 1), 'Cost': cost_history}).to_csv('vqe_cost_first_decision.csv', index=False)
        
        theta_records = []
        for i, th in enumerate(theta_history):
            record = {'Iteration': i + 1}
            for j, val in enumerate(th):
                record[f'Theta_{j}'] = val
            theta_records.append(record)
        pd.DataFrame(theta_records).to_csv('vqe_theta_first_decision.csv', index=False)
        
        # Output Circuit Diagram
        fig, ax = qml.draw_mpl(cost_circuit)(params)
        fig.savefig("vqe_ansatz_circuit.png")
        plt.close(fig)

    @qml.qnode(dev)
    def prob_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits - 1):
                    qml.CNOT(wires=[q, q + 1])
                qml.CNOT(wires=[n_qubits - 1, 0])
        return qml.probs(wires=range(n_qubits))

    probs = prob_circuit(params)
    
    if export_convergence:
        prob_data = []
        for idx, prob in enumerate(probs):
            bs = format(idx, f'0{n_qubits}b')
            prob_data.append({'Bitstring': bs, 'Probability': float(prob)})
        pd.DataFrame(prob_data).to_csv('vqe_probs_first_decision.csv', index=False)
    
    sorted_indices = np.argsort(probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break
            
    if export_convergence:
        # Export final state vector
        @qml.qnode(dev)
        def state_circuit(params):
            weights = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(weights[layer, q, 0], wires=q)
                    qml.RZ(weights[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])
            return qml.state()

        final_state = state_circuit(params)
        state_records = []
        for idx, amp in enumerate(final_state):
            bs = format(idx, f'0{n_qubits}b')
            state_records.append({
                'Index': idx, 'State': bs,
                'Real': float(np.real(amp)), 'Imaginary': float(np.imag(amp)),
                'Probability': float(np.abs(amp)**2)
            })
        pd.DataFrame(state_records).to_csv('vqe_final_state.csv', index=False)

        # Export step-by-step circuit evolution
        evolution_records = []
        step_idx = 0
        
        def record_state(name, param_slice=None):
            nonlocal step_idx
            @qml.qnode(dev)
            def partial_circuit():
                if name == "Init":
                    pass # Just initial |00...0> state
                else:
                    weights = params.reshape((depth + 1, n_qubits, 2))
                    # Reconstruct circuit up to current step
                    for layer in range(depth + 1):
                        if name == f"Layer_{layer}_Rotations" and layer == param_slice:
                            for q in range(n_qubits):
                                qml.RY(weights[layer, q, 0], wires=q)
                                qml.RZ(weights[layer, q, 1], wires=q)
                            break # Stop after this layer's rotations
                        elif name == f"Layer_{layer}_Entanglement" and layer == param_slice:
                            for q in range(n_qubits):
                                qml.RY(weights[layer, q, 0], wires=q)
                                qml.RZ(weights[layer, q, 1], wires=q)
                            if layer < depth:
                                for q in range(n_qubits - 1):
                                    qml.CNOT(wires=[q, q + 1])
                                qml.CNOT(wires=[n_qubits - 1, 0])
                            break # Stop after this layer's entanglement
                        else:
                            # Apply full completed layer
                            for q in range(n_qubits):
                                qml.RY(weights[layer, q, 0], wires=q)
                                qml.RZ(weights[layer, q, 1], wires=q)
                            if layer < depth:
                                for q in range(n_qubits - 1):
                                    qml.CNOT(wires=[q, q + 1])
                                qml.CNOT(wires=[n_qubits - 1, 0])
                return qml.state()
            
            st = partial_circuit()
            for idx, amp in enumerate(st):
                bs = format(idx, f'0{n_qubits}b')
                evolution_records.append({
                    'Step_Order': step_idx, 'Step_Name': name,
                    'Basis_State': bs, 'Real': float(np.real(amp)),
                    'Imaginary': float(np.imag(amp)), 'Probability': float(np.abs(amp)**2)
                })
            step_idx += 1

        record_state("Init")
        for layer in range(depth + 1):
            record_state(f"Layer_{layer}_Rotations", layer)
            if layer < depth:
                record_state(f"Layer_{layer}_Entanglement", layer)
                
        pd.DataFrame(evolution_records).to_csv('vqe_circuit_evolution.csv', index=False)
            
    if best_bitstring is None:
        best_bitstring = "0011" 
        
    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices
