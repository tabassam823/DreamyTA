# === Backtesting Engine: 2021 - 2023 (Monthly Rebalance, 3-Month Rolling Window) ===
# Metodologi sesuai Bab-3.tex (Alur Penelitian) dan bab10.tex (Contoh Perhitungan)

import yfinance as yf
import pennylane as qml
from pennylane import numpy as pnp
import numpy as np
import pandas as pd
import scipy.linalg as la
import matplotlib.pyplot as plt
from itertools import combinations
import warnings

warnings.filterwarnings('ignore')

print("Starting Setup for Backtesting (2021-2023)...")

# =============================================================================
# 1. Konfigurasi
# =============================================================================
tickers = ['DUK', 'MSFT', 'CVX', 'TSLA']
N       = len(tickers)       # Jumlah aset kandidat
K       = 2                  # Jumlah aset target portofolio
penalty_A = 5.0              # Pengali Lagrange (A) untuk H_penalty
max_depth = 4                # Kedalaman maksimum ansatz (adaptive)
maxiter   = 100              # Iterasi SPSA per depth-level

# Parameter Kalender
initial_capital = 100_000_000.0
lookback_days  = 63   # ~3 bulan perdagangan
rebalance_days = 21   # ~1 bulan perdagangan

# =============================================================================
# 2. Download Data
# =============================================================================
data = yf.download(tickers, start="2020-09-01", end="2024-01-01", progress=False)['Close']
data = data.dropna()
data_clean = data.sort_index()

print(f"Data Berhasil Diunduh. Total hari observasi: {len(data_clean)}")

# =============================================================================
# 3. Helper: Endogenous Lambda (Risk-Aversion Parameter)
# =============================================================================
def compute_endogenous_lambda(log_returns, tickers):
    """
    Menghitung parameter risk-aversion lambda secara endogen berdasarkan
    Sharpe Ratio rata-rata lintas aset, menggunakan fungsi sigmoid/logistik.
    """
    mu_annual    = log_returns[tickers].mean() * 252
    sigma_annual = log_returns[tickers].std()  * np.sqrt(252)
    mu_avg    = abs(mu_annual).mean()
    sigma_avg = sigma_annual.mean()
    if np.isnan(mu_avg) or np.isnan(sigma_avg) or (mu_avg + sigma_avg) == 0:
        return 0.5
    Z = mu_avg / sigma_avg   # Sharpe Ratio agregat
    return 1.0 / (1.0 + np.exp(Z))

# =============================================================================
# 4. Helper: Payoff Matrix & Bias h_i (Game Theory)
# =============================================================================
def calc_payoff(ret_A, ret_B, st_A, st_B, lam):
    """
    Menghitung matriks payoff 2x2 untuk pasangan aset (A, B).
    
    Utilitas setiap hari: u_i(t) = (1-lam)*r_i(t)*252 - lam*|r_i(t)*252|
    Payoff dirata-ratakan per konfigurasi biner (s_A, s_B).
    """
    pA     = np.zeros((2, 2))
    pB     = np.zeros((2, 2))
    counts = np.zeros((2, 2))

    for t in range(len(st_A)):
        s, r  = int(st_A[t]), int(st_B[t])
        u_A   = (1 - lam) * (ret_A[t] * 252) - lam * abs(ret_A[t] * 252)
        u_B   = (1 - lam) * (ret_B[t] * 252) - lam * abs(ret_B[t] * 252)
        counts[s, r] += 1
        pA[s, r]     += u_A
        pB[s, r]     += u_B

    for s in range(2):
        for r in range(2):
            if counts[s, r] > 0:
                pA[s, r] /= counts[s, r]
                pB[s, r] /= counts[s, r]
    return pA, pB


def compute_bias_GT(pA, pB):
    """
    Menghitung bias lokal h_i^GT berdasarkan selisih expected payoff:
        h_A^GT = (E[pA | s_A=+1] - E[pA | s_A=-1]) / 2
        h_B^GT = (E[pB | s_B=+1] - E[pB | s_B=-1]) / 2

    Sesuai bab10.tex §3 (Pencarian Bias Lokal melalui Game Theory).
    s=+1 (naik)  → baris/kolom indeks 0  (state biner 0 ≡ |0⟩)
    s=-1 (turun) → baris/kolom indeks 1  (state biner 1 ≡ |1⟩)

    E[pA | s_A=+1] = rata-rata baris 0 → (pA[0,0] + pA[0,1]) / 2
    E[pA | s_A=-1] = rata-rata baris 1 → (pA[1,0] + pA[1,1]) / 2
    """
    E_A_up   = (pA[0, 0] + pA[0, 1]) / 2.0
    E_A_down = (pA[1, 0] + pA[1, 1]) / 2.0
    h_A_GT   = (E_A_up - E_A_down) / 2.0

    E_B_up   = (pB[0, 0] + pB[1, 0]) / 2.0
    E_B_down = (pB[0, 1] + pB[1, 1]) / 2.0
    h_B_GT   = (E_B_up - E_B_down) / 2.0

    return h_A_GT, h_B_GT

# =============================================================================
# 5. Helper: QMI & Kopling J_ij (Quantum Mutual Information)
# =============================================================================
def von_neumann_entropy(rho):
    """Von Neumann entropy S(rho) = -Tr(rho log rho) untuk density matrix diagonal."""
    eig = np.real(la.eigvalsh(rho))
    eig = eig[eig > 1e-12]
    return -np.sum(eig * np.log(eig))


def calc_qmi(st_A, st_B):
    """
    Menghitung Quantum Mutual Information (QMI) antara dua aset:
        I(A:B) = S(rho_A) + S(rho_B) - S(rho_AB)
    
    Density matrix dibangun dari distribusi probabilitas joint biner
    dengan Laplace smoothing (pseudocount +1) untuk stabilitas numerik.
    Sesuai bab10.tex §4 dan Appendix QMI.
    """
    n_ij = np.zeros((2, 2))
    for t in range(len(st_A)):
        n_ij[int(st_A[t]), int(st_B[t])] += 1

    # Distribusi probabilitas joint dengan Laplace smoothing
    prob_joint = (n_ij + 1.0) / (len(st_A) + 4.0)

    # Density matrices marginal dan joint (diagonal → separable basis)
    rho_AB = np.diag(prob_joint.flatten())
    rho_A  = np.diag(prob_joint.sum(axis=1))
    rho_B  = np.diag(prob_joint.sum(axis=0))

    I_QMI = von_neumann_entropy(rho_A) + von_neumann_entropy(rho_B) - von_neumann_entropy(rho_AB)
    return max(I_QMI, 0.0)   # QMI ≥ 0 secara definisi


def compute_coupling_QMI(qmi_val, rho_corr, T_market, k_B=1.0):
    """
    Menghitung kopling informasional J_ij^QMI:
        alpha     = k_B * T_market   (k_B = 1 sesuai konvensi Econophysics)
        J_ij^QMI = alpha * sgn(rho_corr) * sqrt(I_QMI)

    Sesuai bab10.tex §4 (Kopling Informasi melalui Quantum Mutual Information).
    Tanda kopling ditentukan oleh korelasi Pearson empiris rho_corr.
    """
    alpha  = k_B * T_market
    sign   = np.sign(rho_corr) if not np.isnan(rho_corr) else 1.0
    return alpha * sign * np.sqrt(qmi_val)

# =============================================================================
# 6. Konstruksi Hamiltonian Total
# =============================================================================
def build_hamiltonian_total(h_total, J_total, n_assets):
    """
    Membangun operator Hamiltonian Ising dari parameter TOTAL yang sudah
    menggabungkan kontribusi Game Theory dan Penalty:
        H = sum_i h_total[i] * Z_i + sum_{i<j} J_total[i,j] * Z_i Z_j

    Parameter h_total dan J_total sudah mengandung:
        h_total[i]   = h_i^GT   + h_i^pen
        J_total[i,j] = J_ij^QMI + J_ij^pen

    Sesuai bab10.tex §5 (Sintesis Hamiltonian Akhir).
    """
    coeffs = []
    obs    = []

    # Suku linear: h_i * Z_i
    for i in range(n_assets):
        if abs(h_total[i]) > 1e-10:
            coeffs.append(float(h_total[i]))
            obs.append(qml.PauliZ(i))

    # Suku kuadratik: J_ij * Z_i Z_j
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J_total[i, j]) > 1e-10:
                coeffs.append(float(J_total[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))

    # Fallback agar Hamiltonian tidak kosong
    if len(coeffs) == 0:
        coeffs.append(0.0)
        obs.append(qml.Identity(0))

    return qml.Hamiltonian(coeffs, obs)

# =============================================================================
# 7. VQE dengan Adaptive Layer Selection (EfficientSU(2) + SPSA)
# =============================================================================
def run_vqe_adaptive(H, n_qubits, K=2, max_depth=4,
                     maxiter=100, max_total_iter=2000,
                     batch_size=25, conv_window=4, conv_tol=1e-4,
                     seed=42):
    """
    Menjalankan VQE dengan dua mekanisme adaptif:

    (A) Adaptive SPSA Iterations (konvergensi otomatis):
        - SPSA dijalankan dalam batch kecil (``batch_size`` iterasi per batch).
        - Setelah setiap batch, evaluasi energi disimpan ke ``energy_history``.
        - Konvergensi terdeteksi jika relative change energi pada jendela
          ``conv_window`` batch terakhir di bawah ``conv_tol``:
              |E_{t-w} - E_t| / (|E_{t-w}| + eps) < conv_tol
        - Berhenti otomatis saat konvergen atau ``max_total_iter`` tercapai.
        - ``maxiter`` hanya digunakan sebagai batas bawah (minimal iterasi
          awal sebelum cek konvergensi dimulai).

    (B) Adaptive Layer Selection (sesuai flowchart Bab-3.tex):
        - Mulai dari depth=1; setelah SPSA konvergen, evaluasi E_L.
        - Tambah layer jika E_L < E_{L-1} (penurunan energi signifikan).
        - Berhenti jika energi tidak turun atau ``max_depth`` tercapai.

    Ansatz: EfficientSU(2) manual → lapisan RY-RZ dengan entanglement CNOT ring.
    Optimizer: SPSA dengan parameter standar (a=0.1, c=0.1, alpha=0.602, gamma=0.101).
    """
    dev = qml.device("default.qubit", wires=n_qubits)
    rng = np.random.default_rng(seed)

    def make_circuit(depth):
        @qml.qnode(dev)
        def cost_circuit(params):
            w = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(w[layer, q, 0], wires=q)
                    qml.RZ(w[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])
            return qml.expval(H)

        @qml.qnode(dev)
        def prob_circuit(params):
            w = params.reshape((depth + 1, n_qubits, 2))
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    qml.RY(w[layer, q, 0], wires=q)
                    qml.RZ(w[layer, q, 1], wires=q)
                if layer < depth:
                    for q in range(n_qubits - 1):
                        qml.CNOT(wires=[q, q + 1])
                    qml.CNOT(wires=[n_qubits - 1, 0])
            return qml.probs(wires=range(n_qubits))

        return cost_circuit, prob_circuit

    def run_spsa(cost_circuit, n_params, init_params=None):
        """
        Menjalankan SPSA dengan adaptive convergence detection.

        Iterasi dibagi menjadi batch kecil (``batch_size``). Setelah setiap
        batch selesai, energi dievaluasi dan disimpan ke ``energy_history``.
        Konvergensi dianggap tercapai apabila memenuhi SALAH SATU kondisi:
            (1) Total iterasi >= ``max_total_iter``, atau
            (2) Setelah minimal ``maxiter`` iterasi, relative energy change
                dalam jendela ``conv_window`` batch terakhir < ``conv_tol``:
                    |E_{hist[-w]} - E_{hist[-1]}| / (|E_{hist[-w]}| + 1e-12)
                    < conv_tol

        Return:
            params        (np.ndarray): Parameter optimal hasil SPSA
            final_energy  (float)     : Energi terakhir saat konvergen
            energy_history (list)     : Energi per-batch untuk diagnostik
            total_iters   (int)       : Total iterasi yang digunakan
        """
        a, c      = 0.1, 0.1
        A_coeff   = maxiter * 0.1    # A mengacu pada ``maxiter`` awal sebagai referensi skala
        alpha_exp = 0.602
        gamma_exp = 0.101

        if init_params is not None:
            params = init_params.copy()
        else:
            params = rng.uniform(0, 2 * np.pi, n_params)

        energy_history = []
        total_iters    = 0
        converged      = False

        while total_iters < max_total_iter:
            # --- Satu batch SPSA ---
            for _ in range(batch_size):
                k     = total_iters
                a_k   = a / (A_coeff + k + 1) ** alpha_exp
                c_k   = c / (k + 1)           ** gamma_exp
                delta = 2 * rng.integers(0, 2, size=n_params) - 1

                cost_plus  = float(cost_circuit(params + c_k * delta))
                cost_minus = float(cost_circuit(params - c_k * delta))
                grad       = (cost_plus - cost_minus) / (2 * c_k * delta)
                params     = params - a_k * grad
                total_iters += 1

            # --- Evaluasi energi setelah batch selesai ---
            current_energy = float(cost_circuit(params))
            energy_history.append(current_energy)

            # --- Cek konvergensi (hanya setelah minimal maxiter iterasi) ---
            if total_iters >= maxiter and len(energy_history) >= conv_window:
                E_old = energy_history[-conv_window]
                E_now = energy_history[-1]
                rel_change = abs(E_old - E_now) / (abs(E_old) + 1e-12)
                if rel_change < conv_tol:
                    converged = True
                    break

        return params, energy_history[-1], energy_history, total_iters

    # --- Adaptive Layer Loop ---
    best_energy    = np.inf
    best_params    = None
    best_depth     = 1
    best_history   = []

    for depth in range(1, max_depth + 1):
        n_params = n_qubits * 2 * (depth + 1)
        cost_fn, prob_fn = make_circuit(depth)

        # Inisialisasi: warm-start dari parameter depth sebelumnya jika ada
        if best_params is not None and len(best_params) < n_params:
            init_p = np.concatenate([
                best_params,
                rng.uniform(0, 2 * np.pi, n_params - len(best_params))
            ])
        else:
            init_p = None

        params, energy, e_hist, n_iters = run_spsa(cost_fn, n_params, init_params=init_p)

        print(f"    [Depth {depth}] Konvergen dalam {n_iters} iterasi | E = {energy:.6f}")

        if energy < best_energy:
            best_energy  = energy
            best_params  = params
            best_depth   = depth
            best_history = e_hist
        else:
            # Energi tidak turun → berhenti menambah layer
            break

    # Evaluasi probabilitas pada depth terbaik
    _, prob_fn = make_circuit(best_depth)
    probs = prob_fn(best_params)

    # Pilih bitstring dengan tepat K qubit = 1 dan probabilitas tertinggi
    sorted_indices = np.argsort(probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break

    if best_bitstring is None:
        # Fallback: pilih K indeks dengan probabilitas tertinggi
        best_bitstring = '0' * n_qubits
        top_k = np.argsort(probs)[-K:]
        bs_list = list('0' * n_qubits)
        for idx in top_k:
            bs_list[idx] = '1'
        best_bitstring = ''.join(bs_list)

    selected_indices = [i for i, bit in enumerate(best_bitstring) if bit == '1']
    return selected_indices, best_depth, best_energy

# =============================================================================
# 8. Pipeline Strategi Per Rebalancing Step
# =============================================================================
def run_strategy_step(lookback_data, tickers, K=2, penalty_A=5.0,
                      max_depth=4, maxiter=100,
                      max_total_iter=2000, batch_size=25,
                      conv_window=4, conv_tol=1e-4):
    """
    Pipeline lengkap sesuai Bab-3.tex:
      1. Log return & binerisasi state
      2. Hitung lambda endogen
      3. Bangun payoff matrix → h_i^GT (Game Theory)
      4. Hitung QMI → J_ij^QMI (dengan scaling alpha = T_market)
      5. Hitung parameter penalti: h_i^pen dan J_ij^pen (bab10.tex §2)
      6. Susun parameter total: h_total, J_total
      7. Bangun Hamiltonian total
      8. Optimasi VQE adaptif (SPSA + adaptive layers)
    """
    n_assets = len(tickers)
    log_rets  = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_st = (log_rets <= 0).astype(int)   # 1 = turun (|1⟩), 0 = naik (|0⟩)

    lam = compute_endogenous_lambda(log_rets, tickers)

    # ------------------------------------------------------------------
    # Step 3: Payoff Matrix dan Bias h_i^GT
    # ------------------------------------------------------------------
    all_payoffs = {}
    for idx_a, idx_b in combinations(range(n_assets), 2):
        a, b = tickers[idx_a], tickers[idx_b]
        pA, pB = calc_payoff(
            log_rets[a].values, log_rets[b].values,
            binary_st[a].values, binary_st[b].values, lam
        )
        all_payoffs[(idx_a, idx_b)] = (pA, pB)

    # Akumulasi h_GT per aset dari semua pair yang melibatkannya
    h_GT     = np.zeros(n_assets)
    h_counts = np.zeros(n_assets)
    for (idx_a, idx_b), (pA, pB) in all_payoffs.items():
        h_a, h_b = compute_bias_GT(pA, pB)
        h_GT[idx_a]     += h_a
        h_GT[idx_b]     += h_b
        h_counts[idx_a] += 1
        h_counts[idx_b] += 1

    for i in range(n_assets):
        if h_counts[i] > 0:
            h_GT[i] /= h_counts[i]

    # ------------------------------------------------------------------
    # Step 4: QMI & Kopling J_ij^QMI
    # ------------------------------------------------------------------
    # T_market = rata-rata varians log return (konvensi Econophysics, k_B=1)
    var_daily  = log_rets[tickers].var().values
    T_market   = var_daily.mean()
    if T_market < 1e-12:
        T_market = 1e-6

    J_QMI = np.zeros((n_assets, n_assets))
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            qmi_val  = calc_qmi(binary_st[tickers[i]].values,
                                binary_st[tickers[j]].values)
            # Korelasi empiris untuk menentukan tanda kopling
            rho_corr = np.corrcoef(log_rets[tickers[i]].values,
                                   log_rets[tickers[j]].values)[0, 1]
            j_val = compute_coupling_QMI(qmi_val, rho_corr, T_market)
            J_QMI[i, j] = j_val
            J_QMI[j, i] = j_val

    # ------------------------------------------------------------------
    # Step 5: Parameter Penalti (bab10.tex §2)
    #   K' = N/2 - K
    #   h_i^pen = -A * K'
    #   J_ij^pen = A / 2
    # ------------------------------------------------------------------
    K_prime   = (n_assets / 2.0) - K
    h_pen     = -penalty_A * K_prime           # Skalar (sama untuk semua i)
    J_pen_val =  penalty_A / 2.0              # Skalar (sama untuk semua i,j)

    h_pen_vec  = np.full(n_assets, h_pen)
    J_pen_mat  = np.zeros((n_assets, n_assets))
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            J_pen_mat[i, j] = J_pen_val
            J_pen_mat[j, i] = J_pen_val

    # ------------------------------------------------------------------
    # Step 6: Parameter Total
    # ------------------------------------------------------------------
    h_total = h_GT    + h_pen_vec
    J_total = J_QMI   + J_pen_mat

    # ------------------------------------------------------------------
    # Step 7 & 8: Bangun Hamiltonian & Optimasi VQE
    # ------------------------------------------------------------------
    H = build_hamiltonian_total(h_total, J_total, n_assets)
    selected_indices, depth_used, energy_final = run_vqe_adaptive(
        H, n_assets, K=K, max_depth=max_depth, maxiter=maxiter,
        max_total_iter=max_total_iter, batch_size=batch_size,
        conv_window=conv_window, conv_tol=conv_tol
    )

    return selected_indices, depth_used, energy_final

# =============================================================================
# 9. Fungsi Metrik Evaluasi Finansial
# =============================================================================
def compute_metrics(value_series, initial_capital, label=""):
    """
    Menghitung metrik evaluasi finansial standar:
        - Total Return (%)
        - Annualized Sharpe Ratio
        - Maximum Drawdown (MDD) (%)
    """
    vals   = np.array(value_series)
    rets   = np.diff(vals) / vals[:-1]

    total_return = (vals[-1] - initial_capital) / initial_capital * 100.0

    if len(rets) > 0 and rets.std() > 1e-12:
        sharpe = (rets.mean() / rets.std()) * np.sqrt(252)
    else:
        sharpe = 0.0

    peak = np.maximum.accumulate(vals)
    dd   = (peak - vals) / peak
    mdd  = dd.max() * 100.0

    print(f"\n{'='*50}")
    print(f"  Metrik Kinerja: {label}")
    print(f"{'='*50}")
    print(f"  Total Return   : {total_return:+.2f}%")
    print(f"  Sharpe Ratio   : {sharpe:.4f}")
    print(f"  Max Drawdown   : {mdd:.2f}%")
    print(f"{'='*50}")
    return total_return, sharpe, mdd

# =============================================================================
# 10. MAIN BACKTEST LOOP
# =============================================================================
start_bt_date    = pd.to_datetime('2021-01-04')
start_idx        = np.searchsorted(data_clean.index, start_bt_date)
rebalance_indices = range(start_idx, len(data_clean), rebalance_days)

# Tracking Array
value_vqe   = [initial_capital] * start_idx
value_bench = [initial_capital] * start_idx
value_assets = {t: [initial_capital] * start_idx for t in tickers}

holdings_vqe, holdings_bench = np.zeros(N), np.zeros(N)
cash_vqe, cash_bench = initial_capital, initial_capital
cash_assets    = {t: initial_capital for t in tickers}
holdings_assets = {t: 0.0 for t in tickers}

print(f"\n--- Memulai Backtest dari {data_clean.index[start_idx].date()} "
      f"hingga {data_clean.index[-1].date()} ---")

def rebalance_portfolio(current_cash, current_holdings, target_weights, prices):
    """Eksekusi rebalancing portofolio tanpa biaya transaksi."""
    total_value    = current_cash + np.sum(current_holdings * prices)
    target_values  = total_value * target_weights
    new_holdings   = current_holdings.copy()
    new_cash       = current_cash

    # Jual aset berlebih terlebih dahulu
    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val > target_values[j]:
            sell_val        = c_val - target_values[j]
            new_cash       += sell_val
            new_holdings[j] -= sell_val / prices[j]

    # Kemudian beli aset yang kurang
    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val < target_values[j]:
            buy_val       = min(target_values[j] - c_val, new_cash)
            new_cash     -= buy_val
            new_holdings[j] += buy_val / prices[j]

    return new_cash, new_holdings


for i, curr_idx in enumerate(rebalance_indices):
    curr_date      = data_clean.index[curr_idx]
    train_start    = max(0, curr_idx - lookback_days)
    train_data     = data_clean.iloc[train_start:curr_idx]

    next_idx = (rebalance_indices[i + 1]
                if i + 1 < len(rebalance_indices)
                else len(data_clean))

    # --- Alokasi VQE ---
    selected_indices, depth_used, energy_final = run_strategy_step(
        train_data, tickers, K=K, penalty_A=penalty_A,
        max_depth=max_depth, maxiter=maxiter
    )
    selected_names = [tickers[idx] for idx in selected_indices]
    print(f"[{curr_date.date()}] VQE Terpilih: {selected_names} "
          f"| Depth: {depth_used} | E_min: {energy_final:.6f}")

    target_w_vqe = np.zeros(N)
    if len(selected_indices) > 0:
        w = 1.0 / len(selected_indices)
        for idx in selected_indices:
            target_w_vqe[idx] = w

    # --- Benchmark: Buy & Hold Equal Weight ---
    target_w_bench = np.full(N, 1.0 / N)

    current_prices = data_clean.iloc[curr_idx].values

    # Rebalance VQE (setiap bulan)
    cash_vqe, holdings_vqe = rebalance_portfolio(
        cash_vqe, holdings_vqe, target_w_vqe, current_prices
    )

    # Benchmark & Single Asset: hanya di awal periode
    if i == 0:
        cash_bench, holdings_bench = rebalance_portfolio(
            cash_bench, holdings_bench, target_w_bench, current_prices
        )
        for j, t in enumerate(tickers):
            target_w_indiv = np.zeros(N)
            target_w_indiv[j] = 1.0
            c_t, h_t = rebalance_portfolio(
                cash_assets[t], np.zeros(N), target_w_indiv, current_prices
            )
            cash_assets[t]    = c_t
            holdings_assets[t] = h_t[j]

    # --- Mark to Market ---
    start_d = curr_idx if i == 0 else curr_idx + 1
    for d in range(start_d, next_idx):
        prices = data_clean.iloc[d].values
        value_vqe.append(cash_vqe + np.sum(holdings_vqe * prices))
        value_bench.append(cash_bench + np.sum(holdings_bench * prices))
        for j, t in enumerate(tickers):
            value_assets[t].append(cash_assets[t] + holdings_assets[t] * prices[j])

print("\nBacktesting Selesai.")

# =============================================================================
# 11. Evaluasi Metrik Kinerja
# =============================================================================
tr_vqe,   sr_vqe,   mdd_vqe   = compute_metrics(value_vqe,   initial_capital, "QBGT VQE (Adaptive Layers)")
tr_bench, sr_bench, mdd_bench = compute_metrics(value_bench, initial_capital, "Buy & Hold Equal Weight")
for t in tickers:
    compute_metrics(value_assets[t], initial_capital, f"Buy & Hold {t}")

# =============================================================================
# 12. Visualisasi Pertumbuhan Portofolio
# =============================================================================
plt.figure(figsize=(14, 7))

dates = data_clean.index

plt.plot(dates[:len(value_vqe)],   value_vqe,
         label=f'QBGT VQE SPSA Adaptive (K={K})',
         linewidth=2.5, color='blue')

plt.plot(dates[:len(value_bench)], value_bench,
         label='Buy & Hold Benchmark (Equal Weight)',
         linewidth=2.5, color='black', linestyle='--')

colors = ['red', 'green', 'orange', 'purple']
for j, t in enumerate(tickers):
    plt.plot(dates[:len(value_assets[t])], value_assets[t],
             label=f'Buy & Hold {t}', color=colors[j], alpha=0.6)

plt.title(
    'Simulasi Backtesting Kinerja Portofolio Ekonomi Kuantum (2021–2023)\n'
    'Metodologi: Game Theory + QMI Hamiltonian + VQE Adaptive Layers'
)
plt.ylabel('Ekuitas Portofolio (Rupiah)')
plt.xlabel('Tanggal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('backtest_result.png', dpi=150)
plt.show()
print("\nGrafik disimpan sebagai backtest_result.png")
