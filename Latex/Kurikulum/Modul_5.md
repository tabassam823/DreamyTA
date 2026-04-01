# Modul 5: Variational Quantum Eigensolver (VQE)

Modul ini akan membahas algoritma hibrida klasik-kuantum yang digunakan untuk menyelesaikan masalah optimasi portofolio dengan mencari energi keadaan dasar (*ground state*) dari sebuah sistem Hamiltonian Ising. Mahasiswa akan mempelajari bagaimana prinsip-prinsip mekanika kuantum diaplikasikan pada domain ekonofisika untuk mendapatkan solusi optimal dalam keterbatasan perangkat keras kuantum saat ini.

## 1. Pendahuluan: Paradigma Komputasi Kuantum NISQ

Era *Noisy Intermediate-Scale Quantum* (NISQ) ditandai dengan ketersediaan perangkat kuantum yang memiliki jumlah qubit terbatas dan tingkat kebisingan (*noise*) yang signifikan. Dalam konteks ini, algoritma kuantum murni seperti algoritma Grover atau Shor sering kali tidak praktis karena membutuhkan *error correction* yang sangat besar. Oleh karena itu, pendekatan hibrida klasik-kuantum seperti *Variational Quantum Eigensolver* (VQE) menjadi solusi yang sangat relevan. VQE memanfaatkan keunggulan komputer kuantum dalam merepresentasikan ruang Hilbert yang besar, sementara tugas optimasi parameter dilakukan oleh komputer klasik yang lebih stabil.

Implementasi VQE dalam optimasi portofolio didasarkan pada pemetaan fungsi biaya (*cost function*) keuangan ke dalam operator Hamiltonian $\hat{H}$. Masalah pemilihan aset yang awalnya merupakan masalah optimasi kombinatorial klasik, kini ditransformasikan menjadi pencarian nilai eigen terendah dari $\hat{H}$. Proses ini bersifat iteratif, di mana sirkuit kuantum menyiapkan sebuah state percobaan (*trial state*) $|\psi(\theta)\rangle$ yang kemudian diukur energinya. Data pengukuran tersebut dikirim kembali ke optimisator klasik untuk memperbarui parameter $\theta$ guna meminimalkan ekspektasi energi pada iterasi berikutnya.

## 2. Landasan Teori: Prinsip Variasional dan Hamiltonian Ising

Fondasi utama dari algoritma VQE adalah Prinsip Variasional (*Variational Principle*) dalam mekanika kuantum. Prinsip ini menyatakan bahwa nilai ekspektasi energi dari sembarang fungsi gelombang percobaan $|\psi_{trial}\rangle$ akan selalu merupakan batas atas (*upper bound*) bagi energi keadaan dasar sejati ($E_0$) dari sebuah sistem. Secara matematis, jika kita memiliki Hamiltonian $\hat{H}$ dengan energi keadaan dasar $E_0$, maka untuk sembarang state $|\psi\rangle$ yang ternormalisasi, berlaku ketidaksamaan berikut:

$$ \langle \psi | \hat{H} | \psi \rangle \geq E_0 \qquad (1) $$

Penurunan rumus ini sangat krusial untuk memahami validitas VQE. Misalkan $|n\rangle$ adalah set lengkap dari state eigen dari $\hat{H}$ dengan nilai eigen $E_n$, sedemikian sehingga $\hat{H}|n\rangle = E_n|n\rangle$. Kita asumsikan state eigen ini telah diurutkan berdasarkan energinya, yaitu $E_0 \leq E_1 \leq E_2 \leq \dots$. Sembarang fungsi gelombang percobaan $|\psi\rangle$ dapat diekspansikan sebagai kombinasi linier dari state-state eigen tersebut:

$$ |\psi\rangle = \sum_n c_n |n\rangle \qquad (2) $$

Di mana $c_n$ adalah koefisien kompleks yang memenuhi syarat normalisasi $\sum_n |c_n|^2 = 1$. Jika kita menghitung nilai ekspektasi energi dari state $|\psi\rangle$, kita mendapatkan:

$$ \langle E \rangle = \langle \psi | \hat{H} | \psi \rangle \qquad (3) $$

Substitusikan persamaan (2) ke dalam persamaan (3):

$$ \langle E \rangle = \left( \sum_m c_m^* \langle m | \right) \hat{H} \left( \sum_n c_n | n \rangle \right) \qquad (4) $$

Karena $\hat{H}$ bersifat linier dan $|n\rangle$ adalah state eigen, maka $\hat{H}|n\rangle = E_n|n\rangle$. Persamaan (4) menjadi:

$$ \langle E \rangle = \sum_m \sum_n c_m^* c_n E_n \langle m | n \rangle \qquad (5) $$

Mengingat sifat ortonormalitas dari basis state eigen, di mana $\langle m | n \rangle = \delta_{mn}$ (bernilai 1 jika $m=n$ dan 0 jika lainnya), maka jumlahan ganda pada persamaan (5) menyusut menjadi:

$$ \langle E \rangle = \sum_n |c_n|^2 E_n \qquad (6) $$

Karena kita telah menetapkan bahwa $E_n \geq E_0$ untuk semua $n$, maka kita dapat menuliskan ketidaksamaan:

$$ \sum_n |c_n|^2 E_n \geq \sum_n |c_n|^2 E_0 \qquad (7) $$

Dengan mengeluarkan $E_0$ dari jumlahan karena nilainya konstan terhadap $n$, dan menggunakan syarat normalisasi $\sum_n |c_n|^2 = 1$, kita peroleh:

$$ \langle E \rangle \geq E_0 (1) \implies \langle E \rangle \geq E_0 \qquad (8) $$

Pembuktian ini menunjukkan bahwa dengan meminimalkan nilai ekspektasi $\langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle$ melalui variasi parameter $\theta$, kita secara sistematis mendekati energi keadaan dasar sejati $E_0$. Dalam praktiknya, kita menggunakan variabel biner portofolio $x_i \in \{0, 1\}$ yang dipetakan ke operator spin Pauli-Z melalui transformasi $Z_i = 1 - 2x_i$. Hamiltonian Ising total yang dibangun untuk optimasi portofolio memiliki bentuk:

$$ \hat{H} = \sum_i h_i \sigma_i^z + \sum_{i<j} J_{ij} \sigma_i^z \sigma_j^z \qquad (9) $$

Di mana $h_i$ merepresentasikan bias lokal (terkait dengan imbal hasil dan penalti risiko) dan $J_{ij}$ merepresentasikan kopling antar aset (terkait dengan kovariansi dan penalti kendala jumlah aset). VQE bertugas mencari konfigurasi spin $\{\sigma_1, \sigma_2, \dots, \sigma_N\}$ yang meminimalkan nilai ekspektasi dari operator $\hat{H}$ tersebut.

## 3. Arsitektur Sirkuit: Teori Grup SU(2) dan Ansatz EfficientSU2

Untuk memahami bagaimana sebuah sirkuit kuantum variabel parameter bekerja, mahasiswa harus terlebih dahulu memahami mekanisme dasar manipulasi *state* kuantum melalui lensa aljabar linier dan teori grup. Ansatz yang digunakan dalam algoritma ini berbasis pada arsitektur *EfficientSU2*, yang merupakan spesialisasi dari grup uniter spesial derajat 2, atau $SU(2)$. Grup ini mendefinisikan seluruh transformasi rotasi yang mungkin terjadi pada sebuah qubit tunggal dalam ruang Hilbert dua dimensi.

### A. Generator dan Grup SU(2)
Grup $SU(2)$ terdiri dari matriks uniter $2 \times 2$ dengan determinan +1. Secara fisik, setiap elemen dalam grup ini dapat direpresentasikan sebagai rotasi pada bola Bloch. Transformasi ini dibangun oleh tiga generator yang merupakan matriks Pauli ($\sigma_x, \sigma_y, \sigma_z$):

$$ \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \qquad (9) $$

Sebuah operator rotasi terhadap sumbu unit $\hat{n}$ dengan sudut $\theta$ didefinisikan melalui eksponensial matriks dari generator tersebut:

$$ R_{\hat{n}}(\theta) = \exp\left(-i \frac{\theta}{2} \hat{n} \cdot \vec{\sigma}\right) \qquad (10) $$

Penurunan eksplisit untuk operator rotasi $R_y(\theta)$ dapat dilakukan dengan menggunakan ekspansi deret Taylor untuk eksponensial matriks:

$$ R_y(\theta) = \exp\left(-i \frac{\theta}{2} \sigma_y\right) = \sum_{k=0}^{\infty} \frac{1}{k!} \left(-i \frac{\theta}{2} \sigma_y\right)^k \qquad (11) $$

Mengingat sifat matriks Pauli $\sigma_y^2 = I$, kita dapat memisahkan deret tersebut menjadi suku genap dan ganjil:

$$ R_y(\theta) = I \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k)!} \left(\frac{\theta}{2}\right)^{2k} - i \sigma_y \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!} \left(\frac{\theta}{2}\right)^{2k+1} \qquad (12) $$

Dengan mengenali deret Taylor untuk fungsi trigonometri $\cos$ dan $\sin$, kita mendapatkan bentuk matriks rotasi yang sangat familiar:

$$ R_y(\theta) = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) \sigma_y = \begin{pmatrix} \cos(\frac{\theta}{2}) & -\sin(\frac{\theta}{2}) \\ \sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2}) \end{pmatrix} \qquad (13) $$

Prosedur yang sama berlaku untuk $R_z(\theta)$, menghasilkan matriks diagonal yang mengubah fase relatif qubit:

$$ R_z(\theta) = \exp\left(-i \frac{\theta}{2} \sigma_z\right) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} \qquad (14) $$

### B. Struktur Ansatz EfficientSU2
Arsitektur *EfficientSU2* memanfaatkan kombinasi gerbang $R_y$ dan $R_z$ untuk menjamin universalitas rotasi pada satu qubit tunggal dengan jumlah parameter minimum (2 parameter per qubit). Struktur ini disusun secara modular dalam bentuk *reps* (repetisi) yang terdiri dari dua lapisan utama:

1.  **Lapisan Rotasi ($L$):** Mengaplikasikan transformasi lokal $\text{Rot}_{SU(2)}(\theta) = R_z(\theta_2) R_y(\theta_1)$ pada setiap qubit secara independen.
2.  **Lapisan Keterbelitan ($W$):** Mengaplikasikan gerbang CNOT ($CX$) untuk menciptakan korelasi non-lokal antar qubit (aset).

Dalam representasi matriks $4 \times 4$ untuk sistem dua qubit, gerbang CNOT ($CX$) dengan qubit 0 sebagai kontrol dan qubit 1 sebagai target didefinisikan sebagai:

$$ CX_{0,1} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \qquad (15) $$

Gerbang ini bersifat non-parameterisasi dan berfungsi untuk memetakan *basis state* $|c, t\rangle$ menjadi $|c, t \oplus c\rangle$, di mana $\oplus$ adalah operasi penambahan modulo 2 (XOR). Transformasi total sirkuit dengan kedalaman $d$ repetisi dapat dinyatakan sebagai operator uniter $U(\theta)$ yang bekerja pada *initial state* $|0\rangle^{\otimes N}$:

$$ |\psi(\theta)\rangle = L_d(\theta_d) \left( \prod_{i=0}^{d-1} W_{ent} L_i(\theta_i) \right) |0\rangle^{\otimes N} \qquad (16) $$

Di mana $W_{ent}$ adalah operator keterbelitan kolektif yang terdiri dari jajaran gerbang $CX$ sesuai pola konektivitas (misal: *Linear Entanglement*):

$$ W_{ent} = \prod_{j=0}^{N-2} CX_{j, j+1} \qquad (17) $$

Tanpa lapisan keterbelitan $W_{ent}$, sirkuit hanya akan mampu merepresentasikan *product states* ($|\psi\rangle = |\phi_1\rangle \otimes |\phi_2\rangle \otimes \dots$), yang secara finansial berarti aset-aset dalam portofolio dianggap tidak memiliki korelasi. Dengan adanya $W_{ent}$, VQE dapat mengeksplorasi ruang Hilbert yang jauh lebih luas untuk menangkap dinamika kompleks dalam matriks kovariansi aset keuangan.

### C. Konsep Adaptive Depth
Implementasi sirkuit pada perangkat NISQ menuntut keseimbangan antara ekspresivitas dan kebisingan (*noise*). Di sinilah peran **Adaptive Depth** menjadi krusial. Alih-alih menetapkan jumlah repetisi $d$ secara statis di awal, algoritma secara adaptif menambah kompleksitas sirkuit dengan meningkatkan nilai $d$ hanya jika target konvergensi energi belum tercapai.

Secara formal, setiap penambahan satu unit *depth* ($d \to d+1$) akan menambah jumlah parameter variabel $\theta$ sebanyak:
$$ \Delta_{\text{params}} = 2 \times N \qquad (18) $$

Peningkatan kedalaman ini secara matematis memperluas jangkauan *ansatz* di dalam ruang Hilbert, yang memungkinkannya untuk merepresentasikan keadaan yang lebih mendekati *ground state* sejati. Namun, mahasiswa harus menyadari adanya hukum *diminishing returns*: semakin dalam sirkuit, semakin besar akumulasi galat gerbang (*gate errors*) dan dekoherensi qubit. Oleh karena itu, mekanisme *adaptive depth* dalam kode `run_vqe_adaptive` dirancang untuk menghentikan penambahan lapisan segera setelah penurunan energi ($\Delta E$) berada di bawah ambang batas toleransi tertentu, guna menjaga efisiensi sumber daya kuantum.

## 4. Mekanisme Optimasi: SPSA (Simultaneous Perturbation Stochastic Approximation)

Optimasi parameter $\theta$ dalam VQE menghadapi tantangan besar karena adanya *noise* pada pengukuran energi. Metode berbasis gradien klasik seperti *Finite Difference* memerlukan $2 \times p$ pengukuran (di mana $p$ adalah jumlah parameter) hanya untuk satu langkah gradien. Untuk sistem dengan banyak aset, biaya komputasi ini menjadi sangat mahal. *Simultaneous Perturbation Stochastic Approximation* (SPSA) mengatasi masalah ini dengan hanya membutuhkan dua pengukuran per iterasi, terlepas dari berapa pun jumlah parameternya.

Mekanisme SPSA bekerja dengan melakukan perturbasi pada seluruh parameter secara simultan ke arah acak. Misalkan $\theta_k$ adalah vektor parameter pada iterasi $k$, dan $\Delta_k$ adalah vektor perturbasi acak (distribusi Bernoulli $\pm 1$). Gradien diestimasi melalui dua pengukuran energi $y_k^{(+)}$ dan $y_k^{(-)}$ sebagai berikut:

$$ y_k^{(+)} = \langle E(\theta_k + c_k \Delta_k) \rangle + \epsilon_k^{(+)} \qquad (10) $$
$$ y_k^{(-)} = \langle E(\theta_k - c_k \Delta_k) \rangle + \epsilon_k^{(-)} \qquad (11) $$

Di mana $c_k$ adalah parameter langkah perturbasi dan $\epsilon_k$ adalah *noise* pengukuran. Untuk membuktikan validitas estimasi gradien, kita lakukan ekspansi Taylor orde-dua terhadap fungsi energi $L(\theta) = \langle E(\theta) \rangle$ di sekitar titik $\theta_k$.

**Langkah 1: Ekspansi Taylor Orde-Dua**
Ekspansi untuk pengukuran positif ($y_k^{(+)}$):
$$ L(\theta_k + c_k \Delta_k) = L(\theta_k) + c_k \Delta_k^T \nabla L(\theta_k) + \frac{1}{2} c_k^2 \Delta_k^T \nabla^2 L(\theta_k) \Delta_k + O(c_k^3) \qquad (12) $$
Ekspansi untuk pengukuran negatif ($y_k^{(-)}$):
$$ L(\theta_k - c_k \Delta_k) = L(\theta_k) - c_k \Delta_k^T \nabla L(\theta_k) + \frac{1}{2} c_k^2 \Delta_k^T \nabla^2 L(\theta_k) \Delta_k - O(c_k^3) \qquad (13) $$

**Langkah 2: Proses Pengurangan**
Jika kita mengurangkan persamaan (12) dengan persamaan (13), maka suku orde-nol ($L(\theta_k)$) dan suku orde-dua (Hessian) yang mengandung $c_k^2$ akan saling meniadakan:
$$ L(\theta_k + c_k \Delta_k) - L(\theta_k - c_k \Delta_k) = [c_k \Delta_k^T \nabla L(\theta_k) - (-c_k \Delta_k^T \nabla L(\theta_k))] + [O(c_k^3) - (-O(c_k^3))] \qquad (14) $$
$$ y_k^{(+)} - y_k^{(-)} = 2 c_k \Delta_k^T \nabla L(\theta_k) + O(c_k^3) \qquad (15) $$

Perhatikan bahwa $\Delta_k^T \nabla L(\theta_k)$ adalah hasil kali titik (*dot product*) yang dapat dituliskan sebagai jumlahan komponen: $\sum_{j=1}^p \Delta_{kj} g_j(\theta_k)$, di mana $g_j$ adalah komponen gradien sejati ke-$j$.

**Langkah 3: Proses Pembagian dan Aproksimasi**
Untuk mendapatkan estimasi komponen gradien ke-$i$ ($\hat{g}_{ki}$), kita bagi hasil pengurangan tersebut dengan $2 c_k \Delta_{ki}$:
$$ \hat{g}_{ki}(\theta_k) = \frac{y_k^{(+)} - y_k^{(-)}}{2 c_k \Delta_{ki}} = \frac{2 c_k \sum_{j=1}^p \Delta_{kj} g_j(\theta_k) + O(c_k^3)}{2 c_k \Delta_{ki}} \qquad (16) $$
$$ \hat{g}_{ki}(\theta_k) = \frac{\Delta_{ki} g_i(\theta_k) + \sum_{j \neq i} \Delta_{kj} g_j(\theta_k)}{\Delta_{ki}} + O(c_k^2) \qquad (17) $$
$$ \hat{g}_{ki}(\theta_k) = g_i(\theta_k) + \sum_{j \neq i} \frac{\Delta_{kj}}{\Delta_{ki}} g_j(\theta_k) + O(c_k^2) \qquad (18) $$

Karena $\Delta_{kj}$ dipilih secara acak dari distribusi Bernoulli $\pm 1$ dan bersifat independen satu sama lain, maka nilai ekspektasi dari suku jumlahan di atas adalah nol, $E[\Delta_{kj}/\Delta_{ki}] = 0$ untuk $j \neq i$. Hal ini membuktikan bahwa $\hat{g}_{ki}$ adalah estimasi tak bias (*unbiased estimate*) dari gradien sejati $g_i$ di tengah *noise*. Parameter $\theta$ kemudian diperbarui dengan aturan:

$$ \theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k) \qquad (19) $$

Di mana $a_k$ adalah *learning rate* yang disesuaikan untuk memastikan konvergensi menuju minimum global di tengah fluktuasi data.

## 5. Akselerasi Konvergensi: Nash Equilibrium Warm-Start

Salah satu hambatan utama dalam VQE adalah fenomena *Barren Plateaus*, di mana lanskap energi menjadi sangat datar sehingga gradien sulit ditemukan. Untuk memitigasi hal ini, algoritma *Ising-SBR* menggunakan strategi *Warm-Start* berbasis *Nash Equilibrium* (NE). Strategi ini mengasumsikan bahwa solusi optimal klasik yang ditemukan melalui *Sequential Best Response* (SBR) berada dalam lingkungan yang cukup dekat dengan *ground state* kuantum. Dengan memulai pencarian parameter di area yang sudah "hangat", algoritma dapat menghindari jebakan minimum lokal dan mempercepat waktu konvergensi.

Secara teknis, hasil dari pencarian NE berupa bitstring biner $x_{NE} \in \{0, 1\}^N$ digunakan untuk menginduksi parameter awal $\theta_0$. Dalam sirkuit RY-RZ, jika aset $i$ terpilih dalam bitstring ($x_i = 1$), maka parameter rotasi gate $RY$ pada qubit $i$ diinisialisasi mendekati nilai $\pi$ untuk membalikkan state $|0\rangle$ menjadi $|1\rangle$. Sebaliknya, jika aset tidak terpilih ($x_i = 0$), parameter diinisialisasi mendekati 0. Inisialisasi ini memberikan bias struktural awal pada sirkuit kuantum yang selaras dengan insentif ekonomi klasik, sehingga lintasan optimasi parameter di ruang Hilbert menjadi lebih efisien dan terarah.

## 6. Analisis Implementasi dan Interpretasi Data

Implementasi VQE dalam proyek ini direalisasikan melalui fungsi utama `run_vqe_adaptive` yang mengintegrasikan seluruh komponen di atas. Mahasiswa dapat melihat dalam kode bahwa fungsi ini melakukan iterasi melalui berbagai tingkat kedalaman sirkuit (*max_depth*). Pada setiap kedalaman, optimisator SPSA dijalankan melalui fungsi `run_spsa` dengan parameter seperti *batch_size* dan *convergence window* untuk memastikan stabilitas hasil di tengah *noise* simulasi. Penanganan bitstring hasil pengukuran dilakukan secara probabilistik, di mana solusi akhir dipilih berdasarkan probabilitas tertinggi dari state yang memenuhi kendala kardinalitas $K$.

Untuk mengevaluasi performa algoritma, mahasiswa wajib menganalisis dua grafik utama: *Energy Convergence* dan *Energy vs Depth*. Grafik konvergensi energi menunjukkan bagaimana SPSA secara perlahan menurunkan biaya (energi) sistem hingga mencapai dataran stabil (*steady state*). Sementara itu, grafik *Energy vs Depth* memberikan pemahaman tentang hukum *diminishing returns* dalam komputasi kuantum; penambahan kedalaman sirkuit mungkin menurunkan energi, namun setelah titik tertentu, kompleksitas ekstra tersebut tidak lagi memberikan penurunan energi yang signifikan dibandingkan dengan penambahan galat yang mungkin muncul. Analisis kritis terhadap grafik-grafik ini adalah kunci untuk menentukan apakah portofolio yang terpilih benar-benar merupakan representasi dari efisiensi pasar yang diharapkan.
