# BAB 3: METODOLOGI PENELITIAN

## 3.1 Alur Penelitian
Penelitian ini dilakukan dengan pendekatan eksperimental simulasi komputasi. Tahapan penelitian dibagi menjadi lima fase utama:
1.  **Pengumpulan Data:** Akuisisi data harga saham historis.
2.  **Pemodelan Game Theory Klasik:** Konstruksi matriks *Payoff* berdasarkan *return* dan risiko.
3.  **Kuantisasi (Encoding):** Transformasi masalah ke dalam bentuk Operator Hamiltonian.
4.  **Implementasi VQE:** Eksekusi algoritma kuantum variasional dengan skema EWL.
5.  **Evaluasi & Analisis:** Perbandingan kinerja portofolio kuantum vs klasik.

## 3.2 Pengumpulan dan Pra-pemrosesan Data
*   **Objek:** Dua aset saham ($N=2$) dengan kapitalisasi pasar besar (Blue Chip) yang memiliki korelasi historis tinggi (misalnya: sektor perbankan atau teknologi).
*   **Sumber Data:** *Yahoo Finance* (menggunakan library Python `yfinance`).
*   **Periode:** Data harian (*Adjusted Close*) selama 5-10 tahun terakhir.
*   **Preprocessing:**
    *   Menghitung *Logarithmic Returns* harian: $R_t = \ln(P_t / P_{t-1})$.
    *   Menghitung *Expected Return* ($\mu$) dan Matriks Kovarians ($\Sigma$).

## 3.3 Konstruksi Model Permainan (Game Modeling)

### 3.3.1 Definisi Strategi
Setiap aset dianggap sebagai "Pemain".
*   **Strategi $C$ (Cooperate):** Alokasi bobot tinggi / Beli.
*   **Strategi $D$ (Defect):** Alokasi bobot rendah / Tahan (atau Jual).

### 3.3.2 Matriks Payoff ($M$)
Matriks *payoff* 2x2 dikonstruksi untuk merepresentasikan keuntungan portofolio pada berbagai kondisi kombinasi strategi.
$$
M = \begin{pmatrix}
(CC) & (CD) \\
(DC) & (DD)
\end{pmatrix}
$$
*   Nilai entri matriks dihitung berdasarkan fungsi utilitas Markowitz ($U = \mu_p - \frac{\lambda}{2}\sigma_p^2$) atau *Trend Ratio* untuk setiap kombinasi bobot.

### 3.3.3 Pemetaan ke Hamiltonian ($H$)
Agar dapat diproses oleh VQE, matriks *payoff* klasik ($M$) dipetakan menjadi operator Hermitian (Hamiltonian). Karena VQE mencari energi minimum (Ground State), sedangkan tujuan investasi adalah maksimasi profit, maka Hamiltonian didefinisikan sebagai negasi dari Payoff:
$$ H = - \sum_{i,j \in \{0,1\}} M_{ij} |ij\rangle\langle ij| $$
Dalam bentuk *Pauli Strings* (untuk 2 Qubit), ini dapat didekomposisi menjadi:
$$ H = c_0 I + c_1 Z_0 + c_2 Z_1 + c_3 Z_0 Z_1 $$
Dimana $Z$ adalah Pauli-Z operator.

## 3.4 Desain Sirkuit VQE (Skema EWL)

Simulasi dilakukan menggunakan kerangka kerja **Pennylane** atau **Qiskit**.

### 3.4.1 Inisialisasi State
Keadaan awal qubit dimulai dari $|00\rangle$.

### 3.4.2 Operator Entanglement ($\hat{J}$)
Sesuai skema EWL, operator ini menciptakan korelasi kuantum antar pemain sebelum strategi dipilih.
$$ \hat{J} = e^{-i \frac{\\gamma}{2} \sigma_x \otimes \sigma_x} $$
Untuk $\\gamma = \pi/2$, ini menciptakan *Maximal Entanglement*. Dalam sirkuit, ini diimplementasikan menggunakan kombinasi gerbang **CNOT** dan **Rotasi X ($R_x$)**.

### 3.4.3 Ansatz (Strategi Pemain)
Menggunakan **Hardware Efficient Ansatz** (atau *RyRz Ansatz*) untuk merepresentasikan strategi pemain yang akan dioptimasi.
*   Parameter: $\\vec{\\theta}$ (sudut rotasi).
*   Gerbang: Rotasi qubit tunggal ($R_y, R_z$) diikuti oleh *entangling layer* (CNOT) jika kedalaman sirkuit $>1$.
*   Bentuk Unitary: $U(\\theta) = \prod_{l} U_{ent} \prod_{q} R_y(\\theta_{l,q})$.

### 3.4.4 Pengukuran (Cost Function)
Sirkuit diakhiri dengan operator *inverse entanglement* $\\hat{J}^\dagger$. Nilai ekspektasi Hamiltonian dihitung:
$$ \mathcal{L}(\\theta) = \langle \psi(\\theta) | H | \psi(\\theta) \rangle $$
Tujuan VQE adalah mencari $\theta^*$ yang meminimalkan $\\mathcal{L}$.

## 3.5 Optimasi Klasik
*   **Optimizer:** COBYLA (*Constrained Optimization by Linear Approximation*).
*   **Alasan:** Efisien untuk masalah dengan jumlah evaluasi fungsi terbatas dan tidak memerlukan perhitungan gradien (*gradient-free*), cocok untuk simulasi variasi stokastik pasar.
*   **Iterasi:** Parameter $\\theta$ diperbarui berulang kali hingga nilai ekspektasi konvergen.

## 3.6 Evaluasi Kinerja (Metrics)
Bobot portofolio optimal yang dihasilkan oleh strategi kuantum akan dievaluasi dan dibandingkan dengan strategi klasik (*Mean-Variance* standar) menggunakan indikator:
1.  **Trend Ratio:** Mengukur kemiringan garis tren dibagi volatilitas deviasi (fokus utama penelitian).
2.  **Sharpe Ratio:** *Excess return* per unit varians.
3.  **Maximum Drawdown (MDD):** Risiko penurunan maksimum dari puncak ke lembah.
