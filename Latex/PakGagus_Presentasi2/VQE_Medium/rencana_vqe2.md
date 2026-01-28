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
