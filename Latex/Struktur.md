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
## 2.1 Dasar Analisis Teknikal & Representasi Data Finansial
- **Visualisasi Runtun Waktu (Time-Series):**
    - Grafik Harga: Sumbu-X sebagai waktu ($t$) dan Sumbu-Y sebagai harga ($P$).
    - Fluktuasi Harga sebagai pergerakan stokastik dalam koordinat harga-waktu.
- **Anatomi Candlestick (OHLC):**
    - Open, High, Low, Close: Empat variabel utama dalam jendela waktu ($\Delta t$).
    - Interpretasi Visual: Body dan Wick sebagai indikator momentum pasar.
- **Timeframe & Sampling Data:**
    - Penentuan resolusi data (Daily, Hourly, dll) dan sifat stokastik sistem.
    - Transformasi dari Harga ($P_t$) ke *Logarithmic Returns* ($R_t$) untuk mencapai stasioneritas.

## 2.2 Dinamika Pasar & Analisis Fundamental
- **Mekanisme Penggerak Harga:**
    - **Teori Lelang (Auction Theory):** Proses *price discovery* melalui interaksi *bid* (permintaan) dan *ask* (penawaran).
    - **Hukum Penawaran dan Permintaan (Supply and Demand):** Ketidakseimbangan (*imbalance*) volume sebagai gaya penggerak utama perubahan harga.
- **Analisis Fundamental & Rasio Keuangan:**
    - **Metrik Valuasi:** Price-to-Earnings (P/E) Ratio, Dividend Yield, dan Earnings Per Share (EPS) sebagai indikator nilai intrinsik.
    - **Metrik Risiko-Return:** Sharpe Ratio, Sortino Ratio, dan Trend Ratio.
- **Makroekonomi & Siklus Pasar:**
    - **Rezim Pasar:** Karakteristik fase Bullish, Bearish, dan Sideways sebagai keadaan sistemik.
    - **Inflasi & Suku Bunga:** Dampak kebijakan moneter terhadap likuiditas dan biaya modal.
- **Alokasi Aset & Rotasi Ekonomi:**
    - **Siklus Ekonomi:** Fase Ekspansi, Puncak (Peak), Kontraksi, dan Palung (Trough).
    - **Klasifikasi Aset (Defensif vs Siklikal):** Karakteristik saham berbasis sensitivitas terhadap suku bunga dan daya beli (misal: Finance vs Consumer).
    - **Strategi Alokasi:** Pergeseran aset (Saham, Obligasi, Kas) dalam merespon kebijakan makro (Rotasi Sektoral).
- **Modern Portfolio Theory (MPT):** Konsep Efficient Frontier dan optimalitas alokasi aset klasik.

## 2.3 Game Theory (Klasik)
- **Definisi & Model Matematika:** Payoff Matrix, Nash Equilibrium, dan Pareto Optimum.
- **Klasifikasi Permainan:** Coordination, Anti-Coordination, dan Mixed Strategy Game.
- **Model Strategis Sekuensial:**
    - **Prisoner's Dilemma:** Analogi kegagalan pasar/bearish market.
    - **Model Stackelberg:** Dinamika Leader-Follower, asimetri informasi, dan logika *Backward Induction*.

## 2.4 Teori Informasi Kuantum & Game Theory
- **Konsep Encoding Klasik ke Kuantum:** Representasi informasi klasik pada qubit melalui superposisi dan probabilitas kuantum.
- **Kuantisasi EWL (Eisert-Wilkens-Lewenstein):** Operator Entangling ($\hat{J}$) dan strategi Unitary.
- **Matriks Densitas ($\rho$):** Representasi keadaan statistik sistem aset.
- **Von Neumann Entropy:** Pengukuran ketidakpastian dalam sistem kuantum ($S = -\text{Tr}(\rho \ln \rho)$).
- **Quantum Mutual Information (QMI):** Pengukuran korelasi total antar aset melalui sharing information.

## 2.5 Quantum Algorithm (VQE)
- **Dasar Matematika:** Persamaan Eigen ($H|\psi\rangle = E|\psi\rangle$) dan Prinsip Variasi.
- **Variational Quantum Eigensolver:**
    - Algoritma hibrid sebagai pencari Ground State (strategi optimal).
    - **Interpretasi Ground State sebagai Market Regime Optimal:** Identifikasi kondisi equilibrium pasar paling menguntungkan/stabil dari Hamiltonian Ising.
- **Struktur Ansatz (Parameterized Quantum Circuit):**
    - **Rotasi Qubit Tunggal ($U_{rot}$):** Peran gerbang $R_y$ dan $R_z$ dalam pemetaan ruang strategi.
    - **Layer Entanglement ($U_{ent}$):** Penggunaan gerbang CNOT untuk memodelkan interdependensi aset.
- **Teknik Optimasi Klasik:**
    - **SPSA:** Penurunan rumus pendekatan gradien melalui perturbasi simultan.
    - **COBYLA:** Logika optimasi berbasis *linear approximation* tanpa gradien.
- **Formulasi Ising Hamiltonian:**
    - Transformasi QUBO ke model Ising dan pemetaan ke operator Pauli-Z ($\sigma^z$).
    - **Peran Parameter Ising ($h_i, J_{ij}$):** Bagaimana bias dan interaksi mengkodekan kondisi pasar dari Game Theory.

# BAB 3: METODOLOGI PENELITIAN
## 3.1 Alur Penelitian (Flowchart)
## 3.2 Pengumpulan Data & Pra-pemrosesan
- Akuisisi data LQ45 via Yahoo Finance.
- **Diskretisasi Biner (Digitalisasi Data Finansial):** Transformasi *log return* kontinu menjadi state biner sebagai jembatan ke qubit.
- **Laplace Smoothing:** Stabilisasi probabilitas untuk perhitungan entropi.

## 3.3 Konstruksi Model Permainan (Mapping Pipeline)
- **Konstruksi Matriks Payoff:** Perhitungan utilitas Markowitz dengan $\lambda$ endogen.
- **Pemodelan Dinamika Stackelberg:** Identifikasi peran Leader-Follower berbasis kapitalisasi pasar.
- **Ekstraksi Parameter Hamiltonian:**
    - Penentuan **Bias ($h_i$)** dari nilai payoff marginal.
    - Penentuan **Interaksi ($J_{ij}$)** berbasis nilai Quantum Mutual Information (QMI).
- **Klasifikasi Tipe Permainan:** Identifikasi dinamika pasar (Coordination/Anti-Coordination).

## 3.4 Implementasi Kuantum & Optimasi
- **Konstruksi Hamiltonian Total:** 
    - **Cost Hamiltonian ($H_{cost}$):** $H = \sum h_i Z_i + \sum J_{ij} Z_i Z_j$.
    - **Constraint Hamiltonian ($H_{constraint}$):** Penalti kuadratik untuk seleksi tepat $K$ aset.
- **Konfigurasi VQE:** Penentuan depth, inisialisasi parameter, dan setting sampling (shots).
- **Proses Iterasi SPSA:** Pembaruan parameter secara stokastik hingga konvergen.

## 3.5 Evaluasi dan Analisis Kinerja
- **Identifikasi State Optimal:** Ekstraksi bitstring dengan probabilitas tertinggi.
- **Analisis Dinamika Rezim (Backtesting):** 
    - Implementasi *Sliding Window Analysis* untuk melihat perubahan alokasi aset terpilih secara historis.
    - Observasi hubungan antara perubahan hasil VQE dengan peristiwa makroekonomi (regime shift).
- **Validasi Metrik:** Perbandingan Sharpe Ratio dan Trend Ratio antara strategi Kuantum dan Klasik.
