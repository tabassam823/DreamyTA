
import pennylane as qml
from pennylane import numpy as np
import inspect

print(f"PennyLane version: {qml.__version__}")

try:
    from pennylane import qchem
    symbols = ["H", "H"]
    coordinates = np.array([[0.0, 0.0, -0.6614], [0.0, 0.0, 0.6614]])
    molecule = qchem.Molecule(symbols, coordinates)
    h, _ = qchem.molecular_hamiltonian(molecule)
    coeffs, ops = h.terms()
    h_ham = qml.Hamiltonian(qml.math.real(coeffs), ops)
    
    print(f"h_ham type: {type(h_ham)}")
    
    if hasattr(h_ham, 'compute_grouping'):
        print("compute_grouping exists.")
        sig = inspect.signature(h_ham.compute_grouping)
        print(f"Signature: {sig}")
        
    else:
        print("compute_grouping DOES NOT exist.")

except Exception as e:
    print(f"Error: {e}")
