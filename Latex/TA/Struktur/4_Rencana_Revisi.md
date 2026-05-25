# Rencana Revisi Bab 4

Bab 4 yang sudah dibuat pada file latex masih sangat jauh dari ekspektasiku. Oleh karena itu, dibutuhkan revisi dan penyesuaian struktur agar dapat membahas semua hal yang dapat dibahas dengan mengikuti batasan masalah yang ada di bab 1.

## Paragraf Pengantar
Aku ingin:
1. Seperti pada format pomits, paragraf pengantar memberikan:
	1. Latar belakang singkat, 
	2. Penyebutan dasar teori dengan pengelompokan fasenya, 
	3. Metodologi singkat, 
	4. Penyebutan jenis data dan data yang didapatkan,
	5. Lalu baru masuk ke penyebutan 11 subbab Pembahasan yang ada di bawahnya.
2. Masing-masing kelimanya memiliki paragraf sendiri-sendiri minimal 1.
3. Semua data mulai dari akuisisi sampai interpretasi grafik terakhir ditunjukkan/disebutkan di paragraf pengantar ini agar poin Pembahasan di bawah hanya perlu menyebutkan dan membahas data-data yang perlu dibahas saja.

## Rincian 11 Subbab Pembahasan

### 4.1 Akuisisi dan Prapemrosesan Data Runtun Waktu Saham
*   **Fokus Pembahasan:** Akuisisi data historis (`harga_harian_saham_N2.csv`).
*   **Isi:** 
	1. Alasan memilih periode 2021-2023 dengan *timeframe* harian.
	2. Penurunan matematis dari harga Penutupan menjadi *logarithmic return* dan pembentukan *covariance matrix*.
	3. Bukti perlunya *simple return* untuk linearitas ekspektasi portofolio.
	4. Analisis diversifikasi independen BBCA & TLKM.
	5. *Risk Aversion* endogen sebagai parameter pasar dinamis.
*   **Interpretasi:** Persiapan data stokastik pasar menjadi variabel interaksi fisika.

### 4.2 Formulasi Exact Potential Game (EPG) dan Pencarian Nash Equilibrium
*   **Fokus Pembahasan:** File `riwayat_nash_sbr_N2.csv`. Pemetaan Markowitz ke domain klasik *Game Theory*.
*   **Isi:** 
	1. Konstruksi fungsi utilitas individu dan penurunan fungsi potensial $\Phi(\vec{x})$ (Monderer & Shapley).
	2. Pembuktian $\Delta u_i \equiv \Delta \Phi$ untuk menjamin keberadaan *Pure Strategy Nash Equilibrium* (PSNE).
	3. Analisis iterasi *Stochastic Best Response* (SBR) dalam mencapai kesetimbangan (*Nash Equilibrium*).
*   **Interpretasi:** Memformulasikan optimasi sebagai permainan multi-agen dan menyelesaikan solusi klasiknya (PSNE) sebelum masuk ke domain kuantum.

### 4.3 Pemetaan Hamiltonian: Dari EPG ke Model Ising melalui QUBO
*   **Fokus Pembahasan:** File `bias_h_total_N2.csv` dan `interaksi_J_total_N2.csv`.
*   **Isi:** 
	1. Transformasi fungsi potensial $\Phi(\vec{x})$ menjadi QUBO dengan menyertakan *penalty term* untuk kendala anggaran.
	2. Substitusi variabel biner ke spin Pauli-Z ($x_i = \frac{1-z_i}{2}$).
	3. Ekstraksi dan interpretasi fisis koefisien $h_i$ (bias medan) dan $J_{ij}$ (interaksi spin/entanglement risiko).
*   **Interpretasi Fisis:** Mengubah matriks ekonomi menjadi lanskap energi fisika kuantum (*ground state problem*).

### 4.4 Inisialisasi Kuantum: Arsitektur Ansatz dan Strategi Warm-Start
*   **Fokus Pembahasan:** Gambar `rangkaian_kuantum_depth..._N2.png` dan parameter awal VQE.
*   **Isi:** 
	1. Injeksi solusi PSNE (dari Subbab 4.2) ke dalam sirkuit sebagai status awal pasti (*Warm-Start*) menggunakan rotasi absolut ($0$ atau $\pi$).
	2. Peran gerbang rotasi ($R_y, R_z$) dalam mengeksplorasi ruang probabilitas dari titik awal tersebut.
	3. Peran gerbang *entanglement* (CZ/CNOT) dalam menciptakan korelasi fitur risiko antar aset.
*   **Interpretasi:** Menggabungkan kecerdasan klasik (GT) ke dalam anatomi sirkuit kuantum (*Hardware-Efficient Ansatz*) sebagai titik tolak optimasi.

### 4.5 Konvergensi Energi dan Optimasi SPSA di Lanskap Kuantum
*   **Fokus Pembahasan:** File `riwayat_iterasi_vqe_N2.csv`.
*   **Isi:** 
	1. Mekanisme estimasi gradien SPSA yang efisien untuk sistem kuantum ber-noise.
	2. Pemilihan *learning rate* via LR Finder untuk menjaga stabilitas.
	3. Visualisasi penurunan ekspektasi energi $\langle H \rangle$ menuju titik minimum (*ground state*).
*   **Interpretasi:** Bukti bahwa optimizer klasik berhasil menavigasi lanskap energi kuantum yang kompleks.

### 4.6 Evolusi Entropi Von Neumann: Eksplorasi Kuantum hingga Keruntuhan State
*   **Fokus Pembahasan:** Grafik riwayat entropi dari `best_ent_hist`.
*   **Isi:** 
	1. Makna fisis entropi tinggi di awal iterasi sebagai bukti "fase eksplorasi paralel" (keunggulan kuantum).
	2. Konvergensi Sempurna (Entropi $\to 0$): Keruntuhan state (*collapse*) ke basis klasik portofolio secara absolut.
	3. Konvergensi Parsial (Entropi $\approx 0.5$): Terjadi akibat degenerasi lanskap energi (dua aset memiliki profil risiko-return identik) atau keterbatasan parameter ansätze.
*   **Interpretasi:** Memvalidasi secara empiris mekanisme internal sirkuit (dari superposisi menuju determinisme).

### 4.7 Analisis Stabilitas Warm-Start Klasik pada Dinamika Entropi
*   **Fokus Pembahasan:** Perilaku spike (lonjakan) entropi pada awal iterasi VQE.
*   **Isi:** 
	1. Jejak sidik jari *Warm-Start*: Entropi dimulai dari 0 karena diinisialisasi murni di state klasik (PSNE).
	2. "Pemberontakan Entropi": Lonjakan tajam entropi menuju $1.0$ akibat paksaan optimizer SPSA untuk menyulam *entanglement* keluar dari *state* klasik.
	3. Diagnosa *Barren Plateaus*: Jika entropi gagal turun dari $1.0$, menandakan *Hard Warm-Start* justru menjebak VQE di lanskap tanpa gradien.
*   **Interpretasi:** Evaluasi kritis terhadap kelemahan memaksakan solusi klasik murni pada awal algoritma variasi kuantum.

### 4.8 Pengaruh Kedalaman Sirkuit (Depth) Terhadap Akurasi Solusi
*   **Fokus Pembahasan:** Grafik `grafik_depth_per_window_N2.png`.
*   **Isi:** 
	1. Perbandingan capaian energi minimal lintas *depth* (1-6).
	2. Titik jenuh ekspresibilitas (*saturation point*) vs beban komputasi.
	3. Analisis *over-parameterization* yang memicu kegagalan entropi (nyambung dari 4.7).

### 4.9 Validasi State Probabilitas Kuantum vs Brute Force Klasik
*   **Fokus Pembahasan:** File `hasil_brute_force_validation_N2.csv`.
*   **Isi:** 
	1. Pembuktian bahwa amplitudo tertinggi VQE identik dengan solusi eksak klasik (*Oracle*).
	2. Analisis dominasi probabilitas solusi optimal terhadap kombinasi suboptimal.

### 4.10 Analisis Performa Portofolio Akhir: Perbandingan GT-VQE vs Benchmark
*   **Fokus Pembahasan:** Gambar `hasil_backtest_vqe_N2.png` dan `metrik_return_dan_lambda_N2.csv`.
*   **Isi:** 
	1. Analisis komparatif *Cumulative Return*, *Sharpe Ratio*, dan *Maximum Drawdown*.
	2. Dampak injeksi kecerdasan Game Theory dalam menghaluskan kurva ekuitas saat *market crash*.

### 4.11 Dinamika Rebalancing Jendela Waktu Ekstrem (Window Analysis)
*   **Fokus Pembahasan:** Gambar sirkuit & bar chart probabilitas dari `Analisis_Window_N2/`.
*   **Isi:** 
	1. Studi kasus pada jendela volatilitas tinggi: Bagaimana perubahan input empiris merubah Hamiltonian dan memicu rotasi radikal pada sirkuit kuantum.
	2. Agilitas portofolio hibrida dalam mengeksekusi strategi peralihan (*switching*).
