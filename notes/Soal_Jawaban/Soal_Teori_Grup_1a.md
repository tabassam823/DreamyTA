# Jawaban Soal 1a: Generator-Generator Grup SU(4)

## 1. Pendahuluan
Grup $SU(4)$ (*Special Unitary group*) adalah grup transformasi linear pada ruang vektor kompleks 4-dimensi yang bersifat uniter dan memiliki determinan 1. Matriks-matriks $U \in SU(4)$ memenuhi:
- $U^\dagger U = I$ (Uniter)
- $\det(U) = 1$ (Spesial)

Elemen grup ini dapat dinyatakan melalui eksponensial dari generator-generatornya:
$$U = e^{i 	heta_a T_a}$$
di mana $T_a$ adalah generator grup.

## 2. Sifat-Sifat Generator $SU(4)$
Generator $T_a$ untuk grup $SU(4)$ harus memenuhi syarat:
1. **Hermitian**: $T_a^\dagger = T_a$ (agar $U$ uniter).
2. **Traceless**: $	ext{Tr}(T_a) = 0$ (agar $\det(U) = 1$).
3. **Jumlah Generator**: Untuk $SU(n)$, terdapat $n^2 - 1$ generator. Maka untuk $SU(4)$, terdapat $4^2 - 1 = 15$ generator.

Biasanya, generator dinyatakan dalam matriks $\lambda_a$ (Matriks Gell-Mann yang diperluas) di mana $T_a = \frac{1}{2} \lambda_a$. Matriks-matriks ini dinormalisasi sehingga $	ext{Tr}(\lambda_a \lambda_b) = 2 \delta_{ab}$.

## 3. Representasi Matriks Generator $\lambda_1$ - $\lambda_{15}$

Generator-generator $SU(4)$ dapat disusun sebagai berikut:

### Subgrup $SU(2)$ dan $SU(3)$ (Generator 1-8)
Delapan generator pertama adalah perluasan dari matriks Gell-Mann $SU(3)$ dengan menambahkan baris dan kolom keempat yang bernilai nol.

$$
\lambda_1 = \begin{pmatrix} 0 & 1 & 0 & 0 \ 1 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_2 = \begin{pmatrix} 0 & -i & 0 & 0 \ i & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_3 = \begin{pmatrix} 1 & 0 & 0 & 0 \ 0 & -1 & 0 & 0 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}
$$

$$
\lambda_4 = \begin{pmatrix} 0 & 0 & 1 & 0 \ 0 & 0 & 0 & 0 \ 1 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_5 = \begin{pmatrix} 0 & 0 & -i & 0 \ 0 & 0 & 0 & 0 \ i & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_6 = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 1 & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}
$$

$$
\lambda_7 = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & -i & 0 \ 0 & i & 0 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_8 = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \ 0 & 0 & -2 & 0 \ 0 & 0 & 0 & 0 \end{pmatrix}
$$

### Generator yang Melibatkan Dimensi ke-4 (Generator 9-14)
Generator ini menghubungkan tiga baris/kolom pertama dengan baris/kolom keempat.

$$
\lambda_9 = \begin{pmatrix} 0 & 0 & 0 & 1 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ 1 & 0 & 0 & 0 \end{pmatrix}, \quad
\lambda_{10} = \begin{pmatrix} 0 & 0 & 0 & -i \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ i & 0 & 0 & 0 \end{pmatrix}
$$

$$
\lambda_{11} = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 1 \ 0 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \end{pmatrix}, \quad
\lambda_{12} = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & 0 & -i \ 0 & 0 & 0 & 0 \ 0 & i & 0 & 0 \end{pmatrix}
$$

$$
\lambda_{13} = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 1 \ 0 & 0 & 1 & 0 \end{pmatrix}, \quad
\lambda_{14} = \begin{pmatrix} 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & -i \ 0 & 0 & i & 0 \end{pmatrix}
$$

### Generator Diagonal Terakhir (Generator 15)
Generator diagonal ke-15 melengkapi himpunan generator $SU(4)$.

$$
\lambda_{15} = \frac{1}{\sqrt{6}} \begin{pmatrix} 1 & 0 & 0 & 0 \ 0 & 1 & 0 & 0 \ 0 & 0 & 1 & 0 \ 0 & 0 & 0 & -3 \end{pmatrix}
$$

## 4. Kesimpulan
Himpunan matriks $\{\lambda_1, \dots, \lambda_{15}\}$ di atas membentuk basis untuk aljabar Lie $\mathfrak{su}(4)$. Setiap matriks bersifat Hermitian dan memiliki trace nol, serta memenuhi relasi komutasi $[T_a, T_b] = i f_{abc} T_c$ di mana $f_{abc}$ adalah konstanta struktur dari grup $SU(4)$.
