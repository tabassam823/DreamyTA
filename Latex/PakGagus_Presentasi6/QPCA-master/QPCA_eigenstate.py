from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
import numpy as np
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_state_city, plot_bloch_multivector, plot_state_hinton
import math
import matplotlib.pyplot as plt

# Inisialisasi Register
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

# State awal
state_vector = [1/math.sqrt(2), 1/math.sqrt(2)]
qc.initialize(state_vector, [q[2]])
qc.h(q[0])
qc.h(q[1])

# Controlled Unitary
qc.cu(1.59899, -1.11512, 2.02647, 0, q[1], q[2])
qc.cu(2.22862, 0.513123, 3.65472, 0, q[0], q[2])

# Inverse QFT
qc.h(q[0])
qc.cp(-1/2*np.pi, q[0], q[1])
qc.h(q[1])

# --- SIMULASI STATEVECTOR ---
backend_state = Aer.get_backend('statevector_simulator')
qc_state = transpile(qc, backend_state)
outputstate = backend_state.run(qc_state).result().get_statevector(qc_state, decimals=3)

plot_state_city(outputstate).savefig("state_city_eigenstate.png")
plot_bloch_multivector(outputstate).savefig("bloch_eigenstate.png")
plot_state_hinton(outputstate).savefig("hinton_eigenstate.png")

# --- PENGUKURAN ---
qc.barrier()
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

# 1. Simpan Sirkuit Original (Level Tinggi)
qc.draw(output='mpl').savefig("circuit_eigenstate.png")

# 2. Simpan Sirkuit Transpiled (Level Rendah/Hardware)
# Kita paksa menggunakan basis gates IBM: cx, id, rz, sx, x
qc_resynthesized = transpile(qc, basis_gates=['id', 'rz', 'sx', 'x', 'cx'], optimization_level=1)
qc_resynthesized.draw(output='mpl').savefig("circuit_transpiled_eigenstate.png")
print("Sirkuit Transpiled (Dekomposisi Hardware) telah disimpan.")

# --- SIMULASI COUNTS ---
backend_qasm = Aer.get_backend('qasm_simulator')
qc_qasm = transpile(qc, backend_qasm)
counts = backend_qasm.run(qc_qasm, shots=8192).result().get_counts()

plot_histogram(counts)
plt.savefig("qpca_eigenstate_result.png")
