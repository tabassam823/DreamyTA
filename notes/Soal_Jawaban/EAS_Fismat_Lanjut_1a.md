```prompt
berikan aku jawaban untuk soal nomor 1 subnomor 1 pada file @Soal.md dengan megambil dua buat vektor dengan komponen terurut di mana $a \ge b$ pada interval $t \in [0, a-b]$ lalu mendefinisikan $\lambda = t/(a-b) \in [0,1] \Rightarrow t=\lambda (a-b). kemudian mengambil asumsi f konveks lalu menjumlahkan kedua fungsi ($f(a-t)$ dan $f(a+t)$)
```
**1. Buktikan bahwa $\sum_{i=1}^{n}f(x_i) \ge \sum_{i=1}^{n}f(y_i)$**

**Diberikan:**
*   Dua vektor riil $x = (x_1,..., x_n)$ dan $y = (y_1,..., y_n)$ dengan komponen yang terurut menurun: $x_1 ≥ x_2 ≥ ... ≥ x_n$ dan $y_1 ≥ y_2 ≥ ... ≥ y_n$.
*   $x$ memayorisasi $y$ ($x ≻ y$), yang berarti:
    *   $\sum_{i=1}^{k}x_i ≥ \sum_{i=1}^{k}y_i$ untuk semua $k=1,...,n-1$
    *   $\sum_{i=1}^{n}x_i = \sum_{i=1}^{n}y_i$
*   Fungsi $f: ℝ → ℝ$ yang kontinu dan konveks pada interval yang memuat $x_i$ dan $y_i$.

**Tujuan:**
Membuktikan $\sum_{i=1}^{n}f(x_i) ≥ \sum_{i=1}^{n}f(y_i)$.

**Strategi Pembuktian:**
1.  **Dekomposisi Majorisasi:** Menggunakan fakta bahwa jika $x ≻ y$, maka $y$ dapat diperoleh dari $x$ melalui serangkaian **transformasi-T** (T-transformations).
2.  **Efek Transformasi-T:** Membuktikan bahwa satu transformasi-T pada dua komponen akan mengurangi (atau mempertahankan) nilai total $\sum f(v_i)$ dengan menggunakan definisi fungsi konveks dan substitusi parameter yang diberikan.

---

**Langkah 1: Dekomposisi Majorisasi**
Berdasarkan teorema Hardy-Littlewood-Pólya, jika $x \succ y$, maka vektor $y$ dapat dicapai dari $x$ melalui urutan terbatas transformasi-T. Transformasi-T hanya mengubah dua komponen, katakanlah $x_j$ dan $x_k$ (dengan $x_j > x_k$), menjadi komponen baru $y_j$ dan $y_k$ sedemikian rupa sehingga:
*   $y_j + y_k = x_j + x_k$ (jumlah tetap)
*   $x_k \le y_k \le y_j \le x_j$ (komponen menjadi lebih dekat/kurang tersebar)

---

**Langkah 2: Membuktikan $f(x_j) + f(x_k) \ge f(y_j) + f(y_k)$ menggunakan parameter $\lambda$**

Misalkan kita mengambil dua komponen $a$ dan $b$ dari vektor $x$ dengan $a \ge b$.
Kita definisikan komponen baru $a'$ dan $b'$ yang lebih dekat satu sama lain dengan parameter $t \in [0, a-b]$:
$$a' = a - t \quad \text{dan} \quad b' = b + t$$
Sesuai arahan, kita definisikan parameter $\lambda \in [0, 1]$ sebagai:
$$\lambda = \frac{t}{a-b} \implies t = \lambda(a-b)$$

Sekarang kita nyatakan $a'$ dan $b'$ sebagai kombinasi konveks dari $a$ dan $b$:
1.  Untuk $a'$:
    $$a' = a - \lambda(a-b) = a - \lambda a + \lambda b = (1-\lambda)a + \lambda b$$
2.  Untuk $b'$:
    $$b' = b + \lambda(a-b) = b + \lambda a - \lambda b = \lambda a + (1-\lambda)b$$

Karena $f$ adalah fungsi **konveks**, maka berlaku definisi:
$$f((1-\lambda)x_1 + \lambda x_2) \le (1-\lambda)f(x_1) + \lambda f(x_2)$$

Terapkan pada $a'$ dan $b'$:
*   $f(a') = f((1-\lambda)a + \lambda b) \le (1-\lambda)f(a) + \lambda f(b)$
*   $f(b') = f(\lambda a + (1-\lambda)b) \le \lambda f(a) + (1-\lambda)f(b)$

Jika kita menjumlahkan kedua ketidaksamaan di atas:
$$f(a') + f(b') \le [(1-\lambda) + \lambda]f(a) + [\lambda + (1-\lambda)]f(b)$$
$$f(a') + f(b') \le 1 \cdot f(a) + 1 \cdot f(b)$$
$$f(a) + f(b) \ge f(a') + f(b')$$

Ini membuktikan bahwa setiap langkah transformasi-T (yang memindahkan komponen lebih dekat ke rata-rata) akan mengurangi atau mempertahankan nilai total dari jumlah fungsi konveks tersebut.

---

**Langkah 3: Kesimpulan**
Karena majorisasi $x \succ y$ menjamin bahwa $y$ dapat diperoleh dari $x$ melalui urutan transformasi-T yang masing-masing memenuhi $f(x_j) + f(x_k) \ge f(y_j) + f(y_k)$, maka secara keseluruhan berlaku:
$$\sum_{i=1}^{n}f(x_i) \ge \sum_{i=1}^{n}f(y_i)$$