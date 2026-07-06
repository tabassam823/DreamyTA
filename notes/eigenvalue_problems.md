# Masalah Nilai Eigen (Eigenvalue Problems)

Catatan ini membahas definisi masalah nilai eigen dan penurunan persamaan karakteristik.

## 1. Definisi Dasar

Misalkan kita mengoperasikan sebuah matriks $A$ pada sebuah vektor tak nol $|v\rangle \in \mathbb{C}^n$ (di mana $|v\rangle \neq 0$). Secara umum, hasil $A|v\rangle$ tidak proporsional dengan $|v\rangle$. Namun, jika $|v\rangle$ dipilih dengan tepat, kita mungkin mendapatkan hasil $A|v\rangle$ yang merupakan kelipatan skalar dari $|v\rangle$ itu sendiri:

$$
 A|v\rangle = \lambda |v\rangle, \quad \lambda \in \mathbb{C}
$$ 

*   $\lambda$ disebut **nilai eigen** (eigenvalue) dari $A$.
*   $|v\rangle$ disebut **vektor eigen** (eigenvector) yang bersesuaian dengan $\lambda$.

Karena persamaan di atas adalah persamaan linear, norma (panjang) dari vektor eigen tidak ditetapkan secara unik. Biasanya, kita menormalisasi $|v\rangle$ sehingga $\|v\rangle\| = 1$. Seringkali notasi $|\lambda\u0003\rangle$ digunakan untuk melambangkan vektor eigen yang bersesuaian dengan nilai eigen $\lambda$.

### Representasi Komponen
Misalkan { $|e_k\rangle$ } adalah basis ortonormal di $\mathbb{C}^n$.
*   $A_{ij} = \langle e_i | A | e_j \rangle$ adalah elemen matriks $A$.
*   $v_j = \langle e_j | v \rangle$ adalah komponen vektor $|v\rangle$.

Persamaan nilai eigen dalam bentuk komponen dapat diturunkan sebagai berikut:

$$ 
 A|v\rangle = \sum_{i,j} |e_i\rangle \langle e_i | A | e_j \rangle \langle e_j | v \rangle = \sum_{i,j} A_{ij} v_j |e_i\rangle 
$$ 

Sehingga persamaan $A|v\rangle = \lambda |v\rangle$ menjadi:

$$ 
 \sum_{j} A_{ij} v_j = \lambda v_i 
$$ 

## 2. Persamaan Karakteristik

Untuk mencari nilai $\lambda$, kita tulis ulang persamaan di atas dengan memindahkan suku kanan ke kiri:

$$ 
 \sum_{j} (A - \lambda I)_{ij} v_j = 0 
$$ 

Ini adalah sistem persamaan linear homogen. Agar sistem ini memiliki solusi non-trivial (solusi di mana $|v\rangle \neq 0$), matriks $(A - \lambda I)$ **tidak boleh memiliki invers**.

Jika matriks tersebut memiliki invers, maka satu-satunya solusi adalah $|v\rangle = (A - \lambda I)^{-1} 0 = 0$, yang tidak kita inginkan.

Syarat agar matriks tidak memiliki invers adalah determinannya harus nol:

$$ 
 D(\lambda) \equiv \det(A - \lambda I) = 0 
$$ 

Persamaan ini disebut **persamaan karakteristik** atau **persamaan eigen** dari $A$.

### Solusi Persamaan Karakteristik
Jika $A$ adalah matriks $n \times n$, persamaan karakteristik ini akan menghasilkan polinomial derajat $n$ dalam $\lambda$, yang memiliki $n$ solusi (termasuk multiplisitasnya): { $\lambda_1, \lambda_2, \dots, \lambda_n$ }.

Fungsi $D(\lambda)$ dapat diekspansi sebagai:

$$ 
 \begin{aligned} 
 D(\lambda) &= \prod_{i=1}^n (\lambda_i - \lambda) \\ 
 &= (-\lambda)^n + \sum_i \lambda_i (-\lambda)^{n-1} + \dots + \prod_{i=1}^n \lambda_i \\ 
 &= (-\lambda)^n + (\text{tr } A)(-\lambda)^{n-1} + \dots + \det A 
 \end{aligned} 
$$ 

Di mana kita menggunakan identitas:
*   $\text{tr} A = \sum_{i=1}^n \lambda_i$ (Trace adalah jumlah nilai eigen)
*   $\det A = \prod_{i=1}^n \lambda_i$ (Determinan adalah hasil kali nilai eigen)
