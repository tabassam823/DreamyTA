# Filosofi dan Penurunan Formulasi Markowitz

Model Markowitz, atau dikenal sebagai **Modern Portfolio Theory (MPT)**, diperkenalkan oleh Harry Markowitz pada tahun 1952. Berikut adalah langkah-langkah penurunan rumusnya dari tingkat filosofis hingga menjadi persamaan optimasi biner.

---

## 1. Fondasi Filosofis dan Aksioma Dasar
Penurunan ini bermula dari beberapa postulat tentang perilaku manusia dan pasar:

### A. Aksioma Rasionalitas (Risk Aversion)
Investasi bukan sekadar mencari keuntungan sebesar-besarnya. Investor diasumsikan rasional:
- Jika ada dua aset dengan **return yang sama**, investor akan memilih yang memiliki **risiko lebih rendah**.
- Jika ada dua aset dengan **risiko yang sama**, investor akan memilih yang memiliki **return lebih tinggi**.

### B. Konvensi Risiko sebagai Volatilitas
Dalam pandangan Markowitz, risiko bukanlah "kemungkinan bangkrut", melainkan **ketidakpastian**. Secara statistik, ketidakpastian diukur sebagai dispersi dari rata-rata, yaitu **Varians ($\sigma^2$)** atau **Deviasi Standar ($\sigma$)**.

### C. Filosofi Diversifikasi
"Don't put all your eggs in one basket." Markowitz membuktikan secara matematis bahwa menggabungkan aset yang tidak berkorelasi sempurna dapat menurunkan risiko total portofolio tanpa harus mengurangi return yang diharapkan.

---

## 2. Postulat Matematis: Mean-Variance Optimization

Diberikan $N$ aset, kita mendefinisikan dua variabel statistik utama:
1. **Expected Return ($\mu$):** Nilai rata-rata keuntungan di masa depan.
2. **Kovarians ($\Sigma$):** Matriks yang merangkum varians tiap aset (diagonal) dan hubungan pergerakan antar aset (off-diagonal).

Tujuan investor adalah meminimalkan risiko total portofolio:
$$ \text{Minimize } \sigma_p^2 = \sum_{i,j} w_i w_j \Sigma_{ij} $$

### Konstruksi Matriks Kovarians ($\Sigma$)
Risiko portofolio bukan sekadar jumlah risiko aset individu, melainkan bagaimana aset-aset tersebut bergerak bersama. Matriks $\Sigma$ (ukuran $N \times N$) dirumuskan sebagai:

$$ \Sigma = \begin{pmatrix} 
\sigma_1^2 & \sigma_{12} & \dots & \sigma_{1N} \\
\sigma_{21} & \sigma_2^2 & \dots & \sigma_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
\sigma_{N1} & \sigma_{N2} & \dots & \sigma_N^2
\end{pmatrix} $$

Dimana:
1. **Elemen Diagonal ($\sigma_i^2$):** Merupakan **Varians** dari aset $i$. Ini mewakili risiko intrinsik atau volatilitas aset tersebut.
2. **Elemen Off-Diagonal ($\sigma_{ij}$):** Merupakan **Kovarians** antara aset $i$ dan $j$. Kovarians tidak bisa didapatkan hanya dari $\sigma$ masing-masing aset, melainkan membutuhkan **Koefisien Korelasi ($\rho_{ij}$)**.

Hubungan matematisnya adalah:
$$ \sigma_{ij} = \rho_{ij} \cdot \sigma_i \cdot \sigma_j $$

Di mana:
- $\sigma_i, \sigma_j$: Deviasi standar (volatilitas) masing-masing aset.
- **Koefisien Korelasi ($\rho_{ij}$):** Didapatkan dengan menormalisasi kovarians terhadap produk deviasi standar kedua aset:
  $$ \rho_{ij} = \frac{\sigma_{ij}}{\sigma_i \cdot \sigma_j} $$
- Rentang nilai $\rho_{ij}$ adalah $[-1, 1]$:
    - **1:** Korelasi positif sempurna (bergerak searah).
    - **0:** Tidak ada hubungan linear.
    - **-1:** Korelasi negatif sempurna (bergerak berlawanan arah).

#### Bagaimana $\Sigma$ didapatkan?
Misalkan kita memiliki matriks return terpusat $\tilde{R}$ berukuran $T \times N$ (dimana setiap elemen sudah dikurangi rata-ratanya, $R_{it} - \bar{R}_i$). Matriks $\Sigma$ didapat dari perkalian dot product antar kolom aset:
$$ \Sigma = \frac{1}{T-1} \tilde{R}^T \tilde{R} $$

Dalam perkalian ini, kolom aset $i$ yang dikalikan dengan dirinya sendiri ($\tilde{R}_i \cdot \tilde{R}_i$) mengisi posisi diagonal sebagai varians, sedangkan perkalian antar kolom berbeda ($\tilde{R}_i \cdot \tilde{R}_j$) mengisi posisi off-diagonal sebagai kovarians.

---

## 3. Transformasi ke Model Keputusan Biner ($x \in \{0,1\}$)

Dalam model Markowitz asli, variabelnya adalah bobot ($w \in [0,1]$). Namun, dalam masalah seleksi aset (seperti pada komputasi kuantum), kita sering menggunakan variabel keputusan biner:
- $x_i = 1$: Aset dipilih untuk masuk portofolio.
- $x_i = 0$: Aset tidak dipilih.

Maka, fungsi objektif dasarnya adalah:
$$ \text{Objektif} = \underbrace{x^T \Sigma x}_{\text{Risiko}} - \underbrace{\lambda \mu^T x}_{\text{Return}} $$
Dimana $\lambda$ adalah **Risk Aversion Coefficient**. Jika $\lambda$ besar, investor sangat mengejar return. Jika $\lambda$ kecil, investor sangat menghindari risiko.

---

## 4. Penanganan Batasan (The Penalty Term)

Dalam dunia nyata, investasi memiliki batasan (*constraints*), misalnya: "Saya hanya ingin memilih tepat $K$ aset dari $N$ pilihan."
Secara matematis:
$$ \sum_{i=1}^N x_i = K $$

Dalam teknik optimasi konvensional, kita menggunakan metode **[[Lagrange_Multiplier]]**. Namun, agar persamaan ini bisa diselesaikan oleh sistem Ising atau QUBO (yang bersifat *unconstrained*), kita harus mengubah "batasan keras" (*hard constraint*) menjadi "penalti lunak" (*soft penalty*).

### Mengapa Kuadratik?
Kita menggunakan bentuk selisih kuadrat:
$$ \text{Penalti} = A \left( \sum x_i - K \right)^2 $$
- Jika $\sum x_i = K$, maka $(K-K)^2 = 0$. Tidak ada penalti (energi minimum).
- Jika $\sum x_i \neq K$, maka nilai tersebut akan dikuadratkan (selalu positif) dan dikalikan dengan konstanta $A$ yang besar. Ini akan meningkatkan total energi secara drastis, sehingga sistem akan dipaksa menjauhi solusi yang melanggar batasan ini.

---

## 5. Formulasi Akhir (The Markowitz Lagrangian)

Dengan menggabungkan semua postulat di atas, kita mendapatkan fungsi energi total (Hamiltonian) yang digunakan dalam optimasi:

$$ \min_{x \in \{0,1\}^N} \mathcal{L}(x) = \underbrace{x^T \Sigma x}_{\text{Postulat Risiko}} - \underbrace{\lambda \mu^T x}_{\text{Aksioma Return}} + \underbrace{A \left(\sum_{i=1}^N x_i - K \right)^2}_{\text{Konvensi Batasan}} $$

Persamaan ini merangkum seluruh filosofi Markowitz:
1. **Suku pertama** menjaga agar aset yang dipilih tidak saling bergejolak (diversifikasi).
2. **Suku kedua** menarik sistem ke arah keuntungan yang lebih tinggi.
3. **Suku ketiga** memastikan solusi yang ditemukan adalah solusi yang valid sesuai batasan jumlah aset.
