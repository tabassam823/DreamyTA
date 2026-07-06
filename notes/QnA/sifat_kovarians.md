Persamaan tersebut merupakan hasil dari penerapan **sifat linearitas operator kovarians**.

Dalam statistika, operator kovarians bersifat **bilinear**. Artinya, jika Anda memiliki variabel acak yang dikombinasikan secara linear, Anda bisa menjabarkannya satu per satu (mirip dengan metode perkalian pelangi atau distributif pada aljabar).

Berikut adalah langkah-langkah penurunannya:

### 1. Properti Dasar Bilinearitas

Secara umum, sifat kovarians adalah sebagai berikut:

$$\text{Cov}(a + b, c + d) = \text{Cov}(a, c) + \text{Cov}(a, d) + \text{Cov}(b, c) + \text{Cov}(b, d)$$

### 2. Substitusi Variabel

Mari kita definisikan variabel dari persamaan Anda:

- Sisi kiri ($X$): $R_A - \frac{1}{2}R_A^2$
    
- Sisi kanan ($Y$): $R_B - \frac{1}{2}R_B^2$
    

Maka:

$$\text{Cov}\left( \underbrace{R_A}_{a} \underbrace{- \frac{1}{2}R_A^2}_{b}, \underbrace{R_B}_{c} \underbrace{- \frac{1}{2}R_B^2}_{d} \right)$$

### 3. Penjabaran (Ekspansi)

Kita kalikan setiap elemen di sisi kiri dengan setiap elemen di sisi kanan:

1. **Elemen Pertama:** $\text{Cov}(R_A, R_B)$
    
2. **Elemen Kedua:** $\text{Cov}(R_A, -\frac{1}{2}R_B^2) \rightarrow$ Konstanta $-\frac{1}{2}$ bisa dikeluarkan menjadi: $-\frac{1}{2}\text{Cov}(R_A, R_B^2)$
    
3. **Elemen Ketiga:** $\text{Cov}(-\frac{1}{2}R_A^2, R_B) \rightarrow$ Konstanta $-\frac{1}{2}$ bisa dikeluarkan menjadi: $-\frac{1}{2}\text{Cov}(R_A^2, R_B)$
    
4. **Elemen Keempat:** $\text{Cov}(-\frac{1}{2}R_A^2, -\frac{1}{2}R_B^2) \rightarrow$ Kedua konstanta dikalikan $(-\frac{1}{2} \times -\frac{1}{2} = \frac{1}{4})$ menjadi: $+\frac{1}{4}\text{Cov}(R_A^2, R_B^2)$
    

### 4. Hasil Akhir

Jika kita gabungkan keempat elemen di atas, kita mendapatkan bentuk lengkap yang Anda tanyakan:

$$\text{Cov}(r_A, r_B) \approx \text{Cov}(R_A, R_B) - \frac{1}{2}\text{Cov}(R_A, R_B^2) - \frac{1}{2}\text{Cov}(R_A^2, R_B) + \frac{1}{4}\text{Cov}(R_A^2, R_B^2)$$

---

> **Catatan Konteks:** > Persamaan ini biasanya muncul dalam keuangan (Finance) saat menghubungkan _log-returns_ ($r$) dengan _arithmetic returns_ ($R$) menggunakan deret Taylor. Mengingat nilai $R$ biasanya kecil (misal 0.05), suku-suku terakhir seperti $\frac{1}{4}\text{Cov}(R_A^2, R_B^2)$ sering kali dianggap sangat kecil sehingga dalam praktiknya sering diabaikan.

Apakah Anda sedang menganalisis aproksimasi risiko portofolio atau sedang menurunkan rumus untuk aset dengan volatilitas tinggi?

---
Tentu, ini adalah cara yang sangat bagus untuk memahami "mekanisme" di balik matematika keuangan. Sifat linearitas (atau lebih tepatnya **bilinearitas**) kovarians sebenarnya muncul dari sifat dasar **Ekspektasi ($E$)**.

Mari kita turunkan langkah demi langkah menggunakan definisi dasar.

### 1. Definisi Umum

Kovarians antara dua variabel acak $X$ dan $Y$ didefinisikan sebagai:

$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$

Untuk membuktikan sifat penjabaran yang Anda tanyakan sebelumnya, kita akan menggunakan identitas ini karena jauh lebih mudah dimanipulasi secara aljabar daripada menggunakan bentuk $(X - \mu)$.

---

### 2. Memasukkan Variabel Komposit

Mari kita ganti $X$ dengan $(a + b)$ dan $Y$ dengan $(c + d)$. Maka:

$$\text{Cov}(a + b, c + d) = E[(a + b)(c + d)] - E[a + b]E[c + d]$$

Sekarang, kita jabarkan kedua bagian tersebut:

**Bagian A: Ekspansi Perkalian $E[(a+b)(c+d)]$**

Gunakan perkalian distributif (pelangi):

$$E[ac + ad + bc + bd]$$

Karena ekspektasi bersifat linear ($E[X+Y] = E[X] + E[Y]$), maka:

$$E[ac] + E[ad] + E[bc] + E[bd]$$

**Bagian B: Ekspansi Perkalian $E[a+b]E[c+d]$**

Sama halnya dengan di atas, kita kalikan dua kurung ini:

$$(E[a] + E[b])(E[c] + E[d])$$

$$E[a]E[c] + E[a]E[d] + E[b]E[c] + E[b]E[d]$$

---

### 3. Menggabungkan Kembali

Sekarang kita kurangi **Bagian A** dengan **Bagian B**:

$$\text{Cov}(a+b, c+d) = (E[ac] - E[a]E[c]) + (E[ad] - E[a]E[d]) + (E[bc] - E[b]E[c]) + (E[bd] - E[b]E[d])$$

Perhatikan bahwa setiap pasangan di dalam kurung di atas adalah definisi dari kovarians:

- $E[ac] - E[a]E[c] = \text{Cov}(a, c)$
    
- $E[ad] - E[a]E[d] = \text{Cov}(a, d)$
    
- ...dan seterusnya.
    

Sehingga terbukti bahwa:

$$\text{Cov}(a+b, c+d) = \text{Cov}(a, c) + \text{Cov}(a, d) + \text{Cov}(b, c) + \text{Cov}(b, d)$$

---
---

### 4. Bagaimana dengan Konstanta (seperti $-1/2$)?

Ada satu sifat lagi yang Anda gunakan: **$\text{Cov}(kX, Y) = k \cdot \text{Cov}(X, Y)$**.

Ini berasal dari fakta bahwa $E[kX] = kE[X]$.

Jika kita masukkan ke rumus $E[kXY] - E[kX]E[Y]$:

$$kE[XY] - (kE[X])E[Y] = k(E[XY] - E[X]E[Y]) = k \cdot \text{Cov}(X, Y)$$

Inilah alasan mengapa angka $-\frac{1}{2}$ pada $R_A^2$ dan $R_B^2$ bisa "keluar" dan saling mengalikan menjadi $+\frac{1}{4}$ pada suku terakhir persamaan Anda.

Apakah penurunan ini membuat langkah-langkah aljabar di pertanyaan sebelumnya jadi lebih masuk akal?