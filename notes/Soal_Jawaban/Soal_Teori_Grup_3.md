# Jawaban Soal 3a dan 3b: Interaksi Dua Partikel Spin-1

## 3a. Representasi Matriks Operator Penaik dan Penurun

Untuk partikel tunggal dengan momentum sudut (spin) $l=1$, terdapat 3 keadaan basis: $|1, 1angle, |1, 0angle, |1, -1angle$.
Operator penaik ($L_+$) dan penurun ($L_-$) bekerja sebagai berikut:
$$L_\pm |l, mangle = \sqrt{l(l+1) - m(m \pm 1)} |l, m \pm 1angle$$

Dalam basis matriks $3 	imes 3$:
$$L_+ = \begin{pmatrix} 0 & \sqrt{2} & 0 \ 0 & 0 & \sqrt{2} \ 0 & 0 & 0 \end{pmatrix}, \quad L_- = \begin{pmatrix} 0 & 0 & 0 \ \sqrt{2} & 0 & 0 \ 0 & \sqrt{2} & 0 \end{pmatrix}$$

Untuk sistem dua partikel ($l_1=1, l_2=1$), ruang Hilbert memiliki dimensi $3 	imes 3 = 9$. Operator total dalam representasi perkalian langsung (uncoupled) adalah:
$$\mathcal{L}_\pm = (L_\pm \otimes I) + (I \otimes L_\pm)$$
di mana $I$ adalah matriks identitas $3 	imes 3$.

Hasilnya adalah matriks $9 	imes 9$ yang bersifat blok-diagonal atau sparse. Sebagai contoh, elemen matriks untuk $\mathcal{L}_+$ adalah:
$$\mathcal{L}_+ = L_+ \otimes I + I \otimes L_+$$
(Secara eksplisit, matriks ini menghubungkan keadaan $|m_1, m_2angle$ ke $|m_1+1, m_2angle$ dan $|m_1, m_2+1angle$).

---

## 3b. Semua Kemungkinan Keadaan Gabungan

Penjumlahan dua momentum sudut $l_1=1$ dan $l_2=1$ menghasilkan total momentum sudut $J$ yang berkisar dari $|l_1 - l_2|$ hingga $l_1 + l_2$.
$$J = 0, 1, 2$$

Dekomposisi representasinya adalah: $3 \otimes 3 = 5 \oplus 3 \oplus 1$.

### 1. Quintet ($J=2$) - Simetris
Terdapat 5 keadaan:
- $|2, 2angle = |1, 1angle$
- $|2, 1angle = \frac{1}{\sqrt{2}}(|1, 0angle + |0, 1angle)$
- $|2, 0angle = \frac{1}{\sqrt{6}}(|1, -1angle + 2|0, 0angle + |-1, 1angle)$
- $|2, -1angle = \frac{1}{\sqrt{2}}(|0, -1angle + |-1, 0angle)$
- $|2, -2angle = |-1, -1angle$

### 2. Triplet ($J=1$) - Anti-simetris
Terdapat 3 keadaan:
- $|1, 1angle = \frac{1}{\sqrt{2}}(|1, 0angle - |0, 1angle)$
- $|1, 0angle = \frac{1}{\sqrt{2}}(|1, -1angle - |-1, 1angle)$
- $|1, -1angle = \frac{1}{\sqrt{2}}(|0, -1angle - |-1, 0angle)$

### 3. Singlet ($J=0$) - Simetris
Terdapat 1 keadaan:
- $|0, 0angle = \frac{1}{\sqrt{3}}(|1, -1angle - |0, 0angle + |-1, 1angle)$

Keadaan-keadaan di atas dinyatakan dalam basis $|m_1, m_2angle$. Koefisien di depan setiap suku adalah Koefisien Clebsch-Gordan.
