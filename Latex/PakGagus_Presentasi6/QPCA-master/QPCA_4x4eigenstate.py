from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import numpy as np
import math
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_state_city, plot_bloch_multivector, plot_state_hinton
import matplotlib.pyplot as plt

q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

# initial state
val_total = 3087 + 906 + 1405 + 58
state_vector = [
    math.sqrt(3087 / val_total),
    math.sqrt(906 / val_total),
    math.sqrt(1405 / val_total),
    math.sqrt(58 / val_total)
]
qc.initialize(state_vector, [q[1], q[2]])
qc.h(q[0])

# operations
qc.p(0.785398, q[1])
qc.cu(1.1747, -2.83038, 3.83087, 0, q[1], q[2])
qc.cx(q[0], q[1])
qc.p(-0.785398, q[1])
qc.cu(1.1747, -0.689273, -0.31121, 0, q[1], q[2])
qc.p(-1.5708, q[0])
qc.cu(2.07033, 3.76782, -0.626228, 0, q[0], q[1])
qc.p(0.785398, q[0])
qc.cu(1.1747, -2.83038, 3.83087, 0, q[0], q[2])
qc.cx(q[2], q[0])
qc.cu(1.07126, 0.626228, 0.626228, 0, q[0], q[1])
qc.cx(q[2], q[0])
qc.cu(1.07126, -3.76782, 2.51536, 0, q[2], q[1])
qc.cu(2.3749, -0.251338, -1.38469, 0, q[1], q[2])
qc.cx(q[0], q[1])
qc.cu(2.3749, -1.7569, 3.39293, 0, q[1], q[2])
qc.p(1/4 * np.pi, q[0])
qc.cu(1/2 * np.pi, -1/2 * np.pi, 1/2 * np.pi, 0, q[0], q[1])
qc.cu(2.3749, -0.251338, -1.38469, 0, q[1], q[2])
qc.cx(q[2], q[0])
qc.p(1/4 * np.pi, q[0])
qc.cu(1/2 * np.pi, -1/2 * np.pi, 1/2 * np.pi, 0, q[0], q[1])
qc.cx(q[2], q[0])
qc.p(-1/4 * np.pi, q[2])
qc.cu(1/2 * np.pi, 1/2 * np.pi, -1/2 * np.pi, 0, q[2], q[1])

qc.h(q[0])

# --- STATEVECTOR ---
backend_state = Aer.get_backend('statevector_simulator')
qc_state = transpile(qc, backend_state)
outputstate = backend_state.run(qc_state).result().get_statevector(qc_state, decimals=3)

plot_state_city(outputstate).savefig("state_city_4x4.png")
plot_bloch_multivector(outputstate).savefig("bloch_4x4.png")
plot_state_hinton(outputstate).savefig("hinton_4x4.png")

# --- MEASUREMENT ---
qc.barrier()
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

# 1. Original
qc.draw(output='mpl').savefig("circuit_4x4.png")

# 2. Transpiled (Hardware level)
qc_resynthesized = transpile(qc, basis_gates=['id', 'rz', 'sx', 'x', 'cx'], optimization_level=1)
qc_resynthesized.draw(output='mpl').savefig("circuit_transpiled_4x4.png")
print("Sirkuit Transpiled 4x4 telah disimpan.")

# --- COUNTS ---
backend_qasm = Aer.get_backend('qasm_simulator')
qc_qasm = transpile(qc, backend_qasm)
counts = backend_qasm.run(qc_qasm, shots=8192).result().get_counts()
plot_histogram(counts)
plt.savefig("qpca_4x4_result.png")
