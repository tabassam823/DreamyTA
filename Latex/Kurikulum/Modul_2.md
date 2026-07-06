# Modul 2: Teori Informasi & Metrik Non-Linier (NMI)

## 1. Urgensi & Konteks Fisika: Ketergantungan Non-Linier dalam Sistem Kompleks

Analisis ketergantungan antar-aset dalam pasar modal merupakan pilar fundamental dalam teori portofolio modern guna memitigasi risiko sistemik. Secara tradisional, koefisien korelasi Pearson digunakan secara luas untuk mengukur hubungan linier antara imbal hasil aset, namun metode ini sering kali gagal menangkap dinamika pasar yang bersifat *non-trivial*. Sistem keuangan, serupa dengan sistem fisis kompleks lainnya, sering kali menunjukkan fenomena *fat-tail distribution* dan ketergantungan non-linier yang tidak dapat direpresentasikan melalui statistik orde kedua sederhana. Oleh karena itu, diperlukan sebuah metrik yang lebih robust dan mampu mengakomodasi seluruh spektrum informasi, baik yang bersifat linier maupun non-linier, guna menghasilkan estimasi risiko yang lebih akurat.

Pendekatan *Information Theory* yang diperkenalkan oleh Claude Shannon menawarkan kerangka kerja alternatif untuk memahami interaksi antar-variabel melalui konsep entropi. Dalam konteks ekonofisika, pasar saham dipandang sebagai sistem stokastik di mana setiap pergerakan harga membawa sejumlah informasi tertentu yang dapat dikuantifikasi dalam satuan *bits*. Penggunaan *Mutual Information* (MI) memungkinkan peneliti untuk mengidentifikasi redundansi informasi dan dependensi struktural yang sering kali tersembunyi dari analisis korelasi klasik. Dengan mengintegrasikan metrik berbasis informasi ini ke dalam formulasi portofolio, sistem dapat mengantisipasi risiko penularan (*contagion risk*) dengan lebih baik, terutama pada periode volatilitas tinggi di mana hubungan linier antar-aset cenderung meluruh atau berubah secara drastis.

## 2. Entropi Shannon: Ukuran Ketidakpastian Informasional

### 2.1. Penurunan Formalisme Informasi Shannon
Entropi Shannon ($H$) memiliki akar konseptual yang identik dengan entropi Boltzmann dalam mekanika statistik, di mana keduanya berfungsi sebagai ukuran derajat ketidakteraturan atau ketidakpastian dalam suatu sistem. Dalam *Information Theory*, satuan dasar informasi didefinisikan sebagai *bit*, yang merepresentasikan jumlah informasi yang diperoleh ketika ruang kemungkinan tereduksi menjadi separuhnya (probabilitas $1/2$). Secara fundamental, jika sebuah observasi memotong ruang kemungkinan sebesar $1/p$, maka hubungan antara jumlah bit informasi ($I$) dan probabilitas ($p$) dapat dinyatakan melalui hubungan eksponensial $2^I = 1/p$. Dengan menerapkan logaritma basis dua, kita memperoleh besaran *Information Shannon* atau *Surprisal* ($I$) untuk satu kejadian tunggal:

$$I(x) = \log_2\left(\frac{1}{p(x)}\right) = -\log_2 p(x) \qquad(1)$$

Persamaan (1) memberikan justifikasi fisis bahwa kejadian dengan probabilitas rendah (kejutan tinggi) memberikan kandungan informasi yang lebih besar bagi pengamat dibandingkan kejadian yang sudah umum terjadi. Untuk menguantifikasi rata-rata informasi dari seluruh ruang sampel variabel acak $X$, kita menggunakan prinsip *Expected Value* atau nilai harapan ($E$) dari fungsi informasi tersebut. Entropi ($H$) didefinisikan sebagai nilai harapan dari informasi Shannon, yang secara matematis dirumuskan sebagai jumlahan terbobot dari informasi setiap kemungkinan status dikalikan dengan probabilitas kemunculannya:

$$H(X) = E[I(X)] = \sum_{x \in X} p(x) I(x) \qquad(2)$$

Dengan mensubstitusikan Persamaan (1) ke dalam Persamaan (2), kita memperoleh formulasi akhir entropi Shannon yang menjadi standar dalam analisis sistem stokastik dan komputasi kuantum:

$$H(X) = -\sum_{x \in X} p(x) \log_2 p(x) \qquad(3)$$

### 2.2. Studi Kasus: Analisis Stokastik Cuaca Surabaya
Penerapan praktis dari Persamaan (3) dapat diilustrasikan melalui pemodelan prediksi cuaca harian di wilayah Surabaya selama periode pancaroba. Misalkan sebuah sistem cuaca memiliki tiga status *mutually exclusive* dengan probabilitas historis sebagai berikut: cerah ($p_1=0.5$), mendung ($p_2=0.25$), dan hujan ($p_3=0.25$). Berdasarkan perhitungan menggunakan Persamaan (1), informasi yang diperoleh dari masing-masing kondisi adalah $I(\text{cerah}) = 1$ *bit*, sedangkan status mendung dan hujan memberikan kejutan informasional sebesar $I = 2$ *bits*. Hal ini mengonfirmasi bahwa kejadian hujan yang lebih jarang terjadi memberikan "kejutan" data yang lebih signifikan bagi model prediksi dibandingkan kondisi cerah.

Perhitungan entropi total untuk sistem cuaca tersebut dilakukan dengan menjumlahkan kontribusi informasi terbobot dari ketiga status tersebut sesuai dengan kaidah nilai harapan. Hasil kalkulasi memberikan nilai $H(X) = (0.5 \times 1) + (0.25 \times 2) + (0.25 \times 2) = 1.5$ *bits*. Interpretasi fisis dari angka ini menunjukkan bahwa rata-rata ketidakpastian cuaca harian di Surabaya setara dengan hasil dari 1.5 kali pelemparan koin yang adil (*fair coin toss*). Dalam konteks portofolio, besaran entropi ini akan memetakan derajat acak pergerakan harga aset ke dalam sirkuit kuantum, di mana nilai entropi yang lebih tinggi menuntut kompleksitas *ansatz* yang lebih besar untuk mencapai konvergensi energi.

## 3. Mutual Information (MI) & Upper Bound Theorem

### 3.1. Penurunan Matematis Mutual Information (MI)
*Mutual Information* ($I(X;Y)$) merupakan metrik yang mengukur reduksi ketidakpastian pada suatu variabel acak $X$ setelah dilakukannya observasi terhadap variabel acak $Y$. Secara konseptual, jika kita memulai dengan ketidakpastian awal $H(X)$, maka sisa ketidakpastian yang masih ada setelah mengetahui variabel $Y$ didefinisikan sebagai *Conditional Entropy* atau entropi bersyarat $H(X|Y)$. Selisih antara ketidakpastian awal dengan ketidakpastian sisa inilah yang merepresentasikan jumlah informasi yang dibagikan antar-kedua variabel tersebut. Formulasi dasar MI dinyatakan sebagai berikut:

$$I(X;Y) = H(X) - H(X|Y) \qquad(4)$$

Untuk menurunkan bentuk eksplisit dari Persamaan (4), kita harus mendefinisikan entropi bersyarat sebagai rata-rata entropi $X$ untuk setiap kemungkinan nilai $y$ yang terbobot oleh probabilitas marginal $p(y)$. Secara matematis, formulasi entropi bersyarat tersebut adalah:

$$H(X|Y) = -\sum_{y \in Y} p(y) \sum_{x \in X} p(x|y) \log_2 p(x|y) \qquad(5)$$

Dengan mensubstitusikan Persamaan (3) dan (5) ke dalam Persamaan (4) serta menerapkan sifat logaritma ($\log a - \log b = \log \frac{a}{b}$), kita memperoleh rumus standar MI berbasis distribusi gabungan (*joint distribution*):

$$I(X;Y) = \sum_{x,y} p(x,y) \log_2 \left( \frac{p(x,y)}{p(x)p(y)} \right) \qquad(6)$$

### 3.2. Logika Distribusi: Realita vs. Independensi
Persamaan (6) memberikan perspektif yang sangat fundamental dalam statistik, di mana kita membandingkan dua kondisi probabilitas yang berbeda. Pembilang ($p(x,y)$) merepresentasikan "Realita" atau distribusi gabungan aktual dari data yang menunjukkan seberapa sering dua kejadian muncul bersamaan. Sebaliknya, penyebut ($p(x)p(y)$) merepresentasikan kondisi "Independensi", di mana secara teoritis dua variabel dianggap tidak memiliki hubungan sama sekali sehingga peluang gabungannya hanyalah hasil kali peluang masing-masing.

Melalui rasio di dalam logaritma tersebut, MI bertindak sebagai detektor dependensi yang sangat sensitif. Jika variabel $X$ dan $Y$ bersifat independen sempurna, maka $p(x,y) = p(x)p(y)$, yang menyebabkan rasio bernilai 1 dan hasil logaritma menjadi 0, sehingga nilai MI adalah nol. Namun, jika terdapat keterkaitan sistemik, maka distribusi aktual ($p(x,y)$) akan menyimpang secara signifikan dari asumsi independensi, menghasilkan nilai MI positif yang menunjukkan adanya informasi yang dibagikan. Dalam konteks portofolio, hal ini memungkinkan sirkuit kuantum untuk membedakan antara fluktuasi harga acak dengan korelasi struktural yang bermakna.

### 3.3. Studi Kasus: Dependensi Dua Koin Magnetik
Sebagai ilustrasi numerik, pertimbangkan sistem yang terdiri dari dua koin yang saling berhubungan karena adanya gaya magnetik, sehingga hasil lemparan koin pertama memengaruhi peluang koin kedua. Misalkan koin kedua ($Y$) memiliki probabilitas awal $P(\text{Heads}) = 0.6$ dan $P(\text{Tails}) = 0.4$, yang menghasilkan entropi awal $H(Y) = 0.97$ *bit*. Tanpa informasi dari koin pertama, ketidakpastian kita terhadap koin kedua hampir mencapai nilai maksimum.

Namun, setelah kita mengamati hasil lemparan koin pertama ($X$), ketidakpastian koin kedua berkurang menjadi $H(Y|X) = 0.71$ *bit* karena adanya dependensi fisik antar-koin. Berdasarkan Persamaan (4), jumlah informasi yang dibagikan oleh kedua koin tersebut adalah:

$$I(X;Y) = 0.97 - 0.71 = 0.26 \text{ bit}$$

Nilai **0.26 bit** ini merupakan kuantifikasi dari "kekuatan" hubungan antar-koin tersebut. Dalam sistem portofolio, besaran informasi ini akan menentukan kekuatan interaksi antar-aset dalam Hamiltonian Ising. Semakin besar nilai MI, semakin kuat penalti redundansi yang diberikan, guna memastikan bahwa aset yang dipilih dalam portofolio memiliki profil informasi yang unik dan tidak tumpang tindih.

### 3.4. Upper Bound Theorem & Signifikansi Portofolio
Salah satu sifat fisis yang krusial dari MI adalah kepatuhannya terhadap *Upper Bound Theorem*, yang menyatakan bahwa nilai informasi bersama tidak akan pernah melampaui nilai entropi marginal dari variabel penyusunnya. Hal ini memberikan batasan matematis yang tegas bahwa $I(X_i : X_j) \leq \min(H(X_i), H(X_j))$, yang menjamin bahwa informasi yang dibagikan tidak mungkin lebih besar daripada ketidakpastian variabel itu sendiri. Prinsip ini menjadi fondasi krusial sebelum melakukan proses normalisasi informasi pada tahap selanjutnya, guna memastikan metrik korelasi tetap berada dalam batas-batas fisis yang valid.

## 4. Normalized Mutual Information (NMI) sebagai Skalar Korelasi

### 4.1. Rasionalitas Normalisasi & Batas Atas Informasi
*Normalized Mutual Information* (NMI) merupakan bentuk standardisasi dari *Mutual Information* mentah guna menghasilkan koefisien skalar yang terikat pada rentang $[0, 1]$. Tanpa normalisasi, perbandingan dependensi informasi antara pasangan variabel dengan tingkat entropi yang berbeda akan menjadi bias dan sulit untuk diinterpretasikan secara statistik. Berdasarkan *Upper Bound Theorem*, kita mengetahui bahwa kapasitas maksimum informasi bersama dibatasi oleh entropi terkecil dari variabel yang terlibat. Oleh karena itu, diperlukan suatu faktor pembagi (*normalizer*) yang merepresentasikan total kapasitas informasi sistem guna mengubah satuan *bits* menjadi angka persentase korelasi.

Pemilihan faktor pembagi ini dapat menggunakan berbagai jenis rata-rata entropi marginal, yang masing-masing memberikan karakteristik sensitivitas berbeda terhadap ketimpangan informasi. Dalam implementasi teknis, NMI sangat populer digunakan untuk evaluasi algoritma *clustering*, seleksi fitur (*feature selection*), hingga bioinformatika. Dengan mentransformasikan MI menjadi skalar nirdimensi, peneliti dapat membandingkan struktur data yang berbeda secara objektif, serupa dengan fungsi koefisien korelasi Pearson namun dengan kemampuan menangkap hubungan non-linier.

### 4.2. Variasi Model Normalisasi: Geometrik vs. Aritmatika
Terdapat dua model normalisasi utama yang sering digunakan dalam literatur ekonofisika dan *data science*. Model pertama menggunakan **Rata-Rata Geometrik** (*Geometric Mean*), yang memberikan penalti lebih ketat jika terjadi perbedaan drastis pada magnitudo entropi marginal. Model ini secara matematis konsisten dengan *Cauchy-Schwarz Inequality* dan sering dianggap sebagai "korelasi informasi". Formulasi NMI Geometrik didefinisikan sebagai:

$$NMI_{geom}(X_i, X_j) = \frac{I(X_i : X_j)}{\sqrt{H(X_i)H(X_j)}} \qquad(7)$$

Model kedua menggunakan **Rata-Rata Aritmatika** (*Arithmetic Mean*), yang lebih umum digunakan dalam standar evaluasi *machine learning* (seperti pada *library scikit-learn*). Model ini cenderung lebih stabil dan memberikan hasil yang lebih intuitif untuk perbandingan hasil pengelompokan (*clustering*). Formulasi NMI Aritmatika didefinisikan sebagai:

$$NMI_{arith}(X_i, X_j) = \frac{I(X_i : X_j)}{(H(X_i) + H(X_j)) / 2} \qquad(8)$$

### 4.3. Studi Kasus Numerik: Evaluasi Clustering Jurusan Mahasiswa
Untuk memahami perbedaan kedua model tersebut, bayangkan sebuah kasus evaluasi pengelompokan 6 mahasiswa yang terbagi ke dalam dua jurusan: Fisika ($U=1$) dan Biologi ($U=0$). Data asli (*ground truth*) adalah `[1, 1, 1, 0, 0, 0]`, sedangkan hasil prediksi mesin adalah `[1, 1, 0, 0, 0, 0]`, yang berarti terjadi kesalahan klasifikasi pada satu mahasiswa Fisika. Berdasarkan data tersebut, kita peroleh nilai entropi marginal $H(U) = 1.0$ *bit* dan $H(V) \approx 0.918$ *bit*, dengan nilai MI mentah sebesar $0.19$ *bit*.

Jika kita menerapkan model pada Persamaan (8) (Aritmatika), maka nilai NMI yang diperoleh adalah $0.19 / 0.959 \approx 0.198$. Namun, jika menggunakan model Persamaan (7) (Geometrik), nilainya menjadi $0.19 / \sqrt{1.0 \cdot 0.918} \approx 0.198$. Meskipun dalam kasus dengan entropi seimbang hasilnya serupa, pada kasus dengan ketimpangan besar (misal $H(X)=2.0$ dan $H(Y)=0.5$), model Geometrik akan menghasilkan nilai yang lebih tinggi ($0.40$) dibandingkan model Aritmatika ($0.32$). Hal ini menunjukkan bahwa pemilihan model normalisasi sangat bergantung pada karakteristik data dan tujuan penelitian yang ingin dicapai.

## 5. Integrasi NMI ke dalam Matriks Kovariansi & Hamiltonian Ising

Tahap krusial dalam algoritma *Ising-SBR* adalah penguatan matriks risiko tradisional menggunakan metrik redundansi informasional yang diperoleh dari NMI. Integrasi ini bertujuan untuk menyesuaikan elemen kovariansi empiris ($\sigma_{ij}$) dengan mengalikan faktor amplifikasi berbasis informasi, sehingga risiko sistemik dalam portofolio tidak hanya diukur berdasarkan variansi harga, melainkan juga berdasarkan redundansi pola pergerakan antar-aset. Melalui skema ini, aset yang memiliki ketergantungan non-linier tinggi akan diberikan penalti risiko yang lebih besar, yang secara efektif mencegah pemilihan aset yang terlalu berkorelasi. Formulasi bagi elemen matriks kovariansi yang telah diperkuat ($\tilde{\sigma}_{ij}$) dinyatakan sebagai berikut:

$$\tilde{\sigma}_{ij} = \sigma_{ij} [1 + NMI(i, j)] \qquad(9)$$

Berdasarkan matriks kovariansi yang telah dimodifikasi pada Persamaan (9), koefisien kopling ($J_{ij}$) dalam Hamiltonian Ising dapat diekstraksi untuk memetakan masalah ekonomi ke dalam sistem fisik. Parameter $J_{ij}$ ini mengintegrasikan faktor *risk-aversion* ($\gamma$) dan penalti Lagrange ($\lambda_{pen}$) ke dalam satu koefisien interaksi antar-spin. Dalam representasi fisik ini, interaksi biner dalam model Ising akan secara intrinsik membawa informasi mengenai dependensi non-linier pasar. Formulasi akhir bagi koefisien kopling tersebut didefinisikan sebagai:

$$J_{ij} = \frac{\gamma \tilde{\sigma}_{ij} + 2\lambda_{pen}}{4} \qquad(10)$$

Integrasi NMI melalui Persamaan (10) menjamin bahwa konfigurasi *ground state* yang ditemukan oleh algoritma VQE akan menghasilkan portofolio yang lebih terdiversifikasi secara struktural. Hal ini dikarenakan lanskap energi Hamiltonian telah dimodifikasi sedemikian rupa sehingga status energi rendah (solusi optimal) hanya dapat dicapai dengan meminimalkan redundansi informasi yang tumpang tidih antar-aset terpilih.

## 6. Implementasi Teknis: Algoritma Perhitungan NMI

Implementasi numerik NMI dalam sistem *Ising-SBR* dilakukan secara modular untuk menjamin efisiensi komputasi pada semesta aset yang besar. Langkah pertama dimulai dengan menghitung entropi Shannon individual menggunakan fungsi `calc_shannon_entropy`, di mana distribusi probabilitas biner dihitung berdasarkan frekuensi kemunculan status imbal hasil. Status biner ini diekstraksi dari *log-returns* harian, di mana nilai 1 merepresentasikan penurunan harga dan 0 merepresentasikan kenaikan atau stagnansi harga. Melalui proses ini, volatilitas pasar yang kompleks dipetakan menjadi urutan bit informasi yang siap diolah lebih lanjut. Berikut adalah potongan kode fundamental bagi perhitungan entropi tersebut:

```python
def calc_shannon_entropy(st_A):
    p1 = np.mean(st_A)
    p0 = 1.0 - p1
    H = 0.0
    if p0 > 0: H -= p0 * np.log2(p0)
    if p1 > 0: H -= p1 * np.log2(p1)
    return H
```

Setelah entropi individual diperoleh, fungsi `calc_NMI` dipanggil untuk menghitung korelasi informasional antar-pasangan aset. Algoritma ini pertama-tama menghitung *joint probability distribution* biner melalui matriks kontingensi 2x2 guna mendapatkan nilai *Mutual Information* (MI). Nilai MI tersebut kemudian dinormalisasi menggunakan rata-rata geometrik entropi marginal sesuai dengan batasan teoritis pada Persamaan (7). Integrasi fungsi-fungsi ini memastikan bahwa seluruh parameter interaksi dalam sirkuit kuantum memiliki landasan teori informasi yang rigor. Kode implementasi NMI tersebut adalah sebagai berikut:

```python
def calc_NMI(st_A, st_B):
    I_AB = calc_classical_mutual_information(st_A, st_B)
    H_A = calc_shannon_entropy(st_A)
    H_B = calc_shannon_entropy(st_B)
    if H_A == 0 or H_B == 0:
        return 0.0
    return I_AB / np.sqrt(H_A * H_B)
```

## 7. Analisis Dampak: NMI vs. Pearson dalam Pemilihan Aset

Perbandingan antara efektivitas NMI dan koefisien korelasi Pearson menunjukkan perbedaan fundamental dalam mendiversifikasi portofolio. Korelasi Pearson cenderung hanya mendeteksi hubungan linier yang bersifat eksplisit, yang sering kali tidak memadai untuk memitigasi risiko saat terjadi guncangan pasar non-linier. Sebaliknya, NMI mampu mengidentifikasi redundansi informasi yang lebih dalam, bahkan ketika hubungan linier antar-aset tampak lemah secara statistik. Dengan demikian, penggunaan NMI dalam model portofolio kuantum memberikan perlindungan tambahan terhadap *tail risk* yang tidak terdeteksi oleh statistik kovariansi tradisional.

Integrasi NMI ke dalam Hamiltonian Ising juga berdampak langsung pada efisiensi konvergensi algoritma VQE. Dengan memberikan penalti yang lebih akurat pada aset-aset yang memiliki redundansi tinggi, lanskap energi sistem menjadi lebih terstruktur dengan lembah energi yang lebih curam pada titik optimal yang sebenarnya. Hal ini membantu agen kuantum untuk menavigasi ruang pencarian konfigurasi dengan lebih efektif, sehingga mempercepat proses penemuan *ground state* pada sirkuit kuantum. Pada akhirnya, pemilihan aset berbasis informasi ini menghasilkan portofolio yang lebih tangguh terhadap dinamika pasar yang bersifat asimetris dan kompleks.
