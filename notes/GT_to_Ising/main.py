# =============================================================================
# main.py — Pipeline Utama: GT-Ising-VQE Portfolio Optimization
# =============================================================================
# Pipeline ini mengorkestrasi seluruh modul sesuai alur algoritma pada
# Rencana_kombinasi.md:
#
#   A. Pra-pemrosesan Data (data_loader)
#   B. Analisis Game Theory & CMI (game_theory)
#   C. Konstruksi Hamiltonian Ising (hamiltonian)
#   D. Pencarian Nash Equilibrium (nash_equilibrium)
#   E. Optimasi VQE (vqe_optimizer)
#   F. Ekstraksi CSV & Visualisasi
#
# Tanpa backtesting — langsung mengekstrak hasil optimasi.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# --- Import modul internal ---
from config import (
    TICKERS, N, K, LAMBDA_PENALTY,
    MAX_DEPTH, MAXITER, MAX_TOTAL_ITER, BATCH_SIZE,
    CONV_WINDOW, CONV_TOL, SEED,
    DATA_START, DATA_END, OUTPUT_DIR
)
from data_loader import (
    download_data, compute_log_returns, binarize_states,
    compute_endogenous_gamma, compute_covariance_matrix
)
from game_theory import (
    compute_strategic_return, compute_nmi_matrix,
    compute_xi_cmi, amplify_risk_matrix
)
from hamiltonian import (
    build_qubo_matrix, qubo_to_ising,
    build_pennylane_hamiltonian, brute_force_ising
)
from nash_equilibrium import best_response_dynamics
from vqe_optimizer import run_vqe_adaptive

warnings.filterwarnings('ignore')


def main():
    print("=" * 70)
    print("  Pipeline GT-Ising-VQE: Optimasi Portofolio Kuantum")
    print("=" * 70)

    # Buat direktori output
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # =====================================================================
    # TAHAP A: Pra-pemrosesan Data
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP A: Pra-pemrosesan Data")
    print("=" * 70)

    prices = download_data(TICKERS, DATA_START, DATA_END)
    log_returns = compute_log_returns(prices)
    binary_states = binarize_states(log_returns)
    gamma = compute_endogenous_gamma(log_returns, TICKERS)
    cov_matrix = compute_covariance_matrix(log_returns, TICKERS)
    cov_diag = np.diag(cov_matrix)

    print(f"\n  Aset        : {TICKERS}")
    print(f"  N           : {N}")
    print(f"  K (target)  : {K}")
    print(f"  Periode     : {DATA_START} → {DATA_END}")
    print(f"  Gamma       : {gamma:.4f}")
    print(f"  Lambda (pen): {LAMBDA_PENALTY}")

    # =====================================================================
    # TAHAP B: Analisis Game Theory & CMI
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP B: Analisis Game Theory & CMI")
    print("=" * 70)

    # Strategic returns μ̃
    mu_tilde = compute_strategic_return(log_returns, binary_states, TICKERS)

    # NMI matrix
    nmi_matrix = compute_nmi_matrix(binary_states, TICKERS)

    # Koefisien penskalaan ξ^CMI
    xi_cmi = compute_xi_cmi(cov_matrix, nmi_matrix, N)

    # Matriks risiko yang diamplifikasi σ̃
    sigma_tilde = amplify_risk_matrix(cov_matrix, nmi_matrix, xi_cmi, N)

    # =====================================================================
    # TAHAP C: Konstruksi Hamiltonian Ising
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP C: Konstruksi Hamiltonian Ising")
    print("=" * 70)

    # Matriks QUBO total
    Q_total = build_qubo_matrix(
        mu_tilde, cov_diag, sigma_tilde,
        gamma, LAMBDA_PENALTY, K, N
    )

    # Pemetaan ke Ising
    h_ising, J_ising = qubo_to_ising(Q_total, N)

    # Hamiltonian PennyLane
    H = build_pennylane_hamiltonian(h_ising, J_ising, N)

    # =====================================================================
    # TAHAP D: Brute Force (Klasikal, untuk validasi)
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP D: Brute Force Ground State (Validasi)")
    print("=" * 70)

    bf_bitstring, bf_energy, all_energies = brute_force_ising(
        h_ising, J_ising, N, K=K
    )
    bf_selected = [i for i, b in enumerate(bf_bitstring) if b == '1']
    bf_selected_names = [TICKERS[i] for i in bf_selected]
    print(f"  Aset terpilih (BF)  : {bf_selected_names}")

    # =====================================================================
    # TAHAP E: Pencarian Nash Equilibrium
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP E: Pencarian Nash Equilibrium")
    print("=" * 70)

    x_nash, phi_nash = best_response_dynamics(
        N, mu_tilde, sigma_tilde, cov_diag,
        gamma, LAMBDA_PENALTY, K,
        max_iter=200, n_restarts=20, seed=SEED
    )
    nash_selected = [i for i in range(N) if x_nash[i] == 1]
    nash_selected_names = [TICKERS[i] for i in nash_selected]

    # Hitung energi Ising untuk Nash solution
    spins_nash = np.array([1 - 2 * x_nash[i] for i in range(N)])
    E_nash = 0.0
    for i in range(N):
        E_nash += h_ising[i] * spins_nash[i]
    for i in range(N):
        for j in range(i + 1, N):
            E_nash += J_ising[i, j] * spins_nash[i] * spins_nash[j]

    print(f"  Energi Ising (Nash) : {E_nash:.6f}")

    # =====================================================================
    # TAHAP F: Optimasi VQE
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP F: Optimasi VQE (EfficientSU2 + SPSA Adaptive)")
    print("=" * 70)

    vqe_selected, vqe_depth, vqe_energy, vqe_history, vqe_probs = \
        run_vqe_adaptive(
            H, N, K=K,
            max_depth=MAX_DEPTH, maxiter=MAXITER,
            max_total_iter=MAX_TOTAL_ITER, batch_size=BATCH_SIZE,
            conv_window=CONV_WINDOW, conv_tol=CONV_TOL, seed=SEED
        )
    vqe_selected_names = [TICKERS[i] for i in vqe_selected]

    # =====================================================================
    # TAHAP G: Ringkasan Perbandingan
    # =====================================================================
    print("\n" + "=" * 70)
    print("  RINGKASAN PERBANDINGAN METODE")
    print("=" * 70)
    print(f"  {'Metode':<20} {'Aset Terpilih':<25} {'E_min':<15}")
    print(f"  {'-'*58}")
    print(f"  {'Brute Force':<20} {str(bf_selected_names):<25} {bf_energy:<15.6f}")
    print(f"  {'Nash Equilibrium':<20} {str(nash_selected_names):<25} {E_nash:<15.6f}")
    print(f"  {'VQE (Depth '+str(vqe_depth)+')':<20} {str(vqe_selected_names):<25} {vqe_energy:<15.6f}")

    # =====================================================================
    # TAHAP H: Ekstraksi Data CSV
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP H: Ekstraksi Data CSV")
    print("=" * 70)

    # --- CSV 1: Perbandingan Energi ---
    df_energies = pd.DataFrame({
        'Metode': ['Brute Force', 'Nash Equilibrium', f'VQE (Depth {vqe_depth})'],
        'E_min': [bf_energy, E_nash, vqe_energy],
        'Bitstring': [
            bf_bitstring,
            ''.join([str(int(b)) for b in x_nash]),
            format(np.argmax(vqe_probs), f'0{N}b')
        ],
        'Aset_Terpilih': [
            ', '.join(bf_selected_names),
            ', '.join(nash_selected_names),
            ', '.join(vqe_selected_names)
        ]
    })
    path_energies = os.path.join(OUTPUT_DIR, 'results_energies.csv')
    df_energies.to_csv(path_energies, index=False)
    print(f"  Disimpan: {path_energies}")

    # --- CSV 2: Riwayat Konvergensi VQE ---
    df_conv = pd.DataFrame({
        'Batch': list(range(1, len(vqe_history) + 1)),
        'Energy': vqe_history
    })
    path_conv = os.path.join(OUTPUT_DIR, 'results_convergence.csv')
    df_conv.to_csv(path_conv, index=False)
    print(f"  Disimpan: {path_conv}")

    # --- CSV 3: Parameter Metrik (μ̃ dan σ̃) ---
    metrics_data = {'Ticker': TICKERS, 'mu_tilde': mu_tilde}
    for j in range(N):
        metrics_data[f'sigma_tilde_{TICKERS[j]}'] = sigma_tilde[:, j]
    df_metrics = pd.DataFrame(metrics_data)
    path_metrics = os.path.join(OUTPUT_DIR, 'results_metrics.csv')
    df_metrics.to_csv(path_metrics, index=False)
    print(f"  Disimpan: {path_metrics}")

    # --- CSV 4: Seluruh Energi Brute Force ---
    df_bf = pd.DataFrame({
        'Bitstring': list(all_energies.keys()),
        'Energy': list(all_energies.values())
    }).sort_values('Energy')
    path_bf = os.path.join(OUTPUT_DIR, 'results_brute_force.csv')
    df_bf.to_csv(path_bf, index=False)
    print(f"  Disimpan: {path_bf}")

    # =====================================================================
    # TAHAP I: Visualisasi
    # =====================================================================
    print("\n" + "=" * 70)
    print("  TAHAP I: Visualisasi")
    print("=" * 70)

    # --- Plot 1: Convergence Plot ---
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(range(1, len(vqe_history) + 1), vqe_history,
             'b-o', markersize=3, linewidth=1.5, label='VQE Energy')
    ax1.axhline(y=bf_energy, color='r', linestyle='--', linewidth=1.2,
                label=f'Brute Force E = {bf_energy:.4f}')
    ax1.axhline(y=E_nash, color='g', linestyle=':', linewidth=1.2,
                label=f'Nash EQ E = {E_nash:.4f}')
    ax1.set_xlabel('Batch SPSA', fontsize=12)
    ax1.set_ylabel('Energy', fontsize=12)
    ax1.set_title('VQE Convergence Plot (SPSA Adaptive)', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.4)
    path_conv_plot = os.path.join(OUTPUT_DIR, 'plot_convergence.png')
    fig1.tight_layout()
    fig1.savefig(path_conv_plot, dpi=150)
    print(f"  Disimpan: {path_conv_plot}")

    # --- Plot 2: State Probability Histogram ---
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    n_states = 2 ** N
    state_labels = [format(i, f'0{N}b') for i in range(n_states)]

    # Tandai state dengan K qubit aktif
    colors = []
    for label in state_labels:
        if label.count('1') == K:
            colors.append('steelblue')
        else:
            colors.append('lightgray')

    ax2.bar(range(n_states), vqe_probs, color=colors, edgecolor='navy',
            linewidth=0.3)
    ax2.set_xticks(range(n_states))
    ax2.set_xticklabels(state_labels, rotation=90, fontsize=8)
    ax2.set_xlabel('Basis State |s⟩', fontsize=12)
    ax2.set_ylabel('Probability', fontsize=12)
    ax2.set_title('VQE State Probability Distribution', fontsize=14)

    # Annotate ground state
    gs_idx = int(bf_bitstring, 2)
    ax2.annotate(f'GS: |{bf_bitstring}⟩',
                 xy=(gs_idx, vqe_probs[gs_idx]),
                 xytext=(gs_idx + 1, vqe_probs[gs_idx] + 0.05),
                 arrowprops=dict(arrowstyle='->', color='red'),
                 fontsize=9, color='red', fontweight='bold')

    path_prob_plot = os.path.join(OUTPUT_DIR, 'plot_state_probability.png')
    fig2.tight_layout()
    fig2.savefig(path_prob_plot, dpi=150)
    print(f"  Disimpan: {path_prob_plot}")

    # --- Plot 3: Comparison Chart ---
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    methods = ['Brute Force', 'Nash EQ', 'VQE']
    energies = [bf_energy, E_nash, vqe_energy]
    bar_colors = ['#2ecc71', '#e74c3c', '#3498db']

    bars = ax3.bar(methods, energies, color=bar_colors, edgecolor='black',
                   linewidth=0.8, width=0.5)
    for bar, e in zip(bars, energies):
        ax3.text(bar.get_x() + bar.get_width() / 2., bar.get_height(),
                 f'{e:.4f}', ha='center', va='bottom', fontsize=11,
                 fontweight='bold')

    ax3.set_ylabel('Ising Energy (E_min)', fontsize=12)
    ax3.set_title('Perbandingan Energi Minimum: BF vs Nash vs VQE', fontsize=14)
    ax3.grid(axis='y', alpha=0.4)

    path_comp_plot = os.path.join(OUTPUT_DIR, 'plot_comparison.png')
    fig3.tight_layout()
    fig3.savefig(path_comp_plot, dpi=150)
    print(f"  Disimpan: {path_comp_plot}")

    plt.close('all')

    # =====================================================================
    # SELESAI
    # =====================================================================
    print("\n" + "=" * 70)
    print("  PIPELINE SELESAI")
    print("=" * 70)
    print(f"\n  Seluruh output tersimpan di: ./{OUTPUT_DIR}/")
    print(f"  CSV files : results_energies.csv, results_convergence.csv,")
    print(f"              results_metrics.csv, results_brute_force.csv")
    print(f"  Plots     : plot_convergence.png, plot_state_probability.png,")
    print(f"              plot_comparison.png")


if __name__ == '__main__':
    main()
