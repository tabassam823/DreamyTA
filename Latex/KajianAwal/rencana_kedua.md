# Rencana Pengeditan Bab 2 (Tahap 2)

**Tujuan:** Menyempurnakan struktur Bab 2 berdasarkan saran revisi `Saran_Pengeditan_Bab_2_kedua.md` untuk menghilangkan redundansi dan memperkuat alur narasi, khususnya pada bagian Ekonofisika.

## Analisis Masalah Saat Ini
1.  **Redundansi:** Sub-bab 2.4.2 mengulang materi yang sudah dibahas lebih mendalam di 2.1.2 dan 2.1.4.
2.  **Fragmentasi Topik:** Pembahasan Black-Scholes (2.4.1) terpisah dari landasan teorinya di 2.2.2 (GBM). Arbitrase Statistik (2.4.3) terisolasi di akhir bab.

## Rencana Aksi

### 1. Restrukturisasi Bab 2.2 (Fisika Statistik & Dinamika Pasar)
*   **Modifikasi Sub-bab 2.2.2:** Menggabungkan isi **2.4.1 (Model Black-Scholes dan Derivatif Finansial)** ke dalam **2.2.2 (Proses Stokastik dan Gerak Brown Geometris)**.
    *   *Alur Baru:* Jelaskan GBM sebagai dasar -> Masukkan Model Black-Scholes sebagai solusi standar (dari 2.4.1) -> Jelaskan Limitasi Klasik -> Masuk ke Solusi Fraktal.
*   **Tambah Sub-bab 2.2.4:** Memindahkan isi **2.4.3 (Arbitrase Statistik dan Kointegrasi)** menjadi sub-bab baru **2.2.4** dengan judul **"Dinamika Mean-Reverting dan Arbitrase Statistik"**.

### 2. Penghapusan Bab 2.4 (Ekonofisika dan Teori Permainan)
*   Hapus **2.4.2 (Teori Permainan Klasik vs Kuantum)** sepenuhnya karena isinya redundan dengan 2.1.2 dan 2.1.4.
*   Hapus judul **2.4** beserta seluruh sisa isinya karena sub-bab lain sudah dipindahkan ke 2.2.

### 3. Perapihan Bab 2.3 (Metode Solusi Komputasi)
*   Memperbaiki penomoran sub-bab **2.3.4 Algoritma Optimasi Kuantum (QAOA)** menjadi **2.3.3**, karena urutannya melompat.

## Struktur Final yang Diharapkan

**2.1 Formalisme Mekanika Kuantum untuk Pemodelan Informasi**
*   2.1.1 Ruang Hilbert, Superposisi, dan Sistem Qubit vs Qutrit
*   2.1.2 Formalisme Teori Permainan Klasik
*   2.1.3 Formalisme Matriks Densitas
*   2.1.4 Protokol Kuantisasi Permainan (EWL & MW)
*   2.1.5 Teori Permainan Bayesian dan Quantum Discord

**2.2 Fisika Statistik dalam Pemodelan Pasar dan Optimasi**
*   2.2.1 Model Ising dan Distribusi Boltzmann dalam Konteks Optimasi
*   2.2.2 Proses Stokastik: Dari Black-Scholes hingga Fraktal (Gabungan)
*   2.2.3 Fraktal dan Analisis Runtun Waktu (Time Series)
*   2.2.4 Dinamika Mean-Reverting dan Arbitrase Statistik

**2.3 Metode Solusi Komputasi untuk Ekuilibrium Ekonomi**
*   2.3.1 Metode Monte Carlo dan Rantai Markov (MCMC)
*   2.3.2 Persamaan Diferensial Stokastik Mundur (BSDE) dan Deep Learning
*   2.3.3 Algoritma Optimasi Kuantum (QAOA)
