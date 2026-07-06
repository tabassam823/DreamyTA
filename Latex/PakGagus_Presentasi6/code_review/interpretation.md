# Interpretasi Hasil Simulasi Quantum Principal Component Analysis (qPCA)

Dokumen ini menyajikan analisis mendalam terhadap hasil *running* kode simulasi kuantum untuk reduksi dimensi matriks kovarians dalam kerangka model *Heath-Jarrow-Morton* (HJM). Interpretasi difokuskan pada fidelitas estimasi *eigenvalue* dan karakteristik *eigenvector* yang dihasilkan oleh sirkuit kuantum.

## 1. Quantum Phase Estimation (QPhE)

### 1.1. Arsitektur Sirkuit dan Dekomposisi Uniter
Sirkuit yang direpresentasikan dalam `circuit_qphe.png` mengimplementasikan algoritma *Quantum Phase Estimation* (QPE) dengan register fase $n=3$ qubit dan satu qubit register *state*. Implementasi ini menggunakan gerbang *Controlled-Unitary* ($CU$) yang dikonfigurasi secara spesifik untuk menyandikan matriks kovarians $\rho_2$ melalui parameter sudut $(\theta, \phi, \lambda)$ yang presisi. Transformasi *Walsh-Hadamard* pada register fase menciptakan superposisi *uniform*, memungkinkan ekstraksi fase *eigenvalue* secara paralel melalui mekanisme *phase kickback*.

![[circuit_qphe.png]]
![[circuit_transpiled_qphe.png]]

Pada file `circuit_transpiled_qphe.png`, terlihat dekomposisi gerbang tingkat tinggi menjadi gerbang basis *hardware* seperti gerbang $U3$ dan $CX$. Proses *transpilation* ini krusial untuk memahami *depth* sirkuit yang sebenarnya sebelum dieksekusi pada prosesor riil. Struktur sekuensial gerbang $CU$ yang disusun secara biner (pangkat $2^j$) memastikan bahwa setiap qubit dalam register fase menangkap resolusi fase yang berbeda, mulai dari *most significant bit* hingga resolusi terkecil.

### 1.2. Distribusi Spektral dan Estimasi Eigenvalue Utama
Hasil simulasi pada `qpca_qphe_result.png` menunjukkan histogram probabilitas dari pengukuran register fase setelah penerapan *Inverse Quantum Fourier Transform* (IQFT). Terdapat puncak dominan pada *state* biner $|111\rangle$, yang jika dikonversi ke nilai desimal memberikan estimasi $\Lambda \approx 0.875$. Nilai ini berkorelasi kuat dengan *eigenvalue* dominan $\lambda_1 = 0.8576$ yang ditemukan dalam analisis klasik, menunjukkan keberhasilan algoritma dalam mengidentifikasi komponen utama volatilitas.

![[qpca_qphe_result.png]]

Kehadiran amplitudo pada *state* biner selain puncak utama menunjukkan adanya fenomena *spectral leakage*. Hal ini terjadi karena fase *eigenvalue* yang sebenarnya tidak tepat merupakan kelipatan dari $1/2^n$, di mana $n=3$ dalam kasus ini. Selain itu, efek *noise* pada *qasm_simulator* atau galat statistik dari 8192 *shots* turut berkontribusi pada distribusi probabilitas yang lebih lebar, meskipun puncak interferensi konstruktif tetap terdefinisi dengan jelas.

### 1.3. Analisis Tomografi State dan Orientasi Qubit
Visualisasi `state_city_qphe.png` dan `hinton_qphe.png` memberikan representasi matriks densitas sistem sebelum dilakukan pengukuran akhir. Elemen riil dan imajiner pada *state city* menunjukkan kemurnian *state* yang tinggi, mengonfirmasi bahwa interferensi kuantum terjadi sesuai dengan prediksi teoretis tanpa dekoherensi prematur. Distribusi amplitudo pada peta Hinton mengilustrasikan korelasi antara register fase dan register target yang merupakan karakteristik utama dari *entangled state* dalam protokol qPCA.

![[state_city_qphe.png]]
![[hinton_qphe.png]]
![[bloch_qphe.png]]

Pada `bloch_qphe.png`, setiap qubit divisualisasikan dalam bola Bloch untuk menunjukkan orientasi *statevector* masing-masing. Qubit register fase cenderung menunjuk ke arah ekuator sebelum IQFT dan berotasi menuju kutub $|0\rangle$ atau $|1\rangle$ setelah interferensi selesai secara sempurna. Visualisasi ini memverifikasi bahwa rotasi fase yang diinduksi oleh gerbang $CU$ telah berhasil dipetakan ke dalam derajat kebebasan qubit dengan presisi fasa yang memadai untuk aplikasi finansial.

## 2. Validation with Pure Eigenstates

### 2.1. Konvergensi Fase pada Register 2-Bit
Sirkuit dalam `circuit_eigenstate.png` berfungsi sebagai protokol validasi menggunakan register fase yang lebih sederhana yaitu 2-bit. Penggunaan *eigenstate* murni $|+\rangle$ sebagai input register target bertujuan untuk mengisolasi efek dekomposisi uniter dari kompleksitas *state* inisial. Dengan membatasi register fase pada $n=2$, sirkuit ini meminimalkan *gate error* akumulatif, memberikan gambaran yang lebih murni mengenai mekanisme *interferensi* internal algoritma.

![[circuit_eigenstate.png]]

Konvergensi fase pada konfigurasi ini terlihat lebih tajam dibandingkan dengan kasus 3-bit. Hal ini disebabkan oleh pengurangan jumlah gerbang *entangling* yang diperlukan untuk melakukan operasi terkontrol. Melalui pendekatan deduktif, stabilitas hasil pada register 2-bit ini menjadi fondasi untuk memvalidasi parameter rotasi $(\theta, \phi, \lambda)$ sebelum diterapkan pada sistem multivariat yang lebih luas dalam model HJM.

### 2.2. Interferensi Konstruktif dan Probabilitas Hasil
Histogram pada `qpca_eigenstate_result.png` menunjukkan puncak probabilitas yang sangat terfokus pada *state* biner tertentu. Ketajaman puncak ini mengindikasikan bahwa fase yang diinduksi oleh operator uniter sangat mendekati nilai diskret yang dapat direpresentasikan oleh register 2-bit. Rendahnya probabilitas pada *state* non-target membuktikan bahwa interferensi destruktif bekerja secara efektif dalam menekan amplitudo fase parasit.

![[qpca_eigenstate_result.png]]

Rasio *signal-to-noise* yang tinggi pada hasil ini memberikan tingkat kepercayaan (*confidence level*) yang besar terhadap implementasi gerbang uniter. Dalam konteks ekonomi fisik, keberhasilan ini berarti profil volatilitas yang disandikan ke dalam operator uniter dapat diekstraksi kembali dengan galat biner yang minimal. Hasil ini mengonfirmasi bahwa algoritma qPCA mampu mempertahankan integritas informasi spektral pada matriks kovarians berukuran kecil.

### 2.3. Visualisasi Multivektor pada Bola Bloch
Representasi `bloch_eigenstate.png` memberikan gambaran geometris dari *state* kuantum selama proses validasi. Vektor Bloch pada register fase menunjukkan orientasi yang konsisten dengan fasa yang diharapkan, memverifikasi ketiadaan rotasi liar yang seringkali muncul akibat *crosstalk* antar qubit. Koherensi sistem terlihat terjaga, yang ditunjukkan oleh panjang vektor Bloch yang mendekati satu (jari-jari bola unit).

![[bloch_eigenstate.png]]
![[state_city_eigenstate.png]]
![[hinton_eigenstate.png]]

Integrasi visual melalui `state_city_eigenstate.png` semakin memperkuat bukti kemurnian *state*. Tidak adanya komponen *off-diagonal* yang signifikan pada bagian imajiner menunjukkan bahwa korelasi fasa yang terbentuk bersifat stabil dan terikat erat pada register fase. Analisis visual ini secara kolektif membuktikan bahwa sirkuit validasi telah mencapai target performa yang diperlukan untuk melanjutkan ke kasus numerik $4 \times 4$.

## 3. Scalability Analysis: 4x4 Covariance Matrix

### 3.1. Kompleksitas Sirkuit dan Circuit Depth
Analisis terhadap `circuit_4x4.png` menunjukkan peningkatan kompleksitas yang signifikan dengan total 28 operasi gerbang sebelum pengukuran. Peningkatan jumlah gerbang *Controlled-Unitary* dan *CNOT* secara drastis menambah *circuit depth*, sebagaimana dikonfirmasi oleh visualisasi `circuit_transpiled_4x4.png`. Dalam era *Noisy Intermediate-Scale Quantum* (NISQ), kedalaman sirkuit ini menjadi faktor pembatas utama karena akumulasi galat pada setiap gerbang dua-qubit.

![[circuit_4x4.png]]
![[circuit_transpiled_4x4.png]]

Struktur sirkuit $4 \times 4$ memerlukan koordinasi fase yang jauh lebih rumit antar register target 2-qubit ($q_1, q_2$) dan register fase ($q_0$). Setiap gerbang uniter sekuensial harus secara kolektif membangun operator evolusi total yang menyandikan korelasi silang antar tiga tenor maturitas. Kompleksitas ini mencerminkan tantangan nyata dalam memetakan model finansial multifaktor ke dalam arsitektur kuantum kontemporer.

### 3.2. Akumulasi Galat pada Era NISQ
Histogram `qpca_4x4_result.png` menyajikan konsekuensi dari akumulasi galat sistemik tersebut. Berbeda dengan kasus $2 \times 2$, distribusi probabilitas di sini terlihat lebih homogen (mendekati distribusi *uniform*), yang mengindikasikan terjadinya dekoherensi yang signifikan. Penurunan kontras antara puncak utama dan *background noise* menunjukkan bahwa informasi fase mulai "terhapus" oleh akumulasi galat gerbang yang mencapai estimasi lebih dari 100%.

![[qpca_4x4_result.png]]

Meskipun puncak teoretis mungkin masih dapat diidentifikasi melalui teknik *post-processing*, hasil mentah ini menunjukkan keterbatasan *hardware* IBMQX2 dalam menangani sirkuit dengan kedalaman tinggi. Analisis induktif dari hasil ini menunjukkan perlunya penerapan metodologi *error mitigation* seperti *Richardson’s extrapolation* untuk mengekstraksi informasi yang bermakna dari data yang terdegradasi oleh noise simulator atau hardware riil.

### 3.3. Rekonstruksi Tomografi dan Tantangan Fidelitas
Visualisasi `state_city_4x4.png` mengungkapkan degradasi fidelitas melalui penyebaran amplitudo pada elemen-elemen matriks densitas yang seharusnya nol. Peta `hinton_4x4.png` menunjukkan pola korelasi yang mulai kabur, mencerminkan hilangnya ketajaman *eigenvector* utama $|u_{max}\rangle$ dalam basis komputasi. Fenomena ini membuktikan bahwa skalabilitas algoritma qPCA sangat bergantung pada kemampuan sistem dalam mempertahankan koherensi fasa selama operasi uniter yang panjang.

![[state_city_4x4.png]]
![[hinton_4x4.png]]
![[bloch_4x4.png]]

Tantangan fidelitas ini memberikan wawasan kritis bahwa untuk matriks kovarians berdimensi lebih tinggi, diperlukan qubit dengan tingkat *fidelity* gerbang dua-qubit yang jauh lebih tinggi. Rekonstruksi tomografi ini menjadi bukti empiris bahwa meskipun secara algoritmis qPCA bersifat universal, implementasi praktisnya pada model instrumen keuangan memerlukan optimasi gerbang dasar. Hasil ini menutup analisis dengan menegaskan urgensi pengembangan teknik mitigasi galat untuk menjamin akurasi *pricing* derivatif keuangan di masa depan.
