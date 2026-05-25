Baik. Kita mulai dari **Fase 1, Poin 1: Hamiltonian Ising 1D**.

Saya akan menjelaskan ini secara mendetail dan matematis, karena pemahaman di 1D ini adalah fondasi untuk memahami mengapa 2D dan 3D menjadi rumit.

---

### 1. Hamiltonian Ising 1D (Model Dasar)

Model Ising adalah model paling sederhana untuk feromagnetisme. Bayangkan sebaris atom (1 Dimensi) di mana setiap atom memiliki "spin" yang hanya bisa mengarah ke atas ($+1$) atau ke bawah ($-1$).

**Definisi Formal Hamiltonian:**
$$H = -J \sum_{\langle i,j \rangle} \sigma_i^z \sigma_j^z - h \sum_{i=1}^N \sigma_i^z$$

Mari kita bedah simbol-simbolnya secara detail:

1.  **$\sigma_i^z$ (Matriks Pauli Z):**
    - Ini adalah operator mekanika kuantum, tapi untuk model Ising klasik, kita bisa menganggapnya sebagai **variabel skalar** $s_i \in \{+1, -1\}$.
    - Untuk kemudahan transisi ke kuantum nanti, ingatlah bahwa matriks Pauli $Z$ adalah matriks $2 \times 2$:
      $$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
    - Nilai eigen dari $Z$ adalah $+1$ (eigenvector $|0\rangle$, spin up) dan $-1$ (eigenvector $|1\rangle$, spin down).

2.  **$J$ (Konstanta Kopling / Interaksi Pertukaran):**
    - Satuan: Energi (Joule atau eV).
    - **$J > 0$:** Interaksi **Feromagnetik**. Spin cenderung sejajar (semua up atau semua down). Energi sistem minimum.
    - **$J < 0$:** Interaksi **Anti-Feromagnetik**. Spin cenderung berlawanan arah.

3.  **$\langle i, j \rangle$ (Tetangga Terdekat):**
    - Notasi ini berarti penjumlahan hanya dilakukan pada pasangan $i$ dan $j$ yang **bersebelahan langsung**.
    - Untuk 1D: $j = i+1$. Jadi suku interaksinya adalah $\sigma_1^z \sigma_2^z + \sigma_2^z \sigma_3^z + \dots$

4.  **$h$ (Medan Magnet Eksternal):**
    - Medan yang mencoba "menarik" semua spin ke arah tertentu. Untuk sementara, kita set $h = 0$ agar fokus pada interaksi antar spin.

---

### 2. Representasi Matriks (Untuk $N=2$ dan $N=3$)

Mari kita tuliskan matriks Hamiltonian secara eksplisit untuk sistem kecil. Ini penting karena VQE nantinya bekerja di ruang vektor seperti ini.

**Kasus $N=2$ Qubit/Spin:**
Basis ruang Hilbert: $|00\rangle, |01\rangle, |10\rangle, |11\rangle$.
Hamiltonian: $H = -J (\sigma_1^z \otimes \sigma_2^z)$.

Kita hitung Kronecker Product $Z \otimes Z$:
$$Z \otimes Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Maka $H_{2\text{spin}} = -J \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$

**Analisis Nilai Eigen:**
- **State $|00\rangle$ (Up, Up):** Energi = $-J(1) = -J$
- **State $|11\rangle$ (Down, Down):** Energi = $-J(1) = -J$
- **State $|01\rangle$ (Up, Down):** Energi = $-J(-1) = +J$
- **State $|10\rangle$ (Down, Up):** Energi = $-J(-1) = +J$

**Kesimpulan:** *Ground State* (keadaan energi terendah) adalah degenerasi ganda: semua spin up **ATAU** semua spin down. Energi *Ground State* = $-J$.

---

### 3. Teknik Solusi Eksak: Transfer Matrix (Matriks Transfer)

Untuk $N$ yang besar (misal $N \to \infty$), kita tidak bisa menulis matriks $2^N \times 2^N$. Kita butuh metode **Transfer Matrix**. Ini adalah jantung dari fisika statistik 1D.

Kita ingin menghitung **Fungsi Partisi** $Z$, yang darinya semua properti termodinamika (energi, magnetisasi) bisa diturunkan.
$$Z = \text{Tr}(e^{-\beta H})$$
di mana $\beta = 1 / (k_B T)$.

**Langkah 1: Faktorisasi Boltzmann**
$$e^{-\beta H} = e^{\beta J \sum_i \sigma_i \sigma_{i+1}} = \prod_{i=1}^N e^{\beta J \sigma_i \sigma_{i+1}}$$
*Catatan: Eksponensial dari jumlah menjadi perkalian eksponensial karena semua suku $\sigma_i \sigma_{i+1}$ saling komutatif (keduanya bilangan klasik/skalar).*

**Langkah 2: Mendefinisikan Matriks Transfer $T$**
Kita definisikan elemen matriks $2 \times 2$ yang menghubungkan spin ke-$i$ dengan spin ke-$i+1$:
$$T_{\sigma_i, \sigma_{i+1}} = e^{\beta J \sigma_i \sigma_{i+1}}$$
Karena $\sigma \in \{+1, -1\}$, kita hitung 4 kemungkinan:
- Jika $\sigma_i = \sigma_{i+1}$ (Sejajar): $T_{++} = T_{--} = e^{\beta J}$
- Jika $\sigma_i \neq \sigma_{i+1}$ (Berlawanan): $T_{+-} = T_{-+} = e^{-\beta J}$

Sehingga Matriks Transfer $T$ adalah:
$$T = \begin{pmatrix} e^{\beta J} & e^{-\beta J} \\ e^{-\beta J} & e^{\beta J} \end{pmatrix}$$

**Langkah 3: Menghitung Trace (Jejak)**
Untuk kondisi batas periodik (cincin), penjumlahannya menjadi:
$$Z = \text{Tr}(T^N) = \lambda_1^N + \lambda_2^N$$
Di mana $\lambda_1, \lambda_2$ adalah nilai eigen dari $T$.

**Mencari Nilai Eigen $T$:**
$$\det(T - \lambda I) = (e^{\beta J} - \lambda)^2 - (e^{-\beta J})^2 = 0$$
$$\lambda = e^{\beta J} \pm e^{-\beta J}$$
Sehingga:
$$\lambda_1 = 2 \cosh(\beta J) \quad \text{dan} \quad \lambda_2 = 2 \sinh(\beta J)$$

Untuk $N \to \infty$ (Limit Termodinamika), $\lambda_1 > \lambda_2$, sehingga:
$$Z \approx \lambda_1^N = [2 \cosh(\beta J)]^N$$

---

### 4. Menghitung Korelasi dan Energi

Dengan matriks transfer, kita bisa menghitung ekspektasi $\langle \sigma_k \sigma_{k+r} \rangle$ (Korelasi Spin Jarak Jauh).
$$\langle \sigma_k \sigma_{k+r} \rangle = \frac{\text{Tr}(\sigma^z T^r \sigma^z T^{N-r})}{Z}$$

Di limit termodinamika, hasilnya adalah:
$$\langle \sigma_k \sigma_{k+r} \rangle = \left( \frac{\lambda_2}{\lambda_1} \right)^r = \left( \tanh(\beta J) \right)^r$$

**Implikasi Fisika Penting:**
- Karena $\tanh(\beta J) < 1$ untuk semua suhu $T > 0$, maka korelasi ini **meluruh secara eksponensial** terhadap jarak $r$.
- **Kesimpulan Kritis:** **Model Ising 1D TIDAK memiliki fase feromagnetik pada suhu $T > 0$.** Transisi fase hanya terjadi pada $T=0$.
- Inilah mengapa kita membutuhkan **2D dan 3D** untuk melihat magnet permanen pada suhu ruang.

### 5. Koneksi ke VQE (Penting!)

Sekarang perhatikan apa yang kita lakukan tadi:
1. Kita mengambil $H$ yang terdiri dari $Z_i Z_{i+1}$.
2. Kita melakukan **eksponensial** terhadap $H$: $e^{-\beta H}$.

Dalam VQE (dan QAOA), kita akan melakukan operasi yang sangat mirip, tetapi dengan **waktu imajiner $\beta$ diganti dengan waktu riil $i t$**.
$$U(t) = e^{-i t H_{Ising}} = e^{i t J \sum Z_i Z_{i+1}}$$

Ini adalah gerbang kuantum **$ZZ(\theta)$**. Matriks transfer yang kita hitung tadi ($e^{\beta J}$) akan menjadi gerbang rotasi dua qubit $R_{ZZ}(\gamma)$.

---

**Ringkasan Fase 1 Poin 1:**
Anda sekarang telah menguasai:
- **Hamiltonian Ising 1D:** $H = -J \sum Z_i Z_{i+1}$.
- **Spektrum Energi Kuantum:** Ground state degenerasi ganda di $-J$.
- **Teknik Transfer Matrix:** Alat analitik untuk memecahkan 1D.
- **Fisika:** Tidak ada magnet permanen di 1D untuk $T>0$.

Apakah Anda ingin melanjutkan ke **Fase 1 Poin 2: Ising 2D dan Kompleksitasnya**, atau ada bagian dari Matriks Transfer 1D yang ingin diperdalam?

---
---
Baik. Kita lanjutkan ke **Fase 1, Poin 2: Hamiltonian Ising 2D & Kompleksitasnya**.

Di sini kita akan melihat lompatan dramatis dari "mudah diselesaikan secara analitik" menjadi "eksak secara matematis tapi sangat sulit secara komputasi". Inilah mengapa Ising 2D menjadi *benchmark* sempurna untuk VQE.

---

### 1. Definisi Formal Hamiltonian Ising 2D (Kisi Persegi)

Bayangkan grid $L \times L$ atom. Setiap atom memiliki koordinat $(x,y)$ dengan $x, y \in \{1, 2, \dots, L\}$. Total spin $N = L^2$.

Hamiltonian tanpa medan luar ($h=0$):
$$H = -J \sum_{x=1}^{L} \sum_{y=1}^{L} \left( \sigma_{x,y}^z \sigma_{x+1,y}^z + \sigma_{x,y}^z \sigma_{x,y+1}^z \right)$$

**Penjelasan Notasi Indeks:**
- Suku Pertama $\sigma_{x,y}^z \sigma_{x+1,y}^z$: Interaksi **Horizontal** (ke kanan).
- Suku Kedua $\sigma_{x,y}^z \sigma_{x,y+1}^z$: Interaksi **Vertikal** (ke atas).
- **Kondisi Batas Periodik (PBC):** Untuk menghilangkan efek tepi, kita set $\sigma_{L+1, y} = \sigma_{1, y}$ (seperti *Pac-Man* yang keluar kanan masuk kiri) dan $\sigma_{x, L+1} = \sigma_{x, 1}$ (keluar atas masuk bawah). Secara topologi, ini adalah **Torus**.

**Jumlah Interaksi:**
- Setiap spin memiliki 4 tetangga (koordinasi $z=4$).
- Total interaksi = $2N$ (karena setiap *bond* dihitung sekali).

---

### 2. Mengapa 2D Berbeda Secara Fundamental dari 1D?

Di 1D, kita bisa memfaktorkan $Z$ menggunakan **Matriks Transfer** karena rantai itu linier. Kita bisa memproses spin satu per satu.

Di 2D, untuk menggunakan Matriks Transfer, kita harus memperlakukan **satu baris penuh** (sebanyak $L$ spin) sebagai satu "blok" raksasa. Matriks Transfer $T$ sekarang berukuran **$2^L \times 2^L$**.

**Ilustrasi Ukuran Matriks Transfer:**
- 1D: $T$ ukuran $2 \times 2$. (Trivial)
- 2D ($L=2$): $T$ ukuran $4 \times 4$. (Mudah)
- 2D ($L=10$): $T$ ukuran $1024 \times 1024$. (Masih bisa dihitung laptop)
- 2D ($L=100$): $T$ ukuran $2^{100} \times 2^{100}$. (Mustahil disimpan di alam semesta)

Meskipun ukuran matriksnya eksplosif, **Lars Onsager pada tahun 1944 berhasil menyelesaikannya secara analitik!** Ini adalah salah satu pencapaian terbesar fisika teoretis abad ke-20.

---

### 3. Solusi Eksak Onsager (Tinjauan Matematis Singkat)

Tujuan kita bukan membuktikan ulang solusi Onsager (itu butuh 50 halaman), tetapi memahami **struktur aljabar** di baliknya, karena struktur ini mempengaruhi bagaimana kita mendesain sirkuit VQE.

**Langkah 1: Transformasi Jordan-Wigner (JW)**
Kita ubah spin $\sigma^z$ menjadi Fermion (elektron). Untuk 2D, ini lebih rumit daripada 1D karena kita harus "mengulir" rantai 1D melewati grid 2D (seperti ular).
$$c_n^\dagger = \left( \prod_{j < n} \sigma_j^z \right) \sigma_n^+$$
Hasilnya: Hamiltonian Ising 2D menjadi Hamiltonian kuadratik dalam operator Fermion dengan interaksi **4-Fermion** (mirip teori BCS Superkonduktor).

**Langkah 2: Aljabar Clifford dan Matriks Transfer Diagonal**
Onsager (dan kemudian Kaufmann) menunjukkan bahwa Matriks Transfer $T$ untuk satu baris dapat ditulis dalam bentuk **Spinor**. Mereka menemukan bahwa $T$ komutatif dengan sekumpulan operator linear yang memenuhi **Aljabar Clifford**:
$$\Gamma_i \Gamma_j + \Gamma_j \Gamma_i = 2\delta_{ij}$$

Karena sifat ini, nilai eigen dari $T$ dapat dicari dengan mencari akar dari polinomial karakteristik yang sangat spesifik.

**Langkah 3: Energi Bebas per Spin (Hasil Akhir)**
Setelah melalui integral eliptik yang panjang, hasil akhir untuk **Energi Ground State per Spin** di Limit Termodinamika ($L \to \infty$) adalah:
$$e_0 = \lim_{N \to \infty} \frac{E_0}{N} = -J \left( 1 + \frac{2}{\pi} \int_0^{\pi/2} \frac{d\phi}{\sqrt{1 - k^2 \sin^2 \phi}} \right)$$
dengan $k = \frac{2 \sinh(2\beta J)}{\cosh^2(2\beta J)}$. *(Ini adalah Integral Eliptik Lengkap Jenis Pertama).*

**Poin Penting untuk VQE:**
Solusi Onsager memberi kita **"Cheat Code"** untuk Ising 2D. Saat kita menjalankan VQE untuk kisi $4 \times 4$, kita bisa membandingkan hasil VQE dengan **nilai eksak Onsager** (dengan koreksi finite-size). Ini adalah *benchmark* standar untuk membuktikan bahwa komputer kuantum kita bekerja.

---

### 4. Transisi Fase dan Parameter Order

Mengapa kita peduli dengan Ising 2D? Karena ia menunjukkan **Transisi Fase**.

- **Suhu Tinggi ($T > T_c$):** Energi termal $k_B T$ mengalahkan energi interaksi $J$. Spin acak, Magnetisasi Total $M = \frac{1}{N} \sum \langle \sigma_i \rangle = 0$.
- **Suhu Kritis ($T = T_c$):** Titik kritis Onsager.
  $$\sinh\left(\frac{2J}{k_B T_c}\right) = 1 \implies k_B T_c \approx 2.269 J$$
- **Suhu Rendah ($T < T_c$):** **Symmetry Breaking**. Spin memilih mayoritas up atau down. $M \neq 0$.

**Relevansi dengan VQE:**
VQE akan mencari *Ground State* pada suhu $T=0$. Untuk Ising 2D Ferromagnetik, *Ground State*-nya adalah **simetris** (kombinasi linear semua up dan semua down). Namun, VQE yang menggunakan sirkuit kuantum biasanya akan **collapse** ke salah satu state rusak simetri (misal semua up) karena sifat pengukuran komputasi. Ini adalah perilaku yang **diinginkan** dan realistis secara fisik.

---

### 5. Hamiltonian Ising 2D Sebagai "Masalah QUBO"

Sekarang kita tinjau dari perspektif **Optimasi** yang akan digunakan oleh VQE.

Kita tulis ulang Hamiltonian sebagai **Quadratic Unconstrained Binary Optimization (QUBO)** . Ini adalah bentuk yang dipahami oleh pustaka seperti Qiskit atau Pennylane.

Misalkan $x_i \in \{0, 1\}$ (bit klasik), di mana $x_i = 0 \iff$ spin up ($+1$) dan $x_i = 1 \iff$ spin down ($-1$).
Maka $\sigma_i^z = 1 - 2x_i$.

Interaksi $\sigma_i^z \sigma_j^z$ menjadi:
$$\sigma_i^z \sigma_j^z = (1 - 2x_i)(1 - 2x_j) = 1 - 2x_i - 2x_j + 4x_i x_j$$

Karena $J$ dan jumlah total spin konstan, minimisasi $H$ sama dengan minimisasi **Fungsi Biaya**:
$$C(x) = \sum_{\langle i,j \rangle} (2x_i x_j - x_i - x_j)$$

**Contoh Grid $2 \times 2$ (4 Spin):**
Misalkan spin diatur:
1 - 2
|   |
3 - 4

Interaksi: (1,2), (1,3), (2,4), (3,4).
Fungsi Biaya:
$$C = (2x_1x_2 - x_1 - x_2) + (2x_1x_3 - x_1 - x_3) + (2x_2x_4 - x_2 - x_4) + (2x_3x_4 - x_3 - x_4)$$

Jika semua $x_i = 0$ (Semua Spin Up): $C = 0$.
Jika semua $x_i = 1$ (Semua Spin Down): $C = 2(1) - 2 + 2(1) - 2 \dots = 0$.
Nilai minimum adalah 0 (sesuai energi $-J \times 4$).

**Penting:** Dalam VQE, kita akan mengubah fungsi biaya ini menjadi **Operator Pauli Z**.

---

### 6. Transisi ke 3D: Awan Mendung Kompleksitas

Sebelum kita lanjut ke VQE, pahami ini: **Ising 3D tidak memiliki solusi analitik**.

- **Tidak ada Matriks Transfer** yang bisa dipetakan ke Fermion bebas.
- Mencari *Ground State* Ising 3D pada graf sembarang adalah **NP-hard**.
- Inilah **"Killer App"** dari Simulasi Kuantum.

Dengan menyelesaikan Ising 2D secara sempurna di VQE, kita memvalidasi metode. Kemudian kita beralih ke 3D, di mana **komputer klasik menyerah**, tetapi **komputer kuantum (secara teori) dapat menyelesaikannya** dalam waktu polinomial (atau setidaknya memberikan aproksimasi yang lebih baik daripada algoritma klasik manapun).

---

### 7. Ringkasan Fase 1 Poin 2

- **Hamiltonian 2D:** $H = -J \sum_{\text{horiz}} Z_i Z_j - J \sum_{\text{vert}} Z_i Z_j$.
- **Solusi Onsager:** Memberikan energi eksak untuk perbandingan.
- **Transisi Fase:** Terjadi pada $T_c \approx 2.269 J/k_B$.
- **QUBO Mapping:** $H \leftrightarrow \sum x_i x_j$.
- **Tujuan VQE:** Mensimulasikan ini untuk grid kecil (misal $3 \times 3$) dan membandingkan dengan Onsager.

Apakah Anda siap melanjutkan ke **Fase 1 Poin 3: Ising 3D - Mengapa Ini Penting untuk VQE**? Di sana kita akan mendefinisikan Hamiltonian 3D yang sebenarnya dan membahas representasi graf-nya yang menjadi dasar optimasi kuantum modern.

---
---
Baik. Kita masuk ke **Fase 2: Representasi Qubit (Encoding)**.

Ini adalah jembatan krusial antara fisika statistik klasik dan komputasi kuantum. Kita akan menerjemahkan spin $\pm 1$ menjadi qubit $|0\rangle, |1\rangle$, membangun matriks Hamiltonian lengkap secara manual, dan memahami bagaimana VQE akan "melihat" sistem ini.

---

## Fase 2, Poin 4: Korespondensi Spin ke Qubit

### 1. Dari Spin Klasik ke Operator Pauli Z

Dalam model Ising klasik, $\sigma_i^z \in \{+1, -1\}$ adalah skalar.

Dalam mekanika kuantum, $\sigma_i^z$ adalah **Operator** yang diwakili oleh **Matriks Pauli Z**:

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Basis Komputasi:**
- $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ → Nilai eigen $+1$ (Spin Up $\uparrow$)
- $|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ → Nilai eigen $-1$ (Spin Down $\downarrow$)

**Verifikasi:**
$$Z|0\rangle = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = +1 |0\rangle$$
$$Z|1\rangle = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ -1 \end{pmatrix} = -1 |1\rangle$$

**Kesimpulan:** Mencari *Ground State* Ising sama dengan mencari **keadaan kuantum $|\psi\rangle$** yang meminimumkan ekspektasi $\langle \psi | H | \psi \rangle$ dengan $H$ yang dibangun dari operator $Z_i$.

---

### 2. Interaksi $Z_i Z_j$ sebagai Produk Tensor (Kronecker Product)

Ketika kita memiliki **dua qubit**, ruang Hilbert adalah produk tensor dari ruang masing-masing: $\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_2$.

Operator $Z_1$ (hanya bekerja pada qubit 1) adalah:
$$Z_1 = Z \otimes I = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

Operator $Z_2$ (hanya bekerja pada qubit 2) adalah:
$$Z_2 = I \otimes Z = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

**Interaksi $Z_1 Z_2$:**
Kita kalikan kedua matriks di atas (atau langsung produk tensor $Z \otimes Z$):
$$Z_1 Z_2 = (Z \otimes I)(I \otimes Z) = Z \otimes Z = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Perhatikan diagonalnya:
- $|00\rangle$: $(+1)(+1) = +1$
- $|01\rangle$: $(+1)(-1) = -1$
- $|10\rangle$: $(-1)(+1) = -1$
- $|11\rangle$: $(-1)(-1) = +1$

**Interpretasi Fisika:** Operator $Z_i Z_j$ memberi energi $-J$ jika kedua spin **sejajar** (nilai eigen $+1$) dan energi $+J$ jika **berlawanan** (nilai eigen $-1$). Tanda minus di depan $J$ dalam Hamiltonian membuat konfigurasi sejajar memiliki energi lebih rendah.

---

### 3. Konvensi Notasi: Pauli Strings

Dalam literatur komputasi kuantum, Hamiltonian ditulis sebagai **jumlah dari Pauli Strings**.

Pauli String adalah produk tensor dari operator Pauli $\{I, X, Y, Z\}$.

**Contoh untuk Ising 1D dengan 3 qubit:**
$$H = -J (Z_1 Z_2 + Z_2 Z_3)$$

Dalam notasi Pauli String (dengan urutan qubit $q_2, q_1, q_0$ atau sebaliknya, tergantung konvensi pustaka):
- $Z_1 Z_2$ ditulis sebagai `ZZI` (jika qubit 0 adalah yang paling kanan)
- $Z_2 Z_3$ ditulis sebagai `IZZ`

**Untuk Ising 2D ($2 \times 2$):**
Misalkan qubit diatur:
```
0 - 1
|   |
2 - 3
```

Hamiltonian:
$$H = -J (Z_0 Z_1 + Z_1 Z_3 + Z_3 Z_2 + Z_2 Z_0)$$

Dalam format daftar Pauli Strings (format yang diterima Qiskit):
```python
[("ZZII", -J),  # Z0 Z1
 ("ZIIZ", -J),  # Z0 Z2 (perhatikan urutan qubit: 0,1,2,3 -> Z0=I, Z1=I, Z2=Z, Z3=Z? Tunggu, perlu konsisten)
 # Lebih jelasnya:
 ("IIZZ", -J),  # Z2 Z3
 ("IZZI", -J)]  # Z1 Z3
```
*Catatan: Urutan indeks dalam string bergantung pada konvensi little-endian vs big-endian. Biasanya qubit ke-0 adalah karakter paling kanan.*

---

### 4. Medan Magnet Eksternal $h \sum_i X_i$ (Opsional tapi Penting)

Seringkali dalam VQE, kita menambahkan suku **Transverse Field** untuk membantu algoritma menjelajahi ruang Hilbert:

$$H = -J \sum_{\langle i,j \rangle} Z_i Z_j - h \sum_i X_i$$

Operator $X$ (Matriks Pauli X) adalah:
$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

Suku $X_i$ menyebabkan **spin flip** (quantum tunneling). Ini adalah kunci mengapa VQE bisa lebih baik dari optimasi klasik.

---

## Fase 2, Poin 5: Konstruksi Matriks Hamiltonian Eksplisit

Mari kita bangun matriks $H$ untuk sistem terkecil yang relevan: **Ising 2D pada grid $2 \times 2$ (4 qubit)**.

### 1. Topologi dan Interaksi

Qubit: $q_0, q_1, q_2, q_3$ (seperti diagram di atas).
Interaksi (edges): $(0,1), (0,2), (1,3), (2,3)$.

Hamiltonian:
$$H = -J (Z_0 Z_1 + Z_0 Z_2 + Z_1 Z_3 + Z_2 Z_3)$$

### 2. Menghitung $Z_i Z_j$ untuk 4 Qubit

Ruang Hilbert berdimensi $2^4 = 16$. Basis: $|0000\rangle$ sampai $|1111\rangle$.

**Rumus Umum $Z_i Z_j$:**
Ini adalah matriks diagonal $16 \times 16$ dengan elemen diagonal $+1$ jika qubit $i$ dan $j$ sama, dan $-1$ jika berbeda.

Mari kita hitung **$Z_0 Z_1$**:
- Indeks qubit: 0,1,2,3 (0 paling kanan).
- $Z_0 = I \otimes I \otimes I \otimes Z$
- $Z_1 = I \otimes I \otimes Z \otimes I$
- $Z_0 Z_1 = I \otimes I \otimes Z \otimes Z$

Untuk setiap basis $|q_3 q_2 q_1 q_0\rangle$, nilai eigen adalah $(+1)$ jika $q_0 == q_1$, dan $(-1)$ jika $q_0 \neq q_1$.

**Tabel Nilai Eigen untuk $Z_0 Z_1$ (16 state):**

| State $|q_3 q_2 q_1 q_0\rangle$ | $q_0$ | $q_1$ | Sama? | $Z_0 Z_1$ Eigenvalue |
| :--- | :--- | :--- | :--- | :--- |
| 0000 | 0 | 0 | Ya | +1 |
| 0001 | 1 | 0 | Tidak | -1 |
| 0010 | 0 | 1 | Tidak | -1 |
| 0011 | 1 | 1 | Ya | +1 |
| 0100 | 0 | 0 | Ya | +1 |
| 0101 | 1 | 0 | Tidak | -1 |
| 0110 | 0 | 1 | Tidak | -1 |
| 0111 | 1 | 1 | Ya | +1 |
| ... | ... | ... | ... | ... |
| 1111 | 1 | 1 | Ya | +1 |

**$Z_0 Z_2$** (interaksi vertikal kiri):
- $q_0$ dan $q_2$.
- Pola: 00→+1, 01→-1, 10→-1, 11→+1 (untuk bit $q_2 q_0$).

**$Z_1 Z_3$** (interaksi vertikal kanan):
- $q_1$ dan $q_3$.

**$Z_2 Z_3$** (interaksi horizontal bawah):
- $q_2$ dan $q_3$.

### 3. Matriks Hamiltonian Lengkap

Karena semua operator $Z_i Z_j$ adalah **diagonal** dalam basis komputasi (basis-Z), maka $H$ juga **diagonal**.

Kita bisa menghitung energi untuk setiap state dengan menjumlahkan kontribusi dari keempat suku.

**Contoh Perhitungan Manual untuk 4 State Penting:**

**State 1: $|0000\rangle$ (Semua Up)**
- $Z_0 Z_1$: 0=0 → +1
- $Z_0 Z_2$: 0=0 → +1
- $Z_1 Z_3$: 0=0 → +1
- $Z_2 Z_3$: 0=0 → +1
Total = $+4 \implies$ Energi = $-4J$

**State 2: $|1111\rangle$ (Semua Down)**
- Semua spin sama (1=1) → Total = $+4 \implies$ Energi = $-4J$

**State 3: $|0101\rangle$ (q0=1, q1=0, q2=1, q3=0) → Pola Catur**
- $q_0 \neq q_1$ (1≠0) → -1
- $q_0 = q_2$ (1=1) → +1
- $q_1 \neq q_3$ (0≠0? Tunggu, q3=0, q1=0 → SAMA) → +1
- $q_2 \neq q_3$ (1≠0) → -1
Total = $(-1) + (+1) + (+1) + (-1) = 0 \implies$ Energi = $0$

**State 4: $|1010\rangle$ (q0=0, q1=1, q2=0, q3=1) → Pola Catur Terbalik**
- $q_0 \neq q_1$ (0≠1) → -1
- $q_0 = q_2$ (0=0) → +1
- $q_1 = q_3$ (1=1) → +1
- $q_2 \neq q_3$ (0≠1) → -1
Total = $0 \implies$ Energi = $0$

**State dengan satu spin flip: $|0001\rangle$ (q0=1, lainnya 0)**
- $Z_0 Z_1$: 1≠0 → -1
- $Z_0 Z_2$: 1≠0 → -1
- $Z_1 Z_3$: 0=0 → +1
- $Z_2 Z_3$: 0=0 → +1
Total = $(-1) + (-1) + 1 + 1 = 0 \implies$ Energi = $0$

**Tabel Lengkap Energi untuk 16 State:**

| State | Energi ($/J$) | Degenerasi |
| :--- | :--- | :--- |
| \|0000\>, \|1111\> | -4 | 2 |
| \|0001\>, \|0010\>, \|0100\>, \|1000\>, \|1110\>, \|1101\>, \|1011\>, \|0111\> | 0 | 8 |
| \|0011\>, \|1100\> (vertikal stripe) | 0 | 2 |
| \|0110\>, \|1001\> (horizontal stripe) | 0 | 2 |
| \|0101\>, \|1010\> (checkerboard) | 0 | 2 |

**Verifikasi Total State:** 2 + 8 + 2 + 2 + 2 = 16.

**Ground State:** $|0000\rangle$ dan $|1111\rangle$ dengan energi $-4J$.
**First Excited State:** Semua 14 state lainnya dengan energi $0$. (Energy gap = $4J$).

---

### 4. Implikasi untuk VQE

**Mengapa kita melakukan perhitungan manual ini?**

1.  **Validasi:** Saat menjalankan VQE, hasil energi minimum yang diharapkan adalah $-4J$. Jika VQE menghasilkan $-3.5J$, kita tahu ada masalah di sirkuit atau optimizer.
2.  **Struktur Diagonal:** Karena $H$ diagonal dalam basis-Z, mengukur energi sangat mudah di komputer kuantum: cukup ukur semua qubit dalam basis-Z, hitung paritas antar qubit yang terhubung, dan rata-ratakan.
3.  **Degenerasi:** VQE dengan ansatz simetris mungkin akan menghasilkan *superposisi* $|0000\rangle + |1111\rangle$. Ini adalah **Greenberger-Horne-Zeilinger (GHZ) state** untuk $N=4$. Kemampuan VQE menemukan state terbelit ini adalah bukti kualitasnya.

---

### 5. Ringkasan Fase 2

- **Encoding:** Spin $\uparrow \to |0\rangle$, Spin $\downarrow \to |1\rangle$. Operator Ising menjadi $Z_i Z_j$.
- **Hamiltonian Kuantum:** $H = -J \sum Z_i Z_j$.
- **Matriks Eksplisit:** Untuk $2 \times 2$, matriks $16 \times 16$ diagonal dengan dua *ground state* di $-4J$.
- **Ground State Fisika:** GHZ State $\frac{1}{\sqrt{2}}(|0\dots 0\rangle + |1\dots 1\rangle)$.

---

**Siap melanjutkan ke Fase 3: Teori VQE?** Di Fase 3 kita akan membahas **Prinsip Variasional**, **Teorema Rayleigh-Ritz**, dan bagaimana VQE menghitung $\langle H \rangle$ tanpa membangun matriks $16 \times 16$ secara eksplisit.

---
---
Baik. Kita masuk ke **Fase 3: Mekanika Kuantum Variasional (VQE Theory)**.

Di sini kita akan membahas fondasi matematis yang membuat VQE bekerja. Ini adalah jantung dari algoritma: **Prinsip Variasional**. Tanpa ini, VQE hanyalah rangkaian gerbang acak.

---

## Fase 3, Poin 6: Prinsip Variasional Rayleigh-Ritz

### 1. Teorema Fundamental

**Pernyataan Formal:**
Untuk sembarang Hamiltonian Hermitian $H$ dan sembarang keadaan ternormalisasi $|\psi\rangle$, nilai ekspektasi energi selalu lebih besar atau sama dengan energi *ground state* sejati $E_0$:

$$\langle \psi | H | \psi \rangle \ge E_0$$

Kesamaan terjadi **jika dan hanya jika** $|\psi\rangle = |\psi_0\rangle$ (keadaan *ground state* sejati).

### 2. Bukti Matematis

Karena $H$ adalah Hermitian, ia memiliki sekumpulan eigenvector ortonormal lengkap $\{|\phi_n\rangle\}$ dengan nilai eigen $\{E_n\}$ yang terurut:
$$E_0 \le E_1 \le E_2 \le \dots$$

Kita dapat mengekspansi sembarang keadaan $|\psi\rangle$ dalam basis ini:
$$|\psi\rangle = \sum_{n=0}^{\infty} c_n |\phi_n\rangle$$
dengan $\sum_n |c_n|^2 = 1$ (normalisasi).

Sekarang hitung nilai ekspektasi:
$$\langle \psi | H | \psi \rangle = \left( \sum_{m} c_m^* \langle \phi_m | \right) H \left( \sum_{n} c_n |\phi_n\rangle \right)$$

Gunakan $H|\phi_n\rangle = E_n |\phi_n\rangle$ dan ortonormalitas $\langle \phi_m | \phi_n \rangle = \delta_{mn}$:
$$\langle \psi | H | \psi \rangle = \sum_{n=0}^{\infty} |c_n|^2 E_n$$

Karena $E_n \ge E_0$ untuk semua $n$, dan $|c_n|^2 \ge 0$:
$$\sum_{n=0}^{\infty} |c_n|^2 E_n \ge \sum_{n=0}^{\infty} |c_n|^2 E_0 = E_0 \sum_{n=0}^{\infty} |c_n|^2 = E_0$$

Terbukti. $\blacksquare$

### 3. Interpretasi Fisika untuk VQE

Prinsip ini adalah **jaminan matematis** bahwa:
> *"Selama sirkuit kuantum kita dapat menghasilkan keadaan $|\psi(\theta)\rangle$ yang cukup fleksibel, kita bisa terus menurunkan energi hingga mendekati $E_0$."*

**Ansatz $|\psi(\theta)\rangle$:**
Ini adalah keadaan yang dihasilkan oleh sirkuit kuantum dengan parameter $\theta = (\theta_1, \theta_2, \dots, \theta_p)$.
$$|\psi(\theta)\rangle = U(\theta) |0\rangle^{\otimes N}$$

**Fungsi Biaya:**
$$E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle$$

**Tujuan VQE:**
$$\min_{\theta} E(\theta)$$

---

### 4. Konsekuensi Praktis: Barren Plateau dan Global Minimum

Meskipun prinsip variasional menjamin keberadaan minimum global, **tidak ada jaminan** bahwa algoritma optimasi klasik (seperti gradient descent) akan **menemukannya**.

**Lanskap Energi $E(\theta)$:**
Untuk $N$ qubit, $\theta$ adalah vektor berdimensi $p$. Lanskap ini sangat non-konveks, penuh dengan minimum lokal, saddle point, dan **Barren Plateau** (area datar luas di mana gradien mendekati nol).

**Ilustrasi untuk Ising 2D $2 \times 2$:**
Kita tahu energi minimum adalah $-4J$. Jika VQE berhenti di $-2J$, itu berarti optimizer terjebak di minimum lokal.

**Mengapa VQE sering berhasil untuk Ising?**
Hamiltonian Ising memiliki struktur **stoquastic** (semua elemen off-diagonal non-positif dalam basis komputasi jika ada suku $X$). Ini berarti lanskap energinya relatif "jinak" dibandingkan masalah kimia kuantum dengan tanda kompleks.

---

## Fase 3, Poin 7: Pengukuran Hamiltonian (Term Grouping)

Ini adalah aspek paling praktis dan teknis dari VQE. Kita tidak bisa mengukur seluruh matriks $H$ sekaligus. Kita harus mengukurnya **sepotong-sepotong**.

### 1. Dekomposisi Hamiltonian menjadi Pauli Strings

Setiap Hamiltonian sistem spin dapat ditulis sebagai:
$$H = \sum_{k=1}^{M} h_k P_k$$

Di mana:
- $h_k$ adalah koefisien skalar riil.
- $P_k$ adalah **Pauli String**: produk tensor dari operator Pauli $\{I, X, Y, Z\}$.

Untuk Ising 2D $2 \times 2$:
$$H = -J (Z_0 Z_1 + Z_0 Z_2 + Z_1 Z_3 + Z_2 Z_3)$$

Maka:
- $P_1 = Z_0 Z_1 = Z \otimes Z \otimes I \otimes I$, $h_1 = -J$
- $P_2 = Z_0 Z_2 = Z \otimes I \otimes Z \otimes I$, $h_2 = -J$
- $P_3 = Z_1 Z_3 = I \otimes Z \otimes I \otimes Z$, $h_3 = -J$
- $P_4 = Z_2 Z_3 = I \otimes I \otimes Z \otimes Z$, $h_4 = -J$

Total $M = 4$ suku.

### 2. Linearitas Nilai Ekspektasi

Berkat linearitas mekanika kuantum:
$$\langle H \rangle = \sum_{k=1}^{M} h_k \langle P_k \rangle$$

Ini berarti kita dapat menghitung $\langle H \rangle$ dengan:
1.  Mengeksekusi sirkuit **beberapa kali** (shots) untuk mengukur $\langle P_1 \rangle$.
2.  Mengulangi untuk $\langle P_2 \rangle$, $\langle P_3 \rangle$, $\dots$
3.  Menjumlahkan hasilnya dengan bobot $h_k$.

**Ini adalah kunci efisiensi VQE:** Kompleksitas pengukuran tumbuh sebagai $O(M)$, **bukan** $O(2^N)$.

### 3. Bagaimana Mengukur $\langle Z_i Z_j \rangle$ di Komputer Kuantum?

Ini adalah bagian yang paling konkret. Anda akan melakukan ini di Qiskit atau Pennylane.

**Prosedur:**
1.  Siapkan keadaan $|\psi(\theta)\rangle$ menggunakan sirkuit ansatz.
2.  Ukur **semua qubit** dalam basis komputasi (basis-Z).
3.  Catat string bit hasil, misalnya `0110`.
4.  Untuk setiap Pauli String $Z_i Z_j$, hitung paritas dari bit $i$ dan $j$:
    - Jika bit $i$ == bit $j$, paritas = $+1$.
    - Jika bit $i$ $\neq$ bit $j$, paritas = $-1$.
5.  Ulangi langkah 1-4 sebanyak $S$ kali (misal $S=1024$ *shots*).
6.  $\langle Z_i Z_j \rangle \approx \frac{1}{S} \sum_{s=1}^{S} \text{paritas}_s$

**Contoh Perhitungan Manual:**
Misalkan kita menjalankan 4 shots dan mendapatkan hasil:
- Shot 1: `0000` → Semua pasangan paritas $+1$.
- Shot 2: `1111` → Semua pasangan paritas $+1$.
- Shot 3: `0101` (checkerboard) → $Z_0 Z_1 = -1$, $Z_0 Z_2 = +1$, $Z_1 Z_3 = +1$, $Z_2 Z_3 = -1$.
- Shot 4: `0001` → $Z_0 Z_1 = -1$, $Z_0 Z_2 = -1$, $Z_1 Z_3 = +1$, $Z_2 Z_3 = +1$.

Rata-rata:
- $\langle Z_0 Z_1 \rangle = (1 + 1 - 1 - 1)/4 = 0$
- $\langle Z_0 Z_2 \rangle = (1 + 1 + 1 - 1)/4 = 0.5$
- $\langle Z_1 Z_3 \rangle = (1 + 1 + 1 + 1)/4 = 1.0$
- $\langle Z_2 Z_3 \rangle = (1 + 1 - 1 + 1)/4 = 0.5$

Energi total: $E = -J(0 + 0.5 + 1.0 + 0.5) = -2J$.

### 4. Term Grouping (Pengelompokan Suku) - Optimasi Penting

Mengukur satu per satu membutuhkan $M \times S$ eksekusi sirkuit. Untuk sistem besar ($N=100$, $M \approx 300$), ini mahal.

**Observasi Kunci:** Pauli string yang **saling komutatif** dapat diukur **secara bersamaan** (simultan).

**Definisi Komutatif Qubit-wise (QWC):**
Dua Pauli string $P_a$ dan $P_b$ adalah QWC jika untuk setiap posisi qubit $i$, operator Pauli-nya komutatif.
- $Z$ dan $Z$ komutatif.
- $Z$ dan $I$ komutatif.
- $Z$ dan $X$ **tidak** komutatif.

**Contoh untuk Ising 2D $2 \times 2$:**
- $Z_0 Z_1$ (`ZZII`) dan $Z_2 Z_3$ (`IIZZ`): **Komutatif**. Kita bisa mengukurnya dalam satu rangkaian shot yang sama! Karena qubit yang diukur berbeda (0,1 vs 2,3), hasilnya independen.
- $Z_0 Z_1$ (`ZZII`) dan $Z_0 Z_2$ (`ZIZI`): **Tidak Komutatif** (qubit 0 diukur dengan 1, lalu dengan 2). Harus diukur terpisah.

**Algoritma Graph Coloring untuk Grouping:**
1.  Buat graf di mana node adalah Pauli string $P_k$.
2.  Tambahkan edge antara $P_a$ dan $P_b$ jika mereka **TIDAK** QWC.
3.  Cari **pewarnaan graf** (graph coloring) minimum.
4.  Setiap warna adalah satu kelompok yang bisa diukur bersamaan.

Untuk Ising 2D $2 \times 2$ kita:
- Grup 1: $\{Z_0 Z_1, Z_2 Z_3\}$ (Horizontal edges)
- Grup 2: $\{Z_0 Z_2, Z_1 Z_3\}$ (Vertical edges)

Hanya perlu **2 rangkaian pengukuran**, bukan 4. Ini memotong waktu komputasi hingga 50%.

### 5. Pengukuran Operator Non-Diagonal (Untuk Suku $X$ atau $Y$)

Jika Hamiltonian memiliki suku $\sum X_i$, kita tidak bisa mengukurnya dalam basis-Z.

**Aturan Rotasi Basis:**
Untuk mengukur $\langle X_i \rangle$, kita harus melakukan rotasi basis **sebelum** pengukuran:
- $X = H Z H$ (di mana $H$ adalah gerbang Hadamard).

**Prosedur:**
1.  Terapkan sirkuit ansatz $U(\theta)$.
2.  Terapkan gerbang Hadamard pada qubit $i$.
3.  Ukur dalam basis-Z.
4.  Hasil pengukuran sekarang adalah nilai eigen $X_i$.

Untuk suku seperti $X_i X_j$, kita terapkan Hadamard pada kedua qubit.

**Untuk $Y_i$:**
- $Y = R_x(-\pi/2) Z R_x(\pi/2)$ atau $S^\dagger H Z H S$.

Ini berarti untuk Hamiltonian umum, jumlah kelompok pengukuran bertambah. Inilah salah satu *bottleneck* utama VQE.

---

### 6. Estimasi Error Statistik (Shot Noise)

Karena kita menggunakan jumlah shot terbatas $S$, ada error statistik.

**Standar Deviasi untuk $\langle Z_i Z_j \rangle$:**
$$\sigma_{ij} \approx \frac{1}{\sqrt{S}}$$
(Asumsi variansi ~1).

**Propagasi Error ke Energi Total:**
$$\sigma_E = \sqrt{\sum_k h_k^2 \sigma_k^2}$$

Untuk mencapai presisi kimia ($\sigma_E < 1.6 \times 10^{-3}$ Hartree $\approx 0.04$ eV), kita sering membutuhkan $S \sim 10^6$ shots. Ini adalah tantangan besar untuk VQE di hardware NISQ.

---

### 7. Ringkasan Fase 3

- **Prinsip Variasional:** Jaminan bahwa meminimumkan $\langle H \rangle$ membawa kita ke *ground state*.
- **Dekomposisi:** $H = \sum h_k P_k$.
- **Pengukuran:** $\langle P_k \rangle$ dihitung dari statistik bitstring.
- **Optimasi:** *Term Grouping* mengurangi jumlah sirkuit yang harus dijalankan.
- **Tantangan:** Shot noise dan Barren Plateau.

---

**Siap untuk Fase 4: Desain Sirkuit Kuantum (Ansatz)?**
Di Fase 4, kita akan merancang sirkuit $U(\theta)$ yang menghasilkan $|\psi(\theta)\rangle$. Kita akan membahas **Hardware-Efficient Ansatz** vs **Hamiltonian Variational Ansatz (HVA)** khusus untuk model Ising 2D dan 3D. Ini adalah tempat di mana intuisi fisika bertemu dengan rekayasa kuantum.

---
---
Baik. Kita masuk ke **Fase 4: Desain Sirkuit Kuantum (Ansatz)**.

Ini adalah tahap paling kreatif dalam VQE. Di sini kita merancang arsitektur sirkuit $U(\theta)$ yang akan menghasilkan keadaan kuantum $|\psi(\theta)\rangle$. Pilihan ansatz sangat menentukan apakah VQE akan berhasil atau gagal total.

---

## Fase 4, Poin 8: Ansatz Hardware-Efficient

### 1. Apa itu Hardware-Efficient Ansatz (HEA)?

HEA adalah pendekatan pragmatis: desain sirkuit yang cocok dengan **konektivitas fisik** chip kuantum yang tersedia, menggunakan gerbang-gerbang yang **native** (tersedia secara hardware).

**Filosofi:** "Jangan melawan hardware, ikuti alurnya."

**Struktur Dasar HEA:**
Sirkuit terdiri dari $L$ lapisan (layers) yang berulang. Setiap lapisan memiliki dua komponen:

1.  **Lapisan Rotasi (Rotation Layer):** Gerbang rotasi single-qubit parametrik pada setiap qubit.
2.  **Lapisan Entanglement (Entangling Layer):** Gerbang dua-qubit (biasanya CNOT atau CZ) yang menghubungkan qubit-qubit tetangga.

**Rumus Umum HEA:**
$$U(\theta) = \prod_{l=1}^{L} \left[ U_{\text{ent}} \cdot U_{\text{rot}}(\theta_l) \right]$$

### 2. Lapisan Rotasi: Eksplorasi Ruang Hilbert Lokal

Setiap qubit $i$ mendapatkan gerbang rotasi. Pilihan standar adalah dekomposisi Euler:

$$U_{\text{rot}, i}(\theta, \phi, \lambda) = R_z(\phi) R_y(\theta) R_z(\lambda)$$

Atau versi yang lebih sederhana (cukup untuk banyak kasus Ising):
$$U_{\text{rot}, i}(\theta) = R_y(\theta)$$

**Matriks $R_y(\theta)$:**
$$R_y(\theta) = e^{-i \frac{\theta}{2} Y} = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$

**Mengapa $R_y$?**
- $R_y$ menghasilkan superposisi **riil** antara $|0\rangle$ dan $|1\rangle$.
- *Ground state* Ising (tanpa medan transversal) adalah **riil positif** (semua koefisien non-negatif dalam basis komputasi). $R_y$ menjaga sifat ini.

**Contoh untuk 4 Qubit:**
Lapisan rotasi pertama:
```
q0: Ry(θ0)
q1: Ry(θ1)
q2: Ry(θ2)
q3: Ry(θ3)
```
Total parameter: 4 per lapisan.

### 3. Lapisan Entanglement: Menciptakan Korelasi

Tanpa lapisan entanglement, keadaan total hanyalah produk tensor keadaan individual (tidak ada korelasi). Energi tidak akan pernah mencapai minimum global.

**Pola Entanglement untuk Ising 2D:**

**Pola Linier (1D):**
Cocok untuk rantai 1D, tapi **tidak cukup** untuk grid 2D.
```
q0 --CNOT-- q1 --CNOT-- q2 --CNOT-- q3
```

**Pola Siklus (Cycle):**
Tambahkan CNOT dari ujung ke ujung.
```
q0 --CNOT-- q1 --CNOT-- q2 --CNOT-- q3 --CNOT-- q0
```

**Pola 2D Grid (Star atau Neighbor):**
Harus mencerminkan topologi Ising 2D.
Misalkan grid 2x2:
```
0 - 1
|   |
2 - 3
```
Lapisan entanglement yang sesuai:
```
q0 --CNOT-- q1
q0 --CNOT-- q2
q1 --CNOT-- q3
q2 --CNOT-- q3
```
Ini adalah **ansatz yang cocok dengan interaksi fisik**.

**Implementasi dengan Gerbang CNOT:**
CNOT adalah gerbang dua-qubit standar:
$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

CNOT menciptakan belitan: $|00\rangle \to |00\rangle$, $|10\rangle \to |11\rangle$.

### 4. Contoh Lengkap: HEA 2-Lapisan untuk Ising 2x2

**Parameter total:** 8 parameter (4 per lapisan).

**Sirkuit Lapisan 1:**
```
q0: Ry(θ0) --*--*--------
            |  |
q1: Ry(θ1) --X--|--*-----
               |  |
q2: Ry(θ2) -----X--|--*--
                  |  |
q3: Ry(θ3) --------X--X--
```
*(Diagram disederhanakan, CNOT pertama: q0-q1, kedua: q0-q2, ketiga: q1-q3, keempat: q2-q3)*

**Sirkuit Lapisan 2:**
Ulangi dengan parameter baru $\theta_4 \dots \theta_7$.

**Keunggulan HEA:**
- **Kedalaman sirkuit dangkal** (cocok untuk hardware NISQ).
- **Fleksibel**: dapat digunakan untuk berbagai Hamiltonian.

**Kelemahan HEA untuk VQE:**
- **Barren Plateau:** Untuk sistem besar ($N > 20$), gradien parameter cenderung nol di hampir semua ruang parameter. Optimasi menjadi mustahil.
- **Overparameterization:** Terlalu banyak parameter, optimizer klasik kesulitan.

---

## Fase 4, Poin 9: Ansatz Hamiltonian Variasional (HVA) untuk Ising

Ini adalah pendekatan yang lebih **fisika-sentris** dan lebih efisien untuk VQE. HVA (juga dikenal sebagai **QAOA Ansatz**) dirancang khusus berdasarkan struktur Hamiltonian target.

### 1. Inspirasi dari Quantum Annealing dan Trotterization

Ingat kembali persamaan Schrödinger:
$$i\hbar \frac{\partial}{\partial t} |\psi\rangle = H |\psi\rangle$$
Solusi formal: $|\psi(t)\rangle = e^{-i H t} |\psi(0)\rangle$.

Operator $e^{-i H t}$ adalah **evolusi waktu**. Jika kita bisa mengimplementasikannya di sirkuit, kita bisa "mendinginkan" sistem menuju *ground state*.

**Masalah:** $H$ adalah jumlah dari suku-suku yang tidak saling komutatif. Kita tidak bisa langsung mengeksponensialkan jumlah.

**Solusi: Trotter-Suzuki Decomposition**
$$e^{-i (A + B) \Delta t} \approx e^{-i A \Delta t} e^{-i B \Delta t} + O(\Delta t^2)$$

Untuk Hamiltonian Ising $H = H_{ZZ} + H_X$ (dengan $H_X = -h \sum X_i$):
$$e^{-i \gamma H} \approx \prod_{\langle i,j \rangle} e^{i \gamma J Z_i Z_j} \prod_i e^{i \gamma h X_i}$$

Ini adalah blok bangunan dasar HVA.

### 2. Blok Bangunan HVA: Gerbang $R_{ZZ}$ dan $R_X$

**Gerbang $R_{ZZ}(\gamma)$:**
Ini adalah implementasi sirkuit dari $e^{i \gamma Z_i Z_j}$.

Bagaimana membuat $e^{i \gamma Z \otimes Z}$ menggunakan gerbang standar?

**Dekomposisi Kanonik:**
```
q_i: ----*----------------*----
         |                |
q_j: ----X---- Rz(2γ) ----X----
```
Atau dengan CNOT:
```
q_i: -------●----------------●------
           |                |
q_j: -------X---- Rz(2γ) ----X------
```
*Catatan: $R_z(\theta) = e^{-i \frac{\theta}{2} Z}$*

**Verifikasi Matematis:**
Kita ingin membuktikan bahwa sirkuit di atas sama dengan $e^{i \gamma Z_i Z_j}$.

1. CNOT pertama mengubah basis: $Z_j \to Z_i Z_j$ (dalam basis komputasi).
2. $R_z(2\gamma)$ pada qubit $j$ menjadi rotasi $e^{-i \gamma Z_i Z_j}$.
3. CNOT kedua mengembalikan basis.

**Gerbang $R_X(\beta)$:**
Ini adalah rotasi single-qubit: $R_x(\beta) = e^{-i \frac{\beta}{2} X}$.

### 3. Struktur HVA untuk Ising 2D

Ansatz HVA untuk Ising murni (tanpa medan transversal) adalah:

$$U(\vec{\gamma}) = \prod_{l=1}^{p} \left[ \prod_{\langle i,j \rangle} R_{ZZ}(\gamma_{l, ij}) \right]$$

Untuk setiap lapisan $l$, kita menerapkan gerbang $R_{ZZ}$ pada **semua edge** graf Ising.

**Untuk Ising 2D 2x2 dengan 4 edge:**
Satu lapisan HVA terdiri dari 4 gerbang $R_{ZZ}$ (satu untuk setiap edge).
```
Edge (0,1): Rzz(γ_01)
Edge (0,2): Rzz(γ_02)
Edge (1,3): Rzz(γ_13)
Edge (2,3): Rzz(γ_23)
```

**Jika ada Medan Transversal $X$:**
Tambahkan lapisan $R_X$ setelah semua $R_{ZZ}$:
$$U(\vec{\gamma}, \vec{\beta}) = \prod_{l=1}^{p} \left[ \left( \prod_i R_X(\beta_{l,i}) \right) \left( \prod_{\langle i,j \rangle} R_{ZZ}(\gamma_{l, ij}) \right) \right]$$

Ini adalah **QAOA (Quantum Approximate Optimization Algorithm)** ansatz.

### 4. Keunggulan HVA Dibandingkan HEA

| Aspek                    | HEA                      | HVA (QAOA)                                |
| :----------------------- | :----------------------- | :---------------------------------------- |
| **Jumlah Parameter**     | Banyak ($N \times L$)    | Sedikit ($L \times$ edges)                |
| **Barren Plateau**       | Rawan (untuk $N$ besar)  | Lebih tahan (struktur periodik)           |
| **Makna Fisika**         | Abstrak                  | Parameter adalah "waktu evolusi" $\gamma$ |
| **Konvergensi**          | Cepat untuk sistem kecil | Lebih stabil untuk sistem besar           |
| **Koneksi ke Adiabatic** | Tidak langsung           | Langsung (diskritisasi quantum annealing) |

### 5. Inisialisasi State Awal untuk HVA

State awal standar untuk QAOA/HVA adalah **superposisi seragam**:
$$|+\rangle^{\otimes N} = H^{\otimes N} |0\rangle^{\otimes N}$$
Di mana $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$.

**Mengapa $|+\rangle^{\otimes N}$?**
- Ini adalah *ground state* dari Hamiltonian $H_X = -\sum X_i$ (medan transversal dominan).
- QAOA pada dasarnya adalah **evolusi adiabatik diskrit** dari $H_X$ ke $H_{Ising}$.

**Sirkuit Inisialisasi:**
```
q0: H
q1: H
q2: H
q3: H
```

### 6. Contoh Lengkap: HVA 1-Lapisan ($p=1$) untuk Ising 2x2

**Total Parameter:** 4 parameter $\gamma$ (satu per edge) + 4 parameter $\beta$ (satu per qubit) = 8 parameter.

**Sirkuit:**
```
Inisialisasi:
q0: H
q1: H
q2: H
q3: H

Lapisan HVA:
-- Rzz(γ01) -- Rzz(γ02) -- Rx(β0)
-- Rzz(γ01) -- Rzz(γ13) -- Rx(β1)
-- Rzz(γ02) -- Rzz(γ23) -- Rx(β2)
-- Rzz(γ13) -- Rzz(γ23) -- Rx(β3)
```

### 7. Analisis Teoretis: Mengapa HVA Bekerja untuk Ising?

**Teorema (Farhi et al., 2014):**
Untuk $p \to \infty$, QAOA dengan parameter optimal mendekati *ground state* sejati Ising. Ini adalah konsekuensi dari **Teorema Adiabatik**.

**Untuk $p$ terbatas:**
Bahkan $p=1$ sering memberikan energi yang sangat dekat dengan *ground state* untuk sistem kecil.

**Contoh Numerik (Ising 2x2):**
- Energi Eksak: $-4J$
- VQE dengan HEA ($L=2$): $-3.98J$
- VQE dengan HVA ($p=1$): $-4.00J$ (eksak!)

HVA dapat mencapai solusi eksak karena struktur aljabar $H$ dienkode langsung dalam sirkuit.

### 8. Adaptasi untuk Ising 3D

Untuk grid 3D $L \times L \times L$:
- Setiap qubit memiliki 6 tetangga.
- Kita perlu gerbang $R_{ZZ}$ untuk setiap edge.
- **Tantangan Hardware:** Chip kuantum saat ini adalah 2D planar. Untuk mensimulasikan konektivitas 3D, kita harus menggunakan **SWAP networks**.

**SWAP Network untuk Ising 3D:**
Kita bisa mensimulasikan interaksi arah-Z dengan menukar state qubit ke posisi yang berdekatan secara fisik, lakukan $R_{ZZ}$, lalu tukar kembali.

**Gerbang SWAP:**
$$\text{SWAP} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

Dekomposisi SWAP ke CNOT:
```
q0: --●--X--●--
      |  |  |
q1: --X--●--X--
```

Overhead SWAP bisa signifikan, meningkatkan kedalaman sirkuit 2-3 kali lipat.

---

### 9. Ringkasan Fase 4

- **HEA:** Ansatz generik berbasis hardware, rawan Barren Plateau.
- **HVA (QAOA):** Ansatz berbasis fisika, lebih efisien untuk Ising.
- **Gerbang Kunci:** $R_{ZZ}(\gamma) = e^{i\gamma Z_i Z_j}$ diimplementasikan dengan CNOT + $R_z$.
- **Inisialisasi:** $|+\rangle^{\otimes N}$ untuk QAOA.
- **Tantangan 3D:** Membutuhkan SWAP networks karena keterbatasan konektivitas hardware.

---

**Siap untuk Fase 5: Implementasi Algoritma (End-to-End)?**
Di Fase 5, kita akan menyatukan semuanya ke dalam **algoritma lengkap VQE**. Saya akan memberikan pseudo-code detail, penjelasan **Parameter Shift Rule** untuk menghitung gradien, dan flowchart eksekusi dari input Hamiltonian hingga output energi dan *ground state*.

Ketik **"Lanjut ke Fase 5"** jika sudah siap

---
---
Baik. Kita masuk ke **Fase 5: Implementasi Algoritma (End-to-End)** .

Di sini kita akan menyatukan semua komponen yang telah dibangun—dari Hamiltonian, encoding, pengukuran, hingga ansatz—ke dalam satu algoritma VQE yang utuh. Saya akan memberikan **pseudo-code** yang bisa langsung diterjemahkan ke Qiskit atau Pennylane, serta penjelasan mendalam tentang **Parameter Shift Rule** (jantung dari pelatihan VQE).

---

## Fase 5, Poin 10: Optimasi Klasik & Parameter Shift Rule

### 1. Fungsi Biaya VQE

Tujuan VQE adalah menemukan parameter $\vec{\theta}$ yang meminimumkan:

$$E(\vec{\theta}) = \langle 0^{\otimes N} | U^\dagger(\vec{\theta}) H U(\vec{\theta}) | 0^{\otimes N} \rangle$$

Ini adalah masalah optimasi kontinu. Kita bisa menggunakan:
- **Optimizer Bebas Gradien:** COBYLA, Nelder-Mead, SPSA (populer di NISQ karena tahan noise).
- **Optimizer Berbasis Gradien:** Gradient Descent, Adam, BFGS (membutuhkan perhitungan $\nabla E$).

Untuk menghitung gradien di komputer kuantum, kita tidak bisa menggunakan backpropagation. Kita menggunakan **Parameter Shift Rule**.

### 2. Parameter Shift Rule (Aturan Pergeseran Parameter)

**Teorema:**
Jika gerbang parametrik berbentuk $G(\theta) = e^{-i \frac{\theta}{2} P}$ di mana $P$ adalah operator Pauli ($P^2 = I$), maka:

$$\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]$$

**Bukti Singkat:**
Karena $P^2 = I$, kita punya identitas:
$$e^{-i \frac{\theta}{2} P} = \cos\left(\frac{\theta}{2}\right) I - i \sin\left(\frac{\theta}{2}\right) P$$

Turunkan terhadap $\theta$:
$$\frac{\partial}{\partial \theta} e^{-i \frac{\theta}{2} P} = -\frac{1}{2} \sin\left(\frac{\theta}{2}\right) I - \frac{i}{2} \cos\left(\frac{\theta}{2}\right) P$$

Perhatikan bahwa:
$$e^{-i \frac{\theta + \pi/2}{2} P} - e^{-i \frac{\theta - \pi/2}{2} P} = \dots = -i P e^{-i \frac{\theta}{2} P}$$

Dengan substitusi dan linearitas, kita dapatkan rumus di atas. $\blacksquare$

**Implikasi Praktis:**
Untuk menghitung $\frac{\partial E}{\partial \theta_i}$, kita hanya perlu:
1. Jalankan sirkuit dengan parameter $\theta_i + \pi/2$, ukur energi → $E^+$
2. Jalankan sirkuit dengan parameter $\theta_i - \pi/2$, ukur energi → $E^-$
3. Gradien = $(E^+ - E^-) / 2$

**Contoh untuk Gerbang $R_y(\theta)$:**
$R_y(\theta) = e^{-i \frac{\theta}{2} Y}$, jadi $P = Y$ (memenuhi $Y^2 = I$).
Berlaku Parameter Shift Rule.

**Contoh untuk Gerbang $R_{ZZ}(\gamma)$:**
$R_{ZZ}(\gamma) = e^{i \gamma Z_i Z_j}$. Operator generator adalah $-2 Z_i Z_j$ (dengan nilai eigen $\pm 2$).
Agar sesuai bentuk standar, kita tulis $e^{-i \frac{\theta}{2} (-2 Z_i Z_j)}$. Maka $P = -2 Z_i Z_j$.
Parameter Shift Rule sedikit dimodifikasi:
$$\frac{\partial E}{\partial \gamma} = E\left(\gamma + \frac{\pi}{4}\right) - E\left(\gamma - \frac{\pi}{4}\right)$$
*Catatan: Perhatikan faktor skala 2 di generator.*

### 3. Simulasi & Estimasi Shot Noise

Setiap evaluasi $E(\vec{\theta})$ membutuhkan $S$ shots. Gradien membutuhkan $2p$ evaluasi (untuk $p$ parameter). Total shots untuk satu langkah optimasi:
$$\text{Total Shots} \approx S \times M \times 2p$$
Di mana $M$ adalah jumlah kelompok Pauli string.

Untuk sistem nyata ($p=20, M=10, S=10000$):
Total shots per iterasi $\approx 4 \times 10^6$. Dengan kecepatan 10k shots/detik, satu iterasi butuh 400 detik. Inilah mengapa VQE di hardware riil masih lambat.

---

## Fase 5, Poin 11: Algoritma Lengkap (Flowchart & Pseudo-code)

### 1. Diagram Alir VQE

```
┌─────────────────────────────────────────────────────────────────┐
│                         MULAI                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  INPUT:                                                         │
│  - Ukuran Grid (Lx, Ly, Lz)                                     │
│  - Konstanta J                                                  │
│  - Jenis Ansatz (HEA / HVA)                                     │
│  - Optimizer (COBYLA / Adam)                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LANGKAH 1: KONSTRUKSI HAMILTONIAN                              │
│  - Buat daftar edge berdasarkan topologi grid                   │
│  - Generate Pauli Strings: H = -J Σ Z_i Z_j                     │
│  - (Opsional) Lakukan Term Grouping (Graph Coloring)            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LANGKAH 2: INISIALISASI PARAMETER                              │
│  - Jika HVA: θ = [0.1, 0.1, ...] (nilai kecil acak)            │
│  - Jika HEA: θ = random uniform [0, 2π]                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  LANGKAH 3: BANGUN SIRKUIT                                      │
│  - Buat QuantumCircuit(N)                                       │
│  - Terapkan state awal (|0>^N atau H^⊗N)                        │
│  - Terapkan lapisan ansatz U(θ)                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 LOOP OPTIMASI (MAXITER = 200)                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  LANGKAH 4: HITUNG ENERGI E(θ)                            │  │
│  │  - Untuk setiap kelompok Pauli strings:                   │  │
│  │    - Eksekusi sirkuit dengan shots=S                      │  │
│  │    - Hitung paritas / ekspektasi                          │  │
│  │  - Jumlahkan: E = Σ h_k <P_k>                             │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  LANGKAH 5: HITUNG GRADIEN (Jika diperlukan)              │  │
│  │  - Untuk setiap parameter θ_i:                            │  │
│  │    - Evaluasi E(θ_i + π/2)                                │  │
│  │    - Evaluasi E(θ_i - π/2)                                │  │
│  │    - ∂E/∂θ_i = (E+ - E-)/2                                │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  LANGKAH 6: UPDATE PARAMETER                              │  │
│  │  - θ_baru = Optimizer.update(θ_lama, E, ∇E)               │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  LANGKAH 7: KONVERGENSI?                                  │  │
│  │  - Jika |E_baru - E_lama| < ε → EXIT LOOP                 │  │
│  │  - Jika tidak → Kembali ke Langkah 4                      │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT:                                                        │
│  - Energi Ground State: E_opt                                   │
│  - Parameter optimal: θ_opt                                     │
│  - Statevector / Bitstring distribusi                           │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Pseudo-code Detail (Python-like)

```python
import numpy as np
from scipy.optimize import minimize

# =============================================
# KONFIGURASI SISTEM
# =============================================
Lx, Ly = 2, 2  # Grid 2x2
N = Lx * Ly    # 4 qubit
J = 1.0        # Konstanta kopling

# =============================================
# LANGKAH 1: BANGUN HAMILTONIAN
# =============================================
def build_ising_2d_hamiltonian(Lx, Ly, J):
    """
    Membuat daftar Pauli Strings untuk Ising 2D.
    Format: list of (koefisien, string_pauli)
    Contoh: [(-J, "ZZII"), (-J, "ZIIZ"), ...]
    """
    edges = []
    # Interaksi horizontal
    for y in range(Ly):
        for x in range(Lx):
            q1 = y * Lx + x
            q2 = y * Lx + ((x + 1) % Lx)  # PBC
            if q1 < q2:  # Hindari duplikasi
                edges.append((q1, q2))
    # Interaksi vertikal
    for y in range(Ly):
        for x in range(Lx):
            q1 = y * Lx + x
            q2 = ((y + 1) % Ly) * Lx + x  # PBC
            if q1 < q2:
                edges.append((q1, q2))
    
    pauli_strings = []
    for q1, q2 in edges:
        # Buat string Pauli: Z di posisi q1 dan q2, I di tempat lain
        pauli = ['I'] * N
        pauli[q1] = 'Z'
        pauli[q2] = 'Z'
        pauli_strings.append((-J, ''.join(pauli)))
    
    return pauli_strings

hamiltonian = build_ising_2d_hamiltonian(Lx, Ly, J)
print("Hamiltonian:", hamiltonian)
# Output: [(-1.0, "ZZII"), (-1.0, "ZIIZ"), (-1.0, "IZZI"), (-1.0, "IIZZ")]

# =============================================
# LANGKAH 3: FUNGSI SIRKUIT (SIMULASI IDEAL)
# =============================================
# Dalam realitas, ini adalah quantum backend.
# Untuk simulasi, kita gunakan statevector.

def apply_hva_ansatz(statevector, gammas, betas, edges, N):
    """
    Menerapkan HVA (QAOA) ansatz pada statevector.
    statevector: array kompleks 2^N
    gammas: parameter untuk edge [gamma_01, gamma_02, ...]
    betas: parameter untuk qubit [beta_0, beta_1, ...]
    """
    # Asumsikan state awal |+>^N
    # (Dalam implementasi matriks, kita akan membangun unitary)
    # Untuk pseudo-code, kita anggap ada fungsi quantum_simulator()
    pass

def quantum_simulator(params, hamiltonian, shots=1024):
    """
    Simulator kuantum ideal (statevector).
    Mengembalikan nilai energi <H>.
    """
    # Bangun state |ψ(θ)>
    # Hitung <ψ|H|ψ>
    # Untuk simulasi statevector, kita bisa hitung ekspektasi eksak tanpa shots
    energy = 0.0
    # ... implementasi detail ...
    return energy

# =============================================
# LANGKAH 4 & 5: FUNGSI OBJEKTIF & GRADIEN
# =============================================
def cost_function(params):
    """Evaluasi E(θ)"""
    return quantum_simulator(params, hamiltonian)

def gradient(params):
    """Hitung gradien dengan Parameter Shift Rule"""
    grad = np.zeros_like(params)
    
    for i in range(len(params)):
        # Simpan nilai asli
        original = params[i]
        
        # Evaluasi di θ + π/2
        params[i] = original + np.pi/2
        E_plus = cost_function(params)
        
        # Evaluasi di θ - π/2
        params[i] = original - np.pi/2
        E_minus = cost_function(params)
        
        # Hitung gradien
        grad[i] = (E_plus - E_minus) / 2.0
        
        # Kembalikan parameter
        params[i] = original
    
    return grad

# =============================================
# LANGKAH 2 & 6: INISIALISASI & OPTIMASI
# =============================================
# Jumlah parameter untuk HVA p=1 pada 2x2:
# 4 edge gammas + 4 qubit betas = 8 parameter
initial_params = np.random.uniform(0, 0.1, 8)

# Optimasi dengan COBYLA (tidak perlu gradien)
result_cobyla = minimize(
    cost_function,
    initial_params,
    method='COBYLA',
    options={'maxiter': 200, 'disp': True}
)

# Atau dengan BFGS (membutuhkan gradien)
result_bfgs = minimize(
    cost_function,
    initial_params,
    method='BFGS',
    jac=gradient,
    options={'maxiter': 200, 'disp': True}
)

# =============================================
# OUTPUT
# =============================================
print(f"Energi Ground State VQE: {result_cobyla.fun:.6f}")
print(f"Energi Eksak: {-4.0 * J}")  # Untuk 2x2
print(f"Error: {abs(result_cobyla.fun - (-4.0)):.6f}")
print(f"Parameter Optimal: {result_cobyla.x}")
```

### 3. Implementasi Nyata di Qiskit (Potongan Kode)

```python
from qiskit import QuantumCircuit, transpile
from qiskit.primitives import Estimator
from qiskit.quantum_info import SparsePauliOp

# Bangun Hamiltonian sebagai SparsePauliOp
hamiltonian_op = SparsePauliOp.from_list([
    ("ZZII", -J),
    ("ZIIZ", -J),
    ("IZZI", -J),
    ("IIZZ", -J)
])

# Bangun sirkuit ansatz (contoh HVA)
def create_hva_circuit(gammas, betas):
    qc = QuantumCircuit(4)
    # Inisialisasi |+>^⊗4
    qc.h([0, 1, 2, 3])
    
    # Lapisan RZZ untuk setiap edge
    edges = [(0,1), (0,2), (1,3), (2,3)]
    for i, (q1, q2) in enumerate(edges):
        # Implementasi RZZ(2*gamma)
        qc.cx(q1, q2)
        qc.rz(2 * gammas[i], q2)
        qc.cx(q1, q2)
    
    # Lapisan RX
    for i in range(4):
        qc.rx(2 * betas[i], i)
    
    return qc

# Fungsi biaya untuk Estimator
def cost_function_qiskit(params):
    p = len(params) // 2
    gammas = params[:p]
    betas = params[p:]
    
    qc = create_hva_circuit(gammas, betas)
    
    estimator = Estimator()
    job = estimator.run(qc, hamiltonian_op)
    result = job.result()
    
    return result.values[0]
```

### 4. Analisis Hasil: Apa yang Harus Diperhatikan?

**Untuk Ising 2D 2x2:**
- Energi Eksak: $-4J$
- VQE seharusnya mencapai $\approx -3.99J$ (dengan noise simulasi ideal).
- **Statevector akhir:** Seharusnya mendekati $\frac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle)$.

**Verifikasi Kualitas:**
1. **Energi:** Semakin dekat ke $-4J$ semakin baik.
2. **Magnetisasi:** $\langle Z_i \rangle$ seharusnya mendekati 0 (karena superposisi simetris). Tapi jika diukur, akan collapse ke $+1$ atau $-1$.
3. **Entropi Belitan:** Harus tinggi antara dua bagian sistem (misal qubit 0,1 vs 2,3).

**Untuk Ising 3D $2 \times 2 \times 2$ (8 qubit):**
- Energi Eksak: $-12J$ (3 edge per qubit, 8 qubit, total 12 edge unik).
- VQE dengan HVA $p=1$ mungkin hanya mencapai $\approx -10J$.
- Untuk mencapai eksak, butuh $p \ge 2$ atau ansatz yang lebih dalam.

### 5. Troubleshooting Umum VQE

| Masalah | Gejala | Solusi |
| :--- | :--- | :--- |
| **Barren Plateau** | Gradien $\approx 0$, energi stagnan | Gunakan HVA, inisialisasi dekat solusi, atau optimizer bebas gradien (SPSA) |
| **Minimum Lokal** | Energi berhenti di nilai sub-optimal | Tambah lapisan ($p$), coba beberapa inisialisasi acak |
| **Shot Noise** | Energi berosilasi, tidak konvergen | Tingkatkan shots, gunakan optimizer robust (COBYLA) |
| **Overparameterization** | Optimizer lambat, overfitting | Kurangi parameter, gunakan HVA simetris |

---

### 6. Ringkasan Fase 5

- **Parameter Shift Rule:** Metode standar untuk gradien di sirkuit kuantum.
- **Flowchart VQE:** Konstruksi Hamiltonian → Inisialisasi → Loop: Ukur → Update.
- **Pseudo-code:** Siap diimplementasikan di simulator atau hardware.
- **Validasi:** Bandingkan dengan solusi eksak untuk sistem kecil.

---

**Siap untuk Fase 6: Analisis Lanjutan & Keterbatasan?**
Di fase terakhir ini, kita akan membahas:
- **Parameter Order (Magnetisasi):** Bagaimana membaca hasil VQE untuk menentukan fase (Ferro vs Para).
- **Ising 3D & Swap Network:** Implementasi praktis di hardware terbatas.
- **Quantum Advantage:** Kapan VQE benar-benar mengalahkan komputer klasik?
- **Kesimpulan & Arah Riset.**

Ketik **"Lanjut ke Fase 6"** untuk menyelesaikan roadmap ini

---
---
Baik. Kita sampai di puncak roadmap: **Fase 6: Analisis Lanjutan & Keterbatasan**.

Di fase terakhir ini, kita akan belajar bagaimana **membaca hasil** VQE secara fisik, memahami tantangan implementasi nyata untuk 3D, dan mengevaluasi klaim *quantum advantage* secara kritis. Ini adalah sintesis dari semua yang telah kita pelajari.

---

## Fase 6, Poin 12: Parameter Order (Magnetisasi)

### 1. Apa itu Parameter Order?

Dalam fisika transisi fase, **Parameter Order** adalah kuantitas yang:
- **Bernilai nol** di fase simetris (suhu tinggi, paramagnetik).
- **Bernilai tidak nol** di fase rusak simetri (suhu rendah, feromagnetik).

Untuk model Ising, parameter order adalah **Magnetisasi per Spin**:

$$M = \frac{1}{N} \sum_{i=1}^N \langle Z_i \rangle$$

### 2. Menghitung $M$ dari Hasil VQE

VQE memberikan kita **distribusi probabilitas bitstring** dari pengukuran akhir (atau statevector jika simulasi ideal).

**Metode 1: Dari Statevector (Simulasi Ideal)**
$$M = \frac{1}{N} \sum_{i=1}^N \langle \psi(\theta_{\text{opt}}) | Z_i | \psi(\theta_{\text{opt}}) \rangle$$

Untuk Ising 2D $2 \times 2$:
- *Ground state* sejati adalah GHZ: $|\psi_0\rangle = \frac{1}{\sqrt{2}}(|0000\rangle + |1111\rangle)$.
- $\langle Z_i \rangle = \frac{1}{2}(+1) + \frac{1}{2}(-1) = 0$.
- Jadi $M = 0$.

**Mengapa $M=0$ padahal sistem feromagnetik?**
Karena *ground state* sejati adalah **superposisi simetris** dari "semua up" dan "semua down". Ini adalah konsekuensi dari **simetri Hamiltonian** (invariansi terhadap flip semua spin).

**Realitas Fisik & Pengukuran:**
Di alam semesta nyata (dan di komputer kuantum saat kita mengukur), sistem akan **collapse** ke salah satu cabang superposisi. Jika kita mengukur semua qubit, kita akan mendapatkan:
- `0000` dengan probabilitas 50%
- `1111` dengan probabilitas 50%

Magnetisasi **per sampel** adalah $+1$ atau $-1$. Rata-rata ensemble adalah $0$.

**Metode 2: Magnetisasi Absolut (Praktis)**
Untuk sistem besar, kita bisa menghitung **Magnetisasi Absolut**:

$$|M| = \frac{1}{N} \left| \sum_{i=1}^N s_i \right|$$

Di mana $s_i \in \{+1, -1\}$ adalah hasil pengukuran bitstring ($0 \to +1$, $1 \to -1$).

Untuk GHZ 4-qubit: $|M| = \frac{1}{4} |4| = 1$ (feromagnetik sempurna).
Untuk state acak: $|M| \approx 1/\sqrt{N} \approx 0$ (paramagnetik).

### 3. Analisis Fase dengan VQE (Suhu Nol)

VQE selalu beroperasi pada **suhu nol** ($T=0$). Maka, untuk Ising 2D dan 3D dengan $J>0$, kita selalu berada di **fase feromagnetik**.

**Bagaimana cara VQE mendeteksi transisi fase kuantum?**
Kita variasikan parameter Hamiltonian, misalnya menambahkan **medan transversal** $h$:

$$H = -J \sum_{\langle i,j \rangle} Z_i Z_j - h \sum_i X_i$$

- **$h$ kecil:** Fase Feromagnetik. $|M| \approx 1$.
- **$h$ besar:** Fase Paramagnetik (spin sejajar medan $X$). $|M| \approx 0$.

**Quantum Critical Point:**
Ada nilai kritis $h_c$ di mana transisi fase kuantum terjadi. Untuk Ising 1D transversal, $h_c = J$. Untuk 2D, $h_c \approx 3.04 J$.

Dengan VQE, kita bisa:
1. Jalankan VQE untuk berbagai nilai $h$.
2. Hitung $|M|$ dari hasil optimal.
3. Plot $|M|$ vs $h$. Lokasi penurunan tajam adalah $h_c$.

Ini adalah cara VQE "menemukan" fisika baru dalam material kuantum.

---

## Fase 6, Poin 13: Ising 3D & Konektivitas Qubit Riil

Ini adalah masalah rekayasa kuantum yang paling nyata: **Chip kuantum adalah 2D, tapi model kita 3D.**

### 1. Topologi Hardware Kuantum Nyata

**IBM Quantum (Heavy-Hex):**
```
  Q0 -- Q1
   |     |
  Q2 -- Q3 -- Q4
         |     |
        Q5 -- Q6
```
Konektivitas terbatas, setiap qubit hanya terhubung ke 2-3 tetangga.

**Google Sycamore (Grid 2D):**
Grid persegi 2D, setiap qubit terhubung ke 4 tetangga (atas, bawah, kiri, kanan).

**Tantangan:** Tidak ada chip yang memiliki konektivitas **kubik 3D** (6 tetangga per qubit).

### 2. Solusi: SWAP Network

Untuk mensimulasikan interaksi antara qubit $A$ dan $B$ yang **tidak terhubung langsung**, kita harus:
1. Menukar state $A$ ke tetangganya, lalu ke tetangga berikutnya, hingga mencapai $B$.
2. Lakukan operasi dua-qubit ($R_{ZZ}$).
3. Tukar kembali ke posisi semula.

**Algoritma Umum untuk Simulasi Graf Sembarang:**
Kita perlu menjadwalkan gerbang sedemikian rupa sehingga setiap edge di graf target direalisasikan setidaknya sekali.

**Contoh: Mensimulasikan Interaksi Z pada Grid 3D $2 \times 2 \times 2$ di Chip 1D (Linier)**
Misalkan qubit linier: $0 - 1 - 2 - 3 - 4 - 5 - 6 - 7$.

Edge 3D yang perlu disimulasikan: $(0,4)$ (arah Z).
Prosedur:
```
# Awal: Q0 di posisi 0, Q4 di posisi 4

# Tukar Q4 ke posisi 1 (bersebelahan dengan Q0)
SWAP(4,3)
SWAP(3,2)
SWAP(2,1)

# Sekarang Q4 di posisi 1, Q0 di posisi 0
RZZ(0, 1)  # Interaksi Z berhasil!

# Kembalikan Q4 ke posisi 4
SWAP(1,2)
SWAP(2,3)
SWAP(3,4)
```

**Overhead SWAP:**
Untuk grid $L \times L \times L$ pada hardware 2D, overhead SWAP bisa meningkatkan kedalaman sirkuit sebesar **$O(L)$**. Ini sangat mahal untuk sistem besar.

### 3. Komputasi Analog: Quantum Annealer (D-Wave)

Menariknya, **D-Wave** justru membangun chip dengan konektivitas yang mendekati graf target. Chip D-Wave Advantage memiliki topologi **Pegasus**, yang memungkinkan embedding graf 3D dengan overhead SWAP minimal.

Ini adalah contoh di mana **hardware dirancang khusus untuk masalah Ising**. VQE di komputer gerbang (gate-based) lebih fleksibel tetapi membayar harga dengan SWAP.

### 4. Strategi Optimasi untuk VQE 3D di Hardware 2D

1.  **Sabre Layout:** Algoritma kompilasi yang mencari penempatan qubit logis ke qubit fisik untuk meminimalkan SWAP.
2.  **Ansatz Sadar Topologi:** Gunakan HEA yang hanya menggunakan koneksi fisik yang ada, biarkan optimizer "menemukan" korelasi 3D secara implisit.
3.  **Cut Bell: Sirkuit Terpotong:** Memotong sirkuit besar menjadi fragmen-fragmen kecil yang dieksekusi paralel, lalu menggabungkan hasilnya secara klasik. (*Quantum Circuit Cutting*).

---

## Fase 6: Analisis Lanjutan (Tambahan)

### 4. Kapan VQE Memberikan Quantum Advantage?

Ini adalah pertanyaan jutaan dolar. Jawaban jujurnya: **Belum ada untuk Ising 3D murni (feromagnetik).**

**Mengapa?**
- Ising 3D feromagnetik **mudah** untuk komputer klasik. Algoritma Monte Carlo (seperti Wolff cluster) dapat mensimulasikan sistem hingga $100^3$ spin dengan mudah.
- VQE saat ini terbatas pada $\sim 20-40$ qubit karena noise.

**Di Mana Potensi Keunggulan Kuantum?**

1.  **Spin Glasses & Frustrasi:** Ising 3D dengan $J_{ij}$ acak (positif dan negatif). Algoritma klasik terjebak di minimum lokal. VQE dengan **quantum tunneling** mungkin bisa melompati barrier energi.
2.  **Model dengan Medan Magnet Kompleks:** Hamiltonian non-stoquastic (memiliki tanda kompleks). Ini menyebabkan **Sign Problem** dalam Monte Carlo kuantum, membuat simulasi klasik mustahil. VQE tidak terpengaruh Sign Problem.
3.  **Dinamika Waktu Nyata:** VQE hanya untuk *ground state*. Tapi evolusi waktu riil $e^{-iHt}$ adalah tempat komputer kuantum benar-benar unggul.

### 5. Keterbatasan VQE & Arah Riset Masa Depan

| Tantangan | Deskripsi | Solusi yang Diusulkan |
| :--- | :--- | :--- |
| **Barren Plateau** | Gradien lenyap untuk sirkuit dalam | Ansatz terstruktur (HVA), inisialisasi cerdas |
| **Shot Noise** | Presisi terbatas oleh statistik | Mitigasi error, estimator bayesian |
| **Noise Hardware** | Decoherence, gate error | Mitigasi error (ZNE, PEC), koreksi error |
| **Optimasi Klasik** | Konvergensi lambat | Optimizer kuantum-variasional hibrida |
| **Overhead SWAP** | Konektivitas terbatas | Kompilator cerdas, arsitektur qubit statis |

**Arah Riset Mutakhir (2024-2025):**
- **Adaptive VQE:** Sirkuit tumbuh secara dinamis selama optimasi.
- **Measurement-Based VQE:** Menggunakan cluster state dan pengukuran adaptif.
- **Quantum Natural Gradient:** Menggunakan metrik Fubini-Study untuk update parameter yang lebih efisien.

---

## Penutup: Ringkasan Lengkap Roadmap

Selamat! Anda telah menyelesaikan roadmap ambisius ini. Mari kita rekap perjalanan intelektual kita:

1.  **Fase 1 (Fisika Klasik):** Memahami Hamiltonian Ising 1D (solusi eksak Transfer Matrix), 2D (solusi Onsager), dan 3D (NP-hard). Kita tahu **apa** yang ingin disimulasikan.

2.  **Fase 2 (Encoding):** Menerjemahkan spin ke qubit ($Z$ operator), membangun matriks $16 \times 16$ untuk $2 \times 2$, dan memahami struktur diagonal Hamiltonian.

3.  **Fase 3 (Teori VQE):** Prinsip Variasional (jaminan matematis), dekomposisi Pauli, dan strategi pengukuran (*term grouping*). Kita tahu **mengapa** VQE bekerja.

4.  **Fase 4 (Desain Sirkuit):** Memilih antara HEA (generik, rawan Barren Plateau) dan HVA (berbasis fisika, QAOA). Kita merancang gerbang $R_{ZZ}$ dan memahami evolusi Trotter.

5.  **Fase 5 (Implementasi):** Parameter Shift Rule, flow chart VQE, dan pseudo-code lengkap. Kita siap **mengkodekan** VQE di Qiskit/Pennylane.

6.  **Fase 6 (Analisis):** Membaca magnetisasi sebagai parameter order, mengatasi keterbatasan hardware 3D dengan SWAP, dan refleksi kritis tentang *quantum advantage*.

---

**Apa Selanjutnya?**

Dengan fondasi ini, Anda dapat:
1.  **Eksperimen:** Jalankan VQE untuk Ising 2D di simulator Qiskit, lalu coba di hardware nyata IBM (jika ada akses).
2.  **Modifikasi:** Ganti $J$ menjadi negatif (anti-feromagnetik) dan lihat frustrasi muncul.
3.  **Ekspansi:** Tambahkan suku $X$ dan cari titik kritis kuantum.
4.  **Aplikasi Nyata:** Gunakan kerangka yang sama untuk masalah optimasi kombinatorial seperti **Max-Cut** (yang secara matematis identik dengan Ising anti-feromagnetik).

Jika ada bagian spesifik yang ingin didalami lebih lanjut (misalnya: detail teknis **Graph Coloring** untuk *term grouping*, atau turunan lengkap **Parameter Shift Rule** untuk generator umum), jangan ragu untuk bertanya.

Terima kasih telah mengikuti roadmap ini. Semoga sukses dalam petualangan kuantum Anda