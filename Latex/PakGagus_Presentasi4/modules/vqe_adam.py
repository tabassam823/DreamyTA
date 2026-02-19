
import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
import os

def run_vqe_adam(H, n_qubits, K=2, depth=2, maxiter=100, stepsize=0.1, seed=42):
    """Run VQE using Adam optimizer."""
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def cost_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        return qml.expval(H)
    
    # Use standard numpy for random gen, then convert to PennyLane tensor
    rng = np.random.default_rng(seed)
    n_params = n_qubits * 2 * (depth + 1)
    params_init = rng.uniform(0, 2 * np.pi, n_params)
    params = np.array(params_init, requires_grad=True)
    
    # Adam Optimization
    opt = qml.AdamOptimizer(stepsize=stepsize)
    cost_history = []
    
    print(f"Starting Adam Optimization (maxiter={maxiter}, stepsize={stepsize})...")
    
    for i in range(maxiter):
        params, cost = opt.step_and_cost(cost_circuit, params)
        cost_history.append(float(cost))
        
        if (i + 1) % 10 == 0:
            print(f"Iter {i+1}: Cost = {cost:.6f}")
            
    return params, cost_history

def generate_vqe_visualization(cost_history, output_dir="generated_images"):
    """Generates VQE convergence plot."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.figure(figsize=(8, 5))
    plt.plot(cost_history, marker='o', markersize=2, linestyle='-', linewidth=1, color='green')
    plt.title("VQE Optimization Convergence (Adam)")
    plt.xlabel("Iteration")
    plt.ylabel("Cost Value (Energy)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/vqe_convergence_adam.png")
    plt.close()
    print(f"VQE convergence plot saved to {output_dir}")

# Reusing the sample helper logic from previous module (or redefining it here for completeness)
def sample_results(params, n_qubits, depth=2, K=2):
    """Sample from the optimized circuit to find best bitstring."""
    dev_sample = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev_sample)
    def sample_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        return qml.probs(wires=range(n_qubits))
    
    probs = sample_circuit(params)
    
    # Find best bitstring with Hamming weight K
    best_bitstring = None
    best_prob = -1.0
    
    # Check all bitstrings
    for i, p in enumerate(probs):
        bitstring = format(i, f'0{n_qubits}b')
        if bitstring.count('1') == K:
            if p > best_prob:
                best_prob = p
                best_bitstring = bitstring
                
    # Fallback
    if best_bitstring is None:
        sorted_indices = np.argsort(probs)[::-1]
        for idx in sorted_indices:
             bs = format(idx, f'0{n_qubits}b')
             if bs.count('1') == K:
                 best_bitstring = bs
                 break
        if best_bitstring is None:
             best_bitstring = "1" * K + "0" * (n_qubits - K)
             
    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices, best_bitstring, probs

def generate_probs_visualization(probs, n_qubits, best_bitstring, output_dir="generated_images", K=2):
    """Generates probability distribution bar chart filtered for Hamming weight K."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Filter for bitstrings with Hamming weight K
    valid_indices = []
    valid_probs = []
    valid_labels = []
    
    for i, p in enumerate(probs):
        bs = format(i, f'0{n_qubits}b')
        if bs.count('1') == K:
            valid_indices.append(i)
            valid_probs.append(p)
            valid_labels.append(bs)
            
    # Sort by probability
    sorted_pairs = sorted(zip(valid_probs, valid_labels), key=lambda x: x[0], reverse=True)
    if not sorted_pairs:
        print("No valid bitstrings found to plot.")
        return
        
    top_probs = [p for p, l in sorted_pairs]
    top_labels = [l for p, l in sorted_pairs]
    
    colors = ['green' if l == best_bitstring else 'lightgreen' for l in top_labels]
    
    plt.figure(figsize=(8, 5))
    plt.bar(top_labels, top_probs, color=colors)
    plt.title(f"Probabilities for K={K} Asset Combinations (Adam)\nSelected: {best_bitstring}")
    plt.xlabel("Bitstrings (Assets)")
    plt.ylabel("Probability")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/vqe_probs_adam.png")
    plt.close()
