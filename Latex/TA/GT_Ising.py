# === Backtesting Engine: 2021 - 2023 (Monthly Rebalance, 3-Month Rolling Window) ===
# Metodologi berdasarkan Kombinasi_GT_Ising.pdf: Discrete Markowitz as Exact Potential Game
# dengan Normalized Mutual Information (NMI) dan VQE Warm-Start menggunakan Nash Equilibrium.

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
penalty_A = 5.0              # Pengali Lagrange (A) untuk H_penalty (lambda)
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
    Menghitung parameter risk-aversion (gamma) secara endogen berdasarkan
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
# 4. Helper: Strategic Returns & Information Matrix (NMI)
# =============================================================================
def compute_strategic_returns(log_rets, binary_st, tickers):
    """
    [Tugas 2: Perhitungan Imbal Hasil Strategis]
    Menghitung imbal hasil strategis (mu_tilde_i) sebagai jumlahan terbobot
    dari ekspektasi bersyarat pada 16 microstates sistem 4 aset.
    """
    n_assets = len(tickers)
    total_days = len(log_rets)
    mu_tilde = np.zeros(n_assets)
    
    # Kelompokkan return berdasarkan binary states (microstates) dari semua aset
    grouped = log_rets.groupby([binary_st[t] for t in tickers])
    
    for state, group in grouped:
        P_s = len(group) / total_days           # Probabilitas microstate P(s)
        R_bar_s = group[tickers].mean().values  # Ekspektasi return bersyarat R_bar_i(s)
        mu_tilde += P_s * R_bar_s               # Jumlahan terbobot
        
    return mu_tilde

def calc_shannon_entropy(st_A):
    """[Tugas 1] Menghitung entropi Shannon H(X) dari distribusi probabilitas biner."""
    p1 = np.mean(st_A)
    p0 = 1.0 - p1
    H = 0.0
    if p0 > 0: H -= p0 * np.log2(p0)
    if p1 > 0: H -= p1 * np.log2(p1)
    return H

def calc_classical_mutual_information(st_A, st_B):
    """[Tugas 1] Menghitung Classical Mutual Information I(X_i; X_j)."""
    n_ij = np.zeros((2, 2))
    for t in range(len(st_A)):
        n_ij[int(st_A[t]), int(st_B[t])] += 1
    
    prob_joint = n_ij / len(st_A)
    prob_A = prob_joint.sum(axis=1)
    prob_B = prob_joint.sum(axis=0)
    
    I_MI = 0.0
    for i in range(2):
        for j in range(2):
            if prob_joint[i, j] > 0:
                I_MI += prob_joint[i, j] * np.log2(prob_joint[i, j] / (prob_A[i] * prob_B[j]))
    return max(I_MI, 0.0)

def calc_NMI(st_A, st_B):
    """
    [Tugas 1] Menghitung Normalized Mutual Information (NMI) 
    menggunakan Upper Bound Theorem: NMI(i,j) = I(X_i:X_j) / sqrt(H(X_i)*H(X_j)).
    """
    I_AB = calc_classical_mutual_information(st_A, st_B)
    H_A = calc_shannon_entropy(st_A)
    H_B = calc_shannon_entropy(st_B)
    
    if H_A == 0 or H_B == 0:
        return 0.0
    
    return I_AB / np.sqrt(H_A * H_B)

# =============================================================================
# 5. Helper: Nash Equilibrium Search
# =============================================================================
def find_nash_equilibrium(h, J, N=4, K=2):
    """
    [Tugas 4: Pencarian Nash Equilibrium Klasik]
    Mengevaluasi energi potensial (Ising) klasik untuk kombinasi bitstring feasible.
    """
    best_energy = np.inf
    best_bitstring = None
    
    # Terdapat (N choose K) = 6 kombinasi feasible
    for combo in combinations(range(N), K):
        # Buat vektor solusi dalam {0, 1}
        x = np.zeros(N, dtype=int)
        for idx in combo:
            x[idx] = 1
            
        # Konversi x_i in {0,1} ke spin Z_i in {1, -1}
        Z = 1 - 2 * x 
        
        # Evaluasi energi Ising klasik untuk state tersebut
        E = 0.0
        for i in range(N):
            E += h[i] * Z[i]
            for j in range(i + 1, N):
                E += J[i, j] * Z[i] * Z[j]
                
        if E < best_energy:
            best_energy = E
            best_bitstring = "".join(str(bit) for bit in x)
            
    return best_bitstring, best_energy

# =============================================================================
# 6. Konstruksi Hamiltonian Total
# =============================================================================
def build_hamiltonian_total(h_total, J_total, n_assets):
    """
    Membangun operator Hamiltonian Ising dari parameter h_i dan J_ij.
    """
    coeffs = []
    obs    = []

    for i in range(n_assets):
        if abs(h_total[i]) > 1e-10:
            coeffs.append(float(h_total[i]))
            obs.append(qml.PauliZ(i))

    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J_total[i, j]) > 1e-10:
                coeffs.append(float(J_total[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))

    if len(coeffs) == 0:
        coeffs.append(0.0)
        obs.append(qml.Identity(0))

    return qml.Hamiltonian(coeffs, obs)

# =============================================================================
# 7. VQE dengan Adaptive Layer Selection & NE Warm-Start
# =============================================================================
def run_vqe_adaptive(H, n_qubits, ne_bitstring=None, K=2, max_depth=4,
                     maxiter=100, max_total_iter=2000,
                     batch_size=25, conv_window=4, conv_tol=1e-4,
                     seed=42):
    """
    Menjalankan VQE dengan seeding awal (warm-start) dari Nash Equilibrium.
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
        a, c      = 0.1, 0.1
        A_coeff   = maxiter * 0.1
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

            current_energy = float(cost_circuit(params))
            energy_history.append(current_energy)

            if total_iters >= maxiter and len(energy_history) >= conv_window:
                E_old = energy_history[-conv_window]
                E_now = energy_history[-1]
                rel_change = abs(E_old - E_now) / (abs(E_old) + 1e-12)
                if rel_change < conv_tol:
                    converged = True
                    break

        return params, energy_history[-1], energy_history, total_iters

    best_energy    = np.inf
    best_params    = None
    best_depth     = 1
    best_history   = []

    for depth in range(1, max_depth + 1):
        n_params = n_qubits * 2 * (depth + 1)
        cost_fn, prob_fn = make_circuit(depth)

        # Inisialisasi parameter: Warm-start
        if best_params is not None and len(best_params) < n_params:
            init_p = np.concatenate([
                best_params,
                rng.uniform(-0.1, 0.1, n_params - len(best_params))
            ])
        else:
            if ne_bitstring is not None:
                # [Tugas 5: VQE Warm-Start menggunakan NE]
                init_w = np.zeros((depth + 1, n_qubits, 2))
                for q in range(n_qubits):
                    bit = int(ne_bitstring[q])
                    if bit == 1:
                        init_w[0, q, 0] = np.pi # Parameter RY diinduksi dekat pi jika aset terpilih
                    else:
                        init_w[0, q, 0] = 0.0   # Parameter RY diinduksi dekat 0 jika tidak terpilih
                # Tambahkan noise acak secara keseluruhan (misal rentang ±0.1)
                init_p = init_w.flatten() + rng.uniform(-0.1, 0.1, n_params)
            else:
                init_p = rng.uniform(0, 2 * np.pi, n_params)

        params, energy, e_hist, n_iters = run_spsa(cost_fn, n_params, init_params=init_p)

        print(f"    [Depth {depth}] Konvergen dalam {n_iters} iterasi | E = {energy:.6f}")

        if energy < best_energy:
            best_energy  = energy
            best_params  = params
            best_depth   = depth
            best_history = e_hist
        else:
            break

    _, prob_fn = make_circuit(best_depth)
    probs = prob_fn(best_params)

    sorted_indices = np.argsort(probs)[::-1]
    best_bitstring = None
    for idx in sorted_indices:
        bs = format(idx, f'0{n_qubits}b')
        if bs.count('1') == K:
            best_bitstring = bs
            break

    if best_bitstring is None:
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
    Eksekusi satu periode pembelajaran.
    Mengimplementasikan formulasi objektif PDF.
    """
    n_assets = len(tickers)
    log_rets  = np.log(lookback_data / lookback_data.shift(1)).dropna()
    binary_st = (log_rets <= 0).astype(int)   # 1 = turun, 0 = naik

    # gamma disini mewakili degree of risk-aversion, yang diestimasi serupa endogenous lambda
    gamma = compute_endogenous_lambda(log_rets, tickers)
    lam = penalty_A # penalty lambda untuk pembatas kardinalitas
    
    # [Tugas 2] Perhitungan Imbal Hasil Strategis 
    mu_tilde = compute_strategic_returns(log_rets, binary_st, tickers)
    
    # [Tugas 1] Modifikasi Matriks Kovariansi dengan NMI
    cov_emp = log_rets.cov().values
    sigma_tilde = np.zeros((n_assets, n_assets))
    
    for i in range(n_assets):
        for j in range(n_assets):
            if i == j:
                sigma_tilde[i, i] = cov_emp[i, i]
            else:
                nmi_val = calc_NMI(binary_st[tickers[i]].values, binary_st[tickers[j]].values)
                # Formula penyusuaian kovariansi
                sigma_tilde[i, j] = cov_emp[i, j] * (1.0 + nmi_val)

    # [Tugas 3] Konstruksi Hamiltonian Ising (Pauli-Z) Sesuai PDF
    h_total = np.zeros(n_assets)
    J_total = np.zeros((n_assets, n_assets))

    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            # Formula kopling J_ij
            J_val = (gamma * sigma_tilde[i, j] + 2 * lam) / 4.0
            J_total[i, j] = J_val
            J_total[j, i] = J_val
            
    for i in range(n_assets):
        sum_J_ij = 0.0
        for j in range(n_assets):
            if i != j:
                sum_J_ij += (gamma * sigma_tilde[i, j] + 2 * lam) / 4.0
                
        # Formula bias lokal h_i
        h_total[i] = -0.5 * ((gamma / 2.0) * sigma_tilde[i, i] - mu_tilde[i] + lam * (1.0 - 2.0 * K)) - sum_J_ij

    # [Tugas 4] Pencarian Nash Equilibrium
    ne_bitstring, ne_energy = find_nash_equilibrium(h_total, J_total, N=n_assets, K=K)
    print(f"    [Nash Eq] Bitstring: {ne_bitstring} | Energy: {ne_energy:.6f}")

    H = build_hamiltonian_total(h_total, J_total, n_assets)
    
    # Optimasi VQE dengan adaptive depth
    selected_indices, depth_used, energy_final = run_vqe_adaptive(
        H, n_assets, ne_bitstring=ne_bitstring, K=K, max_depth=max_depth, maxiter=maxiter,
        max_total_iter=max_total_iter, batch_size=batch_size,
        conv_window=conv_window, conv_tol=conv_tol
    )

    return selected_indices, depth_used, energy_final

# =============================================================================
# 9. Fungsi Metrik Evaluasi Finansial
# =============================================================================
def compute_metrics(value_series, initial_capital, label=""):
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
    total_value    = current_cash + np.sum(current_holdings * prices)
    target_values  = total_value * target_weights
    new_holdings   = current_holdings.copy()
    new_cash       = current_cash

    for j in range(N):
        c_val = new_holdings[j] * prices[j]
        if c_val > target_values[j]:
            sell_val        = c_val - target_values[j]
            new_cash       += sell_val
            new_holdings[j] -= sell_val / prices[j]

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

    target_w_bench = np.full(N, 1.0 / N)
    current_prices = data_clean.iloc[curr_idx].values

    cash_vqe, holdings_vqe = rebalance_portfolio(
        cash_vqe, holdings_vqe, target_w_vqe, current_prices
    )

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

    start_d = curr_idx if i == 0 else curr_idx + 1
    for d in range(start_d, next_idx):
        prices = data_clean.iloc[d].values
        value_vqe.append(cash_vqe + np.sum(holdings_vqe * prices))
        value_bench.append(cash_bench + np.sum(holdings_bench * prices))
        for j, t in enumerate(tickers):
            value_assets[t].append(cash_assets[t] + holdings_assets[t] * prices[j])

print("\nBacktesting Selesai.")

tr_vqe,   sr_vqe,   mdd_vqe   = compute_metrics(value_vqe,   initial_capital, "Quantum Exact Potential Game (VQE)")
tr_bench, sr_bench, mdd_bench = compute_metrics(value_bench, initial_capital, "Buy & Hold Equal Weight")
for t in tickers:
    compute_metrics(value_assets[t], initial_capital, f"Buy & Hold {t}")

# =============================================================================
# 11. Visualisasi Pertumbuhan Portofolio
# =============================================================================
plt.figure(figsize=(14, 7))

dates = data_clean.index

plt.plot(dates[:len(value_vqe)],   value_vqe,
         label=f'Quantum Exact Potential Game VQE (K={K})',
         linewidth=2.5, color='blue')

plt.plot(dates[:len(value_bench)], value_bench,
         label='Buy & Hold Benchmark (Equal Weight)',
         linewidth=2.5, color='black', linestyle='--')

colors = ['red', 'green', 'orange', 'purple']
for j, t in enumerate(tickers):
    plt.plot(dates[:len(value_assets[t])], value_assets[t],
             label=f'Buy & Hold {t}', color=colors[j], alpha=0.6)

plt.title(
    'Simulasi Backtesting Kinerja Portofolio Kuantum (2021–2023)\n'
    'Metodologi: Exact Potential Game + NMI + Nash Equilibrium Warm-Start'
)
plt.ylabel('Ekuitas Portofolio (Rupiah)')
plt.xlabel('Tanggal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('backtest_result.png', dpi=150)
plt.show()
print("\nGrafik disimpan sebagai backtest_result.png")
