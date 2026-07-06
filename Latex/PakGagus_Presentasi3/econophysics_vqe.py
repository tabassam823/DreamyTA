"""
=================================================================
Econophysics Kuantum: Portfolio Optimization via HE-VQE
=================================================================
Pipeline lengkap dari percakapan econophysics_kuantum.pdf:
  Tahap 1: Data Acquisition & Pre-Selection (4 saham LQ45)
  Tahap 2: Konstruksi Matriks Payoff (Markowitz × Game Theory)
  Tahap 3: Konstruksi Hamiltonian (Ising Model + Penalty)
  Tahap 4: Eksekusi HE-VQE dengan SPSA
  Tahap 5: Hasil & Analisis

Aset: BBCA.JK, ASII.JK, TLKM.JK, UNVR.JK → Pilih 2 terbaik
"""

import pennylane as qml
from pennylane import numpy as pnp
import numpy as np
import pandas as pd
import scipy.linalg as la
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

# ================================================================
# TAHAP 1: DATA ACQUISITION & PRE-SELECTION
# ================================================================

def download_stock_data(tickers, period="2y"):
    """Download data saham historis dari Yahoo Finance."""
    print("=" * 70)
    print("TAHAP 1: DATA ACQUISITION & PRE-SELECTION")
    print("=" * 70)
    
    import yfinance as yf
    print(f"Downloading data for: {tickers}...")
    data = yf.download(tickers, period=period, progress=True)['Close']
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data = data.dropna()
    print(f"  Data shape: {data.shape}")
    print(f"  Period: {data.index[0].strftime('%Y-%m-%d')} to {data.index[-1].strftime('%Y-%m-%d')}")
    
    # Hitung log return: R_t = ln(P_t / P_{t-1})
    log_returns = np.log(data / data.shift(1)).dropna()
    
    # Discretization: |0⟩ (Naik) jika R > 0, |1⟩ (Turun) jika R ≤ 0
    binary_states = (log_returns <= 0).astype(int)
    
    print(f"\n  Log Returns (sample):")
    for t in tickers:
        mu = log_returns[t].mean()
        sigma = log_returns[t].std()
        up_pct = (binary_states[t] == 0).mean() * 100
        print(f"    {t}: μ = {mu:.6f}, σ = {sigma:.6f}, Naik = {up_pct:.1f}%")
    
    return data, log_returns, binary_states


# ================================================================
# TAHAP 2: KONSTRUKSI MATRIKS PAYOFF (MARKOWITZ × GAME THEORY)
# ================================================================

def compute_endogenous_lambda(log_returns, tickers):
    """
    Hitung risk aversion endogen dari data (annualized):
    λ_market = σ_avg / (μ_avg + σ_avg)
    
    Annualisasi: μ × 252, σ × √252
    Menggunakan abs per-ticker sebelum averaging untuk menghindari cancellation.
    
    Jika σ besar → λ mendekati 1 → lebih risk averse
    Jika μ besar → λ kecil → lebih agresif
    """
    # Annualisasi sebelum hitung λ
    mu_annual = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std() * np.sqrt(252)
    
    # Mean of abs (hindari cancellation antar ticker)
    mu_avg = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    
    lambda_market = sigma_avg / (mu_avg + sigma_avg)
    return lambda_market


def compute_markowitz_payoff_matrix(log_returns, binary_states, asset_a, asset_b, lambda_risk):
    """
    Hitung matriks payoff Markowitz 2×2 untuk pasangan aset.
    U = (1-λ)·μ_p - λ·σ_p
    
    4 kondisi: (0,0), (0,1), (1,0), (1,1) = state aset A × aset B
    """
    state_A = binary_states[asset_a].values
    state_B = binary_states[asset_b].values
    ret_A = log_returns[asset_a].values
    ret_B = log_returns[asset_b].values
    
    payoff_A = np.zeros((2, 2))
    payoff_B = np.zeros((2, 2))
    counts = np.zeros((2, 2))
    
    for t in range(len(state_A)):
        i, j = state_A[t], state_B[t]
        counts[i, j] += 1
        
        # Return dan risk pada kondisi ini
        mu_a = ret_A[t]
        mu_b = ret_B[t]
        
        # Utilitas Markowitz untuk masing-masing aset (annualized)
        payoff_A[i, j] += (1 - lambda_risk) * (mu_a * 252) - lambda_risk * abs(mu_a * 252)
        payoff_B[i, j] += (1 - lambda_risk) * (mu_b * 252) - lambda_risk * abs(mu_b * 252)
    
    # Rata-ratakan
    for i in range(2):
        for j in range(2):
            if counts[i, j] > 0:
                payoff_A[i, j] /= counts[i, j]
                payoff_B[i, j] /= counts[i, j]
    
    return payoff_A, payoff_B, counts


def classify_game_type(payoff_A, payoff_B):
    """
    Klasifikasi tipe permainan berdasarkan struktur payoff.
    Coordination Game: P(0,0) > P(1,0) dan P(1,1) > P(0,1)
    """
    # Cek dari perspektif A
    coord_A = (payoff_A[0, 0] > payoff_A[1, 0]) and (payoff_A[1, 1] > payoff_A[0, 1])
    # Cek dari perspektif B
    coord_B = (payoff_B[0, 0] > payoff_B[0, 1]) and (payoff_B[1, 1] > payoff_B[1, 0])
    
    if coord_A and coord_B:
        return "Coordination Game"
    elif (not coord_A) and (not coord_B):
        return "Anti-Coordination Game"
    else:
        return "Mixed Strategy Game"


def plot_payoff_matrices(all_payoffs, tickers):
    """Visualisasi 2×2 payoff matrices sebagai heatmap untuk semua pasangan aset."""
    pairs = list(all_payoffs.keys())
    n_pairs = len(pairs)
    
    fig, axes = plt.subplots(n_pairs, 2, figsize=(10, 4 * n_pairs))
    fig.suptitle('2x2 Payoff Matrices for All Asset Pairs', fontsize=14, fontweight='bold', y=1.01)
    
    # Tentukan vmin/vmax global dari semua payoff untuk colorbar konsisten
    all_vals = []
    for (pA, pB) in all_payoffs.values():
        all_vals.extend(pA.flatten().tolist())
        all_vals.extend(pB.flatten().tolist())
    vmin, vmax = min(all_vals), max(all_vals)
    
    for row, (idx_a, idx_b) in enumerate(pairs):
        pA, pB = all_payoffs[(idx_a, idx_b)]
        a_name = tickers[idx_a]
        b_name = tickers[idx_b]
        
        for col, (payoff, name) in enumerate([(pA, a_name), (pB, b_name)]):
            ax = axes[row, col] if n_pairs > 1 else axes[col]
            im = ax.imshow(payoff, cmap='viridis', vmin=vmin, vmax=vmax, 
                          origin='upper', aspect='equal')
            
            # Anotasi nilai di tiap sel
            for i in range(2):
                for j in range(2):
                    val = payoff[i, j]
                    color = 'white' if val < (vmin + vmax) / 2 else 'black'
                    ax.text(j, i, f'{val:.4f}', ha='center', va='center',
                           fontsize=11, fontweight='bold', color=color)
            
            ax.set_title(f'Payoff for {name}', fontsize=11)
            ax.set_xlabel('State B (0=Up, 1=Down)', fontsize=9)
            ax.set_ylabel('State A (0=Up, 1=Down)', fontsize=9)
            ax.set_xticks([0, 1])
            ax.set_yticks([0, 1])
            
            plt.colorbar(im, ax=ax, shrink=0.8)
    
    plt.tight_layout()
    plt.savefig('payoff_matrices_2x2.png', dpi=150, bbox_inches='tight')
    print("  Plot saved: payoff_matrices_2x2.png")
    plt.show()


def run_game_theory_analysis(log_returns, binary_states, tickers, lambda_risk):
    """Tahap 2: Analisis Game Theory untuk seluruh pasangan aset."""
    print("\n" + "=" * 70)
    print("TAHAP 2: KONSTRUKSI MATRIKS PAYOFF (MARKOWITZ × GAME THEORY)")
    print("=" * 70)
    print(f"  λ_market (endogen) = {lambda_risk:.4f}")
    print(f"  Interpretasi: U = ({1-lambda_risk:.2f})·μ - ({lambda_risk:.2f})·σ")
    
    all_payoffs = {}
    all_counts = {}
    all_game_types = {}
    
    pairs = list(combinations(range(len(tickers)), 2))
    for idx_a, idx_b in pairs:
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB, counts = compute_markowitz_payoff_matrix(
            log_returns, binary_states, a, b, lambda_risk
        )
        game_type = classify_game_type(pA, pB)
        
        all_payoffs[(idx_a, idx_b)] = (pA, pB)
        all_counts[(idx_a, idx_b)] = counts
        all_game_types[(idx_a, idx_b)] = game_type
        
        print(f"\n  Pasangan {a} vs {b}:")
        print(f"    Game Type: {game_type}")
        print(f"    Payoff {a}:")
        print(f"      {pA}")
        print(f"    Payoff {b}:")
        print(f"      {pB}")
        print(f"    Frekuensi: {counts}")
    
    # Visualisasi 2×2 heatmap
    print("\n  Generating 2×2 payoff matrix heatmaps...")
    plot_payoff_matrices(all_payoffs, tickers)
    
    return all_payoffs, all_counts, all_game_types


# ================================================================
# TAHAP 3: EKSTRAKSI PARAMETER HAMILTONIAN (h_i, J_ij via QMI)
# ================================================================

def compute_bias_hi(all_payoffs, tickers):
    """
    Hitung bias h_i dari matriks payoff marginal:
    h_i = (P_i[1,0] + P_i[1,1]) - (P_i[0,0] + P_i[0,1])
    
    Jika h_i negatif → aset cenderung dipilih (energi lebih rendah)
    """
    n_assets = len(tickers)
    h = np.zeros(n_assets)
    
    for i in range(n_assets):
        payoff_sum = 0
        count = 0
        for (a, b), (pA, pB) in all_payoffs.items():
            if a == i:
                # Aset i sebagai "Leader"
                payoff_sum += (pA[1, 0] + pA[1, 1]) - (pA[0, 0] + pA[0, 1])
                count += 1
            elif b == i:
                # Aset i sebagai "Follower"
                payoff_sum += (pB[0, 1] + pB[1, 1]) - (pB[0, 0] + pB[1, 0])
                count += 1
        if count > 0:
            h[i] = payoff_sum / count
    
    return h


def compute_qmi_jij(binary_states, asset_a, asset_b, alpha=1.0):
    """
    Hitung Quantum Mutual Information (QMI) sebagai J_ij.
    
    Langkah:
    1. Hitung probabilitas gabungan dengan Laplace Smoothing
    2. Bangun density matrix ρ_LF
    3. Hitung Von Neumann Entropy: S(ρ) = -Tr(ρ ln ρ)
    4. QMI = S(L) + S(F) - S(L,F)
    """
    state_A = binary_states[asset_a].values
    state_B = binary_states[asset_b].values
    N = len(state_A)
    
    # 1. Frekuensi dengan Laplace Smoothing
    n_ij = np.zeros((2, 2))
    for t in range(N):
        n_ij[state_A[t], state_B[t]] += 1
    
    # P(i,j) = (n_ij + α) / (N + 4α)
    prob_joint = (n_ij + alpha) / (N + 4 * alpha)
    
    # 2. Density Matrix ρ_LF = Σ P(i,j)|i,j⟩⟨i,j|
    rho_LF = np.diag(prob_joint.flatten())  # 4×4 diagonal matrix
    
    # 3. Marginal density matrices (partial trace)
    # ρ_L = Tr_F(ρ_LF)
    prob_L = prob_joint.sum(axis=1)  # sum over Follower states
    rho_L = np.diag(prob_L)
    
    # ρ_F = Tr_L(ρ_LF)
    prob_F = prob_joint.sum(axis=0)  # sum over Leader states
    rho_F = np.diag(prob_F)
    
    # 4. Von Neumann Entropy: S(ρ) = -Tr(ρ ln ρ)
    def von_neumann_entropy(rho):
        eigenvalues = np.real(la.eigvalsh(rho))
        eigenvalues = eigenvalues[eigenvalues > 1e-12]  # avoid log(0)
        return -np.sum(eigenvalues * np.log(eigenvalues))
    
    S_LF = von_neumann_entropy(rho_LF)
    S_L = von_neumann_entropy(rho_L)
    S_F = von_neumann_entropy(rho_F)
    
    # QMI = S(L) + S(F) - S(L,F)
    qmi = S_L + S_F - S_LF
    
    return qmi, prob_joint, S_L, S_F, S_LF


def extract_hamiltonian_params(binary_states, all_payoffs, tickers):
    """Tahap 3: Ekstraksi h_i dan J_ij."""
    print("\n" + "=" * 70)
    print("TAHAP 3: EKSTRAKSI PARAMETER HAMILTONIAN")
    print("=" * 70)
    
    n_assets = len(tickers)
    
    # Bias h_i
    h = compute_bias_hi(all_payoffs, tickers)
    print("\n  Bias (h_i):")
    for i, t in enumerate(tickers):
        interpretation = "cenderung dipilih" if h[i] < 0 else "kurang menarik"
        print(f"    h_{t} = {h[i]:.6f} ({interpretation})")
    
    # Interaksi J_ij via QMI
    J = np.zeros((n_assets, n_assets))
    qmi_details = {}
    
    print("\n  Interaksi J_ij (Quantum Mutual Information):")
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            qmi, prob_joint, S_L, S_F, S_LF = compute_qmi_jij(
                binary_states, tickers[i], tickers[j]
            )
            J[i, j] = qmi
            J[j, i] = qmi
            qmi_details[(i, j)] = {
                'qmi': qmi, 'prob': prob_joint,
                'S_L': S_L, 'S_F': S_F, 'S_LF': S_LF
            }
            
            sync = "tinggi (sinkron)" if qmi > 0.05 else "rendah (independen)"
            print(f"    J_{tickers[i]}_{tickers[j]} = {qmi:.6f} (korelasi {sync})")
            print(f"      S(L)={S_L:.4f}, S(F)={S_F:.4f}, S(L,F)={S_LF:.4f}")
    
    return h, J, qmi_details


# ================================================================
# TAHAP 4: KONSTRUKSI HAMILTONIAN (ISING MODEL + PENALTY)
# ================================================================

def build_hamiltonian(h, J, n_assets=4, K=2, penalty_A=10.0):
    """
    Bangun Hamiltonian total = H_cost + H_constraint
    
    H_cost = Σ h_i Z_i + Σ J_ij Z_i Z_j
    H_constraint = A·(Σ (I-Z_i)/2 - K)²
    
    K = jumlah aset yang harus dipilih (2)
    A = konstanta penalti (besar agar constraint dihormati)
    """
    print("\n" + "=" * 70)
    print("TAHAP 4: KONSTRUKSI HAMILTONIAN (ISING MODEL)")
    print("=" * 70)
    print(f"  Jumlah aset (qubit): {n_assets}")
    print(f"  Target seleksi (K): {K}")
    print(f"  Konstanta penalti (A): {penalty_A}")
    
    coeffs = []
    obs = []
    
    # === H_cost: bias terms ===
    for i in range(n_assets):
        if abs(h[i]) > 1e-10:
            coeffs.append(float(h[i]))
            obs.append(qml.PauliZ(i))
    
    # === H_cost: interaction terms ===
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J[i, j]) > 1e-10:
                coeffs.append(float(J[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    # === H_constraint: A·(Σ (I-Z_i)/2 - K)² ===
    # Expand: (I-Z_i)/2 = n_i (number operator in Z-basis)
    # Σ n_i = Σ (I-Z_i)/2 = N/2 - (1/2)Σ Z_i
    # (Σ n_i - K)² = (N/2 - K)² - (N/2-K)·Σ Z_i + (1/4)(Σ Z_i)²
    # 
    # (Σ Z_i)² = Σ Z_i² + 2·Σ_{i<j} Z_iZ_j = N·I + 2·Σ_{i<j} Z_iZ_j
    #
    # Full expansion:
    # = (N/2-K)²·I - (N/2-K)·Σ Z_i + (1/4)·(N·I + 2·Σ Z_iZ_j)
    # = [(N/2-K)² + N/4]·I - (N/2-K)·Σ Z_i + (1/2)·Σ Z_iZ_j

    N_half_minus_K = n_assets / 2 - K  # N/2 - K
    
    # Constant term: A·[(N/2-K)² + N/4]
    const_term = penalty_A * (N_half_minus_K**2 + n_assets / 4)
    coeffs.append(float(const_term))
    obs.append(qml.Identity(0))
    
    # Linear terms: -A·(N/2-K)·Z_i
    for i in range(n_assets):
        coeffs.append(float(-penalty_A * N_half_minus_K))
        obs.append(qml.PauliZ(i))
    
    # Quadratic terms: A·(1/2)·Z_iZ_j
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            coeffs.append(float(penalty_A * 0.5))
            obs.append(qml.PauliZ(i) @ qml.PauliZ(j))
    
    H = qml.Hamiltonian(coeffs, obs)
    H = qml.simplify(H)
    
    print(f"\n  Hamiltonian terms: {len(H.ops)}")
    print(f"  H = {H}")
    
    # Verifikasi: hitung energi exact untuk semua 2^4 = 16 states
    print("\n  Energi untuk setiap bitstring:")
    H_matrix = qml.matrix(H)
    best_energy = float('inf')
    best_state = None
    for s in range(2**n_assets):
        bits = format(s, f'0{n_assets}b')
        energy = np.real(H_matrix[s, s])
        n_selected = bits.count('1')
        marker = ""
        if n_selected == K and energy < best_energy:
            best_energy = energy
            best_state = bits
            marker = " ← OPTIMAL"
        print(f"    |{bits}⟩: E = {energy:.4f}, selected = {n_selected}{marker}")
    
    print(f"\n  Ground state (exact): |{best_state}⟩ dengan E = {best_energy:.4f}")
    
    return H, best_state, best_energy


# ================================================================
# TAHAP 5: EKSEKUSI HE-VQE DENGAN SPSA
# ================================================================

def run_he_vqe(H, n_qubits=4, depth=2, maxiter=200, n_shots=1024, seed=42):
    """
    Jalankan Hardware-Efficient VQE:
    - Ansatz: RY(θ) dan RZ(φ) + CNOT chain (0→1, 1→2, 2→3, 3→0)
    - Optimizer: SPSA (2 evaluasi per iterasi)
    """
    print("\n" + "=" * 70)
    print("TAHAP 5: EKSEKUSI HE-VQE DENGAN SPSA")
    print("=" * 70)
    
    rng = np.random.default_rng(seed)
    
    # Parameter count: depth+1 layers × n_qubits × 2 (RY + RZ)
    n_params = n_qubits * 2 * (depth + 1)
    print(f"  Qubits: {n_qubits}")
    print(f"  Depth: {depth}")
    print(f"  Parameters: {n_params}")
    print(f"  Optimizer: SPSA ({maxiter} iterasi)")
    
    dev = qml.device("default.qubit", wires=n_qubits)
    
    @qml.qnode(dev)
    def vqe_circuit(params):
        """HE Ansatz: [Rot] - [CNOT] - [Rot] - [CNOT] - ... - [Rot]"""
        weights = params.reshape((depth + 1, n_qubits, 2))
        
        for layer in range(depth + 1):
            # Rotation layer: RY(θ) + RZ(φ)
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            
            # Entanglement layer (setelah setiap rotation kecuali terakhir)
            if layer < depth:
                # CNOT chain: 0→1, 1→2, 2→3, 3→0
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        
        return qml.expval(H)
    
    def cost_fn(params):
        return float(vqe_circuit(params))
    
    # SPSA Optimizer
    initial_params = rng.uniform(0, 2 * np.pi, n_params)

    # Visualisasi Sirkuit (Added for Presentation)
    print("\n  Generating circuit image...")
    try:
        # Gunakan initial_params untuk visualisasi
        # qml.draw_mpl mengembalikan figure dan axes
        fig, ax = qml.draw_mpl(vqe_circuit, decimals=2)(initial_params)
        plt.title(f"Hardware-Efficient Ansatz (HE-VQE)\n{n_qubits} Qubits, Depth={depth}", fontsize=14)
        plt.tight_layout()
        plt.savefig('he_vqe_circuit.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("  Circuit image saved: he_vqe_circuit.png")
    except Exception as e:
        print(f"  WARNING: Failed to generate circuit image: {e}")
    
    # Auto-calibrate SPSA: scale 'a' by initial cost magnitude
    initial_cost = cost_fn(initial_params)
    print(f"  Initial cost: {initial_cost:.6f}")
    
    # SPSA parameters (calibrated)
    a = 0.2 * max(1.0, abs(initial_cost))  # scale to cost landscape
    c = 0.15
    A = maxiter * 0.1
    alpha = 0.602
    gamma = 0.101
    
    params = initial_params.copy()
    history = []
    best_params = params.copy()
    best_energy = float('inf')
    
    print(f"\n  Memulai optimasi SPSA...")
    for k in range(maxiter):
        # Gain sequences
        a_k = a / (A + k + 1) ** alpha
        c_k = c / (k + 1) ** gamma
        
        # Random perturbation ±1
        delta = 2 * rng.integers(0, 2, size=n_params) - 1
        
        # Evaluate perturbed points (2 evaluasi saja!)
        f_plus = cost_fn(params + c_k * delta)
        f_minus = cost_fn(params - c_k * delta)
        
        # Approximate gradient
        grad = (f_plus - f_minus) / (2 * c_k * delta)
        
        # Update parameters
        params = params - a_k * grad
        
        cost_mid = (f_plus + f_minus) / 2
        history.append(cost_mid)
        
        if cost_mid < best_energy:
            best_energy = cost_mid
            best_params = params.copy()
        
        if k % 40 == 0 or k == maxiter - 1:
            print(f"    Iter {k:4d}: E = {cost_mid:.6f} (best = {best_energy:.6f})")
    
    print(f"\n  Optimasi selesai!")
    print(f"  Best Energy: {best_energy:.6f}")
    print(f"  Total evaluasi fungsi: {2 * maxiter}")
    
    # === SAMPLING AKHIR ===
    print(f"\n  Sampling {n_shots} shots dari sirkuit optimal...")
    
    dev_sample = qml.device("default.qubit", wires=n_qubits, shots=n_shots)
    
    @qml.qnode(dev_sample)
    def sample_circuit(params):
        weights = params.reshape((depth + 1, n_qubits, 2))
        for layer in range(depth + 1):
            for q in range(n_qubits):
                qml.RY(weights[layer, q, 0], wires=q)
                qml.RZ(weights[layer, q, 1], wires=q)
            if layer < depth:
                for q in range(n_qubits):
                    qml.CNOT(wires=[q, (q + 1) % n_qubits])
        return qml.probs(wires=range(n_qubits))
    
    probs = sample_circuit(best_params)
    
    # Tampilkan distribusi
    print("\n  Distribusi State (top 10):")
    state_probs = []
    for s in range(2**n_qubits):
        bits = format(s, f'0{n_qubits}b')
        state_probs.append((bits, float(probs[s])))
    
    state_probs.sort(key=lambda x: x[1], reverse=True)
    for bits, prob in state_probs[:10]:
        n_sel = bits.count('1')
        bar = "█" * int(prob * 50)
        print(f"    |{bits}⟩: {prob:.4f} {bar} (selected={n_sel})")
    
    return best_params, best_energy, history, state_probs


# ================================================================
# TAHAP 6: HASIL & ANALISIS
# ================================================================

def analyze_results(state_probs, tickers, log_returns, exact_state, exact_energy, 
                    vqe_energy, history):
    """Analisis hasil VQE: seleksi aset, Sharpe Ratio, visualisasi."""
    print("\n" + "=" * 70)
    print("TAHAP 6: HASIL & ANALISIS")
    print("=" * 70)
    
    # 1. Identifikasi bitstring terbaik dengan tepat 2 aset
    best_bitstring = None
    best_prob = 0
    for bits, prob in state_probs:
        if bits.count('1') == 2 and prob > best_prob:
            best_bitstring = bits
            best_prob = prob
    
    if best_bitstring is None:
        print("  WARNING: Tidak ditemukan bitstring dengan tepat 2 aset!")
        best_bitstring = state_probs[0][0]
        best_prob = state_probs[0][1]
    
    selected_indices = [i for i, b in enumerate(best_bitstring) if b == '1']
    selected_assets = [tickers[i] for i in selected_indices]
    
    print(f"\n  Bitstring optimal: |{best_bitstring}⟩ (prob = {best_prob:.4f})")
    print(f"  Exact ground state: |{exact_state}⟩")
    print(f"  Match: {'✓ YES' if best_bitstring == exact_state else '✗ NO'}")
    print(f"\n  ★ ASET TERPILIH: {selected_assets}")
    
    # 2. Sharpe Ratio
    print(f"\n  Validasi Sharpe Ratio:")
    rf = 0.0  # risk-free rate
    
    # Sharpe untuk setiap pasangan
    all_pairs = list(combinations(range(len(tickers)), 2))
    sharpe_dict = {}
    for i, j in all_pairs:
        pair_return = (log_returns[tickers[i]] + log_returns[tickers[j]]) / 2
        mu = pair_return.mean() * 252  # annualized
        sigma = pair_return.std() * np.sqrt(252)
        sharpe = (mu - rf) / sigma if sigma > 0 else 0
        sharpe_dict[(i, j)] = sharpe
        selected_marker = " ★" if set([i, j]) == set(selected_indices) else ""
        print(f"    {tickers[i]} + {tickers[j]}: Sharpe = {sharpe:.4f}{selected_marker}")
    
    # 3. Energi comparison
    print(f"\n  Energi:")
    print(f"    VQE:   {vqe_energy:.6f}")
    print(f"    Exact: {exact_energy:.6f}")
    print(f"    Error: {abs(vqe_energy - exact_energy):.6f}")
    
    # 4. Visualisasi
    print("\n  Generating plots...")
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Plot 1: Konvergensi VQE
    ax1 = axes[0]
    ax1.plot(history, 'b-', alpha=0.6, linewidth=0.8)
    # Moving average
    window = 10
    if len(history) > window:
        ma = np.convolve(history, np.ones(window)/window, mode='valid')
        ax1.plot(range(window-1, len(history)), ma, 'r-', linewidth=2, label=f'MA-{window}')
    ax1.axhline(y=exact_energy, color='g', linestyle='--', label=f'Exact = {exact_energy:.4f}')
    ax1.set_xlabel('Iterasi SPSA')
    ax1.set_ylabel('Energi ⟨H⟩')
    ax1.set_title('Konvergensi VQE')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Distribusi State
    ax2 = axes[1]
    top_states = state_probs[:8]
    labels = [f"|{b}⟩" for b, _ in top_states]
    probs_plot = [p for _, p in top_states]
    colors = ['#2ecc71' if b.count('1') == 2 else '#e74c3c' for b, _ in top_states]
    ax2.bar(labels, probs_plot, color=colors, edgecolor='black', linewidth=0.5)
    ax2.set_xlabel('State')
    ax2.set_ylabel('Probabilitas')
    ax2.set_title('Distribusi State (hijau = 2 aset)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Plot 3: Sharpe Ratio semua pasangan
    ax3 = axes[2]
    pair_labels = [f"{tickers[i]}\n+\n{tickers[j]}" for i, j in all_pairs]
    sharpe_vals = [sharpe_dict[pair] for pair in all_pairs]
    colors_sharpe = ['#2ecc71' if set(pair) == set(selected_indices) else '#3498db' 
                     for pair in all_pairs]
    ax3.bar(pair_labels, sharpe_vals, color=colors_sharpe, edgecolor='black', linewidth=0.5)
    ax3.set_ylabel('Sharpe Ratio (annualized)')
    ax3.set_title('Sharpe Ratio per Pasangan Aset')
    ax3.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('econophysics_vqe_results.png', dpi=150, bbox_inches='tight')
    print(f"  Plot saved: econophysics_vqe_results.png")
    plt.show()
    
    return selected_assets, selected_indices


# ================================================================
# MAIN EXECUTION
# ================================================================

def main():
    print("╔" + "═" * 68 + "╗")
    print("║   ECONOPHYSICS KUANTUM: Portfolio Optimization via HE-VQE         ║")
    print("║   4 Aset Large Cap LQ45 → Seleksi 2 Terbaik                      ║")
    print("╚" + "═" * 68 + "╝")
    
    # === Konfigurasi ===
    tickers = ['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'UNVR.JK']
    K = 2           # Pilih 2 aset
    penalty_A = 10.0  # Konstanta penalti
    depth = 2        # Kedalaman ansatz
    maxiter = 500    # Iterasi SPSA
    n_shots = 1024   # Sampling shots
    seed = 42
    
    # TAHAP 1: Data
    data, log_returns, binary_states = download_stock_data(tickers, period="2y")
    
    # TAHAP 2: Risk Aversion + Payoff Matrix
    lambda_risk = compute_endogenous_lambda(log_returns, tickers)
    all_payoffs, all_counts, all_game_types = run_game_theory_analysis(
        log_returns, binary_states, tickers, lambda_risk
    )
    
    # TAHAP 3: Parameter Hamiltonian
    h, J, qmi_details = extract_hamiltonian_params(
        binary_states, all_payoffs, tickers
    )
    
    # TAHAP 4: Hamiltonian
    H, exact_state, exact_energy = build_hamiltonian(
        h, J, n_assets=len(tickers), K=K, penalty_A=penalty_A
    )
    
    # TAHAP 5: HE-VQE
    best_params, vqe_energy, history, state_probs = run_he_vqe(
        H, n_qubits=len(tickers), depth=depth, 
        maxiter=maxiter, n_shots=n_shots, seed=seed
    )
    
    # TAHAP 6: Analisis
    selected_assets, selected_indices = analyze_results(
        state_probs, tickers, log_returns, exact_state, exact_energy,
        vqe_energy, history
    )
    
    # === Ringkasan Akhir ===
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║                        RINGKASAN AKHIR                            ║")
    print("╠" + "═" * 68 + "╣")
    print(f"║  Aset Input:  {', '.join(tickers):<54}║")
    print(f"║  λ_market:    {lambda_risk:.4f} (endogen dari data){' ':<36}║")
    print(f"║  VQE Energy:  {vqe_energy:.6f}{' ':<46}║")
    print(f"║  Exact Energy: {exact_energy:.6f}{' ':<45}║")
    sel_str = f"{selected_assets[0]} & {selected_assets[1]}"
    print(f"║  ★ Terpilih:  {sel_str:<54}║")
    print("╚" + "═" * 68 + "╝")


if __name__ == "__main__":
    main()
