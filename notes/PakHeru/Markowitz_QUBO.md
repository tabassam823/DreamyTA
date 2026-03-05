# Penurunan Model Markowitz ke Ising Hamiltonian

Dokumen ini menjelaskan transformasi matematis dari model optimasi portofolio Markowitz menjadi representasi Quadratic Unconstrained Binary Optimization (QUBO) dan akhirnya menjadi Hamiltonian Ising untuk diselesaikan menggunakan algoritma kuantum seperti VQE atau QAOA.

## 1. Pendahuluan: Risk-Return Trade-off
Dalam teori portofolio, kita mencari keseimbangan antara risiko dan keuntungan. Fungsi energi (objektif) dinyatakan sebagai:
$$ E = \text{Risiko Total} - \text{Bobot Return} + \text{Penalti Batasan} $$

Tujuan utama adalah mencari **ground state** (kondisi energi minimum) yang berarti:
- Meminimalkan risiko ($\min x^T \Sigma x$)
- Memaksimalkan return ($\max \mu^T x \implies \min -\lambda \mu^T x$)
- Memenuhi batasan jumlah aset yang dibeli (Penalty term)

Secara matematis, model [[Markowitz]] untuk variabel biner $x_i \in \{0, 1\}$ adalah:
$$ \min_{x \in \{0,1\}^N} \mathcal{L}(x) = x^T \Sigma x - \lambda \mu^T x + A \left(\sum_{i=1}^N x_i - K \right)^2 $$
Dimana:
- $N$: Jumlah total aset tersedia.
- $x_i$: Keputusan investasi ($1$ jika dibeli, $0$ jika tidak).
- $\mu$: Vektor expected return.
- $\lambda$: Parameter *risk aversion* (toleransi risiko).
- $\Sigma$: Matriks kovarians (risiko antar aset).
- $K$: Jumlah aset yang ingin dipilih.
- $A$: Faktor penalti (Lagrange multiplier) untuk memastikan batasan terpenuhi.

---

## 2. Detail Komponen Matematis

### A. Suku Pertama: Risiko ($x^T \Sigma x$)
$$ x^T \Sigma x = \sum_{i=1}^N \sum_{j=1}^N \Sigma_{ij} x_i x_j = \sum_i \Sigma_{ii} x_i^2 + \sum_{i \ne j} \Sigma_{ij} x_i x_j $$
Karena $x_i \in \{0,1\}$, maka $x_i^2 = x_i$. Persamaan menjadi:
$$ x^T \Sigma x = \sum_i \sigma_i^2 x_i + \sum_{i \ne j} \Sigma_{ij} x_i x_j $$

Dimana $\Sigma_{ii} = \sigma_i^2$ adalah varians aset $i$, dan $\Sigma_{ij}$ adalah kovarians antar aset. Kovarians dapat dihitung melalui perkalian deviasi standar kedua aset ($\sigma_i \sigma_j$) dengan koefisien korelasi ($\rho_{ij}$):
$$ \Sigma_{ij} = \sigma_i \sigma_j \rho_{ij} $$

Secara statistik, komponen-komponen ini dihitung sebagai berikut:
1. **Varians ($\sigma_i^2$):** mengukur volatilitas aset tunggal.
   $$ \sigma_i^2 = \frac{1}{T-1} \sum_{t=1}^T (R_{i,t} - \bar{R}_i)^2 $$
2. **Kovarians ($\Sigma_{ij}$):** mengukur hubungan pergerakan antar dua aset.
   $$ \Sigma_{ij} = \frac{1}{T-1} \sum_{t=1}^T (R_{i,t} - \bar{R}_i)(R_{j,t} - \bar{R}_j) $$
3. **Korelasi ($\rho_{ij}$):** menormalisasi kovarians ke dalam rentang [-1, 1].
   $$ \rho_{ij} = \frac{\Sigma_{ij}}{\sigma_i \sigma_j} $$

Dengan return harian $R_{i,t} = \frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}}$ dan $\bar{R}_i$ adalah rata-rata return.

### B. Suku Kedua: Return ($\lambda \mu^T x$)
Menghitung keuntungan yang diharapkan:
$$ \mu_A = \frac{1}{T} \sum_{t=1}^T R_{A,t} $$
Parameter $\lambda$ dapat ditentukan secara endogen (misal melalui fungsi sigmoid):
$$ \lambda = \frac{1}{1 + e^{-\mu/\sigma}} $$

### C. Suku Ketiga: Penalti Batasan ($A (\sum x_i - K)^2$)
Karena QUBO adalah model optimasi *unconstrained* (tanpa kendala), batasan atau *constraint* harus dimasukkan ke dalam fungsi objektif sebagai penalti. Suku ini memastikan bahwa jumlah aset yang dipilih mendekati atau sama dengan $K$.

$$ P(x) = A \left( \sum_{i=1}^N x_i - K \right)^2 $$

Karakteristik suku penalti:
1. **Fungsi**: Jika $\sum x_i = K$, maka nilai penalti adalah 0 (minimum). Jika terjadi pelanggaran ($\sum x_i \neq K$), nilai energi akan meningkat secara kuadratik, sehingga algoritma akan menghindari solusi tersebut.
2. **Konstanta $A$**: Merupakan bobot penalti ([[Lagrange_Multiplier]]). Nilai $A$ harus dipilih cukup besar agar pelanggaran batasan "dihukum" lebih berat daripada potensi keuntungan dari risiko atau return, namun tidak terlalu besar sehingga merusak lanskap energi optimasi.
3. **Bentuk Ekspansi**:
   $$ A \left( \sum x_i - K \right)^2 = A \left( \sum_i x_i + 2 \sum_{i < j} x_i x_j - 2K \sum_i x_i + K^2 \right) $$
   Ini menunjukkan bahwa batasan memberikan kontribusi baik pada suku linear maupun suku interaksi (kuadratik) dalam QUBO.

## 3. Transformasi Markowitz ke QUBO (Kasus 2 Aset)
Misalkan kita memilih $K=1$ dari 2 aset ($x_1, x_2$). Kita akan mengekspansi fungsi objektif $\mathcal{L}(x) = \text{Risiko} - \text{Return} + \text{Penalti}$:

### Langkah 1: Ekspansi Suku Risiko
$$ x^T \Sigma x = \begin{pmatrix}x_1 & x_2 \end{pmatrix} \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \end{pmatrix} = \sigma_1^2 x_1^2 + 2\sigma_{12}x_1x_2 + \sigma_2^2 x_2^2 $$
Dengan properti biner $x_i^2 = x_i$:
$$ \text{Risiko} = \sigma_1^2 x_1 + \sigma_2^2 x_2 + 2\sigma_{12}x_1x_2 $$

### Langkah 2: Ekspansi Suku Return
$$ \lambda \mu^T x = \lambda \begin{pmatrix}\mu_1 & \mu_2 \end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \end{pmatrix} $$
$$ \text{Return} = \lambda\mu_1x_1 + \lambda\mu_2x_2 $$

### Langkah 3: Ekspansi Suku Penalti ($K=1$)
$$ A(x_1 + x_2 - 1)^2 = A(x_1^2 + x_2^2 + 1 + 2x_1x_2 - 2x_1 - 2x_2) $$
Substitusi $x_i^2 = x_i$:
$$ \text{Penalti} = A(x_1 + x_2 + 1 + 2x_1x_2 - 2x_1 - 2x_2) $$
$$ \text{Penalti} = 2Ax_1x_2 - Ax_1 - Ax_2 + A $$

### Langkah 4: Penggabungan Seluruh Suku
Gabungkan (Langkah 1) - (Langkah 2) + (Langkah 3):
$$ \mathcal{L}(x) = (\sigma_1^2 x_1 + \sigma_2^2 x_2 + 2\sigma_{12}x_1x_2) - (\lambda\mu_1x_1 + \lambda\mu_2x_2) + (2Ax_1x_2 - Ax_1 - Ax_2 + A) $$

Kelompokkan variabel yang sama:
$$ \mathcal{L}(x) = (2\sigma_{12} + 2A)x_1x_2 + (\sigma_1^2 - \lambda\mu_1 - A)x_1 + (\sigma_2^2 - \lambda\mu_2 - A)x_2 + A $$

### Definisikan Koefisien QUBO:
- **Interaksi ($Q_{12}$):** $2\sigma_{12} + 2A$
- **Linear ($C_1$):** $\sigma_1^2 - \lambda\mu_1 - A$
- **Linear ($C_2$):** $\sigma_2^2 - \lambda\mu_2 - A$
- **Konstanta:** $A$

Sehingga bentuk QUBO sederhananya adalah:
$$ \mathcal{L}(x_1, x_2) = Q_{12}x_1x_2 + C_1x_1 + C_2x_2 + A $$

---

### Verifikasi Hasil (Check Table)
Untuk memastikan penurunan benar, kita substitusi nilai $x_1, x_2$:
- Jika $x_1=1, x_2=0$: $\mathcal{L} = C_1 + A = \sigma_1^2 - \lambda\mu_1$ (Hanya aset 1)
- Jika $x_1=0, x_2=1$: $\mathcal{L} = C_2 + A = \sigma_2^2 - \lambda\mu_2$ (Hanya aset 2)
- Jika $x_1=1, x_2=1$: $\mathcal{L} = Q_{12} + C_1 + C_2 + A = \sigma_1^2 + \sigma_2^2 + 2\sigma_{12} - \lambda(\mu_1 + \mu_2) + A$ (Penalti $A$ muncul karena $K=1$)
- Jika $x_1=0, x_2=0$: $\mathcal{L} = A$ (Penalti $A$ muncul karena tidak memilih aset)

---

## 4. Transformasi QUBO ke Ising
Algoritma kuantum seperti VQE menggunakan operator Pauli-Z yang memiliki nilai eigen $\{1, -1\}$. Oleh karena itu, kita harus mengonversi variabel biner $x_i \in \{0, 1\}$ menjadi variabel spin $s_i \in \{1, -1\}$ menggunakan transformasi:
$$ x_i = \frac{1 - s_i}{2} $$
*(Catatan: Jika $x_i=0 \to s_i=1$, dan jika $x_i=1 \to s_i=-1$)*

### Langkah 1: Substitusi Variabel
Masukkan substitusi $x_i$ ke dalam persamaan QUBO 2 aset:
$$ E(s) = Q_{12}\left(\frac{1-s_1}{2}\right)\left(\frac{1-s_2}{2}\right) + C_1\left(\frac{1-s_1}{2}\right) + C_2\left(\frac{1-s_2}{2}\right) + A $$

### Langkah 2: Ekspansi Aljabar
Kita ekspansi setiap suku secara terpisah:
1. **Suku Interaksi:**
   $$ \frac{Q_{12}}{4}(1 - s_1 - s_2 + s_1s_2) = \frac{Q_{12}}{4} - \frac{Q_{12}}{4}s_1 - \frac{Q_{12}}{4}s_2 + \frac{Q_{12}}{4}s_1s_2 $$
2. **Suku Linear Aset 1:**
   $$ \frac{C_1}{2}(1 - s_1) = \frac{C_1}{2} - \frac{C_1}{2}s_1 $$
3. **Suku Linear Aset 2:**
   $$ \frac{C_2}{2}(1 - s_2) = \frac{C_2}{2} - \frac{C_2}{2}s_2 $$

### Langkah 3: Pengelompokan (Ising Hamiltonian)
Gabungkan semua suku dan kelompokkan berdasarkan variabel spinnya:
$$ E(s) = \left( \frac{Q_{12}}{4} \right)s_1s_2 + \left( -\frac{Q_{12}}{4} - \frac{C_1}{2} \right)s_1 + \left( -\frac{Q_{12}}{4} - \frac{C_2}{2} \right)s_2 + \left( \frac{Q_{12}}{4} + \frac{C_1}{2} + \frac{C_2}{2} + A \right) $$

### Langkah 4: Definisi Parameter Ising
Persamaan di atas kini sesuai dengan format standar Ising $H = J_{12}s_1s_2 + h_1s_1 + h_2s_2 + \text{offset}$:
- **Kopling ($J_{12}$):** $\frac{Q_{12}}{4}$
- **Field Lokal ($h_1$):** $-\left(\frac{Q_{12}}{4} + \frac{C_1}{2}\right)$
- **Field Lokal ($h_2$):** $-\left(\frac{Q_{12}}{4} + \frac{C_2}{2}\right)$
- **Konstanta (Energy Offset):** $\frac{Q_{12}}{4} + \frac{C_1}{2} + \frac{C_2}{2} + A$

### Representasi Operator
Dalam komputasi kuantum, variabel $s_i$ diganti dengan operator Pauli-Z ($\hat{Z}_i$):
$$ \hat{H} = J_{12}\hat{Z}_1\hat{Z}_2 + h_1\hat{Z}_1 + h_2\hat{Z}_2 + \text{offset} \cdot \hat{I} $$

---

## 5. Ekspektasi Energi dan Variational Kuantum
Untuk mencari solusi, kita menggunakan ansatz state $|\psi(\theta)\rangle$:
$$ |\psi(\theta_1, \theta_2)\rangle = R_y(\theta_1)|0\rangle \otimes R_y(\theta_2)|0\rangle $$
Dimana $R_y(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

Nilai ekspektasi energi adalah:
$$ \langle E \rangle = \langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle $$
$$ \langle E \rangle = J_{12}\langle \hat{Z}_1\hat{Z}_2 \rangle + h_1\langle \hat{Z}_1 \rangle + h_2\langle \hat{Z}_2 \rangle + \text{const} $$

Karena $\langle \hat{Z} \rangle = \cos(2\theta)$ (untuk rotasi $\theta$ pada $|0\rangle$), maka:
$$ \langle E \rangle = J_{12}\cos(2\theta_1)\cos(2\theta_2) + h_1\cos(2\theta_1) + h_2\cos(2\theta_2) + \text{const} $$

### Gradien Energi:
Untuk optimasi parameter $\theta$ menggunakan *gradient descent*:
$$ \frac{\partial \langle E \rangle}{\partial \theta_1} = -2 J_{12}\sin(2\theta_1)\cos(2\theta_2) - 2h_1\sin(2\theta_1) $$
$$ \frac{\partial \langle E \rangle}{\partial \theta_2} = -2 J_{12}\cos(2\theta_1)\sin(2\theta_2) - 2h_2\sin(2\theta_2) $$