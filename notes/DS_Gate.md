Baik, kita mulai dari **Modul 1: Fondasi Aljabar Linier Kompleks**.

---

## Modul 1: Ruang Vektor Kompleks $\mathbb{C}^2$ dan Notasi Dirac

### 1.1 Vektor Basis Standar dalam Notasi Dirac

Dalam komputasi kuantum, keadaan sistem 2-level (qubit) direpresentasikan dalam ruang Hilbert $\mathcal{H} \cong \mathbb{C}^2$. Basis standar yang digunakan adalah **basis komputasi**:

$$
|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

Vektor keadaan umum $|\psi\rangle$ adalah kombinasi linear kompleks:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha, \beta \in \mathbb{C}
$$

dengan syarat normalisasi $\langle\psi|\psi\rangle = 1$.

---

### 1.2 Definisi Bra sebagai Conjugate Transpose (Hermitian Adjoint)

**Bra** $\langle\psi|$ didefinisikan sebagai **conjugate transpose** dari ket $|\psi\rangle$:

$$
\langle\psi| = (|\psi\rangle)^\dagger = \begin{pmatrix} \alpha^* & \beta^* \end{pmatrix}
$$

**Sifat-sifat fundamental:**

1. **Konjugat skalar:**
   $$
   (c|\psi\rangle)^\dagger = c^* \langle\psi|
   $$

2. **Adjoint dari penjumlahan:**
   $$
   (|\psi\rangle + |\phi\rangle)^\dagger = \langle\psi| + \langle\phi|
   $$

---

### 1.3 Inner Product dalam $\mathbb{C}^2$

**Definisi:** Untuk dua vektor $|\psi\rangle = \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}$ dan $|\phi\rangle = \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}$, inner product didefinisikan sebagai:

$$
\boxed{\langle\phi|\psi\rangle = \alpha_2^* \alpha_1 + \beta_2^* \beta_1}
$$

**Pembuktian bahwa ini adalah inner product yang valid:**

#### Aksioma 1: Sesqui-linearity (Linear di argumen kedua, konjugat-linear di pertama)

Ambil $|\psi\rangle = c_1|\psi_1\rangle + c_2|\psi_2\rangle$:

$$
\langle\phi|\psi\rangle = \langle\phi|(c_1|\psi_1\rangle + c_2|\psi_2\rangle) = c_1\langle\phi|\psi_1\rangle + c_2\langle\phi|\psi_2\rangle \quad \checkmark
$$

Ambil $|\phi\rangle = d_1|\phi_1\rangle + d_2|\phi_2\rangle$:

$$
\langle\phi|\psi\rangle = (d_1^*\langle\phi_1| + d_2^*\langle\phi_2|)|\psi\rangle = d_1^*\langle\phi_1|\psi\rangle + d_2^*\langle\phi_2|\psi\rangle \quad \checkmark
$$

#### Aksioma 2: Conjugate Symmetry

$$
\langle\phi|\psi\rangle^* = (\alpha_2^*\alpha_1 + \beta_2^*\beta_1)^* = \alpha_2\alpha_1^* + \beta_2\beta_1^* = \alpha_1^*\alpha_2 + \beta_1^*\beta_2 = \langle\psi|\phi\rangle \quad \checkmark
$$

#### Aksioma 3: Positive Definiteness

$$
\langle\psi|\psi\rangle = |\alpha|^2 + |\beta|^2 \ge 0
$$

dan $\langle\psi|\psi\rangle = 0 \iff \alpha = \beta = 0 \iff |\psi\rangle = \mathbf{0} \quad \checkmark$

---

### 1.4 Outer Product dan Operator Proyeksi

**Definisi Outer Product:**

$$
|\psi\rangle\langle\phi| = \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix} \begin{pmatrix} \alpha_2^* & \beta_2^* \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2^* & \alpha_1\beta_2^* \\ \beta_1\alpha_2^* & \beta_1\beta_2^* \end{pmatrix}
$$

Ini adalah **matriks** (operator) yang bekerja pada vektor.

**Contoh penting - Operator proyeksi basis:**

$$
|0\rangle\langle 0| = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}
$$

$$
|1\rangle\langle 1| = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}
$$

Perhatikan bahwa $|0\rangle\langle 0| + |1\rangle\langle 1| = I$ (Kelengkapan/Completeness relation).

---

### 1.5 Definisi Matriks Uniter

Sebuah matriks $U \in \mathbb{C}^{n \times n}$ disebut **uniter** jika:

$$
\boxed{U^\dagger U = U U^\dagger = I}
$$

di mana $U^\dagger = (U^*)^T$ adalah **conjugate transpose**.

**Sifat-sifat penting matriks uniter:**

1. **Kekekalan Inner Product:**
   $$
   \langle U\phi | U\psi \rangle = \langle\phi|U^\dagger U|\psi\rangle = \langle\phi|I|\psi\rangle = \langle\phi|\psi\rangle
   $$

2. **Kekekalan Norm:**
   $$
   \|U|\psi\rangle\|^2 = \langle\psi|U^\dagger U|\psi\rangle = \langle\psi|\psi\rangle = \|\psi\|^2
   $$

3. **Determinan:** $|\det(U)| = 1$

4. **Nilai Eigen:** Semua nilai eigen $\lambda$ dari $U$ memenuhi $|\lambda| = 1$, yaitu $\lambda = e^{i\theta}$.

5. **Kolom dan Baris Orthonormal:**
   - Kolom-kolom $U$ membentuk basis ortonormal.
   - Baris-baris $U$ membentuk basis ortonormal.

---

### 1.6 Dekomposisi Umum Matriks Uniter $2 \times 2$

**Teorema:** Setiap matriks uniter $2 \times 2$ dapat ditulis dalam bentuk:

$$
\boxed{U = e^{i\alpha} \begin{pmatrix} a & b \\ -b^* e^{i\phi} & a^* e^{i\phi} \end{pmatrix}}
$$

dengan $|a|^2 + |b|^2 = 1$ dan $\alpha, \phi \in \mathbb{R}$.

**Penurunan:**

Misalkan $U = \begin{pmatrix} u_{11} & u_{12} \\ u_{21} & u_{22} \end{pmatrix}$. Syarat $U^\dagger U = I$ memberikan:

1. **Normalisasi kolom 1:** $|u_{11}|^2 + |u_{21}|^2 = 1$
2. **Normalisasi kolom 2:** $|u_{12}|^2 + |u_{22}|^2 = 1$
3. **Orthogonalitas:** $u_{11}^* u_{12} + u_{21}^* u_{22} = 0$

Dari (3), kita dapat menulis $u_{21}^* u_{22} = -u_{11}^* u_{12}$. Karena $u_{11} \neq 0$ (asumsikan tidak nol), maka:

$$
u_{22} = -\frac{u_{11}^* u_{12}}{u_{21}^*}
$$

Dengan manipulasi aljabar dan parameterisasi trigonometrik $|u_{11}| = \cos\theta$, kita peroleh bentuk standar:

$$
U = e^{i\alpha} \begin{pmatrix} \cos\theta & e^{i\phi}\sin\theta \\ -e^{-i\phi}\sin\theta & \cos\theta \end{pmatrix}
$$

untuk kasus determinan $1$ (setelah faktor fase global dikeluarkan).

---

### 1.7 Bentuk Eksponensial: Hubungan dengan Matriks Pauli

Representasi yang **paling fundamental** untuk konstruksi gerbang kuantum adalah:

$$
\boxed{U = e^{i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta)}
$$

di mana:

$$
R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

$$
R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}
$$

Matriks Pauli $X, Y, Z$ adalah:

$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

**Teorema Z-Y-Z:** Untuk setiap $U \in SU(2)$ (matriks uniter dengan $\det = 1$), terdapat sudut $\beta, \gamma, \delta$ sehingga $U = R_z(\beta) R_y(\gamma) R_z(\delta)$.

**Bukti singkat:**
Misalkan $U = \begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix}$ dengan $|a|^2+|b|^2=1$. Tulis $a = \cos\frac{\gamma}{2} e^{-i(\beta+\delta)/2}$ dan $b = -\sin\frac{\gamma}{2} e^{-i(\beta-\delta)/2}$, maka hasil perkalian $R_z(\beta) R_y(\gamma) R_z(\delta)$ akan menghasilkan matriks tersebut.

---

### 1.8 Rangkuman Kunci Modul 1

| Konsep                | Definisi                                         | Implikasi untuk Gerbang Kuantum                     |
| --------------------- | ------------------------------------------------ | --------------------------------------------------- |
| **Ket** $\psi\rangle$ | Vektor kolom di $\mathbb{C}^n$                   | Keadaan kuantum                                     |
| **Bra** $\langle\psi$ | Konjugat transpose dari ket                      | Mengukur/memproyeksikan                             |
| **Inner Product**     | $\langle\phi\psi\rangle = \sum_i \phi_i^*\psi_i$ | Amplitudo probabilitas transisi                     |
| **Outer Product**     | $\psi\rangle\langle\phi$                         | Membangun operator (proyektor, gerbang)             |
| **Matriks Uniter**    | $U^\dagger U = I$                                | Evolusi kuantum yang *reversible*                   |
| **Dekomposisi**       | $U = e^{i\alpha} R_z R_y R_z$                    | Semua gerbang 1-qubit adalah rotasi di Bloch Sphere |

---

### Latihan Verifikasi (Kerjakan untuk memastikan pemahaman)

1. Buktikan bahwa $H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ memenuhi $H^\dagger H = I$.
2. Hitung $\langle 0 | H | 0 \rangle$ dan $\langle 1 | H | 0 \rangle$.
3. Tunjukkan bahwa $(|0\rangle\langle 0|)(|0\rangle\langle 0|) = |0\rangle\langle 0|$ (sifat idempoten proyektor).

---

**Apakah Anda sudah siap melanjutkan ke Modul 2 (Generator Gerbang Kuantum dan Eksponensial Matriks Pauli)?** Di sana kita akan menurunkan secara detail mengapa $e^{i\theta X} = I\cos\theta + iX\sin\theta$ dari deret Taylor.

---
---
Baik, kita lanjut ke **Modul 2: Generator Gerbang Kuantum dan Aljabar Lie $\mathfrak{su}(2)$**.

---

## Modul 2: Generator Gerbang Kuantum dan Eksponensial Matriks

### 2.1 Matriks Pauli sebagai Basis Ruang Operator Hermitian Traceless

Dalam ruang Hilbert $\mathbb{C}^2$, himpunan semua operator Hermitian dengan *trace* nol membentuk ruang vektor real berdimensi 3. **Matriks Pauli** membentuk basis ortonormal untuk ruang ini:

$$
\boxed{
\sigma_x = X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad
\sigma_y = Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad
\sigma_z = Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
}
$$

**Sifat-sifat Aljabar Matriks Pauli:**

#### 1. Hermitian:
$$
X^\dagger = X, \quad Y^\dagger = Y, \quad Z^\dagger = Z
$$

#### 2. Uniter:
$$
X^\dagger X = X^2 = I, \quad Y^\dagger Y = Y^2 = I, \quad Z^\dagger Z = Z^2 = I
$$

#### 3. Trace Nol:
$$
\text{Tr}(X) = 0, \quad \text{Tr}(Y) = 0, \quad \text{Tr}(Z) = 0
$$

#### 4. Determinan:
$$
\det(X) = -1, \quad \det(Y) = -1, \quad \det(Z) = -1
$$

#### 5. Relasi Komutasi (Aljabar Lie $\mathfrak{su}(2)$):
$$
\boxed{[X, Y] = 2iZ, \quad [Y, Z] = 2iX, \quad [Z, X] = 2iY}
$$

di mana $[A, B] = AB - BA$ adalah komutator.

**Pembuktian $[X, Y] = 2iZ$:**

$$
XY = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}
$$

$$
YX = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix}
$$

$$
[X, Y] = XY - YX = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix} - \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = \begin{pmatrix} 2i & 0 \\ 0 & -2i \end{pmatrix} = 2iZ \quad \checkmark
$$

#### 6. Relasi Anti-Komutasi:
$$
\boxed{\{X, Y\} = 0, \quad \{Y, Z\} = 0, \quad \{Z, X\} = 0}
$$

di mana $\{A, B\} = AB + BA$.

#### 7. Identitas Produk:
$$
\boxed{\sigma_j \sigma_k = \delta_{jk} I + i \varepsilon_{jkl} \sigma_l}
$$

di mana $\varepsilon_{jkl}$ adalah simbol Levi-Civita, dan $\delta_{jk}$ adalah delta Kronecker.

**Contoh:** $XY = iZ$, $YZ = iX$, $ZX = iY$.

---

### 2.2 Eksponensial Matriks: Definisi dan Deret Taylor

Untuk matriks persegi $A$, eksponensial matriks didefinisikan melalui deret Taylor:

$$
\boxed{e^A = \sum_{n=0}^{\infty} \frac{A^n}{n!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \frac{A^4}{4!} + \cdots}
$$

**Sifat-sifat penting:**

1. **Tidak selalu komutatif:** $e^A e^B \neq e^{A+B}$ kecuali $[A,B] = 0$.
2. **Rumus Baker-Campbell-Hausdorff:** Untuk kasus non-komutatif, $e^A e^B = e^{A + B + \frac{1}{2}[A,B] + \cdots}$.
3. **Determinan:** $\det(e^A) = e^{\text{Tr}(A)}$.
4. **Invers:** $(e^A)^{-1} = e^{-A}$.

---

### 2.3 Penurunan Eksponensial Matriks Pauli

Kita akan menurunkan rumus fundamental:

$$
\boxed{e^{i\theta X} = I \cos\theta + iX \sin\theta}
$$

**Langkah 1: Hitung pangkat-pangkat $X$**

Karena $X^2 = I$, kita memiliki pola periodik:

$$
\begin{align}
X^0 &= I \\
X^1 &= X \\
X^2 &= I \\
X^3 &= X \\
X^4 &= I \\
X^5 &= X
\end{align}
$$

Secara umum:
- $X^{2k} = I$ untuk $k \ge 0$
- $X^{2k+1} = X$ untuk $k \ge 0$

**Langkah 2: Ekspansi deret $e^{i\theta X}$**

$$
\begin{align}
e^{i\theta X} &= \sum_{n=0}^{\infty} \frac{(i\theta X)^n}{n!} \\
&= \sum_{n=0}^{\infty} \frac{(i\theta)^n X^n}{n!}
\end{align}
$$

**Langkah 3: Pisahkan suku genap dan ganjil**

$$
\begin{align}
e^{i\theta X} &= \sum_{k=0}^{\infty} \frac{(i\theta)^{2k} X^{2k}}{(2k)!} + \sum_{k=0}^{\infty} \frac{(i\theta)^{2k+1} X^{2k+1}}{(2k+1)!} \\
&= \sum_{k=0}^{\infty} \frac{(i\theta)^{2k} I}{(2k)!} + \sum_{k=0}^{\infty} \frac{(i\theta)^{2k+1} X}{(2k+1)!}
\end{align}
$$

**Langkah 4: Sederhanakan pangkat $i$**

Untuk suku genap: $(i)^{2k} = (i^2)^k = (-1)^k$
Untuk suku ganjil: $(i)^{2k+1} = i \cdot (i^2)^k = i(-1)^k$

$$
\begin{align}
e^{i\theta X} &= \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k}}{(2k)!}\right) I + i \left(\sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!}\right) X
\end{align}
$$

**Langkah 5: Kenali deret Taylor trigonometri**

Dari kalkulus, kita tahu:
$$
\cos\theta = \sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k}}{(2k)!}, \quad \sin\theta = \sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!}
$$

Sehingga:

$$
\boxed{e^{i\theta X} = I \cos\theta + iX \sin\theta}
$$

**Verifikasi:**
$$
e^{i\theta X} = \begin{pmatrix} \cos\theta & 0 \\ 0 & \cos\theta \end{pmatrix} + i \begin{pmatrix} 0 & \sin\theta \\ \sin\theta & 0 \end{pmatrix} = \begin{pmatrix} \cos\theta & i\sin\theta \\ i\sin\theta & \cos\theta \end{pmatrix}
$$

---

### 2.4 Penurunan untuk $Y$ dan $Z$

Dengan metode yang sama, karena $Y^2 = I$ dan $Z^2 = I$:

**Untuk $Y$:**
$$
\boxed{e^{i\theta Y} = I \cos\theta + iY \sin\theta = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}}
$$

**Untuk $Z$:**
$$
\boxed{e^{i\theta Z} = I \cos\theta + iZ \sin\theta = \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix}}
$$

**Verifikasi untuk $Z$:**
$$
I\cos\theta + iZ\sin\theta = \begin{pmatrix} \cos\theta + i\sin\theta & 0 \\ 0 & \cos\theta - i\sin\theta \end{pmatrix} = \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix}
$$

---

### 2.5 Konvensi Fase dalam Gerbang Kuantum: Faktor $\frac{1}{2}$

Dalam komputasi kuantum, gerbang rotasi standar didefinisikan dengan **setengah sudut**:

$$
\boxed{R_x(\theta) = e^{-i\frac{\theta}{2}X} = \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}X}
$$

$$
\boxed{R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}Y}
$$

$$
\boxed{R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}}
$$

**Mengapa faktor $\frac{1}{2}$?**

1. **Interpretasi Geometris di Bloch Sphere:**
   Keadaan qubit $|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle$ memiliki parameter $\frac{\theta}{2}$. Rotasi sebesar $\theta$ pada keadaan ini membutuhkan operator $e^{-i\frac{\theta}{2}\hat{n}\cdot\vec{\sigma}}$.

2. **Periodisitas:**
   - $R_x(2\pi) = -I$ (bukan $I$)
   - $R_x(4\pi) = I$

   Ini mencerminkan sifat spinor: rotasi $2\pi$ memberikan tanda minus, baru kembali ke identitas setelah rotasi $4\pi$.

3. **Hubungan dengan $SU(2)$:**
   Pemetaan dari $SU(2)$ ke $SO(3)$ adalah homomorfisma 2-ke-1. Sudut rotasi di ruang fisik ($\theta$) adalah **dua kali** sudut parameter di ruang spinor ($\theta/2$).

---

### 2.6 Hubungan Eksponensial dengan Sifat Uniter

**Teorema:** Jika $H$ adalah matriks Hermitian ($H^\dagger = H$), maka $U = e^{iH}$ adalah matriks uniter.

**Bukti:**

$$
U^\dagger = (e^{iH})^\dagger = e^{-iH^\dagger} = e^{-iH}
$$

$$
U^\dagger U = e^{-iH} e^{iH} = e^{-iH + iH} = e^0 = I \quad \checkmark
$$

Karena matriks Pauli adalah Hermitian ($X^\dagger = X$, dll.), maka $e^{i\theta X}$, $e^{i\theta Y}$, dan $e^{i\theta Z}$ semuanya **otomatis uniter**.

**Aplikasi:** Setiap gerbang kuantum 1-qubit dapat ditulis sebagai:

$$
U = e^{i\alpha} e^{-i\frac{\theta}{2} \hat{n} \cdot \vec{\sigma}}
$$

di mana $\hat{n} = (n_x, n_y, n_z)$ adalah vektor satuan 3D, dan $\vec{\sigma} = (X, Y, Z)$.

---

### 2.7 Generator sebagai Operator Momentum Sudut

Dalam fisika kuantum, operator momentum sudut spin-$\frac{1}{2}$ adalah:

$$
S_x = \frac{\hbar}{2}X, \quad S_y = \frac{\hbar}{2}Y, \quad S_z = \frac{\hbar}{2}Z
$$

Dengan $\hbar = 1$ dalam unit natural komputasi kuantum, kita memiliki:

$$
\text{Gerbang rotasi} = e^{-i \theta S_j} = e^{-i\frac{\theta}{2} \sigma_j}
$$

Ini menjelaskan mengapa matriks Pauli disebut **generator** rotasi.

---

### 2.8 Rangkuman Modul 2

| Konsep             | Rumus                                          | Signifikansi                            |
| ------------------ | ---------------------------------------------- | --------------------------------------- |
| **Matriks Pauli**  | $X, Y, Z$                                      | Basis operator Hermitian traceless      |
| **Komutator**      | $[X,Y] = 2iZ$                                  | Struktur aljabar Lie $\mathfrak{su}(2)$ |
| **Eksponensial**   | $e^{i\theta X} = \cos\theta I + i\sin\theta X$ | Konstruksi fundamental gerbang rotasi   |
| **Gerbang Rotasi** | $R_x(\theta) = e^{-i\frac{\theta}{2}X}$        | Rotasi di Bloch Sphere                  |
| **Sifat Uniter**   | $(e^{iH})^\dagger = e^{-iH}$                   | Jaminan reversibilitas evolusi kuantum  |

---

### Latihan Modul 2

1. **Buktikan** bahwa $e^{i\theta Y} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}$ menggunakan metode deret Taylor.

2. **Verifikasi** bahwa $R_x(\pi) = -iX$ dan jelaskan mengapa ini setara dengan gerbang $X$ secara fisis (abaikan fase global).

3. **Hitung** $e^{i\alpha X} e^{i\beta Z}$ dan bandingkan dengan $e^{i\beta Z} e^{i\alpha X}$. Apakah keduanya sama? Mengapa?

4. **Tunjukkan** bahwa $\text{Tr}(R_y(\theta)) = 2\cos\frac{\theta}{2}$.

---

**Apakah Anda siap melanjutkan ke Modul 3 (Konstruksi Rinci Gerbang Hadamard)?** Di sana kita akan membangun $H$ dari prinsip simetri dan melihat bagaimana $H = \frac{X+Z}{\sqrt{2}}$ muncul secara alami dari rotasi di Bloch Sphere.

---
---
Baik, kita lanjut ke **Modul 3: Konstruksi Rinci Gerbang Hadamard ($H$)**.

---

## Modul 3: Konstruksi Rinci Gerbang Hadamard

### 3.1 Definisi dan Matriks Hadamard

Gerbang Hadamard adalah gerbang 1-qubit yang didefinisikan oleh matriks:

$$
\boxed{H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}}
$$

**Sifat-sifat fundamental $H$:**

1. **Hermitian:** $H^\dagger = H$
2. **Uniter:** $H^\dagger H = H^2 = I$
3. **Trace:** $\text{Tr}(H) = 0$
4. **Determinan:** $\det(H) = -1$

---

### 3.2 Verifikasi Sifat Uniter dan Hermitian

**Pembuktian $H^\dagger = H$:**

$$
H^\dagger = \frac{1}{\sqrt{2}} \begin{pmatrix} 1^* & 1^* \\ 1^* & -1^* \end{pmatrix}^T = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}^T = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H \quad \checkmark
$$

**Pembuktian $H^2 = I$:**

$$
\begin{align}
H^2 &= \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \cdot \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 1\cdot 1 + 1\cdot 1 & 1\cdot 1 + 1\cdot (-1) \\ 1\cdot 1 + (-1)\cdot 1 & 1\cdot 1 + (-1)\cdot (-1) \end{pmatrix} \\
&= \frac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark
\end{align}
$$

Karena $H^\dagger = H$ dan $H^2 = I$, maka $H^\dagger H = H^2 = I$, sehingga $H$ uniter.

---

### 3.3 Konstruksi dari Prinsip Simetri: Superposisi Setimbang

**Persyaratan fisik:** Gerbang Hadamard harus memetakan basis komputasi ke superposisi setimbang.

Untuk $|0\rangle$:
$$
H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle
$$

Untuk $|1\rangle$:
$$
H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle
$$

**Penurunan matriks dari syarat ini:**

Misalkan $H = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Dari $H|0\rangle = |+\rangle$:

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} a \\ c \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} \implies a = \frac{1}{\sqrt{2}}, \quad c = \frac{1}{\sqrt{2}}
$$

Dari $H|1\rangle = |-\rangle$:

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} b \\ d \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \implies b = \frac{1}{\sqrt{2}}, \quad d = -\frac{1}{\sqrt{2}}
$$

Sehingga $H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

---

### 3.4 Konstruksi dari Matriks Pauli: $H = \frac{X + Z}{\sqrt{2}}$

**Teorema:** Gerbang Hadamard dapat dinyatakan sebagai kombinasi linear matriks Pauli:

$$
\boxed{H = \frac{X + Z}{\sqrt{2}}}
$$

**Pembuktian:**

$$
X + Z = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}
$$

Maka:
$$
\frac{X + Z}{\sqrt{2}} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H \quad \checkmark
$$

**Mengapa bentuk ini fundamental?**
- $X$ dan $Z$ adalah generator grup Pauli.
- Ini menunjukkan bahwa $H$ adalah **rotasi $\pi$ terhadap sumbu $\frac{X+Z}{\sqrt{2}}$** di ruang Bloch.

---

### 3.5 Interpretasi Geometris di Bloch Sphere

**Representasi vektor Bloch:**

Setiap matriks uniter $2 \times 2$ dengan determinan $1$ dapat ditulis sebagai:

$$
U = e^{-i\frac{\theta}{2} \hat{n} \cdot \vec{\sigma}} = \cos\frac{\theta}{2} I - i \sin\frac{\theta}{2} (\hat{n} \cdot \vec{\sigma})
$$

Untuk Hadamard, kita ingin merepresentasikannya dalam bentuk ini.

**Langkah 1: Normalisasi sumbu rotasi**

Vektor sumbu: $\vec{v} = (1, 0, 1)$ (koefisien $X$ dan $Z$).

Normalisasi: $\hat{n} = \frac{\vec{v}}{\|\vec{v}\|} = \frac{(1, 0, 1)}{\sqrt{2}} = \left(\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}\right)$

**Langkah 2: Mencari sudut $\theta$**

Kita ingin $H = e^{i\alpha} \left(\cos\frac{\theta}{2} I - i \sin\frac{\theta}{2} (\hat{n} \cdot \vec{\sigma})\right)$

Hitung $\hat{n} \cdot \vec{\sigma}$:
$$
\hat{n} \cdot \vec{\sigma} = \frac{1}{\sqrt{2}} X + \frac{1}{\sqrt{2}} Z = \frac{X + Z}{\sqrt{2}} = H
$$

**Langkah 3: Mencocokkan dengan bentuk eksponensial**

Kita ingin:
$$
H = e^{i\alpha} \left(\cos\frac{\theta}{2} I - i \sin\frac{\theta}{2} H\right)
$$

Bandingkan dengan $H = 0 \cdot I + 1 \cdot H$.

Ini berarti:
- $\cos\frac{\theta}{2} = 0 \implies \frac{\theta}{2} = \frac{\pi}{2} \implies \theta = \pi$
- $-i e^{i\alpha} \sin\frac{\pi}{2} = 1 \implies -i e^{i\alpha} = 1 \implies e^{i\alpha} = i \implies \alpha = \frac{\pi}{2}$

**Kesimpulan:**

$$
\boxed{H = e^{i\frac{\pi}{2}} e^{-i\frac{\pi}{2} \left(\frac{X+Z}{\sqrt{2}}\right)} = i e^{-i\frac{\pi}{2} \frac{X+Z}{\sqrt{2}}}}
$$

Atau dalam bentuk yang lebih standar (mengabaikan fase global $i$):

$$
H \cong e^{-i\frac{\pi}{2} \frac{X+Z}{\sqrt{2}}}
$$

---

### 3.6 Konstruksi Alternatif: Hadamard sebagai Rotasi $Y$ dan $Z$

Ada cara lain untuk mengkonstruksi $H$ dari rotasi-rotasi dasar di Bloch Sphere:

$$
\boxed{H = R_y\left(\frac{\pi}{4}\right) \cdot Z \cdot R_y\left(-\frac{\pi}{4}\right)^\dagger}
$$

Atau ekuivalen:

$$
\boxed{H = R_y\left(\frac{\pi}{2}\right) \cdot Z}
$$

**Pembuktian:**

$$
\begin{align}
R_y\left(\frac{\pi}{2}\right) &= e^{-i\frac{\pi}{4}Y} = \cos\frac{\pi}{4}I - i\sin\frac{\pi}{4}Y = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \\
Z &= \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \\
R_y\left(\frac{\pi}{2}\right) \cdot Z &= \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = H \quad \checkmark
\end{align}
$$

---

### 3.7 Dekomposisi Spektral Hadamard

Karena $H$ adalah Hermitian, ia dapat didiagonalkan dengan basis vektor eigennya:

**Nilai eigen:**
$$
\det(H - \lambda I) = \begin{vmatrix} \frac{1}{\sqrt{2}}-\lambda & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}-\lambda \end{vmatrix} = \lambda^2 - 1 = 0
$$

Sehingga $\lambda_1 = 1$ dan $\lambda_2 = -1$.

**Vektor eigen:**

Untuk $\lambda = 1$:
$$
(H - I)|v_1\rangle = 0 \implies \begin{pmatrix} \frac{1}{\sqrt{2}}-1 & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}-1 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = 0
$$

Solusi: $|v_1\rangle = \cos\frac{\pi}{8}|0\rangle + \sin\frac{\pi}{8}|1\rangle$

Untuk $\lambda = -1$:
$$
|v_2\rangle = -\sin\frac{\pi}{8}|0\rangle + \cos\frac{\pi}{8}|1\rangle
$$

**Dekomposisi spektral:**
$$
H = 1 \cdot |v_1\rangle\langle v_1| + (-1) \cdot |v_2\rangle\langle v_2|
$$

Ini menegaskan bahwa $H$ adalah operator refleksi.

---

### 3.8 Aksi Hadamard pada Keadaan Umum

Untuk keadaan umum $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$:

$$
H|\psi\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \frac{1}{\sqrt{2}} \begin{pmatrix} \alpha + \beta \\ \alpha - \beta \end{pmatrix} = \frac{\alpha+\beta}{\sqrt{2}}|0\rangle + \frac{\alpha-\beta}{\sqrt{2}}|1\rangle
$$

**Kasus-kasus khusus:**
- $H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$
- $H|1\rangle = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = |-\rangle$
- $H|+\rangle = |0\rangle$
- $H|-\rangle = |1\rangle$

Ini menunjukkan $H$ adalah **transformasi basis** antara basis komputasi $\{|0\rangle, |1\rangle\}$ dan basis Hadamard $\{|+\rangle, |-\rangle\}$.

---

### 3.9 Generalisasi: Keluarga Gerbang Hadamard Umum

Kita dapat mendefinisikan keluarga gerbang yang memetakan ke superposisi dengan amplitudo berbeda:

$$
H_{\text{general}}(\theta) = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}
$$

Untuk $\theta = \frac{\pi}{4}$, kita dapatkan Hadamard standar.

**Verifikasi uniteritas:**
$$
H_{\text{general}}^\dagger H_{\text{general}} = \begin{pmatrix} \cos^2\theta + \sin^2\theta & \cos\theta\sin\theta - \sin\theta\cos\theta \\ \sin\theta\cos\theta - \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{pmatrix} = I
$$

---

### 3.10 Rangkuman Modul 3

| Aspek            | Rumus/Konsep                                                  | Signifikansi                     |
| ---------------- | ------------------------------------------------------------- | -------------------------------- |
| **Matriks**      | $H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | Definisi standar                 |
| **Dari Pauli**   | $H = \frac{X+Z}{\sqrt{2}}$                                    | Kombinasi generator              |
| **Rotasi Bloch** | $H \cong e^{-i\frac{\pi}{2} \frac{X+Z}{\sqrt{2}}}$            | Rotasi $\pi$ thd sumbu $(1,0,1)$ |
| **Dekomposisi**  | $H = R_y(\frac{\pi}{2}) Z$                                    | Konstruksi dari rotasi dasar     |
| **Nilai eigen**  | $\lambda = \pm 1$                                             | Operator refleksi                |
| **Aksi**         | $H0\rangle =+\rangle$, $H1\rangle =-\rangle$                  | Transformasi basis               |

---

### Latihan Modul 3

1. **Buktikan** bahwa $H X H = Z$ dan $H Z H = X$. Interpretasikan hasil ini secara geometris.

2. **Tunjukkan** bahwa $H = \frac{1}{\sqrt{2}}(|0\rangle\langle 0| + |0\rangle\langle 1| + |1\rangle\langle 0| - |1\rangle\langle 1|)$.

3. **Hitung** $H \otimes H$ (Hadamard pada 2 qubit) dan verifikasi bahwa ini adalah matriks uniter $4 \times 4$.

4. **Buktikan** bahwa $H^{\otimes n} |0\rangle^{\otimes n} = \frac{1}{\sqrt{2^n}} \sum_{x \in \{0,1\}^n} |x\rangle$ (superposisi seragam semua keadaan basis).

---

**Apakah Anda siap melanjutkan ke Modul 4 (Konstruksi Rinci CNOT dari Produk Kronecker dan Operator Proyeksi)?** Di sana kita akan membangun gerbang 2-qubit paling fundamental dalam komputasi kuantum.

---
---
Baik, kita lanjut ke **Modul 4: Konstruksi Rinci CNOT (Controlled-NOT)**.

---

## Modul 4: Konstruksi Rinci CNOT dari Produk Kronecker dan Operator Proyeksi

### 4.1 Definisi dan Matriks CNOT

CNOT (Controlled-NOT) adalah gerbang 2-qubit yang bekerja pada **qubit kontrol** dan **qubit target**. Aksi logikanya:

- Jika qubit kontrol = $|0\rangle$, target tidak berubah.
- Jika qubit kontrol = $|1\rangle$, target di-$X$-kan (flip).

**Matriks CNOT dalam basis komputasi $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$:**

$$
\boxed{CNOT = \begin{pmatrix} 
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}}
$$

---

### 4.2 Notasi Dirac untuk Keadaan 2-Qubit

Sebelum mengkonstruksi CNOT, kita perlu memahami **Produk Kronecker** ($\otimes$).

**Definisi Produk Kronecker untuk vektor:**

Untuk $|a\rangle = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$ dan $|b\rangle = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$:

$$
|a\rangle \otimes |b\rangle = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \otimes \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} a_1 b_1 \\ a_1 b_2 \\ a_2 b_1 \\ a_2 b_2 \end{pmatrix}
$$

**Basis komputasi 2-qubit:**
$$
\begin{align}
|00\rangle &= |0\rangle \otimes |0\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \\
|01\rangle &= |0\rangle \otimes |1\rangle = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \\
|10\rangle &= |1\rangle \otimes |0\rangle = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \\
|11\rangle &= |1\rangle \otimes |1\rangle = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
\end{align}
$$

**Konvensi urutan:** Qubit pertama (kiri) adalah kontrol, qubit kedua (kanan) adalah target. Jadi $|10\rangle$ berarti kontrol = $|1\rangle$, target = $|0\rangle$.

---

### 4.3 Produk Kronecker untuk Matriks

Untuk matriks $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ dan $B = \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix}$:

$$
A \otimes B = \begin{pmatrix} 
a_{11}B & a_{12}B \\ 
a_{21}B & a_{22}B 
\end{pmatrix} = \begin{pmatrix}
a_{11}b_{11} & a_{11}b_{12} & a_{12}b_{11} & a_{12}b_{12} \\
a_{11}b_{21} & a_{11}b_{22} & a_{12}b_{21} & a_{12}b_{22} \\
a_{21}b_{11} & a_{21}b_{12} & a_{22}b_{11} & a_{22}b_{12} \\
a_{21}b_{21} & a_{21}b_{22} & a_{22}b_{21} & a_{22}b_{22}
\end{pmatrix}
$$

**Contoh penting - Identitas 2-qubit:**
$$
I \otimes I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} = I_{4 \times 4}
$$

---

### 4.4 Operator Proyeksi untuk Kontrol

Ingat dari Modul 1:
$$
|0\rangle\langle 0| = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad |1\rangle\langle 1| = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}
$$

Operator proyeksi ini **memilih** komponen keadaan yang sesuai dengan qubit kontrol.

**Proyeksi pada ruang 2-qubit:**

Untuk memproyeksikan qubit kontrol ke $|0\rangle$ (dan membiarkan target bebas):
$$
P_0 = |0\rangle\langle 0| \otimes I = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Untuk memproyeksikan qubit kontrol ke $|1\rangle$:
$$
P_1 = |1\rangle\langle 1| \otimes I = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**Verifikasi:** $P_0 + P_1 = I \otimes I = I_{4 \times 4}$.

---

### 4.5 Konstruksi CNOT dari Operator Proyeksi

**Prinsip:** CNOT menerapkan $I$ pada target jika kontrol $|0\rangle$, dan $X$ pada target jika kontrol $|1\rangle$.

$$
\boxed{CNOT = P_0 \cdot (I \otimes I) + P_1 \cdot (I \otimes X)}
$$

Atau ekuivalen:
$$
\boxed{CNOT = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X}
$$

**Pembuktian dengan perkalian matriks:**

**Suku pertama:** $|0\rangle\langle 0| \otimes I$
$$
|0\rangle\langle 0| \otimes I = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \otimes \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

**Suku kedua:** $|1\rangle\langle 1| \otimes X$
$$
|1\rangle\langle 1| \otimes X = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \otimes \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}
$$

**Jumlahkan:**
$$
CNOT = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix} + \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix} \quad \checkmark
$$

---

### 4.6 Verifikasi Aksi CNOT pada Keadaan Basis

Mari kita verifikasi bahwa matriks ini bekerja sesuai definisi.

**Kasus 1: Kontrol $|0\rangle$, target $|0\rangle$**
$$
CNOT|00\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} = |00\rangle \quad \checkmark
$$

**Kasus 2: Kontrol $|0\rangle$, target $|1\rangle$**
$$
CNOT|01\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} = |01\rangle \quad \checkmark
$$

**Kasus 3: Kontrol $|1\rangle$, target $|0\rangle$**
$$
CNOT|10\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = |11\rangle \quad \checkmark
$$

**Kasus 4: Kontrol $|1\rangle$, target $|1\rangle$**
$$
CNOT|11\rangle = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} = |10\rangle \quad \checkmark
$$

---

### 4.7 Pembuktian Uniteritas CNOT

Kita harus membuktikan $CNOT^\dagger \cdot CNOT = I_{4 \times 4}$.

**Langkah 1: Hitung $CNOT^\dagger$**

Karena semua elemen CNOT adalah real:
$$
CNOT^\dagger = CNOT^T = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}^T = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix} = CNOT
$$

Jadi CNOT adalah **Hermitian** sekaligus **uniter**.

**Langkah 2: Hitung $CNOT \cdot CNOT$**
$$
\begin{align}
CNOT \cdot CNOT &= \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix} \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix} \\
&= \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} = I_{4 \times 4} \quad \checkmark
\end{align}
$$

**Kesimpulan:** $CNOT^\dagger \cdot CNOT = CNOT^2 = I$, sehingga CNOT uniter.

---

### 4.8 CNOT sebagai Gerbang Non-Lokal: Tidak Dapat Difaktorkan

**Teorema:** CNOT **tidak dapat** ditulis sebagai produk Kronecker dari dua gerbang 1-qubit.

**Bukti dengan kontradiksi:**

Misalkan CNOT = $A \otimes B$ dengan $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ dan $B = \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix}$.

Maka:
$$
A \otimes B = \begin{pmatrix}
a_{11}B & a_{12}B \\
a_{21}B & a_{22}B
\end{pmatrix}
$$

Bandingkan dengan CNOT:
- Blok kiri-atas: $a_{11}B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \implies a_{11} \neq 0$ dan $B = \frac{1}{a_{11}} I$.
- Blok kanan-atas: $a_{12}B = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \implies a_{12} = 0$ atau $B = 0$. Karena $B \neq 0$, maka $a_{12} = 0$.
- Blok kiri-bawah: $a_{21}B = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \implies a_{21} = 0$.
- Blok kanan-bawah: $a_{22}B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

Karena $a_{12}=0$ dan $a_{21}=0$, matriks $A$ adalah diagonal. Maka $a_{22}B$ harus proporsional terhadap $B$. Tapi $B \propto I$ sedangkan $a_{22}B \propto X$. Kontradiksi! $\quad \blacksquare$

**Implikasi:** CNOT adalah gerbang **entangling** - dapat menciptakan keterbelitan dari keadaan terpisah.

---

### 4.9 Representasi Eksponensial CNOT

Meskipun CNOT tidak dapat difaktorkan sebagai $A \otimes B$, ia dapat ditulis dalam bentuk eksponensial menggunakan **Hamiltonian interaksi**:

$$
\boxed{CNOT = e^{i\frac{\pi}{4}} \cdot e^{-i\frac{\pi}{4} (I \otimes I - Z \otimes I - I \otimes X + Z \otimes X)}}
$$

Atau dalam bentuk yang lebih kompak:

$$
\boxed{CNOT = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X = e^{-i\frac{\pi}{4} (I-Z) \otimes (I-X)}}
$$

**Pembuktian singkat:**

Perhatikan bahwa:
$$
|0\rangle\langle 0| = \frac{I+Z}{2}, \quad |1\rangle\langle 1| = \frac{I-Z}{2}
$$

Maka:
$$
\begin{align}
CNOT &= \frac{I+Z}{2} \otimes I + \frac{I-Z}{2} \otimes X \\
&= \frac{1}{2}(I \otimes I + Z \otimes I + I \otimes X - Z \otimes X)
\end{align}
$$

Kita dapat menulis ini sebagai eksponensial dari operator Hermitian:
$$
CNOT = e^{-i\frac{\pi}{4} (I \otimes I - Z \otimes I - I \otimes X + Z \otimes X)}
$$

dikalikan dengan fase global.

---

### 4.10 Variasi CNOT: Kontrol Fase dan Kontrol-Z

**Controlled-Z (CZ):**
$$
CZ = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes Z = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & -1
\end{pmatrix}
$$

**Hubungan dengan CNOT:**
$$
CZ = (I \otimes H) \cdot CNOT \cdot (I \otimes H)
$$

**Controlled-Phase (CPhase):**
$$
CPhase(\theta) = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}
$$

---

### 4.11 Rangkuman Modul 4

| Konsep | Rumus/Konstruksi | Signifikansi |
|--------|------------------|--------------|
| **Matriks CNOT** | $\begin{pmatrix} 1&0&0&0 \\ 0&1&0&0 \\ 0&0&0&1 \\ 0&0&1&0 \end{pmatrix}$ | Definisi standar |
| **Dari Proyeksi** | $CNOT = \|0\rangle\langle 0\| \otimes I + \|1\rangle\langle 1\| \otimes X$ | Konstruksi fundamental |
| **Uniteritas** | $CNOT^2 = I$ | Self-inverse, Hermitian |
| **Non-Lokalitas** | Tidak dapat difaktorkan $A \otimes B$ | Menciptakan keterbelitan |
| **Eksponensial** | $e^{-i\frac{\pi}{4}(I-Z)\otimes(I-X)}$ | Representasi Hamiltonian |

---

### Latihan Modul 4

1. **Verifikasi** bahwa $CNOT = (H \otimes H) \cdot CNOT_{terbalik} \cdot (H \otimes H)$, di mana $CNOT_{terbalik}$ adalah CNOT dengan target dan kontrol ditukar.

2. **Tunjukkan** bahwa $CNOT \cdot (X \otimes X) \cdot CNOT = X \otimes I$. Interpretasikan hasil ini.

3. **Buktikan** bahwa $(CNOT \otimes I) \cdot (I \otimes CNOT) \cdot (CNOT \otimes I) = SWAP \cdot CNOT_{12} \cdot CNOT_{23}$ (petunjuk: ini terkait dengan dekomposisi Toffoli).

4. **Hitung** $CNOT (|+\rangle \otimes |0\rangle)$ dan tentukan apakah hasilnya terbelit.

---

**Apakah Anda siap melanjutkan ke Modul 5 (Konstruksi Gerbang Lain: Phase, Rotasi, dan Gerbang Universal)?** Di sana kita akan membangun gerbang $S$, $T$, rotasi umum, dan membahas set gerbang universal untuk komputasi kuantum.

---
---
Baik, kita lanjut ke **Modul 5: Konstruksi Gerbang Lain dari Bentuk Umum**.

---

## Modul 5: Konstruksi Gerbang Phase, Rotasi, dan Gerbang Universal

### 5.1 Gerbang Phase ($S$) dan $\pi/8$ ($T$)

Gerbang phase adalah keluarga gerbang diagonal yang menambahkan fase relatif antara $|0\rangle$ dan $|1\rangle$.

#### Gerbang $S$ (Phase Gate)

**Definisi:**
$$
\boxed{S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}}
$$

**Sifat-sifat:**
- **Uniter:** $S^\dagger S = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} = I$
- **Pangkat:** $S^2 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = Z$
- **Aksi:** $S|0\rangle = |0\rangle$, $S|1\rangle = i|1\rangle$

**Konstruksi dari $Z$:**
Karena $S^2 = Z$, kita dapat menulis $S$ sebagai "akar kuadrat dari $Z$":

$$
\boxed{S = \sqrt{Z} = Z^{1/2}}
$$

**Representasi eksponensial:**
$$
S = e^{i\pi/4} e^{-i\frac{\pi}{4}Z} = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}
$$

**Pembuktian:**
$$
e^{-i\frac{\pi}{4}Z} = \cos\frac{\pi}{4}I - i\sin\frac{\pi}{4}Z = \frac{1}{\sqrt{2}}\begin{pmatrix} 1-i & 0 \\ 0 & 1+i \end{pmatrix}
$$
Kalikan dengan $e^{i\pi/4} = \frac{1+i}{\sqrt{2}}$:
$$
\frac{1+i}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix} 1-i & 0 \\ 0 & 1+i \end{pmatrix} = \frac{1}{2}\begin{pmatrix} (1+i)(1-i) & 0 \\ 0 & (1+i)(1+i) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \quad \checkmark
$$

---

#### Gerbang $T$ ($\pi/8$ Gate)

**Definisi:**
$$
\boxed{T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}}
$$

**Sifat-sifat:**
- **Uniter:** $T^\dagger T = I$
- **Pangkat:** $T^2 = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} = S$
- **Nama:** Disebut $\pi/8$ karena dapat ditulis sebagai $e^{i\pi/8} e^{-i\frac{\pi}{8}Z}$

**Konstruksi sebagai $Z^{1/4}$:**
$$
T = Z^{1/4}
$$

**Representasi eksponensial:**
$$
T = e^{i\pi/8} e^{-i\frac{\pi}{8}Z} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}
$$

**Pembuktian:**
$$
e^{-i\frac{\pi}{8}Z} = \begin{pmatrix} e^{-i\pi/8} & 0 \\ 0 & e^{i\pi/8} \end{pmatrix}
$$
Kalikan dengan $e^{i\pi/8}$:
$$
e^{i\pi/8} \begin{pmatrix} e^{-i\pi/8} & 0 \\ 0 & e^{i\pi/8} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix} \quad \checkmark
$$

---

### 5.2 Gerbang Rotasi Umum $R_x, R_y, R_z$

Dari Modul 2, kita telah menurunkan rumus umum. Sekarang kita akan mengkonstruksi secara rinci.

#### Gerbang $R_x(\theta)$

**Definisi:**
$$
\boxed{R_x(\theta) = e^{-i\frac{\theta}{2}X} = \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}X}
$$

**Bentuk matriks:**
$$
R_x(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \\ -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

**Penurunan detail:**
$$
\begin{align}
e^{-i\frac{\theta}{2}X} &= \sum_{n=0}^{\infty} \frac{(-i\frac{\theta}{2})^n X^n}{n!} \\
&= \sum_{k=0}^{\infty} \frac{(-i\frac{\theta}{2})^{2k} X^{2k}}{(2k)!} + \sum_{k=0}^{\infty} \frac{(-i\frac{\theta}{2})^{2k+1} X^{2k+1}}{(2k+1)!} \\
&= \sum_{k=0}^{\infty} \frac{(-1)^k (\frac{\theta}{2})^{2k}}{(2k)!} I - i \sum_{k=0}^{\infty} \frac{(-1)^k (\frac{\theta}{2})^{2k+1}}{(2k+1)!} X \\
&= \cos\frac{\theta}{2} I - i\sin\frac{\theta}{2} X \quad \checkmark
\end{align}
$$

**Kasus khusus:**
- $R_x(\pi) = -iX \cong X$ (gerbang NOT)
- $R_x(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -i \\ -i & 1 \end{pmatrix}$

---

#### Gerbang $R_y(\theta)$

**Definisi:**
$$
\boxed{R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}Y}
$$

**Bentuk matriks:**
$$
R_y(\theta) = \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}
$$

**Penurunan detail:**
$$
\begin{align}
e^{-i\frac{\theta}{2}Y} &= \sum_{k=0}^{\infty} \frac{(-1)^k (\frac{\theta}{2})^{2k}}{(2k)!} I - i \sum_{k=0}^{\infty} \frac{(-1)^k (\frac{\theta}{2})^{2k+1}}{(2k+1)!} Y \\
&= \cos\frac{\theta}{2} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - i\sin\frac{\theta}{2} \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \\
&= \begin{pmatrix} \cos\frac{\theta}{2} & 0 \\ 0 & \cos\frac{\theta}{2} \end{pmatrix} + \begin{pmatrix} 0 & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & 0 \end{pmatrix} \\
&= \begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix} \quad \checkmark
\end{align}
$$

**Kasus khusus:**
- $R_y(\pi) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \cong Y$
- $R_y(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ (transformasi ke basis $X$)

---

#### Gerbang $R_z(\theta)$

**Definisi:**
$$
\boxed{R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}}
$$

**Penurunan:**
$$
\begin{align}
e^{-i\frac{\theta}{2}Z} &= \cos\frac{\theta}{2}I - i\sin\frac{\theta}{2}Z \\
&= \begin{pmatrix} \cos\frac{\theta}{2} - i\sin\frac{\theta}{2} & 0 \\ 0 & \cos\frac{\theta}{2} + i\sin\frac{\theta}{2} \end{pmatrix} \\
&= \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix} \quad \checkmark
\end{align}
$$

**Hubungan dengan gerbang phase:**
- $S = e^{i\pi/4} R_z(\pi/2)$
- $T = e^{i\pi/8} R_z(\pi/4)$
- $Z = e^{i\pi/2} R_z(\pi)$

---

### 5.3 Rotasi Sembarang di Bloch Sphere

Setiap gerbang 1-qubit dapat ditulis sebagai rotasi terhadap sumbu $\hat{n} = (n_x, n_y, n_z)$:

$$
\boxed{R_{\hat{n}}(\theta) = e^{-i\frac{\theta}{2} \hat{n} \cdot \vec{\sigma}} = \cos\frac{\theta}{2} I - i\sin\frac{\theta}{2} (n_x X + n_y Y + n_z Z)}
$$

**Parameterisasi umum matriks uniter $2 \times 2$:**

Dari Modul 1, setiap $U \in U(2)$ dapat ditulis sebagai:
$$
U = e^{i\alpha} \begin{pmatrix} \cos\frac{\theta}{2} e^{i\beta} & \sin\frac{\theta}{2} e^{i\gamma} \\ -\sin\frac{\theta}{2} e^{-i\gamma} & \cos\frac{\theta}{2} e^{-i\beta} \end{pmatrix}
$$

Dengan memilih $\alpha, \beta, \gamma, \theta$ yang tepat, kita dapat mengkonstruksi **semua** gerbang 1-qubit.

---

### 5.4 Dekomposisi Z-Y-Z

**Teorema:** Setiap matriks uniter $2 \times 2$ dengan determinan 1 dapat didekomposisi sebagai:

$$
\boxed{U = R_z(\alpha) R_y(\beta) R_z(\gamma)}
$$

**Penurunan:**
$$
\begin{align}
R_z(\alpha) R_y(\beta) R_z(\gamma) &= \begin{pmatrix} e^{-i\alpha/2} & 0 \\ 0 & e^{i\alpha/2} \end{pmatrix} 
\begin{pmatrix} \cos\frac{\beta}{2} & -\sin\frac{\beta}{2} \\ \sin\frac{\beta}{2} & \cos\frac{\beta}{2} \end{pmatrix}
\begin{pmatrix} e^{-i\gamma/2} & 0 \\ 0 & e^{i\gamma/2} \end{pmatrix} \\
&= \begin{pmatrix} 
e^{-i(\alpha+\gamma)/2} \cos\frac{\beta}{2} & -e^{-i(\alpha-\gamma)/2} \sin\frac{\beta}{2} \\
e^{i(\alpha-\gamma)/2} \sin\frac{\beta}{2} & e^{i(\alpha+\gamma)/2} \cos\frac{\beta}{2}
\end{pmatrix}
\end{align}
$$

Bandingkan dengan bentuk umum $U = \begin{pmatrix} a & b \\ -b^* & a^* \end{pmatrix}$:
- $a = e^{-i(\alpha+\gamma)/2} \cos\frac{\beta}{2}$
- $b = -e^{-i(\alpha-\gamma)/2} \sin\frac{\beta}{2}$

Dari sini kita dapat menyelesaikan $\alpha, \beta, \gamma$ untuk sebarang $a, b$.

---

### 5.5 Gerbang Kontrol Lainnya

#### Controlled-U (CU)

Untuk sebarang gerbang 1-qubit $U$, kita dapat mengkonstruksi versi terkontrolnya:

$$
\boxed{CU = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes U}
$$

**Bentuk matriks blok:**
$$
CU = \begin{pmatrix} I & 0 \\ 0 & U \end{pmatrix}
$$

**Contoh: Controlled-Hadamard**
$$
CH = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ 0 & 0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{pmatrix}
$$

---

#### SWAP Gate

**Definisi:** Menukar keadaan dua qubit.

**Matriks:**
$$
\boxed{SWAP = \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}}
$$

**Konstruksi dari CNOT:**
$$
SWAP = CNOT_{12} \cdot CNOT_{21} \cdot CNOT_{12}
$$

di mana $CNOT_{12}$ adalah CNOT dengan kontrol qubit 1 dan target qubit 2.

**Representasi eksponensial:**
$$
SWAP = e^{i\frac{\pi}{4}} e^{-i\frac{\pi}{4} (X \otimes X + Y \otimes Y + Z \otimes Z)}
$$

---

#### Toffoli Gate (CCNOT)

**Definisi:** CNOT dengan dua qubit kontrol.

**Matriks $8 \times 8$:**
$$
CCNOT = \begin{pmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{pmatrix}
$$

**Konstruksi dari proyeksi:**
$$
CCNOT = (I - |11\rangle\langle 11|) \otimes I + |11\rangle\langle 11| \otimes X
$$

---

### 5.6 Set Gerbang Universal

**Definisi:** Sebuah set gerbang disebut **universal** jika sebarang operasi uniter dapat diaproksimasi hingga akurasi sembarang menggunakan gerbang dari set tersebut.

**Set Universal Diskrit:**
$$
\boxed{\{H, T, CNOT\}}
$$

**Set Universal Kontinu:**
$$
\boxed{\{R_x(\theta), R_y(\theta), R_z(\theta), CNOT\}}
$$

**Teorema Solovay-Kitaev:** Setiap gerbang uniter dapat diaproksimasi dengan $O(\log^c(1/\epsilon))$ gerbang dari set universal diskrit, di mana $\epsilon$ adalah akurasi yang diinginkan.

---

### 5.7 Konstruksi Gerbang Sembarang dari Set Universal

#### Contoh: Mengkonstruksi $R_x(\theta)$ dari $\{H, T\}$

Menggunakan aproksimasi Solovay-Kitaev, kita dapat mendekomposisi $R_x(\theta)$ menjadi urutan $H$ dan $T$.

**Langkah 1:** Nyatakan $R_x(\theta)$ sebagai $H R_z(\theta) H$.

**Langkah 2:** Aproksimasi $R_z(\theta)$ menggunakan $T$ dan $T^\dagger$:
$$
R_z(\theta) \approx T^{n_1} (T^\dagger)^{n_2} \cdots
$$

**Langkah 3:** Gunakan identitas $T = R_z(\pi/4)$ untuk membangun rotasi $Z$ sebarang.

---

### 5.8 Tabel Ringkasan Gerbang-Gerbang Penting

| Gerbang | Matriks | Eksponensial | Aksi |
|---------|---------|--------------|------|
| $X$ (NOT) | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $e^{-i\frac{\pi}{2}X}$ | Flip |
| $Y$ | $\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ | $e^{-i\frac{\pi}{2}Y}$ | Flip+fase |
| $Z$ | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | $e^{-i\frac{\pi}{2}Z}$ | Fase $\pi$ |
| $H$ | $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ | $e^{-i\frac{\pi}{2}\frac{X+Z}{\sqrt{2}}}$ | Superposisi |
| $S$ | $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$ | $e^{-i\frac{\pi}{4}Z}$ | Fase $\pi/2$ |
| $T$ | $\begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$ | $e^{-i\frac{\pi}{8}Z}$ | Fase $\pi/4$ |
| $R_x(\theta)$ | $\begin{pmatrix} c & -is \\ -is & c \end{pmatrix}$ | $e^{-i\frac{\theta}{2}X}$ | Rotasi X |
| $R_y(\theta)$ | $\begin{pmatrix} c & -s \\ s & c \end{pmatrix}$ | $e^{-i\frac{\theta}{2}Y}$ | Rotasi Y |
| $R_z(\theta)$ | $\begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$ | $e^{-i\frac{\theta}{2}Z}$ | Rotasi Z |
| CNOT | $\begin{pmatrix} I & 0 \\ 0 & X \end{pmatrix}$ | Non-lokal | Controlled-NOT |
| SWAP | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ | $e^{-i\frac{\pi}{4}(X \otimes X + Y \otimes Y + Z \otimes Z)}$ | Tukar qubit |

Keterangan: $c = \cos\frac{\theta}{2}$, $s = \sin\frac{\theta}{2}$.

---

### 5.9 Rangkuman Modul 5

| Konsep | Poin Kunci |
|--------|------------|
| **Gerbang Phase** | $S = Z^{1/2}$, $T = Z^{1/4}$ |
| **Rotasi** | $R_k(\theta) = e^{-i\frac{\theta}{2}\sigma_k}$ |
| **Dekomposisi** | Semua gerbang 1-qubit = $R_z R_y R_z$ |
| **Gerbang Kontrol** | $CU = \|0\rangle\langle 0\| \otimes I + \|1\rangle\langle 1\| \otimes U$ |
| **Universal Set** | $\{H, T, CNOT\}$ atau $\{R_x, R_y, R_z, CNOT\}$ |

---

### Latihan Modul 5

1. **Buktikan** bahwa $T^\dagger S T = S$ (gunakan sifat komutasi).

2. **Tunjukkan** bahwa $R_x(\theta) = H R_z(\theta) H$.

3. **Dekomposisi** gerbang $U = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix}$ ke dalam bentuk $R_z(\alpha) R_y(\beta) R_z(\gamma)$.

4. **Buktikan** bahwa $\{H, S, CNOT\}$ juga merupakan set universal (petunjuk: $T$ dapat diaproksimasi dari $H$ dan $S$? Tidak secara eksak, tapi untuk universalitas aproksimasi ya).

5. **Konstruksi** $SWAP$ dari tiga CNOT dan verifikasi dengan perkalian matriks.

---

## Penutup

Anda telah menyelesaikan kelima modul dalam roadmap pembelajaran ini. Berikut ringkasan perjalanan Anda:

- **Modul 1:** Fondasi aljabar linier kompleks, notasi Dirac, definisi uniter.
- **Modul 2:** Generator Pauli, eksponensial matriks, aljabar Lie $\mathfrak{su}(2)$.
- **Modul 3:** Konstruksi Hadamard dari simetri dan rotasi Bloch.
- **Modul 4:** Konstruksi CNOT dari produk Kronecker dan operator proyeksi.
- **Modul 5:** Gerbang phase, rotasi umum, controlled gates, set universal.

**Apakah ada topik spesifik dari kelima modul ini yang ingin Anda perdalam, atau Anda ingin melanjutkan ke topik lanjutan seperti dekomposisi rangkaian kuantum, Hamiltonian simulasi, atau koreksi error kuantum?**