# Operator Linear dan Matriks

Catatan ini menjelaskan hubungan antara operator linear dan representasi matriksnya dalam sebuah basis ortonormal, serta menurunkan bagaimana elemen-elemen matriks didapatkan.

## 1. Definisi Operator Linear

Sebuah pemetaan $A : \mathbb{C}^n \to \mathbb{C}^n$ disebut sebagai **operator linear** jika memenuhi sifat linearitas berikut:

$$
A(c_1|x\rangle + c_2|y\rangle) = c_1 A|x\rangle + c_2 A|y\rangle
$$

untuk sembarang vektor $|x\rangle, |y\rangle \in \mathbb{C}^n$ dan skalar kompleks $c_1, c_2 \in \mathbb{C}$.

Artinya, operator $A$ bekerja pada kombinasi linear vektor dengan cara bekerja pada masing-masing vektor lalu mengombinasikan hasilnya dengan koefisien yang sama.

## 2. Representasi Matriks dari Operator Linear

Kita akan menunjukkan bahwa setiap operator linear $A$ dapat direpresentasikan sebagai sebuah matriks $n \times n$ jika kita memilih sebuah basis ortonormal {$|e_k\rangle$}.

### Aksi pada Vektor Sembarang
Misalkan $|v\rangle$ adalah sembarang vektor di $\mathbb{C}^n$. Kita dapat mengekspansinya dalam basis ortonormal {$|e_k\rangle$}:

$$|v\rangle = \sum_{k=1}^n v_k |e_k\rangle$$

Terapkan operator $A$ pada $|v\rangle$. Karena sifat linearitas (Persamaan 1.20), kita bisa memasukkan $A$ ke dalam penjumlahan:

$$A|v\rangle = A \left( \sum_{k=1}^n v_k |e_k\rangle \right) = \sum_{k=1}^n v_k A|e_k\rangle$$

Persamaan ini menunjukkan poin penting: **Aksi operator $A$ pada sembarang vektor sepenuhnya ditentukan oleh aksinya pada vektor-vektor basis.** Jika kita tahu ke mana $A$ memetakan setiap $|e_k\rangle$, kita tahu ke mana $A$ memetakan *semua* vektor.

### Ekspansi Aksi pada Basis
Hasil dari operasi $A|e_k\rangle$ adalah sebuah vektor baru di $\mathbb{C}^n$. Oleh karena itu, vektor hasil ini pun bisa diekspansi kembali dalam basis {|$e_i\rangle$} yang sama.

$$A|e_k\rangle = \sum_{i=1}^n A_{ik} |e_i\rangle$$

Di sini, $A_{ik}$ adalah koefisien ekspansi (komponen) dari vektor $A|e_k\rangle$ pada basis $|e_i\rangle$.
*   Indeks $k$ menunjukkan vektor basis asal yang dikenai operator.
*   Indeks $i$ menunjukkan komponen basis tujuan.

### Mencari Elemen Matriks ($A_{jk}$)
Untuk mendapatkan nilai skalar $A_{jk}$, kita ambil *inner product* persamaan di atas dengan bra $\langle e_j|$ dari kiri:

$$ \langle e_j | A | e_k \rangle = \langle e_j | \left( \sum_{i=1}^n A_{ik} |e_i\rangle \right) $$

Keluarkan konstanta $A_{ik}$ dari inner product:

$$ \langle e_j | A | e_k \rangle = \sum_{i=1}^n A_{ik} \langle e_j | e_i \rangle $$

Gunakan sifat ortonormalitas $\langle e_j | e_i \rangle = \delta_{ji}$:

$$ \langle e_j | A | e_k \rangle = \sum_{i=1}^n A_{ik} \delta_{ji} $$

Suku penjumlahan hanya bernilai tidak nol saat $i=j$, sehingga:

$$A_{jk} = \langle e_j | A | e_k \rangle$$

Ini adalah rumus untuk **elemen matriks** dari operator $A$ dalam basis {|$e_k\rangle$}. $A_{jk}$ adalah elemen pada baris ke-$j$ dan kolom ke-$k$.

---

## 3. Rekonstruksi Operator dari Elemen Matriks

Kita juga bisa membuktikan hubungan sebaliknya: bagaimana operator $A$ dituliskan kembali menggunakan elemen-elemen matriksnya.

$$A = \sum_{j,k} A_{jk} |e_j\rangle \langle e_k|$$

### Bukti Menggunakan Completeness Relation
Kita mulai dengan identitas $A = I A I$, di mana $I$ adalah operator identitas.
Ingat *Completeness Relation*: $I = \sum_{i} |e_i\rangle \langle e_i|$.

Kita selipkan $I$ di kiri dan kanan $A$:

$$A = \left( \sum_{j=1}^n |e_j\rangle \langle e_j| \right) A \left( \sum_{k=1}^n |e_k\rangle \langle e_k| \right)$$

Gabungkan kedua penjumlahan (karena indeks $j$ dan $k$ independen):

$$A = \sum_{j=1}^n \sum_{k=1}^n |e_j\rangle \underbrace{\langle e_j | A | e_k \rangle}_{\text{Definisi } A_{jk}} \langle e_k|$$

Substitusikan definisi $A_{jk} = \langle e_j | A | e_k \rangle$:

$$A = \sum_{j,k} A_{jk} |e_j\rangle \langle e_k|$$

### Interpretasi
Persamaan ini menyatakan bahwa operator $A$ dapat dipandang sebagai penjumlahan (superposisi) dari operator-operator $|e_j\rangle \langle e_k|$ yang diberi bobot sebesar $A_{jk}$.
*   Operator $|e_j\rangle \langle e_k|$ mengambil input yang searah $|e_k\rangle$ dan mengubahnya menjadi output yang searah $|e_j\rangle$.
*   $A_{jk}$ adalah "kekuatan" atau amplitudo transisi dari keadaan $k$ ke keadaan $j$.

---

## 4. Konjugat Hermitian, Matriks Hermitian, dan Matriks Unitary

Konsep matriks Hermitian sangat krusial dalam fisika kuantum karena besaran yang dapat diobservasi (observables) direpresentasikan oleh operator Hermitian.

### 4.1 Konjugat Hermitian ($A^\dagger$)

**Definisi:**
Diberikan operator linear $A: \mathbb{C}^n \to \mathbb{C}^n$, konjugat Hermitiannya, dilambangkan dengan $A^\dagger$ (dibaca "A dagger"), didefinisikan melalui hubungan *inner product* berikut:

$$ \langle u | A | v \rangle \equiv \langle A^\dagger u | v \rangle = \langle v | A^\dagger | u \rangle^* $$

untuk sembarang vektor $|u\rangle, |v\rangle \in \mathbb{C}^n$.

**Hubungan Elemen Matriks:**
Elemen matriks dari $A^\dagger$ dapat diturunkan dari definisi di atas. Misalkan $|u\rangle = |e_j\rangle$ dan $|v\rangle = |e_k\rangle$, maka:

$$ (A^\dagger)_{jk} = \langle e_j | A^\dagger | e_k \rangle $$

Berdasarkan definisi di atas (dan sifat konjugat kompleks $\langle a|b\rangle = \langle b|a\rangle^*$):
$$ \langle e_j | A^\dagger | e_k \rangle = \langle A e_j | e_k \rangle = \langle e_k | A | e_j \rangle^* = (A_{kj})^* $$

Sehingga kita mendapatkan hubungan:

$$ (A^\dagger)_{jk} = A_{kj}^* $$

Ini berarti matriks $A^\dagger$ diperoleh dengan melakukan **transpose** pada matriks $A$ (menukar baris dan kolom $j \leftrightarrow k$), lalu mengambil **konjugat kompleks** dari setiap elemennya.

**Sifat-sifat:**
1.  $(cA)^\dagger = c^* A^\dagger$ (untuk skalar $c \in \mathbb{C}$)
2.  $(A + B)^\dagger = A^\dagger + B^\dagger$
3.  $(AB)^\dagger = B^\dagger A^\dagger$ (urutan dibalik)
4.  $|x\rangle^\dagger = \langle x|$ (Ket menjadi Bra adalah operasi Hermitian Conjugate)

---

### 4.2 Matriks Hermitian

Sebuah operator atau matriks $A$ disebut **Hermitian** jika ia sama dengan konjugat Hermitian-nya sendiri:

$$ A^\dagger = A $$

Dalam bentuk elemen matriks, ini berarti:
$$ A_{ji}^* = A_{ij} $$
Implikasinya, elemen diagonal ($i=j$) haruslah bilangan real ($A_{ii}^* = A_{ii}$), yang merupakan alasan mengapa operator Hermitian dalam mekanika kuantum menghasilkan nilai eigen (hasil pengukuran) yang real.

---

### 4.3 Matriks Unitary

Sebuah operator atau matriks $U$ disebut **Unitary** jika inversnya sama dengan konjugat Hermitian-nya:

$$ U^\dagger = U^{-1} \quad \text{atau} \quad U^\dagger U = I $$

**Sifat Penting:**
Operator Unitary mempertahankan *inner product* (dan karenanya mempertahankan panjang vektor/norm).
Jika kita memetakan basis ortonormal {$|e_k\rangle$} menggunakan $U$ menjadi himpunan vektor baru {$|f_k\rangle$} di mana $|f_k\rangle = U|e_k\rangle$, maka basis baru tersebut **tetap ortonormal**:

$$ \begin{aligned} \langle f_j | f_k \rangle &= \langle U e_j | U e_k \rangle \\ &= \langle e_j | U^\dagger U | e_k \rangle \\ &= \langle e_j | I | e_k \rangle \\ &= \delta_{jk} \end{aligned} $$

**Determinan:**
Karena $U^\dagger U = I$, maka:
$$ \det(U^\dagger U) = \det(U^\dagger) \det(U) = (\det U)^* (\det U) = |\det U|^2 = 1 $$
Jadi, modulus dari determinan matriks unitary adalah 1 ($|\det U| = 1$).

*   **Special Unitary Group SU(n):** Himpunan matriks unitary $n \times n$ dengan syarat tambahan $\det U = 1$.
*   **Orthogonal Group O(n):** Analogi untuk matriks real ($A : \mathbb{R}^n \to \mathbb{R}^n$) di mana $A^T = A^{-1}$. Jika $\det A = 1$, disebut Special Orthogonal Group SO(n).
