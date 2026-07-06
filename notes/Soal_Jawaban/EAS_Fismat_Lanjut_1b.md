```prompt
lanjut ke nomor 1 subnomor 2 dengan megambil definisi dari jawaban subnomor 1 lalu memproses fungsi definisinya dengan menganggap f strictly konveks sehingga pada akhirnya akan menunjukkan hal yang kontradiktif
```

**1.2. Tunjukkan bahwa kesetaraan $\sum_{i=1}^{n}f(x_i) = \sum_{i=1}^{n}f(y_i)$ terjadi jika dan hanya jika $x$ dan $y$ adalah permutasi satu sama lain.**

**Diberikan:**
*   Dua vektor riil $x$ dan $y$ dengan komponen terurut menurun ($x_1 \ge \dots \ge x_n$ dan $y_1 \ge \dots \ge y_n$).
*   $x$ memayorisasi $y$ ($x \succ y$).
*   Fungsi $f: \mathbb{R} \to \mathbb{R}$ yang kontinu dan **strictly convex**.

**Tujuan:**
Membuktikan bahwa $\sum_{i=1}^{n}f(x_i) = \sum_{i=1}^{n}f(y_i) \iff x \text{ adalah permutasi } y$.

---

**Pembuktian Bagian "Jika" ($\Leftarrow$):**
Jika $x$ adalah permutasi dari $y$ dan keduanya terurut menurun, maka $x_i = y_i$ untuk semua $i$. Jelas bahwa $\sum f(x_i) = \sum f(y_i)$.

---

**Pembuktian Bagian "Hanya Jika" ($\Rightarrow$):**

Asumsikan $\sum_{i=1}^{n} f(x_i) = \sum_{i=1}^{n} f(y_i)$. Kita akan membuktikan dengan kontradiksi bahwa $x$ harus sama dengan $y$.

**1. Sifat Strictly Convex pada Transformasi-T**
Dari jawaban subnomor 1a, kita tahu bahwa $y$ dapat diperoleh dari $x$ melalui serangkaian transformasi-T. Misalkan kita melakukan satu transformasi-T pada komponen $a$ dan $b$ ($a > b$) untuk mendapatkan $a'$ dan $b'$ dengan parameter $\lambda = \frac{t}{a-b} \in (0, 1)$:
$$a' = (1-\lambda)a + \lambda b \quad \text{dan} \quad b' = \lambda a + (1-\lambda)b$$

Karena $f$ adalah **strictly convex**, maka ketidaksamaan Jensen menjadi ketidaksamaan ketat untuk $0 < \lambda < 1$:
1.  $f(a') = f((1-\lambda)a + \lambda b) < (1-\lambda)f(a) + \lambda f(b)$
2.  $f(b') = f(\lambda a + (1-\lambda)b) < \lambda f(a) + (1-\lambda)f(b)$

Jika kita menjumlahkan keduanya:
$$f(a') + f(b') < [(1-\lambda) + \lambda]f(a) + [\lambda + (1-\lambda)]f(b)$$
$$f(a') + f(b') < f(a) + f(b)$$

Ini menunjukkan bahwa setiap transformasi-T yang **non-trivial** ($a > a' \ge b' > b$) akan secara **ketat mengurangi** nilai total $\sum f(x_i)$.

**2. Menunjukkan Kontradiksi**
Misalkan $x \neq y$. Karena $x \succ y$ dan $x, y$ terurut, maka harus ada setidaknya satu transformasi-T non-trivial untuk mengubah $x$ menjadi $y$.
Berdasarkan hasil di atas:
*   Jika terdapat minimal satu transformasi-T non-trivial, maka $\sum f(x_i) > \sum f(y_i)$.
*   Namun, diberikan di awal bahwa $\sum f(x_i) = \sum f(y_i)$.

Ini adalah sebuah **kontradiksi**.

**3. Kesimpulan**
Satu-satunya cara agar kesetaraan $\sum f(x_i) = \sum f(y_i)$ terpenuhi di bawah kondisi $x \succ y$ dan $f$ strictly convex adalah jika tidak ada transformasi-T non-trivial yang dilakukan. Hal ini berarti $x = y$. Karena $x$ dan $y$ terurut menurun, $x=y$ berarti $x$ adalah permutasi dari $y$. $\square$
