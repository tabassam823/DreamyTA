# Modul 1: Teori Portofolio Modern & Ekonofisika

## 1. Pendahuluan: Dinamika Pasar dan Pendekatan Ekonofisika

Pasar keuangan global merupakan sistem stokastik yang sangat kompleks, di mana interaksi antar aset seringkali menunjukkan perilaku non-linear yang sulit diprediksi oleh model ekonomi konvensional. Fenomena seperti keruntuhan pasar (*market crashes*) dan volatilitas ekstrem menunjukkan bahwa distribusi return seringkali memiliki ekor gemuk (*heavy-tailed distribution*) yang melampaui asumsi distribusi normal. Dalam konteks ini, pendekatan *Econophysics* hadir sebagai kerangka kerja yang kokoh dengan mengadopsi prinsip-metode dari fisika statistik untuk memodelkan dinamika harga sebagai interaksi banyak partikel (*many-body interaction*). Penggunaan analogi fisik ini memungkinkan kita untuk melihat fluktuasi pasar bukan sebagai derau acak belaka, melainkan sebagai manifestasi dari hukum-hukum statistik yang mendasari sistem fisik yang kompleks.

Integrasi antara mekanika statistik dan teori keuangan memberikan perspektif baru dalam memahami stabilitas portofolio melalui konsep energi sistem. Dengan memetakan aset-aset finansial ke dalam variabel-variabel fisik seperti spin dalam model Ising, optimasi portofolio dapat didefinisikan ulang sebagai upaya pencarian keadaan energi terendah (*ground state search*). Pendekatan reduksionisme ini sangat krusial karena memungkinkan pemanfaatan algoritma komputasi mutakhir, seperti *Variational Quantum Eigensolver* (VQE), untuk menyelesaikan masalah optimasi kombinatorial yang secara komputasi sangat berat bagi komputer klasik. Oleh karena itu, modul ini akan membangun fondasi teoretis mulai dari teori portofolio klasik hingga transformasi matematis yang diperlukan untuk implementasi pada perangkat keras kuantum.

## 1.1 Pipeline Data Finansial: Dari Harga ke Parameter Statistik

Sebelum melakukan optimasi portofolio menggunakan kerangka kerja Markowitz, kita harus mentransformasi data mentah yang bersifat kontinu menjadi parameter statistik yang relevan. Proses ini sangat krusial karena validitas Hamiltonian Ising sangat bergantung pada kualitas input data historis. Alur kerja (*pipeline*) data tersebut dapat dirincikan melalui tahapan formal berikut:

**1. Observasi Data Harga Mentah ($P_t$):**
Data mentah yang diamati adalah harga penutupan harian (*Close Price*) aset pada waktu $t$, yang kita nyatakan sebagai $P_t$. Data ini merupakan runtun waktu (*time series*) yang mencerminkan kapitalisasi pasar secara dinamis. Namun, harga mentah tidak dapat digunakan langsung dalam pemodelan karena sifatnya yang tidak stasioner.

**2. Transformasi ke Imbal Hasil (*Returns*):**
Terdapat dua jenis imbal hasil yang umum digunakan dalam pengolahan data statistik, yaitu *simple return* dan *log return*. *Simple return* ($R_s$) biasanya diaplikasikan untuk menghitung imbal hasil portofolio lintas aset (*cross-sectional aggregation*) karena sifat linearitasnya terhadap bobot investasi. Namun, dalam kerangka ekonofisika dan komputasi kuantum, kita memprioritaskan penggunaan *log return* ($r_t$) karena sifat aditifnya terhadap waktu (*time-series additivity*) dan ekuivalensinya dengan konsep energi dalam sistem fisik. Kita menghitung perubahan harga relatif menggunakan transformasi logaritmik untuk mendapatkan imbal hasil harian ($r_{daily,t}$), sebagaimana dibahas secara mendalam pada Bab 3. Transformasi ini mengubah domain harga yang bersifat multiplikatif menjadi domain imbal hasil yang bersifat aditif:

$$\begin{aligned}
R_{daily,s} &= \frac{P_t - P_{t-1}}{P_{t-1}} \\
R_{daily,s} &= \frac{P_t}{P_{t-1}} -1 \\
r_{daily,t} &= \ln(R_{daily,s}) \\
r_{daily,t} &= \ln \left(\frac{P_t}{P_{t-1}}\right) - \ln(1) \\
r_{daily,t} &= \ln \left(\frac{P_t}{P_{t-1}}\right) \\
r_{daily,t} &= \ln(1+R_{daily,s}) \end{aligned} \qquad (1) $$

**3. Estimasi Momen Statistik ($\mu$ dan $\sigma$):**
Dari distribusi imbal hasil harian tersebut, kita mengekstrak dua momen statistik utama sebagai representasi fundamental aset:
*   **Ekspektasi Imbal Hasil ($\mu$):** Rata-rata aritmatika dari imbal hasil harian.
$$\mu = \frac{\sum_{i=0}^N r_{daily,t}}{N}$$
*   **Volatilitas ($\sigma$):** Deviasi standar dari imbal hasil harian, yang mengukur dispersi atau risiko ketidakpastian harga.
$$\sigma = $$

**4. Skalasi Tahunan (*Annualization*):**
Untuk keperluan pemodelan investasi jangka panjang, parameter harian harus diskalakan ke basis tahunan (dengan asumsi 252 hari perdagangan). Skalasi ini dilakukan sebagai berikut:
$$ \mu_{annual} = \mu_{daily} \times 252 \qquad (2) $$
$$ \sigma_{annual} = \sigma_{daily} \times \sqrt{252} \qquad (3) $$

Melalui *pipeline* ini, kita mendapatkan parameter $\mu_i$ dan $\sigma_i$ tahunan yang akan menjadi input bagi konstruksi Hamiltonian pada Bab 2, memungkinkan sirkuit kuantum untuk memproses data finansial dunia nyata dalam representasi energi sistem fisik.

## 2. Modern Portfolio Theory (MPT): Kerangka Dasar Markowitz

Teori Portofolio Modern (*Modern Portfolio Theory* atau MPT) yang diperkenalkan oleh Harry Markowitz pada tahun 1952 merupakan landasan matematis pertama yang mengkuantifikasi hubungan antara risiko dan imbal hasil (*risk-return tradeoff*). Prinsip utama dari teori ini adalah diversifikasi, di mana risiko keseluruhan dari suatu portofolio tidak hanya ditentukan oleh variansi individual masing-masing aset, melainkan juga oleh kovariansi atau korelasi antar aset tersebut. Dalam pandangan Markowitz, investor yang rasional akan selalu berusaha untuk berada pada garis *Efficient Frontier*, yaitu himpunan portofolio yang menawarkan imbal hasil maksimum untuk tingkat risiko tertentu, atau risiko minimum untuk tingkat imbal hasil tertentu. Hal ini mengubah paradigma pemilihan aset dari yang sebelumnya hanya fokus pada performa individual menjadi analisis sistemik terhadap kontribusi setiap aset dalam struktur portofolio kolektif.

Secara matematis, masalah pemilihan aset ini dirumuskan sebagai pencarian titik ekstrem dari fungsi utilitas yang merepresentasikan *trade-off* antara risiko dan ekspektasi imbal hasil. Untuk membangun fungsi objektif optimasi ini, kita dapat menurunkannya melalui beberapa tahapan formal berikut:

**1. Definisi Variabel Keadaan**
Pertama, kita definisikan sebuah sistem yang terdiri dari $N$ aset kandidat. Status setiap aset direpresentasikan oleh variabel biner $x_i \in \{0, 1\}$, yang menunjukkan apakah aset $i$ dipilih ($x_i=1$) atau tidak ($x_i=0$) dalam portofolio. Kita juga mendefinisikan ekspektasi imbal hasil individual sebagai $\mu_i$, dan elemen matriks kovariansi sebagai $\sigma_{ij}$, yang mengkuantifikasi korelasi pergerakan harga antara aset $i$ dan $j$.

**2. Formulasi Ekspektasi Imbal Hasil**
Imbal hasil keseluruhan dari portofolio, $E[R_p]$, merupakan superposisi linear dari ekspektasi imbal hasil masing-masing aset yang berpartisipasi. Secara matematis, ini dirumuskan sebagai rata-rata tertimbang:
$$ E[R_p] = \sum_{i=1}^{N} x_i \mu_i \qquad (4) $$

**3. Formulasi Risiko (Variansi Portofolio)**
Berbeda dengan imbal hasil yang bersifat linear, risiko sistemik dari portofolio ($\sigma_p^2$) memiliki sifat kuadratik. Hal ini disebabkan karena risiko total tidak hanya terakumulasi dari variansi masing-masing aset secara independen, melainkan sangat bergantung pada interaksi atau korelasi silang (kovariansi) antar aset penyusunnya:
$$ \sigma_p^2 = \sum_{i=1}^{N} \sum_{j=1}^{N} x_i x_j \sigma_{ij} \qquad (5) $$

**4. Konstruksi Fungsi Objektif (Fungsi Utilitas)**
Tujuan rasional dari seorang investor adalah meminimalkan eksposur terhadap risiko sekaligus memaksimalkan akumulasi imbal hasil. Dalam kerangka optimasi matematis, kedua tujuan yang saling bertolak belakang ini dikonsolidasikan ke dalam satu metrik tunggal yang dikenal sebagai Fungsi Utilitas Kuadrat. Secara konseptual, kita mencari kondisi minimum dari relasi: $\min (\text{Risiko} - \text{Imbal Hasil})$.

Dengan mengintroduksi parameter $\gamma$ sebagai koefisien *risk aversion* (derajat ketidaksukaan terhadap risiko yang berfungsi sebagai pengali faktor skala), persamaan utilitas tersebut diformalkan menjadi:
$$ O(x) = \gamma \cdot (\sigma_p^2) - (E[R_p]) \qquad (6) $$

**5. Persamaan Akhir Markowitz**
Substitusi Persamaan (4) dan (5) ke dalam Persamaan (6) menghasilkan bentuk analitik eksplisit dari fungsi objektif Markowitz:
$$ O(x) = \gamma \left( \sum_{i=1}^{N} \sum_{j=1}^{N} x_i x_j \sigma_{ij} \right) - \sum_{i=1}^{N} x_i \mu_i \qquad (7) $$

Atau dalam notasi tensor yang lebih padat:
$$ O(x) = \gamma \sum_{i,j}^N \sigma_{ij} x_i x_j - \sum_i^N \mu_i x_i \qquad (8) $$

Dalam Persamaan (8), suku pertama merepresentasikan total variansi portofolio. Semakin besar nilai $\gamma$, semakin sensitif investor terhadap risiko, sehingga algoritma optimasi akan memprioritaskan penekanan suku kuadratik ini sekecil mungkin. Sebaliknya, kehadiran tanda negatif pada suku kedua memastikan bahwa proses minimalisasi terhadap fungsi $O(x)$ secara inheren akan berusaha memaksimalkan akumulasi imbal hasil $\mu_i$. 

Justifikasi fisik dari formulasi ini sangat eksplisit: fungsi objektif tersebut memiliki topologi matematis yang identik dengan energi potensial dalam mekanika statistik, di mana interaksi antar partikel (kovariansi $\sigma_{ij}$) dan pengaruh medan eksternal lokal (imbal hasil $\mu_i$) menentukan konfigurasi sistem yang paling stabil. Dengan demikian, meminimalkan fungsi $O(x)$ secara langsung ekuivalen dengan mencari susunan aset yang merepresentasikan keadaan energi dasar (*ground state*), menjadikan portofolio sangat tangguh dalam menghadapi ketidakpastian pasar.

## 3. Metrik Finansial: Log-Returns dan Sharpe Ratio

Dalam pemodelan keuangan kuantitatif, terdapat dua metodologi utama untuk mengkuantifikasi imbal hasil (*return*) aset: *Simple Return* ($R_s$) dan *Log Return* ($r_t$). *Simple Return* mengukur perubahan persentase harga secara linear, sedangkan *Log Return* mengukur tingkat pertumbuhan kontinu. Secara matematis, keduanya didefinisikan sebagai:

$$ R_s = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1 \qquad (9) $$
$$ r_t = \ln\left(\frac{P_t}{P_{t-1}}\right) \qquad (10) $$

Pemilihan *Log-Return* (Persamaan 10) jauh lebih disukai dalam ranah ekonofisika karena sifat aditifnya terhadap waktu. Properti aditif ini memungkinkan kita untuk menjumlahkan imbal hasil dari beberapa periode secara linear, yang secara konseptual identik dengan penjumlahan tingkat energi dalam mekanika statistik. Untuk memahami perbedaan fundamental antara keduanya, kita perlu meninjau perbandingannya dalam tiga skenario pergerakan harga berikut:

### A. Skenario 1: Kenaikan Drastis ($P_t \gg P_{t-1}$)
Ketika harga aset melonjak tinggi, perbedaan nilai antara keduanya menjadi sangat lebar. Sifat fungsi logaritma yang cenderung "mengerem" pertumbuhan angka besar menyebabkan nilai $r_t$ akan selalu lebih kecil daripada $R_s$ ($R_s > r_t$). Sebagai contoh, jika harga naik dari 100 ke 600 (+500%), maka $R_s = 5,0$, sedangkan $r_t = \ln(6) \approx 1,79$. Dalam hal ini, *Log-Return* meremehkan (*understate*) keuntungan besar jika dibandingkan dengan pertumbuhan linear.

### B. Skenario 2: Penurunan Drastis ($P_t \ll P_{t-1}$)
Perbedaan sifat matematis yang paling mencolok terlihat pada batas bawahnya. *Simple Return* dibatasi secara vertikal pada angka -1 (-100%), karena harga aset tidak mungkin turun di bawah nol. Sebaliknya, *Log Return* tidak memiliki batas bawah; jika $P_t$ mendekati nol, maka $r_t$ akan menuju negatif tak hingga ($-\infty$). Hal ini memberikan gambaran yang lebih simetris dan ekstrem untuk kerugian total dalam permodelan risiko kuantum.

### C. Skenario 3: Perubahan Kecil ($P_t \approx P_{t-1}$)
Ketika rasio harga $\frac{P_t}{P_{t-1}}$ mendekati 1, nilai $r_t$ akan sangat mendekati $R_s$ ($R_s \approx r_t$). Secara matematis, hal ini didasarkan pada ekspansi deret Taylor untuk $\ln(1+x) \approx x$ ketika $x \to 0$. Untuk fluktuasi harian yang kecil (di bawah 1%), perbedaan antara kedua metrik ini biasanya tidak signifikan secara praktis.

Ringkasan perbandingan sifat matematis kedua metrik disajikan pada Tabel 1:

| Fitur | Simple Return ($R_s$) | Log Return ($r_t$) |
| :--- | :--- | :--- |
| **Batas Bawah** | -1 (-100%) | $-\infty$ |
| **Batas Atas** | $+\infty$ | $+\infty$ |
| **Sifat Agregasi** | *Cross-sectional* (Portofolio) | *Time-series* (Akumulasi Waktu) |
| **Sifat Matematis** | Linear | Non-linear (Logaritmik) |

Secara visual, kurva *Log-Return* akan selalu berada di bawah garis *Simple Return* (kecuali pada titik nol), mengikuti properti ketidaksamaan logaritmik $\ln(x) \leq x-1$ untuk seluruh $x > 0$.

### D. Analisis Efisiensi: Sharpe Ratio
Setelah imbal hasil dihitung, kita memerlukan metrik untuk mengevaluasi efisiensi portofolio relatif terhadap risiko yang diambil. *Sharpe Ratio* ($S_p$) merupakan standar industri yang mengukur imbal hasil berlebih (*excess return*) per unit volatilitas. Metrik ini memberikan indikasi apakah keuntungan yang diperoleh merupakan kompensasi yang adekuat atas risiko yang ditanggung oleh investor. Secara formal, *Sharpe Ratio* didefinisikan sebagai:

$$ S_p = \frac{R_p - R_f}{\sigma_p} \qquad (11) $$

Di mana komponen-komponennya adalah:
* **$R_p$ (*Portfolio Return*):** Tingkat pengembalian yang dihasilkan oleh portofolio.
* **$R_f$ (*Risk-Free Rate*):** Tingkat pengembalian bebas risiko (misal: obligasi pemerintah).
* **$\sigma_p$ (*Standard Deviation*):** Volatilitas atau deviasi standar dari imbal hasil portofolio.

Untuk memahami bagaimana *Sharpe Ratio* berperan dalam berbagai kondisi pasar, kita meninjau interaksi antara pembilang (imbal hasil berlebih) dan penyebut (volatilitas) melalui enam skenario berikut:

1. **Skenario Terburuk ($R_p \ll R_f, \sigma_p \uparrow \uparrow$):**
   Jika imbal hasil berada di bawah aset bebas risiko dengan volatilitas tinggi, pembilang bernilai negatif besar sementara penyebut besar.
   $$ S_p = \frac{\downarrow \text{negatif besar}}{\uparrow \text{besar}} < 0 $$
   Hasilnya adalah *Sharpe Ratio* negatif, menunjukkan investasi yang sangat tidak efisien dibandingkan instrumen aman ($R_f$).

2. **Skenario Tidak Efisien ($R_p \approx R_f, \sigma_p \uparrow \uparrow$):**
   Ketika imbal hasil hanya sedikit berbeda dari $R_f$ namun memiliki risiko sangat besar, pembilang mendekati nol.
   $$ S_p = \frac{\approx 0}{\uparrow \text{besar}} \approx 0 $$
   Nilai $S_p$ mendekati nol mengindikasikan bahwa risiko yang diambil tidak menghasilkan kompensasi keuntungan yang berarti.

3. **Skenario Sangat Negatif ($R_p \ll R_f, \sigma_p \to 0$):**
   Jika portofolio secara konsisten memberikan hasil di bawah $R_f$ dengan volatilitas yang sangat rendah (kepastian tinggi dalam kerugian relatif terhadap $R_f$).
   $$ S_p = \frac{\downarrow \text{negatif besar}}{\epsilon \to 0} \to -\infty $$
   Penyebut yang mendekati nol membuat $S_p$ menjadi sangat negatif secara ekstrem.

4. **Skenario Volatil ($R_p \uparrow \uparrow, \sigma_p \uparrow \uparrow$):**
   Meskipun imbal hasil sangat besar, tingginya volatilitas akan "menekan" nilai efisiensi portofolio.
   $$ S_p = \frac{\uparrow \text{positif besar}}{\uparrow \text{besar}} \approx \text{moderat} $$
   Keuntungan besar ini dianggap kurang berkualitas karena fluktuasi yang ekstrem.

5. **Skenario Ideal (*Holy Grail*) ($R_p \uparrow \uparrow, \sigma_p \to 0$):**
   Pembagian angka imbal hasil yang besar dengan penyebut yang mendekati nol (risiko hampir tidak ada).
   $$ S_p = \frac{\uparrow \text{positif besar}}{\epsilon \to 0} \to +\infty $$
   Ini merepresentasikan portofolio "Cawan Suci" dengan keuntungan maksimal dan risiko minimal.

6. **Skenario Kesetimbangan ($R_p = R_f = \sigma_p$):**
   Jika seluruh parameter bernilai sama, maka imbal hasil berlebih (*excess return*) adalah nol.
   $$ S_p = \frac{R_p - R_f}{\sigma_p} = \frac{0}{R_p} = 0 $$
   Artinya, investasi hanya menyamai aset bebas risiko tanpa memberikan premi atas risiko yang diambil.

Secara logis, pembilang ($R_p - R_f$) menentukan arah atau kualitas imbal hasil (positif/negatif), sedangkan penyebut ($\sigma_p$) menentukan besaran atau magnitudo dari efisiensi tersebut. Dalam konteks algoritma VQE yang kita kembangkan, *Sharpe Ratio* agregat dari seluruh aset kandidat digunakan sebagai sinyal input untuk mengkalibrasi parameter psikologi pasar secara otomatis melalui fungsi *Sigmoid* pada bab berikutnya.

## 4. Risk Aversion Endogen: Pemodelan Psikologi Investor

Salah satu tantangan utama dalam implementasi praktis MPT adalah penentuan parameter *risk aversion* $\gamma$, yang menentukan keseimbangan antara keamanan dan keuntungan. Model tradisional seringkali memperlakukan $\gamma$ sebagai konstanta statis yang dipilih secara subjektif, namun pada kenyataannya, selera risiko investor bersifat dinamis dan sangat dipengaruhi oleh kondisi pasar saat itu. Dengan memperkenalkan konsep *Endogenous Risk Aversion*, kita memungkinkan sistem untuk menyesuaikan nafsu investasinya secara mandiri berdasarkan rasio *Signal-to-Noise* ($\mu/\sigma$) dari data historis. Pendekatan ini menggunakan fungsi aktivasi *Sigmoid* (logistik) untuk memetakan input pasar yang tak terbatas menjadi parameter bobot yang terikat dalam rentang $(0, 1)$.

Penggunaan fungsi *Sigmoid* ini memiliki dasar psikologis yang kuat, yaitu mewakili efek saturasi dalam pengambilan keputusan manusia. Ketika imbal hasil yang diharapkan meningkat jauh melampaui risiko, selera investasi akan tumbuh, namun pada titik tertentu akan mencapai ambang jenuh di mana tambahan keuntungan tidak lagi secara signifikan meningkatkan keberanian investor untuk mengambil risiko lebih tinggi. Secara formal, parameter selera risiko endogen $\lambda$ dirumuskan sebagai:

$$ \lambda(\mu, \sigma) = \frac{1}{1 + e^{-(\mu/\sigma)}} \qquad (12) $$

Untuk memahami dinamika pengambilan keputusan yang dihasilkan oleh Persamaan (12), kita perlu meninjau tiga skenario batas berdasarkan rasio *Signal-to-Noise* ($\mu/\sigma$) sebagai berikut:

1. **Pasar Euphoria ($\mu \gg \sigma$):**
   Ketika ekspektasi imbal hasil jauh melampaui tingkat volatilitas, rasio $\mu/\sigma$ akan menjadi angka positif yang sangat besar (menuju $+\infty$). Secara matematis, suku eksponensial $e^{-(\mu/\sigma)}$ akan meluruh mendekati **0**. Akibatnya, nilai $\lambda$ akan berkonvergensi menuju **1**, yang menandakan bahwa sistem secara agresif memprioritaskan maksimalisasi keuntungan dengan mengabaikan variabel risiko.

2. **Pasar Netral atau Stagnan ($\sigma \gg \mu$):**
   Jika volatilitas mendominasi pasar sementara imbal hasil berada pada level minimal (mendekati 0), maka rasio $\mu/\sigma$ akan mengecil menuju **0**. Dalam kondisi ini, suku eksponensial menjadi $e^0 = 1$, sehingga nilai $\lambda$ akan berada pada titik kesetimbangan **0,5**. Nilai ini merepresentasikan sikap netral di mana risiko dan imbal hasil diberi bobot yang setara. Perlu dicatat bahwa jika pasar mengalami tren negatif yang ekstrem ($-\mu \gg \sigma$), maka $\lambda$ akan meluruh menuju **0**, memaksa sistem untuk beralih sepenuhnya ke strategi defensif.

3. **Pasar Seimbang ($\mu \approx \sigma$):**
   Pada kondisi di mana imbal hasil yang diharapkan setara dengan tingkat risiko aset, rasio $\mu/\sigma$ bernilai **1**. Persamaan (12) kemudian menghasilkan nilai $\lambda = (1 + e^{-1})^{-1} \approx \mathbf{0,731}$. Angka ini menunjukkan bahwa dalam kondisi pasar yang sehat dan terukur, sistem memiliki kecenderungan moderat untuk sedikit lebih condong mengejar imbal hasil dibandingkan sekadar meminimalkan risiko.

Ringkasan perilaku parameter $\lambda$ terhadap berbagai kondisi pasar disajikan pada Tabel 1:

| Kondisi Pasar | Rasio $\mu/\sigma$ | Nilai $\lambda$ | Perilaku Algoritma |
| :--- | :--- | :--- | :--- |
| **Euphoria** | Menuju $+\infty$ | $\approx 1,00$ | Agresif (Fokus Return) |
| **Seimbang** | $1$ | $\approx 0,73$ | Moderat (Optimasi Campuran) |
| **Netral** | $0$ | $\approx 0,50$ | Netral (Risk-Balanced) |
| **Panic** | Menuju $-\infty$ | $\approx 0,00$ | Defensif (Fokus Risiko) |

Parameter $\lambda$ ini kemudian bertindak sebagai "termostat" otomatis dalam konstruksi Hamiltonian Ising. Saat pasar berada dalam kondisi euforia, $\lambda \uparrow 1$ mengarahkan algoritma kuantum untuk memprioritaskan aset dengan profitabilitas tertinggi. Sebaliknya, saat pasar mengalami panik atau volatilitas tinggi, $\lambda \downarrow 0$ memaksa sistem untuk memprioritaskan aset dengan variansi terendah guna melindungi nilai portofolio.

## 5. Implementasi Kode: Dari Data ke Parameter Keuangan

Dalam implementasi praktis pada file `GT_Ising_SBR.ipynb`, konsep teoritis mengenai *risk aversion* endogen diterjemahkan ke dalam fungsi `compute_endogenous_lambda`. Proses ini dimulai dengan pengambilan data harga historis menggunakan pustaka `yfinance`, yang kemudian diproses untuk mendapatkan *log-returns* tahunan serta deviasi standar untuk setiap aset kandidat. Dengan melakukan rata-rata metrik tersebut di seluruh aset, kita memperoleh ukuran agregat dari performa pasar relatif terhadap derau (*noise*). Rasio Sharpe agregat ($Z$) ini kemudian menjadi input bagi fungsi eksponensial dalam formula sigmoid, menghasilkan nilai skalar $\lambda$ tunggal yang mengatur seluruh siklus optimasi untuk periode *rebalancing* tersebut.

Selain itu, persiapan matriks informasi dan imbal hasil strategis sangat bergantung pada transformasi pergerakan harga kontinu menjadi *binary states*. Keadaan biner ini (0 untuk kenaikan harga dan 1 untuk penurunan harga) memungkinkan algoritma untuk menangkap dependensi non-linear melalui *Normalized Mutual Information* (NMI). Sintesis dari berbagai metrik finansial ini pada akhirnya membentuk koefisien-koefisien dalam Hamiltonian Ising, khususnya medan lokal ($h_i$) dan kekuatan kopling ($J_{ij}$). Dengan menjembatani data finansial tingkat tinggi dengan operator kuantum tingkat rendah, kita menciptakan alur kerja (*pipeline*) yang tidak hanya kuat secara teoretis tetapi juga dapat diintegrasikan secara koheren dengan implementasi algoritma hibrida kuantum-klasik.
