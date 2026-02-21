dokumen ini adalah struktur proposal yang berisi bagian, bab, subbab, dan poin-poin yang akan ditulis.

# STRUKTUR PROPOSAL: OPTIMASI PORTOFOLIO DUA ASET DENGAN QUANTUM GAME THEORY (EWL) BERBASIS VQE

# BAB 1: PENDAHULUAN
## 1.1 Latar Belakang
- Fenomena korelasi tinggi antar aset saat krisis keuangan (Financial Dilemma).
- Keterbatasan metode optimasi klasik (Mean-Variance) dalam menangkap interaksi strategis.
- Potensi Quantum Computing dalam optimasi finansial.
## 1.2 Rumusan Masalah
- Bagaimana memodelkan korelasi aset ke dalam skema permainan kuantum EWL?
- Bagaimana efektivitas VQE dalam mencari Nash Equilibrium pada portofolio?
## 1.3 Tujuan Penelitian
## 1.4 Batasan Masalah (2 Aset, Skema EWL, Simulator Qiskit/Pennylane)

# BAB 2: TINJAUAN PUSTAKA
## 2.1 Diversifikasi Portofolio & Analisis Finansial
- **Modern Portfolio Theory (MPT):** Konsep Efficient Frontier dan Risk-Return Trade-off.
- **Teori Ekonomi Pendukung:** Auction Theory, Supply and Demand, dan Risk Aversion Endogen.
- **Time Series Analysis:** Korelasi, Volatilitas, dan Expected Return.
- **Indikator Kinerja:** Sharpe Ratio vs Trend Ratio.

## 2.2 Game Theory (Klasik)
- **Definisi & Model Matematika:** Payoff Matrix, Nash Equilibrium, dan Pareto Optimum.
- **Klasifikasi Permainan:** Coordination, Anti-Coordination, dan Mixed Strategy Game.
- **Model Strategis Sekuensial:**
    - **Prisoner's Dilemma:** Analogi kegagalan pasar/bearish market.
    - **Model Stackelberg:** Dinamika Leader-Follower, asimetri informasi, dan logika *Backward Induction* dalam pengambilan keputusan aset.

## 2.3 Teori Informasi Kuantum & Game Theory
- **Kuantisasi EWL (Eisert-Wilkens-Lewenstein):** Operator Entangling ($\hat{J}$) dan strategi Unitary.
- **Matriks Densitas ($\rho$):** Representasi keadaan statistik sistem aset.
- **Von Neumann Entropy:** Pengukuran ketidakpastian dalam sistem kuantum ($S = -\text{Tr}(\rho \ln \rho)$).
- **Quantum Mutual Information (QMI):** Pengukuran korelasi total antar aset melalui sharing information.

## 2.4 Quantum Algorithm (VQE)
- **Dasar Matematika:** Persamaan Eigen ($H|\psi\rangle = E|\psi\rangle$) dan Prinsip Variasi.
- **Variational Quantum Eigensolver:** Algoritma hibrid sebagai pencari Ground State (strategi optimal).
- **Struktur Ansatz (Parameterized Quantum Circuit):**
    - **Rotasi Qubit Tunggal ($U_{rot}$):** Peran gerbang $R_y$ dan $R_z$ dalam pemetaan ruang strategi.
    - **Layer Entanglement ($U_{ent}$):** Penggunaan gerbang CNOT untuk memodelkan interdependensi aset.
    - **Hardware-Efficient Ansatz (HEA):** Keseimbangan antara ekspresibilitas sirkuit dan kedalaman (depth).
- **Teknik Optimasi Klasik:**
    - **SPSA:** Penurunan rumus pendekatan gradien melalui perturbasi simultan (efisiensi pengukuran).
    - **COBYLA:** Logika optimasi berbasis *linear approximation* dan *trust region* tanpa gradien.
- **Formulasi Ising Hamiltonian:**
    - Transformasi QUBO ke model Ising.
    - Pemetaan variabel biner ($0,1$) ke operator Pauli-Z ($\sigma^z$).

# BAB 3: METODOLOGI PENELITIAN
## 3.1 Alur Penelitian (Flowchart)
## 3.2 Pengumpulan Data & Pra-pemrosesan
- Akuisisi data LQ45 via Yahoo Finance.
- **Diskretisasi Biner:** Penentuan state $|0\rangle$ (Up) dan $|1\rangle$ (Down).
- **Laplace Smoothing:** Stabilisasi probabilitas untuk perhitungan entropi.

## 3.3 Konstruksi Model Permainan (Mapping Pipeline)
- **Konstruksi Matriks Payoff:** Perhitungan utilitas Markowitz dengan $\lambda$ endogen.
- **Pemodelan Dinamika Stackelberg:**
    - Identifikasi peran Leader-Follower berbasis kapitalisasi pasar (Market Cap).
    - Konstruksi payoff asimetris berdasarkan prediksi respon Follower terhadap strategi Leader.
- **Ekstraksi Parameter Hamiltonian:**
    - Penentuan **Bias ($h_i$)** dari nilai payoff marginal tiap aset.
    - Penentuan **Interaksi ($J_{ij}$)** berbasis nilai Quantum Mutual Information (QMI).
- **Klasifikasi Tipe Permainan:** Identifikasi dinamika pasar (Coordination/Anti-Coordination).

## 3.4 Implementasi Kuantum & Optimasi
- **Konstruksi Hamiltonian Total:** 
    - **Cost Hamiltonian ($H_{cost}$):** $H = \sum h_i Z_i + \sum J_{ij} Z_i Z_j$.
    - **Constraint Hamiltonian ($H_{constraint}$):** Penalti kuadratik untuk batasan pemilihan aset ($K$).
- **Konfigurasi VQE:** Penentuan jumlah layer (depth), inisialisasi parameter $\theta$, dan setting jumlah sampling (shots).
- **Proses Iterasi SPSA:** 
    - Penentuan *gain sequences* ($a_k, c_k$) untuk stabilitas konvergensi.
    - Evaluasi fungsi biaya dan pembaruan parameter secara stokastik).

## 3.5 Evaluasi dan Analisis Kinerja
- **Identifikasi State Optimal:** Ekstraksi bitstring dengan probabilitas tertinggi.
- **Backtesting & Validasi:** Perbandingan Sharpe Ratio dan Trend Ratio antara strategi Kuantum dan Klasik.
