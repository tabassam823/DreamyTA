# Rencana Revisi Bab 4

Bab 4 yang sudah dibuat pada file latex masih sangat jauh dari ekspektasiku. Oleh karena itu, dibutuhkan revisi dan penyesuaian struktur agar dapat membahas semua hal yang dapat dibahas dengan mengikuti batasan masalah yang ada di bab 1.

## Paragraf Pengantar
Aku ingin:
1. Seperti pada format pomits, paragraf pengantar memberikan:
	1. Latar belakang singkat, 
	2. Penyebutan dasar teori dengan pengelompokan fasenya, 
	3. Metodologi singkat, 
	4. Penyebutan jenis data dan data yang didapatkan,
	5. Lalu baru masuk ke penyebutan 12 subbab Pembahasan yang ada di bawahnya.
2. Masing-masing kelimanya memiliki paragraf sendiri-sendiri minimal 1.
3. Semua data mulai dari akuisisi sampai interpretasi grafik terakhir ditunjukkan/disebutkan di paragraf pengantar ini agar poin Pembahasan di bawah hanya perlu menyebutkan dan membahas data-data yang perlu dibahas saja.

## Rincian 12 Subbab Pembahasan

### 4.1 Akuisisi dan Prapemrosesan Data Runtun Waktu Saham
*   **Fokus Pembahasan:** Akuisisi data historis (`harga_harian_saham_N2.csv`) dan metrik finansial.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Perumusan *log return* untuk stasioneritas dan pembuktian linearitas *simple return* bagi ekspektasi portofolio.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Langkah perhitungan imbal hasil dan matriks kovariansi harian untuk pasangan BBCA-TLKM. Penjelasan simetri *log return* (1, 0, -1) vs asimetri *simple return* ($\infty$, -1) serta dampaknya pada Hamiltonian (merujuk pada **Lampiran C**).

### 4.2 Formulasi Exact Potential Game (EPG) dan Pencarian Nash Equilibrium
*   **Fokus Pembahasan:** File `riwayat_nash_sbr_N2.csv`. Pemetaan Markowitz ke domain klasik *Game Theory*.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Syarat Monderer-Shapley dalam pembentukan fungsi potensial $\Phi(\vec{x})$ dari utilitas Markowitz.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Penentuan *best response* antar dua agen saham menggunakan tabel *payoff*. Analisis sensitivitas dampak parameter *risk aversion* ($\gamma$) terhadap pergeseran titik *Nash Equilibrium* (merujuk pada **Lampiran C**).

### 4.3 Pemetaan Hamiltonian: Dari EPG ke Model Ising melalui QUBO
*   **Fokus Pembahasan:** File `bias_h_total_N2.csv` dan `interaksi_J_total_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Ekspansi kuadratik penalti kendala anggaran dan substitusi variabel biner ke operator Pauli-Z ($x_i = \frac{1-z_i}{2}$).
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Konversi koefisien QUBO menjadi parameter fisis $h_i$ dan $J_{ij}$. Analisis sensitivitas pengaruh koefisien penalti ($A$) terhadap pemisahan tingkat energi portofolio valid vs invalid (merujuk pada **Lampiran C**).

### 4.4 Inisialisasi Kuantum: Arsitektur Ansatz dan Strategi Warm-Start
*   **Fokus Pembahasan:** Parameter awal VQE dan arsitektur sirkuit.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Representasi matematis status sirkuit $|\psi(\theta)\rangle$ melalui operator rotasi dan gerbang keterikatan.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Penentuan sudut rotasi awal berdasarkan bitstring PSNE. Analisis stabilitas inisialisasi *warm start* dalam menghindari *barren plateaus* dibandingkan inisialisasi acak (merujuk pada **Lampiran D**).

### 4.5 Algoritma Pencarian \textit{Learning Rate} Otomatis (LR Finder)
*   **Fokus Pembahasan:** File `hasil_pencarian_lr_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Formulasi pembaruan batas atas dan bawah parameter SPSA selama proses pencarian awal menggunakan EMA.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Demonstrasi pemilihan $\eta$ optimal melalui kemiringan kurva energi tercuram. Analisis sensitivitas interval pencarian terhadap risiko *premature convergence* (merujuk pada **Lampiran C**).

### 4.6 Konvergensi Energi dan Optimasi SPSA di Lanskap Kuantum
*   **Fokus Pembahasan:** File `riwayat_iterasi_vqe_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Estimasi gradien simultan SPSA pada parameter sirkuit dengan \textit{learning rate} yang telah terkalibrasi.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Simulasi langkah pembaruan parameter sudut $\theta$. Analisis stabilitas konvergensi energi terhadap fluktuasi pengukuran kuantum (\textit{noise}) (merujuk pada **Lampiran C**).

### 4.7 Evolusi Entropi Von Neumann: Eksplorasi Kuantum hingga Keruntuhan State
*   **Fokus Pembahasan:** Grafik riwayat entropi dari `best_ent_hist` dan derivasi dari `contoh_hitung.md`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Kalkulasi entropi Von Neumann melalui *reduced density matrix* ($\rho_A = \text{Tr}_B(\rho_{AB})$).
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Perhitungan nilai entropi pada status superposisi vs murni. Analisis korelasi antara kedalaman gerbang keterikatan dengan laju peluruhan entropi (merujuk pada `contoh_hitung.md`).

### 4.8 Analisis Stabilitas Warm-Start Klasik pada Dinamika Entropi
*   **Fokus Pembahasan:** Perilaku spike (lonjakan) entropi pada awal iterasi VQE.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Persamaan laju perubahan entropi akibat perturbasi parameter pada sirkuit terinisialisasi klasik.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Komparasi entropi pada iterasi ke-0 vs iterasi ke-10. Analisis fenomena "Pemberontakan Entropi" dan dampaknya terhadap navigasi gradien sirkuit.

### 4.9 Pengaruh Kedalaman Sirkuit (Depth) Terhadap Akurasi Solusi
*   **Fokus Pembahasan:** Grafik `grafik_depth_per_window_N2.png`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Analisis derajat kebebasan sirkuit sebagai fungsi linier dari *depth*.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Pemetaan *energy gap* terhadap variasi Depth 1-6. Analisis titik jenuh ekspresibilitas sirkuit vs risiko *over-parameterization* (merujuk pada **Lampiran D**).

### 4.10 Validasi State Probabilitas Kuantum vs Brute Force Klasik
*   **Fokus Pembahasan:** File `hasil_brute_force_validation_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Formulasi norma kuadrat amplitudo untuk estimasi probabilitas bitstring portofolio.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Tabel komparasi output VQE terhadap *ground truth* energi klasik. Analisis ketahanan dominasi amplitudo solusi terhadap gangguan parameter sudut (merujuk pada **Lampiran C**).

### 4.11 Analisis Performa Portofolio Akhir: Perbandingan GT-VQE vs Benchmark
*   **Fokus Pembahasan:** Hasil backtesting dan metrik finansial.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Kalkulasi metrik finansial: *Cumulative Return*, *Sharpe Ratio*, dan *Maximum Drawdown*.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Pertumbuhan modal berdasarkan bobot optimasi hibrida. Analisis ketangguhan performa GT-VQE dalam mitigasi risiko pada berbagai kondisi pasar (merujuk pada **Lampiran D**).

### 4.12 Dinamika Rebalancing Jendela Waktu Ekstrem (Window Analysis)
*   **Fokus Pembahasan:** Gambar sirkuit & bar chart probabilitas dari analisis jendela waktu.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Relasi perubahan gradien Hamiltonian terhadap fluktuasi parameter kovariansi pasar.
	2.  **Contoh Perhitungan Numerik & Analisis Fisis:** Analisis pergeseran bobot radikal pada jendela kritis Februari-Maret 2021. Analisis kecepatan respon sirkuit (\textit{agility}) terhadap anomali pasar (merujuk pada **Lampiran B**).
