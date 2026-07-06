# Jawaban Quiz Fisika Matematika Lanjut - Nomor 2

## Soal
Diberikan sebuah matriks densitas:
$$ho_2 = \begin{pmatrix} \frac{p}{2} & 0 & 0 & \frac{p}{2} \ 0 & \frac{1-p}{2} & \frac{1-p}{2} & 0 \ 0 & \frac{1-p}{2} & \frac{1-p}{2} & 0 \ \frac{p}{2} & 0 & 0 & \frac{p}{2} \end{pmatrix} ; \space 0 \le p \le 1$$
Tunjukkan bahwa negativitas tidak eksis hanya untuk $p=1/2$.

---

## Pembahasan

### 1. Definisi Transpos Parsial
Sebagaimana pada nomor sebelumnya, kita menggunakan kriteria PPT. Negativitas tidak eksis jika semua nilai eigen dari matriks transpos parsial $ho^{T_B}$ bernilai non-negatif ($\lambda_i \ge 0$).

Operasi transpos parsial terhadap subsistem kedua ($B$) pada basis $\{|00angle, |01angle, |10angle, |11angle\}$ memetakan elemen matriks sebagai berikut:
$$\langle i,j | ho | k,l angle \xrightarrow{T_B} \langle i,l | ho | k,j angle$$

### 2. Konstruksi Matriks $ho_2^{T_B}$
Diberikan $ho_2$:
- $\langle 00 | ho_2 | 00 angle = p/2$, $\langle 00 | ho_2 | 11 angle = p/2$
- $\langle 01 | ho_2 | 01 angle = (1-p)/2$, $\langle 01 | ho_2 | 10 angle = (1-p)/2$
- $\langle 10 | ho_2 | 01 angle = (1-p)/2$, $\langle 10 | ho_2 | 10 angle = (1-p)/2$
- $\langle 11 | ho_2 | 00 angle = p/2$, $\langle 11 | ho_2 | 11 angle = p/2$

Melakukan transpos parsial pada indeks kedua:
- $|00angle\langle 11| 	o |01angle\langle 10|$ dengan nilai $p/2$
- $|01angle\langle 10| 	o |00angle\langle 11|$ dengan nilai $(1-p)/2$
- $|10angle\langle 01| 	o |11angle\langle 00|$ dengan nilai $(1-p)/2$
- $|11angle\langle 00| 	o |10angle\langle 01|$ dengan nilai $p/2$

Matriks $ho_2^{T_B}$ menjadi:
$$ho_2^{T_B} = \begin{pmatrix} \frac{p}{2} & 0 & 0 & \frac{1-p}{2} \ 0 & \frac{1-p}{2} & \frac{p}{2} & 0 \ 0 & \frac{p}{2} & \frac{1-p}{2} & 0 \ \frac{1-p}{2} & 0 & 0 & \frac{p}{2} \end{pmatrix}$$

### 3. Perhitungan Nilai Eigen
Matriks $ho_2^{T_B}$ adalah matriks blok diagonal (setelah permutasi baris/kolom) yang terdiri dari dua blok $2 	imes 2$.

*   **Blok 1 (Elemen pojok):**
    $$M_1 = \begin{pmatrix} \frac{p}{2} & \frac{1-p}{2} \ \frac{1-p}{2} & \frac{p}{2} \end{pmatrix}$$
    Nilai eigennya adalah $\lambda = \frac{p}{2} \pm \frac{1-p}{2}$:
    $$\lambda_1 = \frac{p + 1 - p}{2} = \frac{1}{2}$$
    $$\lambda_2 = \frac{p - (1-p)}{2} = \frac{2p - 1}{2} = p - \frac{1}{2}$$

*   **Blok 2 (Elemen tengah):**
    $$M_2 = \begin{pmatrix} \frac{1-p}{2} & \frac{p}{2} \ \frac{p}{2} & \frac{1-p}{2} \end{pmatrix}$$
    Nilai eigennya adalah $\lambda = \frac{1-p}{2} \pm \frac{p}{2}$:
    $$\lambda_3 = \frac{1-p+p}{2} = \frac{1}{2}$$
    $$\lambda_4 = \frac{1-p-p}{2} = \frac{1-2p}{2} = \frac{1}{2} - p$$

Himpunan nilai eigen $ho_2^{T_B}$ adalah: $\{ \frac{1}{2}, \frac{1}{2}, p - \frac{1}{2}, \frac{1}{2} - p \}$.

### 4. Analisis Keberadaan Negativitas
Negativitas **tidak eksis** jika dan hanya jika semua nilai eigen $\ge 0$.
Mari kita periksa syarat tersebut:
1. $\lambda_1, \lambda_3 = 1/2 > 0$ (selalu terpenuhi)
2. $\lambda_2 = p - 1/2 \ge 0 \implies p \ge 1/2$
3. $\lambda_4 = 1/2 - p \ge 0 \implies p \le 1/2$

Agar kedua syarat (2 dan 3) terpenuhi secara bersamaan:
$$p \ge 1/2 \quad 	ext{dan} \quad p \le 1/2 \implies p = 1/2$$

*   Jika $p > 1/2$, maka $\lambda_4 < 0$ (Negativitas eksis).
*   Jika $p < 1/2$, maka $\lambda_2 < 0$ (Negativitas eksis).
*   Jika $p = 1/2$, maka $\lambda_2 = 0$ dan $\lambda_4 = 0$ (Tidak ada nilai eigen negatif).

### Kesimpulan
Telah ditunjukkan bahwa matriks transpos parsial $ho_2^{T_B}$ memiliki setidaknya satu nilai eigen negatif untuk setiap nilai $p \in [0, 1]$ kecuali saat $p = 1/2$. Oleh karena itu, **negativitas tidak eksis hanya untuk $p = 1/2$**. Pada titik ini, matriks $ho_2$ merepresentasikan keadaan yang *separable*.
