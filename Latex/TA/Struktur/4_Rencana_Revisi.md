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
*   **Fokus Pembahasan:** Akuisisi data historis (`harga_harian_saham_N2.csv`) dan metrik finansial.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Perumusan *log return* untuk stasioneritas dan pembuktian linearitas *simple return* bagi ekspektasi portofolio.
	2.  **Analisis Sensitivitas:** Pengaruh panjang jendela historis (*lookback window*) terhadap stabilitas estimasi parameter pasar.
	3.  **Contoh Perhitungan Numerik:** Langkah perhitungan imbal hasil dan matriks kovariansi harian untuk pasangan BBCA-TLKM pada satu jendela waktu sampel (merujuk pada **Lampiran C: Tabel Harga Harian Saham** dan **Tabel Metrik Finansial**).
*   **Interpretasi:** Persiapan data stokastik pasar menjadi variabel interaksi fisika.

### 4.2 Formulasi Exact Potential Game (EPG) dan Pencarian Nash Equilibrium
*   **Fokus Pembahasan:** File `riwayat_nash_sbr_N2.csv`. Pemetaan Markowitz ke domain klasik *Game Theory*.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Syarat Monderer-Shapley dalam pembentukan fungsi potensial $\Phi(\vec{x})$ dari utilitas Markowitz.
	2.  **Analisis Sensitivitas:** Dampak parameter *risk aversion* ($\gamma$) terhadap pergeseran titik *Nash Equilibrium* antar aset.
	3.  **Contoh Perhitungan Numerik:** Penentuan *best response* antar dua agen saham menggunakan tabel *payoff* dari data pasar aktual (merujuk pada **Lampiran C: Riwayat Pencarian Nash Equilibrium (SBR)**).
*   **Interpretasi:** Memformulasikan optimasi sebagai permainan multi-agen dan menyelesaikan solusi klasiknya (PSNE) sebelum masuk ke domain kuantum.

### 4.3 Pemetaan Hamiltonian: Dari EPG ke Model Ising melalui QUBO
*   **Fokus Pembahasan:** File `bias_h_total_N2.csv` dan `interaksi_J_total_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Ekspansi kuadratik penalti kendala anggaran dan substitusi variabel biner ke operator Pauli-Z ($x_i = \frac{1-z_i}{2}$).
	2.  **Analisis Sensitivitas:** Pengaruh koefisien penalti ($A$) terhadap pemisahan tingkat energi antara *ground state* dan *excited states*.
	3.  **Contoh Perhitungan Numerik:** Konversi koefisien QUBO menjadi parameter fisis medan magnet lokal ($h_i$) dan interaksi spin ($J_{ij}$) (merujuk pada **Lampiran C: Parameter Hamiltonian (Bias dan Interaksi)** serta **Parameter Penalti**).
*   **Interpretasi Fisis:** Mengubah matriks ekonomi menjadi lanskap energi fisika kuantum (*ground state problem*).

### 4.4 Inisialisasi Kuantum: Arsitektur Ansatz dan Strategi Warm-Start
*   **Fokus Pembahasan:** Parameter awal VQE dan arsitektur sirkuit.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Representasi matematis status sirkuit $|\psi(\theta)\rangle$ melalui operator rotasi dan gerbang keterikatan.
	2.  **Analisis Sensitivitas:** Perbandingan akurasi inisialisasi antara *random start* vs *warm start* terhadap kecepatan konvergensi.
	3.  **Contoh Perhitungan Numerik:** Penentuan sudut rotasi awal ($\theta = \pi$ atau $0$) berdasarkan bitstring hasil pencarian PSNE (merujuk pada **Lampiran D: Gambar Arsitektur Sirkuit Kuantum**).
*   **Interpretasi:** Menggabungkan kecerdasan klasik (GT) ke dalam anatomi sirkuit kuantum sebagai titik tolak optimasi.

### 4.5 Konvergensi Energi dan Optimasi SPSA di Lanskap Kuantum
*   **Fokus Pembahasan:** File `riwayat_iterasi_vqe_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Estimasi gradien simultan menggunakan perturbasi stokastik SPSA pada parameter sirkuit.
	2.  **Analisis Sensitivitas:** Evaluasi stabilitas konvergensi terhadap variasi *hyperparameters* (faktor penguatan $a$ dan $c$).
	3.  **Contoh Perhitungan Numerik:** Simulasi satu langkah pembaruan parameter sudut $\theta$ berdasarkan dua evaluasi fungsi biaya pada satu iterasi (merujuk pada **Lampiran C: Perbandingan Konvergensi VQE (Depth vs Energi)**).
*   **Interpretasi:** Bukti bahwa optimizer klasik berhasil menavigasi lanskap energi kuantum yang kompleks.

### 4.6 Evolusi Entropi Von Neumann: Eksplorasi Kuantum hingga Keruntuhan State
*   **Fokus Pembahasan:** Grafik riwayat entropi dari `best_ent_hist` dan derivasi dari `contoh_hitung.md`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Kalkulasi entropi Von Neumann melalui *reduced density matrix* ($\rho_A = \text{Tr}_B(\rho_{AB})$) dari status gabungan portofolio.
	2.  **Analisis Sensitivitas:** Korelasi antara kedalaman gerbang keterikatan dengan laju peluruhan entropi menuju state murni.
	3.  **Contoh Perhitungan Numerik:** Perhitungan nilai entropi (dalam bit) pada saat sirkuit berada dalam status superposisi vs status murni portofolio (diadaptasi dari metode pada `contoh_hitung.md`).
*   **Interpretasi:** Memvalidasi secara empiris mekanisme internal sirkuit (dari superposisi menuju determinisme).

### 4.7 Analisis Stabilitas Warm-Start Klasik pada Dinamika Entropi
*   **Fokus Pembahasan:** Perilaku spike (lonjakan) entropi pada awal iterasi VQE.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Persamaan laju perubahan entropi akibat perturbasi parameter pada sirkuit yang telah terinisialisasi klasik.
	2.  **Analisis Sensitivitas:** Dampak intensitas perturbasi awal terhadap risiko terjebak dalam *entanglement trap* (entropi tertahan di 1.0).
	3.  **Contoh Perhitungan Numerik:** Komparasi nilai entropi sistem pada iterasi ke-0 (*pure classical*) dan iterasi ke-10 (*quantum exploration*).
*   **Interpretasi:** Evaluasi kritis terhadap kelemahan memaksakan solusi klasik murni pada awal algoritma variasi kuantum.

### 4.8 Pengaruh Kedalaman Sirkuit (Depth) Terhadap Akurasi Solusi
*   **Fokus Pembahasan:** Pengaruh *Depth* terhadap akurasi.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Analisis derajat kebebasan sirkuit (*degrees of freedom*) sebagai fungsi linier dari *depth*.
	2.  **Analisis Sensitivitas:** Pemetaan *energy gap* terhadap variasi jumlah lapis sirkuit (Depth 1 s/d 6) (merujuk pada **Lampiran D: Grafik Analisis Kedalaman Sirkuit**).
	3.  **Contoh Perhitungan Numerik:** Perbandingan nilai energi minimum dan jumlah parameter sudut pada sirkuit *depth* rendah vs *depth* tinggi.
*   **Interpretasi:** Mencari titik optimal antara akurasi solusi dengan kompleksitas beban komputasi kuantum.

### 4.9 Validasi State Probabilitas Kuantum vs Brute Force Klasik
*   **Fokus Pembahasan:** File `hasil_brute_force_validation_N2.csv`.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Formulasi norma kuadrat amplitudo untuk estimasi probabilitas kemunculan bitstring portofolio.
	2.  **Analisis Sensitivitas:** Ketahanan dominasi amplitudo solusi terhadap *noise* parameter sudut.
	3.  **Contoh Perhitungan Numerik:** Tabel perbandingan probabilitas output VQE terhadap nilai energi objektif murni hasil *brute force* (merujuk pada **Lampiran C: Hasil Validasi Eksak Brute Force**).
*   **Interpretasi:** Membuktikan integritas sirkuit kuantum sebagai "Oracle" pencari solusi optimal global.

### 4.10 Analisis Performa Portofolio Akhir: Perbandingan GT-VQE vs Benchmark
*   **Fokus Pembahasan:** Hasil backtesting dan metrik finansial.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Kalkulasi metrik finansial: *Cumulative Return*, *Sharpe Ratio*, dan *Maximum Drawdown*.
	2.  **Analisis Sensitivitas:** Evaluasi ketangguhan portofolio terhadap variasi kondisi pasar (*bullish*, *bearish*, dan *sideways*).
	3.  **Contoh Perhitungan Numerik:** Simulasi pertumbuhan modal investasi awal berdasarkan runtun waktu bobot aset hasil optimasi hibrida (merujuk pada **Lampiran D: Kurva Performa Kumulatif Strategi GT-VQE vs Benchmark**).
*   **Interpretasi:** Menunjukkan keunggulan strategis model hibrida dalam mitigasi risiko dan maksimisasi imbal hasil.

### 4.11 Dinamika Rebalancing Jendela Waktu Ekstrem (Window Analysis)
*   **Fokus Pembahasan:** Gambar sirkuit & bar chart probabilitas dari analisis jendela waktu.
*   **Sub-subbab Detail:**
	1.  **Penurunan Rumus:** Relasi perubahan gradien Hamiltonian terhadap fluktuasi mendadak parameter kovariansi pasar.
	2.  **Analisis Sensitivitas:** Kecepatan respon sirkuit (delta sudut $\theta$) dalam melakukan *switching* posisi aset secara radikal.
	3.  **Contoh Perhitungan Numerik:** Analisis kuantitatif pergeseran bobot 100% pada transisi jendela kritis Februari-Maret 2021 (merujuk pada **Lampiran B: Visualisasi Perbandingan Alokasi Portofolio per Window**).
*   **Interpretasi:** Mendemonstrasikan kelincahan (*agility*) algoritma dalam merespons anomali pasar secara *real-time*.
