import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

# --- Configuration from Notebook ---
N = 5 # Number of assets/qubits
n_layers = 3 # Circuit depth

# --- Device & Circuit Definition ---
dev = qml.device("default.qubit", wires=N)

# The ansatz used in the notebook (Cell 9)
def ansatz(params, wires):
    qml.BasicEntanglerLayers(weights=params, wires=wires)

# Create a QNode just for drawing
@qml.qnode(dev)
def circuit_node(params):
    ansatz(params, wires=range(N))
    return qml.probs(wires=range(N))

# --- Parameters ---
# Shape from BasicEntanglerLayers.shape(n_layers=3, n_wires=5)
# It expects a shape of (n_layers, n_wires)
shape = (n_layers, N)
np.random.seed(0) # For reproducibility
params = np.random.random(shape)

# --- Visualization ---

print("\n--- Circuit Text Diagram ---\n")
print(qml.draw(circuit_node, level="device")(params))
print("\n----------------------------\n")

# Try to save graphical representation
try:
    fig, ax = qml.draw_mpl(circuit_node)(params)
    plt.title(f"VQE Ansatz: BasicEntanglerLayers\n(Wires={N}, Layers={n_layers})")
    plt.savefig("circuit_visualization.png")
    print("Circuit image saved to 'circuit_visualization.png'")
except Exception as e:
    print(f"Could not save image (matplotlib/drawer issue): {e}")
