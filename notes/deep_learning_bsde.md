# Ringkasan "Deep Learning-Based BSDE Solver for Libor Market Model"

## Ringkasan Pendahuluan

Dokumen ini merangkum pendahuluan dari paper "Deep Learning-Based BSDE Solver for Libor Market Model with Application to Bermudan Swaption Pricing and Hedging" oleh Haojie Wang, Han Chen, Agus Sudjianto, Richard Liu, dan Qi Shen. Ringkasan ini disusun berdasarkan paragraf.

### Paragraf 1
Paragraf ini memperkenalkan Libor Market Model (LMM), yang juga dikenal sebagai Model BGM, sebagai model struktur suku bunga yang banyak digunakan. Model ini disajikan sebagai perluasan dari model Heath, Jarrow, dan Morton (HJM) yang menggunakan variabel pasar yang dapat diamati sebagai input langsung. Paragraf ini menyoroti keunggulan LMM dibandingkan model HJM, seperti kemampuannya untuk mengatasi masalah teknis seperti suku bunga yang meledak, dan aplikasinya dalam penetapan harga opsi vanilla seperti caps, floors, dan swaption Eropa.

### Paragraf 2
Paragraf ini membahas implementasi LMM menggunakan simulasi Monte Carlo, khususnya untuk mengevaluasi swaption Amerika dan Bermuda. Paragraf ini menunjukkan tantangan yang terkait dengan keputusan eksekusi awal dan menyebutkan beberapa pendekatan yang ada yang diusulkan oleh Andersen (1998), Broadie dan Glasserman (1997), dan Longstaff dan Schwartz (1998). Kompleksitas penghitungan sensitivitas (Greeks) menggunakan simulasi Monte Carlo juga disebutkan.

### Paragraf 3
Paragraf ini memperkenalkan metode Persamaan Diferensial Parsial (PDE) numerik sebagai alternatif yang lebih alami untuk menghitung turunan Yunani. Paragraf ini mencantumkan keuntungan dari metode ini tetapi juga menekankan tantangan signifikan dari "Kutukan Dimensi" ketika berhadapan dengan masalah berdimensi tinggi. Paragraf ini secara singkat menyebutkan tiga kategori metode tradisional yang digunakan untuk mengatasi masalah dimensi ini.

### Paragraf 4
Paragraf ini memperkenalkan kemajuan terkini dalam menyelesaikan PDE parabola nonlinier berdimensi tinggi menggunakan algoritma berdasarkan Backward Stochastic Differential Equations (BSDEs). Dijelaskan bahwa pendekatan ini secara teoritis didasarkan pada teorema Feynman-Kac yang digeneralisasi dan memanfaatkan hubungan yang mendalam dengan teori kontrol optimal stokastik dan pembelajaran mesin, khususnya Deep Neural Networks (DNNs). Keberhasilan DNN di berbagai bidang dan penerapannya untuk memecahkan BSDE dan masalah terkait disorot.

### Paragraf 5
Paragraf ini menguraikan pendekatan penulis, yang terinspirasi oleh perkembangan terkini dalam kecerdasan buatan dan pembelajaran mendalam. Ini membedakan penelitian mereka dari dunia matematika komputasi, menjelaskan bagaimana mereka menggunakan DNN maju untuk menyelesaikan PDE parabola berdimensi tinggi melalui representasi BSDE berdasarkan rumus Feynman-Kac nonlinier.

### Paragraf 6
Paragraf ini membahas keterbatasan pemecah DNN maju konvensional, yang hanya cocok untuk penetapan harga derivatif gaya Eropa. Ini memperkenalkan kompleksitas penetapan harga instrumen yang dapat dipanggil seperti swaption Bermuda, yang banyak digunakan untuk melindungi risiko suku bunga. Paragraf ini menekankan perlunya menangani eksekusi awal dengan tepat, biasanya menggunakan prinsip pemrograman dinamis Bellman dan proses penilaian mundur.

### Paragraf 7
Paragraf ini menegaskan bahwa paper ini adalah yang pertama menerapkan DNN mundur untuk menilai derivatif yang dapat dipanggil dalam literatur rekayasa keuangan. Ini memperkenalkan pendekatan baru "pembelajaran DNN mundur", di mana harga opsi diproyeksikan ke belakang, dan model belajar dengan meminimalkan varians dari nilai awal yang diproyeksikan. Para penulis menyoroti penerapan umum dari metode mereka untuk derivatif yang dapat dipanggil dan hubungannya dengan Kontrol Optimal Stokastik, teori FBSDE, dan teori PDE.

### Paragraf 8
Paragraf ini memberikan gambaran umum tentang struktur paper. Bagian 2 memperkenalkan dasar-dasar model pasar Libor. Bagian 3 menyajikan masalah penetapan harga derivatif keuangan dalam formulasi PDE dan BSDE, membahas pemecah yang terinspirasi dari pembelajaran mendalam, dan merinci kontribusi utama paper. Bagian 4 menyajikan eksperimen numerik yang membandingkan pemecah DNN mundur dengan hasil dari QuantLib. Bagian 5 menyimpulkan paper dan menyarankan arah penelitian di masa depan.

## Ringkasan Bab 2: Deskripsi Libor Market Model

Bab ini memperkenalkan Libor Market Model (LMM) dan kerangka teoretisnya untuk implementasi numerik menggunakan jaringan saraf dalam (deep neural networks). Pembahasan mengikuti notasi dari Andersen-Piterbarg (2011).

### Sub-bab 2.1: Dinamika LMM dan Ukuran Penetapan Harga
Sub-bab ini mendefinisikan elemen-elemen dasar LMM. Dimulai dengan pendefinisian [[ruang probabilitas tersaring (filtered probability space)]] dan struktur tenor (tenor structure) yang tetap. Selanjutnya, mendefinisikan suku bunga Libor forward, $L(t; T_n, T_{n+1})$, sebagai suku bunga sederhana yang berlaku antara dua tanggal di masa depan, yang nilainya ditentukan oleh harga obligasi tanpa kupon (zero-coupon bond).

Dinamika suku bunga Libor dimodelkan sebagai proses stokastik di bawah ukuran probabilitas tertentu. Paper ini menjelaskan dinamika proses tersebut di bawah dua ukuran yang berbeda: ukuran forward $T_{n+1}$ (di mana suku bunga $L_n(t)$ adalah [[martingale]]) dan ukuran terminal $T_N$. [[Persamaan diferensial stokastik]] (SDE) yang mengatur evolusi suku bunga Libor disajikan untuk masing-masing ukuran.

#### Pengembangan Ide dan Penurunan Rumus (2.1)
**Pengembangan Ide**
Tujuan utama dari LMM adalah untuk memodelkan evolusi suku bunga forward. Ide dasarnya adalah memulai dengan suku bunga yang dapat diamati di pasar (yaitu, suku bunga Libor) dan memodelkan dinamika mereka secara langsung, yang merupakan peningkatan dari model HJM yang memodelkan suku bunga forward sesaat yang tidak dapat diamati secara langsung.

Untuk melakukan ini, pertama-tama ditetapkan kerangka waktu diskrit yang disebut **struktur tenor** ($T_0, T_1, \dots, T_N$), yang sesuai dengan tanggal reset suku bunga di pasar nyata. Suku bunga Libor forward, $L_n(t)$, didefinisikan sebagai suku bunga yang berlaku pada periode antara $T_n$ dan $T_{n+1}$, seperti yang terlihat dari waktu $t$.

Kunci pemodelan adalah memilih **ukuran probabilitas** (measure) yang tepat. Dalam keuangan, mengubah ukuran probabilitas (menggunakan Teorema Girsanov) setara dengan mengubah *numéraire* (aset yang digunakan untuk diskonto). LMM memanfaatkan ini secara ekstensif. Dengan memilih obligasi tanpa kupon $P(t, T_{n+1})$ sebagai numéraire, suku bunga forward $L_n(t)$ menjadi sebuah **martingale** di bawah ukuran probabilitas yang sesuai (disebut ukuran forward $T_{n+1}$). Ini sangat menyederhanakan persamaan dinamikanya karena tidak ada *drift term*. Namun, untuk menilai derivatif yang kompleks, seringkali lebih mudah untuk bekerja di bawah satu ukuran tunggal yang konsisten, seperti **ukuran terminal** yang menggunakan $P(t, T_N)$ sebagai numéraire. Perubahan ke ukuran ini memunculkan kembali *drift term* yang kompleks, tetapi memungkinkan semua suku bunga dimodelkan dalam kerangka yang sama.

**Penurunan Rumus**
1. **Definisi Suku Bunga Libor Forward (2.2):** Hubungan antara suku bunga forward ($L_n(t)$) dan harga obligasi tanpa kupon ($P(t,T)$) adalah dasar. Harga obligasi pada waktu $t$ untuk jatuh tempo $T_n$ adalah $P(t, T_n)$. Jika Anda berinvestasi dalam obligasi ini, Anda akan menerima \$1 pada $T_n$. Ini setara dengan menginvestasikan kembali secara berulang pada suku bunga Libor. Dari prinsip non-arbitrase, hubungan berikut harus berlaku:
   $$ P(t, T_n) = P(t, T_{n+1}) \cdot (1 + \tau_n L_n(t)) $$ 
di mana $\tau_n = T_{n+1} - T_n$. Dengan mengatur ulang persamaan ini, kita mendapatkan definisi $L_n(t)$:
   $$ L_n(t) = \frac{1}{\tau_n} \left( \frac{P(t, T_n)}{P(t, T_{n+1})} - 1 \right) $$ 

2. **Dinamika di Bawah Ukuran Forward (2.3):** Di bawah ukuran probabilitas $Q^{T_{n+1}}$ (di mana obligasi $P(t, T_{n+1})$ adalah numéraire), proses harga aset yang didiskontokan adalah martingale. Dalam kasus ini, aset tersebut adalah $L_n(t)$. Sebuah proses yang merupakan martingale tidak memiliki *drift term* (kecenderungan arah), sehingga dinamikanya hanya digerakkan oleh komponen stokastik (acak):
   $$ dL_n(t) = \sigma_n(t, L_n(t)) dW^{(n+1)}(t) $$ 

3. **Dinamika di Bawah Ukuran Terminal (2.4 & 2.5):** Ketika kita beralih dari ukuran $Q^{T_{n+1}}$ ke ukuran terminal $Q^{T_N}$, kita perlu menggunakan Teorema Girsanov untuk menemukan bagaimana proses stokastik $dW^{(n+1)}$ berubah dan bagaimana hal itu mempengaruhi dinamika $L_n(t)$. Perubahan ini memperkenalkan sebuah *drift term*, $\mu_n$, ke dalam SDE:
   $$ dL_n(t) = \mu_n(t, L(t))dt + \sigma_n(t, L_n(t))dW^{N}(t) $$ 
Rumus (2.5) memberikan bentuk eksplisit dari *drift term* ini. Ini adalah jumlah dari produk volatilitas dan korelasi antara suku bunga forward yang berbeda. Secara intuitif, drift dari satu suku bunga forward dipengaruhi oleh pergerakan suku bunga forward lainnya karena adanya korelasi di antara mereka.
   $$ \mu_n(t) = -\sum_{j=n+1}^{N-1} \frac{\tau_j \xi_j(t, L_j(t)) \xi_n(t, L_n(t)) \rho_{n,j}}{1 + \tau_j L_j(t)} $$ 

### Sub-bab 2.2: Fungsi Volatilitas Deterministik yang Dapat Dipisahkan
Sub-bab ini menjelaskan bahwa LMM dapat menangkap berbagai bentuk pergerakan kurva imbal hasil (yield curve) yang kompleks—seperti pergeseran paralel, perubahan kemiringan (steepening), dan pembentukan punuk (humps)—dengan menggunakan penggerak Brownian motion yang saling berkorelasi. Untuk tujuan simulasi dalam paper ini, penulis menggunakan struktur korelasi yang lebih sederhana, yaitu korelasi eksponensial $\rho_{ij} = \exp(-\beta|i - j|)$, yang cukup untuk mendemonstrasikan efektivitas metode yang diusulkan.

#### Pengembangan Ide dan Penurunan Rumus (2.2)
**Pengembangan Ide**
Masalah utama dengan LMM dalam bentuk umumnya adalah bahwa ia tidak bersifat **Markovian**. Artinya, volatilitas pada waktu $t$ bisa bergantung pada seluruh riwayat pergerakan suku bunga hingga waktu $t$, bukan hanya pada nilai suku bunga saat ini $L(t)$. Model non-Markovian sangat sulit untuk diselesaikan menggunakan metode PDE (Persamaan Diferensial Parsial).

Untuk mengatasi ini, sebuah asumsi penyederhanaan dibuat: volatilitas diasumsikan memiliki struktur yang dapat dipisahkan (separable). Idenya adalah untuk memisahkan pengaruh waktu dari pengaruh tingkat suku bunga itu sendiri. Dengan asumsi ini, model menjadi Markovian dalam variabel keadaan $L(t)$, yang memungkinkan penggunaan teknik PDE dan penyelesaian numerik yang lebih efisien.

**Penurunan Rumus**
1. **Bentuk Volatilitas Separabel (2.9):** Asumsi ini menyatakan bahwa vektor volatilitas $\sigma_n$ untuk setiap suku bunga forward $L_n$ dapat ditulis sebagai produk dari dua fungsi: 
   $$ \sigma_n(t, L_n(t)) = \lambda_n(t) \phi(L_n(t)) $$ 
   di mana:
   - $\lambda_n(t)$ adalah sebuah vektor baris dari fungsi-fungsi deterministik waktu. Bagian ini menangkap bagaimana volatilitas berubah seiring berjalannya waktu (misalnya, volatilitas mungkin lebih tinggi menjelang tanggal jatuh tempo).
   - $\phi(L_n(t))$ adalah fungsi skalar yang time-homogeneous (tidak bergantung pada waktu secara eksplisit) dan hanya bergantung pada nilai suku bunga saat ini $L_n(t)$. Bagian ini menangkap bagaimana volatilitas bereaksi terhadap perubahan tingkat suku bunga (misalnya, apakah volatilitas konstan atau meningkat saat suku bunga naik).
2. **Contoh Parameterisasi (Tabel 1):** Paper ini menyajikan tabel dengan beberapa bentuk fungsional yang umum digunakan untuk $\phi(x)$, yang masing-masing mengarah ke model yang berbeda:
   - **Log-normal:** $\phi(x) = x$. Ini adalah kasus standar di mana volatilitas proporsional dengan tingkat suku bunga. Ini mengarah pada distribusi log-normal untuk suku bunga, sama seperti dalam model Black-Scholes.
   - **CEV (Constant Elasticity of Variance):** $\phi(x) = x^p$, dengan $0 < p < 1$. Model ini memungkinkan "volatility smile", sebuah fitur yang sering diamati di pasar nyata.
   - **Displaced Log-normal:** $\phi(x) = bx + a$. Ini adalah modifikasi dari model log-normal yang dapat mencegah suku bunga menjadi negatif dan juga dapat menghasilkan beberapa tingkat "smile".

### Sub-bab 2.3: Struktur Korelasi
Sub-bab ini menjelaskan bahwa LMM dapat menangkap berbagai bentuk pergerakan kurva imbal hasil (yield curve) yang kompleks—seperti pergeseran paralel, perubahan kemiringan (steepening), dan pembentukan punuk (humps)—dengan menggunakan penggerak Brownian motion yang saling berkorelasi. Untuk tujuan simulasi dalam paper ini, penulis menggunakan struktur korelasi yang lebih sederhana, yaitu korelasi eksponensial $\rho_{ij} = \exp(-\beta|i - j|)$, yang cukup untuk mendemonstrasikan efektivitas metode yang diusulkan.

#### Pengembangan Ide dan Penurunan Rumus (2.3)
**Pengembangan Ide**
Dalam kenyataannya, suku bunga forward yang berbeda tidak bergerak secara independen. Ketika suku bunga jangka pendek naik, suku bunga jangka panjang cenderung ikut naik. Struktur korelasi adalah mekanisme dalam LMM untuk menangkap hubungan ini. Dengan mendefinisikan bagaimana guncangan acak (Brownian motions) untuk suku bunga yang berbeda saling terkait, model ini dapat menghasilkan pergerakan kurva imbal hasil yang realistis. Pergerakan ini tidak hanya pergeseran paralel sederhana, tetapi bisa juga berupa "rotational steepening" (ujung pendek dan panjang bergerak berlawanan arah) atau "humps" (bagian tengah kurva bergerak berbeda dari ujung-ujungnya).

Untuk paper ini, tujuannya bukan untuk membangun model kalibrasi yang paling akurat, melainkan untuk mendemonstrasikan kelayakan metode numerik baru (Backward DNN Solver). Oleh karena itu, dipilih struktur korelasi yang sederhana namun masuk akal secara intuitif.

**Penurunan Rumus**
1. **Definisi Korelasi:** Korelasi antara dua penggerak Brownian motion $dW_i$ dan $dW_j$ didefinisikan sebagai $E[dW_i dW_j] = \rho_{ij} dt$. Matriks dari semua $\rho_{ij}$ ini mendefinisikan seluruh struktur korelasi.

2. **Struktur Korelasi Eksponensial Sederhana:** Paper ini mengadopsi bentuk spesifik untuk korelasi:
   $$ \rho_{ij} = \exp(-\beta|i - j|) $$ 
   di mana $\beta$ adalah konstanta positif.
   - **Interpretasi:** Rumus ini berarti korelasi antara dua suku bunga forward, $L_i$ dan $L_j$, menurun secara eksponensial seiring dengan semakin jauhnya jarak mereka di sepanjang kurva tenor (diukur dengan $|i-j|$). 
   - **Implikasi:** Suku bunga forward yang berdekatan (misalnya, Libor 3-bulan dan Libor 6-bulan) akan sangat berkorelasi, sementara suku bunga yang berjauhan (misalnya, Libor 3-bulan dan Libor 10-tahun) akan memiliki korelasi yang jauh lebih rendah. Ini adalah asumsi yang masuk akal dan umum digunakan di pasar keuangan.