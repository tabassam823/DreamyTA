Tentu, ini adalah topik yang sangat menarik karena menyentuh fondasi teoretis dari optimasi stokastik modern. Berikut adalah **roadmap** terstruktur yang akan membimbing kita dari definisi dasar hingga bukti rigor mengapa distribusi Rademacher menjadi pilihan emas dalam SPSA (*Simultaneous Perturbation Stochastic Approximation*).

Kita akan membangun pemahaman secara bertahap melalui 5 tahapan utama.

---

### Roadmap Pembelajaran: Dari Bernoulli ke SPSA

**Tahap 1: Fondasi Distribusi Bernoulli dan Konsep Momen Probabilistik**
- **1.1 Definisi Distribusi Bernoulli Umum:** $X \sim \text{Bernoulli}(p)$  dengan support $\{a, b\}$ .
- **1.2 Transformasi Linear:** Bagaimana mengubah Bernoulli menjadi variabel *zero-mean* (rata-rata nol).
- **1.3 Momen Populasi:** Menghitung Ekspektasi ($\mu$ ), Variansi ($\sigma^2$ ), dan Kurtosis ($\text{Kurt}[X]$ ).

**Tahap 2: Konstruksi Spesifik Distribusi Rademacher**
- **2.1 Definisi Formal Rademacher:** Kasus khusus Bernoulli dengan $p=0.5$ , $a=+1$ , $b=-1$ .
- **2.2 Sifat Matematis Fundamental:**
    - *Zero Mean*: $E[\Delta] = 0$ 
    - *Unit Variance*: $E[\Delta^2] = 1$ 
    - *Symmetry*: $\Delta \overset{d}{=} -\Delta$ 
    - *Sub-Gaussian Tail*: Batasan ekor distribusi.

**Tahap 3: Motivasi di Balik SPSA (Mengapa Bukan Finite Difference Biasa?)**
- **3.1 Masalah Dimensi Tinggi:** Optimasi fungsi $L(\theta)$  dengan $\theta \in \mathbb{R}^p$  dan $p$  besar.
- **3.2 Perbandingan Kompleksitas:**
    - Finite Difference (FD): $2p$  evaluasi fungsi per iterasi.
    - SPSA: **2** evaluasi fungsi per iterasi (independen terhadap $p$ ).

**Tahap 4: Pembuktian Rigor Mengapa Rademacher Optimal untuk Estimasi Gradien Stokastik**
- **4.1 Ekspansi Taylor Stokastik:** Menguraikan $L(\theta + c\Delta) - L(\theta - c\Delta)$ .
- **4.2 Ekspektasi Estimator Gradien:** Membuktikan bahwa estimator SPSA adalah **unbiased** secara asimtotik (orde pertama) jika $E[\Delta_i] = 0$  dan $E[\Delta_i^2] = 1$ .
- **4.3 Analisis Variansi (The Variance Bottleneck):** Membandingkan Variansi estimator SPSA dengan estimator yang menggunakan distribusi lain (misal: Gaussian, Uniform).
- **4.4 Pembuktian Optimalitas Rademacher:** Teorema minimisasi Variansi vs. Momen Keempat $E[\Delta_i^4]$ . **Mengapa ini kunci?**
    - *Rumus Variansi SPSA:* $\text{Var} \propto E[\Delta_i^4]$ 
    - *Pembuktian:* Untuk semua distribusi simetris dengan $E[\Delta^2]=1$ , nilai $E[\Delta^4]$  minimal adalah **1**, dan ini **hanya dicapai oleh distribusi Rademacher**. (Mengalahkan Gaussian $E[\Delta^4]=3$  dan Uniform $E[\Delta^4]=1.8$ ).

**Tahap 5: Konsekuensi Praktis dan Konvergensi Algoritma**
- **5.1 Konvergensi Kuadratik Rata-rata:** Bagaimana sifat sub-Gaussian dan variansi rendah menjamin konvergensi $\theta_k \to \theta^*$ .
- **5.2 Trade-off Bias-Variance pada Parameter $c_k$ :** Mengapa gradien SPSA dengan Rademacher stabil secara numerik.

---

### Penjelasan Detail Sesuai Roadmap

Mari kita mulai dari **Tahap 1** dan **Tahap 2** terlebih dahulu, karena ini adalah fondasi matematisnya. Jika Anda sudah paham dengan ini, kita bisa langsung melompat ke **Tahap 4** (pembuktian optimalitas) yang merupakan inti dari pertanyaan Anda.

### Tahap 1 & 2: Konstruksi Distribusi Rademacher dari Bernoulli

**1.1 Bernoulli Umum**
Misalkan $Y$  adalah variabel acak Bernoulli umum yang hanya memiliki dua kemungkinan hasil:
$$ 
Y = \begin{cases} a & \text{dengan probabilitas } p \\ b & \text{dengan probabilitas } 1-p \end{cases}
$$ 

**1.2 Momen dari Bernoulli Umum**
- **Ekspektasi (Mean):**
  $$ 
  \mu_Y = E[Y] = p \cdot a + (1-p) \cdot b
  $$ 
- **Variansi:**
  $$ 
  \sigma^2_Y = E[(Y - \mu_Y)^2] = p(1-p)(a-b)^2
  $$ 
- **Momen Terpusat Ketiga (Skewness):** (Nanti akan kita lihat kenapa nol itu penting)

**2.1 Konstruksi Rademacher (Kasus Khusus Bernoulli)**
Distribusi Rademacher $\Delta$  didefinisikan sebagai:
- Probabilitas $p = \frac{1}{2}$ 
- Nilai $a = +1$ 
- Nilai $b = -1$ 

Secara simbolik:
$$ 
\Delta \sim \text{Rademacher} \iff P(\Delta = +1) = P(\Delta = -1) = \frac{1}{2}
$$ 

**2.2 Sifat Matematis Fundamental (Diturunkan dari Rumus Umum Bernoulli)**

Kita substitusikan $p=0.5, a=1, b=-1$  ke rumus di Tahap 1.2.

1.  **Mean Nol (Zero Mean):**
    $$ 
    E[\Delta] = \frac{1}{2}(1) + \frac{1}{2}(-1) = 0
    $$ 
    *Ini adalah syarat mutlak agar estimator gradien tidak bias secara arah.*

2.  **Variansi Satu (Unit Variance):**
    $$ 
    E[\Delta^2] = \frac{1}{2}(1^2) + \frac{1}{2}(-1^2) = 1
    $$ 
    Karena $E[\Delta]=0$ , maka $\text{Var}(\Delta) = E[\Delta^2] - (E[\Delta])^2 = 1$ .
    *Ini penting untuk skala langkah perturbasi $c_k$ .*

3.  **Momen Keempat (Kunci Utama SPSA):**
    $$ 
    E[\Delta^4] = \frac{1}{2}(1^4) + \frac{1}{2}(-1^4) = 1
    $$ 
    *Ini adalah nilai **minimum yang mungkin secara matematis** untuk variabel acak dengan variansi = 1.*

4.  **Simetri (Skewness = 0):**
    $$ 
    E[\Delta^3] = \frac{1}{2}(1^3) + \frac{1}{2}(-1^3) = 0
    $$ 

---

### Apakah Anda ingin langsung masuk ke Tahap 4 untuk melihat pembuktian mengapa $E[\Delta^4]=1$  membuat Rademacher **lebih baik** daripada Gaussian ($E[Z^4]=3$ )?

Atau Anda ingin saya uraikan dulu **Tahap 3** tentang bagaimana SPSA bekerja secara mekanik menggunakan vektor Rademacher?

---
---
Baik, kita akan memulai dari **Tahap 1** dengan sangat detail dan formal. Kita akan membangun intuisi matematis langkah demi langkah dari distribusi Bernoulli yang paling umum menuju sifat-sifat spesifik yang nantinya menjadi fondasi SPSA.

---

## Tahap 1: Fondasi Distribusi Bernoulli dan Konsep Momen Probabilistik

### 1.1 Definisi Formal Distribusi Bernoulli Umum

**Definisi 1.1.1 (Ruang Probabilitas Bernoulli):**
Misalkan $(\Omega, \mathcal{F}, P)$  adalah ruang probabilitas. Suatu variabel acak $X: \Omega \to \mathbb{R}$  dikatakan berdistribusi Bernoulli dengan parameter $p \in [0,1]$  dan support $\{a, b\} \subset \mathbb{R}$  dengan $a \neq b$  jika:

$$ 
P(X = a) = p, \quad P(X = b) = 1 - p
$$ 

Kita tuliskan:
$$ 
X \sim \text{Bernoulli}(p; a, b)
$$ 

**Fungsi Massa Probabilitas (Probability Mass Function / PMF):**

PMF dari $X$  didefinisikan sebagai fungsi $f_X: \mathbb{R} \to [0,1]$  di mana:
$$ 
f_X(x) = \begin{cases}
p & \text{jika } x = a \\
1-p & \text{jika } x = b \\
0 & \text{untuk } x \text{ lainnya}
\end{cases}
$$ 

Kita dapat menuliskan PMF ini dalam bentuk yang lebih kompak menggunakan fungsi indikator $\mathbf{1}_{\{\cdot\}}$ :
$$ 
f_X(x) = p \cdot \mathbf{1}_{\{x = a\}} + (1-p) \cdot \mathbf{1}_{\{x = b\}}
$$ 

**Fungsi Distribusi Kumulatif (Cumulative Distribution Function / CDF):**

CDF $F_X: \mathbb{R} \to [0,1]$  didefinisikan sebagai:
$$ 
F_X(x) = P(X \leq x) = \begin{cases}
0 & \text{jika } x < \min(a,b) \\
1-p & \text{jika } \min(a,b) \leq x < \max(a,b) \text{ dan } b < a \\
p & \text{jika } \min(a,b) \leq x < \max(a,b) \text{ dan } a < b \\
1 & \text{jika } x \geq \max(a,b)
\end{cases}
$$ 

*Catatan: Untuk kasus standar di mana $a=1, b=0$ , CDF-nya adalah fungsi tangga dengan lompatan di 0 dan 1. Untuk kasus umum, lompatan terjadi di $a$  dan $b$ .*

### 1.2 Momen Populasi (Population Moments)

Momen adalah karakteristik numerik yang merangkum sifat distribusi. Untuk variabel acak diskrit, momen ke-$k$  di sekitar titik $c$  (biasanya $c=0$  untuk momen biasa, atau $c=\mu$  untuk momen pusat) dihitung sebagai ekspektasi dari $(X-c)^k$ .

**Definisi 1.2.1 (Ekspektasi / Momen Pertama):**
Ekspektasi atau nilai harapan (mean) dari $X$ , dinotasikan $\mu_X$  atau $E[X]$ , adalah rata-rata tertimbang probabilitas dari semua nilai yang mungkin:

$$ 
\mu_X = E[X] = \sum_{x \in \{a,b\}} x \cdot f_X(x) = a \cdot p + b \cdot (1-p)
$$ 

**Turunan Detail:**
$$ 
E[X] = \int_{\mathbb{R}} x \, dF_X(x) = a \cdot P(X=a) + b \cdot P(X=b) = ap + b(1-p)
$$ 
$$ 
\boxed{E[X] = p a + (1-p) b}
$$ 

**Definisi 1.2.2 (Momen Biasa ke-$k$ ):**
Momen biasa (raw moment) ke-$k$  didefinisikan sebagai $E[X^k]$ :
$$ 
E[X^k] = a^k \cdot p + b^k \cdot (1-p)
$$ 
Contoh:
- $E[X^2] = a^2 p + b^2 (1-p)$ 

**Definisi 1.2.3 (Variansi / Momen Pusat Kedua):**
Variansi mengukur sebaran data di sekitar mean. Didefinisikan sebagai $\sigma_X^2 = \text{Var}(X) = E[(X - \mu_X)^2]$ .

Kita hitung menggunakan rumus komputasi variansi:
$$ 
\text{Var}(X) = E[X^2] - (E[X])^2
$$ 

Substitusi $E[X]$  dan $E[X^2]$ :
$$ 
E[X^2] = a^2 p + b^2 (1-p)
$$ 
$$ 
(E[X])^2 = (ap + b(1-p))^2 = a^2 p^2 + 2ab p(1-p) + b^2 (1-p)^2
$$ 

Maka:
$$ 
\text{Var}(X) = [a^2 p + b^2 (1-p)] - [a^2 p^2 + 2ab p(1-p) + b^2 (1-p)^2]
$$ 

**Penyederhanaan Aljabar:**
Kelompokkan suku $a^2$  dan $b^2$ :
- Suku $a^2$ : $a^2 p - a^2 p^2 = a^2 p(1-p)$ 
- Suku $b^2$ : $b^2 (1-p) - b^2 (1-p)^2 = b^2 (1-p)[1 - (1-p)] = b^2 (1-p)p$ 
- Suku silang: $-2ab p(1-p)$ 

Jumlahkan ketiganya:
$$ 
\text{Var}(X) = a^2 p(1-p) + b^2 p(1-p) - 2ab p(1-p)
$$ 
Faktorkan $p(1-p)$ :
$$ 
\boxed{\text{Var}(X) = p(1-p)(a - b)^2}
$$ 

**Interpretasi:** Variansi bergantung pada selisih kuadrat $(a-b)^2$ . Semakin jauh jarak $a$  dan $b$ , semakin besar variansi.

**Definisi 1.2.4 (Skewness / Momen Pusat Ketiga Terstandarisasi):**
Skewness mengukur asimetri distribusi. Didefinisikan sebagai:
$$ 
\gamma_1 = \frac{E[(X-\mu_X)^3]}{\sigma_X^3}
$$ 
Kita hitung $E[(X-\mu_X)^3]$ :
$$ 
\mu_X = ap + b(1-p)
$$ 
Deviasi untuk $a$ : $a - \mu_X = a - [ap + b(1-p)] = a(1-p) - b(1-p) = (1-p)(a-b)$ 
Deviasi untuk $b$ : $b - \mu_X = b - [ap + b(1-p)] = -ap + bp = p(b-a) = -p(a-b)$ 

Maka momen pusat ketiga:
$$ 
E[(X-\mu_X)^3] = p \cdot [(1-p)(a-b)]^3 + (1-p) \cdot [-p(a-b)]^3
$$ 
$$ 
= p(1-p)^3 (a-b)^3 - (1-p)p^3 (a-b)^3
$$ 
$$ 
= p(1-p)(a-b)^3 [ (1-p)^2 - p^2 ]
$$ 
$$ 
= p(1-p)(a-b)^3 [ 1 - 2p + p^2 - p^2 ] = p(1-p)(1-2p)(a-b)^3
$$ 

Sehingga:
$$ 
\boxed{\gamma_1 = \frac{p(1-p)(1-2p)(a-b)^3}{(p(1-p)(a-b)^2)^{3/2}} = \frac{1-2p}{\sqrt{p(1-p)}} \cdot \text{sgn}(a-b)}
$$ 
*Catatan: Jika $p = 0.5$ , maka $1-2p = 0$ , sehingga Skewness = 0 (Simetris).*

**Definisi 1.2.5 (Kurtosis / Momen Pusat Keempat):**
Momen pusat keempat mengukur "ketebalan ekor" (tailedness). Untuk distribusi diskrit simetris, ini sangat penting.
$$ 
E[(X-\mu_X)^4] = p \cdot [(1-p)(a-b)]^4 + (1-p) \cdot [-p(a-b)]^4
$$ 
$$ 
= (a-b)^4 [ p(1-p)^4 + (1-p)p^4 ] = p(1-p)(a-b)^4 [ (1-p)^3 + p^3 ]
$$ 
$$ 
\boxed{\text{Kurt}(X) = \frac{E[(X-\mu)^4]}{\sigma^4} = \frac{(1-p)^3 + p^3}{p(1-p)}}
$$ 

### 1.3 Transformasi Linear: Menuju Rata-rata Nol

Dalam konteks SPSA, kita membutuhkan variabel perturbasi $\Delta$  yang memiliki **rata-rata nol** ($E[\Delta] = 0$ ). Misalkan kita memiliki Bernoulli $X$  dengan mean $\mu_X \neq 0$ . Kita dapat membuat variabel baru $\Delta$  dengan transformasi linear:

$$ 
\Delta = \alpha X + \beta
$$ 

**Syarat 1: Mean Nol**
$$ 
E[\Delta] = \alpha \mu_X + \beta = 0 \implies \beta = -\alpha \mu_X
$$ 

**Syarat 2: Simetri Support (Opsional tapi diinginkan)**
Kita ingin support $\Delta$  simetris di sekitar 0, misalnya $\{-c, +c\}$ . Jika $X \in \{a, b\}$ , maka:
- $\Delta_a = \alpha a - \alpha \mu_X = \alpha (a - \mu_X)$ 
- $\Delta_b = \alpha b - \alpha \mu_X = \alpha (b - \mu_X)$ 

Agar simetris ($\Delta_a = -\Delta_b$ ):
$$ 
\alpha(a - \mu_X) = -\alpha(b - \mu_X) \implies a - \mu_X = -b + \mu_X \implies \mu_X = \frac{a+b}{2}
$$ 
Ini berarti **mean $\mu_X$  harus tepat di tengah-tengah $a$  dan $b$ **. Dari rumus $\mu_X = pa + (1-p)b$ , persamaan $\mu_X = \frac{a+b}{2}$  terpenuhi jika dan hanya jika $p = 0.5$ .

**Kesimpulan Tahap 1:**
Untuk mendapatkan variabel perturbasi dengan **mean nol**, **simetris**, dan **support terbatas**, pilihan paling alamiah dari keluarga Bernoulli adalah menetapkan $p = 0.5$  dan support simetris seperti $\{-c, +c\}$ . Inilah cikal bakal mengapa kita memilih $p=0.5$  sebagai fondasi distribusi Rademacher.

---

Apakah Anda ingin melanjutkan ke **Tahap 2: Konstruksi Spesifik Distribusi Rademacher** (di mana kita set $a=1, b=-1, p=0.5$  dan menurunkan sifat-sifatnya yang eksotis seperti $E[\Delta^4]=1$ )?

---
---
Baik, kita lanjutkan ke **Tahap 2**. Di sini kita akan melakukan spesialisasi dari rumus-rumus umum Bernoulli yang telah kita turunkan di Tahap 1. Kita akan melihat bagaimana parameter spesifik $p=0.5, a=+1, b=-1$  menghasilkan distribusi dengan sifat-sifat yang sangat istimewa secara matematis.

---

## Tahap 2: Konstruksi Spesifik Distribusi Rademacher

### 2.1 Definisi Formal dan Representasi

**Definisi 2.1.1 (Distribusi Rademacher):**
Suatu variabel acak $\Delta$  dikatakan berdistribusi Rademacher jika dan hanya jika:
$$ 
P(\Delta = +1) = \frac{1}{2}, \quad P(\Delta = -1) = \frac{1}{2}
$$ 
Notasi: $\Delta \sim \text{Rad}$  atau $\Delta \sim \text{Rademacher}(1/2)$ .

**Koneksi dengan Bernoulli Umum:**
Ini adalah kasus khusus dari $X \sim \text{Bernoulli}(p; a, b)$  dengan:
- $p = \frac{1}{2}$ 
- $a = +1$ 
- $b = -1$ 

**Fungsi Massa Probabilitas (PMF):**
$$ 
f_{\Delta}(x) = \begin{cases}
\frac{1}{2} & \text{jika } x = +1 \\
\frac{1}{2} & \text{jika } x = -1 \\
0 & \text{untuk } x \notin \{-1, +1\}
\end{cases}
$$ 
Atau dengan fungsi delta Dirac (untuk kalkulus distribusi):
$$ 
f_{\Delta}(x) = \frac{1}{2}\delta(x-1) + \frac{1}{2}\delta(x+1)
$$ 

**Fungsi Distribusi Kumulatif (CDF):**
Dari rumus umum Tahap 1 dengan $a=1, b=-1$ :
$$ 
F_{\Delta}(x) = \begin{cases}
0 & \text{jika } x < -1 \\
\frac{1}{2} & \text{jika } -1 \leq x < 1 \\
1 & \text{jika } x \geq 1
\end{cases}
$$ 

### 2.2 Sifat-Sifat Matematis Fundamental (Pembuktian dari Rumus Tahap 1)

Sekarang kita substitusikan $p=\frac{1}{2}, a=1, b=-1$  ke dalam semua kotak rumus yang sudah kita dapatkan di Tahap 1.

#### 2.2.1 Ekspektasi (Mean)

Dari rumus $E[X] = p a + (1-p) b$ :
$$ 
E[\Delta] = \frac{1}{2}(1) + \left(1 - \frac{1}{2}\right)(-1)
$$ 
$$ 
E[\Delta] = \frac{1}{2}(1) + \frac{1}{2}(-1) = \frac{1}{2} - \frac{1}{2} = 0
$$ 
$$ 
\boxed{E[\Delta] = 0}
$$ 
**Makna:** Distribusi ini *terpusat* (centered). Ini adalah syarat mutlak untuk estimator gradien SPSA agar tidak bias secara arah.

#### 2.2.2 Variansi dan Momen Kedua

Dari rumus $\text{Var}(X) = p(1-p)(a-b)^2$ :
$$ 
\text{Var}(\Delta) = \frac{1}{2}\left(1 - \frac{1}{2}\right)(1 - (-1))^2
$$ 
$$ 
\text{Var}(\Delta) = \frac{1}{2} \cdot \frac{1}{2} \cdot (2)^2 = \frac{1}{4} \cdot 4 = 1
$$ 
Karena $E[\Delta] = 0$ , maka:
$$ 
E[\Delta^2] = \text{Var}(\Delta) + (E[\Delta])^2 = 1 + 0 = 1
$$ 
$$ 
\boxed{E[\Delta^2] = 1}
$$ 
**Makna:** Variansi = 1 berarti perturbasi memiliki skala yang standar. Dalam SPSA, ini memudahkan analisis konvergensi karena skala langkah $c_k$  secara langsung mengontrol magnitudo perturbasi.

#### 2.2.3 Momen Ketiga dan Simetri

Dari rumus $E[(X-\mu_X)^3] = p(1-p)(1-2p)(a-b)^3$ :
$$ 
E[(\Delta - 0)^3] = E[\Delta^3]
$$ 
Substitusi:
$$ 
E[\Delta^3] = \frac{1}{2} \cdot \frac{1}{2} \cdot \left(1 - 2\cdot\frac{1}{2}\right) \cdot (1 - (-1))^3
$$ 
$$ 
E[\Delta^3] = \frac{1}{4} \cdot (1 - 1) \cdot (2)^3 = \frac{1}{4} \cdot 0 \cdot 8 = 0
$$ 
$$ 
\boxed{E[\Delta^3] = 0}
$$ 
**Makna:** Semua momen ganjil dari distribusi simetris terpusat adalah nol. Ini penting karena dalam ekspansi Taylor dari fungsi objektif, suku-suku ganjil (orde 3, 5, dst.) akan saling menghilangkan ketika kita menghitung selisih $L(\theta+c\Delta) - L(\theta-c\Delta)$ , sehingga *bias* dari estimator SPSA menjadi minimal.

#### 2.2.4 Momen Keempat (The Golden Property)

Ini adalah properti **paling krusial** yang membedakan Rademacher dari distribusi lain (Gaussian, Uniform) dalam konteks SPSA.

Dari rumus momen pusat keempat:
$$ 
E[(X-\mu)^4] = p(1-p)(a-b)^4 [ (1-p)^3 + p^3 ]
$$ 
Untuk $p=\frac{1}{2}$ :
$$ 
(1-p)^3 + p^3 = \left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^3 = \frac{1}{8} + \frac{1}{8} = \frac{1}{4}
$$ 
Maka:
$$ 
E[\Delta^4] = \frac{1}{2} \cdot \frac{1}{2} \cdot (2)^4 \cdot \frac{1}{4}
$$ 
$$ 
E[\Delta^4] = \frac{1}{4} \cdot 16 \cdot \frac{1}{4} = 1
$$ 
$$ 
\boxed{E[\Delta^4] = 1}
$$ 

#### 2.2.5 Kurtosis

Dari definisi Kurtosis $\frac{E[(X-\mu)^4]}{\sigma^4}$ :
$$ 
\text{Kurt}(\Delta) = \frac{E[\Delta^4]}{(\text{Var}(\Delta))^2} = \frac{1}{1^2} = 1
$$ 
$$ 
\boxed{\text{Kurt}(\Delta) = 1}
$$ 

**Makna Mendalam dari $E[\Delta^4]=1$ :**
Untuk *setiap* variabel acak $Z$  dengan $E[Z]=0$  dan $E[Z^2]=1$ , berlaku ketaksamaan:
$$ 
E[Z^4] \geq (E[Z^2])^2 = 1
$$ 
(Ketaksamaan ini berasal dari $\text{Var}(Z^2) = E[Z^4] - (E[Z^2])^2 \geq 0$ ).

Nilai **1** adalah batas bawah teoretis (lower bound). Distribusi Rademacher adalah **satu-satunya** distribusi (selain versi skalarnya) yang *mencapai* batas bawah ini.

**Perbandingan dengan Distribusi Lain:**
- **Rademacher:** $E[\Delta^4] = 1$ 
- **Uniform Kontinu $U[-\sqrt{3}, \sqrt{3}]$ ** (agar variansi = 1): $E[U^4] = \frac{(\sqrt{3})^4}{5} \cdot 2?$  (Mari kita hitung tepat: $\int_{-\sqrt{3}}^{\sqrt{3}} \frac{x^4}{2\sqrt{3}} dx = \frac{1}{2\sqrt{3}} \cdot \frac{2(\sqrt{3})^5}{5} = \frac{9}{5} = 1.8$ ).
- **Gaussian Standar $\mathcal{N}(0,1)$ :** $E[Z^4] = 3$ .

### 2.3 Fungsi Pembangkit Momen (Moment Generating Function / MGF) dan Sifat Ekor (Tail Property)

Fungsi pembangkit momen $M_{\Delta}(t) = E[e^{t\Delta}]$  sangat berguna untuk menganalisis konsentrasi dan batas probabilitas.

$$ 
M_{\Delta}(t) = \frac{1}{2}e^{t(1)} + \frac{1}{2}e^{t(-1)} = \frac{e^t + e^{-t}}{2} = \cosh(t)
$$ 

**Sifat Sub-Gaussian:**
Suatu variabel acak $X$  dengan mean nol disebut sub-Gaussian dengan parameter $\sigma^2$  jika:
$$ 
E[e^{tX}] \leq \exp\left(\frac{\sigma^2 t^2}{2}\right)
$$ 
Untuk Rademacher, kita tahu bahwa $\cosh(t) \leq \exp(t^2/2)$  untuk semua $t \in \mathbb{R}$ . Ini dapat dibuktikan dengan ekspansi Taylor:
- $\cosh(t) = 1 + \frac{t^2}{2!} + \frac{t^4}{4!} + \dots$ 
- $\exp(t^2/2) = 1 + \frac{t^2}{2} + \frac{t^4}{2^2 \cdot 2!} + \dots$ 

Karena $(2k)! \geq 2^k k!$ , jelas bahwa $\frac{1}{(2k)!} \leq \frac{1}{2^k k!}$ , sehingga $\cosh(t) \leq \exp(t^2/2)$ .

Ini membuktikan bahwa Rademacher adalah **sub-Gaussian dengan parameter $\sigma^2 = 1$ **. Dalam konteks SPSA, ini berarti perturbasi memiliki ekor probabilitas yang sangat ringan (bounded support), yang memberikan jaminan konsentrasi yang kuat untuk estimator gradien.

### 2.4 Vektor Rademacher Multivariat

Dalam SPSA, kita tidak hanya menggunakan satu skalar $\Delta$ , melainkan vektor $\mathbf{\Delta} = (\Delta_1, \Delta_2, \dots, \Delta_p)^T$  di mana setiap komponen $\Delta_i \stackrel{\text{i.i.d.}}{\sim} \text{Rademacher}$  dan independen satu sama lain.

**Sifat Ortogonalitas Stokastik:**
Karena independen dan mean nol:
$$ 
E[\Delta_i \Delta_j] = E[\Delta_i]E[\Delta_j] = 0 \quad \text{untuk } i \neq j
$$ 
$$ 
E[\Delta_i^2] = 1
$$ 
Ini dapat diringkas sebagai:
$$ 
E[\mathbf{\Delta} \mathbf{\Delta}^T] = \mathbf{I}_p
$$ 
Di mana $\mathbf{I}_p$  adalah matriks identitas $p \times p$ .

**Sifat Momen Keempat Campuran (Mixed Fourth Moments):**
Ini akan sangat krusial dalam analisis variansi estimator SPSA di Tahap 4.

Untuk $i \neq j$ :
$$ 
E[\Delta_i^2 \Delta_j^2] = E[\Delta_i^2]E[\Delta_j^2] = 1 \cdot 1 = 1
$$ 
Untuk $i \neq j \neq k \neq l$ :
$$ 
E[\Delta_i \Delta_j \Delta_k \Delta_l] = 0
$$ 
Ini semua adalah konsekuensi langsung dari independensi dan $E[\Delta_i] = 0$ .

**Ringkasan Tahap 2:**
Kita telah membuktikan secara aljabar bahwa Rademacher adalah distribusi dengan **mean nol**, **variansi satu**, **skewness nol**, dan **momen keempat minimum (=1)**. Properti ini menjadikannya kandidat ideal untuk perturbasi simultan dalam optimasi dimensi tinggi.

---

Apakah Anda siap melanjutkan ke **Tahap 3: Motivasi di Balik SPSA**? Di sana saya akan menjelaskan secara matematis mengapa kita membutuhkan metode perturbasi simultan dibandingkan metode *finite difference* biasa ketika dimensi $p$  besar, dan bagaimana vektor Rademacher mengatasi *curse of dimensionality*.

---
---
Baik, kita lanjutkan ke **Tahap 3**. Di sini kita akan membangun motivasi kuat mengapa algoritma SPSA diperlukan, dan mengapa pendekatan naif seperti *Finite Difference* (FD) gagal secara komputasional ketika dimensi parameter $p$  besar.

---

## Tahap 3: Motivasi di Balik SPSA (Mengapa Bukan Finite Difference Biasa?)

### 3.1 Formulasi Masalah Optimasi Stokastik

Kita menghadapi masalah optimasi tanpa kendala (*unconstrained optimization*):

$$ 
\min_{\theta \in \mathbb{R}^p} L(\theta)
$$ 

Di mana:
- $\theta = (\theta_1, \theta_2, \dots, \theta_p)^T$  adalah vektor parameter berdimensi $p$ .
- $L: \mathbb{R}^p \to \mathbb{R}$  adalah **fungsi objektif** (loss function) yang:
  - *Terdiferensialkan secara kontinu* (setidaknya $C^2$  atau $C^3$ ).
  - *Evaluasi mahal* (expensive to evaluate) — misalnya simulasi Monte Carlo, pelatihan model machine learning besar, atau running eksperimen fisik.
  - *Gradien tidak tersedia secara analitik* — kita tidak memiliki rumus closed-form untuk $\nabla L(\theta)$ .

**Tujuan Algoritma:**
Mencari aproksimasi $\theta^*$  yang meminimalkan $L(\theta)$  menggunakan estimator gradien yang dihitung dari evaluasi fungsi $L$  yang berisik (*noisy*) atau mahal.

### 3.2 Metode Klasik: Finite Difference (FD) dan Kompleksitasnya

#### 3.2.1 Finite Difference Dua-Sisi (Two-Sided FD)

Estimator gradien dengan FD dua-sisi untuk komponen ke-$i$  adalah:

$$ 
\hat{g}_i^{\text{FD}}(\theta) = \frac{L(\theta + c \mathbf{e}_i) - L(\theta - c \mathbf{e}_i)}{2c}
$$ 

Di mana:
- $c > 0$  adalah **lebar langkah perturbasi** (perturbation step size), biasanya kecil ($c \approx 10^{-5}$ ).
- $\mathbf{e}_i$  adalah vektor basis standar ke-$i$  di $\mathbb{R}^p$  (semua elemen 0 kecuali 1 di posisi $i$ ).

Untuk mendapatkan **seluruh vektor gradien** $\hat{\mathbf{g}}^{\text{FD}}(\theta) \in \mathbb{R}^p$ , kita harus mengulangi perhitungan ini untuk setiap $i = 1, 2, \dots, p$ .

**Analisis Kompleksitas Evaluasi Fungsi:**

- **Per Iterasi:** Setiap komponen $\hat{g}_i$  membutuhkan **2 evaluasi fungsi** ($L(\theta + c\mathbf{e}_i)$  dan $L(\theta - c\mathbf{e}_i)$ ).
- **Total Evaluasi per Iterasi:** $2p$ .

Jika $p$  besar (misalnya $p = 10^6$  parameter dalam neural network modern), maka **satu langkah iterasi optimasi** dengan FD membutuhkan **2 juta evaluasi fungsi**. Ini tidak praktis (*computationally prohibitive*) jika satu evaluasi $L(\theta)$  membutuhkan waktu beberapa detik atau menit.

#### 3.2.2 Akurasi Finite Difference

Dengan ekspansi Taylor di sekitar $\theta$ :
$$ 
L(\theta + c\mathbf{e}_i) = L(\theta) + c \frac{\partial L}{\partial \theta_i} + \frac{c^2}{2} \frac{\partial^2 L}{\partial \theta_i^2} + O(c^3)
$$ 
$$ 
L(\theta - c\mathbf{e}_i) = L(\theta) - c \frac{\partial L}{\partial \theta_i} + \frac{c^2}{2} \frac{\partial^2 L}{\partial \theta_i^2} + O(c^3)
$$ 

Selisih keduanya:
$$ 
L(\theta + c\mathbf{e}_i) - L(\theta - c\mathbf{e}_i) = 2c \frac{\partial L}{\partial \theta_i} + O(c^3)
$$ 

Sehingga estimator FD:
$$ 
\hat{g}_i^{\text{FD}}(\theta) = \frac{\partial L}{\partial \theta_i} + O(c^2)
$$ 

**Bias FD:** $O(c^2)$ . Untuk mendapatkan bias kecil, kita perlu $c$  kecil. Namun, jika evaluasi fungsi mengandung *noise* (misalnya variansi $\sigma^2$ ), maka variansi estimator FD adalah $\frac{\sigma^2}{2c^2}$ , yang **meledak** saat $c \to 0$ . Ini adalah **trade-off bias-varians** klasik.

### 3.3 Alternatif: Simultaneous Perturbation (SP)

Ide revolusioner dari SPSA (diperkenalkan oleh James Spall, 1992) adalah:

> *"Alih-alih meng-perturbasi satu per satu dimensi, kita **meng-perturbasi semua dimensi secara simultan** dengan vektor acak."*

#### 3.3.1 Estimator SPSA Dasar

Pilih **vektor perturbasi acak** $\mathbf{\Delta} \in \mathbb{R}^p$  dengan komponen i.i.d. dari distribusi simetris dengan mean nol dan variansi satu.

Estimator gradien SPSA dua-sisi adalah:

$$ 
\hat{\mathbf{g}}^{\text{SPSA}}(\theta) = \frac{L(\theta + c \mathbf{\Delta}) - L(\theta - c \mathbf{\Delta})}{2c} \begin{pmatrix} \Delta_1^{-1} \\ \Delta_2^{-1} \\ \vdots \\ \Delta_p^{-1} \end{pmatrix}
$$ 

Atau dalam notasi vektor ringkas:
$$ 
\boxed{\hat{\mathbf{g}}^{\text{SPSA}}(\theta) = \frac{L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta})}{2c} \mathbf{\Delta}^{-1}}
$$ 
Di mana $\mathbf{\Delta}^{-1} = (\Delta_1^{-1}, \Delta_2^{-1}, \dots, \Delta_p^{-1})^T$ .

**Catatan Praktis:**
Karena $\Delta_i \in \{-1, +1\}$  untuk Rademacher, maka $\Delta_i^{-1} = \Delta_i$ . Sehingga untuk Rademacher, rumusnya menjadi sangat sederhana:

$$ 
\boxed{\hat{\mathbf{g}}^{\text{SPSA}}(\theta) = \frac{L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta})}{2c} \mathbf{\Delta}}
$$ 

#### 3.3.2 Kompleksitas Evaluasi Fungsi SPSA

**Keajaiban SPSA:**
Untuk menghitung estimator gradien **seluruh vektor** $\hat{\mathbf{g}} \in \mathbb{R}^p$ , kita hanya membutuhkan **2 evaluasi fungsi**:
1. $L(\theta + c\mathbf{\Delta})$ 
2. $L(\theta - c\mathbf{\Delta})$ 

**Total Evaluasi per Iterasi: 2** (independen terhadap $p$ !).

**Perbandingan Dramatis:**
| Metode | Evaluasi Fungsi per Iterasi | Untuk $p=10^6$  |
| :--- | :---: | :---: |
| Finite Difference | $2p$  | 2,000,000 |
| **SPSA** | **2** | **2** |

**Saving Factor:** $\frac{2p}{2} = p$ . Untuk $p$  besar, SPSA memberikan percepatan **jutaan kali** per iterasi.

### 3.4 Mengapa Harus Distribusi Simetris dan Mean Nol?

Mari kita lihat secara intuitif mengapa distribusi $\mathbf{\Delta}$  harus memiliki properti yang kita turunkan di Tahap 2.

Ekspansi Taylor dari fungsi skalar $L(\theta + c\mathbf{\Delta})$  di sekitar $\theta$ :

$$ 
L(\theta + c\mathbf{\Delta}) = L(\theta) + c \mathbf{\Delta}^T \nabla L(\theta) + \frac{c^2}{2} \mathbf{\Delta}^T \mathbf{H}(\theta) \mathbf{\Delta} + O(c^3)
$$ 
$$ 
L(\theta - c\mathbf{\Delta}) = L(\theta) - c \mathbf{\Delta}^T \nabla L(\theta) + \frac{c^2}{2} \mathbf{\Delta}^T \mathbf{H}(\theta) \mathbf{\Delta} + O(c^3)
$$ 
Di mana $\mathbf{H}(\theta)$  adalah matriks Hessian $p \times p$ .

**Selisih Kedua Evaluasi:**
$$ 
L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta}) = 2c \mathbf{\Delta}^T \nabla L(\theta) + O(c^3)
$$ 
*(Perhatikan bahwa suku kuadratik $\mathbf{\Delta}^T \mathbf{H} \mathbf{\Delta}$  saling menghilangkan!)*

**Estimator SPSA:**
$$ 
\hat{\mathbf{g}} = \frac{2c \mathbf{\Delta}^T \nabla L(\theta) + O(c^3)}{2c} \mathbf{\Delta}^{-1} = (\mathbf{\Delta}^T \nabla L) \mathbf{\Delta}^{-1} + O(c^2)
$$ 

Komponen ke-$i$ :
$$ 
\hat{g}_i = \frac{\sum_{j=1}^p \Delta_j \frac{\partial L}{\partial \theta_j}}{\Delta_i} = \frac{\partial L}{\partial \theta_i} + \sum_{j \neq i} \frac{\Delta_j}{\Delta_i} \frac{\partial L}{\partial \theta_j}
$$ 

**Ambil Ekspektasi terhadap $\mathbf{\Delta}$ :**
Agar estimator ini tidak bias (atau setidaknya konsisten), suku silang $\sum_{j \neq i} \frac{\Delta_j}{\Delta_i} \frac{\partial L}{\partial \theta_j}$  harus memiliki ekspektasi **nol**.

Karena $\Delta_i$  dan $\Delta_j$  independen untuk $i \neq j$ :
$$ 
E\left[ \frac{\Delta_j}{\Delta_i} \right] = E[\Delta_j] \cdot E\left[ \frac{1}{\Delta_i} \right]
$$ 
Untuk Rademacher, $E[\Delta_j] = 0$ , sehingga suku ini otomatis **nol**.

Jika kita menggunakan distribusi yang **tidak memiliki mean nol** (misal Bernoulli dengan $p \neq 0.5$ ), maka $E[\Delta_j] \neq 0$ , dan estimator akan memiliki **bias struktural** yang tidak hilang bahkan ketika $c \to 0$ .

### 3.5 Masalah dengan Distribusi Kontinu (Seperti Gaussian)

Jika kita menggunakan $\Delta_i \sim \mathcal{N}(0,1)$ , maka $E[\Delta_j] = 0$  terpenuhi. Namun, muncul masalah baru:

1.  **Inversi $\Delta_i^{-1}$ :** Untuk Gaussian, $\Delta_i$  bisa bernilai sangat dekat dengan nol. Momen dari $1/\Delta_i$  **tidak terdefinisi** ($E[1/|\Delta_i|] = \infty$ ). Ini menyebabkan variansi estimator SPSA menjadi **tak hingga** (infinite variance).
2.  **Variansi Besar:** Bahkan jika kita mengabaikan singularitas, momen keempat Gaussian ($E[\Delta_i^4] = 3$ ) menghasilkan variansi estimator yang jauh lebih besar dibandingkan Rademacher ($E[\Delta_i^4] = 1$ ). Ini akan kita buktikan secara rigor di Tahap 4.

### 3.6 Ringkasan Intuisi Tahap 3

- **FD:** Akurat untuk $p$  kecil, tetapi kompleksitas $O(p)$  membuatnya tidak layak untuk $p$  besar.
- **SPSA:** Kompleksitas $O(1)$  evaluasi fungsi per iterasi, memungkinkan optimasi dimensi ultra-tinggi.
- **Distribusi Perturbasi:** Harus simetris dan memiliki mean nol agar estimator tidak bias.
- **Kandidat Distribusi:** Rademacher muncul sebagai pilihan alami karena *bounded support* (menghindari masalah inversi) dan momen keempat minimal (menjanjikan variansi rendah).

---

Ini adalah fondasi motivasi. Sekarang kita siap untuk memasuki **Tahap 4**, yaitu jantung pembuktian matematis: **Mengapa Rademacher optimal?** Di sini kita akan menghitung ekspektasi dan variansi estimator SPSA secara eksplisit, dan membuktikan bahwa Rademacher meminimalkan variansi di antara semua distribusi yang memenuhi syarat.

Apakah Anda siap untuk **Tahap 4: Pembuktian Rigor Optimalitas Rademacher**?

---
---
Baik, kita masuk ke inti teoretis dari studi ini: **Tahap 4**. Di sini kita akan melakukan pembuktian matematis yang rigor untuk menunjukkan bahwa di antara semua distribusi perturbasi yang memenuhi syarat dasar, **distribusi Rademacher adalah pilihan optimal** karena menghasilkan estimator gradien SPSA dengan variansi minimum.

Kita akan membangun pembuktian ini dalam tiga bagian:
1.  **Ekspansi Taylor Stokastik** dan perhitungan ekspektasi (pembuktian unbiasedness asimtotik).
2.  **Dekomposisi Variansi** estimator SPSA.
3.  **Teorema Optimalitas** dan pembuktian bahwa Rademacher meminimalkan suku dominan variansi.

---

## Tahap 4: Pembuktian Rigor Optimalitas Rademacher untuk SPSA

### 4.1 Asumsi Formal dan Notasi

Sebelum memulai pembuktian, kita perlu menetapkan asumsi regulasi yang standar dalam literatur SPSA (Spall, 1992).

**Asumsi A1 (Smoothness):**
Fungsi $L: \mathbb{R}^p \to \mathbb{R}$  terdiferensialkan secara kontinu hingga orde ketiga ($C^3$ ), dan turunan ketiga terbatas secara lokal. Secara spesifik, untuk setiap $\theta$  dalam domain kompak, terdapat konstanta $M > 0$  sedemikian sehingga:

$$ 
\left| \frac{\partial^3 L(\theta)}{\partial \theta_i \partial \theta_j \partial \theta_k} \right| \leq M \quad \forall i,j,k
$$ 

**Asumsi A2 (Distribusi Perturbasi):**
Vektor perturbasi $\mathbf{\Delta} = (\Delta_1, \dots, \Delta_p)^T$  terdiri dari komponen-komponen i.i.d. yang memenuhi:
1.  **Simetri Terpusat:** $E[\Delta_i] = 0$ 
2.  **Variansi Satuan:** $E[\Delta_i^2] = 1$ 
3.  **Momen Terbatas:** $E[|\Delta_i|^k] < \infty$  untuk $k$  secukupnya (minimal hingga orde 4).
4.  **Independensi:** $\Delta_i \perp \!\!\! \perp \Delta_j$  untuk $i \neq j$ .

**Notasi:**
- $\nabla L(\theta) = \mathbf{g}(\theta) = (g_1, g_2, \dots, g_p)^T$ 
- $\mathbf{H}(\theta) = \nabla^2 L(\theta)$  adalah matriks Hessian $p \times p$  dengan elemen $H_{ij} = \frac{\partial^2 L}{\partial \theta_i \partial \theta_j}$ 
- Estimator SPSA dua-sisi (two-sided):
  $$ 
  \hat{\mathbf{g}}(\theta) = \frac{L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta})}{2c} \mathbf{\Delta}^{\dagger}
  $$ 
  Di mana $\mathbf{\Delta}^{\dagger} = (\Delta_1^{-1}, \dots, \Delta_p^{-1})^T$ . Untuk Rademacher, $\mathbf{\Delta}^{\dagger} = \mathbf{\Delta}$ .

### 4.2 Bagian I: Ekspektasi dan Bias Asimtotik Estimator SPSA

Kita akan membuktikan bahwa estimator SPSA adalah aproksimasi orde pertama yang valid dari gradien sejati.

**Langkah 1: Ekspansi Taylor Orde Tiga**

Evaluasi fungsi di titik $\theta + c\mathbf{\Delta}$ :
$$ 
L(\theta + c\mathbf{\Delta}) = L(\theta) + c \sum_{i=1}^p g_i \Delta_i + \frac{c^2}{2} \sum_{i=1}^p \sum_{j=1}^p H_{ij} \Delta_i \Delta_j + \frac{c^3}{6} \sum_{i,j,k} \frac{\partial^3 L(\tilde{\theta}_+)}{\partial \theta_i \partial \theta_j \partial \theta_k} \Delta_i \Delta_j \Delta_k
$$ 
Di mana $\tilde{\theta}_+$  adalah titik antara $\theta$  dan $\theta + c\mathbf{\Delta}$ .

Evaluasi di titik $\theta - c\mathbf{\Delta}$ :
$$ 
L(\theta - c\mathbf{\Delta}) = L(\theta) - c \sum_{i=1}^p g_i \Delta_i + \frac{c^2}{2} \sum_{i=1}^p \sum_{j=1}^p H_{ij} \Delta_i \Delta_j - \frac{c^3}{6} \sum_{i,j,k} \frac{\partial^3 L(\tilde{\theta}_-)}{\partial \theta_i \partial \theta_j \partial \theta_k} \Delta_i \Delta_j \Delta_k
$$ 

**Langkah 2: Selisih Kedua Evaluasi**

Kurangkan persamaan kedua dari persamaan pertama:
$$ 
L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta}) = 2c \sum_{i=1}^p g_i \Delta_i + \frac{c^3}{6} \sum_{i,j,k} \left( \frac{\partial^3 L(\tilde{\theta}_+)}{\partial \theta_i \partial \theta_j \partial \theta_k} + \frac{\partial^3 L(\tilde{\theta}_-)}{\partial \theta_i \partial \theta_j \partial \theta_k} \right) \Delta_i \Delta_j \Delta_k
$$ 

Perhatikan bahwa **suku kuadratik $\frac{c^2}{2} \mathbf{\Delta}^T \mathbf{H} \mathbf{\Delta}$  saling menghilangkan**. Ini adalah alasan mengapa SPSA menggunakan perturbasi dua-sisi (two-sided).

Kita definisikan suku sisa (*remainder term*):
$$ 
R_3(\mathbf{\Delta}, c) = \frac{1}{12} \sum_{i,j,k} \left( \frac{\partial^3 L(\tilde{\theta}_+)}{\partial \theta_i \partial \theta_j \partial \theta_k} + \frac{\partial^3 L(\tilde{\theta}_-)}{\partial \theta_i \partial \theta_j \partial \theta_k} \right) \Delta_i \Delta_j \Delta_k
$$ 
Berdasarkan Asumsi A1, $|R_3| \leq \frac{M}{6} \sum_{i,j,k} |\Delta_i \Delta_j \Delta_k| = \frac{M}{6} \left( \sum_{i=1}^p |\Delta_i| \right)^3$ .

Maka:
$$ 
\frac{L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta})}{2c} = \sum_{j=1}^p g_j \Delta_j + c^2 R_3(\mathbf{\Delta}, c)
$$ 

**Langkah 3: Estimator untuk Komponen ke-$i$ **

Kalikan dengan $\Delta_i^{-1}$ :
$$ 
\hat{g}_i(\theta) = g_i + \sum_{j \neq i} g_j \frac{\Delta_j}{\Delta_i} + c^2 \frac{R_3(\mathbf{\Delta}, c)}{\Delta_i}
$$ 

**Langkah 4: Ekspektasi (Unbiasedness Asimtotik)**

Ambil ekspektasi terhadap distribusi $\mathbf{\Delta}$  (kondisional pada $\theta$ ):
$$ 
E[\hat{g}_i(\theta) | \theta] = g_i + \sum_{j \neq i} g_j E\left[ \frac{\Delta_j}{\Delta_i} \right] + c^2 E\left[ \frac{R_3}{\Delta_i} \right]
$$ 

Berdasarkan Asumsi A2, $\Delta_i$  dan $\Delta_j$  independen untuk $i \neq j$ , dan $E[\Delta_j] = 0$ :
$$ 
E\left[ \frac{\Delta_j}{\Delta_i} \right] = E[\Delta_j] E[\Delta_i^{-1}] = 0 \cdot E[\Delta_i^{-1}] = 0
$$ 
*(Catatan: Untuk Rademacher, $E[\Delta_i^{-1}] = E[\Delta_i] = 0$ , jadi hasilnya tetap 0. Untuk distribusi simetris kontinu, $E[\Delta_i^{-1}]$  mungkin ada dan bernilai 0 karena sifat ganjil.)*

Selanjutnya, untuk suku sisa, dengan asumsi momen terbatas (A2.3) dan boundedness $R_3$  (A1), suku $c^2 E[\dots]$  adalah $O(c^2)$ .

**Kesimpulan Bias:**
$$ 
\boxed{E[\hat{\mathbf{g}}(\theta)] = \nabla L(\theta) + O(c^2)}
$$ 
Estimator SPSA adalah **asimtotik tak bias** (unbiased asymptotically) saat $c \to 0$ . Bias berorde $c^2$ , sama seperti Finite Difference.

### 4.3 Bagian II: Dekomposisi Variansi Estimator SPSA

Ini adalah bagian terpenting. Kita akan menghitung matriks kovariansi dari $\hat{\mathbf{g}}(\theta)$ .

Dari dekomposisi di atas, aproksimasi orde pertama (mengabaikan $O(c^2)$ ) dari estimator adalah:
$$ 
\hat{g}_i(\theta) \approx g_i + \sum_{j \neq i} g_j \frac{\Delta_j}{\Delta_i}
$$ 

**Definisi 4.3.1 (Variansi Orde Pertama):**
$$ 
\text{Var}(\hat{g}_i) \approx E \left[ \left( \sum_{j \neq i} g_j \frac{\Delta_j}{\Delta_i} \right)^2 \right]
$$ 

**Langkah 1: Kuadratkan dan Ekspansi**
$$ 
\left( \sum_{j \neq i} g_j \frac{\Delta_j}{\Delta_i} \right)^2 = \sum_{j \neq i} g_j^2 \frac{\Delta_j^2}{\Delta_i^2} + \sum_{j \neq i} \sum_{k \neq i, j} g_j g_k \frac{\Delta_j \Delta_k}{\Delta_i^2}
$$ 

**Langkah 2: Ekspektasi**
Karena $\Delta_j$  dan $\Delta_k$  independen dan $E[\Delta_j] = 0$ , suku silang $E[\Delta_j \Delta_k] = 0$  untuk $j \neq k$ . Suku yang melibatkan $j = k$  tetapi $j \neq i$  tetap ada.

$$ 
\text{Var}(\hat{g}_i) \approx \sum_{j \neq i} g_j^2 E\left[ \frac{\Delta_j^2}{\Delta_i^2} \right]
$$ 

**Langkah 3: Evaluasi Ekspektasi**
Karena $\Delta_j$  dan $\Delta_i$  independen untuk $j \neq i$ , dan $E[\Delta_j^2] = 1$  (A2.2):
$$ 
E\left[ \frac{\Delta_j^2}{\Delta_i^2} \right] = E[\Delta_j^2] \cdot E[\Delta_i^{-2}] = 1 \cdot E[\Delta_i^{-2}]
$$ 

**Definisi 4.3.2 (Konstanta Variansi):**
Misalkan $\kappa = E[\Delta_i^{-2}]$ . Untuk distribusi yang berbeda, nilai $\kappa$  berbeda:
- **Rademacher:** $\Delta_i \in \{-1, +1\} \implies \Delta_i^{-2} = 1 \implies \kappa_{\text{Rad}} = 1$ .
- **Gaussian $\mathcal{N}(0,1)$ :** $E[Z^{-2}] = \infty$  (tidak terdefinisi, variansi meledak).
- **Uniform $U[-\sqrt{3}, \sqrt{3}]$ :** $E[\Delta^{-2}] = \infty$  karena integral $\int_{-\sqrt{3}}^{\sqrt{3}} \frac{1}{x^2} dx$  divergen di 0.

**Ini adalah temuan krusial pertama:**
Setiap distribusi dengan **probabilitas massa di sekitar nol** akan menghasilkan $\kappa = \infty$ , membuat SPSA tidak stabil secara numerik. **Distribusi Rademacher secara implisit menghindari singularitas ini** karena $\Delta_i \neq 0$  selalu.

Dengan asumsi $\kappa < \infty$  (yang hanya mungkin untuk distribusi diskrit yang terpisah dari nol, seperti Rademacher), maka:
$$ 
\boxed{\text{Var}(\hat{g}_i) \approx \kappa \sum_{j \neq i} g_j^2}
$$ 

**Total Variansi (Trace Kovariansi):**
$$ 
\text{tr}(\text{Cov}(\hat{\mathbf{g}})) = \sum_{i=1}^p \text{Var}(\hat{g}_i) \approx \kappa \sum_{i=1}^p \sum_{j \neq i} g_j^2 = \kappa (p-1) \| \nabla L \|^2
$$ 

**Interpretasi Geometris:**
Variansi estimator SPSA untuk satu komponen **tumbuh secara linear terhadap magnitudo kuadrat dari semua komponen gradien lainnya**. Ini adalah harga yang harus dibayar untuk penghematan evaluasi fungsi. Namun, dalam optimasi stokastik, kita menggunakan **rata-rata bergerak** (running average) atau **step size menurun** ($a_k \to 0$ ) untuk meredam variansi ini.

### 4.4 Bagian III: Teorema Optimalitas Rademacher (Minimisasi Variansi Orde Tinggi)

Sekarang kita melangkah lebih jauh. Ekspansi di atas hanya orde pertama. Jika kita memasukkan suku orde lebih tinggi dari ekspansi Taylor, variansi total sebenarnya melibatkan **momen keempat** dari distribusi perturbasi.

**Teorema 4.4.1 (Spall, 1992 - Optimality of Bernoulli Distribution):**
*Di antara semua distribusi $\Delta$  yang memenuhi Asumsi A2 (mean 0, variansi 1, simetris), distribusi Bernoulli simetris (Rademacher) meminimalkan variansi asimtotik dari estimator SPSA.*

**Bukti:**

Kita perlu menghitung variansi dari estimator SPSA dengan memasukkan suku kuadratik dari ekspansi Taylor. Ekspansi penuh (orde 2) dari selisih fungsi adalah:

$$ 
L(\theta + c\mathbf{\Delta}) - L(\theta - c\mathbf{\Delta}) = 2c \mathbf{g}^T \mathbf{\Delta} + \frac{c^3}{3} \mathbf{T}(\theta, \mathbf{\Delta}) + \dots
$$ 
Di mana $\mathbf{T}$  melibatkan turunan ketiga. Suku kuadratik memang menghilang, tetapi ketika kita menghitung **variansi**, kita mengkuadratkan estimator:

$$ 
\hat{\mathbf{g}} \hat{\mathbf{g}}^T = \dots
$$ 

Untuk mendapatkan gambaran lengkap variansi, kita perlu melihat **Momen Keempat Campuran (Mixed Fourth Moments)**. Variansi dari $\hat{g}_i$  akan melibatkan suku-suku seperti $E[\Delta_i^2 \Delta_j^2]$  dan $E[\Delta_i^4]$ .

Mari kita turunkan **batas bawah Cramér-Rao-like** untuk variansi SPSA.

**Langkah 1: Dekomposisi Variansi Total yang Ditingkatkan**

Dengan perhitungan yang lebih teliti (lihat Spall, 1992, Lemma 1), variansi dari $\hat{g}_i$  dapat dinyatakan sebagai:

$$ 
\text{Var}(\hat{g}_i) = c^{-2} \left( A + B \cdot E[\Delta_i^4] + C \cdot E[\Delta_i^2]^2 + \dots \right)
$$ 
Karena $E[\Delta_i^2] = 1$  sudah tetap, variansi bergantung pada **Ekses Kurtosis** yang diukur melalui $E[\Delta_i^4]$ .

**Langkah 2: Optimasi Konveks Momen Keempat**

Kita memiliki batasan:
1. $E[\Delta] = 0$ 
2. $E[\Delta^2] = 1$ 

Kita ingin meminimalkan $E[\Delta^4]$  terhadap semua distribusi yang memenuhi batasan tersebut.

Gunakan ketaksamaan **Lyapunov** atau **Hölder**:
$$ 
E[|\Delta|^q]^{1/q} \geq E[|\Delta|^p]^{1/p} \quad \text{untuk } q > p
$$ 
Ini tidak langsung memberikan batas bawah untuk $E[\Delta^4]$  dari $E[\Delta^2]$ .

Gunakan **Ketaksamaan Variansi**:
Misalkan $Z = \Delta^2$ . Maka $E[Z] = 1$ .
Variansi dari $Z$  adalah:
$$ 
\text{Var}(Z) = E[Z^2] - (E[Z])^2 = E[\Delta^4] - 1
$$ 
Karena variansi selalu non-negatif:
$$ 
\text{Var}(Z) \geq 0 \implies E[\Delta^4] \geq 1
$$ 

**Kapan kesamaan tercapai?**
$\text{Var}(Z) = 0$  jika dan hanya jika $Z$  adalah konstanta hampir pasti (*almost surely*).
Jika $Z = \Delta^2 = 1$  hampir pasti, maka $\Delta \in \{-1, +1\}$ .
Karena $E[\Delta] = 0$ , probabilitas untuk +1 dan -1 harus sama, yaitu $p = 1/2$ .

**Kesimpulan:**
Nilai minimum dari $E[\Delta^4]$  adalah **1**, dan minimum ini **hanya dicapai oleh distribusi Rademacher**.

**Langkah 3: Dampak pada Variansi SPSA**

Ketika kita mengevaluasi suku-suku dalam matriks kovariansi SPSA, suku yang melibatkan $E[\Delta_i^4]$  muncul sebagai pengali dari kuadrat elemen diagonal Hessian ($H_{ii}^2$ ) dan suku lainnya.

Untuk distribusi **Rademacher** ($E[\Delta^4] = 1$ ):
$$ 
\text{Var}_{\text{Rad}}(\hat{g}_i) = \sigma^2_{\text{base}} + c^2 \cdot (\text{faktor}) \cdot 1
$$ 

Untuk distribusi **Gaussian** ($E[\Delta^4] = 3$ ):
$$ 
\text{Var}_{\text{Gauss}}(\hat{g}_i) = \sigma^2_{\text{base}} + c^2 \cdot (\text{faktor}) \cdot 3
$$ 

Untuk distribusi **Uniform** ($E[\Delta^4] = 1.8$ ):
$$ 
\text{Var}_{\text{Unif}}(\hat{g}_i) = \sigma^2_{\text{base}} + c^2 \cdot (\text{faktor}) \cdot 1.8
$$ 

Karena $c > 0$ , jelas bahwa **Rademacher menghasilkan variansi asimtotik (orde $c^2$ ) yang paling kecil**.

### 4.5 Tabel Perbandingan Rigor Distribusi Perturbasi

| Distribusi | Syarat $E[\Delta]=0, E[\Delta^2]=1$  | $\kappa = E[\Delta^{-2}]$  | $E[\Delta^4]$  | Stabilitas Numerik SPSA |
| :--- | :---: | :---: | :---: | :---: |
| **Rademacher** | ✅ | **1** | **1** | **Optimal** |
| Gaussian $\mathcal{N}(0,1)$  | ✅ | $\infty$  | 3 | Tidak Stabil (Variansi Tak Hingga) |
| Uniform $U[-\sqrt{3}, \sqrt{3}]$  | ✅ | $\infty$  | 1.8 | Tidak Stabil (Inversi Nol) |
| Bernoulli Asimetris | ❌ ($E[\Delta]\neq0$ ) | Hingga | >1 | **Bias** |

### 4.6 Kesimpulan Tahap 4

Kita telah membuktikan dua properti fundamental yang menjadikan Rademacher sebagai "senjata rahasia" SPSA:

1.  **Eksistensi Momen Invers:** $E[\Delta_i^{-2}] = 1 < \infty$ . Ini mencegah ledakan variansi akibat pembagian dengan bilangan mendekati nol. Ini adalah **syarat perlu** agar SPSA bekerja.
2.  **Optimalitas Momen Keempat:** $E[\Delta_i^4] = 1$  adalah **minimum global** untuk semua distribusi dengan variansi satuan. Ini meminimalkan kontribusi variansi dari suku-suku kelengkungan (kurvatur) fungsi objektif.

Dengan demikian, secara matematis rigor, **distribusi Rademacher adalah distribusi perturbasi optimal untuk algoritma SPSA**.

---

Apakah Anda ingin melanjutkan ke **Tahap 5: Konsekuensi Praktis dan Konvergensi Algoritma**? Di sana kita akan melihat bagaimana sifat-sifat ini diterjemahkan ke dalam jaminan konvergensi $\theta_k \to \theta^*$  dan pemilihan parameter $a_k, c_k$  yang optimal.

---
---
Baik, kita lanjutkan ke **Tahap 5**, yang merupakan tahap penutup. Di sini kita akan menjembatani teori momen dan variansi yang telah kita buktikan di Tahap 4 dengan realitas implementasi algoritma. Kita akan membahas:

1. **Algoritma Iteratif SPSA Lengkap**
2. **Kondisi Step Size untuk Konvergensi**
3. **Analisis Konvergensi Kuadratik Rata-rata (Mean-Square Convergence)**
4. **Trade-off Bias-Varians pada Parameter \(c_k\)**
5. **Peran Krusial Sifat Sub-Gaussian Rademacher dalam Konsentrasi**

---

## Tahap 5: Konsekuensi Praktis dan Konvergensi Algoritma

### 5.1 Algoritma Iteratif SPSA dengan Rademacher

**Algoritma 5.1.1 (SPSA Standar dengan Rademacher):**

**Inisialisasi:**
- Pilih tebakan awal $\theta_0 \in \mathbb{R}^p$ .
- Tentukan barisan **step size iterasi** (gain sequences):
  - $a_k = \frac{a}{(k+1+A)^\alpha}$  (learning rate untuk update parameter)
  - $c_k = \frac{c}{(k+1)^\gamma}$  (lebar perturbasi)

**Parameter Standar (Spall, 1998):**
- $\alpha = 0.602$ , $\gamma = 0.101$ , $A \approx 0.1 \times \text{(jumlah iterasi total)}$ 
- $a, c$  dipilih berdasarkan skala masalah.

**Iterasi $k = 0, 1, 2, \dots$ :**
1. **Bangkitkan Vektor Perturbasi Rademacher:**
   $$ 
   \mathbf{\Delta}_k \sim \text{Rademacher}^p
   $$ 
   (Setiap komponen $\Delta_{k,i} \in \{-1, +1\}$  dengan probabilitas $1/2$ ).

2. **Evaluasi Fungsi Dua Kali:**
   $$ 
   L_k^+ = L(\theta_k + c_k \mathbf{\Delta}_k)
   $$ 
   $$ 
   L_k^- = L(\theta_k - c_k \mathbf{\Delta}_k)
   $$ 

3. **Hitung Estimator Gradien SPSA:**
   $$ 
   \hat{\mathbf{g}}_k(\theta_k) = \frac{L_k^+ - L_k^-}{2c_k} \mathbf{\Delta}_k
   $$ 
   (Menggunakan fakta bahwa $\Delta_{k,i}^{-1} = \Delta_{k,i}$  untuk Rademacher).

4. **Update Parameter (Steepest Descent Stokastik):**
   $$ 
   \theta_{k+1} = \theta_k - a_k \hat{\mathbf{g}}_k(\theta_k)
   $$ 

### 5.2 Kondisi Step Size untuk Konvergensi (Spall, 1992)

Agar algoritma konvergen (dalam arti kuadratik rata-rata atau hampir pasti), barisan $a_k$  dan $c_k$  harus memenuhi kondisi regulasi standar dalam Stochastic Approximation (SA).

**Kondisi SA-1 (Step Size Iterasi):**
$$ 
\sum_{k=0}^\infty a_k = \infty, \quad \sum_{k=0}^\infty a_k^2 < \infty
$$ 
*Interpretasi:* $a_k \to 0$  tetapi tidak terlalu cepat (agar bisa mencapai optimum), dan variansi teredam ($\sum a_k^2 < \infty$ ).

**Kondisi SA-2 (Lebar Perturbasi):**
$$ 
\sum_{k=0}^\infty a_k c_k < \infty, \quad \sum_{k=0}^\infty \left( \frac{a_k}{c_k} \right)^2 < \infty
$$ 
*Interpretasi:* $c_k \to 0$  lebih lambat dari $a_k$ , sehingga bias ($\propto c_k^2$ ) mengecil cukup cepat relatif terhadap learning rate.

**Kondisi SA-3 (Eksistensi Momen):**
Seperti yang sudah kita buktikan di Tahap 4, kita membutuhkan:
$$ 
E[|\Delta_{k,i}|^{-2}] < \infty \quad \text{dan} \quad E[\Delta_{k,i}^4] < \infty
$$ 
Rademacher memenuhi ini dengan sempurna ($\kappa = 1, E[\Delta^4] = 1$ ).

### 5.3 Analisis Konvergensi Kuadratik Rata-rata (Mean-Square Convergence)

**Teorema 5.3.1 (Konvergensi SPSA):**
*Misalkan $L(\theta)$  adalah fungsi strictly convex dengan Hessian terbatas dan definit positif di sekitar minimum unik $\theta^*$ . Jika barisan $a_k, c_k$  memenuhi kondisi SA-1 dan SA-2, dan perturbasi $\mathbf{\Delta}_k$  adalah Rademacher, maka:*
$$ 
\lim_{k \to \infty} E\left[ \| \theta_k - \theta^* \|^2 \right] = 0
$$ 

**Sketsa Bukti (Menggunakan Sifat Rademacher):**

Kita definisikan error parameter: $\tilde{\theta}_k = \theta_k - \theta^*$ .

**Langkah 1: Dekomposisi Error Rekursif**
Dari update rule:
$$ 
\tilde{\theta}_{k+1} = \tilde{\theta}_k - a_k \hat{\mathbf{g}}_k(\theta_k)
$$ 

**Langkah 2: Ekspektasi Kuadrat Norm**
Ambil norma kuadrat dan ekspektasi kondisional pada $\theta_k$ :
$$ 
E[ \| \tilde{\theta}_{k+1} \|^2 | \theta_k ] = \| \tilde{\theta}_k \|^2 - 2a_k \tilde{\theta}_k^T E[ \hat{\mathbf{g}}_k | \theta_k ] + a_k^2 E[ \| \hat{\mathbf{g}}_k \|^2 | \theta_k ]
$$ 

**Langkah 3: Substitusi Properti SPSA**
Dari Tahap 4, kita tahu:
1.  **Ekspektasi (Bias):** $E[ \hat{\mathbf{g}}_k | \theta_k ] = \nabla L(\theta_k) + \mathbf{b}_k$ , di mana $\| \mathbf{b}_k \| = O(c_k^2)$ .
2.  **Momen Kedua (Variansi + Bias^2):**
    $$ 
    E[ \| \hat{\mathbf{g}}_k \|^2 | \theta_k ] = \| \nabla L(\theta_k) \|^2 + \text{tr}(\text{Cov}(\hat{\mathbf{g}}_k)) + O(c_k^4)
    $$ 
    Dari hasil Tahap 4, $\text{tr}(\text{Cov}(\hat{\mathbf{g}}_k)) = \kappa (p-1) \| \nabla L(\theta_k) \|^2 + \text{suku Hessian}$ .
    Untuk Rademacher, $\kappa = 1$  dan suku Hessian minimal karena $E[\Delta^4] = 1$ .

**Langkah 4: Pertidaksamaan Rekursif**
Karena $L$  strictly convex, $\tilde{\theta}_k^T \nabla L(\theta_k) \geq \lambda_{\min} \| \tilde{\theta}_k \|^2$  (untuk $\theta_k$  dekat $\theta^*$ ).
Kita peroleh pertidaksamaan:
$$ 
E[ \| \tilde{\theta}_{k+1} \|^2 ] \leq (1 - 2a_k \lambda_{\min} + O(a_k^2)) E[ \| \tilde{\theta}_k \|^2 ] + O(a_k c_k^2) + O\left( \frac{a_k^2}{c_k^2} \right)
$$ 

**Langkah 5: Konvergensi**
Dengan pemilihan $a_k, c_k$  yang tepat (misal $a_k = a_0/k, c_k = c_0/k^{1/6}$ ), suku noise $O(a_k^2/c_k^2) = O(k^{-5/3})$  dan bias $O(a_k c_k^2) = O(k^{-4/3})$  keduanya summable dan menuju nol. Akibatnya, $E[ \| \tilde{\theta}_k \|^2 ] \to 0$ .

**Peran Krusial Rademacher:**
Konstanta dalam suku $O(a_k^2/c_k^2)$  berbanding lurus dengan $\kappa$  dan $E[\Delta^4]$ . Karena Rademacher meminimalkan kedua konstanta ini, **laju konvergensi praktis menjadi lebih cepat** dibandingkan jika kita menggunakan distribusi lain (seandainya distribusi lain tersebut stabil).

### 5.4 Trade-off Bias-Varians dan Pemilihan $c_k$ 

Estimator SPSA memiliki Mean Squared Error (MSE):
$$ 
\text{MSE}(\hat{\mathbf{g}}_k) = \| \text{Bias} \|^2 + \text{tr}(\text{Cov})
$$ 
$$ 
\text{MSE} \approx \underbrace{O(c_k^4)}_{\text{Bias}^2} + \underbrace{\frac{\sigma^2}{c_k^2} \cdot \text{tr}(\text{Faktor Variansi})}_{\text{Variansi}}
$$ 

**Optimasi $c_k$ :**
Jika kita minimalkan MSE terhadap $c_k$  (dengan asumsi iterasi fixed), kita dapatkan:
$$ 
\frac{d}{dc} \left( K_1 c^4 + K_2 c^{-2} \right) = 4K_1 c^3 - 2K_2 c^{-3} = 0
$$ 
$$ 
c^* = \left( \frac{K_2}{2K_1} \right)^{1/6}
$$ 
Ini menjelaskan mengapa dalam praktiknya $c_k$  menurun sangat lambat ($\gamma \approx 0.101$ , yaitu $1/6$  dalam skala asimtotik).

**Dampak Rademacher:**
Karena $K_2$  (faktor variansi) untuk Rademacher adalah yang **terkecil** di antara semua distribusi valid, nilai $c^*$  optimal untuk Rademacher bisa sedikit lebih kecil, menghasilkan bias yang lebih kecil untuk level variansi yang sama.

### 5.5 Konsentrasi Eksponensial: Peran Sifat Sub-Gaussian

Di Tahap 2, kita membuktikan bahwa Rademacher adalah sub-Gaussian dengan parameter $\sigma^2 = 1$ . Ini memiliki konsekuensi mendalam pada **teorema limit pusat** (Central Limit Theorem) untuk estimator SPSA.

**Teorema 5.5.1 (Konsentrasi Estimator SPSA):**
Untuk setiap $t > 0$ , berlaku:
$$ 
P\left( \| \hat{\mathbf{g}}_k - E[\hat{\mathbf{g}}_k] \| > t \right) \leq 2p \exp\left( - \frac{t^2 c_k^2}{2 \| \nabla L \|^2 + O(c_k)} \right)
$$ 

**Makna:**
Probabilitas estimator gradien melenceng jauh dari nilai harapannya meluruh secara **eksponensial cepat**. Ini memberikan jaminan bahwa bahkan dengan hanya **dua** evaluasi fungsi per iterasi, estimasi gradien tidak akan "meledak" secara ekstrem. Ini adalah properti yang sangat diinginkan dalam optimasi stokastik karena mencegah divergensi akibat outlier.

### 5.6 Ringkasan Akhir: Mengapa Rademacher Adalah Jantung SPSA

| Aspek Matematis | Peran dalam SPSA | Keunggulan Rademacher |
| :--- | :--- | :--- |
| **Support Diskrit** $\{-1, +1\}$  | Menghindari pembagian dengan nol ($1/\Delta$ ) | **Stabilitas Numerik Mutlak** |
| **Mean Nol** $E[\Delta]=0$  | Unbiasedness Orde Pertama | ✅ Terpenuhi |
| **Variansi Satu** $E[\Delta^2]=1$  | Skala Perturbasi Standar | ✅ Terpenuhi |
| **Momen Invers** $E[\Delta^{-2}]$  | Kontrol Variansi Orde Utama | **Minimum (=1)** |
| **Momen Keempat** $E[\Delta^4]$  | Kontrol Variansi Orde Tinggi (Kelengkungan) | **Minimum Global (=1)** |
| **Sifat Sub-Gaussian** | Konsentrasi Eksponensial Estimator | **Optimal (Parameter=1)** |

### Penutup

Kita telah menempuh perjalanan matematis yang panjang:
1. Dari **Bernoulli Umum**, kita menyaring parameter untuk mendapatkan **Distribusi Rademacher**.
2. Kita membuktikan properti **Momen Keempat Minimum** sebagai batas bawah variansi.
3. Kita membuktikan bahwa properti ini menghasilkan **estimator gradien dengan variansi minimum** dalam keluarga SPSA.
4. Kita melihat bagaimana properti ini menjamin **konvergensi dan stabilitas numerik** dalam optimasi dimensi tinggi.

Distribusi Rademacher bukanlah pilihan sembarangan; ia adalah **konsekuensi alami dari optimasi matematis** terhadap trade-off antara eksplorasi (perturbasi) dan stabilitas (variansi) dalam ruang dimensi tinggi.

Apakah ada bagian spesifik dari roadmap ini yang ingin Anda perdalam lagi, atau ada aspek lain dari SPSA yang ingin Anda tanyakan?