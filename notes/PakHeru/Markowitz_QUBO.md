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
[[risk_aversion_endogen]]
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
- Jika $x_1=0, x_2=0$: $\mathcal{L} = A$ (Penalti $A$ muncul karena tidak memilih aset sama sekali)

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

## 5. Ekspektasi Energi (Kasus 2 Aset)
Untuk mencari solusi, kita menggunakan ansatz sederhana $|\psi(\theta)\rangle$:
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

---

## 6. Fondasi Teoritis: Prinsip Variasi
Penurunan pada Bab 5 adalah contoh spesifik untuk 2 aset. Secara umum, algoritma VQE (Variational Quantum Eigensolver) didasarkan pada salah satu postulat fundamental dalam mekanika kuantum, yaitu **Prinsip Variasi** (atau [[Teorema_Reyleigh_Ritz]]).

### A. Postulat Ground State
Setiap sistem kuantum didefinisikan oleh operator Hamiltonian $\hat{H}$. Energi dari state mana pun $|\psi\rangle$ dinyatakan sebagai nilai ekspektasi:
$$ E(\psi) = \frac{\langle \psi | \hat{H} | \psi \rangle}{\langle \psi | \psi \rangle} $$

Prinsip variasi menyatakan bahwa untuk sembarang *trial state* (state percobaan) $|\psi\rangle$, nilai ekspektasi energinya tidak akan pernah lebih rendah dari energi ground state ($E_0$):
$$ E(\psi) \ge E_0 $$

### B. Generalisasi Hamiltonian untuk $N$ Aset
Berdasarkan transformasi Ising pada Bab 4, Hamiltonian untuk $N$ aset dapat dituliskan secara umum sebagai:
$$ \hat{H} = \sum_{i=1}^N \sum_{j>i}^N J_{ij} \hat{Z}_i \hat{Z}_j + \sum_{i=1}^N h_i \hat{Z}_i + \text{offset} \cdot \hat{I} $$

Untuk sebuah *trial state* $|\psi(\theta)\rangle$, nilai ekspektasi energi total adalah:
$$ \langle E(\theta) \rangle = \sum_{i<j} J_{ij} \langle \hat{Z}_i \hat{Z}_j \rangle_{\theta} + \sum_i h_i \langle \hat{Z}_i \rangle_{\theta} + \text{offset} $$

Jika kita menggunakan ansatz rotasi independen seperti pada Bab 5, di mana $|\psi(\theta)\rangle = \bigotimes_{i=1}^N R_y(\theta_i)|0\rangle$, maka:
1.  **Suku Linear:** $\langle \hat{Z}_i \rangle = \cos(2\theta_i)$
2.  **Suku Interaksi:** $\langle \hat{Z}_i \hat{Z}_j \rangle = \cos(2\theta_i)\cos(2\theta_j)$

Sehingga fungsi biaya (cost function) yang akan diminimalkan secara klasik adalah:
$$ J(\theta) = \sum_{i<j} J_{ij} \cos(2\theta_i)\cos(2\theta_j) + \sum_i h_i \cos(2\theta_i) + \text{offset} $$

---

## 7. Algoritma Variational Quantum Eigensolver (VQE)
VQE adalah algoritma *hybrid quantum-classical* yang memetakan masalah minimisasi energi ke dalam loop optimasi parameter $\theta$.

### A. Alur Kerja Hybrid secara Matematis
1.  **Preparasi State:** QPU menyiapkan state $|\psi(\theta)\rangle = U(\theta)|0\rangle^{\otimes n}$.
2.  **[[Dekomposisi_Hamiltonian]]:** Karena Hamiltonian $\hat{H}$ adalah kombinasi linear suku-suku Pauli $P_k \in \{I, X, Y, Z\}^{\otimes n}$:
    $$ \hat{H} = \sum_k c_k \hat{P}_k $$
3.  **Pengukuran:** Nilai ekspektasi dihitung sebagai:
    $$ \langle \hat{H} \rangle_{\theta} = \sum_k c_k \langle \psi(\theta) | \hat{P}_k | \psi(\theta) \rangle $$
4.  **Optimasi:** Optimizer klasik mencari $\theta^*$ yang meminimalkan $\langle \hat{H} \rangle_{\theta}$.

### B. Update Parameter ([[Parameter_Shift_Rule]])
Untuk optimasi berbasis gradien, QPU dapat menghitung gradien secara analitik tanpa memerlukan limit numerik:
$$ \frac{\partial \langle E \rangle}{\partial \theta_i} = \frac{1}{2} \left[ \langle E(\theta + \frac{\pi}{2}e_i) \rangle - \langle E(\theta - \frac{\pi}{2}e_i) \rangle \right] $$
Ini memungkinkan konvergensi yang lebih stabil dibandingkan estimasi beda hingga (finite difference).

---

## 8. Arsitektur Ansatz: EfficientSU2
Untuk menangani korelasi aset yang kompleks (suku $J_{ij}$), kita memerlukan ansatz yang memiliki *entanglement*.

### A. Formulasi Unitari Ansatz
Sirkuit `EfficientSU2` didefinisikan sebagai operator uniter $U(\theta)$ yang terdiri dari $d$ lapisan (layers):
$$ U(\theta) = L_d \dots L_1 L_0 $$
Di mana setiap lapisan $L_l$ (untuk $l > 0$) terdiri dari:
1.  **Entanglement Layer ($V_{ent}$):** Biasanya berupa gerbang CNOT linear atau full.
    $$ V_{ent} = \prod_{(i,j) \in \text{pairs}} CX_{i,j} $$
2.  **Rotation Layer ($R(\theta)$):**
    $$ R_i(\theta) = R_z(\theta_{i,l,2}) R_y(\theta_{i,l,1}) $$

### B. Efek Entanglement pada Ekspektasi (Derivasi 2-Qubit)
**Filosofi:** Entanglement adalah sumber daya non-lokal yang memungkinkan ansatz mengeksplorasi korelasi yang tidak dapat dipisahkan (*non-separable*).

**Jembatan Logika:** Kita bandingkan nilai ekspektasi $\langle \hat{Z}_1 \hat{Z}_2 \rangle$ antara sistem tanpa entanglement (Bab 6) dan sistem dengan entanglement (1 layer CNOT).

1.  **State Awal (Setelah Rotasi $R_y$):**
    $$ |\phi\rangle = R_y(2\theta_1)|0\rangle \otimes R_y(2\theta_2)|0\rangle $$
    $$ |\phi\rangle = (\cos\theta_1 |0\rangle + \sin\theta_1 |1\rangle) \otimes (\cos\theta_2 |0\rangle + \sin\theta_2 |1\rangle) $$
    *(Catatan: Menggunakan konvensi Bab 5 di mana rotasi menghasilkan $\cos\theta$)*

2.  **Aplikasi Entanglement (CNOT):**
    $$ |\psi\rangle = CX_{1,2} |\phi\rangle $$
    $$ |\psi\rangle = \cos\theta_1\cos\theta_2 |00\rangle + \cos\theta_1\sin\theta_2 |01\rangle + \sin\theta_1\cos\theta_2 |11\rangle + \sin\theta_1\sin\theta_2 |10\rangle $$
    *(Perhatikan bahwa koefisien $|10\rangle$ dan $|11\rangle$ tertukar karena kontrol qubit 1 bernilai 1)*

3.  **Pengukuran Ekspektasi $\langle \hat{Z}_1 \hat{Z}_2 \rangle$:**
    $$ \langle \hat{Z}_1 \hat{Z}_2 \rangle = \sum_{x \in \{0,1\}^2} P(x) \cdot \text{val}(\hat{Z}_1\hat{Z}_2) $$
    $$ \langle \hat{Z}_1 \hat{Z}_2 \rangle = (|\cos\theta_1\cos\theta_2|^2) \cdot (1) + (|\cos\theta_1\sin\theta_2|^2) \cdot (-1) + (|\sin\theta_1\cos\theta_2|^2) \cdot (1) + (|\sin\theta_1\sin\theta_2|^2) \cdot (-1) $$
    $$ \langle \hat{Z}_1 \hat{Z}_2 \rangle = \cos^2\theta_1(\cos^2\theta_2 - \sin^2\theta_2) + \sin^2\theta_1(\cos^2\theta_2 - \sin^2\theta_2) $$
    $$ \langle \hat{Z}_1 \hat{Z}_2 \rangle = (\cos^2\theta_1 + \sin^2\theta_1) \cos(2\theta_2) = \cos(2\theta_2) $$

**Kesimpulan Jembatan:**
Dibandingkan dengan sistem tanpa entanglement ($\cos 2\theta_1 \cos 2\theta_2$), entanglement "mencampur" parameter sehingga korelasi antar qubit tidak lagi bersifat multiplikatif sederhana. Ini memberikan derajat kebebasan bagi VQE untuk merepresentasikan kovarians aset yang kompleks dalam model Markowitz.

### C. Konvergensi Menuju Ground State
**Filosofi:** Optimasi adalah proses "pendinginan" numerik di mana state $|\psi(\theta)\rangle$ dipaksa sejajar dengan eigenvector energi terendah.

**Jembatan Logika:** Menggunakan [[ekspansi_state]] dalam basis eigen Hamiltonian $\hat{H} |v_i\rangle = E_i |v_i\rangle$.

1.  **Ekspansi State Parametrik:**
    $$ |\psi(\theta)\rangle = \sum_{i=0}^{2^n-1} \alpha_i(\theta) |v_i\rangle $$
    di mana $\sum |\alpha_i(\theta)|^2 = 1$.

2.  **Ekspektasi Energi:**
    $$ E(\theta) = \sum_i E_i |\alpha_i(\theta)|^2 $$

3.  **Proses Minimisasi:**
    Selama iterasi optimasi klasik, parameter $\theta$ diperbarui sedemikian sehingga bobot probabilitas $\alpha_i$ untuk $i > 0$ (state eksitasi) menuju nol, dan bobot untuk $i=0$ (ground state) menuju satu:
    $$ \lim_{\theta \to \theta^*} |\alpha_0(\theta)|^2 \approx 1 $$
    $$ \lim_{\theta \to \theta^*} E(\theta) \approx E_0 $$

Hasil akhirnya adalah state $|\psi(\theta^*)\rangle$ yang merupakan aproksimasi terbaik dari solusi portfolio optimal dalam ruang Hilbert.


---

## 9. Implementasi dan Penentuan Solusi Portfolio
Setelah konvergensi dicapai pada $\theta^*$, kita melakukan ekstraksi solusi melalui pengukuran akhir.

### A. Estimasi Probabilitas ([[Born_Rule]])
Probabilitas terpilihnya konfigurasi portfolio biner $x \in \{0, 1\}^N$ diberikan oleh:
$$ P(x) = |\langle x | \psi(\theta^*) \rangle|^2 $$

Dalam eksekusi riil dengan $M$ kali percobaan (*shots*), probabilitas ini diestimasi sebagai:
$$ \hat{P}(x) = \frac{\text{jumlah kemunculan bitstring } x}{M} $$

### B. Decoding ke Keputusan Investasi
Hasil akhir adalah bitstring $x$ dengan probabilitas tertinggi:
$$ x_{opt} = \arg\max_x \hat{P}(x) $$
- Jika $x_{opt} = [1, 0, 1, 0]$, maka keputusannya adalah membeli aset 1 dan 3, serta tidak membeli aset 2 dan 4.

### C. Verifikasi Constraint (Post-Selection)
Karena suku penalti $A$ dalam QUBO, solusi yang paling sering muncul diharapkan memenuhi batasan $\sum x_i = K$. Jika solusi terbaik melanggar batasan, kita dapat melakukan *post-selection* dengan mengambil solusi terbaik berikutnya dalam distribusi probabilitas yang memenuhi syarat batasan tersebut.

