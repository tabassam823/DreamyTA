```prompt
Hitunglah partial transpose $\rho^{T_B}$ dari state $\rho = \frac{1}{9}(\mathbb{I} - p)$. Tunjukkan bahwa karena setiap state $\ket{\psi_k}$ dalam pembentuk proyektor $p$ adalah state produk dengan koefisien riil, maka $p^{T_B} = p$. Gunakan hasil ini untuk membuktikan bahwa $\rho^{T_B}$ memiliki eigenvalue yang non-negatif (PPT state).
```
**2.b. Hitung partial transpose $\rho^{T_B}$ dan tunjukkan $\rho^{T_B} \ge 0$**

**Diberikan:**
*   State campuran $\rho = \frac{1}{9} (\mathbb{I} - p)$, dengan $p = \sum_{k=1}^5 \ket{\psi_k}\bra{\psi_k}$.
*   Kumpulan state produk $\{\ket{\psi_k}\}$ (UPB):
    1.  $\ket{\psi_1} = \ket{0} \otimes \frac{1}{\sqrt2}(\ket{0}-\ket{1})$
    2.  $\ket{\psi_2} = \ket{2} \otimes \frac{1}{\sqrt2}(\ket{1}-\ket{2})$
    3.  $\ket{\psi_3} = \frac{1}{\sqrt2}(\ket{0}-\ket{1}) \otimes \ket{2}$
    4.  $\ket{\psi_4} = \frac{1}{\sqrt2}(\ket{1}-\ket{2}) \otimes \ket{0}$
    5.  $\ket{\psi_5} = \frac{1}{3}(\ket{0}+\ket{1}+\ket{2}) \otimes (\ket{0}+\ket{1}+\ket{2})$

**Tujuan:**
1.  Menghitung $\rho^{T_B}$ (partial transpose terhadap subsistem B).
2.  Membuktikan bahwa $\rho^{T_B}$ adalah operator positif semi-definit ($\rho^{T_B} \ge 0$).

---

**Langkah 1: Analisis Partial Transpose pada State Produk**

Secara umum, partial transpose terhadap subsistem B dari sebuah operator produk $A \otimes B$ didefinisikan sebagai $(A \otimes B)^{T_B} = A \otimes B^T$. 

Untuk sebuah proyektor state produk murni $\ket{\psi}\bra{\psi} = (\ket{u}\bra{u}) \otimes (\ket{v}\bra{v})$, partial transpose-nya adalah:
$$(\ket{\psi}\bra{\psi})^{T_B} = \ket{u}\bra{u} \otimes (\ket{v}\bra{v})^T$$

Dalam basis komputasional riil, $(\ket{v}\bra{v})^T$ sama dengan konjugat kompleksnya $(\ket{v}\bra{v})^*$. Jika vektor $\ket{v}$ hanya memiliki komponen riil (seperti pada semua $\ket{\psi_k}$ di atas), maka $(\ket{v}\bra{v})^T = \ket{v}\bra{v}$.

Karena setiap $\ket{\psi_k}$ adalah state produk dengan koefisien riil, maka:
$$(\ket{\psi_k}\bra{\psi_k})^{T_B} = \ket{\psi_k}\bra{\psi_k}$$
Sehingga partial transpose dari operator proyeksi $p$ adalah:
$$p^{T_B} = \left( \sum_{k=1}^5 \ket{\psi_k}\bra{\psi_k} \right)^{T_B} = \sum_{k=1}^5 \ket{\psi_k}\bra{\psi_k} = p$$

---

**Langkah 2: Menghitung $\rho^{T_B}$**

Menggunakan sifat linearitas dari operasi partial transpose:
$$\rho^{T_B} = \left[ \frac{1}{9} (\mathbb{I} - p) \right]^{T_B} = \frac{1}{9} (\mathbb{I}^{T_B} - p^{T_B})$$
Diketahui bahwa $\mathbb{I}^{T_B} = \mathbb{I}$ dan dari Langkah 1 kita peroleh $p^{T_B} = p$. Maka:
$$\rho^{T_B} = \frac{1}{9} (\mathbb{I} - p) = \rho$$

Hasil ini menunjukkan bahwa state $\rho$ bersifat invariant di bawah operasi partial transpose terhadap subsistem B.

---

**Langkah 3: Membuktikan Positivitas ($\rho^{T_B} \ge 0$)**

Untuk menunjukkan $\rho^{T_B} \ge 0$, kita cukup memeriksa eigenvalue dari $\rho$.
1.  Operator $p$ adalah proyektor pada subruang $S$ berdimensi 5. Maka $p$ memiliki eigenvalue:
    *   $\lambda = 1$ dengan multiplisitas 5.
    *   $\lambda = 0$ dengan multiplisitas $9 - 5 = 4$.
2.  Operator $(\mathbb{I} - p)$ adalah proyektor pada subruang ortogonal $S^\perp$. Eigenvalue-nya adalah:
    *   $(1 - 1) = 0$ dengan multiplisitas 5.
    *   $(1 - 0) = 1$ dengan multiplisitas 4.
3.  Operator $\rho = \frac{1}{9}(\mathbb{I} - p)$ memiliki eigenvalue:
    *   $0$ (sebanyak 5).
    *   $1/9$ (sebanyak 4).

Karena semua eigenvalue dari $\rho$ (dan karena itu $\rho^{T_B}$) adalah non-negatif ($0$ atau $1/9$), maka terbukti bahwa:
$$\rho^{T_B} \ge 0$$

---

**Kesimpulan:**
State $\rho$ memiliki partial transpose yang positif semi-definit ($\rho^{T_B} \ge 0$). Karena pada subnomor sebelumnya telah dibuktikan bahwa $\rho$ adalah entangled, maka $\rho$ merupakan contoh dari **PPT Entangled State** (atau *Bound Entangled State*). $\square$
