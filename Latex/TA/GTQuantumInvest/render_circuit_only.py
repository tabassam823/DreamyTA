import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from plot_generator import plot_quantum_circuit

# Konfigurasi simulasi untuk N=2
N = 2
# Mencoba merender beberapa kedalaman (depth) yang sempat muncul di backtest
depths_to_render = [1, 2, 4]

for d in depths_to_render:
    filename = f"rangkaian_kuantum_depth{d}_N2_v2.png"
    plot_quantum_circuit(N, d, filename)
    print(f"Rangkaian untuk N={N} Depth={d} telah dirender di: {filename}")
