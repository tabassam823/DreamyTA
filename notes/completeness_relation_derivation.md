# Derivasi Hubungan Kelengkapan (Completeness Relation) dan Interpretasi Geometris

Catatan ini berisi penurunan rumus lengkap untuk *Completeness Relation* (Hubungan Kelengkapan) berdasarkan konsep basis ortonormal, serta penjelasan mendalam mengenai interpretasi grafis dari operator proyeksi.

## 1. Basis Ortonormal

Misalkan kita memiliki sebuah ruang vektor $\mathbb{C}^n$. Setiap himpunan $n$ vektor yang bebas linear {$|v_1\rangle, \dots, |v_n\rangle$} disebut sebagai **basis**.

Artinya, sembarang vektor $|x\rangle \in \mathbb{C}^n$ dapat ditulis secara unik sebagai kombinasi linear dari vektor-vektor basis tersebut:

$$
|x\rangle = \sum_{i=1}^n c_i |v_i\rangle
$$

Di mana $c_i$ adalah bilangan kompleks yang disebut sebagai **komponen** dari $|x\rangle$ terhadap basis tersebut.

### Syarat Ortonormalitas
Sebuah basis {$|e_i\rangle$} dikatakan **ortonormal** jika memenuhi syarat:

$$ 
\langle e_i | e_j \rangle = \delta_{ij} 
$$

Di mana $\delta_{ij}$ adalah *Kronecker delta*:
*   $\delta_{ij} = 1$ jika $i = j$ (vektor ternormalisasi/panjangnya 1).
*   $\delta_{ij} = 0$ jika $i \neq j$ (vektor saling tegak lurus/ortogonal).

## 2. Penurunan Rumus Completeness Relation

Tujuan kita adalah mencari bentuk operator yang jika dikerjakan pada sembarang vektor akan mengembalikan vektor itu sendiri (Operator Identitas), yang dibangun dari basis ortonormal.

### Langkah 1: Ekspansi Vektor
Ambil sembarang vektor $|x\rangle$. Kita ekspansikan dalam basis ortonormal {$|e_i\rangle$}:

$$ 
|x\rangle = \sum_{i=1}^n c_i |e_i\rangle 	...(Persamaan 1)
$$ 

Masalahnya sekarang adalah: **Berapa nilai koefisien $c_i$?**

### Langkah 2: Mencari Koefisien (Proyeksi)
Untuk mencari nilai $c_j$ (salah satu koefisien tertentu), kita kalikan (inner product) Persamaan 1 dengan *bra* $\langle e_j|$ dari kiri:

$$ 
\langle e_j | x \rangle = \langle e_j | 	\left( \sum_{i=1}^n c_i |e_i\rangle 	\right)
$$ 

Karena sifat linearitas *inner product*, kita bisa memasukkan $\langle e_j|$ ke dalam penjumlahan:

$$ 
\langle e_j | x \rangle = \sum_{i=1}^n c_i 	\langle e_j | e_i \rangle
$$ 

Gunakan sifat ortonormalitas $\langle e_j | e_i \rangle = \delta_{ji}$:

$$ 
\langle e_j | x \rangle = \sum_{i=1}^n c_i 	\delta_{ji}
$$ 

Dalam penjumlahan $\sum$, satu-satunya suku yang tidak nol adalah saat $i=j$. Maka:

$$ 
\langle e_j | x \rangle = c_j
$$ 

Jadi, kita menemukan bahwa koefisien $c_j$ hanyalah proyeksi vektor $|x\rangle$ pada basis $|e_j\rangle$.

### Langkah 3: Substitusi Kembali
Substitusikan nilai $c_i = \langle e_i | x \rangle$ kembali ke Persamaan 1. Perhatikan kita mengganti indeks $j$ kembali ke $i$ agar sesuai dengan notasi penjumlahan awal:

$$ 
|x\rangle = \sum_{i=1}^n 	\underbrace{\langle e_i | x \rangle}_{c_i} 	|e_i\rangle
$$ 

### Langkah 4: Rearrangement (Penyusunan Ulang)
Karena $\langle e_i | x \rangle$ adalah sebuah angka (skalar), kita bisa memindahkannya ke posisi mana saja (komutatif terhadap perkalian dengan vektor). Kita tulis di sebelah kanan ket $|e_i\rangle$:

$$ 
|x\rangle = \sum_{i=1}^n |e_i\rangle 	\langle e_i | x \rangle
$$ 

Sekarang, kita bisa "memisahkan" $|x\rangle$ dari penjumlahan tersebut. Perhatikan bahwa $|x\rangle$ ada di setiap suku sebagai faktor pengali di kanan:

$$ 
|x\rangle = 	\left( \sum_{i=1}^n |e_i\rangle 	\langle e_i | 	\right) |x\rangle
$$ 

### Langkah 5: Kesimpulan
Persamaan di atas menyatakan: "Operator dalam kurung, jika dikerjakan pada $|x\rangle$, menghasilkan $|x\rangle$ kembali".

Karena ini berlaku untuk **sembarang** vektor $|x\rangle$, maka operator dalam kurung tersebut pastilah **Operator Identitas ($I$)**.

$$ 
\sum_{i=1}^n |e_i\rangle 	\langle e_i | = I
$$ 

Inilah yang disebut **Completeness Relation** (Hubungan Kelengkapan). Ini menyatakan bahwa jumlah total dari semua proyektor ke arah basis ortonormal adalah sama dengan operator identitas.

---

## 3. Penjelasan Grafik (Proyeksi Operator)

Gambar (Figure 1.1) mengilustrasikan konsep **Operator Proyeksi** $P_k$ untuk satu dimensi basis.

### Definisi Operator Proyeksi
Suku $|e_k\rangle 	\langle e_k|$ disebut sebagai operator proyeksi ($P_k$) ke arah subruang yang direntang oleh vektor $|e_k\rangle$.

$$ 
P_k = |e_k\rangle 	\langle e_k|
$$ 

### Aksi pada Vektor $|v\rangle$
Jika operator ini bekerja pada vektor $|v\rangle$:
$$ 
P_k |v\rangle = |e_k\rangle 	\langle e_k | v \rangle = (\langle e_k | v \rangle) |e_k\rangle
$$ 
Hasilnya adalah sebuah vektor yang:
1.  Searah dengan $|e_k\rangle$.
2.  Panjangnya diskalakan sebesar $\langle e_k | v \rangle$ (proyeksi skalar $v$ pada $e_k$).

### Interpretasi Gambar
Dalam grafik tersebut terlihat dua komponen vektor:

1.  **$P_k |v\rangle$**:
    Ini adalah komponen dari $|v\rangle$ yang sejajar dengan basis $|e_k\rangle$. Ini adalah "bayangan" vektor $|v\rangle$ pada sumbu $|e_k\rangle$.

2.  **$|v\rangle - P_k |v\rangle$**:
    Ini adalah sisa vektor atau komponen "error". Vektor ini tegak lurus (ortogonal) terhadap $|e_k\rangle$.

    **Bukti Ortogonalitas:**
    Mari kita cek inner product antara $|e_k\rangle$ dan vektor sisa tersebut:
    $$ 
    \begin{aligned}
    \langle e_k | 	\left( |v\rangle - P_k |v\rangle \right) &= \langle e_k | v \rangle - \langle e_k | P_k | v \rangle \\
    &= \langle e_k | v \rangle - \langle e_k | e_k \rangle 	\langle e_k | v \rangle \\
    &= \langle e_k | v \rangle - (1) 	\langle e_k | v \rangle \\
    &= 0
    \end{aligned}
    $$ 
    Hasilnya 0, terbukti tegak lurus.

### Hubungan dengan Completeness Relation
Grafik hanya menunjukkan proyeksi ke **satu** basis $|e_k\rangle$. *Completeness relation* mengatakan bahwa jika kita menjumlahkan proyeksi ke **seluruh** basis ($k=1$ sampai $n$), kita akan menyusun ulang vektor $|v\rangle$ secara utuh:

$$ 
|v\rangle = \underbrace{P_1|v\rangle + P_2|v\rangle + \dots + P_n|v\rangle}_{\text{Jumlah seluruh proyeksi}}
$$ 

---

## 4. Gram-Schmidt Orthonormalization

Metode **Gram-Schmidt** adalah algoritma untuk mengubah himpunan sembarang vektor yang bebas linear {$|v_i\rangle$} (di mana $k \le n$) menjadi himpunan vektor ortonormal {$|e_i\rangle$} yang merentang subruang yang sama.

### Langkah 1: Vektor Pertama
Kita mulai dengan vektor pertama $|v_1\rangle$. Karena belum ada vektor basis lain, kita cukup menormalisasinya (membuat panjangnya menjadi 1).

$$ 
|e_1\rangle = 	\frac{|v_1\rangle}{\||v_1\rangle\|}
$$ 

Sekarang kita punya $\| |e_1\rangle \| = 1$.

### Langkah 2: Vektor Kedua
Kita ingin membuat $|e_2\rangle$ dari $|v_2\rangle$. Namun, $|v_2\rangle$ mungkin memiliki komponen yang sejajar dengan $|e_1\rangle$. Kita harus membuang komponen tersebut agar sisa vektornya tegak lurus terhadap $|e_1\rangle$.

Definisikan vektor sementara $|f_2\rangle$:
$$ 
|f_2\rangle = |v_2\rangle - \underbrace{|e_1\rangle\langle e_1|v_2\rangle}_{\text{Proyeksi } |v_2\rangle 	ext{ ke } |e_1\rangle}
$$ 

**Bukti Ortogonalitas:**
$$ 
\langle e_1 | f_2 \rangle = \langle e_1 | v_2 \rangle - \langle e_1 | e_1 \rangle 	\langle e_1 | v_2 \rangle
$$ 
Karena $\langle e_1 | e_1 \rangle = 1$, maka:
$$ 
\langle e_1 | f_2 \rangle = \langle e_1 | v_2 \rangle - \langle e_1 | v_2 \rangle = 0
$$ 
Jadi $|f_2\rangle \perp |e_1\rangle$.

Terakhir, normalisasi $|f_2\rangle$ untuk mendapatkan $|e_2\rangle$:
$$ 
|e_2\rangle = 	\frac{|f_2\rangle}{\||f_2\rangle\|}
$$ 

### Langkah Umum (Langkah ke-$j$)
Secara umum, untuk mendapatkan vektor basis ortonormal ke-$j$ ($|e_j\rangle$), kita ambil vektor asli $|v_j\rangle$ dan kurangi proyeksinya terhadap **semua** vektor basis ortonormal yang telah ditemukan sebelumnya ($|e_1\rangle, \dots, |e_{j-1}\rangle$).

$$ 
|e_j\rangle = 	\frac{|v_j\rangle - \sum_{i=1}^{j-1} \langle e_i | v_j \rangle |e_i\rangle}{\left\| |v_j\rangle - \sum_{i=1}^{j-1} \langle e_i | v_j \rangle |e_i\rangle \right\|}
$$ 

Atau ditulis dalam dua tahap:
1.  **Ortogonalisasi:**
    $$ 
    |f_j\rangle = |v_j\rangle - \sum_{i=1}^{j-1} |e_i\rangle 	\langle e_i | v_j \rangle
    $$ 
2.  **Normalisasi:**
    $$ 
    |e_j\rangle = 	\frac{|f_j\rangle}{\||f_j\rangle\|}
    $$ 

Proses ini diulang untuk $j=1$ sampai $k$. Hasil akhirnya adalah himpunan {$|e_1\rangle, \dots, |e_k\rangle$} yang bersifat ortonormal dan merentang ruang yang sama dengan vektor-vektor asal. Jika $k=n$, maka basis ini merentang seluruh ruang vektor $\mathbb{C}^n$.