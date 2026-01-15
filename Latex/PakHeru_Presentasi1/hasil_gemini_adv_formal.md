# INTRODUCTION

## Paragraf 1
### 1. Vektor Saham ($X$) - _Kondisi Pasar_

Pasar didefinisikan sebagai kumpulan $m$ saham yang direpresentasikan dalam sebuah vektor $X = (X_{1}, X_{2}, \dots, X_{m})$. Komponen $X_i$ dalam vektor tersebut merupakan nilai kembalian (*return*) dari investasi satu unit modal pada saham ke-$i$, bukan merupakan harga nominal saham. Sebagai contoh, apabila investasi senilai \$1 pada suatu saham berkembang menjadi \$1,10, maka nilai $X_i$ adalah 1,10; sebaliknya, apabila nilai investasi tersebut turun menjadi \$0,90, maka $X_i$ bernilai 0,90. Variabel $X_i$ diasumsikan bersifat non-negatif ($X_i \ge 0$), yang mengimplikasikan bahwa kerugian investasi dibatasi sebesar modal yang diinvestasikan sehingga nilai investasi tidak dapat menjadi negatif.

Vektor $X$ ditentukan berdasarkan fungsi distribusi bersama (*joint distribution function*) $F(x)$ yang diasumsikan telah diketahui. Penggunaan distribusi bersama ini menunjukkan bahwa kondisi pasar bersifat stokastik dan terdapat korelasi antar-saham, di mana fluktuasi nilai satu saham dapat memengaruhi probabilitas perubahan nilai saham lainnya.

Strategi investasi dikendalikan oleh investor melalui vektor portofolio $b = (b_{1}, \dots, b_{m})$, yang merupakan variabel keputusan dalam model ini. Komponen $b_i$ merepresentasikan proporsi kekayaan yang dialokasikan pada tiap saham ke-$i$. Vektor $b$ harus memenuhi batasan dalam himpunan $B$, yakni alokasi modal tidak diperbolehkan bernilai negatif ($b_i \ge 0$) guna menghindari praktik *short selling*, serta total seluruh proporsi alokasi modal harus bernilai tepat 1 ($\sum b_i = 1$).

Hasil akhir atau imbal hasil (*payoff*) dari strategi investasi terhadap kondisi pasar dinyatakan sebagai modal acak $S$. Modal akhir ini didefinisikan sebagai hasil perkalian titik (*dot product*) antara vektor strategi $b$ dan vektor pasar $X$, yaitu $S = \sum b_i X_i = b^t X$. Secara konseptual, $S$ merupakan rata-rata tertimbang dari kinerja seluruh saham berdasarkan bobot alokasi yang telah ditentukan. Mengingat vektor pasar $X$ bersifat acak, maka modal akhir $S$ juga merupakan variabel acak. Secara keseluruhan, model ini dapat dipandang sebagai sebuah sistem di mana strategi berupa vektor bobot $b$ dipilih, kondisi pasar $X$ ditentukan secara stokastik, dan hasil akhir investasi diperoleh melalui perhitungan $S = b^t X$.

---

## Paragraf 2
### 1. Teori Permainan dan Fungsi Imbal Hasil (*Payoff*)

Skenario investasi dalam model ini dikembangkan menjadi sebuah kerangka kompetisi melalui implementasi teori permainan, khususnya konsep permainan dua orang jumlah-nol (*two-person zero-sum game*). Dalam skenario ini, dua investor (Pemain 1 dan Pemain 2) diasumsikan beradu strategi di pasar yang sama dengan tujuan untuk mengungguli satu sama lain. Inti dari permainan ini dinyatakan dalam fungsi imbal hasil (*payoff function*) $E\phi(S_1/S_2)$, di mana kriteria kemenangan tidak hanya didasarkan pada akumulasi kekayaan secara absolut, melainkan pada keunggulan relatif terhadap lawan.

Skor dalam permainan ini ditentukan oleh rasio modal akhir antara Pemain 1 ($S_1$) dan Pemain 2 ($S_2$). Apabila nilai rasio $S_1/S_2$ lebih besar dari satu, maka Pemain 1 dianggap menang. Fungsi $\phi$ didefinisikan sebagai fungsi yang tidak menurun (*non-decreasing* atau monoton naik), yang mengimplikasikan bahwa skor akan meningkat seiring dengan bertambahnya rasio kekayaan terhadap lawan. Karena kondisi pasar bersifat stokastik dengan vektor pasar $X$ yang ditarik dari distribusi $F$, maka evaluasi dilakukan terhadap nilai harapan (*expectation*) dari fungsi skor tersebut.

### 2. Randomisasi yang Adil dan Solusi Universal

Strategi optimal dalam teori permainan sering kali melibatkan elemen acak (*mixed strategy*) guna menghindari pola yang dapat diprediksi oleh lawan. Dalam konteks ini, diperkenalkan terminologi randomisasi yang adil (*fair randomization*) terhadap modal awal, yang direpresentasikan dengan notasi $\tilde{S}_1$ dan $\tilde{S}_2$. Sebelum melakukan alokasi aset pada pasar saham, pemain diperkenankan untuk melakukan modifikasi modal awal melalui taruhan yang adil (*fair gamble*), di mana ekspektasi modal tetap terjaga namun memberikan variasi pada nilai awal.

Paper ini mengajukan hipotesis utama bahwa terdapat sebuah solusi universal atau strategi dominan yang disebut sebagai portofolio log-optimal ($b^*$). Strategi ini terbukti mampu mengalahkan atau setidaknya mengimbangi lawan dalam berbagai kriteria fungsi imbal hasil, selama fungsi $\phi$ bersifat monoton naik. Secara matematis, portofolio log-optimal didefinisikan sebagai strategi yang memaksimalkan ekspektasi logaritma dari kekayaan:

$$b^* = \text{arg max}_b \ E[\ln(b^t X)]$$

Tesis ini menegaskan bahwa penggunaan kriteria laju pertumbuhan logaritmik merupakan strategi yang paling tangguh (*robust*) dalam permainan investasi kompetitif, melampaui pendekatan teori portofolio modern konvensional yang cenderung hanya berfokus pada keseimbangan risiko dan imbal hasil secara individual.

---
---

## Paragraf 3-4 (Persamaan 1.1)

### 1. Definisi Strategi dan Persamaan Imbal Hasil Formal

Konfigurasi formal dari kompetisi antara dua pemain (Pemain 1 dan Pemain 2) dinyatakan melalui Persamaan (1.1). Strategi dari setiap pemain $i$ didefinisikan melalui dua tahapan utama. Pertama, dilakukan randomisasi awal di mana setiap pemain memulai dengan satu unit modal yang kemudian ditukarkan dengan variabel acak $W_i$ dari distribusi probabilitas $G_i(w)$. Distribusi ini harus memenuhi batasan keadilan (*fairness constraint*), yaitu nilai ekspektasi $E[W_i] \le 1$ dan $W_i \ge 0$. Kedua, setelah perolehan modal acak $W_i$, alokasi portofolio dilakukan menggunakan vektor $b_i$.

Persamaan (1.1) merepresentasikan nilai harapan dari fungsi imbal hasil sebagai berikut:
$$E \phi\left(\frac{W_{1}b_{1}^{\prime}X}{W_{2}b_{2}^{\prime}X}\right) = \iiint \phi\left(\frac{w_{1}b_{1}^{\prime}x}{w_{2}b_{2}^{\prime}x}\right) dG_{1}(w_{1}) dG_{2}(w_{2}) dF(x)$$

Dalam modal akhir ini, komponen $b_i' X$ merupakan hasil perkalian titik yang menunjukkan performa portofolio saham, sementara $W_i$ berperan sebagai pengali dari taruhan awal. Perhitungan ekspektasi dilakukan melalui integral lipat tiga yang mencakup ketidakpastian strategi pemain ($dG_1$ dan $dG_2$) serta ketidakpastian pasar ($dF$). Secara konseptual, persamaan ini menjumlahkan seluruh kemungkinan hasil skor $\phi$ untuk setiap kombinasi keadaan modal dan kondisi pasar yang dikalikan dengan probabilitas kejadiannya.

### 2. Nilai Permainan dan Konsep Minimax

Tujuan dari permainan ini didefinisikan sebagai masalah minimax (titik pelana), sebagaimana tertuang dalam Persamaan (1.2):
$$v = \sup_{b_1, G_1} \inf_{b_2, G_2} E[\dots]$$

Dalam kerangka ini, Pemain 1 berupaya untuk memaksimalkan skor rata-rata, sementara Pemain 2 diasumsikan akan memilih strategi yang meminimalkan skor tersebut guna mencapai keseimbangan. Struktur matematika ini memiliki kesamaan dengan mekanisme dalam mekanika statistik atau termodinamika, di mana dicari keadaan ekuilibrium makroskopis yang stabil melalui optimasi variabel-variabel yang berlawanan. Implementasi strategi campuran (*mixed strategy*) melalui randomisasi awal dianggap krusial untuk memenuhi sifat konveksitas dalam optimasi ini.

---
---

## Paragraf 5
### 1. Universalitas Model dan Representasi Berbagai Tujuan Investasi

Model yang diajukan menunjukkan tingkat universalitas yang tinggi, di mana bentuk matematis $E \phi(\tilde{S}_1 / \tilde{S}_2)$ dapat merepresentasikan berbagai jenis tujuan investasi kompetitif. Berbagai kasus tujuan investasi dapat diklasifikasikan berdasarkan bentuk fungsi $\phi$ yang digunakan. Sebagai contoh, probabilitas kemenangan murni $P(\tilde{S}_{1}>\tilde{S}_{2})$ direpresentasikan oleh fungsi tangga Heaviside, sedangkan ekspektasi rasio linear $E[\tilde{S}_{1}/\tilde{S}_{2}]$ menggunakan fungsi $\phi(x) = x$. 

Lebih lanjut, tujuan yang lebih agresif dapat dimodelkan melalui ekspektasi eksponensial $E[e^{\tilde{S}_{1}/\tilde{S}_{2}}]$, sementara maksimisasi laju pertumbuhan jangka panjang atau kriteria Kelly diakomodasi melalui ekspektasi logaritmik $E[\ln(\tilde{S}_{1}/\tilde{S}_{2})]$. Selain itu, model ini juga mencakup aspek pangsa pasar (*market share*) melalui fungsi $\phi = S_1/(S_1+S_2)$ dan kepuasan terukur (*truncated gain*) untuk memodelkan sifat saturasi utilitas.

### 2. Generalitas Teorema dan Hubungan Probabilitas-Ekspektasi

Koneksi dengan literatur sebelumnya menegaskan bahwa probabilitas kemenangan merupakan kasus khusus dari fungsi indikator dalam kerangka ekspektasi. Penegasan ini membuktikan bahwa teorema yang diturunkan dalam paper ini berlaku untuk seluruh spektrum kriteria kemenangan selama fungsi imbal hasil bersifat monoton naik. Hal ini mengimplikasikan bahwa strategi yang dikembangkan bersifat robust terhadap berbagai preferensi investor dalam mengungguli kekayaan lawan.

---
---

## Paragraf 6 - selesai
### 1. Sistematika Pembuktian dan Peta Jalan Penelitian

Pembuktian hipotesis utama dalam paper ini disusun secara sistematis melalui beberapa tahapan yang terbagi dalam bagian-bagian logis dari §2 hingga §6. Tahap awal (§2) dimulai dengan analisis permainan primitif (*primitive $\phi$-game*) untuk mengisolasi masalah matematika murni tanpa keterlibatan pasar saham. Pada tahap ini, fokus utama adalah pada pemilihan distribusi probabilitas yang memenuhi syarat keadilan.

Tahap berikutnya (§3) diarahkan untuk menetapkan ekuivalensi matematika antara maksimisasi logaritma dan pertidaksamaan linear dalam keluarga konveks. Hasil dari kedua bagian tersebut kemudian disatukan pada §4 untuk membuktikan faktorisasi solusi, di mana strategi optimal terbagi menjadi komponen permainan ($W^*$) yang bergantung pada $\phi$ dan komponen investasi ($b^*$) yang bersifat universal (log-optimal). Bagian akhir penelitian (§5 dan §6) memperluas temuan tersebut ke dalam model dinamis multi-tahap untuk memastikan keberlakuan strategi dalam jangka panjang. Kerangka kerja ini mengintegrasikan berbagai pemikiran dari tokoh-tokoh besar dalam bidang matematika dan ekonomi guna memberikan solusi yang komprehensif terhadap perdebatan mengenai strategi investasi kompetitif.

---
---
---
# Pure Optimal Strategies for the Primitive $\phi$-Game

## 2.1. Definisi Permainan Primitif (*Primitive $\phi$-Game*)

Bagian kedua ini didedikasikan untuk analisis strategi optimal murni dalam kerangka permainan primitif. Permainan primitif didefinisikan sebagai bentuk paling sederhana dari konflik antara dua investor yang dikonstruksi secara abstrak guna memfasilitasi analisis matematis. Dalam model ini, terdapat beberapa komponen utama yang membedakannya dari skenario pasar saham konvensional. Pertama, medan permainan ditetapkan tanpa adanya keterlibatan pasar saham maupun pemilihan portofolio, sehingga fokus analisis dialihkan sepenuhnya pada pemilihan distribusi probabilitas. Kedua, aturan permainan mengharuskan Pemain 1 dan Pemain 2 untuk memilih variabel acak independen, masing-masing direpresentasikan sebagai $W_1$ dan $W_2$, yang berfungsi sebagai instrumen strategi.

Ketiga, variabel acak yang dipilih harus memenuhi batasan keadilan (*fairness constraint*) agar dapat diklasifikasikan ke dalam himpunan variabel acak adil ($\mathcal{W}$). Syarat keberlakuan strategi mencakup sifat non-negatif ($W \ge 0$) guna memastikan tidak adanya posisi utang, serta nilai harapan yang tidak melebihi satu ($E[W] \le 1$) sebagai bentuk hukum kekekalan modal secara rata-rata. Keempat, tujuan permainan tetap konsisten dengan upaya maksimisasi ekspektasi fungsi imbal hasil $\phi$ dari rasio modal antar-pemain, yaitu $E~\phi(W_{1}/W_{2})$. Melalui kerangka ini, dianalisis jenis distribusi probabilitas yang paling optimal untuk mengungguli lawan berdasarkan kriteria fungsi $\phi$ yang ditentukan.

 Secara konseptual, permainan ini dapat dianalogikan sebagai kompetisi antara dua pihak yang masing-masing merancang distribusi probabilitas secara independen dengan syarat nilai harapan modal tetap terjaga. Strategi optimal yang dipilih sangat bergantung pada bentuk fungsi $\phi$ yang digunakan sebagai alat ukur kemenangan. Apabila fungsi imbal hasil cenderung menyukai risiko (konveks), strategi acak yang agresif dapat menjadi pilihan utama; sebaliknya, apabila fungsi tersebut bersifat menghindari risiko atau kebangkrutan (seperti fungsi logaritmik yang konkaf), maka strategi terbaik didefinisikan sebagai penanganan modal secara utuh tanpa melibatkan elemen perjudian tambahan ($W=1$).

---
---
---
## 2.2. Syarat Strategi Tanpa Randomisasi

Tujuan utama dari analisis selanjutnya adalah menentukan karakteristik spesifik yang harus dimiliki oleh fungsi $\phi$ agar strategi optimal bagi kedua pemain merupakan strategi murni (*pure strategy*), yakni pemilihan $W=1$ sebagai konstanta. Dalam konteks formal, strategi pemain didefinisikan melalui ruang strategi fungsi distribusi $G \in \mathcal{G}$, di mana setiap pemain memilih variabel acak independen dengan nilai harapan modal yang tetap. Perumusan skor rata-rata dinyatakan dalam bentuk integral lipat dua sebagai berikut:

$$E\phi(W_{1}/W_{2}) = \iint \phi(w_{1}/w_{2}) dG_{1}(w_{1}) dG_{2}(w_{2})$$

Representasi matematis ini mencakup seluruh cakupan probabilitas dari strategi Pemain 1 dan Pemain 2. Penentuan bentuk fungsi $\phi$ menjadi krusial guna memastikan bahwa hasil integral mencapai nilai optimal pada saat variabel independen $W$ bernilai konstan satu, sehingga menghilangkan kebutuhan akan variasi atau randomisasi tambahan dalam strategi awal.

---
---

## 2.3. Kondisi Optimalitas dan Teorema 1

Strategi optimal dalam konteks permainan ini didefinisikan melalui konsep titik pelana (*saddlepoint*), sebagaimana tertuang dalam ketidaksamaan ganda pada Persamaan (2.2):
$$\iint\phi dG_{1}dG_{2}^{*} \le \iint\phi dG_{1}^{*}dG_{2}^{*} \le \iint\phi dG_{1}^{*}dG_{2}$$

Ketidaksamaan tersebut merepresentasikan Keseimbangan Nash dalam sebuah permainan jumlah-nol (*zero-sum game*), di mana tidak ada insentif bagi salah satu pihak untuk mengubah strategi optimalnya ($G^*$). Secara formal, nilai permainan $v_{\phi}$ tercapai apabila kedua pemain menerapkan strategi yang menyeimbangkan potensi keuntungan dan kerugian. 

Berdasarkan kerangka titik pelana tersebut, Teorema 1 menetapkan syarat perlu dan cukup agar strategi optimal murni tercapai pada $W_{1}^{*} = W_{2}^{*} = 1$. Syarat tersebut mengharuskan turunan pertama $\phi'(1)$ bernilai non-negatif dan fungsi $\phi$ memenuhi ketidaksamaan berikut untuk seluruh $t > 0$:
$$\left(\frac{t-1}{t}\right)\phi'(1) \le \phi(t)-\phi(1) \le (t-1)\phi'(1)$$

Secara analisis, ketidaksamaan ini membatasi kelengkungan fungsi $\phi$ dan mengharuskannya bersifat konkaf (cekung) di sekitar titik satu. Penggunaan fungsi yang bersifat konkaf, seperti fungsi logaritmik, mengimplikasikan adanya "hukuman" yang lebih berat bagi risiko kerugian dibandingkan dengan utilitas yang diperoleh dari keuntungan. Sebagai konsekuensinya, strategi terbaik yang dapat diterapkan adalah dengan tidak melakukan perjudian tambahan atau mempertahankan modal awal secara utuh. Teorema ini menjadi basis argumen bahwa pengambilan risiko hanya dibenarkan pada pemilihan instrumen pasar saham ($b$), bukan pada modifikasi modal awal ($W$). Contoh konkret dari fungsi yang memenuhi kriteria ini adalah keluarga fungsi pangkat $\phi_{\alpha}(t) = t^{\alpha}$ dengan rentang index $0 \le \alpha \le 1$, termasuk kasus limit logaritmik.

---
---
## 2.4. Analisis Fungsi Pangkat dan Awal Pembuktian

Identifikasi keluarga fungsi pangkat $\phi_{\alpha}(t) = t^{\alpha}$ menunjukkan bahwa syarat optimalitas murni terpenuhi pada rentang $0 \le \alpha \le 1$. Pada kondisi fungsi cekung atau linear tersebut, volatilitas modal awal justru akan mereduksi nilai rata-rata, sehingga strategi terbaik yang disarankan adalah penghindaran perjudian. Sebaliknya, apabila $\alpha > 1$, fungsi bersifat konveks dan mendorong pengambilan risiko secara maksimal.

Pembuktian formal dimulai dengan penyederhanaan masalah melalui normalisasi $\phi(1) = 0$ dan pendefinisian fungsi cermin $\tilde{\phi}(t) = -\phi(1/t)$. Melalui pendekatan ini, pembuktian diarahkan untuk menunjukkan bahwa tidak ada perolehan keuntungan yang dapat dihasilkan melalui perjudian, baik oleh Pemain 1 ($E\phi(W_1) \le 0$) maupun Pemain 2 ($E\tilde{\phi}(W_2) \le 0$). Konstruksi variabel acak biner spesifik $W_1$ dilakukan sebagai instrumen uji untuk mengevaluasi kelengkungan fungsi $\phi$ di sekitar titik kesetimbangan. Variabel ini dirancang dengan menyertakan peluang keuntungan ($\eta$) dan kerugian ($\delta$) kecil yang diatur sedemikian rupa agar nilai harapan modal tetap bernilai satu. Metodologi ini bertujuan untuk menginvestigasi dampak gangguan minimal (*perturbation*) terhadap skor rata-rata pada kurva yang diasumsikan bersifat cekung.

---
---
## 2.5. Derivasi Pertidaksamaan Aljabar dan Turunan

Analisis pada paruh kedua pembuktian difokuskan pada pengolahan pertidaksamaan aljabar berdasarkan variabel uji biner yang telah dikonstruksi. Ekspektasi skor dari variabel $W_1$ dijabarkan pada Persamaan (2.4), di mana hasil penjumlahan probabilitas kerugian dan keuntungan harus bernilai negatif atau nol untuk mendukung hipotesis strategi murni. Melalui manipulasi aljabar, diperoleh perbandingan gradien (kemiringan) yang menunjukkan bahwa laju kenaikan skor pada saat keuntungan harus lebih kecil dibandingkan dengan laju penurunan skor pada saat kerugian. Hal ini secara geometris mendefinisikan sifat kurva yang konkaf atau hukum hasil yang semakin berkurang (*diminishing returns*).

Penggabungan perspektif dari kedua pemain menghasilkan struktur pertidaksamaan yang menghimpit nilai gradien di sekitar titik kesetimbangan. Pada saat langkah taruhan diperkecil mendekati nol ($\eta \to 0$ dan $\delta \to 0$), limit dari rasio perubahan tersebut mendefinisikan keberadaan turunan pertama $\phi'(1)$. Keberadaan turunan yang mulus pada titik satu beserta pemenuhan syarat kelengkungan tertentu menjadi bukti akhir bahwa strategi optimal murni tercapai tanpa adanya kebutuhan untuk melakukan perjudian. Sebaliknya, fungsi yang memiliki karakteristik tajam atau cembung akan meruntuhkan struktur pertidaksamaan ini, yang mengindikasikan perlunya pengambilan risiko acak dalam strategi investasi. Dengan demikian, landasan teoritis mengenai universalitas fungsi logaritmik dalam permainan judi primitif telah ditetapkan secara formal, yang selanjutnya akan diimplementasikan pada analisis portofolio saham sesungguhnya.

---
---
---

# Convex Families
## 3.1. Ekuivalensi Pertumbuhan Logaritmik dan Dominasi Linear

Bagian ini menghubungkan dua domain matematis yang fundamental dalam teori portofolio: pertumbuhan logaritmik dan pertidaksamaan linear. Fokus utama diarahkan pada portofolio log-optimal ($b^*$), yang didefinisikan sebagai strategi pemaksimalan ekspektasi logaritma kekayaan ($E \ln b'X$). Secara matematis, portofolio ini memenuhi kondisi dominasi $E \ln (b^{*'}X/b'X) \ge 0$ terhadap setiap portofolio alternatif ($b$). Namun, guna memfasilitasi analisis dalam kerangka teori permainan, diperlukan sifat dominasi linear yang lebih kuat, yakni keberadaan portofolio $b^{**}$ yang memenuhi syarat $E(b'X/b^{**'}X) \le 1$ untuk seluruh portofolio $b$.

Pernyataan krusial dalam bagian ini menetapkan bahwa portofolio $b^*$ dan $b^{**}$ merupakan entitas yang identik. Kesamaan tersebut merupakan konsekuensi dari hasil yang lebih umum mengenai keluarga konveks dari variabel acak. Implikasinya, strategi yang memaksimalkan laju pertumbuhan logaritmik secara otomatis memenuhi syarat dominasi linear ($E(S/S^*) \le 1$), asalkan himpunan strategi yang tersedia membentuk sebuah keluarga konveks. Sifat konveksitas ini menjamin bahwa setiap campuran linear dari strategi yang valid juga merupakan strategi yang valid, yang merupakan asumsi standar dalam pemilihan portofolio di pasar keuangan.

---
---
## 3.2. Definisi dan Karakteristik Keluarga Konveks

Keluarga variabel acak $\mathcal{S}$ didefinisikan sebagai keluarga konveks apabila untuk setiap dua variabel acak $S_1, S_2 \in \mathcal{S}$ dan setiap parameter $0 \le \lambda \le 1$, campuran linear $\lambda S_1 + (1-\lambda)S_2$ juga merupakan anggota dari $\mathcal{S}$. Prinsip ini menjamin kemungkinan diversifikasi strategi, di mana penggabungan dua strategi investasi yang valid akan menghasilkan strategi baru yang tetap berada dalam ruang solusi yang diizinkan.

Universalitas sifat konveksitas ini ditunjukkan melalui berbagai contoh instrumis investasi. Pertama, pada portofolio standar dengan bobot $b$, pencampuran dua portofolio menghasilkan portofolio baru dengan bobot rata-rata tertimbang. Kedua, pada portofolio dengan batasan tertentu (seperti larangan *short-selling*), sifat konveksitas tetap terjaga selama himpunan batasan tersebut merupakan set konveks. Ketiga, dalam konteks strategi sekuensial atau dinamis di mana keputusan bergantung pada riwayat harga saham, konveksitas dipertahankan melalui mekanisme pembagian modal awal (*initial wealth splitting*). Hal ini membuktikan bahwa teori log-optimalitas tetap berlaku pada sistem investasi yang kompleks dan bergantung pada waktu selama prinsip pembagian modal dapat diterapkan.

---
---

## 3.3. Teorema 2: Ekuivalensi Sifat Logaritmik dan Linear

Teorema 2 menyatakan bahwa dalam sebuah keluarga konveks $\mathcal{S}$, portofolio $S^*$ bersifat log-optimal jika dan hanya jika ia memenuhi sifat dominasi linear. Secara formal, kondisi $E \ln(S/S^*) \le 0$ memiliki ekuivalensi penuh dengan kondisi $E(S/S^*) \le 1$ untuk seluruh $S \in \mathcal{S}$. Pembuktian arah pertama (linear ke logaritmik) dilakukan dengan memanfaatkan Ketidaksamaan Jensen, di mana sifat cekung dari fungsi logaritma memastikan bahwa logaritma dari nilai harapan selalu lebih besar atau sama dengan nilai harapan dari logaritma.

Pembuktian arah kedua (logaritmik ke linear) dilakukan melalui metode variasi. Diasumsikan terdapat sebuah portofolio alternatif $S_1$ yang melanggar sifat linear, yakni $E[S_1/S^*] > 1$. Dengan membentuk campuran linear $S_\lambda = (1-\lambda)S^* + \lambda S_1$ dan melakukan analisis perturbasi pada limit $\lambda \to 0$, ditunjukkan melalui deret Taylor bahwa asumsi tersebut akan menyebabkan kontradiksi terhadap sifat log-optimalitas $S^*$. Keberadaan kontradiksi ini membuktikan bahwa tidak mungkin terdapat strategi yang melebihi $S^*$ dalam aspek rasio linear jika $S^*$ sudah berada pada titik maksimum logaritmik. Ekuivalensi ini sangat fundamental karena menyederhanakan masalah optimasi non-linear menjadi evaluasi pertidaksamaan linear yang lebih mudah dikelola.

---
---

## 3.4. *Corollary* dan Kondisi Ekuilibrium Kuhn-Tucker

Berdasarkan Teorema 2, diturunkan beberapa konsekuensi logis dalam bentuk *corollary*. *Corollary* 1 menegaskan bahwa investasi yang memaksimalkan nilai harapan logaritma ($E \ln S$) secara otomatis mendominasi investasi lainnya dalam skala rasio linear ($E(S/S^*) \le 1$). Selanjutnya, *Corollary* 2 mendefinisikan syarat ekuilibrium pasar yang dikenal sebagai kondisi Kuhn-Tucker untuk pemilihan saham.

Kondisi ekuilibrium ini memberikan alat diagnostik untuk memverifikasi optimalitas suatu portofolio melalui dua kriteria utama. Pertama, untuk setiap saham $i$ dalam pasar, rata-rata rasio kinerjanya terhadap portofolio optimal tidak boleh melebihi satu ($E[X_i/S^*] \le 1$). Kedua, terdapat syarat seleksi di mana aset hanya akan dialokasikan pada saham yang memenuhi persamaan ketat $E[X_i/S^*] = 1$. Apabila performa suatu saham berada di bawah ambang batas tersebut ($E[X_i/S^*] < 1$), maka bobot alokasi pada saham tersebut harus bernilai nol ($b_i^* = 0$). Logika ini konsisten dengan prinsip keseimbangan energi dalam fisika, di mana distribusi massa hanya dilakukan pada titik-titik tumpu yang memberikan gaya reaksi seimbang. Penjumlahan bobot alokasi yang dikalikan dengan nilai harapan rasio tersebut secara keseluruhan akan bernilai tepat satu, yang mengonfirmasi bahwa portofolio $S^*$ telah menyerap seluruh potensi keuntungan pasar secara optimal.

---
---
---

# The $\phi$-Game for the Stock Market
### 4.1. Permainan $\phi$ dalam Pasar Saham dan Teorema Pemisahan

Bagian ini menguraikan implementasi permainan $\phi$ dalam konteks pasar saham melalui integrasi hasil analisis permainan primitif dan teori keluarga konveks. Fokus utama diarahkan pada pembuktian sifat ketangguhan (*robustness*) portofolio log-optimal ($b^*$) dalam jangka pendek. Berbeda dengan pandangan umum yang menyatakan bahwa strategi log-optimal hanya efektif untuk jangka panjang ($t \to \infty$), bagian ini membuktikan optimalitas strategi tersebut dalam skenario satu periode (*single play*) melawan kompetitor. Dalam model ini, strategi setiap pemain didefinisikan melalui dua keputusan independen: pemilihan distribusi probabilitas "adil" ($G_i$) untuk manajemen risiko dan pemilihan vektor portofolio ($b_i$) untuk alokasi aset pasar. Modal akhir merupakan hasil kombinasi dari kedua keputusan tersebut, yang dinyatakan sebagai $W \times S$.

Teorema 3 atau Teorema Pemisahan Variabel (*Separation Theorem*) menetapkan bahwa strategi optimal untuk memenangkan permainan dengan skor $\phi$ terdiri dari dua komponen yang terpisah. Komponen pertama adalah strategi judi ($W^*$) yang merupakan solusi optimal dari permainan primitif dan bergantung pada bentuk fungsi $\phi$. Komponen kedua adalah strategi saham ($b^*$) yang menggunakan portofolio log-optimal. Hasil yang signifikan menunjukkan bahwa strategi saham bersifat universal bagi kedua pemain dan tidak bergantung pada fungsi imbal hasil $\phi$ yang digunakan. Struktur ini analog dengan teknik pemisahan variabel dalam persamaan diferensial fisik, di mana strategi optimal dapat dipecah menjadi komponen pasar yang konstan dan komponen risiko yang adaptif terhadap parameter permainan.

Pembuktian Teorema 3 dilakukan melalui teknik substitusi variabel dengan mendefinisikan variabel acak baru $Z = (W_2 S_2) / S^*$. Mengingat $S^*$ adalah portofolio log-optimal yang mendominasi seluruh portofolio alternatif (sebagaimana dibuktikan dalam Teorema 2), variabel $Z$ terbukti memenuhi kriteria sebagai variabel acak yang adil ($E[Z] \le 1$). Melalui transformasi rasio modal menjadi $W_1/Z$, masalah kompetisi di pasar saham direduksi kembali menjadi masalah permainan primitif yang telah diselesaikan pada bagian sebelumnya. Hal ini menegaskan bahwa strategi dominan dalam pasar saham dicapai dengan mempertahankan disiplin pada portofolio log-optimal ($S^*$) dan menerapkan manajemen risiko ($W^*$) yang sesuai dengan toleransi utilitas yang direpresentasikan oleh $\phi$.

---

---
---
---
# Multistage Market Games
## 5.1. Permainan Pasar Multi-tahap dan Strategi Myopic

Bagian kelima memperluas cakupan teori dari skenario satu periode ke dalam dimensi waktu melalui model permainan pasar multi-tahap ($n$ periode). Dalam kerangka ini, diperkenalkan konsep bunga-berbunga (*compounding*) di mana keuntungan yang diperoleh diinvestasikan kembali, serta mekanisme rebalancing portofolio di setiap akhir periode berdasarkan informasi historis harga saham. Strategi investasi didefinisikan sebagai serangkaian fungsi keputusan sekuensial yang memungkinkan alokasi aset di masa depan bergantung pada riwayat performa pasar sebelumnya.

Teorema 4 menetapkan bahwa strategi optimal dalam jangka panjang bersifat *myopic* (rabun dekat), di mana optimalitas total dicapai dengan memaksimalkan ekspektasi logaritma kondisional pada setiap tahap secara independen. Sifat aditif dari logaritma memungkinkan transformasi operasi perkalian pada mekanisme *compounding* menjadi operasi penjumlahan, sehingga maksimisasi pertumbuhan harian secara otomatis berkontribusi pada maksimisasi akumulasi kekayaan total di akhir periode $n$. Prinsip ini menegaskan bahwa tidak diperlukan pengorbanan keuntungan jangka pendek demi tujuan jangka panjang, karena setiap langkah optimasi lokal secara matematis menjamin lintasan optimal global. Relevansi temuan ini diperkuat dengan bukti bahwa keluarga portofolio sekuensial merupakan keluarga konveks, sehingga Teorema Pemisahan dan sifat dominasi linear tetap berlaku dalam konteks dinamis ini.

---

---
---
---
# Example: Posterior Randomization Based on Relative Capital

## 6.1. Randomisasi Posterior Berdasarkan Modal Relatif

Bagian keenam menganalisis pengaruh observasi perkembangan modal antar-pemain secara berkelanjutan terhadap strategi investasi. Dalam skenario ini, aturan permainan dimodifikasi menjadi sistem observasi penuh (*full observation*), di mana setiap pemain diperkenankan untuk menyesuaikan strategi berdasarkan posisi modal relatif yang teramati setelah setiap periode pasar. Secara intuitif, informasi mengenai ketertinggalan modal sering kali dipandang sebagai pemicu untuk mengadopsi strategi yang lebih agresif guna mengejar ketertinggalan tersebut (*jockeying for position*). Namun, analisis dalam bagian ini menunjukkan hasil yang kontraintuitif, di mana strategi optimal terbukti tetap bersifat independen terhadap fluktuasi modal lawan.

Mekanisme permainan ronde demi ronde melibatkan randomisasi awal, pemilihan portofolio, dan penyesuaian strategi pasca-observasi pasar. Meskipun terdapat peluang untuk melakukan randomisasi bersyarat (*conditional randomization*) berdasarkan rasio modal $S_1/S_2$, temuan matematis menunjukkan bahwa strategi pertahanan terbaik (minimax) dapat dicapai tanpa perlu memperhatikan posisi modal lawan secara spesifik. Upaya untuk memanipulasi hasil berdasarkan posisi relatif justru berpotensi menjadi bumerang yang merugikan pemain. Hal ini menegaskan bahwa kepatuhan pada rencana awal dengan menggunakan portofolio log-optimal ($b^*$) dan randomisasi standar ($W^*$) merupakan pendekatan yang paling stabil dalam mencapai ekuilibrium.

---

## 6.2. Perbandingan Strategi pada Ketimpangan Modal

Analisis terhadap skenario ketimpangan modal mengacu pada temuan sebelumnya dalam konteks judi murni, di mana pemain dengan modal yang lebih kecil cenderung mengadopsi strategi berisiko ekstrem untuk membalikkan keadaan. Dalam permainan judi tanpa elemen pasar saham, strategi optimal bagi pemain yang tertinggal sering kali melibatkan distribusi probabilitas yang memiliki massa di titik nol (peluang kebangkrutan tinggi) demi peluang mendapatkan keuntungan besar. Fenomena ini mencerminkan upaya maksimal untuk mengatasi ketertinggalan modal awal yang signifikan.

Namun, ketika logika ini diterapkan ke pasar saham, terdapat mekanisme penyeimbang otomatis yang disediakan oleh portofolio log-optimal ($b^*$). Berdasarkan sifat dominasi linear $E(S_{lawan}/S_{kita}) \le 1$, pemain yang setia pada strategi log-optimal secara statistik membatasi peluang lawan untuk memperoleh keuntungan melalui strategi judi ekstrem. Permainan pasar dengan randomisasi bersyarat (*conditionally randomized market game*) dimodelkan melalui persamaan imbal hasil yang kompleks guna mengakomodasi ketergantungan strategi terhadap kondisi pasar dan posisi modal. Pembuktian pada bagian selanjutnya menunjukkan bahwa pengambilan risiko ekstrem tersebut tidak diperlukan di pasar saham, karena karakteristik fundamental dari portofolio log-optimal telah menjamin stabilitas nilai permainan dalam jangka panjang.

---

## 6.3. Dekonstruksi Matematis Persamaan 6.1 dan 6.2

Persamaan (6.1) memfungsikan strategi bagi pemain yang berada dalam posisi modal inferior, di mana peningkatan utilitas dicapai melalui kombinasi probabilitas kebangkrutan yang dominan dan peluang perolehan keuntungan yang signifikan secara diskret. Struktur ini merepresentasikan upaya untuk membalikkan ketertinggalan melalui pengambilan risiko ekstrem dibandingkan dengan strategi akumulasi modal yang konservatif. Sebaliknya, Persamaan (6.2) menjelaskan evolusi permainan pasca-observasi pasar, di mana fungsi imbal hasil dihitung sebagai integrasi antara performa pasar ($x$), respons strategi pemain terhadap informasi modal ($S_1, S_2$), dan taktik lawan.

Komponen krusial dalam analisis ini adalah distribusi probabilitas bersyarat $dG(w | x, S_1, S_2)$, yang mencerminkan penyesuaian strategi pasca-pengevaluasian hasil pasar. Persamaan ini menghitung skor akhir pertandingan dengan mempertimbangkan kemampuan pemain untuk melakukan modifikasi taktis berdasarkan posisi relatif mereka di tengah durasi permainan. Integrasi seluruh variabel ketidakpastian ini bertujuan untuk mengevaluasi apakah fleksibilitas taktis tersebut memberikan keunggulan kompetitif yang nyata dibandingkan dengan kepatuhan pada strategi yang bersifat tetap (*unconditional*).

---

## 6.4. Lemma dan Teorema 5: Optimasi Strategi Tetap

Resolusi terhadap perdebatan mengenai kebutuhan akan strategi adaptif disajikan melalui Lemma dan Teorema 5. Lemma menetapkan bahwa fungsi nilai permainan $v_{\phi}(u)$ merupakan fungsi non-dekretif yang bersifat konkaf (cekung) terhadap modal modal relatif $u$. Sifat konkavitas ini bertindak sebagai pembatas alami terhadap keinginan untuk mengadopsi risiko spekulatif secara acak. Berdasarkan Ketidaksamaan Jensen, pembagian modal menjadi taruhan berisiko tidak akan menghasilkan nilai harapan yang lebih tinggi daripada mempertahankan modal tersebut secara stabil, mengingat nilai harapan dari fungsi cekung selalu lebih kecil atau sama dengan fungsi dari nilai harapan modal.

Teorema 5 memberikan kesimpulan bahwa dalam permainan pasar yang memungkinkan observasi berkelanjutan, strategi optimal tetap dicapai melalui penggunaan portofolio log-optimal ($b^*$) dan randomisasi tetap ($W^*$) yang tidak bergantung pada hasil pasar secara *real-time*. Fenomena ini dijelaskan melalui karakteristik rasio modal dalam kondisi rasional, di mana penggunaan portofolio log-optimal oleh kedua pemain akan cenderung menjaga kestabilan rasio modal di sekitar titik kesetimbangan. Penyimpangan dari strategi log-optimal oleh lawan justru akan mereduksi modal relatif mereka secara statistik, sehingga pemain tidak perlu melakukan manuver taktis tambahan untuk mempertahankan dominasi. Temuan ini menegaskan bahwa strategi pertahanan minimax yang bersifat *unconditional* telah memadai untuk mencapai hasil optimal tanpa harus mempedulikan fluktuasi modal lawan.

---
---
## 6.5. Validitas Strategi Tetap Melalui Pasangan Titik Pelana

Pembuktian teknis mengenai keberlakuan strategi tetap dilakukan melalui konsep titik pelana (*saddlepoint*). Strategi pasangan $(b^*, W^*)$ terbukti merupakan titik keseimbangan yang stabil, sebagaimana ditunjukkan melalui kondisi penjepitan pada Persamaan (6.4). Dalam kerangka ini, upaya pemain untuk melakukan modifikasi strategi secara licik berdasar observasi pasar tidak memberikan peningkatan skor rata-rata di atas nilai permainan $v_{\phi}$. Sebaliknya, upaya musuh untuk melakukan hal serupa tidak mampu mereduksi skor pemain di bawah ambang batas kesetimbangan tersebut.

Persamaan (6.5) memberikan dukungan formal terhadap hipotesis ini with menunjukkan bahwa rasio gabungan antara portofolio alternatif dan strategi judi bersyarat memiliki nilai harapan yang tidak melebihi satu ($E \le 1$) terhadap standar portofolio log-optimal. Hasil ini didasarkan pada dua fakta fundamental: kriteria keadilan pada strategi judi yang menjaga nilai harapan tetap pada satu, serta sifat dominasi linear dari portofolio log-optimal terhadap portofolio lainnya. Oleh karena itu, manuver taktis yang kompleks sekalipun tidak dapat menutupi kelemahan statistik dari penyimpangan terhadap strategi log-optimal. Implikasi akhir dari pembuktian ini menegaskan bahwa penggunaan randomisasi yang bersifat *unconditional* telah memadai dalam mencapai efisiensi kompetitif yang optimal di pasar saham.
