# Jawaban Soal 4a dan 4b: Dekomposisi SU(4)

## 4a. Dekomposisi Perkalian Langsung SU(4)

Soal meminta dekomposisi dari perkalian antara representasi simetris rank-2 dan representasi fundamental $SU(4)$.

### Identifikasi Representasi:
1.  **Representasi Pertama**: $\begin{array}{|c|c|c|} \hline ~ & ~ \ \hline \end{array}$ (Dua kotak mendatar)
    - Ini adalah representasi simetris dari $\mathbf{4} \otimes \mathbf{4}$.
    - Dimensinya untuk $SU(4)$ adalah: $d = \frac{n(n+1)}{2} = \frac{4(5)}{2} = \mathbf{10}$.
2.  **Representasi Kedua**: $\begin{array}{|c|c|c|} \hline ~  \ \hline \end{array}$ (Satu kotak)
    - Ini adalah representasi fundamental $\mathbf{4}$.

### Operasi Young Tableaux:
Perkalian $	iny\yng(2) \otimes \yng(1)$ dilakukan dengan menambahkan kotak dari representasi kedua ke representasi pertama mengikuti aturan standar (tidak ada dua kotak dengan label yang sama dalam satu kolom, dan bentuk hasil harus legal).

$$
\begin{array}{|c|c|c|} \hline ~ & ~ \ \hline \end{array}
\space \otimes \space
\begin{array}{|c|c|c|} \hline ~  \ \hline \end{array} 
= 
\begin{array}{|c|c|c|c|} \hline ~ & ~ & ~ \ \hline \end{array}
\space \oplus \space
\begin{array}{|c|c|c|} \hline ~ & ~ \ \hline ~ \ \hline \end{array}
$$

### Perhitungan Dimensi:
Menggunakan rumus Hook Length untuk $SU(4)$:

1.  **Representasi $	iny\yng(3)$ (Simetris Penuh)**:
    - Rumus: $d = \frac{n(n+1)(n+2)}{3 \cdot 2 \cdot 1} = \frac{4 \cdot 5 \cdot 6}{6} = \mathbf{20}$.
2.  **Representasi $	iny\yng(2,1)$ (Simetri Campuran)**:
    - Panjang Hook: (Kotak 1,1)=3, (1,2)=1, (2,1)=1.
    - Nilai Numerator: (1,1)=4, (1,2)=5, (2,1)=3.
    - $d = \frac{4 \cdot 5 \cdot 3}{3 \cdot 1 \cdot 1} = \mathbf{20}$.

**Hasil Akhir:**
$$\mathbf{10} \otimes \mathbf{4} = \mathbf{20}_S \oplus \mathbf{20}_M$$
(Sering juga ditulis sebagai $\mathbf{20} \oplus \mathbf{20}'$ dalam literatur $SU(4)$).

---

## 4b. Basis Representasi Tak Tereduksi

Basis untuk representasi-representasi hasil dekomposisi di atas dalam terminologi tensor adalah:

### 1. Basis Representasi $\mathbf{20}_S$ (Simetris Penuh)
Representasi ini diwakili oleh tensor rank-3 yang simetris terhadap semua pertukaran indeks:
$$T^{(ijk)} \quad 	ext{di mana } i, j, k \in \{1, 2, 3, 4\}$$
Syarat simetri: $T^{ijk} = T^{jik} = T^{ikj}$, dsb.
Jumlah komponen independen adalah $\binom{4+3-1}{3} = \binom{6}{3} = 20$.

### 2. Basis Representasi $\mathbf{20}_M$ (Simetri Campuran)
Representasi ini diwakili oleh tensor $T^{ij,k}$ yang simetris pada dua indeks pertama ($i,j$) namun memenuhi syarat siklik (identitas Bianchi-like) yang membuatnya ortogonal terhadap tensor simetris penuh:
- $T^{ij,k} = T^{ji,k}$
- $T^{ij,k} + T^{jk,i} + T^{ki,j} = 0$

Secara fisik, jika kita menggunakan basis quark $SU(4)$ (u, d, s, c), maka $\mathbf{20}_S$ merepresentasikan dekouplet baryon yang diperluas ke $SU(4)$ (seperti $\Delta^{++}, \Omega^-, C_{ccc}^{++}$), sedangkan $\mathbf{20}_M$ merepresentasikan oktet baryon yang diperluas (seperti proton, neutron, dan baryon-baryon terpesona/charmed lainnya).
