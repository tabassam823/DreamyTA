"""
Experiments for Hardware-Efficient VQE Replication
Based on Kandala et al., Nature 549, 242-246 (2017)

Implements:
1. H2 dissociation curve (chemical accuracy test)
2. LiH dissociation curve (kink feature test)
3. Visualization and comparison with exact results
"""

import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple

from molecular_hamiltonians import (
    get_h2_hamiltonian,
    get_h2_hamiltonian_manual,
    get_lih_hamiltonian,
    get_beh2_hamiltonian,
    get_exact_energy,
    get_bond_distances
)
from vqe_runner import run_vqe, run_vqe_scan


# ============================================================
# H2 Experiments
# ============================================================

def h2_single_point_test(
    depth: int = 1,
    maxiter: int = 100,
    shots: Optional[int] = None,
    seed: int = 42
) -> Tuple[float, float, float]:
    """
    Test H2 at equilibrium bond length for chemical accuracy.
    
    Acceptance Criterion #1 from PRD:
    - Achieve chemical accuracy (error < 1.6 mHa) at equilibrium with d=1
    
    Args:
        depth: Ansatz depth
        maxiter: SPSA iterations
        shots: Measurement shots (None for exact)
        seed: Random seed
        
    Returns:
        (vqe_energy, exact_energy, error_mha)
    """
    print("=" * 60)
    print("H2 Single Point Test (Chemical Accuracy)")
    print("=" * 60)
    
    # Use 2-qubit tapered Hamiltonian for faster testing
    H = get_h2_hamiltonian_manual(bond_length=0.74)
    n_qubits = 2
    
    # Exact reference
    E_exact = get_exact_energy(H)
    print(f"Exact ground state: {E_exact:.6f} Ha")
    
    # Run VQE
    result = run_vqe(
        H,
        n_qubits=n_qubits,
        depth=depth,
        shots=shots,
        maxiter=maxiter,
        seed=seed
    )
    
    E_vqe = result['optimal_energy']
    error = abs(E_vqe - E_exact)
    error_mha = error * 1000
    
    print(f"\nResults:")
    print(f"  VQE energy: {E_vqe:.6f} Ha")
    print(f"  Error: {error_mha:.4f} mHa")
    print(f"  Chemical accuracy (< 1.6 mHa): {'✓ PASS' if error_mha < 1.6 else '✗ FAIL'}")
    
    return E_vqe, E_exact, error_mha


def h2_dissociation_curve(
    n_points: int = 15,
    depth: int = 1,
    maxiter: int = 50,
    shots: Optional[int] = None,
    seed: int = 42,
    save_plot: bool = True
) -> dict:
    """
    Generate H2 dissociation curve (energy vs bond length).
    
    Args:
        n_points: Number of bond distances
        depth: Ansatz depth
        maxiter: SPSA iterations per point
        shots: Measurement shots
        seed: Random seed
        save_plot: Save plot to file
        
    Returns:
        Dictionary with results
    """
    print("=" * 60)
    print("H2 Dissociation Curve")
    print("=" * 60)
    
    bond_distances = np.linspace(0.3, 2.5, n_points)
    vqe_energies = []
    exact_energies = []
    
    for i, r in enumerate(bond_distances):
        print(f"\n[{i+1}/{n_points}] Bond length: {r:.3f} Å")
        
        # Use manual 2-qubit Hamiltonian
        # Note: Coefficients vary with bond length; this is approximate
        H = get_h2_hamiltonian_manual(r)
        n_qubits = 2
        
        # Exact energy
        E_exact = get_exact_energy(H)
        exact_energies.append(E_exact)
        
        # VQE
        result = run_vqe(
            H, n_qubits, depth, shots=shots,
            maxiter=maxiter, seed=seed, verbose=False
        )
        vqe_energies.append(result['optimal_energy'])
        
        print(f"  VQE: {result['optimal_energy']:.6f} Ha, Exact: {E_exact:.6f} Ha")
    
    vqe_energies = np.array(vqe_energies)
    exact_energies = np.array(exact_energies)
    
    # Plot
    if save_plot:
        plt.figure(figsize=(10, 6))
        plt.plot(bond_distances, exact_energies, 'k-', label='Exact', linewidth=2)
        plt.plot(bond_distances, vqe_energies, 'ro-', label=f'HE-VQE (d={depth})', markersize=6)
        plt.xlabel('Bond Distance (Å)', fontsize=12)
        plt.ylabel('Energy (Ha)', fontsize=12)
        plt.title('H2 Dissociation Curve', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('h2_dissociation.png', dpi=150)
        print(f"\nPlot saved to 'h2_dissociation.png'")
    
    return {
        'bond_distances': bond_distances,
        'vqe_energies': vqe_energies,
        'exact_energies': exact_energies
    }


# ============================================================
# LiH Experiments  
# ============================================================

def lih_dissociation_curve(
    n_points: int = 12,
    depth: int = 1,
    maxiter: int = 50,
    shots: Optional[int] = None,
    seed: int = 42,
    save_plot: bool = True
) -> dict:
    """
    Generate LiH dissociation curve.
    
    Acceptance Criterion #2 from PRD:
    - Reproduce "kink" (bendokan) feature at ~2.5 Å with d=1
    
    The kink indicates where the limited ansatz depth fails to 
    accurately capture the wavefunction character change.
    
    Args:
        n_points: Number of bond distances
        depth: Ansatz depth  
        maxiter: SPSA iterations per point
        shots: Measurement shots
        seed: Random seed
        save_plot: Save plot to file
        
    Returns:
        Dictionary with results
    """
    print("=" * 60)
    print("LiH Dissociation Curve (Kink Feature Test)")
    print("=" * 60)
    
    bond_distances = np.linspace(1.0, 4.0, n_points)
    vqe_energies = []
    exact_energies = []
    
    for i, r in enumerate(bond_distances):
        print(f"\n[{i+1}/{n_points}] Bond length: {r:.3f} Å")
        
        try:
            H, n_qubits = get_lih_hamiltonian(r)
            
            # Exact energy
            E_exact = get_exact_energy(H)
            exact_energies.append(E_exact)
            
            # VQE
            result = run_vqe(
                H, n_qubits, depth, shots=shots,
                maxiter=maxiter, seed=seed, verbose=False
            )
            vqe_energies.append(result['optimal_energy'])
            
            print(f"  VQE: {result['optimal_energy']:.6f} Ha, Exact: {E_exact:.6f} Ha")
            
        except Exception as e:
            print(f"  Error: {e}")
            vqe_energies.append(np.nan)
            exact_energies.append(np.nan)
    
    vqe_energies = np.array(vqe_energies)
    exact_energies = np.array(exact_energies)
    
    # Plot
    if save_plot and not np.all(np.isnan(vqe_energies)):
        plt.figure(figsize=(10, 6))
        
        mask = ~np.isnan(vqe_energies)
        plt.plot(bond_distances[mask], exact_energies[mask], 'k-', 
                 label='Exact', linewidth=2)
        plt.plot(bond_distances[mask], vqe_energies[mask], 'bo-', 
                 label=f'HE-VQE (d={depth})', markersize=6)
        
        # Mark kink region
        plt.axvline(x=2.5, color='r', linestyle='--', alpha=0.5, 
                    label='Expected kink (~2.5 Å)')
        
        plt.xlabel('Bond Distance (Å)', fontsize=12)
        plt.ylabel('Energy (Ha)', fontsize=12)
        plt.title('LiH Dissociation Curve', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('lih_dissociation.png', dpi=150)
        print(f"\nPlot saved to 'lih_dissociation.png'")
    
    return {
        'bond_distances': bond_distances,
        'vqe_energies': vqe_energies,
        'exact_energies': exact_energies
    }


# ============================================================
# Visualization Utilities
# ============================================================

def plot_convergence(history, title="VQE Convergence", save_path=None):
    """Plot optimization convergence."""
    plt.figure(figsize=(8, 5))
    plt.plot(history, 'b-', linewidth=1.5)
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Energy (Ha)', fontsize=12)
    plt.title(title, fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved to '{save_path}'")
    
    return plt.gcf()


def plot_error_analysis(vqe_energies, exact_energies, bond_distances, 
                        save_path=None):
    """Plot error vs bond distance."""
    errors = np.abs(vqe_energies - exact_energies) * 1000  # mHa
    
    plt.figure(figsize=(8, 5))
    plt.bar(bond_distances, errors, width=0.1, color='steelblue', alpha=0.8)
    plt.axhline(y=1.6, color='r', linestyle='--', label='Chemical accuracy (1.6 mHa)')
    plt.xlabel('Bond Distance (Å)', fontsize=12)
    plt.ylabel('Error (mHa)', fontsize=12)
    plt.title('VQE Error Analysis', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved to '{save_path}'")
    
    return plt.gcf()


# ============================================================
# Main Entry Point
# ============================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Run HE-VQE experiments')
    parser.add_argument('--experiment', type=str, default='h2_test',
                        choices=['h2_test', 'h2_curve', 'lih_curve'],
                        help='Experiment to run')
    parser.add_argument('--depth', type=int, default=1, help='Ansatz depth')
    parser.add_argument('--maxiter', type=int, default=100, help='Max iterations')
    parser.add_argument('--seed', type=int, default=42, help='Random seed')
    
    args = parser.parse_args()
    
    if args.experiment == 'h2_test':
        h2_single_point_test(depth=args.depth, maxiter=args.maxiter, seed=args.seed)
    elif args.experiment == 'h2_curve':
        h2_dissociation_curve(depth=args.depth, maxiter=args.maxiter, seed=args.seed)
    elif args.experiment == 'lih_curve':
        lih_dissociation_curve(depth=args.depth, maxiter=args.maxiter, seed=args.seed)
