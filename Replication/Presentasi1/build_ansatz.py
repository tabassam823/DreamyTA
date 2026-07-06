from qiskit.circuit.library import TwoLocal

def get_ansatz(num_qubits=12):
    """
    Constructs the Two-Local Ansatz as described in the paper.
    
    Specifications:
    - Rotation Layer: Ry followed by Rz gates.
    - Entanglement Layer: CNOT (cx) gates with linear connectivity.
    - Repetitions: 3 layers.
    - Visuals: Barriers inserted for clarity.
    
    Args:
        num_qubits (int): Number of qubits (assets). Default is 12.
        
    Returns:
        TwoLocal: The constructed variational circuit.
    """
    # Define the rotation blocks
    rotation_blocks = ['ry', 'rz']
    
    # Define the entanglement blocks
    entanglement_blocks = 'cx'
    
    # Define the entanglement strategy (linear: 0-1, 1-2, ...)
    entanglement = 'linear'
    
    # Define the number of repetitions (layers)
    reps = 3
    
    # Construct the TwoLocal circuit
    ansatz = TwoLocal(
        num_qubits=num_qubits,
        rotation_blocks=rotation_blocks,
        entanglement_blocks=entanglement_blocks,
        entanglement=entanglement,
        reps=reps,
        insert_barriers=True,
        parameter_prefix='theta'
    )
    
    return ansatz

if __name__ == "__main__":
    # Parameters
    N = 12
    
    print(f"Constructing Two-Local Ansatz for {N} qubits...")
    ansatz = get_ansatz(num_qubits=N)
    
    # Decompose to see elementary gates
    decomposed_ansatz = ansatz.decompose()
    
    print("\nAnsatz Properties:")
    print(f"Number of qubits: {decomposed_ansatz.num_qubits}")
    print(f"Number of parameters: {ansatz.num_parameters}")
    print(f"Circuit depth (decomposed): {decomposed_ansatz.depth()}")
    
    print("\nCircuit Diagram (Text):")
    print(decomposed_ansatz.draw(output='text'))
