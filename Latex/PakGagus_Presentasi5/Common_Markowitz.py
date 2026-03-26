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
# 4. Solusi Klasik Brute-Force (Warm-Start)
# =============================================================================
def find_classical_markowitz_solution(h, J, N=4, K=2):
    """
    Mencari solusi optimum klasikal secara brute-force untuk warm-start VQE.
    Iterasi pada C(N, K) kombinasi feasible.
    """
    best_energy = float('inf')
    best_state = None
    
    # Kombinasi posisi aset yang dibeli (s=-1 untuk dibeli, s=1 untuk tidak dibeli)
    # Catatan: Variabel x = (1 - s)/2, maka jika x = 1 (dibeli) -> s = -1, jika x = 0 (tidak dibeli) -> s = 1.
    for indices in combinations(range(N), K):
        s = np.ones(N)  # Semua tidak dibeli (x=0 -> s=1)
        for idx in indices:
            s[idx] = -1 # Aset yang dibeli (x=1 -> s=-1)
            
        # Hitung energi model Ising klasik: E = sum(h_i * s_i) + sum(J_ij * s_i * s_j)
        energy = 0.0
        for i in range(N):
            energy += h[i] * s[i]
            for j in range(i + 1, N):
                energy += J[i, j] * s[i] * s[j]

        if energy < best_energy:
            # Toleransi numerik untuk mencegah overwriting berlebih akibat presisi float
            if abs(energy - best_energy) > 1e-10 or best_state is None:
                best_energy = float(energy)
                best_state = s.copy()
            
    return best_state, best_energy

# =============================================================================
# 5. Konstruksi Hamiltonian Markowitz QUBO
# =============================================================================
def build_markowitz_hamiltonian(h, J, n_assets):
    """
    Membangun operator Hamiltonian Ising murni dari parameter h_i dan J_ij Markowitz:
        H = sum_i h[i] * Z_i + sum_{i<j} J[i,j] * Z_i Z_j
    """
    coeffs = []
    obs    = []

    # Suku linear: h_i * Z_i
    for i in range(n_assets):
        if abs(h[i]) > 1e-10:
            coeffs.append(float(h[i]))
            obs.append(qml.PauliZ(i))

    # Suku kuadratik: J_ij * Z_i Z_j
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            if abs(J[i, j]) > 1e-10:
                coeffs.append(float(J[i, j]))
                obs.append(qml.PauliZ(i) @ qml.PauliZ(j))

    # Fallback agar Hamiltonian tidak kosong
    if len(coeffs) == 0:
        coeffs.append(0.0)
        obs.append(qml.Identity(0))

    return qml.Hamiltonian(coeffs, obs)

# =============================================================================
# 6. VQE dengan Adaptive Layer Selection & Warm-Start
# =============================================================================
def run_vqe_adaptive(H, n_qubits, classical_state, K=2, max_depth=4,
                     maxiter=100, max_total_iter=2000,
                     batch_size=25, conv_window=4, conv_tol=1e-4,
                     seed=42):
    """
    Menjalankan VQE dengan dua mekanisme adaptif:
    - Adaptive SPSA Iterations untuk konvergensi otomatis
    - Adaptive Layer Selection 

    Inisialisasi (Warm-Start):
    Menggunakan `classical_state` murni untuk menginisialisasi rotasi RY.
    Jika state = -1 (beli), m=1 -> diinisialisasi ~ pi.
    Jika state = 1 (tidak beli), m=0 -> diinisialisasi ~ 0.
    Ditambahkan noise acak +/- 0.1.
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

        if best_params is not None and len(best_params) < n_params:
            init_p = np.concatenate([
                best_params,
                rng.uniform(0, 2 * np.pi, n_params - len(best_params))
            ])
        else:
            # Warm-start dari classical solution murni Markowitz
            angles = []
            for layer in range(depth + 1):
                for q in range(n_qubits):
                    if classical_state[q] == -1:
                        # Beli (x=1 -> s=-1 -> angle ~ pi +/- 0.1 noise)
                        angles.append(np.pi + rng.uniform(-0.1, 0.1)) # RY
                    else:
                        # Tidak beli (x=0 -> s=1 -> angle ~ 0 +/- 0.1 noise)
                        angles.append(0.0 + rng.uniform(-0.1, 0.1))   # RY
                    angles.append(rng.uniform(-0.1, 0.1))             # RZ
            init_p = np.array(angles)

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
# 7. Pipeline Strategi Per Rebalancing Step
# =============================================================================
def run_strategy_step(lookback_data, tickers, K=2, penalty_A=5.0,
                      max_depth=4, maxiter=100,
                      max_total_iter=2000, batch_size=25,
                      conv_window=4, conv_tol=1e-4):
    """
    Pipeline Markowitz/QUBO murni:
      1. Hitung annual returns & annual covariance secara standar (histori).
      2. Hitung parameter risk aversion: lambda endogen.
      3. Dapatkan parameter interaksi Ising (h_i, J_ij) langsung dengan derivasi Markowitz QUBO.
      4. Cari solusi klasik murni untuk warm-start.
      5. Optimasi VQE adaptif dengan inisialisasi tersebut.
    """
    n_assets = len(tickers)
    
    # Hitung log returns digunakan hanya untuk mengestimasi rata-rata Sharpe limit bagi endogenous lambda
    log_rets = np.log(lookback_data / lookback_data.shift(1)).dropna()
    lam = compute_endogenous_lambda(log_rets, tickers)
    
    # ------------------------------------------------------------------
    # Step 1: Hitung Imbal Hasil & Risiko Tahunan Standar Murni
    # ------------------------------------------------------------------
    returns_pct = lookback_data.pct_change().dropna()
    annual_returns = returns_pct.mean() * 252
    annual_covariance = returns_pct.cov() * 252
    
    mu_annual = annual_returns.values
    cov_annual = annual_covariance.values

    # ------------------------------------------------------------------
    # Step 2 & 3: Formulasi Parameter Ising untuk Pure Markowitz
    # Secara matematis dari energi E(s):
    #   Kopling (J_ij): (lambda * sigma_ij + 2 * penalty_A) / 4
    #   Bias (h_i):    -0.5 * [lambda * sigma_ii - (1-lambda)*mu_i + penalty_A*(1-2K)] - sum_{j!=i} J_ij
    #
    #   di mana: mu_i (annual return), sigma_ij (annual covariance elemen i,j).
    # ------------------------------------------------------------------
    h = np.zeros(n_assets)
    J = np.zeros((n_assets, n_assets))
    
    # Hitung Kopling (J_ij)
    for i in range(n_assets):
        for j in range(i + 1, n_assets):
            J[i, j] = (lam * cov_annual[i, j] + 2.0 * penalty_A) / 4.0
            J[j, i] = J[i, j] # matriks kopling simetris
            
    # Hitung Bias (h_i)
    for i in range(n_assets):
        sum_J_ij = sum(J[i, j] for j in range(n_assets) if j != i)
        
        # Penempatan tanda negatif untuk memastikan proses minimisasi dalam VQE
        h[i] = -0.5 * (lam * cov_annual[i, i] - (1.0 - lam) * mu_annual[i] + penalty_A * (1.0 - 2.0 * K)) - sum_J_ij

    # ------------------------------------------------------------------
    # Step 4: Solusi Brute-Force Klasik (Warm-Start)
    # ------------------------------------------------------------------
    classical_state, classical_energy = find_classical_markowitz_solution(h, J, n_assets, K)
    
    # ------------------------------------------------------------------
    # Step 5: Bangun Hamiltonian & Optimasi VQE
    # ------------------------------------------------------------------
    H = build_markowitz_hamiltonian(h, J, n_assets)
    selected_indices, depth_used, energy_final = run_vqe_adaptive(
        H, n_assets, classical_state, K=K, max_depth=max_depth, maxiter=maxiter,
        max_total_iter=max_total_iter, batch_size=batch_size,
        conv_window=conv_window, conv_tol=conv_tol
    )

    return selected_indices, depth_used, energy_final

# =============================================================================
# 8. Fungsi Metrik Evaluasi Finansial
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
# 9. MAIN BACKTEST LOOP
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
# 10. Evaluasi Metrik Kinerja
# =============================================================================
tr_vqe,   sr_vqe,   mdd_vqe   = compute_metrics(value_vqe,   initial_capital, "Markowitz QUBO VQE (Adaptive Layers)")
tr_bench, sr_bench, mdd_bench = compute_metrics(value_bench, initial_capital, "Buy & Hold Equal Weight")
for t in tickers:
    compute_metrics(value_assets[t], initial_capital, f"Buy & Hold {t}")

# =============================================================================
# 11. Visualisasi Pertumbuhan Portofolio
# =============================================================================
plt.figure(figsize=(14, 7))

dates = data_clean.index

plt.plot(dates[:len(value_vqe)],   value_vqe,
         label=f'Markowitz QUBO VQE SPSA Adaptive (K={K})',
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
    'Metodologi: Pure Markowitz QUBO + VQE Adaptive Layers'
)
plt.ylabel('Ekuitas Portofolio (Rupiah)')
plt.xlabel('Tanggal')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('backtest_result.png', dpi=150)
plt.show()
print("\nGrafik disimpan sebagai backtest_result.png")
