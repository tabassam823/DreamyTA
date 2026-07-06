# Gerbang Rotasi dalam VQE Ansatz

Dalam Variational Quantum Eigensolver (VQE), ansatz sering kali dibangun menggunakan gerbang rotasi parameterisasi. Gerbang-gerbang ini memungkinkan kita untuk menjelajahi ruang Hilbert dengan mengubah parameter sudut $\theta$.

## 1. RX Gate ($R_X$)

Gerbang $R_X$ melakukan rotasi qubit di sekitar sumbu X pada bola Bloch.

### Definisi Matematis
Secara operator, gerbang ini didefinisikan sebagai eksponensial dari matriks Pauli-X:
$$R_X(\theta) = \exp\left(-i \frac{\theta}{2} X\right) = \cos\left(\frac{\theta}{2}\right)I - i\sin\left(\frac{\theta}{2}\right)X$$

### Representasi Matriks
$$R_X(\theta) = \begin{pmatrix} \cos(\frac{\theta}{2}) & -i\sin(\frac{\theta}{2}) \\ -i\sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2}) \end{pmatrix}$$

### Contoh
Jika kita memberikan input state $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ dan rotasi $\theta = \pi$:
$$R_X(\pi) |0\rangle = \begin{pmatrix} \cos(\frac{\pi}{2}) & -i\sin(\frac{\pi}{2}) \\ -i\sin(\frac{\pi}{2}) & \cos(\frac{\pi}{2}) \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ -i \end{pmatrix} = -i|1\rangle$$

---

## 2. RY Gate ($R_Y$)

Gerbang $R_Y$ melakukan rotasi qubit di sekitar sumbu Y. Gerbang ini sangat penting dalam VQE kimia kuantum karena menghasilkan amplitudo real.

### Definisi Matematis
$$R_Y(\theta) = \exp\left(-i \frac{\theta}{2} Y\right) = \cos\left(\frac{\theta}{2}\right)I - i\sin\left(\frac{\theta}{2}\right)Y$$

### Representasi Matriks
$$R_Y(\theta) = \begin{pmatrix} \cos(\frac{\theta}{2}) & -\sin(\frac{\theta}{2}) \\ \sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2}) \end{pmatrix}$$

### Contoh
Jika kita memberikan input state $|0\rangle$ dan rotasi $\theta = \pi/2$:
$$R_Y(\pi/2) |0\rangle = \begin{pmatrix} \cos(\pi/4) & -\sin(\pi/4) \\ \sin(\pi/4) & \cos(\pi/4) \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} = |+\rangle$$

---

## 3. RZ Gate ($R_Z$)

Gerbang $R_Z$ melakukan rotasi qubit di sekitar sumbu Z, yang secara fisik mengubah fase relatif antara $|0\rangle$ dan $|1\rangle$.

### Definisi Matematis
$$R_Z(\phi) = \exp\left(-i \frac{\phi}{2} Z\right)$$

### Representasi Matriks
$$R_Z(\phi) = \begin{pmatrix} e^{-i\phi/2} & 0 \\ 0 & e^{i\phi/2} \end{pmatrix}$$

*Catatan: Gerbang ini sering diimplementasikan secara "virtual" dalam hardware karena hanya melibatkan pergeseran fase.*

### Contoh
Jika kita memberikan input state $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ dan rotasi $\phi = \pi$:
$$R_Z(\pi) |+\rangle = \begin{pmatrix} e^{-i\pi/2} & 0 \\ 0 & e^{i\pi/2} \end{pmatrix} \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix} = \begin{pmatrix} -i/\sqrt{2} \\ i/\sqrt{2} \end{pmatrix} = -i \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = -i|-\rangle$$

---

## 4. U Gate (Universal Single-Qubit Gate)

Gerbang $U$ adalah bentuk paling umum dari rotasi satu qubit. Semua gerbang satu qubit lainnya ($RX, RY, RZ, H$) dapat diturunkan dari gerbang ini.

### Representasi Matriks
$$U(\theta, \phi, \lambda) = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i(\phi+\lambda)}\cos(\theta/2) \end{pmatrix}$$

*   $\theta$: Rotasi sumbu-Y.
*   $\phi, \lambda$: Rotasi sumbu-Z (fase).

### Contoh
Jika kita menggunakan parameter $\theta = \pi/2, \phi = 0, \lambda = \pi$:
$$U(\pi/2, 0, \pi) = \begin{pmatrix} \cos(\pi/4) & -e^{i\pi}\sin(\pi/4) \\ e^0\sin(\pi/4) & e^{i\pi}\cos(\pi/4) \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} \end{pmatrix}$$
*Hasil ini identik dengan Gerbang Hadamard ($H$).*

---

## 5. I Gate (Identity Gate)
Gerbang ini tidak mengubah state qubit (idle cycle).

### Representasi Matriks
$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

### Contoh
$$I |1\rangle = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |1\rangle$$

---

## 6. Hadamard Gate ($H$)
Gerbang ini menciptakan superposisi dengan memutar $\pi$ di sekitar sumbu $X+Z$.

### Representasi Matriks
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

### Contoh
Mentransformasi basis komputasi $|0\rangle$ menjadi $|+\rangle$:
$$H |0\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = |+\rangle$$

---

## 7. Entangling Gates (Gerbang Keterbelitan)

Dalam VQE, gerbang dua qubit digunakan untuk menciptakan korelasi antar qubit (entanglement).

### A. CX Gate (Controlled-NOT / CNOT)
Gerbang ini membalikkan (X) target qubit jika control qubit bernilai $|1\rangle$.

**Representasi Matriks:**
$$CX = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

**Contoh:**
Jika input adalah $|10\rangle = |1\rangle \otimes |0\rangle$:
$$CX |10\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = |11\rangle$$

### B. CZ Gate (Controlled-Z)
Gerbang ini memberikan fase $-1$ (Z) pada target qubit jika control qubit bernilai $|1\rangle$. Gerbang ini simetris.

**Representasi Matriks:**
$$CZ = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$$

**Contoh:**
Jika input adalah $|11\rangle$:
$$CZ |11\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ -1 \end{pmatrix} = -|11\rangle$$

### C. CY Gate (Controlled-Y)
Gerbang ini menerapkan gerbang Pauli-Y pada target qubit jika control qubit bernilai $|1\rangle$.

**Representasi Matriks:**
$$CY = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & 1 & 0 \\ 0 & i & 0 & 0 \end{pmatrix}$$

**Contoh:**
Jika input adalah $|10\rangle$:
$$CY |10\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -i \\ 0 & 0 & 1 & 0 \\ 0 & i & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ i \end{pmatrix} = i|11\rangle$$
*Target qubit berubah dari $|0\rangle$ ke $|1\rangle$ dengan tambahan fase kompleks $i$.*

---

# Struktur VQE Ansatz

Secara umum, sebuah ansatz VQE dibangun dari blok-blok berikut:

1.  **Rotation Layer**: Menggunakan gerbang $R_Y(\theta)$ atau $R_X(\theta)$ untuk memutar basis qubit.
2.  **Entanglement Layer**: Menggunakan gerbang $CX$ atau $CZ$ untuk menghubungkan qubit-qubit tersebut.
3.  **Repetitions ($d$)**: Mengulangi kedua layer di atas sebanyak $d$ kali untuk meningkatkan kedalaman sirkuit dan fleksibilitas ansatz.

---

# Efficient SU(2) Ansatz

`EfficientSU2` adalah jenis ansatz *hardware-efficient* yang sangat populer dalam VQE. Desainnya dioptimalkan agar sirkuit tetap dangkal (*shallow*) namun memiliki kapasitas ekspresi yang tinggi, sehingga cocok untuk era NISQ (*Noisy Intermediate-Scale Quantum*).

## 1. Karakteristik SU(2)
Grup $SU(2)$ adalah grup unitari khusus berdimensi 2. Dalam komputasi kuantum, ini berarti sirkuit hanya menggunakan gerbang rotasi satu qubit (seperti $R_Y$ dan $R_Z$) dan gerbang entangling (biasanya $CX$).

## 2. Struktur Layer
Sirkuit ini dibangun dengan pola:
1.  **Initial Rotation Layer**: Semua qubit diberi gerbang rotasi awal (misal $R_Y$).
2.  **Repetition Blocks** (sebanyak $d$ kali):
    *   **Entanglement Layer**: Menghubungkan qubit menggunakan pola tertentu.
    *   **Rotation Layer**: Memberikan rotasi parameterisasi baru pada setiap qubit.

## 3. Pola Entanglement (Keterbelitan)
Qiskit menyediakan beberapa pola standar untuk menghubungkan qubit:
*   **Linear**: Qubit $i$ terhubung ke $i+1$ (paling hemat gate).
*   **Circular**: Seperti linear, tapi qubit terakhir terhubung kembali ke qubit pertama.
*   **Full**: Setiap qubit terhubung ke semua qubit lainnya (ekspresi tinggi, tapi sirkuit sangat dalam).

## 4. Perhitungan Parameter
Jumlah parameter sudut ($\theta$) yang perlu dioptimasi bergantung pada jumlah qubit ($n$), jumlah repetisi ($r$), dan jumlah jenis gerbang rotasi per qubit ($k$).

**Rumus:**
$$\text{Total Parameter} = n \times k \times (r + 1)$$

*Contoh:*
Jika kita menggunakan 4 qubit, 3 repetisi, dengan gerbang `su2_gates=['ry', 'rz']` ($k=2$):
$$\text{Total Parameter} = 4 \times 2 \times (3 + 1) = 32 \text{ parameter}$$

---

# Optimasi dan Gradien

Tujuan utama VQE adalah meminimalkan nilai ekspektasi Hamiltonian $H$.

## 1. Prinsip Variasional
Nilai energi yang dihitung dari ansatz selalu merupakan batas atas dari energi ground state $E_0$:
$$E(\theta) = \frac{\langle \psi(\theta) | H | \psi(\theta) \rangle}{\langle \psi(\theta) | \psi(\theta) \rangle} \geq E_0$$

Dalam VQE, kita berasumsi state ternormalisasi, sehingga:
$$E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle$$

## 2. Parameter Shift Rule (Gradien)
Untuk mengoptimalkan $\theta$ menggunakan algoritma berbasis gradien (seperti Gradient Descent), kita perlu menghitung turunan $E(\theta)$. Pada hardware kuantum, kita tidak bisa menggunakan backpropagation biasa. Kita menggunakan **Parameter Shift Rule**.

Untuk gerbang rotasi Pauli ($RX, RY, RZ$), turunannya adalah:
$$\frac{\partial E}{\partial \theta} = \frac{1}{2} \left[ E\left(\theta + \frac{\pi}{2}\right) - E\left(\theta - \frac{\pi}{2}\right) \right]$$

**Langkah-langkah:**
1.  Jalankan sirkuit dengan parameter $\theta$ yang digeser $+\pi/2$, ukur energinya.
2.  Jalankan sirkuit dengan parameter $\theta$ yang digeser $-\pi/2$, ukur energinya.
3.  Hitung selisihnya dan bagi dua untuk mendapatkan nilai gradien yang eksak.

Hal ini memungkinkan optimasi parameter ansatz secara efisien langsung di hardware kuantum.
