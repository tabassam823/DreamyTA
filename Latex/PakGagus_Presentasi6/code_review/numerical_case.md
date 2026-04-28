# Kasus Numerik: Implementasi qPCA pada Qiskit

Dokumen ini merinci langkah-langkah numerik dan algoritma yang diimplementasikan dalam kode Python untuk melakukan *Quantum Principal Component Analysis* (qPCA) pada model instrumen keuangan.

# 1. QPhE (Quantum Phase Estimation)
Implementasi pada file `QPCA_QPhE.py` merealisasikan ekstraksi spektral dari operator uniter $U$ yang menyandikan profil volatilitas dalam model *Heath-Jarrow-Morton* (HJM). Algoritma ini memetakan fase uniter ke dalam register biner untuk mengestimasi eigenvalue utama.

### Formalisme Numerik:
1.  **Inisialisasi Register dan State Target:**
    Sistem menggunakan register eigenvalue $n=3$ ($q_0, q_1, q_2$) dan satu register state ($q_3$). Qubit target $| \psi \rangle$ disiapkan dalam superposisi non-trivial untuk menyandikan *eigenvector* awal berdasarkan data historis:
    $$ | \psi_{target} \rangle = \begin{pmatrix} c_0 \\ c_1 \end{pmatrix} = \begin{pmatrix} \cos(0.4996) e^{-i0.1144} \\ \sin(0.4996) e^{i(0.3252 - 0.1144)} \end{pmatrix} \approx \begin{pmatrix} 0.872 - 0.100i \\ 0.468 + 0.100i \end{pmatrix} $$

2.  **Transformasi Walsh-Hadamard dan Konstruksi $|\Phi_0\rangle$:**
    Sebelum interaksi uniter, register fase diinisialisasi ke dalam state superposisi uniform melalui operator $H^{\otimes 3}$. Proses ini secara matematis diuraikan sebagai berikut:
    
    Aksi operator $H$ pada qubit tunggal $|0\rangle$:
    $$ H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) $$
    
    Untuk register 3-qubit ($q_0, q_1, q_2$), transformasi menghasilkan:
    $$ H^{\otimes 3}|000\rangle = \left[ \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \right] \otimes \left[ \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \right] \otimes \left[ \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \right] $$
    $$ H^{\otimes 3}|000\rangle = \frac{1}{\sqrt{8}} \sum_{k=0}^{7} |k\rangle = \frac{1}{\sqrt{8}} \left( |000\rangle + |001\rangle + \dots + |111\rangle \right) $$
    
    State total $|\Phi_0\rangle$ dibentuk melalui *tensor product* antara register fase dan register state $| \psi_{target} \rangle$:
    $$ |\Phi_0\rangle = (H^{\otimes 3} |000\rangle) \otimes |\psi_{target}\rangle $$
    $$ |\Phi_0\rangle = \frac{1}{\sqrt{8}} \sum_{k=0}^{7} |k\rangle \otimes \begin{pmatrix} c_0 \\ c_1 \end{pmatrix} $$
    
    Dengan mensubstitusi nilai numerik $| \psi_{target} \rangle$ yang telah diketahui, kita mendapatkan distribusi amplitudo awal:
    $$ |\Phi_0\rangle \approx \frac{1}{\sqrt{8}} \sum_{k=0}^{7} |k\rangle \otimes \left( (0.872 - 0.100i)|0\rangle + (0.468 + 0.100i)|1\rangle \right) $$
    $$ |\Phi_0\rangle \approx \sum_{k=0}^{7} \left( \frac{0.872 - 0.100i}{\sqrt{8}}|k,0\rangle + \frac{0.468 + 0.100i}{\sqrt{8}}|k,1\rangle \right) $$
    State ini memastikan bahwa setiap basis komputasi pada register fase memiliki probabilitas yang sama untuk berinteraksi dengan komponen eigenvector melalui gerbang *Controlled-Unitary*.

3.  **Interaksi Controlled-Unitary (CU) dan Phase Kickback:**
    Inti dari algoritma QPE adalah pemetaan fase eigenvalue ke dalam amplitudo register fase melalui efek *phase kickback*. Operator uniter $U$ yang merepresentasikan matriks densitas $\rho$ diterapkan dalam berbagai pangkat $2^j$ pada register fase. 
    
    Dalam kode `QPCA_QPhE.py`, operator $U^{2^j}$ diimplementasikan menggunakan gerbang `cu(theta, phi, lambda, gamma)` dengan parameter numerik sebagai berikut:
    - **$U^{2^0}$ (pada $q_2$):** $\theta_0=1.59899, \phi_0=-1.11512, \lambda_0=2.02647$
    - **$U^{2^1}$ (pada $q_1$):** $\theta_1=2.22862, \phi_1=0.513123, \lambda_1=3.65472$
    - **$U^{2^2}$ (pada $q_0$):** $\theta_2=0.797922, \phi_2=-4.53103, \lambda_2=-1.38944$
    
    Setiap gerbang ini membentuk matriks uniter $U_j$ yang memenuhi:
    $$ U_j = \begin{pmatrix} \cos(\theta_j/2) & -e^{i\lambda_j}\sin(\theta_j/2) \\ e^{i\phi_j}\sin(\theta_j/2) & e^{i(\phi_j+\lambda_j)}\cos(\theta_j/2) \end{pmatrix} $$
    
    Ketika gerbang terkontrol $CU^{2^j}$ diterapkan pada qubit register fase ke-$j$, ia memberikan kontribusi fase $e^{2\pi i 2^j \phi}$ kepada komponen $|1\rangle$ pada qubit tersebut:
    $$ CU^{2^j} \left( \frac{|0\rangle + |1\rangle}{\sqrt{2}} \right) \otimes |\psi\rangle = \frac{|0\rangle + e^{2\pi i 2^j \phi}|1\rangle}{\sqrt{2}} \otimes |\psi\rangle $$
    
    Hasil akhir dari aplikasi sekuensial ketiga gerbang tersebut adalah state terikat (*entangled state*) di mana informasi fase eigenvalue $\lambda$ telah terakumulasi secara biner pada register fase:
    $$ |\Phi_1\rangle = \frac{1}{\sqrt{8}} \sum_{k=0}^{7} e^{2\pi i k \phi} |k\rangle \otimes |\psi_{target}\rangle $$
    Di mana fase total $\phi$ ditentukan oleh parameter sudut $(\theta_j, \phi_j, \lambda_j)$ yang secara kolektif menyandikan struktur spektral matriks kovarians $\rho$.

4.  **Inverse Quantum Fourier Transform (IQFT) dan Interferensi:**
    Untuk mengekstraksi nilai $\phi$ dari domain fase ke domain basis komputasi $|y\rangle$, diterapkan operator $\mathcal{QFT}^\dagger$. Operator ini didefinisikan sebagai:
    $$ \mathcal{QFT}^\dagger |k\rangle = \frac{1}{\sqrt{8}} \sum_{y=0}^{7} e^{-2\pi i ky / 8} |y\rangle $$
    
    Menerapkan $\mathcal{QFT}^\dagger$ pada register fase di $|\Phi_1\rangle$ menghasilkan state akhir sistem sebelum pengukuran:
    $$ |\Phi_{final}\rangle = \left( \mathcal{QFT}^\dagger \otimes I \right) |\Phi_1\rangle = \frac{1}{8} \sum_{y=0}^{7} \sum_{k=0}^{7} e^{2\pi i k (\phi - y/8)} |y\rangle \otimes |\psi_{target}\rangle $$
    
    Pada tahap ini, terjadi mekanisme interferensi kuantum:
    - **Interferensi Konstruktif:** Jika $\phi = y/8$ untuk suatu bilangan bulat $y$, maka eksponen menjadi $e^0 = 1$. Jumlahan $\sum_{k=0}^{7} 1 = 8$, sehingga amplitudo untuk state $|y\rangle$ menjadi $8/8 = 1$.
    - **Interferensi Destruktif:** Untuk nilai $y$ lainnya, amplitudo akan saling meniadakan (interferensi destruktif), sehingga probabilitas menemukan sistem pada state tersebut mendekati nol.
    
    Dengan demikian, pengukuran pada register fase akan menghasilkan nilai biner $y$ yang merepresentasikan estimasi fase $\phi \approx y/2^n$.

5.  **Ekstraksi Hasil:**
    Eksperimen dijalankan dengan $N=8192$ *shots* pada `qasm_simulator`. Histogram probabilitas memberikan nilai estimasi $\lambda_{max}$ melalui interpretasi biner dari state yang paling sering terukur.

# 2. Eigenstate
Implementasi pada `QPCA_eigenstate.py` berfungsi sebagai protokol validasi untuk menguji konvergensi algoritma menggunakan *eigenstate* yang disederhanakan. Fokus utama di sini adalah pengujian fidelitas dekomposisi uniter pada register fase 2-bit.

### Formalisme Numerik:
1.  **Inisialisasi Register dan State Target:**
    Sistem menggunakan register fase $n=2$ ($q_0, q_1$) dan satu qubit state ($q_2$). Qubit target $| \psi \rangle$ disiapkan dalam state $| + \rangle$:
    $$ | \psi \rangle = | + \rangle = \frac{1}{\sqrt{2}}(| 0 \rangle + | 1 \rangle) = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix} $$

2.  **Konstruksi $|\Phi_0\rangle$ melalui Walsh-Hadamard:**
    Register fase diinisialisasi ke dalam superposisi uniform menggunakan $H^{\otimes 2}$:
    $$ H^{\otimes 2}|00\rangle = \frac{1}{2}(|00\rangle + |01\rangle + |10\rangle + |11\rangle) $$
    
    State total $|\Phi_0\rangle$ dibentuk melalui *tensor product*:
    $$ |\Phi_0\rangle = \frac{1}{2} \sum_{k=0}^{3} |k\rangle \otimes \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{\sqrt{8}} \sum_{k=0}^{3} (|k,0\rangle + |k,1\rangle) $$

3.  **Interaksi Controlled-Unitary (CU) dan Parameter Sudut:**
    Operator evolusi $U^{2^j}$ diterapkan pada register fase 2-bit dengan parameter sebagai berikut:
    - **$U^{2^0}$ (pada $q_1$):** $\theta_0=1.59899, \phi_0=-1.11512, \lambda_0=2.02647$
    - **$U^{2^1}$ (pada $q_0$):** $\theta_1=2.22862, \phi_1=0.513123, \lambda_1=3.65472$
    
    Melalui mekanisme *phase kickback*, koefisien fase qubit register fase berubah sesuai dengan eigenvalue dari operator uniter $U_j$:
    $$ |\Phi_1\rangle = \frac{1}{2} \bigotimes_{j=0}^{1} (|0\rangle + e^{2\pi i 2^j \phi}|1\rangle) \otimes |+\rangle = \frac{1}{2} \sum_{k=0}^{3} e^{2\pi i k \phi} |k\rangle \otimes |+\rangle $$

4.  **IQFT 2-bit dan Mekanisme Interferensi:**
    Untuk mengonversi fase ke dalam basis komputasi, diterapkan $\mathcal{QFT}^\dagger$ 2-bit:
    $$ \mathcal{QFT}^\dagger |k\rangle = \frac{1}{2} \sum_{y=0}^{3} e^{-2\pi i ky / 4} |y\rangle $$
    
    State sistem sebelum pengukuran menjadi:
    $$ |\Phi_{final}\rangle = \frac{1}{4} \sum_{y=0}^{3} \sum_{k=0}^{3} e^{2\pi i k (\phi - y/4)} |y\rangle \otimes |+\rangle $$
    
    Terjadi interferensi pada amplitudo probabilitas:
    - **Puncak Probabilitas:** Muncul pada state $|y\rangle$ di mana $y/4$ paling dekat dengan nilai fase $\phi$. Pada titik ini, suku-suku dalam jumlahan berinterferensi secara konstruktif.
    - **Supresi Probabilitas:** State lainnya mengalami interferensi destruktif, sehingga probabilitas pengukurannya ditekan secara signifikan.

5.  **Analisis Tomografi Statevector:**
    Sebelum pengukuran biner, simulasi mengekstraksi matriks densitas $\rho$ untuk menghasilkan:
    - **State City:** Menunjukkan komponen riil dan imajiner dari $\rho$, memverifikasi kemurnian state $| \Phi_{final} \rangle$.
    - **Bloch Multivector:** Memvisualisasikan orientasi setiap qubit; qubit register fase diharapkan menunjuk ke kutub atau ekuator tertentu sesuai dengan nilai fase yang terukur.

# 3. 4x4 Eigenstate
Implementasi pada `QPCA_4x4eigenstate.py` merupakan representasi dari ekspansi sistem ke matriks kovarians $4 \times 4$ ($\rho_4$). Tahap ini mensimulasikan tantangan pada era NISQ terkait *circuit depth* dan akumulasi galat pada sistem multivariat.

### Formalisme Numerik:
1.  **Inisialisasi Register dan State Target $| \psi_4 \rangle$:**
    Sistem menggunakan register fase $n=1$ ($q_0$) dan register target 2-qubit ($q_1, q_2$). State target disiapkan menggunakan data *counts* dari iterasi eksperimental sebelumnya ($N_{total} = 5456$):
    $$ | \psi_4 \rangle = \begin{pmatrix} c_{00} \\ c_{01} \\ c_{10} \\ c_{11} \end{pmatrix} = \frac{1}{\sqrt{5456}} \begin{pmatrix} \sqrt{3087} \\ \sqrt{906} \\ \sqrt{1405} \\ \sqrt{58} \end{pmatrix} \approx \begin{pmatrix} 0.752 \\ 0.407 \\ 0.507 \\ 0.103 \end{pmatrix} $$
    Vektor ini merepresentasikan estimasi *eigenvector* utama dalam basis komputasi $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$.

2.  **Konstruksi $|\Phi_0\rangle$ melalui Walsh-Hadamard:**
    Register fase diinisialisasi menggunakan gerbang Hadamard tunggal pada $q_0$ untuk menciptakan superposisi biner yang akan menampung informasi eigenvalue:
    $$ |\Phi_0\rangle = H_{q_0} |0\rangle \otimes |\psi_4\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \otimes |\psi_4\rangle $$
    Pada tahap ini, qubit $q_0$ berada dalam state $|+\rangle$, siap untuk menerima *phase kickback* dari interaksi dengan register target $| \psi_4 \rangle$.

3.  **Dekomposisi Sekuensial Operasi $U_{\rho_4}$:**
    Mengingat kompleksitas sistem $4 \times 4$, operasi didekomposisi menjadi beberapa blok sekuensial. Berikut adalah perincian matematis untuk dua sekuensial pertama:

    **Sekuensial I: Pre-kondisi Register Target ($q_1, q_2$)**
    Langkah ini mempersiapkan korelasi internal pada register target sebelum coupling dengan register fase.
    - **Operasi Fase $P(\pi/4)$ pada $q_1$:**
      $$ P(0.785) = \begin{pmatrix} 1 & 0 \\ 0 & e^{i0.785} \end{pmatrix} \approx \begin{pmatrix} 1 & 0 \\ 0 & 0.707 + i0.707 \end{pmatrix} $$
    - **Gerbang Terkontrol $CU$ (Langkah 1b):** Menerapkan rotasi uniter antara $q_1$ (kontrol) dan $q_2$ (target) dengan parameter $\theta=1.1747, \phi=-2.83038, \lambda=3.83087$:
      $$ U_{1b} = \begin{pmatrix} \cos(0.587) & -e^{i3.831}\sin(0.587) \\ e^{-i2.830}\sin(0.587) & e^{i(1.001)}\cos(0.587) \end{pmatrix} \approx \begin{pmatrix} 0.832 & 0.425 + i0.357 \\ -0.528 + i0.170 & 0.449 + i0.700 \end{pmatrix} $$

    **Sekuensial II: Inisiasi Coupling dan Phase Adjustment**
    Langkah ini mulai mengaitkan informasi dari register target ke register fase $q_0$.
    - **Gerbang $CX(q_0, q_1)$:** Menciptakan *entanglement* antara register fase dan target:
      $$ CX = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X $$
    - **Koreksi Fase $P(-\pi/4)$ pada $q_1$:** Mengimbangi rotasi fase sebelumnya:
      $$ P(-0.785) = \begin{pmatrix} 1 & 0 \\ 0 & 0.707 - i0.707 \end{pmatrix} $$
    - **Gerbang Terkontrol $CU$ (Langkah 2c):** Menerapkan uniter terkontrol dengan parameter $\theta=1.1747, \phi=-0.689273, \lambda=-0.31121$:
      $$ U_{2c} = \begin{pmatrix} 0.832 & 0.527 + i0.170 \\ 0.427 - i0.352 & 0.643 - i0.528 \end{pmatrix} $$

    **Sekuensial III - Akhir: Iterasi Penguatan Fase (20 Operasi Sisa)**
    Sisa operasi (terdiri dari 10x $CU$, 5x $P$, dan 4x $CX$) mengikuti pola matematis yang serupa dengan dua sekuensial pertama, namun dengan parameter sudut yang bervariasi untuk melakukan *refinement* pada fase eigenvalue. Proses ini mencakup:
    - **Ekstraksi Hubungan Antar Maturitas:** Penggunaan parameter sudut seperti $1.07126$ dan $2.3749$ ditujukan untuk menyelaraskan fase yang berasal dari korelasi silang tenor 1, 3, dan 6 bulan.
    - **Stabilisasi State:** Gerbang $CX$ dan $P$ di sela-sela $CU$ berfungsi untuk memitigasi akumulasi fase parasit (*stray phases*) sebelum memasuki tahap IQFT.
    Secara kolektif, 25 operasi inti ini membangun operator evolusi total $\mathcal{U} = \prod U_i$ yang memetakan eigenvalue utama matriks $\rho_4$ ke register fase $q_0$.

4.  **IQFT 1-bit dan Interferensi:**
    Karena register fase hanya menggunakan 1 qubit, transformasi balik dilakukan dengan gerbang Hadamard pada $q_0$:
    $$ |\Phi_{final}\rangle = (H \otimes I \otimes I) \left[ \frac{1}{\sqrt{2}} (|0\rangle + e^{2\pi i \phi}|1\rangle) \otimes |\psi_4\rangle \right] $$
    $$ |\Phi_{final}\rangle = \frac{1}{2} \left[ (1 + e^{2\pi i \phi})|0\rangle + (1 - e^{2\pi i \phi})|1\rangle \right] \otimes |\psi_4\rangle $$
    
    Mekanisme interferensi menentukan hasil pengukuran:
    - **Fase $\phi \approx 0$:** Amplitudo untuk state $|0\rangle$ berinterferensi secara konstruktif ($1+1=2$), sementara $|1\rangle$ destruktif ($1-1=0$).
    - **Fase $\phi \approx 0.5$:** State $|1\rangle$ menjadi konstruktif ($1 - (-1) = 2$), menunjukkan eigenvalue yang signifikan.

5.  **Output dan Visualisasi:**
    - **Histogram QASM:** Menunjukkan distribusi probabilitas pada $q_0$ sebagai indikator kasar dari besaran eigenvalue utama.
    - **Circuit Transpilation:** Gambar `circuit_transpiled_4x4.png` menunjukkan bagaimana rangkaian gerbang uniter didekomposisi menjadi gerbang dasar hardware (seperti $u3$ dan $cx$), yang krusial untuk menganalisis akumulasi *gate error*.

Berdasarkan kode pada file QPCA_4x4eigenstate.py, terdapat total 28 operasi gerbang yang disusun secara sekuensial untuk membentuk sirkuit QPCA tersebut (sebelum tahap pengukuran). Berikut adalah rincian urutan operasinya:
  1. Tahap Inisialisasi & Persiapan (2 Operasi)
   * 1x qc.initialize: Menyiapkan state awal berdasarkan data input pada qubit [1] dan q[2].
   * 1x qc.h (Hadamard): Menempatkan qubit kontrol q[0] ke dalam superposisi.

  2. Tahap Operasi Utama / Inti QPCA (25 Operasi)
  Ini adalah deretan gerbang yang kamu tanyakan sebelumnya, yang terdiri dari
  kombinasi:
   * 7x qc.p (Phase Gate): Melakukan rotasi fase dengan sudut-sudut tertentu.
   * 12x qc.cu (Controlled-Unitary): Gerbang kontrol yang menerapkan transformasi kompleks antar qubit. Ini adalah bagian paling intensif secara komputasi.
   * 6x qc.cx (CNOT): Membuat keterikatan (entanglement) antar qubit.

  3. Tahap Akhir (Inverse QFT) (1 Operasi)
   * 1x qc.h (Hadamard): Diterapkan kembali pada qubit q[0] sebagai bagian dari penyederhanaan Inverse Quantum Fourier Transform untuk mengekstrak fase.
  ---
  Total Kumulatif:
  Jika kita menjumlahkan semuanya:
  2 (Persiapan) + 25 (Inti) + 1 (Akhir) = 28 Operasi Gerbang.
