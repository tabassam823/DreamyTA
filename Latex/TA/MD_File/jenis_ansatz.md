# Real Amplitudes

`RealAmplitudes` adalah ansatz heuristik yang secara khusus dirancang untuk menghasilkan state quantum dengan amplitudo bernilai real. Hal ini sangat berguna untuk masalah di mana ground state Hamiltonian diketahui bersifat real (misalnya dalam banyak sistem kimia kuantum).

### 1. Karakteristik Utama: Amplitudo Real
Secara matematis, state $|\psi\rangle$ memiliki amplitudo real jika dalam basis komputasi, ia dapat dinyatakan sebagai:
$$|\psi\rangle = \sum_{i=0}^{2^n-1} c_i |i\rangle, \quad c_i \in \mathbb{R}$$

Ansatz ini menjamin kondisi tersebut dengan hanya menggunakan:
1.  **Gerbang Rotasi-Y ($R_y$)**: Karena matriks $R_y(\theta)$ hanya berisi elemen bilangan real.
    $$R_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$
2.  **Gerbang CNOT ($CX$)**: Karena matriks $CX$ juga hanya berisi elemen bilangan real (0 dan 1).

### 2. Struktur Layer
Sama seperti `EfficientSU2`, sirkuit ini terdiri dari repetisi layer rotasi dan keterbelitan:
$$|\psi(\theta)\rangle = L_d(\theta_d) \prod_{i=0}^{d-1} [W_i L_i(\theta_i)] |0\rangle^{\otimes n}$$

**Perbedaan Spesifik:**
*   **Layer Rotasi ($L_i$)**: Hanya menggunakan gerbang $R_y$.
    $$L_i(\theta_i) = \bigotimes_{j=0}^{n-1} R_y(\theta_{i,j})$$
*   **Layer Keterbelitan ($W_i$)**: Menggunakan gerbang $CX$ dengan pola seperti *Linear*, *Circular*, atau *Full*.

### 3. Perbandingan dengan EfficientSU2
| Fitur                | RealAmplitudes             | EfficientSU2 (Default)    |
| :------------------- | :------------------------- | :------------------------ |
| **Gerbang Rotasi**   | $R_y$                      | $R_y$ dan $R_z$           |
| **Amplitudo**        | Selalu Real ($\mathbb{R}$) | Kompleks ($\mathbb{C}$)   |
| **Jumlah Parameter** | $n \times (d+1)$           | $n \times 2 \times (d+1)$ |
| **Kegunaan**         | Kimia (Hamiltonian Real)   | Umum / ML                 |

### 4. Keunggulan dalam Optimasi
1.  **Efisiensi Parameter**: Karena hanya menggunakan satu jenis gerbang rotasi ($R_y$), jumlah parameter yang perlu dioptimasi menjadi setengah dari `EfficientSU2`. Hal ini mempercepat konvergensi algoritma optimasi.
2.  **Kesesuaian Fisika**: Banyak masalah kimia kuantum (seperti mencari energi molekul) memiliki fungsi gelombang yang dapat direpresentasikan dengan amplitudo real tanpa kehilangan akurasi fisik.
3.  **Pengurangan Noise**: Dengan parameter yang lebih sedikit dan sirkuit yang lebih sederhana, akumulasi error sistematis pada hardware kuantum NISQ dapat ditekan.
# Pauli Two Design

`PauliTwoDesign` adalah jenis ansatz khusus yang dirancang untuk meniru properti statistik dari distribusi unitari acak (Haar measure) hingga momen kedua. Ansatz ini sangat penting dalam riset *Expressibility* dan masalah *Barren Plateaus*.

### 1. Konsep "2-Design"
Secara matematis, sebuah sirkuit parameterisasi $U(\theta)$ disebut **2-design** jika rata-rata dari sirkuit tersebut mendekati rata-rata distribusi Haar untuk polinomial derajat 2:
$$\int_{Haar} (U \otimes U) dU \approx \int_{\theta} (U(\theta) \otimes U(\theta)) d\theta$$

Hal ini berarti ansatz ini sangat **ekspresif** dan dapat menjelajahi ruang Hilbert secara merata, menyerupai sirkuit acak murni.

### 2. Struktur Sirkuit
`PauliTwoDesign` memiliki struktur yang unik dibandingkan ansatz heuristik lainnya:
1.  **Initial Layer**: Dimulai dengan gerbang $\sqrt{H}$ (ekuivalen dengan $R_y(\pi/4)$) pada setiap qubit.
2.  **Repetition Blocks** ($d$ kali):
    *   **Rotation Layer**: Menggunakan gerbang rotasi Pauli ($RX, RY,$ atau $RZ$). Yang unik di sini adalah sumbu rotasi untuk setiap qubit dipilih secara acak (tetapi tetap parameterisasi).
    *   **Entanglement Layer**: Menggunakan gerbang **CZ** (Controlled-Z) yang disusun secara berpasangan dengan kedalaman 2 (staggered pattern).

### 3. Karakteristik & Properti
*   **Expressibility**: Sangat tinggi. Karena sifat 2-design, ia dapat merepresentasikan hampir semua bagian dari ruang Hilbert.
*   **Entangling Capability**: Kuat. Penggunaan gerbang CZ dalam pola tertentu memungkinkan pembentukan keterbelitan yang kompleks dengan cepat.
*   **Hardware Efficiency**: Sedikit lebih rendah dari `RealAmplitudes` karena penggunaan gerbang CZ (tergantung arsitektur hardware).

### 4. Hubungan dengan Barren Plateaus
Karena `PauliTwoDesign` mendekati distribusi Haar (2-design), ia secara teoretis rentan terhadap fenomena **Barren Plateaus**.
*   **Barren Plateau**: Fenomena di mana gradien fungsi biaya $\partial E / \partial \theta$ menjadi nol secara eksponensial seiring bertambahnya jumlah qubit $n$.
*   Ansatz ini sering digunakan sebagai **benchmark** untuk mempelajari bagaimana cara menghindari barren plateaus atau untuk menguji performa optimizer pada landscape energi yang sangat datar.

### 5. Penggunaan
*   **Quantum Machine Learning (QML)**: Sebagai model generatif yang ekspresif.
*   **Variational Quantum Eigensolver (VQE)**: Digunakan ketika struktur ground state sama sekali tidak diketahui dan kita memerlukan ansatz yang dapat menjangkau seluruh ruang Hilbert (global search).
# Two Local

`TwoLocal` adalah kerangka kerja (*framework*) umum dalam Qiskit untuk membangun ansatz heuristik yang terdiri dari layer rotasi satu-qubit dan layer keterbelitan dua-qubit. Sebenarnya, `RealAmplitudes` dan `EfficientSU2` adalah bentuk khusus dari `TwoLocal`.
	
### 1. Definisi Matematis
Secara umum, sebuah sirkuit `TwoLocal` didefinisikan sebagai urutan operator unitari:
$$U(\theta) = \left( \prod_{i=1}^{d} W_i(\theta_{W,i}) L_i(\theta_{L,i}) \right) L_0(\theta_{L,0})$$

Di mana:
*   $L_i$: **Rotation Layer**, kumpulan gerbang satu-qubit (misal $RX, RY, RZ$).
*   $W_i$: **Entanglement Layer**, kumpulan gerbang dua-qubit (misal $CX, CZ, CRZ$).
*   $d$: **Repetitions ($reps$)**, jumlah pengulangan blok.

### 2. Fleksibilitas Kustomisasi
Kekuatan utama `TwoLocal` adalah kemampuannya untuk dikonfigurasi secara bebas:
1.  **Rotation Blocks**: Kita bisa memilih satu atau lebih gerbang rotasi (misal `['ry', 'rz']`).
2.  **Entanglement Blocks**: Kita bisa memilih gerbang keterbelitan apa pun (misal `cx`, `cz`, atau bahkan gerbang parameterisasi seperti `crz`).
3.  **Entanglement Strategy**: Menentukan bagaimana qubit saling terhubung (Linear, Full, Circular, atau kustom).

### 3. Hubungan dengan Ansatz Lain
| Nama Ansatz        | Konfigurasi `TwoLocal`                                     |
| :----------------- | :--------------------------------------------------------- |
| **RealAmplitudes** | `rotation_blocks='ry'`, `entanglement_blocks='cx'`         |
| **EfficientSU2**   | `rotation_blocks=['ry', 'rz']`, `entanglement_blocks='cx'` |

### 4. Mekanisme Optimasi
Karena `TwoLocal` adalah bentuk umum, ia mewarisi semua properti optimasi dari ansatz heuristik lainnya:
*   **Landscape Energi**: Bergantung pada jenis gerbang dan jumlah repetisi $d$. Semakin besar $d$, semakin ekspresif sirkuitnya, namun landscape energinya menjadi lebih kompleks (banyak local minima).
*   **Barren Plateaus**: Jika jumlah qubit $n$ besar dan sirkuit terlalu dalam, gradien bisa menghilang.
*   **Parameter Counting**: Jumlah total parameter dihitung sebagai:
    $$\text{Params} = n \times (\text{jumlah gerbang rotasi}) \times (d + 1)$$

### 5. Penggunaan dalam VQE
`TwoLocal` sering digunakan sebagai titik awal ketika kita ingin bereksperimen dengan berbagai kombinasi gerbang untuk menemukan ansatz yang paling cocok dengan sistem fisik yang sedang dipelajari. Misalnya, untuk sistem dengan interaksi spin-Z, kita mungkin lebih memilih `entanglement_blocks='cz'`.
# Efficient SU(2)

`EfficientSU2` adalah ansatz heuristik yang dirancang untuk meminimalkan *gate depth* dan *gate count* pada hardware kuantum NISQ. Secara matematis, ia mencoba mengonstruksi operator unitari $U(\theta)$ yang cukup ekspresif untuk mencakup bagian dari ruang Hilbert yang mengandung ground state Hamiltonian $H$.

### 1. Konstruksi Matematis
Ansatz ini didefinisikan sebagai urutan layer rotasi $L$ dan layer keterbelitan $W$ yang diulang sebanyak $d$ kali (*reps*):
$$|\psi(\theta)\rangle = U(\theta) |0\rangle^{\otimes n} = L_d(\theta_d) \prod_{i=0}^{d-1} [W_i L_i(\theta_i)] |0\rangle^{\otimes n}$$

### 2. Layer Rotasi ($L_i$)
Setiap layer rotasi terdiri dari gerbang SU(2) parameterisasi yang diaplikasikan pada setiap qubit secara independen. Secara default, Qiskit menggunakan kombinasi gerbang $R_y$ dan $R_z$:
$$L_i(\theta_i) = \bigotimes_{j=0}^{n-1} R_z(\theta_{i,j,2}) R_y(\theta_{i,j,1})$$
Di mana:
- $n$: Jumlah qubit.
- $\theta_{i,j,1}$: Parameter sudut untuk gerbang $R_y$ pada layer $i$ dan qubit $j$.
- $\theta_{i,j,2}$: Parameter sudut untuk gerbang $R_z$ pada layer $i$ dan qubit $j$.

Grup $SU(2)$ dipilih karena kemampuannya untuk melakukan rotasi sembarang pada bola Bloch, yang secara matematis mencakup semua transformasi unitari 2x2 dengan determinan 1.

### 3. Layer Keterbelitan ($W_i$)
Layer ini menggunakan gerbang dua-qubit (biasanya $CX$ atau $CNOT$) tanpa parameter untuk menciptakan korelasi antar qubit. Pola keterbelitan ditentukan oleh konfigurasi:
*   **Linear**: $W = \prod_{j=0}^{n-2} CX_{j, j+1}$ (Hanya menghubungkan qubit tetangga).
*   **Circular**: $W = CX_{n-1, 0} \prod_{j=0}^{n-2} CX_{j, j+1}$ (Menghubungkan qubit terakhir kembali ke pertama).
*   **Full**: Menghubungkan setiap pasang qubit $(j, k)$ yang unik.

### 4. Mekanisme Optimasi
Tujuan utama adalah menemukan set parameter $\theta^*$ sedemikian rupa sehingga:
$$\theta^* = \arg\min_{\theta} \langle \psi(\theta) | H | \psi(\theta) \rangle$$

**Kelebihan Matematis:**
1.  **Hardware Efficiency**: Karena strukturnya mengikuti topologi qubit fisik (seperti pola linear), noise akibat gerbang dua-qubit dapat diminimalisir.
2.  **Expressibility**: Dengan meningkatkan $d$, ansatz dapat menjangkau area yang lebih luas di ruang Hilbert, meningkatkan probabilitas menemukan energi terendah yang akurat.
3.  **Diferensial**: Fungsi energi $E(\theta)$ terhadap parameter $\theta$ bersifat kontinu dan mulus, memungkinkan penggunaan algoritma optimasi berbasis gradien.

*Catatan: Meskipun kuat, penambahan repetisi $d$ yang terlalu besar dapat menyebabkan masalah **Barren Plateaus**, di mana gradien fungsi biaya menjadi nol secara eksponensial terhadap jumlah qubit.*
