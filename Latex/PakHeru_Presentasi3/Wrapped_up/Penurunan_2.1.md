Persamaan **(2.1)** berasal dari konsep **Ekspektasi Bersyarat (Conditional Expectation)** dalam statistika bayesian atau analisis data _a posteriori_. Secara sederhana, ini adalah cara kita menghitung "rata-rata tertimbang" dari hasil di masa lalu untuk kondisi tertentu.

Berikut adalah langkah-langkah penurunan dan logika di baliknya:

---

### 1. Definisi _A Posteriori_

Dalam konteks ini, _a posteriori_ berarti kita menurunkan nilai berdasarkan **data historis yang telah diobservasi**.

- Kita memiliki data pasangan $(\text{State}, R_k)$.
    
- Kita ingin mengetahui: "Jika sistem berada dalam keadaan $\ket{ij}$, berapa rata-rata pengembalian (return) $R_k$ yang biasanya terjadi?"
    

---

### 2. Formulasi Ekspektasi Diskret

Secara statistik, nilai ekspektasi dari variabel acak $R_k$ yang bergantung pada suatu kejadian (event) $A$ didefinisikan sebagai:

$$\mathbb{E}[R|A] = \sum r \cdot P(R=r|A)$$

Dalam kasus Anda:

- **Event $A$** adalah sistem berada pada State $\ket{ij}$.
    
- **$R_k$** adalah nilai return aset ke-$k$.
    

Maka, nilai $u_{ij}^k$ adalah rata-rata dari semua nilai $R_k$ yang muncul hanya pada hari-hari di mana State tercatat sebagai $\ket{ij}$.

---

### 3. Penurunan dari Data Historis

Misalkan kita memiliki total $N$ hari pengamatan.

1. Identifikasi himpunan waktu $T_{ij}$, yaitu kumpulan hari di mana State adalah $\ket{ij}$:
    
    $$T_{ij} = \{t \in \{1, \dots, N\} \mid \text{State}_t = \ket{ij}\}$$
    
2. Jumlah hari tersebut adalah $n_{ij}$ (seperti pada persamaan 1.8 di gambar sebelumnya).
    
3. Maka, estimasi _a posteriori_ untuk ekspektasi return tersebut adalah **rata-rata aritmetika** dari $R_k$ pada hari-hari tersebut:
    
    $$u_{ij}^k = \frac{1}{n_{ij}} \sum_{t \in T_{ij}} R_k(t)$$
    

---

### 4. Hubungan dengan Probabilitas

Jika kita melihatnya dari sudut pandang probabilitas bersama (_joint probability_), berdasarkan hukum Bayes:

$$P(R_k | \ket{ij}) = \frac{P(R_k \cap \ket{ij})}{P(\ket{ij})}$$

Sehingga $u_{ij}^k$ merepresentasikan nilai pusat (mean) dari distribusi return $R_k$ yang telah "difilter" oleh keadaan kuantum $\ket{ij}$.

---

### Mengapa ini penting?

Dalam manajemen portofolio atau strategi trading, persamaan ini digunakan untuk memetakan **State kuantum** (yang mungkin berisi sinyal teknikal atau makro) ke dalam **estimasi keuntungan**.

- Jika $u_{ij}^k > 0$, maka State $\ket{ij}$ adalah sinyal _bullish_ untuk aset $k$.
    
- Jika $u_{ij}^k < 0$, maka State $\ket{ij}$ adalah sinyal _bearish_.
    

Apakah Anda ingin saya menjelaskan bagaimana $u_{ij}^k$ ini kemudian dimasukkan ke dalam perhitungan **Expected Return Portofolio** menggunakan produk dalam $\langle \Psi | \hat{R} | \Psi \rangle$?