
import pennylane as qml
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import Callable, Optional, Tuple, List

class SPSA:
    """
    SPSA Optimizer for VQE.
    Based on the reference implementation provided by the user.
    """
    
    def __init__(
        self,
        maxiter: int = 100,
        a: float = 0.1,
        c: float = 0.1,
        A: float = 10.0,
        alpha: float = 0.602,
        gamma: float = 0.101,
        seed: Optional[int] = None
    ):
        self.maxiter = maxiter
        self.a = a
        self.c = c
        self.A = A
        self.alpha = alpha
        self.gamma = gamma
        
        self.rng = np.random.default_rng(seed)
        
        # Tracking
        self.history = []
        self.nfev = 0
    
    def _get_gains(self, k: int) -> Tuple[float, float]:
        """Calculate gain sequences at iteration k."""
        a_k = self.a / (self.A + k + 1) ** self.alpha
        c_k = self.c / (k + 1) ** self.gamma
        return a_k, c_k
    
    def _get_perturbation(self, p: int) -> np.ndarray:
        """Generate random ±1 perturbation vector."""
        return 2 * self.rng.integers(0, 2, size=p) - 1
    
    def step(
        self,
        cost_fn: Callable[[np.ndarray], float],
        params: np.ndarray,
        k: int
    ) -> Tuple[np.ndarray, float, float]:
        p = len(params)
        a_k, c_k = self._get_gains(k)
        
        delta = self._get_perturbation(p)
        
        # Evaluate at perturbed points
        params_plus = params + c_k * delta
        params_minus = params - c_k * delta
        
        f_plus = cost_fn(params_plus)
        f_minus = cost_fn(params_minus)
        self.nfev += 2
        
        grad_approx = (f_plus - f_minus) / (2 * c_k * delta)
        
        new_params = params - a_k * grad_approx
        
        # Track smoothed cost (average of probes)
        cost_mid = (f_plus + f_minus) / 2
        
        return new_params, np.linalg.norm(grad_approx), cost_mid
    
    def optimize(
        self,
        cost_fn: Callable[[np.ndarray], float],
        initial_params: np.ndarray
    ) -> Tuple[np.ndarray, float, List[float]]:
        params = initial_params.copy()
        self.history = []
        self.nfev = 0
        
        best_params = params.copy()
        best_cost = float('inf')
        
        for k in range(self.maxiter):
            params, grad_norm, cost = self.step(cost_fn, params, k)
            
            self.history.append(cost)
            
            if cost < best_cost:
                best_cost = cost
                best_params = params.copy()
                
        return best_params, best_cost, self.history

def run_vqe_spsa(H, n_qubits, K=2, depth=2, maxiter=100, seed=42):
    """Run VQE using the SPSA class."""
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
    
    # Initialize parameters
    rng = np.random.default_rng(seed)
    n_params = n_qubits * 2 * (depth + 1)
    initial_params = rng.uniform(0, 2 * np.pi, n_params)
    
    # Evaluate initial cost to calibrate 'a'
    initial_cost = float(cost_circuit(initial_params))
    
    # Heuristic for 'a' from reference
    a_calibration = 0.1 * max(1.0, abs(initial_cost))
    
    # Create Optimizer instance
    optimizer = SPSA(
        maxiter=maxiter,
        a=a_calibration, # Using calibrated a
        c=0.1,           # Standard c
        A=maxiter * 0.1, # Standard stability constant
        seed=seed
    )
    
    print(f"SPSA Initialized via Class: a={optimizer.a:.4f}, c={optimizer.c}, A={optimizer.A}")
    
    # Wrapper for cost function to ensure we pass numpy arrays and return floats
    def cost_fn(p):
        return float(cost_circuit(p))
    
    params, final_cost, cost_history = optimizer.optimize(cost_fn, initial_params)
    
    # Ensure cost_history includes initial cost at the start for plot
    cost_history.insert(0, initial_cost)
    
    return params, cost_history

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
             # Force a default if STILL none (unlikely if n_qubits >= K)
             best_bitstring = "1" * K + "0" * (n_qubits - K)
             
    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices, best_bitstring, probs

def generate_vqe_visualization(cost_history, output_dir="generated_images"):
    """Generates VQE convergence plot."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.figure(figsize=(8, 5))
    plt.plot(cost_history, marker='o', markersize=2, linestyle='-', linewidth=1)
    plt.title("VQE Optimization Convergence (SPSA)")
    plt.xlabel("Iteration")
    plt.ylabel("Cost Value (Energy)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/vqe_convergence.png")
    plt.close()
    print(f"VQE convergence plot saved to {output_dir}")

def generate_probs_visualization(probs, n_qubits, best_bitstring, output_dir="generated_images"):
    """Generates probability distribution bar chart."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Top 10 states
    indices = np.argsort(probs)[::-1][:10]
    top_probs = probs[indices]
    top_labels = [format(i, f'0{n_qubits}b') for i in indices]
    
    colors = ['red' if l == best_bitstring else 'skyblue' for l in top_labels]
    
    plt.figure(figsize=(8, 5))
    plt.bar(top_labels, top_probs, color=colors)
    plt.title(f"Top 10 Bitstring Probabilities\nSelected: {best_bitstring}")
    plt.xlabel("Bitstrings")
    plt.ylabel("Probability")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/vqe_probs.png")
    plt.close()
