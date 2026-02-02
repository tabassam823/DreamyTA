"""
Hardware-Efficient Ansatz for VQE
Based on Kandala et al., Nature 549, 242-246 (2017)

Implements the interleaved structure from Figure 1c:
- Rotation layers: RZ(α) → RX(β) → RZ(γ) (Euler decomposition)
- Entanglement layers: CNOT gates with configurable topology
"""

import pennylane as qml
from pennylane import numpy as np


def rotation_layer(params, wires, layer_idx):
    """
    Single-qubit rotation layer using Euler angles (Z-X-Z decomposition).
    
    Args:
        params: Array of shape (n_qubits, 3) containing [α, β, γ] for each qubit
        wires: List of qubit indices
        layer_idx: Current layer index (used for parameter offset)
    """
    n_qubits = len(wires)
    
    for i, wire in enumerate(wires):
        # RZ(α) → RX(β) → RZ(γ)
        qml.RZ(params[i, 0], wires=wire)
        qml.RX(params[i, 1], wires=wire)
        qml.RZ(params[i, 2], wires=wire)


def entangler_layer(wires, topology='linear'):
    """
    Two-qubit entanglement layer using CNOT gates.
    
    Args:
        wires: List of qubit indices
        topology: 'linear' (chain) or 'star' (central qubit)
    
    Linear: 0-1, 1-2, 2-3, ...
    Star: 0-1, 0-2, 0-3, ... (qubit 0 as center)
    """
    n_qubits = len(wires)
    
    if topology == 'linear':
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[wires[i], wires[i + 1]])
    elif topology == 'star':
        for i in range(1, n_qubits):
            qml.CNOT(wires=[wires[0], wires[i]])
    else:
        raise ValueError(f"Unknown topology: {topology}. Use 'linear' or 'star'.")


def hardware_efficient_ansatz(weights, wires, depth, topology='linear'):
    """
    Full Hardware-Efficient Ansatz with interleaved rotation and entanglement layers.
    
    Structure for depth d:
        [Rot_0] - [Ent] - [Rot_1] - [Ent] - ... - [Rot_d]
        
    Total layers: d entanglement layers + (d+1) rotation layers
    
    Args:
        weights: Array of shape ((depth+1), n_qubits, 3) for all rotation parameters
        wires: List of qubit indices
        depth: Number of entanglement layers (d in paper)
        topology: CNOT topology ('linear' or 'star')
    """
    n_qubits = len(wires)
    
    # Initial rotation layer
    rotation_layer(weights[0], wires, layer_idx=0)
    
    # Interleaved entanglement + rotation
    for d in range(depth):
        entangler_layer(wires, topology)
        rotation_layer(weights[d + 1], wires, layer_idx=d + 1)


def get_param_count(n_qubits, depth):
    """
    Calculate total number of variational parameters.
    
    Formula: p = n_qubits × 3 × (depth + 1)
    
    Note: Paper mentions p = N(3d + 2) when first Z rotation is locked,
    but we implement the full form for flexibility.
    
    Args:
        n_qubits: Number of qubits
        depth: Circuit depth (number of entanglement layers)
        
    Returns:
        Total parameter count
    """
    return n_qubits * 3 * (depth + 1)


def create_ansatz_circuit(n_qubits, depth, topology='linear'):
    """
    Create a PennyLane QNode-compatible ansatz function.
    
    Args:
        n_qubits: Number of qubits
        depth: Circuit depth
        topology: CNOT topology
        
    Returns:
        A function that takes weights and applies the ansatz
    """
    wires = list(range(n_qubits))
    
    def ansatz(weights):
        # Reshape flat weights to (depth+1, n_qubits, 3)
        n_params_per_layer = n_qubits * 3
        weights_reshaped = weights.reshape((depth + 1, n_qubits, 3))
        hardware_efficient_ansatz(weights_reshaped, wires, depth, topology)
    
    return ansatz


# ============================================================
# Testing / Demonstration
# ============================================================
if __name__ == "__main__":
    # Test configuration
    n_qubits = 2
    depth = 1
    
    print(f"Hardware-Efficient Ansatz Test")
    print(f"=" * 50)
    print(f"Number of qubits: {n_qubits}")
    print(f"Depth: {depth}")
    print(f"Total parameters: {get_param_count(n_qubits, depth)}")
    
    # Create a test device and circuit
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def circuit(weights):
        weights_reshaped = weights.reshape((depth + 1, n_qubits, 3))
        hardware_efficient_ansatz(weights_reshaped, list(range(n_qubits)), depth, 'linear')
        return qml.state()
    
    # Random parameters
    np.random.seed(42)
    params = np.random.uniform(0, 2 * np.pi, get_param_count(n_qubits, depth))
    
    # Run circuit
    state = circuit(params)
    print(f"\nOutput state (first 4 amplitudes): {state[:4]}")
    
    # Draw circuit
    print("\nCircuit diagram:")
    print(qml.draw(circuit)(params))
