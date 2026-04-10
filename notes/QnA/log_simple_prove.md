Saya sangat menghargai sikap kritis Anda. Perdebatan mengenai _simple return_ vs _log return_ dalam agregasi portofolio adalah salah satu diskusi klasik yang paling sering menjebak para perancang algoritma _Quantitative Finance_.

Mari kita bedah argumen ini secara matematis. Saya akan mulai dengan meluruskan sedikit miskonsepsi mengenai rentang (range), lalu masuk ke pembuktian matematis mengapa agregasi _log return_ tidak valid secara aljabar (meskipun sering "ditoleransi" dalam praktiknya), beserta analisis sensitivitasnya.

### 1. Koreksi Premis: Rentang Nilai Return

Klaim bahwa rentang kedua return adalah -1 sampai 1 kurang tepat.

- **Simple Return ($R$):** Memiliki rentang $[-1, \infty)$. Nilai -1 terjadi jika aset bangkrut (turun 100%). Namun, tidak ada batas atas; sebuah aset bisa naik 300% ($R = 3.0$).
    
- **Log Return ($r$):** Memiliki rentang $(-\infty, \infty)$. Jika harga aset anjlok mendekati nol, $\ln(P_t/P_{t-1})$ akan mendekati $-\infty$. Jika naik 300%, $\ln(4) \approx 1.38$.
    

Karena _log return_ adalah fungsi non-linear dari _simple return_ ($r = \ln(1+R)$), di situlah inti permasalahannya bermula.

---

### 2. Pembuktian Matematis (Ketidakcocokan Agregasi)

Mari kita buktikan mengapa menghitung _expected return_ portofolio menggunakan rata-rata tertimbang dari _log return_ menyalahi hukum matematika dasar.

Misalkan kita memiliki portofolio dengan bobot $w_i$ dan imbal hasil sederhana $R_i$.

Imbal hasil portofolio yang **sebenarnya** (apa yang terjadi pada uang Anda di dunia nyata) adalah:

$$R_p = \sum_{i=1}^n w_i R_i$$

Maka, **Log Return Portofolio Sejati ($r_{true}$)** adalah:

$$r_{true} = \ln(1 + R_p) = \ln\left(1 + \sum_{i=1}^n w_i R_i\right)$$

Namun, dalam kodingan atau kalkulasi yang menjumlahkan _log return_ per aset secara langsung, **Log Return Aproksimasi ($\hat{r}_p$)** yang dihasilkan adalah:

$$\hat{r}_p = \sum_{i=1}^n w_i r_i = \sum_{i=1}^n w_i \ln(1 + R_i)$$

**Pertanyaan Kritis:** Apakah $\ln\left(1 + \sum w_i R_i\right)$ sama dengan $\sum w_i \ln(1 + R_i)$?

Menurut **Ketaksamaan Jensen (Jensen's Inequality)** untuk fungsi cekung (seperti logaritma), jawabannya adalah **TIDAK**. Secara spesifik:

$$\ln\left(\sum w_i (1 + R_i)\right) \geq \sum w_i \ln(1 + R_i)$$

Artinya, penjumlahan linear dari _log return_ ($\hat{r}_p$) akan **selalu memberikan nilai yang lebih rendah (underestimate)** dibandingkan _log return_ portofolio yang sebenarnya ($r_{true}$).

---

### 3. Analisis Sensitivitas (Deret Taylor & Pembuktian Error)

Seberapa besar simpangan (error) dari pendekatan ini? Kita bisa membedahnya menggunakan ekspansi **Deret Taylor** orde kedua untuk $\ln(1+x) \approx x - \frac{x^2}{2}$.

1. **Ekspansi untuk Aproksimasi (Kodingan Anda):**
    
    $$\hat{r}_p \approx \sum w_i \left(R_i - \frac{R_i^2}{2}\right) = \sum w_i R_i - \frac{1}{2}\sum w_i R_i^2$$
    
2. **Ekspansi untuk Portofolio Sejati:**
    
    $$r_{true} \approx R_p - \frac{R_p^2}{2} = \sum w_i R_i - \frac{1}{2}\left(\sum w_i R_i\right)^2$$
    
3. **Menghitung Besaran Error (Sensitivitas):**
    
    $$\text{Error} = r_{true} - \hat{r}_p$$
    
    $$\text{Error} \approx \left[ \sum w_i R_i - \frac{1}{2}\left(\sum w_i R_i\right)^2 \right] - \left[ \sum w_i R_i - \frac{1}{2}\sum w_i R_i^2 \right]$$
    
    $$\text{Error} \approx \frac{1}{2} \left[ \sum w_i R_i^2 - \left(\sum w_i R_i\right)^2 \right]$$
    

Perhatikan persamaan terakhir tersebut. Bentuk $[\sum w_i R_i^2 - (\sum w_i R_i)^2]$ adalah definisi eksak dari **Variansi Cross-Sectional (Variansi antar-aset dalam portofolio)**.

Maka, persamaan relasi akhirnya adalah:

$$r_{true} \approx \hat{r}_p + \frac{1}{2} \text{Var}(R)$$

**Kesimpulan Analisis Sensitivitas:**

Penggunaan rata-rata _log return_ ($\hat{r}_p$) akan meleset dari kenyataan sebanding dengan setengah variansi antar-aset.

- Jika volatilitas pasar kecil (return mendekati nol), $\text{Var}(R)$ akan sangat kecil, dan error ini bisa diabaikan. Ini sebabnya banyak _quant_ sering "malas" dan tetap menggunakan _log return_ untuk semuanya.
    
- Tetapi, jika volatilitas tinggi (misal saat krisis), error ini membengkak secara kuadratik, merusak perhitungan _expected return_ yang diharapkan algoritma Anda.
    

---

### 4. Pembuktian Kasus Ekstrem (Simulasi Angka)

Untuk membuktikan secara mutlak bahwa agregasi _log return_ bisa sangat menyesatkan, mari kita buat simulasi ekstrem dua aset dengan bobot masing-masing 50% ($w_A = 0.5$, $w_B = 0.5$).

- **Aset A:** Naik 50%. (Simple return $R_A = 0.5$). Log return $r_A = \ln(1.5) = \mathbf{0.405}$
    
- **Aset B:** Turun 50%. (Simple return $R_B = -0.5$). Log return $r_B = \ln(0.5) = \mathbf{-0.693}$
    

**Mari kita hitung portofolionya:**

1. **Kenyataan di Dunia Nyata (True Portfolio Return):**
    
    $R_p = 0.5(0.5) + 0.5(-0.5) = 0$.
    
    Uang Anda tidak bertambah dan tidak berkurang.
    
    Maka, _Log Return_ sejati portofolio adalah $\ln(1 + 0) = \mathbf{0}$.
    
2. **Agregasi Log Return (Cara Kodingan/Aproksimasi):**
    
    $\hat{r}_p = 0.5(0.405) + 0.5(-0.693)$
    
    $\hat{r}_p = 0.2025 - 0.3465 = \mathbf{-0.144}$
    

**Hasil Akhir:** Kenyataannya portofolio Anda memiliki imbal hasil **0%**, tetapi fungsi yang mengagregasikan _log return_ akan melaporkan kepada optimizer SBR bahwa portofolio ini mengalami kerugian logaritmik sebesar **-14.4%**. Algoritma akan menolak portofolio ini, padahal ini adalah titik _hedge_ sempurna.

Inilah mengapa saya menyatakan bahwa penggunaan _log return_ untuk mengevaluasi _expected return_ lintas-aset (portofolio) memiliki cacat matematis secara teoretis, dan penggunaannya hanya bisa ditoleransi pada instrumen dengan volatilitas yang sangat rendah.

---
---
Ini adalah pertanyaan lanjutan yang sangat tajam. Logika Anda benar: jika _log return_ "cacat" untuk menghitung rata-rata (imbal hasil ekspektasi/$\mu$), mengapa alat yang sama tiba-tiba menjadi "valid" dan bahkan direkomendasikan untuk menghitung matriks kovariansi ($\Sigma$)?

Jawabannya terletak pada perbedaan fundamental antara **pengukuran absolut** (seperti rata-rata ekspektasi) dan **pengukuran dispersi relatif** (seperti kovariansi).

Mari kita buktikan secara matematis mengapa kesalahan yang menghancurkan perhitungan _expected return_ justru **saling menghilangkan (cancel out)** saat menghitung kovariansi.

---

### 1. Pembuktian Aljabar: Mengapa Bias (Error) Menghilang

Mari kita ingat kembali rumus dasar Kovariansi. Kovariansi tidak peduli dengan nilai absolut aset Anda; ia hanya peduli pada **penyimpangan data dari rata-ratanya (deviations from the mean)**:

$$Cov(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$$

Sekarang, kita ambil pendekatan _log return_ hasil aproksimasi Deret Taylor yang kita buat sebelumnya. Anggaplah volatilitas kecil, sehingga _log return_ ($r$) adalah _simple return_ ($R$) yang dikurangi sebuah bias/error konstan ($\epsilon$).

$$r_i \approx R_i - \epsilon$$

Mari kita lihat apa yang terjadi saat kita mencari rata-rata dari _log return_ ($E[r_i]$):

$$E[r_i] \approx E[R_i - \epsilon] = E[R_i] - \epsilon$$

**Titik Kritisnya Ada di Sini:**

Sekarang, mari kita masukkan nilai-nilai ini ke dalam komponen penyimpangan (deviasi) yang menjadi mesin utama matriks kovariansi:

$$\text{Deviasi}_{log} = r_i - E[r_i]$$

$$\text{Deviasi}_{log} \approx (R_i - \epsilon) - (E[R_i] - \epsilon)$$

$$\text{Deviasi}_{log} \approx R_i - \epsilon - E[R_i] + \epsilon$$

$$\text{Deviasi}_{log} \approx R_i - E[R_i]$$

**Hasilnya:** Variabel bias/error ($\epsilon$) **saling menghilangkan**.

Deviasi dari _log return_ secara matematis hampir identik dengan deviasi dari _simple return_. Karena kovariansi dibangun murni dari deviasi ini, maka:

$$Cov(r_i, r_j) \approx Cov(R_i, R_j)$$

_Kesimpulan Tahap 1:_ _Log return_ valid untuk matriks kovariansi karena kovariansi kebal terhadap bias translasi (pergeseran nilai absolut yang disebabkan oleh logaritma).

---

### 2. Analisis Sensitivitas (Deret Taylor Orde Dua)

Tentu saja, $\epsilon$ tidak sepenuhnya konstan; ia bergantung pada kuadrat return ($R^2/2$). Mari kita bedah lebih dalam menggunakan ekspansi Taylor orde dua untuk melihat seberapa besar sisa error-nya.

Diketahui: $r \approx R - \frac{1}{2}R^2$

Kovariansi antara _log return_ aset A dan B adalah:

$$Cov(r_A, r_B) \approx Cov\left(R_A - \frac{1}{2}R_A^2, R_B - \frac{1}{2}R_B^2\right)$$

Berdasarkan sifat linearitas kovariansi, persamaan ini dapat dipecah menjadi empat komponen:

$$Cov(r_A, r_B) \approx Cov(R_A, R_B) - \frac{1}{2}Cov(R_A, R_B^2) - \frac{1}{2}Cov(R_A^2, R_B) + \frac{1}{4}Cov(R_A^2, R_B^2)$$

**Mari kita evaluasi magnitudonya (Sensitivitas):**

Dalam pasar keuangan, imbal hasil harian ($R$) sangat kecil, biasanya dalam orde $10^{-2}$ (misal $1\% = 0.01$).

- Suku pertama, $Cov(R_A, R_B)$, adalah **Kovariansi Linear Utama** (orde $10^{-4}$).
    
- Suku kedua dan ketiga, $Cov(R, R^2)$, adalah **Co-Skewness** (orde $10^{-6}$).
    
- Suku keempat, $Cov(R^2, R^2)$, adalah **Co-Kurtosis** (orde $10^{-8}$).
    

Karena suku kedua, ketiga, dan keempat bernilai sangat eksponensial lebih kecil mendekati nol dibandingkan suku pertama, mereka bisa diabaikan. Ini membuktikan secara matematis bahwa matriks kovariansi dari _log return_ ($\Sigma_{log}$) dan _simple return_ ($\Sigma_{simple}$) secara konseptual setara pada frekuensi harian.

---

### 3. Mengapa Log Return Justru LEBIH BAIK untuk Kovariansi?

Setelah membuktikan bahwa mereka setara, para _Quant_ lebih memilih _log return_ untuk mengisi matriks $\Sigma$ karena dua alasan statistik yang sangat kuat:

**A. Syarat Distribusi Normal**

Matriks kovariansi (dan korelasi Pearson) sangat mengandalkan asumsi bahwa data terdistribusi secara normal (Simetris berbentuk lonceng).

- _Simple return_ terikat pada batas bawah $-1$ tetapi tidak punya batas atas. Hal ini memaksa datanya menjadi asimetris (_right-skewed / log-normal_). Menghitung kovariansi dari data yang asimetris akan menghasilkan matriks yang tidak stabil secara statistik.
    
- _Log return_ membentang dari $-\infty$ hingga $\infty$. Transformasi logaritmik secara natural "menarik" data keuangan yang miring menjadi lebih simetris dan mendekati distribusi Gaussian (Normal). $\Sigma$ yang dihitung dari _log return_ jauh lebih tangguh.
    

**B. Scaling Waktu (Time-Aggregation)**

Model Markowitz dan Ising-SBR sering kali menghitung risiko harian, tetapi mengoptimalkan untuk target tahunan.

Variansi _log return_ memiliki sifat linear yang sempurna terhadap waktu (_additivity over time_):

$$Var(r_{tahunan}) = 252 \times Var(r_{harian})$$

Anda bisa mengalikan matriks $\Sigma_{log}$ dengan skalar waktu dengan valid. Sebaliknya, _simple return_ bersifat multiplikatif terhadap waktu. Jika Anda mengalikan matriks variansi _simple return_ harian dengan 252, Anda melanggar hukum matematika probabilistik dan menggelembungkan risiko secara salah.

### Rangkuman Arsitektur Optimal

Berdasarkan pembuktian di atas, standar emas (_best practice_) dalam algoritma optimasi portofolio kuantitatif untuk menangani dualitas ini adalah:

1. Gunakan **Simple Return** untuk menghitung vektor **Expected Return ($\mu$)**.
    
2. Gunakan **Log Return** untuk memodelkan **Matriks Kovariansi ($\Sigma$)** dan menghitung **Penalti NMI**.
    
3. Masukkan keduanya ke dalam Fungsi Objektif Markowitz / Fungsi Potensial _Game Theory_.