Hubungan antara **persentase perubahan (arithmetic return)** dan **log return** merupakan konsep fundamental dalam analisis deret waktu keuangan.

Berikut adalah turunan lengkap mengapa pendekatan tersebut bisa digunakan:

---

## 1. Definisi Dasar

Misalkan $r_t$ adalah _simple return_ (pengembalian aritmetika) dari harga aset $S$ pada waktu $t$:

$$r_t = \frac{S(t) - S(t-1)}{S(t-1)}$$

Kita bisa menulis ulang persamaan di atas menjadi:

$$r_t = \frac{S(t)}{S(t-1)} - \frac{S(t-1)}{S(t-1)}$$

$$r_t = \frac{S(t)}{S(t-1)} - 1$$

Dari sini, kita mendapatkan hubungan:

$$\frac{S(t)}{S(t-1)} = 1 + r_t$$

---

## 2. Menggunakan Logaritma Natural

Jika kita mengambil logaritma natural ($\ln$) pada kedua sisi persamaan di atas, kita mendapatkan:

$$\ln\left(\frac{S(t)}{S(t-1)}\right) = \ln(1 + r_t)$$

Sisi kiri, $\ln(S(t)/S(t-1))$, sering disebut sebagai **log return**.

---

## 3. Ekspansi Deret Taylor

Untuk membuktikan pendekatan (aproksimasi) tersebut, kita menggunakan **Deret Taylor** untuk fungsi $f(x) = \ln(1+x)$ di sekitar $x = 0$:

$$f(x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$$

Jika kita ganti $x$ dengan $r_t$, maka:

$$\ln(1 + r_t) = r_t - \frac{r_t^2}{2} + \frac{r_t^3}{3} - \dots$$

---

## 4. Kesimpulan Aproksimasi

Dalam konteks keuangan, perubahan harga harian biasanya sangat kecil (misalnya $r_t \approx 0.01$ atau 1%). Ketika $r_t$ mendekati nol:

- Nilai $r_t^2, r_t^3,$ dan seterusnya menjadi sangat kecil sehingga bisa diabaikan.
    
- Oleh karena itu, $\ln(1 + r_t) \approx r_t$.
    

Maka, terbuktilah bahwa:

$$r_t = \frac{S(t) - S(t-1)}{S(t-1)} \approx \ln\left(\frac{S(t)}{S(t-1)}\right)$$