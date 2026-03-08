# Bab 1: Analisis Finansial dalam Bingkai Ekonofisika

## 1.1 Fundamental Analysis: Dialektika Nilai dan Gaya Penggerak Pasar

Dalam memandang pasar finansial, kita tidak boleh hanya melihat angka yang berkedip di layar sebagai deretan data mati. Bayangkan pasar sebagai sebuah **sistem fisik yang kompleks** yang terus-menerus mencari titik kesetimbangan (equilibrium) di tengah fluktuasi energi informasi yang masuk.

### 1.1.1 Urgensi: Mengapa Harga Bergerak?
Dari sudut pandang fisika, pergerakan harga adalah manifestasi dari perpindahan energi antar pelaku pasar. Jika kita menganggap harga ($P$) sebagai posisi sebuah partikel, maka perubahan harga ($\Delta P$) memerlukan gaya penggerak. Tanpa gaya ini, sistem akan terjebak dalam kondisi stagnan atau *deadlocks*. Urgensi kita mempelajari analisis fundamental adalah untuk memahami "potensial" yang menyebabkan gaya tersebut muncul.

### 1.1.2 Mekanisme Penggerak: Teori Lelang dan Hukum Termodinamika Pasar
Proses *price discovery* melalui **Teori Lelang (Auction Theory)** sejatinya adalah proses pencarian koordinat di mana jumlah pembeli (*bid*) dan penjual (*ask*) mencapai titik temu. 
- **Ketidakseimbangan (Imbalance):** Seperti perbedaan tekanan udara yang menciptakan angin, ketidakseimbangan volume antara *supply* dan *demand* menciptakan momentum harga. 
- **Aksioma Dasar:** Kita berangkat dari postulat bahwa harga mencerminkan seluruh informasi yang tersedia, namun informasi tersebut tidak terdistribusi secara instan (analog dengan keterbatasan kecepatan cahaya dalam merambatkan medan).

### 1.1.3 Metrik Valuasi sebagai Potensial Intrinsik
Analisis rasio keuangan seperti **Price-to-Earnings (P/E) Ratio** dan **Dividend Yield** dapat kita analogikan sebagai **Energi Potensial** sebuah aset. 
- Aset dengan P/E rendah namun fundamental kuat ibarat partikel di puncak bukit yang memiliki energi potensial tinggi untuk jatuh (dalam hal ini, harganya naik menuju nilai intrinsiknya).
- **Sharpe Ratio** ($\frac{\mu - R_f}{\sigma}$) bertindak sebagai efisiensi sistem, mengukur seberapa banyak "kerja" (return) yang dihasilkan dibandingkan dengan "panas/entropi" (risiko/volatilitas) yang timbul.

### 1.1.4 Makroekonomi: Medan Eksternal dan Siklus Fase
Ekonomi makro adalah **medan eksternal (external field)** yang menyelimuti seluruh aset.
- **Inflasi & Suku Bunga:** Bertindak seperti suhu lingkungan. Suku bunga tinggi meningkatkan "viskositas" pasar, membuat modal sulit bergerak (likuiditas rendah).
- **Rotasi Sektoral:** Bayangkan ini sebagai transisi fase dalam material. Saat ekonomi berpindah dari fase ekspansi ke kontraksi, sistem melakukan reorganisasi. Investor memindahkan massa (modal) dari sektor siklikal (yang sensitif terhadap perubahan suhu ekonomi) ke sektor defensif untuk menjaga stabilitas energi portofolio.

---

## 1.2 Technical Analysis: Observasi Trajektori dalam Ruang Harga-Waktu

Jika fundamental memberi tahu kita *mengapa* sebuah partikel harus bergerak, analisis teknikal fokus pada *bagaimana* partikel tersebut telah dan sedang bergerak dalam ruang-waktu ($P, t$).

### 1.2.1 Visualisasi Time-Series: Jejak Stokastik
Grafik harga adalah trajektori partikel dalam medan stokastik. Kita tidak melihat pergerakan linier, melainkan **Gerak Brown (Brownian Motion)** yang terdistorsi oleh memori pasar. Sumbu-X adalah waktu ($t$) yang terus mengalir secara entropis, dan Sumbu-Y adalah harga ($P$) yang merepresentasikan level energi sistem.

### 1.2.2 Anatomi Candlestick: Snapshot Momentum
Satu batang *candlestick* (OHLC) adalah observasi kuantum dalam jendela waktu $\Delta t$. 
- **Body:** Merepresentasikan perpindahan bersih (displacement) partikel.
- **Wick (Shadow):** Merepresentasikan fluktuasi ekstrem atau "gangguan" yang sempat terjadi namun berhasil diredam oleh gaya pemulih pasar.
Dalam analogi elektronika, *candlestick* adalah seperti sinyal pada osiloskop yang menangkap amplitudo puncak-ke-puncak dalam interval tertentu.

### 1.2.3 Sampling Data dan Stasioneritas
Untuk melakukan analisis matematis yang presisi, kita harus melakukan transformasi data. Harga mentah ($P_t$) bersifat non-stasioner (memiliki tren). Kita menggunakan **Logarithmic Returns** ($R_t$) untuk mencapai stasioneritas, sebuah kondisi di mana properti statistik sistem tidak berubah terhadap waktu:

$$ R_t = \ln\left(\frac{P_t}{P_{t-1}}\right) $$

Ini memungkinkan kita menerapkan alat mekanika statistik untuk memprediksi probabilitas state masa depan.

---

## 1.3 Risk Management: Entropi dan Kontrol Sistem

Manajemen risiko adalah tentang bagaimana kita mengendalikan **Entropi** dalam portofolio kita agar tidak terjadi ledakan (kerugian total).

### 1.3.1 Trade-off Risk and Reward
Dalam fisika, tidak ada sistem yang 100% efisien. Setiap usaha untuk mendapatkan energi (return) pasti menghasilkan panas (risiko). Kita menggunakan pendekatan **Weighted Risk** untuk memastikan bahwa paparan kita terhadap satu aset tidak menyebabkan resonansi yang merusak seluruh struktur portofolio.

### 1.3.2 Risk Aversion Endogen: Respon Non-Linear Investor
Salah satu terobosan dalam riset kita adalah memperlakukan kecenderungan penghindaran risiko ($\lambda$) bukan sebagai konstanta, melainkan sebagai variabel yang bergantung pada kondisi sistem itu sendiri. Bayangkan ini seperti **hambatan (resistance)** dalam rangkaian listrik yang berubah nilainya saat suhu (volatilitas) meningkat.

Kita mendefinisikan **Endogenous Risk Aversion** ($\lambda_{market}$) menggunakan fungsi logistik (sigmoid) berbasis Sharpe Ratio rata-rata pasar:

$$ \lambda_{market} = \frac{1}{1 + e^{\left(\frac{\mu_{avg}}{\sigma_{avg}}\right)}} $$

**Landasan Filosofis:**
1. Jika pasar memberikan return tinggi dengan risiko rendah ($\frac{\mu}{\sigma}$ besar), maka penyebut menjadi besar, $\lambda$ mendekati 0. Investor menjadi lebih berani (risk-seeking).
2. Sebaliknya, jika pasar kacau (volatilitas tinggi, $\frac{\mu}{\sigma}$ kecil), maka $e^0$ mendekati 1, $\lambda$ mendekati 0.5 atau lebih besar. Investor secara alami menarik diri ke zona aman.

Analogi Elektronika: Fungsi ini bekerja seperti **Op-Amp Limiter** atau **Automatic Gain Control (AGC)** yang secara otomatis meredam sinyal input yang terlalu liar untuk menjaga output tetap stabil dalam batas operasional yang aman.
