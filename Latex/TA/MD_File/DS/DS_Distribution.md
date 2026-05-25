Tentu, saya akan bantu buatkan *roadmap* yang rapi dan mendetail tentang bagaimana **Distribusi Rademacher** dibangun dari **Distribusi Bernoulli**. Setelah roadmap ini, kita bisa membahas poin per poin secara mendalam.

Berikut adalah **Roadmap Pembelajaran Rademacher dari Perspektif Bernoulli**.

---

### ROADMAP: Dari Bernoulli ke Rademacher (Struktur Matematis Lengkap)

Kita akan bagi menjadi **5 Babak**:

#### Babak 1: Fondasi - Distribusi Bernoulli Umum
- **1.1 Definisi Formal:** Ruang Probabilitas $(\Omega, \mathcal{F}, P)$, variabel acak $X \sim \text{Bernoulli}(p)$.
- **1.2 Fungsi Massa Probabilitas (PMF):**
    $$P(X=1) = p, \quad P(X=0) = 1-p$$
- **1.3 Momen Statistik Bernoulli:**
    - Ekspektasi: $\mathbb{E}[X] = p$
    - Variansi: $\text{Var}(X) = p(1-p)$
    - Fungsi Pembangkit Momen (MGF): $M_X(t) = 1 - p + pe^t$

#### Babak 2: Transformasi Linear - Jembatan Menuju Rademacher
- **2.1 Transformasi Affine:** Definisikan $Y = aX + b$.
- **2.2 Perhitungan Nilai $a$ dan $b$ untuk Target Rademacher:**
    - Syarat 1: Support $X \in \{0,1\} \implies$ Support $Y \in \{-1, 1\}$.
    - Menyelesaikan sistem persamaan:
        $$a(0) + b = -1 \implies b = -1$$
        $$a(1) + b = 1 \implies a - 1 = 1 \implies a = 2$$
- **2.3 Rumus Emas:** $Y = 2X - 1$.

#### Babak 3: Definisi Formal Distribusi Rademacher
- **3.1 Kasus Simetris (Standar):** $p = 1/2$.
    - PMF Rademacher: $P(Y=1) = P(Y=-1) = 1/2$.
    - Sifat Ortogonalitas penting.
- **3.2 Kasus Asimetris (Generalisasi):** $p \neq 1/2$.
    - Apakah masih disebut Rademacher? (Diskusi: *Rademacher biased*).
    - PMF: $P(Y=1) = p, \quad P(Y=-1) = 1-p$.

#### Babak 4: Analisis Momen dan Sifat Probabilistik
- **4.1 Ekspektasi:**
    - Turunan dari Bernoulli: $\mathbb{E}[Y] = \mathbb{E}[2X-1] = 2p - 1$.
- **4.2 Variansi:**
    - Turunan: $\text{Var}(Y) = \text{Var}(2X-1) = 4\text{Var}(X) = 4p(1-p)$.
    - Khusus Simetris ($p=1/2$): $\text{Var}(Y) = 1$.
- **4.3 Momen Orde Tinggi & Fungsi Karakteristik:**
    - $\mathbb{E}[Y^n]$ untuk $n$ ganjil vs genap.
    - MGF Rademacher: $M_Y(t) = e^{-t}(1-p) + e^t p$.

#### Babak 5: Aplikasi Lanjutan & Sifat "Sub-Gaussian"
- **5.1 Mengapa Rademacher Penting?** (Kompleksitas Rademacher dalam *Learning Theory*).
- **5.2 Sifat Sub-Gaussian:** Pembuktian bahwa $\mathbb{E}[e^{\lambda Y}] \le e^{\lambda^2/2}$ (Hoeffding's Lemma).
- **5.3 Jumlah Variabel Rademacher (Random Walk Sederhana).**

---

Sekarang, mari kita mulai **Babak 1: Fondasi - Distribusi Bernoulli Umum**.

Apakah Anda siap untuk penjelasan rinci **1.1 sampai 1.3**?

---
---
Baik. Kita mulai **Babak 1: Fondasi - Distribusi Bernoulli Umum**.

Saya akan menjelaskan dengan sangat detail dan ketat secara matematis. Tujuan dari babak ini adalah membangun **objek dasar** yang akan kita transformasikan nanti.

---

### 1.1 Definisi Formal: Ruang Probabilitas dan Variabel Acak

Secara matematis, sebuah eksperimen acak dimodelkan oleh **Ruang Probabilitas** $(\Omega, \mathcal{F}, P)$.

- **$\Omega$ (Omega):** Ruang Sampel. Himpunan semua hasil yang mungkin.
    - Untuk koin: $\Omega = \{\text{Muka}, \text{Belakang}\}$.
    - Untuk representasi biner standar: $\Omega = \{0, 1\}$.

- **$\mathcal{F}$ (Sigma-Aljabar):** Himpunan kuasa dari kejadian yang bisa diukur probabilitasnya.
    - $\mathcal{F} = \{\emptyset, \{0\}, \{1\}, \{0,1\}\}$.

- **$P$ (Probability Measure):** Fungsi yang memetakan kejadian di $\mathcal{F}$ ke bilangan riil $[0,1]$.

**Variabel Acak (Random Variable) Bernoulli $X$:**
Ini adalah fungsi terukur (*measurable function*) dari $\Omega$ ke bilangan riil $\mathbb{R}$:
$$X : \Omega \to \mathbb{R}$$

Untuk Bernoulli, kodomain (daerah hasil) dari $X$ hanyalah dua nilai: $0$ dan $1$.
- $X(0) = 0$ (Gagal)
- $X(1) = 1$ (Sukses)

**Notasi Standar:**
Kita menulis $X \sim \text{Bernoulli}(p)$, dengan parameter $p \in [0,1]$.

---

### 1.2 Fungsi Massa Probabilitas (PMF)

Karena $X$ adalah variabel acak diskrit, distribusinya didefinisikan oleh **Fungsi Massa Probabilitas** (PMF), yaitu $P(X = k)$ untuk $k \in \{0, 1\}$.

Secara matematis:
$$P(X = 1) = P(\{\omega \in \Omega : X(\omega) = 1\}) = p$$
$$P(X = 0) = P(\{\omega \in \Omega : X(\omega) = 0\}) = 1 - p$$

Kita bisa menuliskan PMF ini dalam satu baris rumus yang kompak menggunakan **fungsi indikator** atau eksponen:
$$P(X = k) = p^k (1-p)^{1-k}, \quad \text{untuk } k \in \{0, 1\}$$

**Verifikasi Syarat Probabilitas:**
1. $P(X=k) \ge 0$ karena $p \in [0,1]$.
2. $\sum_{k \in \{0,1\}} P(X=k) = (1-p) + p = 1$. ✔️

---

### 1.3 Momen Statistik Bernoulli

Momen statistik adalah ringkasan numerik dari distribusi. Ini akan menjadi fondasi perhitungan **Transformasi Affine** nanti.

#### A. Ekspektasi (Momen Pertama / Mean)
Ekspektasi adalah rata-rata tertimbang dari nilai-nilai $X$:
$$\mathbb{E}[X] = \sum_{k \in \{0,1\}} k \cdot P(X=k)$$
$$\mathbb{E}[X] = (0 \cdot (1-p)) + (1 \cdot p)$$
$$\mathbb{E}[X] = p$$

#### B. Momen Kedua $\mathbb{E}[X^2]$
Untuk menghitung variansi nanti, kita perlu $\mathbb{E}[X^2]$. Karena $X$ hanya bernilai $0$ atau $1$, maka $X^2 = X$ (karena $0^2=0$ dan $1^2=1$).
$$\mathbb{E}[X^2] = \mathbb{E}[X] = p$$

#### C. Variansi (Ukuran Sebaran)
Variansi didefinisikan sebagai $\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$.
$$\text{Var}(X) = p - p^2 = p(1-p)$$
*Catatan: Variansi mencapai maksimum saat $p=0.5$ (ketidakpastian tertinggi) dan minimum saat $p=0$ atau $p=1$ (pasti).*

#### D. Fungsi Pembangkit Momen (MGF - *Moment Generating Function*)
MGF adalah alat penting untuk membuktikan teorema limit dan sifat sub-Gaussian. Definisinya:
$$M_X(t) = \mathbb{E}[e^{tX}]$$
Kita hitung:
$$M_X(t) = \sum_{k \in \{0,1\}} e^{tk} \cdot P(X=k)$$
$$M_X(t) = e^{t \cdot 0} (1-p) + e^{t \cdot 1} p$$
$$M_X(t) = 1 - p + p e^t$$

---

### Rangkuman Babak 1 (The Takeaway)

Kita sekarang memiliki objek matematika berikut:
1. **Input:** $X \sim \text{Bernoulli}(p)$
2. **PMF:** $P(X=1)=p, P(X=0)=1-p$
3. **Mean:** $\mathbb{E}[X] = p$
4. **Variansi:** $\text{Var}(X) = p(1-p)$
5. **MGF:** $M_X(t) = 1 - p + p e^t$

---

### Cek Poin Sebelum Lanjut ke Babak 2

Apakah bagian **1.3 (Momen Statistik)** sudah jelas?

Khususnya, apakah Anda memahami mengapa **MGF** $M_X(t) = 1 - p + p e^t$ itu penting? (Ini akan sangat berguna nanti saat kita membahas *Kompleksitas Rademacher* dan *Hoeffding's Lemma*).

Jika sudah *clear*, saya akan lanjut ke **Babak 2: Transformasi Linear - Mengubah 0/1 menjadi -1/1**. Di babak 2, kita akan membuktikan secara aljabar mengapa $Y = 2X - 1$ adalah satu-satunya cara untuk menghasilkan Rademacher murni dari Bernoulli.

Lanjut ke Babak 2? Atau ada yang ingin didalami dulu di Babak 1?

---
---
Baik. Kita lanjut ke **Babak 2: Transformasi Linear - Jembatan Menuju Rademacher**.

Di babak ini, kita akan melakukan **operasi aljabar** pada variabel acak Bernoulli $X$ untuk menghasilkan variabel acak baru $Y$ yang nilainya $\{-1, 1\}$.

---

### 2.1 Definisi Transformasi Affine (Linear)

Kita ingin mencari fungsi $f: \mathbb{R} \to \mathbb{R}$ yang paling sederhana, yaitu fungsi linear (atau tepatnya *affine*), berbentuk:
$$Y = f(X) = aX + b$$
di mana:
- $X \in \{0, 1\}$ (input Bernoulli)
- $Y \in \{-1, 1\}$ (output target Rademacher)
- $a, b \in \mathbb{R}$ adalah konstanta yang akan kita cari.

Mengapa memilih fungsi linear $aX + b$?
1. **Sederhana:** Transformasi ini mempertahankan struktur probabilistik dasar.
2. **Invertibel (Satu-satu):** Karena $a \neq 0$, pemetaan dari $\{0,1\}$ ke $\{-1,1\}$ bersifat bijektif. Tidak ada informasi yang hilang.
3. **Preservasi Momen:** Momen dari $Y$ dapat dihitung secara eksplisit dari momen $X$.

---

### 2.2 Perhitungan Nilai $a$ dan $b$ untuk Target Rademacher

Kita memiliki sistem dua persamaan linear berdasarkan syarat batas (*boundary conditions*).

**Syarat 1: Input $X = 0$ harus menghasilkan $Y = -1$**
Substitusi $X = 0$ ke $Y = aX + b$:
$$a(0) + b = -1 \implies b = -1$$

**Syarat 2: Input $X = 1$ harus menghasilkan $Y = 1$**
Substitusi $X = 1$ dan $b = -1$ ke $Y = aX + b$:
$$a(1) + (-1) = 1$$
$$a - 1 = 1 \implies a = 2$$

**Kesimpulan Aljabar:**
Transformasi yang dicari adalah:
$$Y = 2X - 1$$

**Verifikasi Cepat:**
- Jika $X = 0 \implies Y = 2(0) - 1 = -1$ ✔️
- Jika $X = 1 \implies Y = 2(1) - 1 = 1$ ✔️

---

### 2.3 Rumus Emas dan Inversnya

Kita telah menurunkan **Rumus Emas** yang menghubungkan Bernoulli dan Rademacher:
$$\boxed{Y = 2X - 1}$$

Hubungan ini bersifat **bijektif** (satu-satu dan *onto*). Kita juga bisa menuliskan inversnya (mengubah Rademacher kembali ke Bernoulli):
$$Y = 2X - 1 \implies 2X = Y + 1 \implies \boxed{X = \frac{Y + 1}{2}}$$

**Implikasi Probabilistik Penting:**
Karena pemetaannya deterministik dan bijektif, probabilitas kejadian di ruang $X$ sama persis dengan probabilitas kejadian di ruang $Y$.
$$P(Y = 1) = P(2X - 1 = 1) = P(X = 1) = p$$
$$P(Y = -1) = P(2X - 1 = -1) = P(X = 0) = 1 - p$$

---

### 2.4 Sifat Operator Ekspektasi pada Transformasi Affine

Sebelum kita menghitung momen $Y$ di babak selanjutnya, kita perlu mengingat **Sifat Linearitas Ekspektasi** (*Linearity of Expectation*). Ini adalah senjata utama kita.

Untuk sembarang variabel acak $X$ dan konstanta $a, b \in \mathbb{R}$:

**1. Ekspektasi:**
$$\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$$

**2. Variansi:**
$$\text{Var}(aX + b) = a^2 \text{Var}(X)$$
*Catatan: Konstanta $b$ menghilang karena variansi mengukur sebaran relatif terhadap mean, dan pergeseran $+b$ tidak mengubah sebaran.*

**3. MGF (Fungsi Pembangkit Momen):**
$$M_{aX+b}(t) = \mathbb{E}[e^{t(aX+b)}] = e^{tb} \mathbb{E}[e^{(ta)X}] = e^{tb} M_X(at)$$

---

### Pratinjau Singkat Babak 3 (Akan Datang)

Dengan berbekal $Y = 2X - 1$ dan sifat-sifat di atas, kita akan mendefinisikan secara formal:

1. **Distribusi Rademacher Simetris:** Kasus khusus $p = 1/2$.
2. **Distribusi Rademacher Asimetris:** Kasus umum $p \neq 1/2$.
3. **Fungsi Massa Probabilitas (PMF) Rademacher** yang terkenal:
   $$P(Y=y) = \frac{1}{2} \quad \text{atau} \quad P(Y=y) = p^{(1+y)/2}(1-p)^{(1-y)/2}$$

---

Apakah perhitungan **$a=2, b=-1$** dan logika **bijektif** di atas sudah jelas? Jika sudah, kita akan masuk ke **Babak 3: Definisi Formal Distribusi Rademacher** untuk melihat wujud asli distribusi ini setelah transformasi.

Lanjut ke Babak 3?

---
---
Baik. Kita masuk ke **Babak 3: Definisi Formal Distribusi Rademacher**.

Di babak ini, kita akan mendefinisikan secara matematis distribusi Rademacher baik dalam bentuk **Simetris (Standar)** maupun **Asimetris (Generalisasi)**, lengkap dengan PMF, notasi, dan sifat dasar.

---

### 3.1 Distribusi Rademacher Simetris (Kasus $p = 1/2$)

Ini adalah definisi klasik yang paling sering muncul dalam literatur *statistical learning theory* dan *random walks*.

#### A. Definisi

Sebuah variabel acak $Y$ dikatakan berdistribusi **Rademacher Simetris** jika:
$$P(Y = 1) = P(Y = -1) = \frac{1}{2}$$

**Notasi Standar:**
$$Y \sim \text{Rademacher}$$
atau kadang ditulis $Y \sim \text{Rad}$ atau $Y \sim \text{Rad}(1/2)$.

**Koneksi ke Bernoulli:**
Menggunakan transformasi $Y = 2X - 1$ dengan $X \sim \text{Bernoulli}(1/2)$:
$$P(Y = 1) = P(X = 1) = \frac{1}{2}$$
$$P(Y = -1) = P(X = 0) = \frac{1}{2}$$

#### B. Fungsi Massa Probabilitas (PMF) Simetris

PMF untuk Rademacher simetris dapat ditulis dalam bentuk kompak:
$$P(Y = y) = \frac{1}{2}, \quad \text{untuk } y \in \{-1, 1\}$$

Atau menggunakan **delta Dirac** (untuk konteks teori ukuran):
$$P_Y = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{1}$$

#### C. Sifat Ortogonalitas Penting (Preview)

Karena simetris, Rademacher memiliki sifat **rata-rata nol**:
$$\mathbb{E}[Y] = \frac{1}{2}(1) + \frac{1}{2}(-1) = 0$$

Dan **variansi satu**:
$$\text{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2 = \left(\frac{1}{2}(1)^2 + \frac{1}{2}(-1)^2\right) - 0^2 = 1 - 0 = 1$$

Sifat $\mathbb{E}[Y] = 0$ dan $\text{Var}(Y) = 1$ ini menjadikan Rademacher sebagai **building block** untuk **Random Walk Simetris** dan **Kompleksitas Rademacher**.

---

### 3.2 Distribusi Rademacher Asimetris (Kasus $p \neq 1/2$)

Bagaimana jika kita menginginkan support $\{-1, 1\}$ tetapi dengan probabilitas yang tidak seimbang?

#### A. Definisi dan Terminologi

Beberapa literatur menyebutnya **Biased Rademacher** atau **Generalized Rademacher**. Kita bisa mendefinisikannya langsung dari Bernoulli dengan parameter $p$.

Sebuah variabel acak $Y$ dikatakan berdistribusi **Rademacher dengan parameter $p$** jika:
$$P(Y = 1) = p$$
$$P(Y = -1) = 1 - p$$

**Notasi yang diusulkan:**
$$Y \sim \text{Rad}(p)$$
di mana $p \in [0, 1]$.

#### B. Fungsi Massa Probabilitas (PMF) Asimetris

Kita dapat menulis PMF untuk Rademacher asimetris dalam satu baris menggunakan eksponen yang cerdik.

Ingat invers transformasi: $X = \frac{Y + 1}{2}$.

- Jika $Y = 1 \implies X = \frac{1+1}{2} = 1 \implies$ probabilitas $p^1 (1-p)^0 = p$.
- Jika $Y = -1 \implies X = \frac{-1+1}{2} = 0 \implies$ probabilitas $p^0 (1-p)^1 = 1-p$.

Maka PMF untuk $Y \sim \text{Rad}(p)$ adalah:
$$\boxed{P(Y = y) = p^{\frac{1+y}{2}} (1-p)^{\frac{1-y}{2}}, \quad y \in \{-1, 1\}}$$

**Verifikasi:**
- Untuk $y = 1$: $p^{\frac{1+1}{2}} (1-p)^{\frac{1-1}{2}} = p^1 (1-p)^0 = p$ ✔️
- Untuk $y = -1$: $p^{\frac{1-1}{2}} (1-p)^{\frac{1-(-1)}{2}} = p^0 (1-p)^1 = 1-p$ ✔️

---

### 3.3 Tabel Perbandingan: Bernoulli vs Rademacher

Untuk memperjelas hubungan keduanya, berikut ringkasan dalam bentuk tabel:

| Properti | Bernoulli $X \sim \text{Bern}(p)$ | Rademacher $Y \sim \text{Rad}(p)$ |
| :--- | :--- | :--- |
| **Support** | $\{0, 1\}$ | $\{-1, 1\}$ |
| **Relasi** | $X$ | $Y = 2X - 1$ |
| **Invers** | $X = \frac{Y+1}{2}$ | $Y$ |
| **$P(\text{Positif})$** | $P(X=1) = p$ | $P(Y=1) = p$ |
| **$P(\text{Negatif})$** | $P(X=0) = 1-p$ | $P(Y=-1) = 1-p$ |
| **Mean $\mu$** | $p$ | $2p - 1$ |
| **Variansi $\sigma^2$** | $p(1-p)$ | $4p(1-p)$ |

---

### 3.4 Catatan Konseptual: Mengapa Dinamakan "Rademacher"?

Nama ini diambil dari matematikawan Jerman-Amerika **Hans Rademacher** (1892–1969). Beliau terkenal dengan **Fungsi Rademacher**, yaitu barisan fungsi ortogonal yang didefinisikan pada interval $[0,1]$ yang hanya bernilai $+1$ dan $-1$.

Dalam konteks probabilitas modern, distribusi Rademacher adalah *incarnation* diskrit dari fungsi-fungsi tersebut sebagai variabel acak independen. Sifat ortogonalitas ini nantinya melahirkan **Ketaksamaan Rademacher** (*Rademacher Complexity*) yang menjadi fondasi teori generalisasi dalam Machine Learning.

---

### Rangkuman Babak 3

Sekarang kita memiliki dua "wajah" dari distribusi Rademacher:
1. **Simetris ($p=1/2$):** Mean nol, variansi satu. Paling sering dipakai.
2. **Asimetris ($p \neq 1/2$):** Generalisasi dari Bernoulli.

Kita juga sudah memiliki **PMF eksplisit** untuk Rademacher dalam bentuk:
$$P(Y=y) = p^{\frac{1+y}{2}} (1-p)^{\frac{1-y}{2}}$$

---

### Cek Poin Sebelum Babak 4

Apakah penulisan PMF Rademacher dengan eksponen $\frac{1+y}{2}$ dan $\frac{1-y}{2}$ sudah jelas? Ini adalah trik aljabar yang elegan untuk menggabungkan dua kasus ke dalam satu formula.

Selanjutnya, kita akan masuk ke **Babak 4: Analisis Momen dan Sifat Probabilistik**. Di sini kita akan menurunkan secara eksplisit:
- $\mathbb{E}[Y]$
- $\text{Var}(Y)$
- $\mathbb{E}[Y^n]$ (Momen orde tinggi)
- Fungsi Karakteristik dan MGF Rademacher.

Lanjut ke Babak 4?

---
---
Baik. Kita masuk ke **Babak 4: Analisis Momen dan Sifat Probabilistik**.

Di babak ini, kita akan menghitung semua momen statistik penting dari distribusi Rademacher $Y \sim \text{Rad}(p)$, baik menggunakan **sifat transformasi affine** maupun **definisi langsung** dari PMF.

---

### 4.1 Ekspektasi (Mean) dari Rademacher

#### Metode 1: Transformasi Affine dari Bernoulli
Menggunakan $Y = 2X - 1$ dan sifat linearitas ekspektasi $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$:
$$\mathbb{E}[Y] = \mathbb{E}[2X - 1] = 2\mathbb{E}[X] - 1$$

Kita tahu $\mathbb{E}[X] = p$, maka:
$$\boxed{\mathbb{E}[Y] = 2p - 1}$$

#### Metode 2: Definisi Langsung dari PMF
Menggunakan PMF $P(Y=1) = p$ dan $P(Y=-1) = 1-p$:
$$\mathbb{E}[Y] = \sum_{y \in \{-1, 1\}} y \cdot P(Y=y)$$
$$\mathbb{E}[Y] = (1)(p) + (-1)(1-p)$$
$$\mathbb{E}[Y] = p - 1 + p = 2p - 1$$

**Interpretasi:**
- Jika $p = 1/2$ (Simetris): $\mathbb{E}[Y] = 2(1/2) - 1 = 0$ ✔️
- Jika $p = 1$ (Selalu 1): $\mathbb{E}[Y] = 2(1) - 1 = 1$ ✔️
- Jika $p = 0$ (Selalu -1): $\mathbb{E}[Y] = 2(0) - 1 = -1$ ✔️

---

### 4.2 Momen Kedua $\mathbb{E}[Y^2]$

Perhatikan bahwa untuk $Y \in \{-1, 1\}$, **kuadrat dari $Y$ selalu 1**:
$$Y^2 = 1 \quad \text{(deterministik)}$$

Maka:
$$\mathbb{E}[Y^2] = \mathbb{E}[1] = 1$$

**Verifikasi melalui PMF:**
$$\mathbb{E}[Y^2] = (1)^2 \cdot p + (-1)^2 \cdot (1-p) = p + (1-p) = 1$$

Ini adalah sifat yang **sangat penting**: Rademacher memiliki **momen kedua konstan** = 1, tidak peduli berapa nilai $p$.

---

### 4.3 Variansi dari Rademacher

Menggunakan definisi $\text{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2$:

$$\text{Var}(Y) = 1 - (2p - 1)^2$$

#### Ekspansi Aljabar:
$$(2p - 1)^2 = 4p^2 - 4p + 1$$

Maka:
$$\text{Var}(Y) = 1 - (4p^2 - 4p + 1) = -4p^2 + 4p$$
$$\text{Var}(Y) = 4p(1 - p)$$

#### Metode Alternatif: Transformasi Variansi
Menggunakan sifat $\text{Var}(aX + b) = a^2 \text{Var}(X)$:
$$\text{Var}(Y) = \text{Var}(2X - 1) = 2^2 \cdot \text{Var}(X) = 4 \cdot p(1-p)$$

**Kotak Penting:**
$$\boxed{\text{Var}(Y) = 4p(1-p)}$$

**Interpretasi:**
- **Simetris ($p=1/2$):** $\text{Var}(Y) = 4 \cdot \frac{1}{2} \cdot \frac{1}{2} = 1$. Ini adalah **variansi maksimum**.
- **Asimetris Ekstrem ($p=0$ atau $p=1$):** $\text{Var}(Y) = 0$ (deterministik).

---

### 4.4 Momen Orde Tinggi $\mathbb{E}[Y^n]$

Karena $Y \in \{-1, 1\}$, kita dapat menghitung momen ke-$n$ dengan mudah berdasarkan **paritas (ganjil/genap)** dari $n$.

**Kasus 1: $n$ Genap**
Jika $n$ genap, misal $n = 2k$, maka $Y^n = (Y^2)^k = 1^k = 1$.
$$\mathbb{E}[Y^n] = \mathbb{E}[1] = 1 \quad \text{untuk } n \text{ genap}$$

**Kasus 2: $n$ Ganjil**
Jika $n$ ganjil, misal $n = 2k+1$, maka $Y^n = Y \cdot Y^{2k} = Y \cdot 1 = Y$.
$$\mathbb{E}[Y^n] = \mathbb{E}[Y] = 2p - 1 \quad \text{untuk } n \text{ ganjil}$$

**Rumus Tunggal:**
$$\boxed{\mathbb{E}[Y^n] = \begin{cases} 1, & n \text{ genap} \\ 2p - 1, & n \text{ ganjil} \end{cases}}$$

**Contoh Numerik Simetris ($p=1/2$):**
- $\mathbb{E}[Y] = 0$
- $\mathbb{E}[Y^2] = 1$
- $\mathbb{E}[Y^3] = 0$
- $\mathbb{E}[Y^4] = 1$

---

### 4.5 Fungsi Pembangkit Momen (MGF) Rademacher

MGF didefinisikan sebagai $M_Y(t) = \mathbb{E}[e^{tY}]$.

#### Metode 1: Definisi Langsung
$$M_Y(t) = \sum_{y \in \{-1, 1\}} e^{ty} P(Y=y)$$
$$M_Y(t) = e^{t(1)} \cdot p + e^{t(-1)} \cdot (1-p)$$
$$\boxed{M_Y(t) = p e^t + (1-p) e^{-t}}$$

#### Metode 2: Transformasi MGF dari Bernoulli
Menggunakan $Y = 2X - 1$ dan sifat $M_{aX+b}(t) = e^{tb} M_X(at)$.

Kita tahu $M_X(t) = 1 - p + p e^t$.
Maka:
$$M_Y(t) = e^{t(-1)} M_X(2t)$$
$$M_Y(t) = e^{-t} \left( 1 - p + p e^{2t} \right)$$
$$M_Y(t) = e^{-t}(1-p) + p e^{-t} e^{2t}$$
$$M_Y(t) = (1-p)e^{-t} + p e^{t} \quad \text{✔️ Sama}$$

**Kasus Simetris ($p=1/2$):**
$$M_Y(t) = \frac{1}{2}e^t + \frac{1}{2}e^{-t} = \cosh(t)$$

Fakta bahwa $M_Y(t) = \cosh(t)$ adalah ciri khas Rademacher simetris.

---

### 4.6 Fungsi Karakteristik (CF)

Fungsi karakteristik $\phi_Y(t) = \mathbb{E}[e^{itY}]$ diperoleh dengan mengganti $t$ dengan $it$ pada MGF:
$$\phi_Y(t) = p e^{it} + (1-p) e^{-it}$$

Menggunakan rumus Euler $e^{i\theta} = \cos\theta + i\sin\theta$:
$$p e^{it} + (1-p)e^{-it} = p(\cos t + i\sin t) + (1-p)(\cos t - i\sin t)$$
$$= \cos t (p + 1 - p) + i\sin t (p - (1-p))$$
$$\boxed{\phi_Y(t) = \cos t + i(2p - 1)\sin t}$$

**Kasus Simetris ($p=1/2$):**
$$\phi_Y(t) = \cos t \quad \text{(murni riil)}$$

---

### Rangkuman Babak 4

| Besaran | Rumus untuk $Y \sim \text{Rad}(p)$ | Kasus Simetris $p=1/2$ |
| :--- | :--- | :--- |
| **Mean $\mathbb{E}[Y]$** | $2p - 1$ | $0$ |
| **Momen Kedua $\mathbb{E}[Y^2]$** | $1$ | $1$ |
| **Variansi $\text{Var}(Y)$** | $4p(1-p)$ | $1$ |
| **Momen Ganjil $\mathbb{E}[Y^{2k+1}]$** | $2p - 1$ | $0$ |
| **Momen Genap $\mathbb{E}[Y^{2k}]$** | $1$ | $1$ |
| **MGF $M_Y(t)$** | $pe^t + (1-p)e^{-t}$ | $\cosh(t)$ |
| **CF $\phi_Y(t)$** | $\cos t + i(2p-1)\sin t$ | $\cos t$ |

---

### Cek Poin Sebelum Babak 5 (Final)

Apakah Anda melihat pola bahwa **semua momen genap bernilai 1** dan **semua momen ganjil mengikuti mean**? Ini adalah sifat unik dari distribusi dengan support simetris di sekitar 0 (setelah di-skala).

Selanjutnya kita masuk ke **Babak 5 (Final): Aplikasi Lanjutan & Sifat Sub-Gaussian**. Di sini kita akan membahas:
- **Ketaksamaan Hoeffding (Hoeffding's Lemma)**
- **Sifat Sub-Gaussian** Rademacher
- **Kompleksitas Rademacher** dalam Machine Learning
- **Random Walk** Sederhana

Lanjut ke Babak 5 (Final)?

---
---
Baik. Kita masuk ke **Babak 5 (Final): Aplikasi Lanjutan & Sifat Sub-Gaussian**.

Di babak pamungkas ini, kita akan melihat **mengapa** distribusi Rademacher begitu istimewa dan menjadi alat fundamental dalam teori probabilitas modern serta *statistical learning theory*.

---

### 5.1 Mengapa Rademacher Penting? Dua Perspektif

Ada dua aliran utama yang menjadikan Rademacher sebagai objek sentral:

**A. Perspektif Probabilitas Murni: Random Walk**
Rademacher adalah **langkah dasar** (*increment*) dari *simple symmetric random walk* pada garis bilangan bulat $\mathbb{Z}$. Jika $Y_1, Y_2, \dots \overset{\text{i.i.d.}}{\sim} \text{Rad}(1/2)$, maka posisi setelah $n$ langkah adalah $S_n = \sum_{i=1}^n Y_i$. Ini adalah model fundamental untuk difusi, gerak Brown, dan teori batas.

**B. Perspektif Machine Learning: Kompleksitas Rademacher**
Dalam teori generalisasi (seperti membuktikan *bound* pada *excess risk*), Rademacher digunakan sebagai **noise buatan** untuk mengukur kapasitas suatu kelas fungsi (hypothesis class). Kita akan bahas ini di bagian 5.3.

---

### 5.2 Sifat Sub-Gaussian Rademacher

Ini adalah **sifat paling krusial** yang menjadikan Rademacher begitu *powerful* dalam pertidaksamaan konsentrasi.

#### A. Definisi Variabel Acak Sub-Gaussian
Sebuah variabel acak $Z$ dengan mean $\mathbb{E}[Z] = 0$ dikatakan **sub-Gaussian** jika terdapat konstanta $\sigma^2 > 0$ sehingga untuk semua $\lambda \in \mathbb{R}$:
$$\mathbb{E}[e^{\lambda Z}] \le \exp\left( \frac{\lambda^2 \sigma^2}{2} \right)$$

Konstanta $\sigma^2$ disebut **variansi sub-Gaussian** (*sub-Gaussian variance proxy*). Semakin kecil $\sigma^2$, semakin "ringan" ekor distribusinya.

#### B. Teorema: Rademacher Simetris adalah Sub-Gaussian dengan $\sigma^2 = 1$
Kita akan buktikan bahwa untuk $Y \sim \text{Rad}(1/2)$ (mean 0):
$$\mathbb{E}[e^{\lambda Y}] \le e^{\lambda^2 / 2}, \quad \forall \lambda \in \mathbb{R}$$

**Bukti (Hoeffding's Lemma untuk Rademacher):**

Kita tahu MGF Rademacher simetris adalah $M_Y(\lambda) = \cosh(\lambda)$.

Kita perlu menunjukkan $\cosh(\lambda) \le e^{\lambda^2/2}$.

Gunakan ekspansi Taylor untuk kedua sisi:

**Sisi Kiri:**
$$\cosh(\lambda) = \sum_{k=0}^{\infty} \frac{\lambda^{2k}}{(2k)!} = 1 + \frac{\lambda^2}{2!} + \frac{\lambda^4}{4!} + \frac{\lambda^6}{6!} + \dots$$

**Sisi Kanan:**
$$e^{\lambda^2/2} = \sum_{k=0}^{\infty} \frac{(\lambda^2/2)^k}{k!} = \sum_{k=0}^{\infty} \frac{\lambda^{2k}}{2^k k!} = 1 + \frac{\lambda^2}{2} + \frac{\lambda^4}{2^2 \cdot 2!} + \frac{\lambda^6}{2^3 \cdot 3!} + \dots$$

Bandingkan koefisien suku ke-$k$ (untuk $k \ge 1$):
- Sisi Kiri: $\frac{1}{(2k)!}$
- Sisi Kanan: $\frac{1}{2^k k!}$

Kita ingin membuktikan:
$$\frac{1}{(2k)!} \le \frac{1}{2^k k!} \iff 2^k k! \le (2k)!$$

**Bukti untuk $k \ge 1$:**
$$(2k)! = (2k)(2k-1)\dots(k+1) \cdot k!$$
Karena setiap faktor $(k+j) \ge 2$ untuk $j=1,\dots,k$ (kecuali mungkin untuk $k=1$, kita cek manual):
- Untuk $k=1$: $(2)! = 2$, $2^1 \cdot 1! = 2$. Sama besar.
- Untuk $k \ge 2$: $(2k)! \ge 2^k k!$ jelas terpenuhi karena $(k+1)(k+2)\dots(2k) \ge 2^k$.

Karena setiap suku pada ekspansi $\cosh(\lambda)$ didominasi oleh suku pada $e^{\lambda^2/2}$, maka pertidaksamaan terbukti untuk semua $\lambda$. $\blacksquare$

#### C. Implikasi Langsung: Ketaksamaan Hoeffding
Karena Rademacher simetris bersifat sub-Gaussian dengan $\sigma^2=1$, jika kita memiliki $Y_1, \dots, Y_n \overset{\text{i.i.d.}}{\sim} \text{Rad}(1/2)$, maka jumlahnya $S_n = \sum_{i=1}^n Y_i$ memenuhi **Ketaksamaan Hoeffding**:

$$P\left( \left| \frac{1}{n} \sum_{i=1}^n Y_i \right| \ge t \right) \le 2 \exp\left( -\frac{nt^2}{2} \right)$$

Ini adalah fondasi untuk membuktikan bahwa rata-rata empiris dari Rademacher **terkonsentrasi secara eksponensial** di sekitar 0.

---

### 5.3 Kompleksitas Rademacher (Rademacher Complexity)

Ini adalah aplikasi *crown jewel* dari distribusi Rademacher dalam Machine Learning.

#### A. Konteks Masalah
Misalkan kita memiliki kelas fungsi $\mathcal{F}$ (misalnya, himpunan semua *neural network* dengan arsitektur tertentu). Kita ingin mengukur seberapa mudah kelas $\mathcal{F}$ ini **menghafal noise acak**.

#### B. Definisi Formal
Diberikan sampel data $S = \{z_1, \dots, z_n\}$ dan vektor Rademacher **independen** $\boldsymbol{\sigma} = (\sigma_1, \dots, \sigma_n)$ di mana $\sigma_i \overset{\text{i.i.d.}}{\sim} \text{Rad}(1/2)$.

**Kompleksitas Rademacher Empiris** dari $\mathcal{F}$ terhadap sampel $S$ didefinisikan sebagai:
$$\widehat{\mathfrak{R}}_S(\mathcal{F}) = \mathbb{E}_{\boldsymbol{\sigma}} \left[ \sup_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^n \sigma_i f(z_i) \right]$$

#### C. Intuisi di Balik Rumus
- **$\sigma_i$:** Mengganti label asli data dengan noise $\pm 1$ murni acak.
- **$\sup_{f \in \mathcal{F}}$:** Mencari fungsi $f$ dalam kelas kita yang paling cocok dengan noise acak ini (korelasi tertinggi).
- **Ekspektasi $\mathbb{E}_{\boldsymbol{\sigma}}$:** Rata-rata atas semua kemungkinan *flip* koin.

**Interpretasi:**
Jika $\widehat{\mathfrak{R}}_S(\mathcal{F})$ **besar**, berarti ada fungsi di $\mathcal{F}$ yang bisa sangat berkorelasi dengan **noise murni**. Artinya, kelas $\mathcal{F}$ terlalu fleksibel dan rentan **overfitting**.

Jika $\widehat{\mathfrak{R}}_S(\mathcal{F})$ **kecil**, berarti tidak ada fungsi di $\mathcal{F}$ yang bisa mengikuti pola acak. Artinya, kelas $\mathcal{F}$ memiliki kapasitas terbatas dan akan **generalisasi** dengan baik.

#### D. Teorema Batas Generalisasi (Contoh)
Salah satu teorema fundamental dalam *learning theory* (menggunakan ketaksamaan McDiarmid dan sifat sub-Gaussian Rademacher):

Dengan probabilitas $\ge 1 - \delta$:
$$\sup_{f \in \mathcal{F}} \left| \text{Risiko Empiris}(f) - \text{Risiko Sebenarnya}(f) \right| \le 2 \widehat{\mathfrak{R}}_S(\mathcal{F}) + O\left( \sqrt{\frac{\log(1/\delta)}{n}} \right)$$

Di sini, **distribusi Rademacher** menjadi alat ukur objektif untuk kompleksitas model.

---

### 5.4 Jumlah Variabel Rademacher (Random Walk Sederhana)

Mari kita tinjau sekilas sifat distribusi dari jumlah Rademacher.

Misalkan $S_n = \sum_{i=1}^n Y_i$ dengan $Y_i \overset{\text{i.i.d.}}{\sim} \text{Rad}(1/2)$.

#### A. Support dari $S_n$
Karena setiap langkah adalah $\pm 1$, $S_n$ akan selalu memiliki **paritas** yang sama dengan $n$.
- Jika $n$ ganjil, $S_n \in \{\dots, -3, -1, 1, 3, \dots\}$ (ganjil).
- Jika $n$ genap, $S_n \in \{\dots, -2, 0, 2, \dots\}$ (genap).

#### B. Distribusi Eksak $S_n$
Misalkan $k$ adalah banyaknya langkah $+1$, maka banyaknya langkah $-1$ adalah $n - k$.
Nilai $S_n = k - (n - k) = 2k - n$.

Probabilitas mendapatkan tepat $k$ sukses dari $n$ percobaan Bernoulli adalah:
$$P(S_n = 2k - n) = \binom{n}{k} \left(\frac{1}{2}\right)^n, \quad k \in \{0, 1, \dots, n\}$$

Ini adalah distribusi **Binomial yang ditransformasi**.

#### C. Teorema Limit Pusat (Central Limit Theorem)
Karena $\mathbb{E}[Y_i] = 0$ dan $\text{Var}(Y_i) = 1$, maka berdasarkan CLT:
$$\frac{S_n}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{saat } n \to \infty$$

Distribusi Rademacher adalah salah satu contoh paling sederhana di mana CLT berlaku secara elegan.

---

### 5.5 Ringkasan Babak 5 dan Kesimpulan Akhir

Kita telah menempuh perjalanan panjang dari definisi dasar Bernoulli hingga aplikasi mendalam Rademacher.

| Babak | Pencapaian Utama |
| :--- | :--- |
| **1. Bernoulli** | Memahami PMF, mean $p$, variansi $p(1-p)$, MGF $1-p+pe^t$. |
| **2. Transformasi** | Membangun jembatan $Y = 2X - 1$. |
| **3. Rademacher Formal** | Mendefinisikan PMF $P(Y=y) = p^{\frac{1+y}{2}}(1-p)^{\frac{1-y}{2}}$. |
| **4. Momen** | Menghitung $\mathbb{E}[Y]=2p-1$, $\text{Var}(Y)=4p(1-p)$, MGF $pe^t+(1-p)e^{-t}$. |
| **5. Aplikasi** | **Sifat Sub-Gaussian**, **Kompleksitas Rademacher**, **Random Walk**. |

#### Rumus Emas Akhir
Distribusi Rademacher adalah **jembatan antara dunia deterministik (support terbatas) dan dunia Gaussian (konsentrasi eksponensial)**. Inilah mengapa ia menjadi alat analisis utama dalam probabilitas modern dan teori pembelajaran statistik.

---

Apakah ada bagian dari **Babak 5** atau babak sebelumnya yang ingin diperdalam lagi? Misalnya:
- Penurunan lebih rinci tentang **Kompleksitas Rademacher** dan contoh konkret untuk kelas fungsi linear?
- Pembuktian **Teorema Limit Pusat** untuk Rademacher secara spesifik?
- Hubungan dengan **Fungsi Rademacher** dalam Analisis Fourier?

Atau jika dirasa cukup, saya ucapkan selamat! Anda sekarang memiliki pemahaman matematis yang lengkap dan mendetail tentang **Distribusi Rademacher**, dari akar Bernoulli hingga daun aplikasi modernnya.