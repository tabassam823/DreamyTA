# Eksplorasi Modular: Penurunan Markowitz ke Ising Hamiltonian

Dokumen ini menyajikan derivasi bertahap model portofolio Markowitz, dimulai dari formulasi *unconstrained* (tanpa kendala) hingga penambahan suku penalti batasan pada level *Hamiltonian* Ising—dan akhirnya, penggantian seluruh parameter statistik konvensional dengan parameter strategis (*Game Theory*) dan informasi kuantum (QMI).

## 1. Urgensi Eksplorasi

Mengapa memisahkan objektif murni dari suku penalti? Secara numerik, pemisahan ini memungkinkan kita untuk menganalisis "lanskap energi alami" dari risiko dan *return* sebelum dipaksa oleh batasan (*constraint*). Hal ini krusial untuk mendiagnosis apakah kegagalan konvergensi VQE disebabkan oleh parameter ekonomi ($\lambda, \mu, \sigma$) ataukah oleh kerasnya batasan penalti ($A$). Dengan memisahkan $H_{final} = H_{pure} + H_{pen}$, kita mendapatkan desain *Hamiltonian* yang *debuggable*: jika optimizer gagal konvergen, kita bisa memeriksa apakah $\lambda$ terlalu besar, $A$ terlalu dominan, atau interaksi antar aset terlalu kuat—sebelum menyentuh kode sirkuit kuantum sama sekali.

Menariknya, ada lapisan lebih dalam yang perlu dijelajahi. Model Markowitz konvensional hanya menggunakan momen statistik historis ($\mu, \sigma$): ia "buta" terhadap dinamika strategi dan aliran informasi di pasar. Dokumen ini membuktikan bahwa struktur fungsional *Hamiltonian* Ising secara alami menerima penggantian parameter statistik tersebut dengan proksi informasi kuantum (*QMI*) untuk kopling $J_{ij}$ dan proksi strategis (*Game Theory payoff*) untuk medan lokal $h_i$—tanpa melanggar satu pun syarat matematis sistem.

## 2. Aksioma & Intuisi

Kita memandang pemilihan aset sebagai sistem partikel biner. Setiap aset $i$ memiliki dua keadaan: $|1\rangle$ (dibeli) dan $|0\rangle$ (dihindari). Analogi fisika yang paling dekat adalah model *magnet Ising* dengan dua orientasi *spin*.

- **Risiko ($\Sigma$):** Bertindak sebagai energi interaksi antar partikel. Jika dua aset berkorelasi positif (co-movement), sistem akan "panas" (energi tinggi) jika keduanya dipilih bersamaan, menciptakan risiko terpusat (*concentration risk*).
- **Return ($\mu$):** Bertindak sebagai medan eksternal yang menarik partikel ke keadaan energi rendah (menguntungkan). Analoginya: medan magnet yang menarik *spin* ke satu arah preferensi.
- **Intuisi Kunci:** Mencari portofolio optimal setara dengan mencari *ground state* pada sistem magnetik—konfigurasi spin yang paling stabil secara energi. Inilah jembatan konversi dari domain ekonomi ke domain fisika.

## 3. Reduksionisme (Kasus Minimal: 2 Aset)

Secara umum, model Markowitz murni (tanpa batasan) untuk $N$ aset dinyatakan sebagai kombinasi kuadratik risiko dan linear *return*:
$$ \mathcal{L}(x) = x^T \Sigma x - \lambda \mu^T x \qquad (1) $$

> **Visualisasi: Operasi Matriks Markowitz (2 Aset)**
> Untuk memahami bagaimana ekspresi (1) berubah menjadi polinomial, kita jabarkan perkalian matriksnya:
> $$ \begin{split} \mathcal{L}(x) &= \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{21} & \sigma_2^2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} - \lambda \begin{pmatrix} \mu_1 & \mu_2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \\\\ &= \sigma_1^2 x_1^2 + \sigma_2^2 x_2^2 + 2\sigma_{12}x_1 x_2 - \lambda(\mu_1 x_1 + \mu_2 x_2) \end{split} $$
> Karena $x_i \in \{0, 1\}$, maka $x_i^2 = x_i$. Suku varians berubah menjadi linear terhadap variabelnya sendiri.

Di mana $\Sigma$ adalah matriks kovarians dan $\mu$ adalah vektor *expected return*. Untuk memahami mekanismenya, mari bedah sistem 2-aset tanpa penalti:
$$ \mathcal{L}_{pure} = \sigma_1^2 x_1 + \sigma_2^2 x_2 + 2\sigma_{12}x_1 x_2 - \lambda(\mu_1 x_1 + \mu_2 x_2) \qquad (2) $$

Jika $x_1=1, x_2=0$, maka $E = \sigma_1^2 - \lambda \mu_1$. Kita mencari kombinasi $x_i$ yang menghasilkan nilai $E$ terkecil.

## 4. Jembatan Formalisme & Logika

Kita menggunakan transformasi variabel biner ke *spin*:
$$ x_i \to s_i \in \{1, -1\} \implies x_i = \frac{1 - s_i}{2} \qquad (3) $$

Logikanya: 
- Jika $s_i = 1$ (*spin up*), maka $x_i = 0$ → aset tidak dipilih.
- Jika $s_i = -1$ (*spin down*), maka $x_i = 1$ → aset dipilih.

Transformasi ini bersifat *affine* murni: linear dan bijektif. Konsekuensi pentingnya adalah bahwa setiap gradien utilitas ekonomi dalam domain $x_i \in \{0,1\}$ akan terproyeksi secara linear ke dalam parameter *spin* dengan faktor normalisasi $\frac{1}{2}$. Faktor ini muncul karena rentang variabel *spin* mencakup dua satuan energi (dari $-1$ ke $+1$), sementara variabel biner hanya satu satuan. Ini jaminan bahwa *ground state* Hamiltonian akan selalu berhimpitan dengan titik utilitas ekonomi maksimum.

## 5. Derivasi "Scratchpad": Objektif Murni

### Fase 1: Transformasi QUBO Murni
> **Visualisasi: Jembatan Generalisasi ($2 \to N$ Aset)**
> Dari Persamaan (2), kita kumpulkan suku-suku berdasarkan variabel $x_i$ dan interaksinya $x_i x_j$:
> $$ \mathcal{L}_{pure} = \underbrace{(\sigma_1^2 - \lambda \mu_1)}_{Q_{11}} x_1 + \underbrace{(\sigma_2^2 - \lambda \mu_2)}_{Q_{22}} x_2 + \underbrace{2\sigma_{12}}_{2Q_{12}} x_1 x_2 $$
> Pola ini digeneralisasikan untuk $N$ aset dengan mendefinisikan elemen diagonal $Q_{ii}$ sebagai bias individu dan elemen *off-diagonal* $Q_{ij}$ sebagai interaksi antar aset.

Model Markowitz murni dalam variabel $x_i$:
$$ \mathcal{L}_{pure}(x) = \sum_{i} (\sigma_i^2 - \lambda \mu_i) x_i + \sum_{i < j} 2\sigma_{ij} x_i x_j \qquad (4) $$

Kita definisikan koefisien QUBO murni:
- $Q_{ii} = \sigma_i^2 - \lambda \mu_i$
- $Q_{ij} = \sigma_{ij}$

### Fase 2: Transformasi ke Ising Murni
Substitusi $x_i = \frac{1-s_i}{2}$ ke persamaan (4):
$$ H_{pure} = \sum_i Q_{ii} \frac{1-s_i}{2} + \sum_{i<j} 2Q_{ij} \left(\frac{1-s_i}{2}\right)\left(\frac{1-s_j}{2}\right) \qquad (5) $$

Ekspansi aljabar:
$$ H_{pure} = \sum_i \frac{Q_{ii}}{2} - \sum_i \frac{Q_{ii}}{2} s_i + \sum_{i<j} \frac{Q_{ij}}{2} (1 - s_i - s_j + s_i s_j) \qquad (6) $$

Kumpulkan suku-suku berdasarkan orde *spin*:
- **Suku Interaksi ($J_{ij}$):** $J_{ij}^{pure} = \frac{Q_{ij}}{2} = \frac{\sigma_{ij}}{2}$
- **Suku Medan ($h_i$):** $h_i^{pure} = -\frac{Q_{ii}}{2} - \sum_{j \neq i} \frac{Q_{ij}}{2}$
- **Konstanta ($C$):** $C^{pure} = \sum_i \frac{Q_{ii}}{2} + \sum_{i<j} \frac{Q_{ij}}{2}$

### Fase 3: Penambahan Suku Penalti ($H_{final} = H_{pure} + H_{pen}$)
Batasan jumlah aset $K$ dinyatakan sebagai $P(x) = A (\sum x_i - K)^2$. Transformasi ke *spin*:
$$ \sum x_i = \frac{N}{2} - \frac{1}{2} \sum s_i $$

> **Derivasi Identitas:**
> Karena $s_i \in \{1, -1\}$, maka $s_i^2 = 1$ untuk setiap $i$, sehingga $\sum_{i=1}^N s_i^2 = N$. 

Maka penalti dalam bentuk *spin*:
$$ H_{pen} = A \left( \left(\frac{N}{2} - K\right) - \frac{1}{2} \sum s_i \right)^2 \qquad (7) $$

Misalkan $K' = \frac{N}{2} - K$, maka:
$$ H_{pen} = A \left( K'^2 - K' \sum s_i + \frac{1}{4} (\sum s_i)^2 \right) \qquad (8) $$

Gunakan identitas $(\sum s_i)^2 = N + 2 \sum_{i<j} s_i s_j$:
> **Derivasi Identitas:**
> Ekspansi kuadrat dari jumlahan *spin* adalah $(\sum_i s_i)(\sum_j s_j) = \sum_i s_i^2 + \sum_{i \neq j} s_i s_j$. 
> Suku *off-diagonal* $\sum_{i \neq j} s_i s_j$ mengandung pasangan $(i,j)$ dan $(j,i)$ yang identik secara nilai, sehingga dapat ditulis sebagai $2 \sum_{i<j} s_i s_j$.
> Maka, $(\sum s_i)^2 = N + 2 \sum_{i<j} s_i s_j$.

$$ H_{pen} = \sum_{i<j} \frac{A}{2} s_i s_j - \sum_i (A K') s_i + A(K'^2 + \frac{N}{4}) \qquad (9) $$

## 6. Visualisasi Perhitungan (Struktur Matriks)
Gabungan parameter *Hamiltonian* total $H = \sum J_{ij} s_i s_j + \sum h_i s_i$ didekomposisi menjadi kontribusi fundamental (ekonomi/strategis) dan kontribusi batasan (penalti):

> **1. Matriks Interaksi ($J_{ij}$):**
> $$ J_{ij}^{total} = J_{ij}^{pure} + J_{ij}^{pen} $$
> Di mana komponen murni ($J_{ij}^{pure}$) merepresentasikan kekuatan kopling intrinsik antar aset:
> $$ J_{ij}^{pure} = \frac{\sigma_{ij}}{2} $$
> *(Catatan: Suku $J_{ij}^{pure}$ ini merupakan titik masuk untuk integrasi Quantum Mutual Information [[QMI]] sebagai proksi total korelasi informasi dalam ruang Hilbert).*
> 
> Dan komponen penalti ($J_{ij}^{pen}$) memberikan tekanan "*anti-ferromagnetic*" untuk memastikan kepatuhan terhadap batasan jumlah aset $K$:
> $$ J_{ij}^{pen} = \frac{A}{2} $$

> **2. Vektor Medan Lokal ($h_i$):**
> $$ h_i^{total} = h_i^{pure} + h_i^{pen} $$
> Di mana komponen murni ($h_i^{pure}$) merepresentasikan bias intrinsik aset:
> $$ h_i^{pure} = -\frac{\sigma_i^2 - \lambda \mu_i}{2} - \sum_{j \neq i} \frac{\sigma_{ij}}{2} $$
> *(Catatan: Suku $h_i^{pure}$ ini merupakan titik masuk untuk integrasi model Game Theory [[GT_to_h]] sebagai proksi *marginal payoff*).*
> 
> Dan komponen penalti ($h_i^{pen}$) memastikan kepatuhan terhadap batasan jumlah aset $K$:
> $$ h_i^{pen} = -A \left(\frac{N}{2} - K\right) $$

## 7. Bukti Kesebandingan: Parameter Hamiltonian vs. Informasi & Strategi

Substitusi parameter statistik konvensional ($\mu, \sigma$) dengan parameter strategis ($E, I$) memerlukan bukti kesebandingan matematis guna menjamin konsistensi fungsional dalam lanskap energi *Hamiltonian*. Proses ini diawali dengan ekstraksi data empiris dari pergerakan harga saham melalui pengamatan pola *candlestick* untuk menentukan probabilitas gabungan aset.

### A. Ekstraksi Data dan Probabilitas Gabungan
Landasan empiris model ini dibangun melalui penghitungan frekuensi kemunculan pola pergerakan harga antara dua aset $i$ dan $j$ pada rentang waktu tertentu. Setiap *candle* dikategorikan ke dalam dua *state* diskret: Naik ($|1\rangle$) dan Turun ($|0\rangle$). Dengan mencatat kemunculan empat kombinasi pola, yaitu Naik-Naik ($n_{11}$), Naik-Turun ($n_{10}$), Turun-Naik ($n_{01}$), dan Turun-Turun ($n_{00}$), kita dapat merumuskan matriks probabilitas gabungan sebagai $P(a,b) = n_{ab} / N$, di mana $N$ adalah total observasi.

Probabilitas gabungan tersebut digunakan secara simultan untuk mendefinisikan dua komponen utama dalam *Hamiltonian* hibrid. Pertama, probabilitas ini digunakan sebagai bobot ekspektasi dalam penentuan nilai *payoff matrix* guna menghitung *marginal payoff* strategis yang menjadi basis medan lokal $h_i$. Kedua, probabilitas tersebut berfungsi untuk mengonstruksi matriks densitas $\rho_{ij}$ dalam bentuk **keadaan campuran** (*mixed state*) diagonal, yaitu:
$$ \rho_{ij} = \sum_{a,b} P(a,b) |ab\rangle\langle ab| \qquad (10) $$

> **Mengapa Mixed State, Bukan Pure State?**
> Jika kita menggunakan *pure state encoder* $|\psi\rangle_{ij} = \sum_{a,b} \sqrt{P(a,b)} |ab\rangle$, maka $\rho_{ij} = |\psi\rangle\langle\psi|$ adalah proyektor *rank-1*. Akibatnya, entropI sistem gabungan $S(\rho_{ij}) = 0$ **secara otomatis dan selalu**, karena *pure state* memiliki entropi nol. Ini membuat QMI menjadi $I(i:j) = S(\rho_i) + S(\rho_j)$—yang hanya mengukur entropi marginal, bukan korelasi sejati. Dengan menggunakan *mixed state* diagonal (persamaan 10), entropi $S(\rho_{ij})$ tidak lagi nol, dan QMI yang dihasilkan **persis ekuivalen** dengan *classical mutual information*:
> $$ I_{classical}(i:j) = \sum_{a,b} P(a,b) \log \frac{P(a,b)}{P(a)P(b)} $$
> Pendekatan ini lebih jujur secara matematis—kita menghitung informasi klasik yang di-*embed* ke dalam formalisme kuantum, dan mengakui itu secara eksplisit.

> **Catatan Orthogonalitas $h_i$ dan $J_{ij}$:**
> Perlu dicatat bahwa $P(a,b)$ yang sama digunakan untuk menghitung $h_i$ (melalui *expected payoff*) dan $J_{ij}$ (melalui $\rho_{ij}$ dan QMI). Namun, keduanya mengekstrak **moment informasi yang berbeda** dari distribusi tersebut: $h_i$ mengekstrak momen pertama (ekspektasi linear per strategi), sedangkan $J_{ij}$ mengekstrak ukuran ketergantungan bersama (entropi gabungan vs. marginal). Ini setara dengan perbedaan antara $\mu_i$ dan $\sigma_{ij}$ dalam Markowitz konvensional—keduanya berasal dari distribusi *return* yang sama, tetapi merepresentasikan informasi yang *orthogonal* secara fungsional.

### B. Linearitas Medan Lokal ($h_i$) dan Marginal Payoff
Medan lokal $h_i$ dalam formalisme Ising merepresentasikan bias linear yang menentukan kecenderungan orientasi *spin* individu di bawah pengaruh tekanan eksternal. Dalam ekosistem pasar, tekanan ini setara dengan insentif strategis atau *marginal payoff* yang mendorong aset untuk berada pada kondisi tertentu guna memaksimalkan utilitas investor. Secara matematis, medan lokal didefinisikan sebagai selisih energi potensial antara dua *state*, yang secara fungsional identik dengan selisih ekspektasi keuntungan antara strategi beli dan strategi hindari. Keselarasan fungsional ini memungkinkan transisi mulus dari domain optimasi utilitas ekonomi menuju domain minimisasi energi *Hamiltonian* kuantum.

Transformasi dari variabel biner Markowitz $x_i \in \{0, 1\}$ menuju variabel *spin* $s_i \in \{1, -1\}$ mengikuti pemetaan *affine* $x_i = (1-s_i)/2$. Akibat dari pemetaan tersebut, gradien utilitas ekonomi akan terproyeksi secara linear ke dalam parameter medan lokal $h_i$ dengan faktor normalisasi sebesar setengah. Faktor penskalaan ini muncul karena rentang variabel *spin* mencakup dua satuan energi dalam ruang konfigurasi, sementara variabel biner hanya mencakup satu satuan tunggal. Dengan demikian, titik *ground state* pada *Hamiltonian* dipastikan akan selalu bertepatan secara eksak dengan titik utilitas strategis maksimum bagi para pelaku pasar [[GT_to_h]].

> **Keterbatasan Diskretisasi Candlestick:**
> Perlu diantisipasi bahwa kategori Naik/Turun ini mengabaikan **magnitudo** pergerakan harga. Hari di mana saham naik 0.5% dan hari di mana saham melonjak 10% sama-sama tercatat sebagai $|1\rangle$. Akibatnya, *marginal payoff* ($h_i$) dan matriks probabilitas yang dihasilkan kehilangan sensitivitas terhadap risiko *tail-end* (kejadian ekstrem pasar). Solusi yang dapat dipertimbangkan adalah menggunakan frekuensi yang dibobot dengan magnitudo *return* aktual, namun hal ini akan meningkatkan kompleksitas model secara signifikan.

### C. Monotonisitas Kopling ($J_{ij}$) dan Quantum Mutual Information (QMI)
Parameter interaksi atau kopling $J_{ij}$ merupakan komponen yang bertanggung jawab atas pembentukan korelasi informasi dan ketergantungan statistik antar aset. Dalam formulasi ini, $J_{ij} \propto \sqrt{I(i:j)}$ tidak diturunkan dari *first principles* termodinamika, melainkan merupakan **pilihan desain** (*ansatz*) yang termotivasi oleh relasi suhu tinggi (*high-temperature limit*) model Ising: $I(i:j) \approx \frac{1}{2}(\beta J_{ij})^2$. Sebagai *ansatz*, ia memenuhi syarat-syarat fisikal yang masuk akal: kopling nol saat tidak ada korelasi informasi, dan kopling membesar secara monoton seiring meningkatnya saling-ketergantungan antar aset. Ini bukan derivasi ketat, tetapi merupakan *ansatz* yang **terformulasi dengan baik** dan ada presedennya dalam literatur *econophysics*.

Penentuan tanda ($\pm$) pada parameter $J_{ij}$ tidak dapat dilakukan hanya melalui QMI karena entropi bersifat selalu positif dan mengukur **total korelasi** tanpa membedakan co-movement dari anti-korelasi. Oleh karena itu, diperlukan data tambahan berupa koefisien korelasi Pearson ($\rho_{ij}$): tanda negatif ($J_{ij} < 0$) merepresentasikan interaksi *ferromagnetic* di mana aset cenderung bergerak searah, sedangkan tanda positif ($J_{ij} > 0$) merepresentasikan interaksi *antiferromagnetic* yang bermanfaat untuk *hedging*. Koefisien normalisasi $\kappa$ diderivasi dari volatilitas pasar rata-rata ($\sigma_{avg}$) yang berperan sebagai "Suhu Pasar" ($T$), mengikuti preseden dari Mantegna & Stanley (1999):
$$ T \sim \sigma_{avg}, \quad \kappa \approx \sqrt{2} \, k_B T \qquad (11) $$

> **Interpretasi Fisik Suhu Pasar:**
> Pasar yang sangat volatil ($\sigma_{avg}$ besar, $T$ tinggi) akan mengaburkan ikatan informasi antar aset—persis seperti fluktuasi termal yang merusak keteraturan *spin* dalam material magnetik. Koefisien $\kappa$ harus dikalibrasi secara hati-hati agar sepadan skalanya dengan penalti $A$. Jika tidak, lanskap energi *Hamiltonian* akan rusak: model akan mengabaikan optimasi portofolio demi mematuhi batasan jumlah aset, atau sebaliknya melanggar batasan demi mengejar *return* tertinggi [[QMI]].

> **Catatan Kompleksitas Komputasi:**
> Untuk portofolio dengan $N$ aset, jumlah pasangan yang memerlukan kalkulasi QMI adalah $\binom{N}{2} = \frac{N(N-1)}{2}$. Untuk $N = 100$, ini berarti 4.950 kalkulasi QMI. Ini masih dalam batas komputasi yang layak, tetapi perlu diperhitungkan dalam implementasi skala besar.

## 8. Verifikasi & Parameter
Mari uji batas untuk $N=2$ dan $K=1$ ($K' = 0$):
- Suku interaksi $J_{12}$ akan didominasi oleh $A/2$. Jika $A$ besar, $J_{12} \gg 0$, memaksa $s_1 s_2 = -1$ (satu *spin up*, satu *spin down*), yang berarti tepat 1 aset terpilih.
- Jika $\lambda$ sangat besar, $h_i$ akan didominasi oleh $\lambda \mu_i/2$ (positif), menarik *spin* ke $s_i = -1$ (beli).

## 9. Analogi "Physical Insight"
Pemodelan ini setara dengan **Antiferromagnetic Ising Model** di bawah medan magnet eksternal. Suku penalti $A$ memaksa sistem untuk memiliki jumlah *spin* "up" dan "down" yang spesifik, mirip dengan *constraint* pada sistem magnetik yang terkurung secara geometris (*geometric frustration*). Dan ini bukan sekadar metafora—constraint $\sum x_i = K$ secara matematis memang menciptakan *frustration* pada hiperkisi konfigurasi, persis seperti yang terjadi pada material magnetik terfrustasi.

> **Koneksi ke Boltzmann Machine:**
> Hamiltonian final kita memiliki struktur persis seperti *energy function* dari *Boltzmann Machine*: $E(x) = -\sum W_{ij} x_i x_j - \sum b_i x_i$, di mana $W_{ij} \leftrightarrow$ QMI dan $b_i \leftrightarrow$ *payoff*. Artinya model ini bisa ditafsirkan sebagai sebuah **Information-Strategic Boltzmann Machine**: mesin generatif yang bobot koneksinya bersumber dari aliran informasi antar aset, dan bias simpulnya bersumber dari tekanan strategis pasar.

## 10. Visualisasi Mentah
Bayangkan sebuah hiperkubus $N$-dimensi. 
1. Tanpa $A$: Titik minimum berada di pojok yang memiliki *return* tertinggi dan risiko terendah.
2. Dengan $A$: Pojok-pojok yang tidak memenuhi $\sum x_i = K$ ditarik ke atas (energi sangat tinggi), menyisakan lembah energi hanya pada bidang potong (*hyperplane*) yang valid.
3. Dengan QMI & GT: Lanskap energi pada *hyperplane* valid tidak lagi datar—ia memiliki topografi yang mencerminkan aliran informasi dan tekanan strategis pasar pada momen tersebut.

## 11. Formulasi Akhir: Hamiltonian Hibrid (Econophysics)
Setelah melalui proses dekomposisi dan pembuktian kesebandingan, kita dapat menyusun operator *Hamiltonian* final yang mengintegrasikan dinamika pasar strategis dan informasi kuantum:

$$ \hat{H}_{final} = \sum_{i<j} J_{ij}^{total} \hat{Z}_i \hat{Z}_j + \sum_i h_i^{total} \hat{Z}_i + C \cdot \hat{I} \qquad (12) $$

Di mana parameter-parameternya didefinisikan secara hibrid sebagai berikut:

> **1. Parameter Interaksi Total (QMI + Penalti):**
> $$ J_{ij}^{total} = \underbrace{\kappa \cdot \text{sgn}(\rho_{ij}) \sqrt{I(i:j)}}_{\text{Resonansi Informasi}} + \underbrace{\frac{A}{2}}_{\text{Batasan Kolektif}} $$
> Di mana $\text{sgn}(\rho_{ij})$ adalah fungsi tanda dari korelasi Pearson dan $\kappa \approx \sqrt{2} k_B T$, $T \sim \sigma_{avg}$.

> **2. Parameter Medan Lokal Total (GT + Penalti):**
> $$ h_i^{total} = \underbrace{\frac{E[i|+] - E[i|-]}{2}}_{\text{Insentif Strategis}} - \underbrace{A\left(\frac{N}{2} - K\right)}_{\text{Batasan Individual}} $$

**Interpretasi Fisik Akhir:**
*Hamiltonian* ini tidak lagi sekadar representasi statistik masa lalu ($\mu, \sigma$), melainkan sebuah **Sistem Terbuka** yang merespon aliran informasi ($I$) dan tekanan strategis ($E$). VQE akan mencari konfigurasi portfolio yang tidak hanya meminimalkan risiko, tetapi juga memaksimalkan "ketahanan informasi" dan "keunggulan strategi" dalam ekosistem pasar yang kompetitif. Dalam konteks *machine learning*, model ini dapat dipandang sebagai *Information-Strategic Boltzmann Machine* berbasis kuantum—sebuah jembatan antara *econophysics*, *game theory*, dan optimasi kuantum.
