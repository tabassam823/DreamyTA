# Plan sequence
1. fetch data finance with yfinance then count the bullish and bearish candlestick
2. calculate the payoff matrix with as well as @Latex/PakHeru_Presentasi4/Adv_Gemini_plan until.md we get the probability of each state as well as @Latex/PakGagus_Presentasi3/rencana_presentasi_analisis_numerik.md
3. fetch calculated value of payoff to calculate bias
4. construct the density matrix to get the value of von neumann entropy as interaction (J_ij)
5. fetch the bias and interaction value to hamiltonian ising
6. use vqe algorithm to get the ground stat with ansatz efficientSU2

# Data Fetching
## Code 1
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

    # Perhitungan Candlestick
    # Bullish: Close > Open
    # Bearish: Close < Open
    # Neutral/Doji: Close == Open
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
## Note Payoff
### Contoh Kalkulasi Manual: Payoff & Probabilitas (Metode Markowitz)

Misalkan kita mengamati 100 hari riwayat perdagangan untuk pasangan saham **Leader (BBCA)** dan **Follower (ASII)**.

#### 1. Parameter Pasar (Endogenous Risk Aversion)
Misalkan dari seluruh data historis bursa didapatkan:
- Rata-rata return pasar ($\mu_{avg}$) = `0.001` (0.1%)
- Rata-rata volatilitas pasar ($\sigma_{avg}$) = `0.015` (1.5%)
- Penghitungan $\lambda_{\text{market}}$ (Fungsi Sigmoid):
$$ \lambda = \frac{1}{1 + e^{\left(\frac{0.001}{0.015}\right)}} = \frac{1}{1 + e^{0.0667}} = \frac{1}{1 + 1.0689} \approx 0.4833 $$

#### 2. Perhitungan pada State $|00\rangle$ (Keduanya Sama-Sama Naik, $R_t > 0$)
Misalkan mereka naik secara bersamaan di hari yang sama sebanyak **45 hari** ($n_{00} = 45$).
- **Probabilitas ($P_{00}$)**: $\frac{n_{00}}{n_{total}} = \frac{45}{100} = 0.45$
- **Amplitudo Kuantum ($a_{00}$)**: $\sqrt{P_{00}} = \sqrt{0.45} \approx 0.6708$

#### 3. Perhitungan Utilitas Markowitz (Payoff) pada State $|00\rangle$
Misalkan jika kita ambil subset 45 hari di mana KEDUANYA NAIK tersebut, kita dapati:
- Rata-rata return harian BBCA $\mu_L^{(00)}$ = `0.010`
- Std dev return BBCA $\sigma_L^{(00)}$ = `0.005`
- Rata-rata return harian ASII $\mu_F^{(00)}$ = `0.012`
- Std dev return ASII $\sigma_F^{(00)}$ = `0.008`

**Maka Nilai Payoff BBCA (Leader) di Matriks (Baris 0, Kolom 0):**
$$ U_L^{(00)} = (1 - \lambda) \cdot \mu_L^{(00)} - \lambda \cdot \sigma_L^{(00)} $$
$$ U_L^{(00)} = (1 - 0.4833) \cdot 0.010 - 0.4833 \cdot 0.005 $$
$$ U_L^{(00)} = 0.005167 - 0.002416 = 0.002751 $$

**Sedangkan Nilai Payoff ASII (Follower) di Matriks (Baris 0, Kolom 0):**
$$ U_F^{(00)} = (1 - \lambda) \cdot \mu_F^{(00)} - \lambda \cdot \sigma_F^{(00)} $$
$$ U_F^{(00)} = (0.5167 \cdot 0.012) - (0.4833 \cdot 0.008) = 0.006200 - 0.003866 = 0.002334 $$

#### 4. Iterasi Selanjutnya (Penempatan di Matriks 2x2)
Proses (Frekuensi $\rightarrow$ $P_{ij}$ $\rightarrow$ Amplitudo Kuantum $a_{ij}$ $\rightarrow$ Nilai Subset $\mu, \sigma$ $\rightarrow$ $U_L, U_F$) ini kemudian diulangi pada:
- State $|01\rangle$: BBCA Naik, ASII Turun
- State $|10\rangle$: BBCA Turun, ASII Naik
- State $|11\rangle$: Keduanya Sama-Sama Turun

Sehingga menghasilkan secara utuh `Payoff_L` (Leader), `Payoff_F` (Follower), `Probabilities`, dan `Quantum_Coeffs`.

## Code Payoff
```python
import numpy as np
import itertools
import pandas as pd
import math

print("1. Menghitung Log Return Harian dan State (0=Naik, 1=Turun)...")
# Dari data 'df' sebelumnya, kita perlu pastikan kita punya seluruh ticker.
# Kita akan mengambil ulang agar lebih bersih dan memiliki dataframe harga yang utuh
data = yf.download(tickers, period=period, interval=interval, progress=False)

if isinstance(data.columns, pd.MultiIndex):
    prices = data['Close']
else:
    prices = data['Close'] # backup

prices = prices.dropna()

# R_t = ln(P_t / P_{t-1})
log_returns = np.log(prices / prices.shift(1)).dropna()

# Diskritisasi: 0 jika R_t > 0, 1 jika R_t <= 0
states = (log_returns <= 0).astype(int)

print("\n2. Menghitung Risk Aversion Endogen (Lambda Market) ...")
mu_avg = log_returns.mean().mean() # Rata-rata return seluruh pasar
sigma_avg = log_returns.std(ddof=1).mean() # Rata-rata volatilitas seluruh pasar

lambda_market = 1 / (1 + math.exp(mu_avg / sigma_avg)) if sigma_avg != 0 else 0.5
print(f"   - Mu_avg    : {mu_avg:.6f}")
print(f"   - Sigma_avg : {sigma_avg:.6f}")
print(f"   - Lambda    : {lambda_market:.6f}")

print("\n3 & 4 & 5. Konstruksi Matriks Payoff, Probabilitas, dan Fungsi Gelombang...")
def calculate_quantum_payoff(asset_L, asset_F):
    payoff_L = np.zeros((2, 2))
    payoff_F = np.zeros((2, 2))
    probs = np.zeros((2, 2))
    n_total = len(log_returns)
    for i in [0, 1]: # State Leader
        for j in [0, 1]: # State Follower
            # Filter data di mana state L=i dan state F=j
            mask = (states[asset_L] == i) & (states[asset_F] == j)
            n_ij = mask.sum()
            # Probabilitas Empiris (P_ij)
            p_ij = n_ij / n_total if n_total > 0 else 0
            probs[i, j] = p_ij
            # Ambil subset return
            subset_L = log_returns.loc[mask, asset_L]
            subset_F = log_returns.loc[mask, asset_F]
            # Hitung rata-rata dan std subset
            if n_ij > 0:
                mu_L, sig_L = subset_L.mean(), subset_L.std(ddof=0)
                mu_F, sig_F = subset_F.mean(), subset_F.std(ddof=0)
            else:
                mu_L, sig_L = 0, 0
                mu_F, sig_F = 0, 0
            # Utilitas Markowitz (Payoff)
            payoff_L[i, j] = (1 - lambda_market) * mu_L - lambda_market * sig_L
            payoff_F[i, j] = (1 - lambda_market) * mu_F - lambda_market * sig_F
    return payoff_L, payoff_F, probs

pairs = list(itertools.permutations(tickers, 2))
quantum_results = {}

for pair in pairs:
    asset_L, asset_F = pair
    pL, pF, prob = calculate_quantum_payoff(asset_L, asset_F)
    # Amplitudo Probabilitas / Koefisien Kuantum a_ij = sqrt(Probability_ij)
    quantum_coeffs = np.sqrt(prob)
    quantum_results[pair] = {
        'Payoff_L': pL,
        'Payoff_F': pF,
        'Probabilities': prob,
        'Quantum_Coeffs': quantum_coeffs
    }
    print(f"\n{'='*50}")
    print(f"Pasangan Leader: {asset_L} | Follower: {asset_F}")
    print(f"{'='*50}")
    print("Matriks Payoff Leader (U_L):")
    print(np.round(pL, 6))
    print("\nMatriks Payoff Follower (U_F):")
    print(np.round(pF, 6))
    print("\nQuantum Coefficients (a_00, a_01, a_10, a_11):")
    print(np.round(quantum_coeffs, 4))
    print(f"\nFungsi Gelombang |psi> : ")
    print(f"{quantum_coeffs[0,0]:.4f} |00> + {quantum_coeffs[0,1]:.4f} |01> + "
          f"{quantum_coeffs[1,0]:.4f} |10> + {quantum_coeffs[1,1]:.4f} |11>")
```

## Output Payoff
```text
1. Menghitung Log Return Harian dan State (0=Naik, 1=Turun)...

2. Menghitung Risk Aversion Endogen (Lambda Market) ...
   - Mu_avg    : -0.000141
   - Sigma_avg : 0.023395
   - Lambda    : 0.501508

3 & 4 & 5. Konstruksi Matriks Payoff, Probabilitas, dan Fungsi Gelombang...

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

==================================================
Pasangan Leader: BBCA.JK | Follower: ASII.JK
==================================================
Matriks Payoff Leader (U_L):
[[ 0.000379  0.002674]
 [-0.007749 -0.013675]]

Matriks Payoff Follower (U_F):
[[ 0.002092 -0.009162]
 [ 0.002314 -0.017807]]

Quantum Coefficients (a_00, a_01, a_10, a_11):
[[0.4752 0.4115]
 [0.508  0.5889]]

Fungsi Gelombang |psi> : 
0.4752 |00> + 0.4115 |01> + 0.5080 |10> + 0.5889 |11>

... (rest of the pairs)
```

## Mathematical Interpretation Payoff
Berdasarkan output matriks di atas, kita dapat merepresentasikan hubungan strategis antara aset Leader ($L$) dan Follower ($F$) ke dalam matriks payoff tunggal bergaya Game Theory $(U_L, U_F)$. Format ini memudahkan kita untuk melihat insentif setiap pihak pada setiap kombinasi pergerakan pasar.

### 1. Pasangan BBCA (Leader) - TPIA (Follower)
| BBCA \ TPIA | $\ket{0}_F$ (Up) | $\ket{1}_F$ (Down) |
| :--- | :---: | :---: |
| **$\ket{0}_L$ (Up)** | $(0.000588, 0.000624)$ | $(0.002103, -0.017209)$ |
| **$\ket{1}_L$ (Down)** | $(-0.008416, 0.001911)$ | $(-0.012949, -0.01679)$ |

**Interpretasi:**
- State $\ket{00}$ (Keduanya naik) memberikan payoff positif bagi keduanya, menandakan korelasi positif yang sehat.
- State $\ket{01}$ (BBCA naik, TPIA turun) memberikan payoff tertinggi bagi BBCA ($0.002103$), namun merugikan TPIA secara signifikan ($-0.017209$). Ini menunjukkan BBCA bisa tetap tangguh meskipun TPIA terkoreksi.

### 2. Pasangan BBCA (Leader) - ASII (Follower)
| BBCA \ ASII | $\ket{0}_F$ (Up) | $\ket{1}_F$ (Down) |
| :--- | :---: | :---: |
| **$\ket{0}_L$ (Up)** | $(0.000379, 0.002092)$ | $(0.002674, -0.009162)$ |
| **$\ket{1}_L$ (Down)** | $(-0.007749, 0.002314)$ | $(-0.013675, -0.017807)$ |

**Interpretasi:**
- State $\ket{00}$ memberikan keuntungan yang jauh lebih besar bagi ASII ($0.002092$) dibandingkan BBCA ($0.000379$), mengindikasikan ASII sangat diuntungkan saat "mengekori" kenaikan BBCA.
- State $\ket{11}$ (Keduanya turun) merupakan kondisi terburuk dengan utilitas negatif terdalam, mencerminkan risiko sistemik pada pasangan ini.

# Construct Density Matrix and QMI 12 Pair
## Note 1
---
### Konstruksi Fungsi Gelombang dan Matriks Payoff
Berdasarkan metodologi **Markowitz $\times$ Game Theory (Risk Aversion Endogen)** dan **Econophysics Kuantum**, berikut adalah langkah-langkah formulasi dari data historis hingga mendapatkan fungsi gelombang $|\psi\rangle$.
#### 1. Perhitungan Return dan Penentuan State
Pertama, kita menghitung *Daily Log Return* ($R_t$) untuk mengidentifikasi pergerakan harga harian. $$ R_t = \ln\left(\frac{P_t}{P_{t-1}}\right) $$
Setiap hari perdagangan kemudian didiskritisasi ke dalam dua *state* kuantum:
- **Naik ($|0\rangle$)**: Jika $R_t > 0$
- **Turun ($|1\rangle$)**: Jika $R_t \le 0$  

#### 2. Risk Aversion Endogen ($\lambda_{\text{market}}$)
Alih-alih berasumsi menggunakan angka statis, kecenderungan penghindaran risiko (risk aversion) pasar dihitung berdasarkan volatilitas agregat:$$ \lambda_{\text{market}} = \frac{1}{1 + e^{\left(\frac{\mu_{avg}}{\sigma_{avg}}\right)}} $$
- $\mu_{avg}$: Rata-rata *return* seluruh aset dalam pasar/portofolio.
- $\sigma_{avg}$: Rata-rata volatilitas (standar deviasi) seluruh aset.
#### 3. Konstruksi Matriks Payoff (Utilitas Markowitz)
Misalkan kita mengamati dua aset: **Leader ($L$)** dan **Follower ($F$)**. Kita menghitung utilitas objektif Markowitz untuk masing-masing aset berdasarkan subset waktu berlakunya state gabungan $|ij\rangle$ (misal: Leader naik, Follower turun).

Fungsi utilitas untuk aset $k \in \{L, F\}$ pada state $|ij\rangle$ adalah:$$ U_k^{(ij)} = (1 - \lambda_{\text{market}}) \cdot \mu_{k}^{(ij)} - \lambda_{\text{market}} \cdot \sigma_{k}^{(ij)} $$
- $\mu_{k}^{(ij)}$: Rata-rata return harian aset $k$ HANYA pada hari-hari di mana state $|ij\rangle$ terjadi.
- $\sigma_{k}^{(ij)}$: Standar deviasi return harian aset $k$ pada hari-hari tersebut.  

Matriks Payoff untuk pasangan $(L, F)$ kemudian dapat divisualisasikan sebagai tabel interaksi (Game Theory):

| L \ F                  |      $\ket{0}_F$ (Up)      |     $\ket{1}_F$ (Down)     |
| :--------------------- | :------------------------: | :------------------------: |
| **$\ket{0}_L$ (Up)**   | $(U_L^{(00)}, U_F^{(00)})$ | $(U_L^{(01)}, U_F^{(01)})$ |
| **$\ket{1}_L$ (Down)** | $(U_L^{(10)}, U_F^{(10)})$ | $(U_L^{(11)}, U_F^{(11)})$ |
#### 4. Probabilitas State Bersama ($P_{ij}$)
Kita menghitung seberapa sering gabungan pergerakan aset ini terjadi. Jika total hari pengamatan adalah $N$ dan gabungan state $|ij\rangle$ terjadi sebanyak $n_{ij}$ kali, maka probabilitas empirisnya:
$$ P_{ij} = \frac{n_{ij}}{N} $$
*(Catatan: $P_{00} + P_{01} + P_{10} + P_{11} = 1$)*
#### 5. Fungsi Gelombang Kuantum ($|\psi\rangle$)
Terakhir, kita merepresentasikan probabilitas bersama ini ke dalam formalisme mekanika kuantum. Amplitudo probabilitas (*Quantum Coefficient*), $a_{ij}$, adalah akar kuadrat dari probabilitas empiris:$$ a_{ij} = \sqrt{P_{ij}} $$
Sehingga fungsi gelombang sistem dua aset tersebut (Leader-Follower) diekspresikan sebagai superposisi linear dari semua kemungkinan state:$$ |\psi\rangle = a_{00} |00\rangle + a_{01} |01\rangle + a_{10} |10\rangle + a_{11} |11\rangle $$
Fungsi gelombang $|\psi\rangle$ inilah yang nantinya kita observasi untuk mencari *Quantum Mutual Information* (seberapa kuat keterikatan/entanglement antara aset L dan F) serta matriks densitas $\rho = |\psi\rangle\langle\psi|$.
$$ I(L : F) = S(\rho_L) + S(\rho_F) - S(\rho_{LF}) $$
$$ J_{LF} = I(L:F) $$

## Code 1
```python
import numpy as np
from scipy.linalg import eigh

print("6. Menghitung Reduced Density Matrix, Entropi Von Neumann, dan Quantum Mutual Information\n")

def vn_entropy(rho):
    # Menghitung Von Neumann Entropy: -Tr(rho * ln(rho))
    # Menggunakan dekomposisi nilai eigen karena matriks Hermite/Simetris
    evals = eigh(rho)[0] # eigh untuk matriks Hermite mengembalikan eigenvalues array terurut
    # Toleransi untuk membuang eigen value 0 (karena 0 * ln(0) limitnya adalah 0)
    evals = np.clip(evals, 1e-12, 1.0)
    entropy_val = -np.sum(evals * np.log(evals))
    return entropy_val

# Dictionary untuk menyimpan nilai interaksi J_ij (QMI)
interaction_J = {}

for pair, res in quantum_results.items():
    asset_L, asset_F = pair
    a = res['Quantum_Coeffs'] # Matriks 2x2 amplitudes
    # 1. State Vector (4x1)
    # Rata kanan (flatten) mengikuti urutan: |00>, |01>, |10>, |11>
    psi = np.array([a[0,0], a[0,1], a[1,0], a[1,1]])
    # 2. Matriks Densitas Sistem Keseluruhan (4x4)
    # rho = |psi><psi|
    rho_system = np.outer(psi, psi)
    # 3. Partial Trace untuk Rho_Leader (2x2)
    rho_L = np.array([
        [psi[0]*psi[0] + psi[1]*psi[1], psi[0]*psi[2] + psi[1]*psi[3]],
        [psi[2]*psi[0] + psi[3]*psi[1], psi[2]*psi[2] + psi[3]*psi[3]]
    ])
    # Partial Trace untuk Rho_Follower (2x2)
    rho_F = np.array([
        [psi[0]*psi[0] + psi[2]*psi[2], psi[0]*psi[1] + psi[2]*psi[3]],
        [psi[1]*psi[0] + psi[3]*psi[2], psi[1]*psi[1] + psi[3]*psi[3]]
    ])
    # 4. Menghitung Entropi Sistem secara terpisah
    S_L = vn_entropy(rho_L)
    S_F = vn_entropy(rho_F)
    S_system = vn_entropy(rho_system)
    # 5. Quantum Mutual Information
    I_LF = S_L + S_F - S_system
    # Nilai QMI ini akan kita pakai sebagai Kekuatan Interaksi J (Ising Hamiltonian)
    interaction_J[pair] = I_LF
    print(f"--- QMI untuk Pasangan [{asset_L} dan {asset_F}] ---")
    print(f"Entropi Von Neumann {asset_L} (S_L) : {S_L:.4f}")
    print(f"Entropi Von Neumann {asset_F} (S_F) : {S_F:.4f}")
    print(f"Joint Entropy Sistem (S_LF)       : {S_system:.4f}")
    print(f"Quantum Mutual Info / J_LF (I)    : {I_LF:.4f}\n")
```

# Bias Determination
## Note 1
---

### Konstruksi Parameter Bias ($h$) untuk Ising Hamiltonian

Setelah mendapatkan nilai kekuatan interaksi ($J_{ij}$) dari Quantum Mutual Information, langkah berikutnya menuju penyusunan model **Ising Hamiltonian** ($H$) adalah menentukan **Parameter Bias ($h_i$)** untuk masing-masing aset (Leader dan Follower).

#### Menghitung Bias dari Matriks Payoff
Nilai Bias dihitung dari **selisih total ekspektasi utilitas (Payoff) ketika aset tersebut naik dibandingkan ketika ia turun**.

**Untuk Aset Leader (L):**
$$ h_L = \frac{(U_L^{(00)} + U_L^{(01)}) - (U_L^{(10)} + U_L^{(11)})}{2} $$

**Untuk Aset Follower (F):**
$$ h_F = \frac{(U_F^{(00)} + U_F^{(10)}) - (U_F^{(01)} + U_F^{(11)})}{2} $$

#### Makna Nilai $h_i$
- Jika **$h_i > 0$**, ini secara dominan mengindikasikan struktur utilitas mendukung aset $i$ untuk berada di kondisi Uptrend/Naik ($|0\rangle$).
- Jika **$h_i < 0$**, utilitas secara dominan mendikte aset $i$ untuk berada di kondisi Downtrend/Turun ($|1\rangle$).

## Code 1
```python
print("7. Menghitung Parameter Bias (h) dari Matriks Payoff\n")

# Dictionary untuk menyimpan nilai Bias individual h_i 
bias_h = {ticker: [] for ticker in tickers}

for pair, res in quantum_results.items():
    asset_L, asset_F = pair
    pL = res['Payoff_L']
    pF = res['Payoff_F']
    # --- Bias Leader (L) ---
    U_L_Up = pL[0, 0] + pL[0, 1]
    U_L_Down = pL[1, 0] + pL[1, 1]
    h_L = (U_L_Up - U_L_Down) / 2
    # --- Bias Follower (F) ---
    U_F_Up = pF[0, 0] + pF[1, 0]
    U_F_Down = pF[0, 1] + pF[1, 1]
    h_F = (U_F_Up - U_F_Down) / 2
    
    bias_h[asset_L].append(h_L)
    bias_h[asset_F].append(h_F)
    print(f"--- Bias untuk Pasangan [{asset_L} dan {asset_F}] ---")
    print(f"Bias {asset_L} (h_L) : {h_L:.6f}")
    print(f"Bias {asset_F} (h_F) : {h_F:.6f}\n")

print("--- Rata-Rata Bias Keseluruhan untuk Masing-Masing Qubit (Saham) ---")
final_bias = {}
for ticker, h_values in bias_h.items():
    if len(h_values) > 0:
        avg_h = np.mean(h_values)
        final_bias[ticker] = avg_h
        trend = "Cenderung Naik (Uptrend)" if avg_h > 0 else "Cenderung Turun (Downtrend)"
        print(f"Saham {ticker:8s} | h_i = {avg_h:>10.6f}  => {trend}")
```

## Output 1
```text
7. Menghitung Parameter Bias (h) dari Matriks Payoff

--- Bias untuk Pasangan [BBCA.JK dan TPIA.JK] ---
Bias BBCA.JK (h_L) : 0.012028
Bias TPIA.JK (h_F) : 0.018267

--- Bias untuk Pasangan [BBCA.JK dan ASII.JK] ---
Bias BBCA.JK (h_L) : 0.012239
Bias ASII.JK (h_F) : 0.015688

--- Rata-Rata Bias Keseluruhan untuk Masing-Masing Qubit (Saham) ---
Saham BBCA.JK  | h_i =   0.012153  => Cenderung Naik (Uptrend)
Saham TPIA.JK  | h_i =   0.018402  => Cenderung Naik (Uptrend)
Saham ASII.JK  | h_i =   0.017347  => Cenderung Naik (Uptrend)
Saham TLKM.JK  | h_i =   0.017801  => Cenderung Naik (Uptrend)
```

## Calculation 1
### Contoh Kalkulasi Numerik: Parameter Bias ($h$)

Mari kita ambil contoh salah satu *output* matriks pada sel Python di atas, yaitu untuk Pasangan **Leader: BBCA** dan **Follower: ASII**:

```text
Matriks Payoff Leader (U_L) BBCA:
[[ 0.000379  0.002674]
 [-0.007749 -0.013675]]

Matriks Payoff Follower (U_F) ASII:
[[ 0.002092 -0.009162]
 [ 0.002314 -0.017807]]
```

#### 1. Menghitung Bias ($h_L$) untuk Leader (BBCA)
- **Ekspektasi Total BBCA Naik ($|0\rangle_L$)**: 
  $$ U_L^{(00)} + U_L^{(01)} = 0.000379 + 0.002674 = 0.003053 $$
- **Ekspektasi Total BBCA Turun ($|1\rangle_L$)**: 
  $$ U_L^{(10)} + U_L^{(11)} = -0.007749 + (-0.013675) = -0.021424 $$

Maka, nilai **Bias Intrinsik BBCA**:
$$ h_L = \frac{0.003053 - (-0.021424)}{2} = \frac{0.024477}{2} = 0.0122385 \approx 0.012239 $$

#### 2. Menghitung Bias ($h_F$) untuk Follower (ASII)
- **Ekspektasi Total ASII Naik ($|0\rangle_F$)**: 
  $$ U_F^{(00)} + U_F^{(10)} = 0.002092 + 0.002314 = 0.004406 $$
- **Ekspektasi Total ASII Turun ($|1\rangle_F$)**: 
  $$ U_F^{(01)} + U_F^{(11)} = -0.009162 + (-0.017807) = -0.026969 $$

Maka, nilai **Bias Intrinsik ASII**:
$$ h_F = \frac{0.004406 - (-0.026969)}{2} = \frac{0.031375}{2} = 0.0156875 \approx 0.015688 $$

*(Catatan: Karena nilai $h$ kini bernilai **positif**, maka kecenderungan pergerakan saham secara mikroskopis (medan magnet) adalah lebih stabil pada state **Naik (Uptrend)** $|0\rangle$ berdasar struktur utilitas terbaru.)*


# VQE
## Note 1
### Konstruksi Hamiltonian Constraint (Penalti Jumlah Portofolio)

  

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