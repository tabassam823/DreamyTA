# Rencana Presentasi: Optimasi Portofolio Eksperimental via HE-VQE
**Topik**: Analisis Numerik dalam Econophysics Kuantum untuk Pemilihan Aset Portofolio

---

## Urutan Slide

### Slide 1: Judul & Pendahuluan
* **Judul**: Integrasi Econophysics, Game Theory, dan Variational Quantum Eigensolver (VQE) untuk Optimasi Portofolio.
* **Sub-judul**: Studi Kasus Pemilihan 2 Aset Terbaik dari Saham LQ45.
* **Poin Utama**: Mengapa pendekatan numerik kuantum? (Menangani kompleksitas korelasi non-linear).

### Slide 2: Metodologi / Pipeline Lengkap
Visualisasi alur kerja dari kode:
1. **Data Acquisition**: Pengambilan data historis.
2. **Markowitz × Game Theory**: Pemodelan matriks payoff.
3. **Parameter Hamiltonian**: Transformasi data pasar ke parameter kuantum ($h_i, J_{ij}$).
4. **Ising Hamiltonian**: Formulasi fungsi biaya dan penalti.
5. **HE-VQE + SPSA**: Optimasi menggunakan sirkuit kuantum.
6. **Hasil & Analisis**: Seleksi aset dan validasi Sharpe Ratio.

### Slide 3: Tahap 1 - Data Acquisition & Pre-Selection
* **Sumber Data**: Yahoo Finance (yfinance).
* **Aset**: BMRI.JK, ADRO.JK, ICBP.JK, KLBF.JK.
* **Proses Numerik**: 
    - Perhitungan *Daily Log Return*: $R_t = \ln(P_t / P_{t-1})$.
    - Diskritisasi biner: $|0\rangle$ (Naik) dan $|1\rangle$ (Turun) untuk identifikasi state pasar.

### Slide 4: Tahap 2 - Markowitz × Game Theory (Risk Aversion Endogen)
* **Inovasi**: Menghitung $\lambda$ (Risk Aversion) secara endogen dari data pasar, bukan asumsi statis.
* **Rumus**: $\lambda_{market} = \frac{\sigma_{avg}}{\mu_{avg} + \sigma_{avg}}$.
* **Utilitas Markowitz**: $U = (1-\lambda)\cdot\mu_p - \lambda\cdot\sigma_p$ yang ditransformasikan menjadi nilai payoff dalam matriks 2x2 untuk setiap pasangan saham.

### Slide 5: Klasifikasi Game Type & Payoff Matrix
* **Analisis Numerik**: Klasifikasi interaksi antar saham (Coordination vs Anti-Coordination Game).
* **Tabel Matriks Payoff (Bi-Matrix)**:
Menampilkan interaksi strategis antara Aset A and Aset B:

| Aset A \ Aset B        |   Naik ($0\rangle$)    | Turun ($1\rangle$)     |
| :--------------------- | :--------------------: | ---------------------- |
| **Naik ($0\rangle$)**  | $(P_{A,00}, P_{B,00})$ | $(P_{A,01}, P_{B,01})$ |
| **Turun ($1\rangle$)** | $(P_{A,10}, P_{B,10})$ | $(P_{A,11}, P_{B,11})$ |

* **Komponen Matriks**: $P_{i,jk}$ adalah utilitas Markowitz yang dihitung dari rata-rata *return* harian pada kondisi state gabungan tertentu.
* **Klasifikasi**: Penentuan tipe permainan berdasarkan perbandingan nilai payoff antar baris/kolom untuk mendeteksi *Nash Equilibrium*.

### Slide 6: Tahap 3 - Ekstraksi Parameter Hamiltonian
* **Bias ($h_i$)**: Dihitung dari selisih payoff marginal (menentukan kecenderungan aset untuk dipilih).
* **Interaksi ($J_{ij}$)**: Menggunakan **Quantum Mutual Information (QMI)**.
    - Menghitung *Von Neumann Entropy* $S(\rho) = -\text{Tr}(\rho \ln \rho)$ dari density matrix pasar.
    - $J_{ij}$ menangkap korelasi informasi antar aset secara lebih mendalam daripada korelasi linier biasa.

### Slide 7: Tahap 4 - Konstruksi Hamiltonian Ising
* **Cost Hamiltonian ($H_{cost}$)**: Representasi profit dan risiko.
* **Constraint Hamiltonian ($H_{constraint}$)**: Penalti untuk memastikan sistem memilih tepat $K=2$ aset.
* **Total**: $H_{total} = H_{cost} + A (\sum x_i - K)^2$.

### Slide 8: Tahap 5 - Implementasi HE-VQE (Hardware-Efficient Ansatz)
* **Arsitektur Sirkuit**: 4 Qubit dengan layer rotasi $R_Y, R_Z$ dan *CNOT chain* untuk entanglement.
* **Optimizer SPSA**: Mengapa SPSA? (Efisien dalam menangani noise dan hanya butuh 2 evaluasi per iterasi).
* **Hyperparameters**: Depth sirkuit, jumlah iterasi (500), dan jumlah sampling (1024 shots).

### Slide 9: Hasil Optimasi & Konvergensi
* **Grafik Konvergensi**: Menunjukkan bagaimana energi VQE mendekati *Exact Ground State*.
* **Perbandingan Energi**: VQE Energy vs Exact Energy (Diagonalisasi Matriks).

### Slide 10: Tahap 6 - Seleksi Aset & Validasi Sharpe Ratio
* **Output Kuantum**: Bitstring dengan probabilitas tertinggi (misal: $|0110
angle$).
* **Aset Terpilih**: Identifikasi nama saham berdasarkan bitstring (contoh: ICBP & KLBF).
* **Validasi**: Perbandingan Sharpe Ratio portofolio terpilih terhadap semua kombinasi pasangan aset lainnya.

### Slide 11: Kesimpulan & Diskusi
* Keberhasilan algoritma dalam mengidentifikasi aset dengan profil risiko/return optimal.
* Akurasi sampling VQE dalam menemukan solusi *combinatorial optimization*.
* Potensi pengembangan (menambah jumlah aset atau menggunakan perangkat keras kuantum riil).
