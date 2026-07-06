import numpy as np
from plot_generator import plot_quantum_circuit

# Konfigurasi: N=2, Depth=6 (4 + N)
N = 2
depth = 6

# Generate parameter dummy agar label angka muncul di gambar
# Total parameter = N * 2 * (depth + 1) = 2 * 2 * 7 = 28
np.random.seed(42)
dummy_params = np.random.uniform(0, 2*np.pi, N * 2 * (depth + 1))

filename = "test_qiskit_depth6_N2.png"
title = "Sample VQE Circuit: N=2, Depth=6 (Standardized)"

print(f"Sedang merender sirkuit contoh ke {filename}...")
plot_quantum_circuit(N, depth, filename, params=dummy_params, title=title)
print("Selesai.")
