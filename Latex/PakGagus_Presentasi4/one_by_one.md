# Plan sequence
1. fetch data finance with yfinance then count the bullish and bearish candlestick
2. calculate the payoff matrix with as well as @Latex/PakHeru_Presentasi4/Adv_Gemini_plan until.md we get the probability of each state as well as @Latex/PakGagus_Presentasi3/rencana_presentasi_analisis_numerik.md
3. fetch calculated value of payoff to calculate bias
4. construct the density matrix to get the value of von neumann entropy as interaction (J_ij)
5. fetch the bias and interaction value to hamiltonian ising
6. use vqe algorithm to get the ground stat with ansatz efficientSU2

# Data Fetching
## Code 1: Fetching Candlestick Data
```python
import yfinance as yf
import pandas as pd

# Daftar saham yang akan diambil datanya
tickers = ['BBCA.JK', 'TPIA.JK', 'ASII.JK', 'TLKM.JK']
period = '6mo'
interval = '1d'

# Dictionary untuk menyimpan hasil perhitungan
candlestick_counts = {}

print("Fetching data and counting candlesticks...\n")

for ticker in tickers:
    # Mengambil data historis
    df = yf.download(ticker, period=period, interval=interval, progress=False)

    if df.empty:
        print(f"No data found for {ticker}")
        continue

    # Menangani MultiIndex columns jika yfinance versi terbaru
    if isinstance(df.columns, pd.MultiIndex):
        open_price = df['Open'][ticker]
        close_price = df['Close'][ticker]
    else:
        open_price = df['Open']
        close_price = df['Close']

    # Perhitungan Candlestick (Bullish, Bearish, Neutral)
    bullish_count = int((close_price > open_price).sum())
    bearish_count = int((close_price < open_price).sum())
    neutral_count = int((close_price == open_price).sum())

    candlestick_counts[ticker] = {
        'Bullish': bullish_count,
        'Bearish': bearish_count,
        'Neutral': neutral_count,
        'Total Data': len(df)
    }

    print(f"[{ticker}]")
    print(f"  Bullish : {bullish_count}")
    print(f"  Bearish : {bearish_count}")
    print(f"  Neutral : {neutral_count}")
    print(f"  Total   : {len(df)}\n")

# Menampilkan rekap dalam bentuk DataFrame
summary_df = pd.DataFrame(candlestick_counts).T
summary_df
```

## Output 1
```text
Fetching data and counting candlesticks...

[BBCA.JK]
  Bullish : 52
  Bearish : 58
  Neutral : 15
  Total   : 125

[TPIA.JK]
  Bullish : 41
  Bearish : 73
  Neutral : 11
  Total   : 125

[ASII.JK]
  Bullish : 52
  Bearish : 61
  Neutral : 12
  Total   : 125

[TLKM.JK]
  Bullish : 56
  Bearish : 64
  Neutral : 5
  Total   : 125
```

# Calculate Payoff Matrix 12 Pair
## Theory: Konstruksi Fungsi Gelombang dan Matriks Payoff
Berdasarkan metodologi **Markowitz $\times$ Game Theory (Risk Aversion Endogen)** dan **Econophysics Kuantum**, berikut adalah langkah-langkah formulasi:

1. **Perhitungan Return dan Penentuan State**:
   $$ R_t = \ln\left(\frac{P_t}{P_{t-1}}\right) $$
   - **Naik ($|0\rangle$)**: Jika $R_t > 0$
   - **Turun ($|1\rangle$)**: Jika $R_t \le 0$

2. **Risk Aversion Endogen ($\lambda_{\text{market}}$)** menggunakan Fungsi Sigmoid:
   $$ \lambda_{\text{market}} = \frac{1}{1 + e^{\left(\frac{\mu_{avg}}{\sigma_{avg}}\right)}} $$

3. **Konstruksi Matriks Payoff (Utilitas Markowitz)**:
   $$ U_k^{(ij)} = (1 - \lambda_{\text{market}}) \cdot \mu_{k}^{(ij)} - \lambda_{\text{market}} \cdot \sigma_{k}^{(ij)} $$

4. **Probabilitas State Bersama ($P_{ij}$)** dan **Fungsi Gelombang ($|\psi\rangle$)**:
   $$ a_{ij} = \sqrt{P_{ij}} $$
   $$ |\psi\rangle = a_{00} |00\rangle + a_{01} |01\rangle + a_{10} |10\rangle + a_{11} |11\rangle $$

## Code 2: Payoff and Probability Calculation
```python
import numpy as np
import itertools
import pandas as pd
import math

print("1. Menghitung Log Return Harian dan State (0=Naik, 1=Turun)...")
data = yf.download(tickers, period=period, interval=interval, progress=False)
prices = data['Close'].dropna()
log_returns = np.log(prices / prices.shift(1)).dropna()
states = (log_returns <= 0).astype(int)

print("\n2. Menghitung Risk Aversion Endogen (Lambda Market) ...")
mu_avg = log_returns.mean().mean()
sigma_avg = log_returns.std(ddof=1).mean()
lambda_market = 1 / (1 + math.exp(mu_avg / sigma_avg)) if sigma_avg != 0 else 0.5
print(f"   - Mu_avg    : {mu_avg:.6f}")
print(f"   - Sigma_avg : {sigma_avg:.6f}")
print(f"   - Lambda    : {lambda_market:.6f}")

print("\n3 & 4 & 5. Konstruksi Matriks Payoff, Probabilitas, dan Fungsi Gelombang...")
def calculate_quantum_payoff(asset_L, asset_F):
    payoff_L = np.zeros((2, 2)); payoff_F = np.zeros((2, 2)); probs = np.zeros((2, 2))
    n_total = len(log_returns)
    for i in [0, 1]:
        for j in [0, 1]:
            mask = (states[asset_L] == i) & (states[asset_F] == j)
            n_ij = mask.sum()
            p_ij = n_ij / n_total if n_total > 0 else 0
            probs[i, j] = p_ij
            subset_L = log_returns.loc[mask, asset_L]
            subset_F = log_returns.loc[mask, asset_F]
            if n_ij > 0:
                mu_L, sig_L = subset_L.mean(), subset_L.std(ddof=0)
                mu_F, sig_F = subset_F.mean(), subset_F.std(ddof=0)
            else:
                mu_L, sig_L = 0, 0; mu_F, sig_F = 0, 0
            payoff_L[i, j] = (1 - lambda_market) * mu_L - lambda_market * sig_L
            payoff_F[i, j] = (1 - lambda_market) * mu_F - lambda_market * sig_F
    return payoff_L, payoff_F, probs

pairs = list(itertools.permutations(tickers, 2))
quantum_results = {}
for pair in pairs:
    asset_L, asset_F = pair
    pL, pF, prob = calculate_quantum_payoff(asset_L, asset_F)
    quantum_coeffs = np.sqrt(prob)
    quantum_results[pair] = {'Payoff_L': pL, 'Payoff_F': pF, 'Probabilities': prob, 'Quantum_Coeffs': quantum_coeffs}
```

## Output 2: Contoh Hasil Kalkulasi (BBCA & TPIA)
```text
==================================================
Pasangan Leader: BBCA.JK | Follower: TPIA.JK
==================================================
Matriks Payoff Leader (U_L):
[[ 0.000588  0.002103]
 [-0.008416 -0.012949]]

Matriks Payoff Follower (U_F):
[[ 0.000624 -0.017209]
 [ 0.001911 -0.01679 ]]

Quantum Coefficients (a_00, a_01, a_10, a_11):
[[0.4115 0.4752]
 [0.4579 0.6286]]

Fungsi Gelombang |psi> : 
0.4115 |00> + 0.4752 |01> + 0.4579 |10> + 0.6286 |11>
```

## Mathematical Interpretation Payoff
Kita dapat menyatukan matriks payoff individual menjadi matriks strategi gabungan Game Theory $(U_L, U_F)$:

### 1. Pasangan BBCA (Leader) - TPIA (Follower)
| BBCA \ TPIA | $\ket{0}_F$ (Up) | $\ket{1}_F$ (Down) |
| :--- | :---: | :---: |
| **$\ket{0}_L$ (Up)** | $(0.000588, 0.000624)$ | $(0.002103, -0.017209)$ |
| **$\ket{1}_L$ (Down)** | $(-0.008416, 0.001911)$ | $(-0.012949, -0.01679)$ |

### 2. Pasangan BBCA (Leader) - ASII (Follower)
| BBCA \ ASII            |    $\ket{0}_F$ (Up)     |    $\ket{1}_F$ (Down)    |
| :--------------------- | :---------------------: | :----------------------: |
| **$\ket{0}_L$ (Up)**   | $(0.000379, 0.002092)$  | $(0.002674, -0.009162)$  |
| **$\ket{1}_L$ (Down)** | $(-0.007749, 0.002314)$ | $(-0.013675, -0.017807)$ |

**Interpretasi:**
- State $\ket{00}$ (Keduanya naik) memberikan payoff positif bagi keduanya, menandakan sinergi korelasi positif.
- State $\ket{11}$ (Keduanya turun) menunjukkan kerugian utilitas terdalam, mencerminkan risiko sistemik.

# Construct Density Matrix and QMI 12 Pair
## Theory: Quantum Mutual Information (QMI)
Relasi antar aset diukur dengan **Quantum Mutual Information (QMI)** atau $J_{ij}$ yang diekstrak dari **Von Neumann Entropy**.

1. **Matriks Densitas Sistem ($\rho$)**: $\rho = |\psi\rangle \langle\psi|$
2. **Reduced Density Matrix ($\rho_L, \rho_F$)**: Menggunakan operasi *Partial Trace*.
3. **Von Neumann Entropy ($S$)**: $S(\sigma) = -\text{Tr}(\sigma \ln \sigma)$
4. **Interaction Hamiltonian ($J_{LF}$)**:
   $$ J_{LF} = I(L:F) = S(\rho_L) + S(\rho_F) - S(\rho_{LF}) $$

## Code 3: Entropy and QMI Calculation
```python
import numpy as np
from scipy.linalg import eigh

def vn_entropy(rho):
    evals = eigh(rho)[0]
    evals = np.clip(evals, 1e-12, 1.0)
    return -np.sum(evals * np.log(evals))

interaction_J = {}
for pair, res in quantum_results.items():
    asset_L, asset_F = pair
    a = res['Quantum_Coeffs']
    psi = np.array([a[0,0], a[0,1], a[1,0], a[1,1]])
    rho_system = np.outer(psi, psi)
    
    rho_L = np.array([
        [psi[0]**2 + psi[1]**2, psi[0]*psi[2] + psi[1]*psi[3]],
        [psi[2]*psi[0] + psi[3]*psi[1], psi[2]**2 + psi[3]**2]
    ])
    rho_F = np.array([
        [psi[0]**2 + psi[2]**2, psi[0]*psi[1] + psi[2]*psi[3]],
        [psi[1]*psi[0] + psi[3]*psi[2], psi[1]**2 + psi[3]**2]
    ])
    
    S_L, S_F, S_system = vn_entropy(rho_L), vn_entropy(rho_F), vn_entropy(rho_system)
    I_LF = S_L + S_F - S_system
    interaction_J[pair] = I_LF
    
    print(f"--- QMI [{asset_L} & {asset_F}] : {I_LF:.4f} ---")
```

# Bias Determination
## Theory: Konstruksi Parameter Bias ($h$)
Parameter Bias ($h_i$) merepresentasikan kecenderungan intrinsik suatu aset untuk naik ($|0\rangle$) atau turun ($|1\rangle$) terlepas dari pasangannya.

$$ h_L = \frac{(U_L^{(00)} + U_L^{(01)}) - (U_L^{(10)} + U_L^{(11)})}{2} $$
$$ h_F = \frac{(U_F^{(00)} + U_F^{(10)}) - (U_F^{(01)} + U_F^{(11)})}{2} $$

## Code 4: Bias Calculation
```python
bias_h = {ticker: [] for ticker in tickers}
for pair, res in quantum_results.items():
    asset_L, asset_F = pair
    pL, pF = res['Payoff_L'], res['Payoff_F']
    
    h_L = ((pL[0,0] + pL[0,1]) - (pL[1,0] + pL[1,1])) / 2
    h_F = ((pF[0,0] + pF[1,0]) - (pF[0,1] + pF[1,1])) / 2
    
    bias_h[asset_L].append(h_L)
    bias_h[asset_F].append(h_F)

print("--- Rata-Rata Bias Keseluruhan ---")
final_bias = {ticker: np.mean(val) for ticker, val in bias_h.items()}
for t, h in final_bias.items():
    trend = "Uptrend" if h > 0 else "Downtrend"
    print(f"Saham {t:8s} | h = {h:10.6f} => {trend}")
```

## Numerical Calculation Example: Parameter Bias ($h$)
Menggunakan data **BBCA (Leader)** dan **ASII (Follower)** dari Output 2:

**1. Bias BBCA ($h_L$):**
- Expected Payoff Naik: $0.000379 + 0.002674 = 0.003053$
- Expected Payoff Turun: $-0.007749 + (-0.013675) = -0.021424$
- $h_L = [0.003053 - (-0.021424)] / 2 = 0.012239$

**2. Bias ASII ($h_F$):**
- Expected Payoff Naik: $0.002092 + 0.002314 = 0.004406$
- Expected Payoff Turun: $-0.009162 + (-0.017807) = -0.026969$
- $h_F = [0.004406 - (-0.026969)] / 2 = 0.015688$

*(Catatan: Nilai $h$ positif menunjukkan kecenderungan pergerakan stabil pada state **Naik** berdasar struktur utilitas terbaru.)*

# VQE Implementation
## 6. Konstruksi Ising Hamiltonian dan Optimasi VQE (Variational Quantum Eigensolver)
Setelah kita berhasil merangkum dinamika pasar menjadi parameter Bias ($h_i$) dan parameter Interaksi/Entanglement ($J_{ij}$), langkah puncak dari metodologi ini adalah merealisasikan **Hamiltonian Operator** ($H$) dan mencari *Ground State* (keadaan energi terendah yang merepresentasikan konfigurasi portofolio paling stabil) menggunakan komputer kuantum.

### A. Ising Hamiltonian ($H$)
Hamiltonian ($H$) dalam bentuk Ising merepresentasikan *cost function* energi total sistem. Secara umum untuk $n$ qubit (misal 4 saham: BBCA, TPIA, ASII, TLKM), persamaannya adalah:
$$ H = - \sum_{i=0}^{n-1} h_i \sigma_i^z - \sum_{i<j}^{n-1} J_{ij} \sigma_i^z \sigma_j^z $$
Di mana $\sigma^z$ adalah Pauli-Z operator (bernilai $+1$ untuk state $|0\rangle$ dan $-1$ untuk state $|1\rangle$). Hamiltonian ini mendikte bahwa sistem akan mencoba mensejajarkan aset (ke arah Naik/Turun) sesuai dengan dorongan $h_i$ dan mensejajarkan pasangan aset searah/berlawanan sesuai dengan $J_{ij}$.

### B. Efficient SU(2) Ansatz
Untuk mencari nilai eigen terendah (Ground State) dari rentabilitas Hamiltonian tersebut sebesar $2^N$ ruang pencarian (tanpa *brute-force* klasik), kita menggunakan pendekatan Variasional Kuantum dengan **EfficientSU2** ansatz parametrik.

Ansatz ini dipilih karena ia mengoptimalkan kedalaman sirkuit (*gate depth*) secara efisien untuk NISQ (Noisy Intermediate-Scale Quantum) devices. State kuantum akan diproses melalui *layer* rotasi satu-qubit dan *layer* keterbelitan (*entanglement*):
$$ |\psi(\theta)\rangle = U(\theta) |0\rangle^{\otimes n} = L_d(\theta_d) \prod_{i=0}^{d-1} [W_i L_i(\theta_i)] |0\rangle^{\otimes n} $$

*   **Layer Rotasi ($L_i$)**: Mengeksplorasi bola Bloch menggunakan gerbang parameter $R_y$ dan $R_z$.
$$ L_i(\theta_i) = \bigotimes_{j=0}^{n-1} R_z(\theta_{i,j,2}) R_y(\theta_{i,j,1}) $$
*   **Layer Keterbelitan ($W_i$)**: Menggunakan gerbang $CX$ (*Linear* atau *Full Entanglement*) tanpa parameter untuk menjalin korelasi prediktif antar qubit di dalam ansatz.

### C. Optimizer SPSA (Simultaneous Perturbation Stochastic Approximation)
Setiap kali VQE mengevaluasi $\langle \psi(\theta) | H | \psi(\theta) \rangle$, hasil energi diserahkan ke *optimizer* klasik untuk memperbarui nilai sudut $\theta$.

Kita menggunakan **SPSA** karena sifat efisiensinya terhadap jumlah parameter dan ketangguhannya terhadap *noise* stokastik fungsi gelombang. Daripada menghitung gradien/kemiringan satu-demi-satu per parameter (yang butuh $2n$ evaluasi), SPSA menggeser **semua** parameter sekaligus secara acak melalui vektor Bernoulli, sehingga hanya membutuhkan **2 evaluasi sirkuit** per iterasi:
1. Hitung Energi plus perturbasi: $E_+ = E(\theta_t + c_t \Delta_t)$
2. Hitung Energi minus perturbasi: $E_- = E(\theta_t - c_t \Delta_t)$
3. Estimasi Gradien Bersama: $\hat{g}_t = \frac{E_+ - E_-}{2 c_t \Delta_t}$
4. *Update Rules*: $\theta_{t+1} = \theta_t - a_t \hat{g}_t$

Sirkuit akan berulang secara adaptif melalui Optimizer SPSA hingga energi Hamiltonian Ising mendekati titik ekuilibrium *(Ground State)* konvergennya. Pada titik inilah kita membaca state binernya $(*bitstring*)$ untuk memilih set aset portofolio terbaik.

## Hamiltonian Constraint (Penalti Jumlah Portofolio)
Dalam dunia nyata, kita tidak mungkin membeli semua saham yang menunjukkan *Uptrend*, melainkan kita terbatas oleh anggaran dana atau regulasi portofolio. Kita bisa memaksa VQE untuk **hanya memilih tepat $K$ aset** (misal $K = 2$) dari keseluruhan $N=4$ aset yang tersedia.

Untuk itu, kita tambahkan satu **Hamiltonian Constraint ($H_C$)** ke dalam sistem energi:
$$ H_C = A \left( \sum_{i=1}^N x_i - K \right)^2 $$
Di mana:
- $A$ adalah Konstanta Penalti yang bernilai besar (misal $A = 5.0$) untuk memastikan *state* yang tidak memenuhi $K=2$ diberi penalti energi sangat tinggi hingga dijauhi oleh VQE.
- $x_i$ adalah biner $\{0, 1\}$ yang menyatakan apakah saham $i$ dipilih atau tidak.

**Transformasi Kuantum:**
Pada basis komputasi Pauli-Z, state $|0\rangle$ (Naik/Beli) memiliki nilai eigen $+1$ dan state $|1\rangle$ (Turun/Hindari) memiliki nilai eigen $-1$.
Maka biner $x_i$ didefinisikan sebagai proyektor:
$$ x_i = \frac{1 - \sigma_i^z}{2} $$

Jika kita substitusikan $x_i$ ke persamaan constraint untuk $N=4$ dan $K=2$:
$$ \sum_{i=1}^4 x_i - 2 = \sum_{i=1}^4 \left(\frac{1 - \sigma_i^z}{2}\right) - 2 $$
$$ = \left(\frac{4}{2} - \frac{1}{2} \sum_{i=1}^4 \sigma_i^z \right) - 2 = -\frac{1}{2} \sum_{i=1}^4 \sigma_i^z $$

Lalu kita kuadratkan sesuai rumusan fungsi $A(\dots)^2$:
$$ H_C = A \left( -\frac{1}{2} \sum_{i=1}^4 \sigma_i^z \right)^2 = \frac{A}{4} \left( \sum_{i=1}^4 \sigma_i^z \right)^2 $$
$$ H_C = \frac{A}{4} \left( \sum_{i=1}^4 (\sigma_i^z)^2 + 2 \sum_{i<j} \sigma_i^z \sigma_j^z \right) $$

Karena dikuadratkan, nilai $(\sigma^z)^2$ di ranah matriks Pauli adalah **Matriks Identitas ($I$)**. Sehingga persamaannya menyusut menjadi:
$$ H_C = \frac{A}{4} \left( 4I + 2 \sum_{i<j} \sigma_i^z \sigma_j^z \right) = A \cdot I + \frac{A}{2} \sum_{i<j} \sigma_i^z \sigma_j^z $$

**Kesimpulan Implikasi:**
Untuk memaksa VQE agar memilih tepat 2 aset, kita tidak perlu repot-repot memodifikasi Bias ($h_i$), tapi **cukup menambahkan penalti sebesar $\frac{A}{2}$ ke setiap bobot Interaksi ($J_{ij}$)** antar kedua aset, ditambah satu konstanta energi dasar $A \cdot I$.

## Numerical Calculation Example: Siklus VQE (Hamiltonian, Ansatz, SPSA)
Agar lebih intuitif, mari kita bedah secara matematis bagaimana matriks Hamiltonian dibangun secara *under-the-hood* dan dioptimasi oleh VQE. Untuk mempermudah ilustrasi, kita pecah menjadi sub-sistem **2 Qubit** saja, misalnya saham **BBCA (Qubit 0)** dan **ASII (Qubit 1)** dengan konstanta numerik rata-rata yang sudah kita hitung sebelumnya:
- $h_{BBCA} \approx 0.0122$ (Cenderung Naik/Beli)
- $h_{ASII} \approx 0.0173$ (Cenderung Naik/Beli)
- $J_{(BBCA, ASII)} \approx -0.0633$ (Anti-Logis/Interaksi Saling Tarik)

*(Asumsikan belum ada Constraint $K=2$, agar ruang energi tidak bias)*

#### 1. Pembangunan Matriks Hamiltonian ($H$)
Hamiltonian Ising untuk 2 Qubit tersebut didefinisikan sebagai Operator linear:
$$ H = -h_{BBCA} (Z \otimes I) - h_{ASII} (I \otimes Z) - J (Z \otimes Z) $$

Mari kita terjemahkan Operator Pauli-Z ini ke dalam matriks $4 \times 4$ klasikal murni. Operator Pauli-Z bekerja di sumbu diagonal:
- $Z \otimes I = \text{diag}(1, 1, -1, -1)$
- $I \otimes Z = \text{diag}(1, -1, 1, -1)$
- $Z \otimes Z = \text{diag}(1, -1, -1, 1)$

Maka lanskap matriks energi $H$ berpusat di garis diagonal pembacaan basis komputasi *state* $|00\rangle, |01\rangle, |10\rangle, |11\rangle$:
$$ H = \begin{bmatrix} (-h_{BBCA} - h_{ASII} - J) & 0 & 0 & 0 \\ 0 & (-h_{BBCA} + h_{ASII} + J) & 0 & 0 \\ 0 & 0 & (h_{BBCA} - h_{ASII} + J) & 0 \\ 0 & 0 & 0 & (h_{BBCA} + h_{ASII} - J) \end{bmatrix} $$

Substitusikan nilai empiris dari kalkulasi matriks Payoff dan QMI:
- E($|00\rangle$ Beli Semua): $-0.0122 - 0.0173 - (-0.0633) = -0.0295 + 0.0633 = \mathbf{0.0338}$
- E($|01\rangle$ Beli BBCA, Jual ASII): $-0.0122 + 0.0173 - 0.0633 = \mathbf{-0.0582}$
- E($|10\rangle$ Jual BBCA, Beli ASII): $0.0122 - 0.0173 - 0.0633 = \mathbf{-0.0684}$
- E($|11\rangle$ Jual Semua): $0.0122 + 0.0173 + 0.0633 = \mathbf{0.0928}$

**Kesimpulan Matriks Hamiltonian**: Secara fisik tanpa *Constraint*, state yang mematuhi hukum termodinamika energi terendah (*Ground State*) adalah kombinasi $|10\rangle$ bernilai $\mathbf{-0.0684}$, yang mempresentasikan strategi \"Hindari BBCA, Beli ASII\".

#### 2. Pemberian Gerbang Rotasi ($R_y, R_z$) dan Entanglement ($CX$)
VQE tidak membedah matriks diagonal di atas secara klasik, ia melempar tebakan gelombang probabilitas parameterik $|\psi(\vec{\theta})\rangle$ layaknya mesin regresi. Misal pada iterasi pertama, sirkuit memulai gelombang dari state mutlak $|00\rangle$.

- **Layer Rotasi Tunggal**:
    - Gerbang $R_y(\theta)$ memutar amplitudo probabilitas, mencampurkan kemungkinan status Beli dan Jual (Superposisi).
    $$ R_y(\theta) |0\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle $$
    - Gerbang $R_z(\phi)$ menggeser fase relatif antara status $|0\rangle$ dan $|1\rangle$ tanpa mengubah probabilitas besarnya.
    $$ R_z(\phi) (\alpha|0\rangle + \beta|1\rangle) = e^{-i\phi/2}\alpha|0\rangle + e^{i\phi/2}\beta|1\rangle $$
- **Layer Entanglement**: Gerbang *CNOT* ($CX$) menembakkan pulsa antar 2 Qubit. Ia memutar rotasi ASII dari ujung ke ujung jika status BBCA adalah $|1\rangle$. Jika BBCA dan ASII berada di superposisi, CNOT secara instan \"mengikat\" keterbelitannya (*Entangled*) layaknya benang merah sehingga nasib probabilitas ASII akan bergantung mutlak pada nasib BBCA saat diukur.

#### 3. Optimasi Menggunakan SPSA (Stochastic Perturbation)
Proses pengukuran (*Measurement*) memproyeksikan vektor tebakan kuantum kita kembali ke Matriks Hamiltonian diagonal $H$.
Total Ekspektasi Energi saat ini adalah: $E = \langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle = |a_{00}|^2 E_{00} + |a_{01}|^2 E_{01} + |a_{10}|^2 E_{10} + |a_{11}|^2 E_{11}$.

Selanjutnya, *optimizer* SPSA (klasik) menggeser derajat pintu gerbang $R_y$/$R_z$ untuk iterasi selanjutnya hingga energi Hamiltonian Ising mendekati titik ekuilibrium *(Ground State)*.

## VQE Implementation Code
### 1. PennyLane Implementation
```python
import pennylane as qml
from pennylane import numpy as pnp
import matplotlib.pyplot as plt

print("--- Membangun Sirkuit Hamiltonian VQE PennyLane ---\n")
num_qubits = len(tickers)

# 1. Definisi Observable Hamiltonian
coeffs = []
obs = []

# A. Field Terms (-h Z_i)
for i, ticker in enumerate(tickers):
    avg_h = final_bias[ticker]
    coeffs.append(-avg_h)
    obs.append(qml.PauliZ(i))

# B. Interaction Terms (-J Z_i Z_j)
def get_index(ticker_name):
    return tickers.index(ticker_name)

for pair, J_value in interaction_J.items():
    idx1 = get_index(pair[0])
    idx2 = get_index(pair[1])
    coeffs.append(-J_value)
    obs.append(qml.PauliZ(idx1) @ qml.PauliZ(idx2))

# Menyusun Hamiltonian dengan Penalty Constraint
print("\n--- Mengaplikasikan Penalty Constraint (K=2, A=5.0) ---")
A = 5.0
coeffs.append(A)
obs.append(qml.Identity(0))

import itertools
for pair in itertools.combinations(range(num_qubits), 2):
    coeffs.append(A / 2)
    obs.append(qml.PauliZ(pair[0]) @ qml.PauliZ(pair[1]))

H = qml.Hamiltonian(coeffs, obs)
H = H.simplify()
print("Ising Hamiltonian Operator (PennyLane):")
print(H)

# 2. Definisi Ansatz Hardware Efficient SU(2)
n_layers = 1
def efficient_su2_ansatz(params, wires):
    for i in range(num_qubits):
        qml.RY(params[0, i, 0], wires=wires[i])
        qml.RZ(params[0, i, 1], wires=wires[i])
    for layer in range(n_layers):
        for i in range(num_qubits - 1):
            qml.CNOT(wires=[wires[i], wires[i+1]])
        for i in range(num_qubits):
            qml.RY(params[layer + 1, i, 0], wires=wires[i])
            qml.RZ(params[layer + 1, i, 1], wires=wires[i])

dev = qml.device("default.qubit", wires=num_qubits)
@qml.qnode(dev)
def cost_function(params):
    efficient_su2_ansatz(params, wires=range(num_qubits))
    return qml.expval(H)

# 3. Optimasi Menggunakan Adam
np.random.seed(42)
initial_params = pnp.random.uniform(0, 2 * pnp.pi, (n_layers + 1, num_qubits, 2), requires_grad=True)
opt = qml.AdamOptimizer(stepsize=0.1)
params = initial_params

print("\nMenjalankan Optimasi VQE (Adam), Harap tunggu...")
for n in range(100):
    params, _ = opt.step_and_cost(cost_function, params)

print(f"\n--- Hasil Optimasi VQE (PennyLane) ---")
print(f"Ground State Energy: {cost_function(params):.6f}")
```

### 2. Qiskit Implementation
```python
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import EfficientSU2
from qiskit.primitives import StatevectorEstimator as Estimator
from qiskit_algorithms.optimizers import SPSA
from qiskit_algorithms import VQE
import numpy as np

print("--- Membangun Sirkuit Hamiltonian VQE Qiskit ---\n")
pauli_list = []; coeffs_list = []; num_assets = len(tickers)

# A. Field Terms
for i, ticker in enumerate(tickers):
    avg_h = final_bias[ticker]
    pauli_str = ['I'] * num_assets
    pauli_str[num_assets - 1 - i] = 'Z'
    pauli_list.append("".join(pauli_str))
    coeffs_list.append(-avg_h)

# B. Interaction Terms with Penalty Constraint
A = 5.0
pauli_list.append('I' * num_assets); coeffs_list.append(A)
for pair in itertools.combinations(range(num_assets), 2):
    pauli_str = ['I'] * num_assets
    pauli_str[num_assets - 1 - pair[0]] = 'Z'
    pauli_str[num_assets - 1 - pair[1]] = 'Z'
    pauli_list.append("".join(pauli_str))
    coeffs_list.append(A / 2 - interaction_J.get((tickers[pair[0]], tickers[pair[1]]), 0))

H_operator = SparsePauliOp(pauli_list, coeffs_list).simplify()
ansatz = EfficientSU2(num_qubits=num_assets, reps=1, entanglement='linear')
optimizer = SPSA(maxiter=200)
vqe = VQE(estimator=Estimator(), ansatz=ansatz, optimizer=optimizer)

print("\nMenjalankan Optimasi VQE (SPSA), Harap tunggu...")
result = vqe.compute_minimum_eigenvalue(operator=H_operator)
print(f"\n--- Hasil Optimasi VQE (Qiskit) ---")
print(f"Ground State Energy: {result.eigenvalue.real:.6f}")
```