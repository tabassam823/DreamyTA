from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import numpy as np
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_state_city, plot_bloch_multivector, plot_state_hinton
import math
import cmath
import matplotlib.pyplot as plt

q = QuantumRegister(4)
c = ClassicalRegister(4)
qc = QuantumCircuit(q, c)

# initial state
phase0 = complex(math.cos(-0.1144), math.sin(-0.1144))
phase1 = complex(math.cos(0.3252 - 0.1144), math.sin(0.3252 - 0.1144))
state_vector = [math.cos(0.4996) * phase0, math.sin(0.4996) * phase1]
qc.initialize(state_vector, [q[3]])

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Controlled Unitary
qc.cu(1.59899, -1.11512, 2.02647, 0, q[2], q[3])
qc.cu(2.22862, 0.513123, 3.65472, 0, q[1], q[3])
qc.cu(0.797922, -4.53103, -1.38944, 0, q[0], q[3])

# Inverse QFT
qc.h(q[0])
qc.cp(-1/2 * np.pi, q[0], q[1])
qc.h(q[1])
qc.cp(-1/4 * np.pi, q[0], q[2])
qc.cp(-1/2 * np.pi, q[1], q[2])
qc.h(q[2])

# --- STATEVECTOR ---
backend_state = Aer.get_backend('statevector_simulator')
qc_state = transpile(qc, backend_state)
outputstate = backend_state.run(qc_state).result().get_statevector(qc_state, decimals=3)

plot_state_city(outputstate).savefig("state_city_qphe.png")
plot_bloch_multivector(outputstate).savefig("bloch_qphe.png")
plot_state_hinton(outputstate).savefig("hinton_qphe.png")

# --- MEASUREMENT ---
qc.barrier()
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])

# 1. Original
qc.draw(output='mpl').savefig("circuit_qphe.png")

# 2. Transpiled (Hardware level)
qc_resynthesized = transpile(qc, basis_gates=['id', 'rz', 'sx', 'x', 'cx'], optimization_level=1)
qc_resynthesized.draw(output='mpl').savefig("circuit_transpiled_qphe.png")
print("Sirkuit Transpiled QPhE telah disimpan.")

# --- COUNTS ---
backend_qasm = Aer.get_backend('qasm_simulator')
qc_qasm = transpile(qc, backend_qasm)
counts = backend_qasm.run(qc_qasm, shots=8192).result().get_counts()
plot_histogram(counts)
plt.savefig("qpca_qphe_result.png")
