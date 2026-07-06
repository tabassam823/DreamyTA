import matplotlib
matplotlib.use('Agg')  # Menggunakan backend non-interaktif
import matplotlib.pyplot as plt
import numpy as np
import pennylane as qml
import pandas as pd
import os

# Memperbesar ukuran legend (deskripsi garis) 50%
plt.rcParams.update({'legend.fontsize': 15})

# Import Qiskit untuk perenderan rangkaian yang lebih baik
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def plot_all(results, data_clean, value_benchmark_idx, config, filenames):
    """
    Menghasilkan semua grafik yang diperlukan untuk analisis.
    """
    tickers = config['tickers']
    N = len(tickers)
    benchmark_ticker = config['benchmark_ticker']

    # 1. Folder Khusus Analisis Jendela
    output_dir = f"Analisis_Window_N{N}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print(f"\n--- Menghasilkan Grafik Analisis Per Jendela di '{output_dir}' ---")
    for i, win_data in enumerate(results['window_analysis_history']):
        win_filename = os.path.join(output_dir, f"{win_data['date']}_window.png")
        plot_window_analysis(win_data, n_qubits=N, filename=win_filename)
        
        # Render sirkuit per jendela
        circ_filename = os.path.join(output_dir, f"{win_data['date']}_circuit.png")
        plot_quantum_circuit(N, win_data['best_depth'], circ_filename, params=win_data['best_params'])

    # 2. Update nama file rangkaian untuk depth terakhir (untuk folder Hasil_NX)
    final_depth = results['depths_history'][-1] if len(results['depths_history']) > 0 else 1
    suffix = f"_N{N}"
    filenames['circuit_png'] = f'rangkaian_kuantum_depth{final_depth}{suffix}.png'
    
    # Rangkaian Kuantum Window Terakhir dengan Parameter
    final_win = results['window_analysis_history'][-1]
    plot_quantum_circuit(N, final_depth, filenames['circuit_png'], params=final_win['best_params'])

    # 4. Hasil Backtest VQE vs Benchmarks
    # Cari data classic jika ada
    classic_file = f"classic_compare/Hasil_Classic_Compare/equity_history_classic_N{N}.csv"
    value_classic = None
    dates_classic = None
    if os.path.exists(classic_file):
        try:
            df_classic = pd.read_csv(classic_file)
            df_classic['Date'] = pd.to_datetime(df_classic['Date'])
            value_classic = df_classic['Equity'].values
            dates_classic = df_classic['Date'].values
        except:
            pass

    plot_equity_growth(data_clean, results['value_vqe'], results['value_bench'],
                       value_benchmark_idx, benchmark_ticker, r'VQE $\mathit{rebalance}$',
                       'blue', filenames['backtest_vqe_png'])

    # 5. Hasil Backtest Nash vs Benchmarks
    plot_equity_growth(data_clean, results['value_nash'], results['value_bench'],
                       value_benchmark_idx, benchmark_ticker, r'$\mathit{Nash \ Equilibrium}$ (Klasik)',
                       'orange', filenames['backtest_nash_png'])

    # 6. Depth per Window
    plot_depth_per_window(results['rebalance_dates'], results['depths_history'], filenames['depth_png'])

def process_histories(histories):
    """Pad histories and calculate mean and std dev."""
    if not histories or not isinstance(histories[0], (list, np.ndarray)):
        return histories, None
    
    max_len = max(len(h) for h in histories)
    padded_histories = []
    for h in histories:
        h_list = list(h)
        if len(h_list) < max_len:
            padded_histories.append(h_list + [h_list[-1]] * (max_len - len(h_list)))
        else:
            padded_histories.append(h_list)
            
    padded_array = np.array(padded_histories)
    mean_hist = np.mean(padded_array, axis=0)
    std_hist = np.std(padded_array, axis=0)
    return mean_hist, std_hist

def plot_window_analysis(win_data, n_qubits, filename):
    """
    Merender 4 panel analisis untuk satu jendela waktu tertentu.
    """
    date = win_data['date']
    best_history = win_data['best_history']
    best_ent_hist = win_data['best_ent_hist']
    depth_energies = win_data['depth_energies']
    probs = win_data['winning_probs']
    K = win_data['K']
    use_warm_start = win_data.get('use_warm_start', True)

    # Hitung Brute Force khusus untuk jendela ini (dengan suffix N)
    bf_energy = calculate_bf_for_window(date, n_qubits)

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Judul Dinamis berdasarkan Warm-Start
    ws_text = r"$\mathit{Warm-Start}$" if use_warm_start else r"tanpa $\mathit{Warm-Start}$"
    fig.suptitle(f"Analisis VQE {ws_text} - Jendela {date} (N={n_qubits}, K={K})", fontsize=20)
    axes = axes.flatten()

    # 1. Konvergensi Energi
    if len(best_history) > 0 and isinstance(best_history[0], (list, np.ndarray)):
        mean_h, std_h = process_histories(best_history)
        iters = np.arange(1, len(mean_h) + 1) * 10
        
        # Plot 5 garis putus-putus
        for h in best_history:
            h_iters = np.arange(1, len(h) + 1) * 10
            axes[0].plot(h_iters, h, color='blue', alpha=0.3, linewidth=1, linestyle='--')
            
        # Area standar deviasi
        axes[0].fill_between(iters, mean_h - std_h, mean_h + std_h, color='blue', alpha=0.15, label='Std Dev')
        
        # Plot garis rata-rata tebal
        final_e_spsa = mean_h[-1]
        axes[0].plot(iters, mean_h, color='blue', linewidth=2.5, label=f'Avg SPSA ({final_e_spsa:.4f})')
        
        if bf_energy is not None:
            axes[0].axhline(y=bf_energy, color='red', linestyle='--', label=f'Brute Force ({bf_energy:.4f})')
            all_vals = [v for h in best_history for v in h] + [bf_energy]
            axes[0].set_ylim(min(all_vals)-0.01, max(all_vals)+0.01)
    else:
        iters = np.arange(1, len(best_history) + 1) * 10 # batch_size=10
        final_e_spsa = best_history[-1] if len(best_history) > 0 else 0
        axes[0].plot(iters, best_history, marker='o', markersize=3, color='blue', label=f'SPSA Progress ({final_e_spsa:.4f})')
            
        if bf_energy is not None:
            axes[0].axhline(y=bf_energy, color='red', linestyle='--', label=f'Brute Force ({bf_energy:.4f})')
            all_vals = list(best_history) + [bf_energy]
            axes[0].set_ylim(min(all_vals)-0.01, max(all_vals)+0.01)

    axes[0].set_title('1. Konvergensi Energi (Iterasi SPSA)')
    axes[0].set_ylabel('Energi')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # 2. Energi vs Depth
    d_list = [d for d, e, it in depth_energies]
    e_list = [e for d, e, it in depth_energies]
    vqe_min_depth = min(e_list)
    axes[1].plot(d_list, e_list, marker='s', markersize=8, color='blue', label=f'VQE Min ({vqe_min_depth:.4f})')
    if bf_energy is not None:
        axes[1].axhline(y=bf_energy, color='red', linestyle='--', label=f'Brute Force ({bf_energy:.4f})')
        all_e = e_list + [bf_energy]
        axes[1].set_ylim(min(all_e)-0.01, max(all_e)+0.01)
    axes[1].set_title('2. Pencarian Energi vs Depth')
    axes[1].set_xticks(d_list)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # 3. Entanglement Entropy
    if len(best_ent_hist) > 0:
        if isinstance(best_ent_hist[0], (list, np.ndarray)):
            mean_ent, std_ent = process_histories(best_ent_hist)
            iters_ent = np.arange(1, len(mean_ent) + 1) * 10
            
            for h in best_ent_hist:
                h_iters = np.arange(1, len(h) + 1) * 10
                axes[2].plot(h_iters, h, color='purple', alpha=0.3, linewidth=1, linestyle='--')
                
            axes[2].fill_between(iters_ent, mean_ent - std_ent, mean_ent + std_ent, color='purple', alpha=0.15)
            axes[2].plot(iters_ent, mean_ent, color='purple', linewidth=2.5)
        else:
            iters_ent = np.arange(1, len(best_ent_hist) + 1) * 10
            axes[2].plot(iters_ent, best_ent_hist, color='purple', marker='^', markersize=3)
            
        axes[2].set_title('3. Entanglement Entropy vs Iterasi')
        axes[2].set_ylabel('Von Neumann Entropy')
        axes[2].grid(True, alpha=0.3)

    # 4. Distribusi Probabilitas (Bar Chart)
    bitstrings = [format(i, f'0{n_qubits}b') for i in range(2**n_qubits)]
    colors = ['limegreen' if b.count('1') == K else 'salmon' for b in bitstrings]
    axes[3].bar(bitstrings, probs, color=colors, edgecolor='black')
    axes[3].set_title(f'4. Probabilitas State (K={K})')
    axes[3].set_ylim(0, 1.1)
    # Tambahkan label teks di atas batang
    for idx, p in enumerate(probs):
        axes[3].text(idx, p + 0.02, f"{p:.2f}", ha='center', fontsize=8)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(filename)
    plt.close()

def plot_quantum_circuit(N, depth, filename, params=None, title=None):
    """
    Merender rangkaian kuantum menggunakan Qiskit untuk hasil yang lebih berwarna,
    informatif (label parameter), dan otomatis dibagi baris (folding).
    """
    qr = QuantumRegister(N, 'q')
    cr = ClassicalRegister(N, 'c')
    qc = QuantumCircuit(qr, cr)

    if params is None:
        params = np.zeros(N * 2 * (depth + 1))
    
    # Reshape parameter sesuai struktur ansatz (layer, qubit, gate_type)
    w = params.reshape((depth + 1, N, 2))
    
    for layer in range(depth + 1):
        for q_idx in range(N):
            # Ambil nilai theta dan bulatkan agar tidak terlalu panjang di gambar
            theta_ry = np.round(float(w[layer, q_idx, 0]), 2)
            theta_rz = np.round(float(w[layer, q_idx, 1]), 2)
            
            # Tambahkan gate RY dan RZ dengan label parameter numerik
            qc.ry(theta_ry, qr[q_idx])
            qc.rz(theta_rz, qr[q_idx])
        
        if layer < depth:
            # Tambahkan Barrier antar layer untuk kejelasan visual
            qc.barrier()
            # Chain CNOT (Entanglement)
            for q_idx in range(N - 1):
                qc.cx(qr[q_idx], qr[q_idx + 1])
            qc.cx(qr[N - 1], qr[0])
            qc.barrier()

    # Tambahkan Pengukuran di akhir
    qc.measure(qr, cr)

    # Pengaturan Visual Qiskit
    # style='iqp' memberikan skema warna modern/IBM standard
    # fold=20 disetel agar muat sekitar 5 depth per baris (mencegah terlalu panjang ke samping)
    fig = qc.draw(output='mpl', style='iqp', plot_barriers=True, justify='left', fold=20)
    
    if title:
        fig.suptitle(title, fontsize=16, fontweight='bold', y=1.05)
    else:
        fig.suptitle(f"VQE Optimized Circuit (N={N}, Depth={depth})", fontsize=16, fontweight='bold', y=1.05)
        
    fig.savefig(filename, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f"Gambar rangkaian kuantum (Qiskit) disimpan sebagai '{filename}'.")

def calculate_bf_for_window(date, n_qubits):
    """Fungsi pembantu untuk hitung BF on-the-fly dengan Penalty Annealing Target."""
    suffix = f"_N{n_qubits}"
    try:
        # 1. Ambil Bias (h)
        h_df = pd.read_csv(f'bias_h_total{suffix}.csv')
        h_win = h_df[h_df['Date'] == str(date)]
        h_obj = h_win['Bias_h_Obj'].values
        h_pen = h_win['Bias_h_Pen'].values
        n = len(h_obj)
        
        # 2. Ambil Interaksi (J)
        J_df = pd.read_csv(f'interaksi_J_total{suffix}.csv')
        J_win = J_df[J_df['Date'] == str(date)]
        J_mat_obj = np.zeros((n, n))
        J_mat_pen = np.zeros((n, n))
        tickers = h_win['Ticker'].values
        t2i = {t: i for i, t in enumerate(tickers)}
        for _, r in J_win.iterrows():
            i, j = t2i[r['Ticker_i']], t2i[r['Ticker_j']]
            J_mat_obj[i,j] = J_mat_obj[j,i] = r['Interaction_J_Obj']
            J_mat_pen[i,j] = J_mat_pen[j,i] = r['Interaction_J_Pen']
            
        # 3. Ambil Konstanta C dan Target Penalty
        c_df = pd.read_csv(f'parameter_pendamping{suffix}.csv')
        c_win = c_df[c_df['Date'] == str(date)].iloc[0]
        c_obj = c_win['C_Obj']
        c_pen = c_win['C_Pen']
        penalty_A = c_win['Penalty_A_Target']
        
        # 4. Kombinasikan menjadi Hamiltonian Total Akhir
        h_total = h_obj + penalty_A * h_pen
        J_total = J_mat_obj + penalty_A * J_mat_pen
        c_total = c_obj + penalty_A * c_pen
        
        from itertools import product
        min_e = float('inf')
        for b in product([0, 1], repeat=n):
            Z = 1 - 2 * np.array(b)
            # E = sum(h_i * Z_i) + sum(J_ij * Z_i * Z_j) + C
            e = np.sum(h_total * Z) + sum(J_total[i,j]*Z[i]*Z[j] for i in range(n) for j in range(i+1, n)) + c_total
            if e < min_e: min_e = e
        return min_e
    except:
        return None

    plt.tight_layout()
    plt.savefig(filename)
    print(f"Grafik konvergensi detail disimpan sebagai '{filename}'.")

def plot_equity_growth(data_clean, value_strategy, value_bench, value_benchmark_idx, benchmark_ticker, strategy_label, color, filename, value_classic=None, dates_classic=None):
    # Hitung persentase pertumbuhan
    pct_strategy = (np.array(value_strategy) - value_strategy[0]) / value_strategy[0] * 100
    pct_bench = (np.array(value_bench) - value_bench[0]) / value_bench[0] * 100
    pct_idx = (value_benchmark_idx.values - value_benchmark_idx.values[0]) / value_benchmark_idx.values[0] * 100
    
    plt.figure(figsize=(12, 6))
    plt.plot(data_clean.index[:len(pct_strategy)], pct_strategy, label=strategy_label, linewidth=2.5, color=color)
    display_ticker = "IHSG" if benchmark_ticker == "^JKSE" else benchmark_ticker
    plt.plot(data_clean.index[:len(pct_bench)], pct_bench, label=r'$\mathit{Benchmark}$ ($\mathit{Equal \ Weight}$)', linestyle=':', color='black', alpha=0.6)
    plt.plot(value_benchmark_idx.index, pct_idx, label=f'Indeks ({display_ticker})', linestyle='-.', color='magenta', linewidth=2)
    
    if value_classic is not None and dates_classic is not None:
        pct_classic = (np.array(value_classic) - value_classic[0]) / value_classic[0] * 100
        plt.plot(dates_classic, pct_classic, label='Classic Markowitz (Mean-Var)', linestyle='--', color='green', linewidth=2)

    plt.title('Persentase Pertumbuhan Modal Strategi Investasi')
    plt.ylabel('Persentase Pertumbuhan Modal (%)')
    plt.xlabel('Tanggal')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Grafik {strategy_label} disimpan sebagai '{filename}'.")

def plot_depth_per_window(rebalance_dates, depths_history, filename):
    plt.figure(figsize=(10, 5))
    avg_depth_floor = int(np.floor(np.mean(depths_history)))
    plt.plot(rebalance_dates, depths_history, marker='o', linestyle='-', color='purple', label='Depth Terpilih')
    plt.axhline(y=avg_depth_floor, color='red', linestyle='--', label=f'Rata-rata Depth (Floor): {avg_depth_floor}')
    plt.title('Depth Terpilih vs Rebalance Window')
    plt.ylabel('Depth')
    plt.xlabel('Tanggal Rebalance')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Grafik depth per window disimpan sebagai '{filename}'. Rata-rata (floor): {avg_depth_floor}")
