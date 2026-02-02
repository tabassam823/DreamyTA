"""
VQE Runner for Hardware-Efficient VQE
Based on Kandala et al., Nature 549, 242-246 (2017)

Implements the full VQE loop:
1. Prepare state with parameterized ansatz
2. Measure energy expectation value
3. Update parameters with classical optimizer
"""

import pennylane as qml
from pennylane import numpy as np
from typing import Callable, Tuple, Optional, Dict, Any
import time

from he_ansatz import hardware_efficient_ansatz, get_param_count
from spsa_optimizer import SPSA


def create_vqe_cost_function(
    hamiltonian,
    n_qubits: int,
    depth: int,
    topology: str = 'linear',
    shots: Optional[int] = 1000
) -> Tuple[Callable, qml.QNode]:
    """
    Create VQE cost function for given Hamiltonian.
    
    Args:
        hamiltonian: PennyLane Hamiltonian
        n_qubits: Number of qubits
        depth: Ansatz depth
        topology: CNOT topology
        shots: Number of measurement shots (None for exact)
        
    Returns:
        cost_fn: Function that takes params and returns energy
        circuit: The underlying QNode
    """
    # Create device
    if shots is not None:
        dev = qml.device("default.qubit", wires=n_qubits, shots=shots)
    else:
        dev = qml.device("default.qubit", wires=n_qubits)
    
    wires = list(range(n_qubits))
    
    @qml.qnode(dev)
    def circuit(weights):
        # Reshape weights to (depth+1, n_qubits, 3)
        weights_reshaped = weights.reshape((depth + 1, n_qubits, 3))
        hardware_efficient_ansatz(weights_reshaped, wires, depth, topology)
        return qml.expval(hamiltonian)
    
    def cost_fn(params):
        return float(circuit(params))
    
    return cost_fn, circuit


def run_vqe(
    hamiltonian,
    n_qubits: int,
    depth: int = 1,
    topology: str = 'linear',
    shots: Optional[int] = 1000,
    maxiter: int = 100,
    seed: Optional[int] = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Run full VQE optimization.
    
    Args:
        hamiltonian: PennyLane Hamiltonian
        n_qubits: Number of qubits
        depth: Ansatz depth (d in paper)
        topology: CNOT topology ('linear' or 'star')
        shots: Measurement shots (None for exact expectation)
        maxiter: Maximum SPSA iterations
        seed: Random seed
        verbose: Print progress
        
    Returns:
        Dictionary with:
            - optimal_params: Best parameters found
            - optimal_energy: Minimum energy achieved
            - history: Energy at each iteration
            - nfev: Total function evaluations
            - time: Total runtime in seconds
    """
    rng = np.random.default_rng(seed)
    
    # Create cost function
    cost_fn, circuit = create_vqe_cost_function(
        hamiltonian, n_qubits, depth, topology, shots
    )
    
    # Initialize parameters
    n_params = get_param_count(n_qubits, depth)
    initial_params = rng.uniform(0, 2 * np.pi, n_params)
    
    if verbose:
        print(f"VQE Configuration:")
        print(f"  Qubits: {n_qubits}")
        print(f"  Depth: {depth}")
        print(f"  Parameters: {n_params}")
        print(f"  Shots: {shots if shots else 'Exact'}")
        print(f"  Max iterations: {maxiter}")
    
    # Create optimizer
    optimizer = SPSA(
        maxiter=maxiter,
        a=0.1,
        c=0.1,
        A=maxiter * 0.1,
        seed=seed
    )
    
    # Run optimization
    start_time = time.time()
    
    def callback(k, params, cost):
        if verbose and k % 20 == 0:
            print(f"  Iter {k:4d}: Energy = {cost:.6f}")
    
    optimal_params, optimal_energy, history = optimizer.optimize(
        cost_fn, initial_params, callback=callback
    )
    
    elapsed_time = time.time() - start_time
    
    if verbose:
        print(f"\nOptimization complete:")
        print(f"  Best energy: {optimal_energy:.6f} Ha")
        print(f"  Function evaluations: {optimizer.nfev}")
        print(f"  Time: {elapsed_time:.2f} s")
    
    return {
        'optimal_params': optimal_params,
        'optimal_energy': optimal_energy,
        'history': history,
        'nfev': optimizer.nfev,
        'time': elapsed_time,
        'circuit': circuit
    }


def run_vqe_scan(
    get_hamiltonian_fn: Callable,
    bond_distances: np.ndarray,
    n_qubits: int,
    depth: int = 1,
    topology: str = 'linear',
    shots: Optional[int] = 1000,
    maxiter: int = 100,
    seed: Optional[int] = None,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Run VQE for multiple bond distances (dissociation curve).
    
    Args:
        get_hamiltonian_fn: Function(bond_length) -> Hamiltonian
        bond_distances: Array of bond lengths
        n_qubits: Number of qubits
        depth: Ansatz depth
        topology: CNOT topology
        shots: Measurement shots
        maxiter: SPSA iterations per point
        seed: Random seed
        verbose: Print progress
        
    Returns:
        Dictionary with:
            - bond_distances: Input bond lengths
            - vqe_energies: VQE energy at each point
            - exact_energies: Exact energy (if available)
            - all_results: Full results for each point
    """
    vqe_energies = []
    exact_energies = []
    all_results = []
    
    for i, r in enumerate(bond_distances):
        if verbose:
            print(f"\n{'='*60}")
            print(f"Bond distance: {r:.3f} Å ({i+1}/{len(bond_distances)})")
            print(f"{'='*60}")
        
        # Get Hamiltonian for this bond length
        H, q = get_hamiltonian_fn(r)
        
        # Run VQE
        result = run_vqe(
            H, q, depth, topology, shots, maxiter,
            seed=seed, verbose=verbose
        )
        
        vqe_energies.append(result['optimal_energy'])
        all_results.append(result)
        
        # Calculate exact energy for comparison
        try:
            H_matrix = qml.matrix(H)
            exact_E = np.real(np.linalg.eigvalsh(H_matrix)[0])
            exact_energies.append(exact_E)
        except Exception:
            exact_energies.append(None)
    
    return {
        'bond_distances': bond_distances,
        'vqe_energies': np.array(vqe_energies),
        'exact_energies': np.array([e for e in exact_energies if e is not None]),
        'all_results': all_results
    }


# ============================================================
# Testing / Demonstration
# ============================================================
if __name__ == "__main__":
    from molecular_hamiltonians import get_h2_hamiltonian, get_exact_energy
    
    print("VQE Runner Test")
    print("=" * 60)
    
    # Use auto-generated H2 Hamiltonian (4 qubits, parity mapping)
    H, n_qubits = get_h2_hamiltonian(bond_length=0.74)
    
    # Exact reference
    E_exact = get_exact_energy(H)
    print(f"\nExact ground state energy: {E_exact:.6f} Ha")
    
    # Run VQE with more iterations
    result = run_vqe(
        H,
        n_qubits=n_qubits,
        depth=1,
        shots=None,  # Exact expectation for testing
        maxiter=200,  # More iterations for better convergence
        seed=42,
        verbose=True
    )
    
    # Compare
    error = abs(result['optimal_energy'] - E_exact)
    error_mha = error * 1000  # Convert to mHa
    
    print(f"\nComparison:")
    print(f"  VQE energy:   {result['optimal_energy']:.6f} Ha")
    print(f"  Exact energy: {E_exact:.6f} Ha")
    print(f"  Error: {error_mha:.4f} mHa")
    print(f"  Chemical accuracy (< 1.6 mHa): {'✓ YES' if error_mha < 1.6 else '✗ NO'}")
