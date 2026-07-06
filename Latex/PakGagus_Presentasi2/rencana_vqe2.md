# Rencana Presentasi: Optimasi Portofolio dengan VQE

Dokumen ini merinci rencana presentasi berdasarkan replikasi kode pada `VQE_2.ipynb`.

## 1. Judul Presentasi
**Optimasi Portofolio Menggunakan Variational Quantum Eigensolver (VQE)**
*Subtitle: Replikasi Studi Kasus pada Saham Teknologi*

---

## 2. Struktur Slide

### Slide 1: Pendahuluan & Latar Belakang
*   **Poin Utama:**
    *   Masalah Optimasi Portofolio: Menyeimbangkan keuntungan (return) dan risiko (risk).
    *   Pendekatan Klasik: Modern Portfolio Theory (Markowitz).
    *   Pendekatan Kuantum: Menggunakan algoritma hibrid VQE untuk menyelesaikan masalah kombinatorial yang kompleks.
*   **Visualisasi:** Ilustrasi sederhana perbandingan grafik Risk vs Return.

### Slide 2: Formulasi Matematis (Markowitz ke QUBO)
*   **1. Fungsi Objektif Awal (Markowitz):**
    Tujuan kita adalah meminimalkan risiko (varians) sambil memaksimalkan *expected return*.
    $$ \text{Minimize} \quad w \underbrace{\sum_{i,j} \sigma_{ij} x_i x_j}_{\text{Risk (Variance)}} - (1-w) \underbrace{\sum_i \mu_i x_i}_{\text{Return}} $$
    *   $x_i \in \{0, 1\}$: Variabel biner (pilih aset atau tidak).
    *   $w$: Parameter penghindaran risiko (risk aversion).

*   **2. Constraint (Kendala):**
    Kita ingin memilih tepat sejumlah $B$ aset.
    $$ \sum_{i=1}^N x_i = B $$

*   **3. Metode Penalti (Unconstrained Optimization):**
    Agar dapat diselesaikan dengan VQE (yang mencari energi terendah tanpa kendala eksplisit), kendala diubah menjadi *penalty term* kuadratik. Jika syarat tidak terpenuhi, nilai fungsi akan meledak tinggi.
    $$ \text{Penalty} = P \left( \sum_{i=1}^N x_i - B \right)^2 $$

*   **4. Total Cost Function (Persamaan Akhir):**
    Menggabungkan objektif dan penalti menghasilkan persamaan Hamiltonian/Biaya total:
    $$ C(x) = w x^T \Sigma x - (1-w) \mu^T x + P \left( \sum x_i - B \right)^2 $$

### Slide 3: Mapping ke Hamiltonian Kuantum
*   **Poin Utama:**
    *   Bagaimana komputer kuantum memahami masalah ini?
    *   Mapping variabel biner $x_i \in \{0, 1\}$ ke operator spin/qubit $Z_i$.
    *   Transformasi: $x_i \rightarrow \frac{1-Z_i}{2}$.
    *   Hasil akhirnya adalah **Ising Hamiltonian** yang akan diminimalkan energinya oleh VQE.

### Slide 4: Persiapan Data & Studi Kasus
*   **Poin Utama:**
    *   Aset yang digunakan: AAPL, GOOGL, MSFT, AMZN, TSLA (5 Aset Teknologi).
    *   Sumber Data: Yahoo Finance (2020-2021).
    *   Parameter:
        *   Risk Aversion ($w$) = 0.5
        *   Budget ($B$) = 2 aset
*   **Visualisasi:** Tabel/Grafik `Expected Returns` dan `Covariance Matrix` dari notebook.

### Slide 5: Implementasi VQE dengan PennyLane
*   **Poin Utama:**
    *   Framework: PennyLane.
    *   **Ansatz:** Menggunakan *Hardware-efficient ansatz* (`BasicEntanglerLayers`) 3 layer.
    *   **Optimizer:** Gradient Descent Klasik untuk mengupdate parameter sirkuit kuantum.
    *   Proses: Loop hibrid (Quantum Circuit $\leftrightarrow$ Classical Optimizer).

### Slide 6: Hasil Optimasi
*   **Poin Utama:**
    *   Grafik Konvergensi: Penurunan nilai Cost function seiring iterasi (0 s.d 100).
    *   Probabilitas State Akhir: State dengan probabilitas tertinggi adalah solusi optimal.
*   **Hasil:**
    *   Optimal State (Binary): `01001` (Contoh dari notebook).
    *   Aset Terpilih: **GOOGL** dan **TSLA**.

### Slide 7: Kesimpulan
*   **Poin Utama:**
    *   VQE berhasil mereplikasi pemilihan portofolio optimal yang mematuhi constraint.
    *   Demonstrasi potensi algoritma kuantum jangka pendek (NISQ) untuk masalah keuangan.
    *   Langkah selanjutnya: Meningkatkan jumlah aset atau menggunakan *Real device*.

---

## 3. Aset Gambar yang Dibutuhkan
Untuk mempersiapkan slide ini, kita perlu mengambil (screenshot/export) aset berikut dari notebook `VQE_2.ipynb`:
1.  **Tabel Data:** Head dari dataframe harga saham.
2.  **Covariance Matrix:** Output print nilai covariance matrix.
3.  **Grafik Konvergensi:** Plot `Cost vs Iterations`.
4.  **Histogram Probabilitas:** (Opsional) Plot probabilitas output sirkuit.

---

## 4. Cara Mendapatkan Visualisasi (Script Otomatis)

Karena gambar-gambar tersebut perlu replikasi persis dari `VQE_2.ipynb`, saya telah membuat script Python `generate_assets.py` yang menggunakan parameter yang sama:
*   **Tickers:** AAPL, GOOGL, MSFT, AMZN, TSLA.
*   **W (Risk Aversion):** 0.5.
*   **B (Budget):** 2.
*   **P (Penalty):** 10.0.
*   **Layers:** 3.
*   **Iterations:** 100.
*   **Seed:** 0.

### Instruksi Penggunaan:
1.  Jalankan script dengan perintah:
    ```bash
    python generate_assets.py
    ```
2.  File gambar berikut akan dihasilkan untuk slide:
    *   **`risk_vs_return.png`**: Ilustrasi konsep (Slide 1).
    *   **`expected_returns.png`**: Data return (Slide 4).
    *   **`covariance_matrix.png`**: Heatmap kovarians (Slide 4).
    *   **`vqe_convergence.png`**: Grafik konvergensi 100 iterasi (Slide 6).
    *   **`probability_histogram.png`**: Probabilitas hasil akhir (Slide 6).

### Source Code (`generate_assets.py`)
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import pennylane as qml

# Konfigurasi sesuai VQE_2.ipynb
TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
START_DATE = "2020-01-01"
END_DATE = "2021-01-01"
W = 0.5
B = 2
P = 10.0
N_LAYERS = 3
MAX_ITERATIONS = 100
STEPSIZE = 0.1
SEED = 0

def plot_risk_return():
    np.random.seed(42)
    returns = np.linspace(0.05, 0.25, 100)
    risks = 0.1 + 2 * (returns - 0.05)**2 + 0.02 * np.random.normal(0, 0.1, 100)
    plt.figure(figsize=(8, 6))
    plt.plot(risks, returns, 'b-', label='Efficient Frontier', linewidth=2)
    plt.scatter(risks + np.random.rand(100)*0.1, returns - np.random.rand(100)*0.05, c='gray', alpha=0.5, s=10)
    plt.title("Konsep: Risk vs Return (Efficient Frontier)")
    plt.xlabel("Risk (Standard Deviation)")
    plt.ylabel("Expected Return")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("risk_vs_return.png")
    plt.close()

def plot_data_visuals():
    data = yf.download(TICKERS, start=START_DATE, end=END_DATE, progress=False, auto_adjust=False)
    df = data['Adj Close']
    returns = df.pct_change().dropna()
    mu = returns.mean().to_numpy()
    sigma = returns.cov().to_numpy()
    
    plt.figure(figsize=(8, 5))
    pd.Series(mu, index=TICKERS).plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Expected Daily Returns (Replikasi)")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig("expected_returns.png")
    plt.close()
    
    plt.figure(figsize=(8, 6))
    plt.imshow(sigma, cmap='coolwarm')
    plt.colorbar(label='Covariance')
    plt.xticks(range(len(TICKERS)), TICKERS)
    plt.yticks(range(len(TICKERS)), TICKERS)
    plt.title("Covariance Matrix Heatmap (Replikasi)")
    plt.savefig("covariance_matrix.png")
    plt.close()
    return mu, sigma

def run_vqe_visuals(mu, sigma):
    N = len(TICKERS)
    coeffs, ops = [], []
    for i in range(N):
        coeff_x = -(1-W) * mu[i] + W * sigma[i,i] + P * (1 - 2*B)
        coeffs.extend([0.5 * coeff_x, -0.5 * coeff_x])
        ops.extend([qml.Identity(i), qml.PauliZ(i)])
        for j in range(i+1, N):
            coeff_xx = 2 * W * sigma[i,j] + 2 * P
            coeffs.extend([0.25*coeff_xx, -0.25*coeff_xx, -0.25*coeff_xx, 0.25*coeff_xx])
            ops.extend([qml.Identity(0), qml.PauliZ(i), qml.PauliZ(j), qml.PauliZ(i)@qml.PauliZ(j)])
    coeffs.append(P * B**2)
    ops.append(qml.Identity(0))
    H = qml.Hamiltonian(coeffs, ops)
    dev = qml.device("default.qubit", wires=N)
    def ansatz(params, wires): qml.BasicEntanglerLayers(weights=params, wires=wires)
    @qml.qnode(dev)
    def cost_function(params):
        ansatz(params, wires=range(N))
        return qml.expval(H)
    shape = qml.BasicEntanglerLayers.shape(n_layers=N_LAYERS, n_wires=N)
    np.random.seed(SEED)
    params = np.random.random(shape)
    opt = qml.GradientDescentOptimizer(stepsize=STEPSIZE)
    costs = []
    for i in range(MAX_ITERATIONS):
        params, cost = opt.step_and_cost(cost_function, params)
        costs.append(cost)
    plt.figure(figsize=(8, 5))
    plt.plot(costs, 'b-')
    plt.title("VQE Optimization Convergence (Replikasi)")
    plt.xlabel("Iterations"); plt.ylabel("Cost")
    plt.grid(True, alpha=0.3)
    plt.savefig("vqe_convergence.png")
    plt.close()
    
    @qml.qnode(dev)
    def probability_circuit(params):
        ansatz(params, wires=range(N))
        return qml.probs(wires=range(N))
    probs = probability_circuit(params)
    plt.figure(figsize=(10, 5))
    plt.bar([format(i, f'0{N}b') for i in range(2**N)], probs, color='purple')
    plt.title("Final State Probabilities (Replikasi)")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("probability_histogram.png")
    plt.close()

if __name__ == "__main__":
    plot_risk_return()
    mu, sigma = plot_data_visuals()
    run_vqe_visuals(mu, sigma)
```