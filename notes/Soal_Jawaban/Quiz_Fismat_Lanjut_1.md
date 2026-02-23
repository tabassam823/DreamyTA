# Jawaban Quiz Fisika Matematika Lanjut - Nomor 1

## Soal
Diberikan sebuah matriks densitas:
$$ho_1 = \begin{pmatrix} \frac{1+p}{4} & 0 & 0 & \frac{p}{2} \ 0 & \frac{1-p}{4} & 0 & 0 \ 0 & 0 & \frac{1-p}{4} & 0 \ \frac{p}{2} & 0 & 0 & \frac{1+p}{4} \end{pmatrix}$$
dengan $0 \le p \le 1$. Tunjukkan bahwa terdapat negativitas saat $p > 1/3$.

---

## Pembahasan

### 1. Kriteria PPT dan Negativitas
Untuk menentukan apakah sebuah keadaan kuantum bipartite (sistem dua-partikel) terjerat (*entangled*), kita dapat menggunakan kriteria **Partial Positive Transpose (PPT)** atau kriteria Peres-Horodecki. Keadaan dikatakan terjerat jika transpos parsial dari matriks densitasnya memiliki setidaknya satu nilai eigen negatif.

**Negativitas** ($\mathcal{N}$) didefinisikan sebagai jumlah absolut dari nilai-nilai eigen negatif dari matriks transpos parsial $ho^{T_B}$:
$$\mathcal{N}(ho) = \sum_i \frac{|\lambda_i| - \lambda_i}{2}$$
di mana $\lambda_i$ adalah nilai-eigen dari $ho^{T_B}$. Jika terdapat $\lambda_i < 0$, maka $\mathcal{N} > 0$.

### 2. Transpos Parsial ($ho_1^{T_B}$)
Misalkan sistem kita terdiri dari dua qubit $A$ dan $B$ dengan basis $\{|00angle, |01angle, |10angle, |11angle\}$. Matriks $ho_1$ dapat dituliskan dalam blok 2x2:
$$ho_1 = \begin{pmatrix} A & B \ C & D \end{pmatrix}$$
di mana:
$A = \begin{pmatrix} \frac{1+p}{4} & 0 \ 0 & \frac{1-p}{4} \end{pmatrix}$, $B = \begin{pmatrix} 0 & \frac{p}{2} \ 0 & 0 \end{pmatrix}$, $C = \begin{pmatrix} 0 & 0 \ \frac{p}{2} & 0 \end{pmatrix}$, $D = \begin{pmatrix} \frac{1-p}{4} & 0 \ 0 & \frac{1+p}{4} \end{pmatrix}$.

Transpos parsial terhadap subsistem $B$ didefinisikan sebagai:
$$ho_1^{T_B} = \begin{pmatrix} A^T & B^T \ C^T & D^T \end{pmatrix}$$
Maka kita peroleh:
$$ho_1^{T_B} = \begin{pmatrix} \frac{1+p}{4} & 0 & 0 & 0 \ 0 & \frac{1-p}{4} & \frac{p}{2} & 0 \ 0 & \frac{p}{2} & \frac{1-p}{4} & 0 \ 0 & 0 & 0 & \frac{1+p}{4} \end{pmatrix}$$

### 3. Perhitungan Nilai Eigen
Kita perlu mencari nilai eigen dari $ho_1^{T_B}$. Matriks ini berbentuk blok diagonal.

*   **Blok 1x1 pertama dan terakhir:**
    Memberikan nilai eigen:
    $$\lambda_1 = \frac{1+p}{4}$$
    $$\lambda_2 = \frac{1+p}{4}$$

*   **Blok 2x2 di tengah:**
    $$M = \begin{pmatrix} \frac{1-p}{4} & \frac{p}{2} \ \frac{p}{2} & \frac{1-p}{4} \end{pmatrix}$$
    Persamaan karakteristik: $\det(M - \lambda I) = 0$
    $$\left( \frac{1-p}{4} - \lambda ight)^2 - \left( \frac{p}{2} ight)^2 = 0$$
    $$\frac{1-p}{4} - \lambda = \pm \frac{p}{2}$$
    $$\lambda = \frac{1-p}{4} \mp \frac{p}{2}$$

    Maka diperoleh dua nilai eigen lainnya:
    $$\lambda_3 = \frac{1-p}{4} + \frac{2p}{4} = \frac{1+p}{4}$$
    $$\lambda_4 = \frac{1-3p}{4}$$

### 4. Analisis Syarat Negativitas
Agar terdapat negativitas, setidaknya satu nilai eigen harus negatif. Dari keempat nilai eigen:
1. $\lambda_1 = \frac{1+p}{4} \ge 0$ (karena $p \ge 0$)
2. $\lambda_2 = \frac{1+p}{4} \ge 0$
3. $\lambda_3 = \frac{1+p}{4} \ge 0$
4. $\lambda_4 = \frac{1-3p}{4}$

Syarat agar $\lambda_4 < 0$ adalah:
$$\frac{1-3p}{4} < 0$$
$$1 - 3p < 0$$
$$3p > 1$$
$$p > 1/3$$

### Kesimpulan
Telah ditunjukkan bahwa matriks transpos parsial $ho_1^{T_B}$ memiliki nilai eigen negatif $\lambda_4 = \frac{1-3p}{4}$ ketika $p > 1/3$. Oleh karena itu, **negativitas eksis (bernilai positif) jika dan hanya jika $p > 1/3$**, yang menandakan bahwa pada rentang tersebut keadaan $ho_1$ merupakan keadaan terjerat (*entangled state*).
