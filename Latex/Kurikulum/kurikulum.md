# Kurikulum Pembelajaran: Algoritma Quantum Exact Potential Game (Ising-SBR)

**Target Audiens:** Mahasiswa Fisika Murni (Mid-Year)  
**Tujuan Utama:** Memahami konvergensi Teori Portofolio Modern, Teori Permainan, Mekanika Statistik (Model Ising), dan Komputasi Kuantum (VQE).

---

## [[Modul_1]]: Teori Portofolio Modern & Ekonofisika
*Tujuan: Memahami masalah optimasi dari kacamata keuangan dan landasan matematisnya.*

1.  **Modern Portfolio Theory (MPT) - Markowitz:**
    *   Konsep *Risk-Return Tradeoff*: Memaksimalkan imbal hasil sambil meminimalkan variansi (risiko).
    *   Fungsi Objektif Markowitz: $O(x) = \gamma \text{ (Risiko)} - \text{Imbal Hasil}$.
2.  **Metrik Finansial:**
    *   *Log-Returns*: Mengapa fisika kuantum/statistik lebih menyukai log-return (sifat aditif dan kemiripan dengan energi).
    *   *Sharpe Ratio*: Metrik untuk mengukur efisiensi portofolio berdasarkan risiko yang diambil.
3.  **Parameter Psikologi Pasar:**
    *   *Risk Aversion* ($\gamma$): Derajat ketakutan investor terhadap risiko.
    *   Estimasi $\gamma$ secara endogen menggunakan fungsi sigmoid/logistik dalam kode.

## [[Modul_2]]: Teori Informasi & Metrik Non-Linier (NMI)
*Tujuan: Memahami penggunaan Normalized Mutual Information (NMI) untuk menangkap dependensi pasar.*

1.  **Shannon Entropy & Mutual Information:**
    *   Menghitung entropi dari distribusi probabilitas biner pergerakan harga aset (naik/turun).
2.  **Normalized Mutual Information (NMI):**
    *   Konsep korelasi non-linier menggunakan *Upper Bound Theorem*.
    *   Kelebihan NMI dibandingkan koefisien korelasi Pearson klasik dalam sistem keuangan yang kompleks.
3.  **Modifikasi Matriks Kovariansi:**
    *   Menyesuaikan bobot risiko ($\sigma_{ij}$) dengan informasi mutual untuk menangkap *tail risk* atau dependensi yang tersembunyi.

## [[Modul_3]]: Game Theory & Nash Equilibrium (SBR)
*Tujuan: Memahami pendekatan strategis dalam pemilihan aset sebagai "Exact Potential Game".*

1.  **Konsep Potential Game:**
    *   Definisi fungsi potensial yang selaras dengan insentif setiap pemain (aset).
    *   Portofolio sebagai sistem multi-agen yang berinteraksi secara strategis.
2.  **Sequential Best Response (SBR):**
    *   Algoritma pencarian Nash Equilibrium secara iteratif.
    *   Analisis fungsi `find_nash_sbr`: Bagaimana aset "memutuskan" untuk masuk atau keluar dari portofolio berdasarkan energi sistem.

## [[Modul_4]]: Pemetaan Hamiltonian Ising (Fondasi Fisika Statistik)
*Tujuan: Memahami bagaimana masalah pemilihan aset diubah menjadi pencarian energi dasar (ground state).*

1.  **Review Model Ising:**
    *   Definisi Spin ($s_i \in \{-1, 1\}$) dan variabel biner ($x_i \in \{0, 1\}$).
    *   Hamiltonian Ising: $H = \sum h_i \sigma_i^z + \sum J_{ij} \sigma_i^z \sigma_j^z$.
2.  **Formulasi Markowitz ke Ising:**
    *   Ekuivalensi antara minimalisasi fungsi objektif keuangan dengan minimalisasi energi sistem spin.
    *   Transformasi variabel: $z_i = 1 - 2x_i$.
3.  **Constraint Handling:**
    *   Penggunaan *Lagrange Multiplier* ($\lambda$) sebagai penalti untuk batasan jumlah aset (*cardinality constraint* $K$).

## [[Modul_5]]: Variational Quantum Eigensolver (VQE)
*Tujuan: Memahami algoritma hibrida klasik-kuantum untuk mencari solusi optimal.*

1.  **Ansatz & Sirkuit Variasional:**
    *   Struktur sirkuit RY-RZ dengan CNOT *entanglement*.
    *   Konsep *Adaptive Depth*: Menambah kompleksitas sirkuit hanya jika diperlukan (efisiensi sumber daya kuantum).
2.  **Optimasi SPSA:**
    *   Metode stokastik untuk memperbarui parameter sirkuit dalam lingkungan yang ber-noise.
3.  **NE Warm-Start:**
    *   Strategi inisialisasi parameter kuantum menggunakan hasil Nash Equilibrium klasik untuk mempercepat konvergensi di sirkuit kuantum.
4. **Contoh**:
	* contoh perhitungan yang diletakkan ke dalam file [[Contoh_Modul_5]]

## [[Modul_6]]: Implementasi & Backtesting (Sintesis)
*Tujuan: Menjalankan dan mengevaluasi algoritma secara keseluruhan.*

1.  **Pipeline Eksekusi:**
    *   `run_strategy_step`: Integrasi dari NMI $\rightarrow$ Ising Mapping $\rightarrow$ SBR $\rightarrow$ VQE.
2.  **Rebalancing Strategy:**
    *   Logika *Monthly Rebalance* dan *Rolling Window* untuk simulasi perdagangan dunia nyata.
3.  **Interpretasi Hasil:**
    *   Menganalisis performa algoritma (Equity Curve) terhadap benchmark IHSG (^JKSE) dan strategi beli-simpan (*Buy & Hold*).

---

## Proyek Akhir: Eksperimen Mandiri
1.  Modifikasi jumlah aset ($N$) dan target portofolio ($K$).
2.  Amati perubahan konvergensi energi pada grafik `best_spsa_history`.
3.  Evaluasi: Apakah strategi berbasis kuantum ini berhasil mengalahkan indeks pasar (IHSG) dalam periode tertentu?
