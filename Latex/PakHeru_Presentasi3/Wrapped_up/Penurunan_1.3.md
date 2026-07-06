## 1. Memahami Simbol dan Notasi

Sebelum masuk ke penurunan, kita harus membedah notasi Dirac tersebut:

- $|j\rangle$: **Ket** (vektor kolom) yang merepresentasikan suatu basis keadaan.
- $\langle i|$: **Bra** (vektor baris konjugat kompleks) yang merupakan dual dari $|i\rangle$.
- $\langle i | j \rangle$: **Produk dalam** (*inner product*) antara dua vektor.
- $\delta_{ij}$: **Delta Kronecker**, yang didefinisikan sebagai:
  $$\delta_{ij} = \begin{cases} 1, & \text{jika } i = j \\ 0, & \text{jika } i \neq j \end{cases}$$

---

## 2. Konsep Fisis: Ortogonalitas dan Normalisasi

Hubungan $\langle i | j \rangle = \delta_{ij}$ sebenarnya adalah gabungan dari dua konsep penting:

### A. Ortogonalitas ($i \neq j$)
Dalam mekanika kuantum, dua keadaan yang berbeda secara fisik harus bersifat saling lepas. Jika sistem berada dalam keadaan $|j\rangle$, probabilitas untuk menemukannya dalam keadaan $|i\rangle$ adalah nol.
- Secara matematis: $\langle i | j \rangle = 0$.

### B. Normalisasi ($i = j$)
Probabilitas total untuk menemukan sebuah partikel dalam seluruh basis keadaan yang mungkin haruslah bernilai 1 (100%). Oleh karena itu, *inner product* sebuah vektor dengan dirinya sendiri harus bernilai satu.
- Secara matematis: $\langle i | i \rangle = 1$.

---

## 3. Penurunan dari Operator Hermitian

Mengapa basis keadaan harus ortonormal? Hal ini bermula dari sifat **Operator Hermitian** (seperti Hamiltonian atau Momentum) yang merepresentasikan variabel teramati (*observables*).

Misalkan kita memiliki operator Hermitian $\hat{A}$ ($\hat{A}^\dagger = \hat{A}$) dengan nilai eigen riil $a_i$ dan $a_j$:
1. $\hat{A} |j\rangle = a_j |j\rangle$
2. $\langle i| \hat{A} = a_i \langle i|$

Kita hitung nilai $\langle i| \hat{A} |j\rangle$ dengan dua cara:
- **Cara 1 (A bekerja ke kanan):** $\langle i | (\hat{A} |j\rangle) = a_j \langle i | j \rangle$
- **Cara 2 (A bekerja ke kiri):** $(\langle i | \hat{A}) |j\rangle = a_i \langle i | j \rangle$

Kurangi keduanya:
$$(a_j - a_i) \langle i | j \rangle = 0$$

**Analisis:**
- Jika $i \neq j$ dan $a_i \neq a_j$, maka haruslah **$\langle i | j \rangle = 0$** (Ortogonal).
- Jika $i = j$, maka $(a_i - a_i) = 0$. Kita mendefinisikan panjang vektor tersebut adalah 1 (**$\langle i | i \rangle = 1$**) untuk memenuhi syarat normalisasi.

Maka terbukti: **$\langle i | j \rangle = \delta_{ij}$**.

---

## 4. Ekspansi Vektor Keadaan

Hubungan ortonormalitas di atas sangat krusial karena memungkinkan kita untuk mengekspansi sembarang vektor keadaan $|\psi\rangle$ ke dalam bentuk kombinasi linear basis $|j\rangle$:

$$|\psi\rangle = \sum_j c_j |j\rangle \tag{1}$$

Di mana $c_j$ adalah koefisien (amplitudo probabilitas) yang ingin kita cari.

---

## 5. Penurunan Mendapatkan Koefisien $c_i$

Untuk mendapatkan nilai $c_i$, kita "memproyeksikan" vektor $|\psi\rangle$ ke arah basis $\langle i|$ dengan melakukan perkalian titik dari kiri:

$$\langle i | \psi \rangle = \langle i | \left( \sum_j c_j |j\rangle \right)$$

Karena operasi ini linear, kita bisa memasukkan Bra $\langle i|$ ke dalam penjumlahan:

$$\langle i | \psi \rangle = \sum_j c_j \langle i | j \rangle$$

Substitusikan sifat ortonormalitas $\langle i | j \rangle = \delta_{ij}$:

$$\langle i | \psi \rangle = \sum_j c_j \delta_{ij}$$

Sifat Delta Kronecker akan membuat seluruh deret bernilai nol kecuali saat $j = i$. Maka, persamaan "runtuh" menjadi:

$$\langle i | \psi \rangle = c_i$$