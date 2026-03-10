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
$$ x^T \Sigma x = \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j = \sum_i \sigma^2_i x_i^2 + \sum_{i \ne j} \sigma_{ij} x_i x_j $$

Karena $x_i \in \{0,1\}$, maka $x_i^2 = x_i$. Persamaan menjadi:
$$ x^T \Sigma x = \sum_i \sigma_i^2 x_i + \sum_{i \ne j} \sigma_{ij} x_i x_j $$

Dimana $\sigma^2_i$ adalah varians aset $i$, dan $\sigma_{ij}$ adalah kovarians antar aset. Kovarians dapat dihitung melalui perkalian deviasi standar kedua aset ($\sigma_i \sigma_j$) dengan koefisien korelasi ($\rho_{ij}$):
$$ \sigma_{ij} = \sigma_i \sigma_j \rho_{ij} $$

Secara statistik, komponen-komponen ini dihitung sebagai berikut:
1. **Varians ($\sigma_i^2$):** mengukur volatilitas aset tunggal.
   $$ \sigma_i^2 = \frac{1}{T-1} \sum_{t=1}^T (R_{i,t} - \bar{R}_i)^2 $$
2. **Kovarians ($\sigma_{ij}$):** mengukur hubungan pergerakan antar dua aset.
   $$ \sigma_{ij} = \frac{1}{T-1} \sum_{t=1}^T (R_{i,t} - \bar{R}_i)(R_{j,t} - \bar{R}_j) $$
3. **Korelasi ($\rho_{ij}$):** menormalisasi kovarians ke dalam rentang [-1, 1].
   $$ \rho_{ij} = \frac{\sigma_{ij}}{\sigma_i \sigma_j} $$

Dengan return harian $R_{i,t} = \frac{P_{i,t} - P_{i,t-1}}{P_{i,t-1}}$ dan $\bar{R}_i$ adalah rata-rata return.

### B. Suku Kedua: Return ($\lambda \mu^T x$)
Menghitung keuntungan yang diharapkan:
$$ \mu_A = \frac{1}{T} \sum_{t=1}^T R_{A,t} $$
[[suku_pertama_kedua]]
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

---

## 3. Estimasi Parameter Alternatif: Perspektif Strategis & Informasi

Selain menggunakan statistik historis standar ($\mu, \sigma$), parameter Hamiltonian dapat diderivasi menggunakan pendekatan yang lebih fundamental untuk menangkap dinamika pasar yang kompleks.

### A. Pendekatan Game Theory (Medan Lokal $h_i$)
**Filosofi:** Model Markowitz standar mengasumsikan aset sebagai entitas pasif. Dalam perspektif ekonomi fisik, aset adalah pemain strategis yang berinteraksi dalam pasar yang kompetitif. Penentuan bias ($h_i$) diderivasi melalui hierarki logika teori permainan untuk menangkap "insentif strategis" ([[GT_to_h]]):

1. **Aksioma Utilitas:** Diasumsikan setiap aset (pemain) bertindak untuk memaksimalkan return sebagai representasi angka kepuasan.
2. **Transisi Model:** Beranjak dari model *Zero-Sum* (konflik murni) menuju *Non Zero-Sum* yang lebih realistis, di mana payoff satu aset dipengaruhi secara dinamis oleh kombinasi aksi aset lainnya.
3. **Mixed Strategy Nash Equilibrium (MSNE):** Karena ketidakpastian pasar, pemain menggunakan strategi probabilitas. Data historis (frekuensi $n$) digunakan sebagai manifestasi empiris dari strategi campuran yang telah dimainkan pasar.

**Jembatan Logika:** Parameter bias $h_i$ didefinisikan sebagai setengah dari selisih *Marginal Expected Payoff* antara strategi beli ($s_i = +1$) dan strategi hindari ($s_i = -1$):
$$ h_i = \frac{E[s_i = +1] - E[s_i = -1]}{2} \qquad (1) $$
Secara fisik, ini setara dengan *medan magnet eksternal* atau **"Gaya Pasang Surut" (Tidal Forces)** pasar. Jika payoff marginal positif, medan ini memberikan tekanan energi yang menarik qubit ke arah ground state $|1\rangle$. Hal ini secara filosofis masuk akal karena mentransformasikan probabilitas strategis masa lalu menjadi tekanan fisik pada lanskap energi Hamiltonian.

### B. Pendekatan Quantum Mutual Information (Interaksi $J_{ij}$)
**Filosofi:** Korelasi antar aset seringkali memiliki dimensi non-linear yang melampaui statistik kovarians $\sigma_{ij}$. *Quantum Mutual Information* (QMI) menyediakan kerangka untuk mengukur total korelasi (klasik dan kuantum) dalam ruang Hilbert ([[QMI]]).

**Jembatan Logika:** Kekuatan interaksi $J_{ij}$ dapat diproksi melalui volume informasi yang dibagikan antar qubit, yang dihitung menggunakan entropi *Von Neumann* ($S$):
$$ I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) \qquad (2) $$
Secara filosofis, korelasi pasar dipandang sebagai manifestasi dari *entanglement* informasi. Menggunakan QMI sebagai landasan $J_{ij}$ memungkinkan VQE menangkap dependensi yang lebih dalam, di mana $J_{ij}$ yang besar berarti kedua aset "beresonansi" dalam aliran informasi yang sama.

---

## 4. Transformasi Markowitz ke QUBO (General Form)
Untuk mentransformasikan model Markowitz ke dalam bentuk QUBO $\min \sum_{i,j} Q_{ij} x_i x_j$, kita harus mengekspansi seluruh suku dalam fungsi objektif $\mathcal{L}(x)$.

### Langkah 1: Ekspansi Suku-Suku Objektif
1. **Risiko:** $\sum_i \sigma_i^2 x_i + \sum_{i \neq j} \sigma_{ij} x_i x_j$
2. **Return:** $-\lambda \sum_i \mu_i x_i$
3. **Penalti:** $A \left( \sum_i x_i - K \right)^2 = A \left( \sum_i x_i^2 + 2 \sum_{i < j} x_i x_j - 2K \sum_i x_i + K^2 \right)$

### Langkah 2: Penggabungan dan Penyederhanaan
Substitusi properti biner $x_i^2 = x_i$:
$$ \mathcal{L}(x) = \sum_i \sigma_i^2 x_i + \sum_{i \neq j} \sigma_{ij} x_i x_j - \lambda \sum_i \mu_i x_i + A \left( \sum_i x_i + 2 \sum_{i < j} x_i x_j - 2K \sum_i x_i + K^2 \right) $$

Kelompokkan berdasarkan derajat variabel ($x_i$ dan $x_i x_j$):
$$ \mathcal{L}(x) = \sum_i (\sigma_i^2 - \lambda \mu_i + A - 2AK) x_i + \sum_{i \neq j} (\sigma_{ij} + A) x_i x_j + AK^2 $$

### Langkah 3: Definisi Matriks QUBO ($Q$)
Dalam format standar QUBO, koefisien dibagi menjadi diagonal ($Q_{ii}$) dan off-diagonal ($Q_{ij}$):
- **Elemen Diagonal (Suku Linear $x_i$):**
  $$ Q_{ii} = \sigma_i^2 - \lambda \mu_i + A(1 - 2K) $$
- **Elemen Off-Diagonal (Suku Interaksi $x_i x_j$):**
  $$ Q_{ij} = \sigma_{ij} + A $$

Sehingga fungsi objektif akhir dalam bentuk QUBO adalah:
$$ \mathcal{L}(x) = \sum_{i=1}^N Q_{ii} x_i + \sum_{i < j}^N 2Q_{ij} x_i x_j + \text{offset} $$
di mana $\text{offset} = AK^2$. Dalam prakteknya, konstanta ini sering diabaikan karena tidak mempengaruhi lokasi titik minimum (ground state).

---

### Interpretasi Koefisien:
1. **$Q_{ii}$**: Mengukur "daya tarik" aset $i$ secara individu. Nilai akan mengecil (lebih disukai) jika return $\mu_i$ tinggi atau varians $\sigma_i^2$ rendah.
2. **$Q_{ij}$**: Mengukur hubungan antar dua aset. Nilai akan membesar (dihindari) jika kovarians $\sigma_{ij}$ positif atau penalti $A$ besar, yang memaksa sistem untuk memilih tepat $K$ aset.

---

## 4. Transformasi QUBO ke Ising (General Form)
Untuk sistem $N$ aset, kita menggunakan transformasi $x_i = \frac{1 - s_i}{2}$ pada setiap variabel.

### Langkah 1: Substitusi ke Bentuk QUBO
$$ E(s) = \sum_i Q_{ii} \left( \frac{1-s_i}{2} \right) + \sum_{i<j} 2Q_{ij} \left( \frac{1-s_i}{2} \right) \left( \frac{1-s_j}{2} \right) + \text{offset} $$

### Langkah 2: Identifikasi Parameter Hamiltonian
Setelah ekspansi aljabar, kita mendapatkan bentuk Ising $H = \sum_{i<j} J_{ij} s_i s_j + \sum_i h_i s_i + C$:

- **Interaksi (Coupling $J_{ij}$):**
  $$ J_{ij} = \frac{Q_{ij}}{2} $$
- **Medan Lokal (Field $h_i$):**
  $$ h_i = -\frac{1}{2} Q_{ii} - \sum_{j \neq i} \frac{Q_{ij}}{2} $$
- **Konstanta (Energy Offset $C$):**
  $$ C = \text{offset} + \sum_i \frac{Q_{ii}}{2} + \sum_{i<j} \frac{Q_{ij}}{2} $$

### Representasi Operator Pauli
$$ \hat{H} = \sum_{i<j} J_{ij} \hat{Z}_i \hat{Z}_j + \sum_i h_i \hat{Z}_i + C \cdot \hat{I} $$
Formula ini berlaku untuk jumlah aset $N$ berapapun, menjadikannya model yang skalabel untuk optimasi portofolio besar.

---

## 5. Ekspektasi Energi dan Optimasi Parametrik
Tujuan kita adalah mencari parameter $\theta$ yang meminimalkan nilai ekspektasi Hamiltonian.

### A. Ansatz Tanpa Entanglement
Jika kita menggunakan ansatz produk $|\psi(\theta)\rangle = \bigotimes_{i=1}^N R_y(\theta_i)|0\rangle$, nilai ekspektasi energinya adalah:
$$ \langle E(\theta) \rangle = \sum_{i<j} J_{ij} \cos(2\theta_i)\cos(2\theta_j) + \sum_i h_i \cos(2\theta_i) + C $$

Fungsi ini adalah lanskap energi non-linear yang akan ditelusuri oleh optimizer klasik. Secara fisik, $\theta_i$ menentukan probabilitas "spin" aset $i$ mengarah ke $+1$ atau $-1$.

### B. Gradien Analitik
Gradien terhadap parameter $\theta_k$ dapat dihitung secara langsung:
$$ \frac{\partial \langle E \rangle}{\partial \theta_k} = -2\sin(2\theta_k) \left[ \sum_{j \neq k} J_{kj} \cos(2\theta_j) + h_k \right] $$

Persamaan gradien ini menunjukkan bahwa perubahan pada satu aset $\theta_k$ dipengaruhi oleh "medan efektif" yang dihasilkan oleh aset lainnya ($J_{kj}$) dan medan lokalnya sendiri ($h_k$).

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

### B. Optimasi Parameter: SPSA vs. Gradient Descent
Dalam sistem kuantum riil (noisy), estimasi gradien menggunakan [[Parameter_Shift_Rule]] atau beda hingga (finite difference) sangat rentan terhadap noise karena memerlukan banyak pengukuran ($2N$ pengukuran per iterasi).

#### 1. Masalah Gradient Descent (GD)
GD menghitung turunan parsial terhadap setiap parameter $\theta_i$ secara bergantian. Pada lanskap energi yang "kasar" akibat noise statistik (*shot noise*), GD cenderung terjebak pada local minima atau gagal konvergen karena estimasi gradien yang bias.

#### 2. Mekanisme [[SPSA]] (Simultaneous Perturbation Stochastic Approximation)
SPSA adalah algoritma optimasi stokastik yang jauh lebih efisien untuk VQE. Alih-alih mengukur gradien satu per satu, SPSA melakukan perturbasi pada **seluruh parameter sekaligus** menggunakan vektor acak $\Delta$:

1.  **Perturbasi Acak:** Pilih vektor $\Delta_k$ di mana setiap elemen bernilai $\pm 1$ secara acak (distribusi Bernoulli).
2.  **Estimasi Gradien Stokastik:** Hitung gradien pendekatan $g(\theta_k)$ hanya dengan **dua pengukuran** fungsi biaya:
    $$ \hat{g}(\theta_k) = \frac{E(\theta_k + c_k \Delta_k) - E(\theta_k - c_k \Delta_k)}{2 c_k \Delta_k} $$
    di mana $c_k$ adalah besarnya perturbasi yang mengecil seiring iterasi.
3.  **Update Parameter:**
    $$ \theta_{k+1} = \theta_k - a_k \hat{g}(\theta_k) $$

#### 3. Keunggulan SPSA untuk Markowitz-VQE
- **Efisiensi Skalabilitas:** Hanya memerlukan 2 *evaluasi fungsi* per iterasi, terlepas dari jumlah aset $N$. GD memerlukan $2N$ evaluasi.
- **Robustness terhadap Noise:** SPSA memiliki sifat "averaging" alami yang membuatnya lebih tahan terhadap fluktuasi statistik hasil pengukuran QPU dibandingkan optimizer berbasis gradien analitik.
- **Konvergensi Global:** Karena sifat stokastiknya, SPSA memiliki peluang lebih besar untuk melompati *local minima* kecil pada lanskap energi portfolio.

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

