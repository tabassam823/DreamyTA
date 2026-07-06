Penjelasan tersebut sebenarnya dapat diturunkan secara sistematis dari keadaan gabungan sistem–lingkungan. Mari kita mulai dari keadaan murni dan menunjukkan bagaimana matriks densitas yang ditampilkan muncul secara alami.

---

# 1. Keadaan Awal Sistem

Misalkan sistem kuantum berada dalam superposisi

$$|\psi_S\rangle = a|1\rangle+b|2\rangle,$$

dengan syarat normalisasi

$$|a|^2+|b|^2=1.$$

Lingkungan mula-mula berada pada keadaan

$$|e_0\rangle.$$

Maka keadaan gabungan sistem–lingkungan adalah

$$|\Psi_0\rangle=(a|1\rangle+b|2\rangle)\otimes |e_0\rangle.$$

Atau

$$|\Psi_0\rangle=a|1\rangle|e_0\rangle+b|2\rangle|e_0\rangle.$$

---

# 2. Interaksi dengan Lingkungan (Pembentukan Entanglement)

Ketika sistem berinteraksi dengan lingkungan, evolusi uniter menghasilkan

$$|1\rangle|e_0\rangle\rightarrow|1\rangle|e_1\rangle,$$

$$|2\rangle|e_0\rangle\rightarrow|2\rangle|e_2\rangle.$$

Karena evolusi kuantum bersifat linear,

$$|\Psi\rangle=a|1\rangle|e_1\rangle+b|2\rangle|e_2\rangle.$$

Inilah keadaan terbelit (entangled state).

---

# 3. Matriks Densitas Gabungan

Matriks densitas total adalah

$$\rho_{SE}= |\Psi\rangle\langle\Psi|.$$

Substitusikan keadaan di atas:

$$\rho_{SE}=\left(a|1,e_1\rangle+b|2,e_2\rangle\right)\left(a^*\langle1,e_1|+b^*\langle2,e_2|\right).$$

Kalikan satu per satu:

$$\rho_{SE}=|a|^2|1,e_1\rangle\langle1,e_1|+ab^*|1,e_1\rangle\langle2,e_2|+ba^*|2,e_2\rangle\langle1,e_1|+|b|^2|2,e_2\rangle\langle2,e_2|+ba^*|2,e_2\rangle\langle1,e_1|+|b|^2|2,e_2\rangle\langle2,e_2|.$
$$

---

# 4. Menghitung Matriks Densitas Sistem

Karena lingkungan tidak diamati, kita melakukan **partial trace** terhadap lingkungan:

$$\rho_S=\mathrm{Tr}*E(\rho*{SE}).$$

Gunakan definisi

$$\mathrm{Tr}_E(A)=\sum_n\langle e_n|A|e_n\rangle.$$

Mari hitung setiap suku.

---

### Suku pertama

$$
\mathrm{Tr}_E(|1,e_1\rangle\langle1,e_1|)= |1\rangle\langle1|\langle e_1|e_1\rangle.
$$

Karena

$$
\langle e_1|e_1\rangle=1,
$$

maka

$$
|1\rangle\langle1|.
$$

---

### Suku kedua

$$\mathrm{Tr}_E\Big(|1,e_1\rangle\langle2,e_2|\Big)= |1\rangle\langle2|\langle e_2|e_1\rangle.
$$

---

### Suku ketiga

$$\mathrm{Tr}_E\Big(|2,e_2\rangle\langle1,e_1|\Big)=|2\rangle\langle|\langle e_1|e_2\rangle.$$

---

### Suku keempat

$$\mathrm{Tr}_E\Big(|2,e_2\rangle\langle2,e_2|\Big)=|2\rangle\langle2|.
$$

---

Menggabungkan semuanya,

$$ \rho_S = |a|^2|1\rangle\langle1| + ab^* \langle e_2|e_1\rangle |1\rangle\langle2| + ba^* \langle e_1|e_2\rangle |2\rangle\langle1| + |b|^2|2\rangle\langle2|. $$

Dalam basis ({|1\rangle,|2\rangle}),

$$ \rho_S = \begin{bmatrix} |a|^2 & ab^*\langle e_2|e_1\rangle \\ ba^*\langle e_1|e_2\rangle & |b|^2 \end{bmatrix}. $$

Inilah matriks pertama pada gambar.

---

# 5. Dekoherensi

Akibat interaksi terus-menerus dengan lingkungan,

$$ |e_1\rangle \quad\text{dan}\quad |e_2\rangle $$

menjadi hampir ortogonal.

Secara matematis,

$$ \langle e_2|e_1\rangle \rightarrow 0. $$

Maka elemen off-diagonal menghilang:

$$ ab^*\langle e_2|e_1\rangle \rightarrow 0, $$

$$ ba^*\langle e_1|e_2\rangle \rightarrow 0. $$

Sehingga

$$ \rho_S \rightarrow \begin{bmatrix} |a|^2 & 0 \\ 0 & |b|^2 \end{bmatrix}. $$

---

# 6. Mengapa Ini Disebut Campuran Statistik?

Perhatikan bahwa

$$ \begin{bmatrix} |a|^2 & 0 \\ 0 & |b|^2 \end{bmatrix} = |a|^2 \begin{bmatrix} 1&0 \\ 0&0 \end{bmatrix} + |b|^2 \begin{bmatrix} 0&0 \\ 0&1 \end{bmatrix}. $$

Atau

$$ \rho_S = |a|^2|1\rangle\langle1| + |b|^2|2\rangle\langle2|. $$

Ini identik dengan deskripsi klasik:

* probabilitas (|a|^2) berada pada keadaan (|1\rangle),
* probabilitas (|b|^2) berada pada keadaan (|2\rangle).

Tidak ada lagi interferensi karena semua informasi fase relatif tersimpan di lingkungan.

---

# 7. Tahap Kolaps (Postulat Pengukuran)

Misalkan kita mengukur operator

$$ A = a_1|1\rangle\langle1| + a_2|2\rangle\langle2|. $$

Proyektor hasil pengukuran adalah

$$ P_1=|1\rangle\langle1|, \qquad P_2=|2\rangle\langle2|. $$

Menurut aturan Born,

$$ p_1 = \mathrm{Tr}(P_1\rho_S) = |a|^2, $$

$$ p_2 = \mathrm{Tr}(P_2\rho_S) = |b|^2. $$

Jika hasil (1) diperoleh, keadaan pasca-pengukuran menjadi

$$ \rho'_1 = \frac{P_1\rho_S P_1}{\mathrm{Tr}(P_1\rho_S)} = |1\rangle\langle1|. $$

Dalam bentuk matriks,

$$ \rho'_1 = \begin{bmatrix} 1&0 \\ 0&0 \end{bmatrix}. $$

Sebaliknya, jika hasil (2) diperoleh,

$$ \rho'_2 = |2\rangle\langle2|, $$

atau

$$ \rho'_2 = \begin{bmatrix} 0&0 \\ 0&1 \end{bmatrix}. $$

---

# Titik Penting Secara Konseptual

Dari sudut pandang matematika modern:

1. **Dekoherensi** dapat diturunkan langsung dari evolusi uniter sistem + lingkungan dan operasi partial trace.
2. Dekoherensi menjelaskan mengapa elemen off-diagonal hilang dan mengapa dunia tampak klasik.
3. Namun dekoherensi hanya menghasilkan

$$ \rho = \begin{bmatrix} |a|^2&0 \\ 0&|b|^2 \end{bmatrix}, $$

bukan salah satu hasil tunggal.

4. Langkah

$$ \begin{bmatrix} |a|^2&0 \\ 0&|b|^2 \end{bmatrix} \rightarrow \begin{bmatrix} 1&0 \\ 0&0 \end{bmatrix} \quad\text{atau}\quad \begin{bmatrix} 0&0 \\ 0&1 \end{bmatrix} $$

tidak berasal dari persamaan Schrödinger, melainkan dari **postulat pengukuran (projection postulate)**. Inilah yang dikenal sebagai *measurement problem* dalam fondasi mekanika kuantum.
