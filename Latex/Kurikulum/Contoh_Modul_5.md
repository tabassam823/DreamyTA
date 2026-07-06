# Contoh Perhitungan Numerik Modul 5: VQE & SPSA

Dokumen ini memberikan ilustrasi numerik eksplisit untuk membantu mahasiswa memahami mekanisme internal dari sirkuit *EfficientSU2* dan algoritma optimasi SPSA yang digunakan dalam proyek portofolio kuantum.

---

## 1. Simulasi Numerik: Arsitektur EfficientSU2 (2 Qubit)

Kita akan mensimulasikan satu lapisan rotasi $RY$ dan satu gerbang keterbelitan CNOT pada sistem dua qubit.

### A. Keadaan Awal (Initial State)
Sistem dimulai pada *basis state* $|00\rangle$:
$$ |\psi_0\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \qquad (1) $$

### B. Lapisan Rotasi SU(2) (Ry dan Rz)
Dalam *EfficientSU2*, setiap qubit mengalami rotasi $R_y$ diikuti $R_z$. Misalkan pada qubit 0:
- Sudut rotasi: $\theta_{y} = \pi/2$, $\theta_{z} = \pi/4$.

1. **Rotasi $R_y(\pi/2)$**:
   Kita gunakan matriks rotasi $R_y(\theta)$ dari Persamaan (13) di Modul 5 dengan $\theta/2 = \pi/4$:
   $$ R_y(\pi/2) |0\rangle = \begin{pmatrix} \cos(\pi/4) & -\sin(\pi/4) \\ \sin(\pi/4) & \cos(\pi/4) \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} $$
   $$ R_y(\pi/2) |0\rangle = \begin{pmatrix} 0.707 & -0.707 \\ 0.707 & 0.707 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0.707(1) + (-0.707)(0) \\ 0.707(1) + 0.707(0) \end{pmatrix} = \begin{pmatrix} 0.707 \\ 0.707 \end{pmatrix} $$

2. **Rotasi $R_z(\pi/4)$**:
   $$ R_z(\pi/4) \begin{pmatrix} 0.707 \\ 0.707 \end{pmatrix} = \begin{pmatrix} e^{-i\pi/8} & 0 \\ 0 & e^{i\pi/8} \end{pmatrix} \begin{pmatrix} 0.707 \\ 0.707 \end{pmatrix} \approx \begin{pmatrix} 0.653 - 0.271i \\ 0.653 + 0.271i \end{pmatrix} \qquad (2) $$

Hasil di atas adalah *state* untuk satu qubit tunggal. Untuk masuk ke sistem dua qubit, kita harus melakukan operasi produk tensor.

### C. Transisi ke Sistem Dua Qubit dan Lapisan Keterbelitan
Sirkuit *EfficientSU2* bekerja pada seluruh register qubit. Jika kita hanya memutar qubit 0, maka operator totalnya adalah $\text{Rot}_{SU(2)} \otimes I$. Sesuai dengan rumus di Modul 5, *state* rotasi sistem $|\psi_{rot}\rangle$ diperoleh melalui:

$$ |\psi_{rot}\rangle = (\text{Rot}_{SU(2)} \otimes I) |00\rangle = (\text{Rot}_{SU(2)} |0\rangle) \otimes (I |0\rangle) $$
$$ |\psi_{rot}\rangle = \begin{pmatrix} 0.653 - 0.271i \\ 0.653 + 0.271i \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} (0.653 - 0.271i) \times 1 \\ (0.653 - 0.271i) \times 0 \\ (0.653 + 0.271i) \times 1 \\ (0.653 + 0.271i) \times 0 \end{pmatrix} = \begin{pmatrix} 0.653 - 0.271i \\ 0 \\ 0.653 + 0.271i \\ 0 \end{pmatrix} \qquad (3) $$

Setelah *state* sistem dua qubit terbentuk, kita aplikasikan gerbang keterbelitan $CX_{0,1}$. Sesuai matriks CNOT, elemen ke-3 dan ke-4 (indeks berbasis 1) akan ditukar:

$$ |\psi_{ent}\rangle = CX_{0,1} |\psi_{rot}\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0.653 - 0.271i \\ 0 \\ 0.653 + 0.271i \\ 0 \end{pmatrix} = \begin{pmatrix} 0.653 - 0.271i \\ 0 \\ 0 \\ 0.653 + 0.271i \end{pmatrix} \qquad (4) $$

**Interpretasi Hasil**: *State* akhir kini menjadi $(0.653 - 0.271i)|00\rangle + (0.653 + 0.271i)|11\rangle$. Ini tetap merupakan *entangled state* yang setara dengan *Bell State*, namun dengan tambahan informasi fase relatif. Secara finansial, ini menunjukkan korelasi kuantum yang kini mencakup dimensi fase (kapan korelasi itu terjadi secara dinamis), bukan sekadar probabilitas statis. Korelasi kompleks inilah yang dieksploitasi oleh VQE untuk menemukan struktur dependensi pasar yang tidak tertangkap oleh metode klasik.

### D. Penjelasan Depth Kedua
Pada **Depth 1**, sirkuit diakhiri setelah satu lapisan $CX$. Untuk **Depth 2**, proses di atas (Rotasi + Entanglement) diulangi kembali dengan set parameter $\theta$ yang baru. Secara matematis, hal ini meningkatkan derajat non-linearitas pemetaan ruang Hilbert. Jika pada Depth 1 kita hanya memiliki keterbelitan antar tetangga, pada Depth 2 kita bisa menghasilkan superposisi yang jauh lebih kompleks seperti $\alpha|00\rangle + \beta|01\rangle + \gamma|10\rangle + \delta|11\rangle$, memberikan fleksibilitas lebih bagi algoritma untuk menemukan solusi optimal di pasar yang dinamis.

---

## 2. Simulasi Numerik: Satu Iterasi Optimasi SPSA

Misalkan kita ingin meminimalkan fungsi energi sederhana $L(\theta_1, \theta_2) = 0.5\theta_1^2 + 2\theta_2^2$ (sebagai analogi risiko portofolio).

### A. Parameter Awal
- Posisi saat ini: $\theta_k = [1.0, 1.0]$
- *Learning rate*: $a_k = 0.1$
- Langkah perturbasi: $c_k = 0.2$
- Vektor perturbasi acak: $\Delta_k = [1, -1]$ (distribusi Bernoulli)

### B. Pengukuran Energi Berisik
Kita hitung energi pada dua titik perturbasi (asumsikan tanpa *noise* untuk kemudahan hitung):
1. **Titik Positif** ($\theta_k + c_k \Delta_k$):
   $$ \theta^{(+)} = [1.0 + 0.2(1), 1.0 + 0.2(-1)] = [1.2, 0.8] $$
   $$ y^{(+)} = 0.5(1.2)^2 + 2(0.8)^2 = 0.5(1.44) + 2(0.64) = 0.72 + 1.28 = 2.00 \qquad (5) $$

2. **Titik Negatif** ($\theta_k - c_k \Delta_k$):
   $$ \theta^{(-)} = [1.0 - 0.2(1), 1.0 - 0.2(-1)] = [0.8, 1.2] $$
   $$ y^{(-)} = 0.5(0.8)^2 + 2(1.2)^2 = 0.5(0.64) + 2(1.44) = 0.32 + 2.88 = 3.20 \qquad (6) $$

### C. Estimasi Gradien Simultan
Hitung selisih energi: $\Delta y = y^{(+)} - y^{(-)} = 2.00 - 3.20 = -1.20$.
Gunakan rumus estimasi gradien (Persamaan 12 di [[Modul_5]]):
- Untuk $\theta_1$: $\hat{g}_{k1} = \frac{-1.20}{2(0.2)(1)} = \frac{-1.20}{0.4} = -3.0$
- Untuk $\theta_2$: $\hat{g}_{k2} = \frac{-1.20}{2(0.2)(-1)} = \frac{-1.20}{-0.4} = 3.0$

**Vektor Gradien Terestimasi**: $\hat{g}_k = [-3.0, 3.0]$.

### D. Pembaruan Parameter (Update Step)
Terapkan aturan pembaruan:
$$ \theta_{k+1} = \theta_k - a_k \hat{g}_k $$
$$ \theta_{k+1} = [1.0, 1.0] - 0.1[-3.0, 3.0] $$
$$ \theta_{k+1} = [1.0 + 0.3, 1.0 - 0.3] = [1.3, 0.7] \qquad (7) $$

**Analisis**: Parameter $\theta_2$ yang memiliki bobot risiko lebih besar (koefisien 2) diturunkan secara signifikan dari 1.0 ke 0.7, sementara $\theta_1$ disesuaikan ke 1.3 untuk mencari titik minimum fungsional energi. Proses ini akan berulang hingga gradien mendekati nol.

---

## 3. Simulasi Numerik: Konvergensi SPSA

Mahasiswa sering bertanya: "Kapan algoritma berhenti?" Algoritma dianggap konvergen ketika perubahan energi ($\Delta E$) atau perubahan parameter ($\Delta \theta$) berada di bawah ambang batas toleransi ($\epsilon$).

### Contoh Numerik Kondisi Konvergen:
Misalkan pada iterasi $k=100$, kita memiliki:
- $\theta_{100} = [0.0012, 0.0005]$
- Energi terukur $y_{100} = -4.9998$

Pada iterasi $k=101$:
1. **Perturbasi**: $\theta^{(+)} = [0.0013, 0.0004]$, $\theta^{(-)} = [0.0011, 0.0006]$
2. **Energi**: $y^{(+)} = -4.99982$, $y^{(-)} = -4.99978$
3. **Selisih**: $\Delta y = -0.00004$
4. **Estimasi Gradien**: $\hat{g} = [-0.0001, 0.0001]$
5. **Update**: $\theta_{101} = \theta_{100} - 0.01[-0.0001, 0.0001] = [0.001201, 0.000499]$

**Analisis Konvergensi:**
- Perubahan parameter: $|\theta_{101} - \theta_{100}| \approx 10^{-6}$
- Perubahan energi: $|y_{101} - y_{100}| \approx 10^{-7}$

---

## 4. Estimasi Nilai Ekspektasi Energi dan Interpretasi Logis

Setelah sirkuit kuantum menyiapkan *state* $|\psi(\theta)\rangle$ melalui lapisan rotasi dan keterbelitan, langkah krusial berikutnya dalam algoritma VQE adalah ekstraksi informasi energi. Energi total sistem tidak diperoleh melalui satu kali pengukuran tunggal yang deterministik, melainkan melalui estimasi statistik dari nilai ekspektasi operator Hamiltonian $\hat{H}$. Mengingat $\hat{H}$ pada model Ising didekomposisi menjadi jumlahan operator Pauli-$Z$, maka nilai ekspektasi total adalah jumlahan terbobot dari ekspektasi masing-masing suku lokal dan interaksi.

### A. Mekanisme Estimasi melalui Sampling (Shot-based Measurement)
Secara matematis, nilai ekspektasi energi $\langle H(\theta) \rangle$ dihitung dengan mengukur proyeksi *state* kuantum terhadap basis komputasi. Karena Hamiltonian Ising terdiri dari jajaran operator $\sigma^z$, kita dapat memecah kalkulasi energi menjadi:

$$ \langle H(\theta) \rangle = \sum_i h_i \langle \sigma_i^z \rangle + \sum_{i<j} J_{ij} \langle \sigma_i^z \sigma_j^z \rangle \qquad (8) $$

Nilai $\langle \sigma_i^z \rangle$ diperoleh dengan melakukan *sampling* (misal: 1024 *shots*) pada sirkuit kuantum. Setiap *shot* akan menghasilkan bitstring biner $s \in \{0, 1\}^N$. Untuk setiap suku $\sigma_i^z$, hasil pengukuran 0 dipetakan ke $+1$ dan hasil 1 dipetakan ke $-1$. Jika $n_0$ adalah jumlah munculnya $|0\rangle$ dan $n_1$ adalah jumlah munculnya $|1\rangle$, maka nilai ekspektasi lokalnya adalah:

$$ \langle \sigma_i^z \rangle = \frac{n_0 - n_1}{n_0 + n_1} \qquad (9) $$

Proses ini dilakukan secara simultan untuk seluruh suku dalam Hamiltonian. Rata-rata terbobot dari hasil pengukuran inilah yang menghasilkan angka energi tunggal (skalar) yang kemudian digunakan oleh optimisator klasik SPSA untuk mengevaluasi kualitas parameter $\theta$ pada iterasi tersebut.

### B. Interpretasi Logis: Energi sebagai Proksi Efisiensi Portofolio
Interpretasi logis dari nilai energi dalam konteks ekonofisika adalah sebagai fungsi biaya (*cost function*) yang merepresentasikan derajat ketidakefisienan portofolio. Keadaan dasar (*ground state*) dengan energi terendah secara fisik identik dengan konfigurasi aset yang memberikan keseimbangan optimal antara risiko dan imbal hasil (*risk-return tradeoff*). Nilai energi yang tinggi mengindikasikan bahwa portofolio tersebut memiliki profil risiko yang ekstrem atau melanggar kendala kardinalitas $K$ yang telah ditetapkan.

Kopling interaksi $J_{ij}$ dalam Hamiltonian berfungsi sebagai gaya penalti terhadap korelasi aset yang tidak diinginkan, sementara bias lokal $h_i$ mendorong sistem menuju aset dengan performa individual yang unggul. Dengan demikian, minimalisasi energi dalam VQE secara efektif merupakan proses pencarian titik ekuilibrium di mana seluruh variabel ekonomi mencapai stabilitas matematis. Keberhasilan VQE dalam mencapai konvergensi pada energi minimum menjamin bahwa bitstring yang dihasilkan adalah representasi dari portofolio yang paling efisien dalam ruang solusi yang tersedia.