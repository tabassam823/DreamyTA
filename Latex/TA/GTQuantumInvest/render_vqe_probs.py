import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pennylane as qml
import pandas as pd
import os

def render_vqe_probability_bar(n_qubits, K):
    # 1. Ambil Parameter Terbaik (Theta) dari hasil run sebelumnya
    # Kita asumsikan file 'theta_final_all_depths.csv' ada
    if not os.path.exists('theta_final_all_depths.csv'):
        print("Error: File theta_final_all_depths.csv tidak ditemukan. Jalankan simulasi terlebih dahulu.")
        return

    df_theta = pd.read_csv('theta_final_all_depths.csv')
    
    # Ambil depth terakhir (max depth) yang tercatat
    max_depth_in_file = df_theta['Depth'].max()
    params = df_theta[df_theta['Depth'] == max_depth_in_file]['Theta_Value'].values
    
    print(f"Merender Probabilitas untuk Depth: {max_depth_in_file}")

    # 2. Definisikan Sirkuit Kuantum untuk mendapatkan Probabilitas
    dev = qml.device("default.qubit", wires=n_qubits)

    @qml.qnode(dev)
    def prob_circuit(p):
        depth = max_depth_in_file
        w = p.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(w[layer, q, 0], wires=q)
                qml.RZ(w[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits - 1):
                    qml.CNOT(wires=[q, q + 1])
                qml.CNOT(wires=[n_qubits - 1, 0])
        return qml.probs(wires=range(n_qubits))

    # Hitung Probabilitas
    probs = prob_circuit(params)
    bitstrings = [format(i, f'0{n_qubits}b') for i in range(2**n_qubits)]

    # 3. Visualisasi Grafik Batang
    plt.figure(figsize=(10, 6))
    
    # Tentukan warna: Hijau untuk yang valid (sum=K), Merah untuk yang melanggar
    colors = []
    for bs in bitstrings:
        if bs.count('1') == K:
            colors.append('limegreen')
        else:
            colors.append('salmon')

    bars = plt.bar(bitstrings, probs, color=colors, edgecolor='black', alpha=0.8)
    
    # Tambahkan Label Probabilitas di atas batang
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.3f}', ha='center', va='bottom', fontsize=10)

    # Tambahkan keterangan/legend manual
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='limegreen', lw=4, label=f'Valid (K={K})'),
        Line2D([0], [0], color='salmon', lw=4, label='Invalid (Penalty Applied)')
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    plt.title(f"Distribusi Probabilitas State VQE (N={n_qubits}, K={K})", fontsize=14)
    plt.ylabel("Probabilitas", fontsize=12)
    plt.xlabel("Bitstring (Spin Interpretation)", fontsize=12)
    plt.ylim(0, 1.1) # Beri ruang untuk label angka
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Tandai Pemenang
    winner_idx = np.argmax(probs)
    plt.annotate('Kandidat Terpilih\n(Energi Terendah)', 
                 xy=(winner_idx, probs[winner_idx]), 
                 xytext=(winner_idx, probs[winner_idx] + 0.15),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 ha='center', fontweight='bold')

    filename = "visualisasi_probabilitas_vqe.png"
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Grafik probabilitas berhasil disimpan sebagai: {filename}")

if __name__ == "__main__":
    # Gunakan parameter yang sesuai dengan run terakhir Anda
    render_vqe_probability_bar(n_qubits=2, K=1)
