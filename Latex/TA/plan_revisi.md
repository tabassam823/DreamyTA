# Rencana Revisi Tugas Akhir: Integrasi Exact Potential Game dan NMI

Rencana ini membagi proses revisi menjadi tiga bagian utama sesuai dengan permintaan, dengan fokus pada penguatan landasan teoretis dan rigoritas matematis berdasarkan dokumen `Kombinasi_GT_Ising.pdf`.

## Bagian 1: Penurunan Rumus Markowitz & Formalisme Potential Game
**Target File:** `Contents/Daster/Bab-2.3.tex`

### Tujuan Revisi:
Mengubah paradigma dari optimasi Markowitz standar menjadi kerangka kerja *Exact Potential Game* untuk membuktikan bahwa maksimisasi utilitas individu selaras dengan optimasi portofolio global.

### Langkah-langkah:
1.  **Redefinisi Lagrangian:** Mengubah persamaan objektif Markowitz agar menggunakan notasi yang konsisten dengan teori permainan.
2.  **Penyelarasan Parameter:** Memasukkan hubungan analitis antara parameter risiko $\lambda$ dan konstanta penghindaran risiko $\gamma$ ($\lambda = 2/\gamma$).
3.  **Definisi Fungsi Potensial:** Memperkenalkan fungsi potensial global $\Phi(x)$ sebagai negatif dari dskalakan Lagrangian.
4.  **Bukti Matematis:** Menambahkan derivasi dekomposisi utilitas untuk membuktikan sifat *Exact Potential Game*, menunjukkan bahwa $\Delta \Phi_i = u_i(1, x_{-i}) - u_i(0, x_{-i})$.

---

## Bagian 2: Redefinisi Imbal Hasil Strategis & Pencarian Bias $h_i$
**Target File:** `Contents/Daster/Bab-2.4.tex`

### Tujuan Revisi:
Mengganti perhitungan *expected payoff* klasik dengan *Strategic Expected Return* ($\tilde{\mu}_i$) yang berbasis pada *microstates* pasar dan probabilitas gabungan yang lebih mendalam.

### Langkah-langkah:
1.  **Digitalisasi Microstate:** Menjelaskan pemetaan status biner $s \in \{u, d\}$ untuk $N=4$ aset (16 *microstates*).
2.  **Kalkulasi $\tilde{\mu}_i$:** Memasukkan rumus jumlahan terbobot dari ekspektasi imbal hasil bersyarat (conditional expected return) terhadap distribusi probabilitas gabungan.
3.  **Unifikasi ke Hamiltonian:** Menurunkan $h_i$ langsung dari elemen diagonal matriks QUBO ($Q_{ii}$) yang sudah mengandung unsur $\tilde{\mu}_i$ dan penalti kardinalitas.

---

## Bagian 3: Integrasi NMI & Pencarian Kopling $J_{ij}$
**Target File:** `Contents/Daster/Bab-2.5.tex`

### Tujuan Revisi:
Mengganti aproksimasi $J_{ij}$ sederhana dengan metode *Amplification* menggunakan *Normalized Mutual Information* (NMI) dan menyertakan bukti reduksi orde informasi.

### Langkah-langkah:
1.  **Teori Informasi Orde Tinggi:** Memperkenalkan *Interaction Information* untuk $N=4$ aset.
2.  **Bukti Reduksi Orde:** Menambahkan pembuktian matematis mengapa suku interaksi orde-3 dan orde-4 lenyap (runtuh) akibat kendala kardinalitas $K=2$ (menggunakan *Pigeonhole Principle*).
3.  **Skalarisasi NMI:** Menjelaskan prosedur skalarisasi untuk mendapatkan NMI nirdimensi dalam rentang $[0, 1]$.
4.  **Redefinisi Kopling:** Mengubah formulasi kopling menjadi penguatan matriks kovariansi: $\tilde{\sigma}_{ij} = \sigma_{ij}[1 + NMI(i, j)]$.
5.  **Ekstraksi $J_{ij}$ Final:** Menurunkan formula $J_{ij}$ dari elemen matriks QUBO $Q_{ij}$ yang telah dimodifikasi oleh $\tilde{\sigma}_{ij}$.

---

## Jadwal Eksekusi (Tahap Berikutnya)
- **Turn 1:** Eksekusi Bagian 1 pada `Bab-2.3.tex`.
- **Turn 2:** Eksekusi Bagian 2 pada `Bab-2.4.tex`.
- **Turn 3:** Eksekusi Bagian 3 pada `Bab-2.5.tex`.
