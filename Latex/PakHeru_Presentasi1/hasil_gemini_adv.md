# INTRODUCTION

## Paragraf 1
### 1. Vektor Saham ($X$) - _Kondisi Pasar_

Penulis mendefinisikan pasar sebagai kumpulan dari $m$ saham, yang dituliskan sebagai vektor $X = (X_{1}, X_{2}, ..., X_{m})$.

- **Apa itu $X_i$?** Ini adalah poin krusial. $X_i$ bukanlah "harga saham", melainkan **nilai kembalian (return) dari investasi satu unit** pada saham ke-$i$.
    
    - _Contoh:_ Jika Anda menginvestasikan $1 di saham A dan nilainya menjadi $1.10, maka $X_A = 1.10$. Jika nilainya turun menjadi $0.90, maka $X_A = 0.90$.
        
- **Sifat $X_i$:** Variabel ini diasumsikan **non-negatif** ($X_i \ge 0$), artinya nilai investasi tidak bisa turun di bawah nol (Anda tidak bisa kehilangan lebih dari uang yang Anda investasikan dalam model ini).
    

### 2. Distribusi Bersama ($F(x)$) - _Ketidakpastian_

Vektor $X$ ditarik berdasarkan fungsi distribusi bersama (_joint distribution function_) $F(x)$ yang diasumsikan **diketahui** ($known$)5.

- **Kontribusi:** Ini menyatakan bahwa pasar bersifat _stokastik_ (acak), bukan deterministik.
    
- **"Joint" (Bersama):** Kata ini penting karena menyiratkan adanya korelasi antar saham. Kenaikan nilai saham $X_1$ mungkin mempengaruhi probabilitas kenaikan atau penurunan saham $X_2$.
    

### 3. Vektor Portofolio ($b$) - _Strategi Investor_

Ini adalah variabel keputusan yang dikendalikan oleh investor. Portofolio didefinisikan sebagai vektor $b = (b_{1}, ..., b_{m})$.

- **Interpretasi $b_i$:** $b_i$ adalah **proporsi kekayaan** yang dialokasikan ke saham ke-$i$.
    
- **Ruang $B$ (Constraint):** Vektor $b$ harus berada dalam himpunan $B$, yang memiliki dua syarat utama:
    
    1. $b_i \ge 0$: Tidak ada _short selling_ (meminjam saham untuk dijual). Anda hanya bisa membeli (long position).
        
    2. $\sum b_i = 1$: Total proporsi harus sama dengan 1 (100% modal dialokasikan).
        

### 4. Modal Acak ($S$) - _Hasil Akhir_

Ini adalah hasil (payoff) dari strategi Anda melawan pasar. Modal akhir $S$ didefinisikan sebagai hasil perkalian titik (_dot product_) antara vektor strategi $b$ dan vektor pasar $X$:

$$S = \sum b_i X_i = b^t X$$

- **Penjelasan:** $S$ adalah rata-rata tertimbang dari kinerja semua saham, di mana bobotnya adalah keputusan alokasi Anda ($b$). Karena $X$ adalah variabel acak, maka $S$ (hasil investasi Anda) juga merupakan variabel acak.
    

---

Ringkasan Paragraf 1:

Kita memiliki sebuah permainan di mana Anda memilih vektor bobot $b$ (strategi), alam semesta melempar dadu untuk menentukan vektor hasil $X$ (pasar), dan skor akhir Anda adalah $S = b^t X$.

Apakah penjelasan definisi variabel dasar ini sudah cukup jelas? Jika ya, kita bisa lanjut ke paragraf berikutnya di mana penulis mulai memperkenalkan konsep "Game Theory" dengan dua pemain.

---
---

## Paragraf 2

Mari kita masuk ke paragraf kedua. Di sini, penulis mengubah skenario dari sekadar "investasi" menjadi sebuah **kompetisi** atau "Game Theory".

Penulis memperkenalkan konsep **Two-Person Zero-Sum Game** (Permainan dua orang jumlah-nol). Bayangkan Anda (Pemain 1) sedang beradu strategi melawan investor lain (Pemain 2) di pasar yang sama.

Berikut adalah penjelasan komponen kuncinya:

### 1. Fungsi Payoff (Fungsi Skor): $E\phi(S_1/S_2)$

Ini adalah inti dari permainannya. Tujuannya bukan sekadar "menjadi kaya", tetapi "mengalahkan lawan".

- **Rasio $S_1/S_2$:** Skor ditentukan oleh perbandingan modal akhir Anda ($S_1$) terhadap modal lawan ($S_2$). Jika $S_1/S_2 > 1$, Anda menang (modal Anda lebih besar).
    
- **Fungsi $\phi$ (Phi):** Penulis menyatakan bahwa $\phi$ bisa berupa fungsi apa saja asalkan **non-decreasing** (tidak menurun/monoton naik).
    
    - _Implikasi:_ Semakin besar rasio kekayaan Anda terhadap lawan, semakin tinggi skornya (atau setidaknya tidak berkurang). Ini generalisasi yang sangat kuat—artinya aturan ini berlaku entah Anda hanya ingin "sedikit lebih kaya" dari lawan atau "jauh lebih kaya".
        
- **E (Ekspektasi):** Karena pasar acak ($X$ ditarik dari distribusi $F$), kita melihat nilai rata-rata (harapan) dari skor tersebut.
    

### 2. Randomisasi yang Adil (_Fair Randomization_): $\tilde{S}$

Penulis memperkenalkan notasi $\tilde{S}_1$ dan $\tilde{S}_2$.

- Dalam _game theory_, strategi optimal seringkali melibatkan elemen acak (mixed strategy) agar tidak mudah ditebak lawan.
    
- Penulis menyebutkan "fair randomization" terhadap modal awal. Artinya, sebelum membeli saham, pemain mungkin melakukan taruhan sampingan yang "adil" (fair gamble) untuk mengubah modal awalnya.
    
    - _Catatan Fisika:_ Anggap ini sebagai fluktuasi termal atau _noise_ yang sengaja ditambahkan ke sistem awal, namun rata-ratanya tetap (konservasi energi/modal rata-rata).
        

### 3. Solusi Universal: Portofolio Log-Optimal ($b^*$)

Ini adalah klaim utama (hipotesis) dari paper ini. Penulis memberikan "bocoran" jawaban dari permainan tersebut 3.

- Ternyata, untuk mengalahkan lawan dengan kriteria payoff apapun (asalkan $\phi$ tidak turun), ada satu strategi "senjata pamungkas", yaitu **$b^*$**.
    
- **Definisi $b^*$:** Portofolio ini adalah portofolio yang **memaksimalkan ekspektasi logaritma dari kekayaan** ($E \ln b'X$)4.
    
    - Secara matematis:
        
        $$b^* = \text{arg max}_b \ E[\ln(b^t X)]$$
        

Kesimpulan Paragraf 2:

Penulis mengajukan tesis bahwa memaksimalkan laju pertumbuhan logaritmik (Log Optimal) adalah strategi paling dominan (robust). Strategi ini akan menang atau setidaknya imbang dalam segala jenis permainan kompetitif melawan investor lain, tidak peduli bagaimana cara skor dihitung ($\phi$), selama skor itu berbasis pada memiliki uang lebih banyak daripada lawan.

Apakah konsep "Fungsi Payoff berdasarkan rasio $S_1/S_2$" ini bisa dipahami? Konsep ini agak berbeda dengan teori portofolio modern biasa (Markowitz) yang hanya melihat _Return_ vs _Risk_ sendirian.

---
---

## Paragraf 3-4 (Persamaan 1.1)

Mari kita bedah **Persamaan (1.1)** dan paragraf di sekitarnya. Ini adalah definisi formal dari "medan pertempuran" antara Anda (Player 1) dan lawan (Player 2).

Persamaannya adalah:

$$E \phi\left(\frac{W_{1}b_{1}^{\prime}X}{W_{2}b_{2}^{\prime}X}\right) = \iiint \phi\left(\frac{w_{1}b_{1}^{\prime}x}{w_{2}b_{2}^{\prime}x}\right) dG_{1}(w_{1}) dG_{2}(w_{2}) dF(x)$$

Mari kita urai setiap komponennya secara bertahap1:

### 1. Strategi Dua Tahap (The Strategy Space)

Penulis mendefinisikan strategi pemain ($i$) bukan hanya memilih saham, tapi terdiri dari dua langkah2:

- **Langkah A: Randomisasi Awal ($G_i$ dan $W_i$)**
    
    - Setiap pemain mulai dengan 1 unit modal3.
        
    - Sebelum masuk pasar saham, pemain memilih distribusi probabilitas $G_i(w)$.
        
    - Pemain menukar 1 unit modalnya dengan variabel acak $W_i$ yang ditarik dari distribusi $G_i$.
        
    - **Constraint (Syarat Batas):** Distribusi ini harus "Adil" (_Fair_), artinya $E[W_i] \le 1$ dan $W_i \ge 0$4.
        
    - _Analogi Fisika:_ Ini seperti Anda memiliki energi awal $E_0=1$. Anda boleh memecahnya menjadi distribusi probabilitas energi (seperti fungsi gelombang), asalkan nilai ekspektasi energinya tidak melebihi energi awal ($\langle E \rangle \le 1$).
        
- **Langkah B: Alokasi Portofolio ($b_i$)**
    
    - Setelah mendapatkan modal acak $W_i$ dari langkah A, barulah pemain mengalokasikannya ke saham menggunakan vektor $b_i$.
        

### 2. Modal Akhir Pemain

Dari strategi di atas, modal akhir (Random Capital) untuk masing-masing pemain adalah:

- **Player 1:** $\tilde{S}_1 = W_1 (b_1' X)$
    
- **Player 2:** $\tilde{S}_2 = W_2 (b_2' X)$
    

Di sini $b_1' X$ adalah notasi _dot product_ ($\sum b_{1j}X_j$), yaitu hasil murni dari portofolio saham. Faktor $W$ adalah pengali dari taruhan awal 6.

### 3. Integral Tiga Lapis (The Expectation)

Sisi kanan persamaan adalah integral lipat tiga. Ini menghitung **rata-rata ansambel** (ensemble average) dari fungsi skor $\phi$ terhadap seluruh kemungkinan semesta:

$$\iiint \dots \underbrace{dG_{1}(w_{1})}_{\text{Acak Player 1}} \underbrace{dG_{2}(w_{2})}_{\text{Acak Player 2}} \underbrace{dF(x)}_{\text{Acak Pasar}}$$

- **$dG_1(w_1)$ & $dG_2(w_2)$:** Ini adalah ketidakpastian yang _dikendalikan_ oleh strategi pemain. Anda memilih bentuk fungsi distribusi $G_1$ untuk mencoba memaksimalkan integral ini.
    
- **$dF(x)$:** Ini adalah ketidakpastian dari _alam_ (pasar). Anda tidak bisa mengontrol $F(x)$, Anda hanya bisa meresponsnya.
    

### 4. Makna Persamaan (1.1)

Persamaan ini menyatakan:

"Skor rata-rata saya adalah total penjumlahan dari nilai skor ($\phi$) pada setiap kemungkinan keadaan ($w_1, w_2, x$), dikalikan dengan probabilitas kejadian tersebut terjadi."

### 5. Nilai Permainan (Game Value) - Persamaan (1.2)

Tepat setelah (1.1), penulis mendefinisikan tujuan permainan sebagai masalah **Minimax** (Saddle Point):

$$v = \sup_{b_1, G_1} \inf_{b_2, G_2} E[\dots]$$

- **Sup (Supremum):** Player 1 mencoba mencari strategi ($b_1, G_1$) yang memberikan skor _tertinggi_.
    
- **Inf (Infimum):** Player 2 (lawan) diasumsikan cerdas dan akan mencari strategi ($b_2, G_2$) yang membuat skor Player 1 serendah mungkin (karena ini _zero-sum game_).
    
- Jika nilai Max-Min sama dengan Min-Max, maka permainan memiliki solusi stabil atau **Value of the Game** ($v$)8.
    

Poin Penting untuk Fisikawan:

Struktur ini sangat mirip dengan mekanika statistik atau termodinamika. Anda mencari keadaan makroskopis yang stabil (ekuilibrium) di mana satu gaya mencoba meminimalkan potensi (lawan), sementara gaya lain mencoba memaksimalkannya (Anda). Titik temunya adalah solusi optimal $b^*$.

Apakah struktur integral dan konsep "Randomisasi Awal" ($W$) ini dapat diterima? Karena bagi investor awam, ide "bertaruh dulu sebelum investasi" terdengar aneh, tapi dalam matematika _game theory_, _mixed strategy_ (strategi campuran/acak) seringkali penting untuk _convexity_.

---
---

## Paragraf 5

Di halaman 2 paragraf pertama ini, penulis melakukan sesuatu yang sangat elegan: mereka menunjukkan **universalitas** dari model mereka.

Penulis mendemonstrasikan bahwa bentuk matematika $E \phi(\tilde{S}_1 / \tilde{S}_2)$ adalah sebuah "Teori Penyatuan Besar" (_Grand Unified Theory_) untuk berbagai jenis tujuan investasi kompetitif.

Mari kita bedah daftar kasus (a) sampai (h) yang disebutkan1, dan apa makna fisis/finansialnya:

### 1. Transformasi Tujuan Menjadi Fungsi $\phi$

Inti dari paragraf ini adalah: Apapun tujuan Anda dalam mengalahkan lawan, itu bisa ditulis ulang sebagai fungsi $\phi$ dari rasio kekayaan $(\tilde{S}_1 / \tilde{S}_2)$.

Berikut adalah bedahannya:

- **(a) $P(\tilde{S}_{1}>\tilde{S}_{2})$ — Probabilitas Menang Murni**
    
    - **Arti:** Anda tidak peduli _seberapa banyak_ Anda menang, Anda hanya peduli _bahwa_ Anda menang (modal akhir Anda lebih besar dari lawan).
        
    - **Bentuk $\phi$:** Ini adalah **Fungsi Tangga Heaviside** (Step Function). Nilainya 0 jika rasio $<1$, dan 1 jika rasio $\ge 1$.
        
    - _Koneksi Fisika:_ Ini seperti operator proyeksi dalam mekanika kuantum, yang hanya bernilai 1 jika sistem berada dalam _eigenstate_ tertentu ("menang").
        
- **(b) $P(\tilde{S}_{1}>t\tilde{S}_{2})$ — Probabilitas Menang Dominan**
    
    - **Arti:** Anda hanya merasa "menang" jika kekayaan Anda minimal $t$ kali lipat dari lawan (misal: "Saya harus 2x lebih kaya dari dia").
        
    - **Bentuk $\phi$:** Sama seperti (a), tapi fungsi tangganya bergeser (_shifted step function_) ke titik $t$.
        
- **(c) $E[\tilde{S}_{1}/\tilde{S}_{2}]$ — Ekspektasi Rasio (Linear)**
    
    - **Arti:** Anda ingin memaksimalkan rata-rata seberapa kali lipat kekayaan Anda dibanding lawan.
        
    - **Bentuk $\phi$:** Fungsi linear, $\phi(x) = x$.
        
- **(d) $E[e^{\tilde{S}_{1}/\tilde{S}_{2}}]$ — Ekspektasi Eksponensial**
    
    - **Arti:** Ini fungsi yang sangat agresif. Anda sangat menghargai kemenangan besar (karena eksponensial tumbuh sangat cepat), tapi sangat menghukum kekalahan.
        
- **(e) $E[\ln(\tilde{S}_{1}/\tilde{S}_{2})]$ — Ekspektasi Logaritmik**
    
    - **Arti:** Ini adalah "bintang utama" paper ini. Fungsi logaritma mengubah rasio menjadi selisih: $\ln(S_1/S_2) = \ln S_1 - \ln S_2$.
        
    - **Implikasi:** Memaksimalkan ini sama dengan memaksimalkan laju pertumbuhan eksponensial jangka panjang (Kelly Criterion).
        
- **(f) $E[\tilde{S}_{1}/(\tilde{S}_{1}+\tilde{S}_{2})]$ — Pangsa Pasar (Market Share)**
    
    - **Arti:** Anda ingin menguasai persentase total kekayaan yang ada di meja. Jika $\phi = S_1/(S_1+S_2)$, Anda sedang memaksimalkan potongan kue ekonomi yang Anda pegang.
        
- **(g) $E \min \{\tilde{S}_{1}/\tilde{S}_{2}, a\}$ — Truncated Gain (Keuntungan Terpotong)**
    
    - **Arti:** Anda ingin menang, tapi utilitas/kepuasan Anda mentok di titik $a$. Menang 1000x lipat tidak memberikan kepuasan lebih dibanding menang $a$ kali lipat. Ini memodelkan sifat "cukup puas" (_satiation_).
        

### 2. Koneksi ke Paper Sebelumnya (Bell & Cover 1980)

Kalimat terakhir paragraf ini merujuk pada karya penulis sebelumnya2.

> _"The payoff function $P(\tilde{S}_{1}>\tilde{S}_{2})$... is obtained when we let $\phi$ be the indicator function of $[1, \infty)$."_

Di sini mereka menegaskan secara matematis:

$$P(\tilde{S}_1 > \tilde{S}_2) = E [ \mathbf{1}_{\tilde{S}_1/\tilde{S}_2 \ge 1} ]$$

Di mana $\mathbf{1}$ adalah fungsi indikator.

Ini penting karena membuktikan bahwa **Probabilitas** hanyalah kasus khusus dari **Ekspektasi** (Expectation). Karena teorema utama paper ini nanti berlaku untuk _semua_ fungsi $\phi$ yang _non-decreasing_, maka teoremanya otomatis berlaku juga untuk memaksimalkan probabilitas kemenangan semata.

Ringkasan untuk Anda:

Paragraf ini berkata: "Hei, tidak peduli apakah Anda ingin sekadar menang, menang telak, atau menguasai pangsa pasar—selama tujuan Anda adalah memiliki lebih banyak uang daripada lawan (fungsi monotonik), matematika yang akan kami turunkan di bab berikutnya akan tetap berlaku untuk Anda."

Cukup jelas bagian ini? Jika ya, kita akan masuk ke **Section 2**, di mana mereka mulai membahas "Primitive Game" tanpa saham.

---
---

## Paragraf 6 - Selesai

Tentu, mari kita bahas paragraf-paragraf transisi ini 1. Ini adalah bagian yang sangat penting karena penulis memberikan **peta jalan (roadmap)** tentang bagaimana mereka akan membuktikan klaim besar mereka.

Penulis memecah pembuktian yang kompleks menjadi beberapa tahap logis (§2 hingga §6). Berikut adalah penjelasan bertahap dari setiap bagian yang mereka rencanakan:

### 1. §2: Permainan Primitif (_The Primitive $\phi$-Game_)

> _"We first consider in §2... game with payoff function $E~\phi(W_{1}/W_{2})$..."_ 2

Sebelum masuk ke kerumitan pasar saham (dengan segala korelasi dan harga sahamnya), penulis melakukan **isolasi sistem**.

- **Apa itu Permainan Primitif?** Ini adalah permainan di mana tidak ada saham sama sekali.
    
- **Mekanisme:** Pemain hanya memilih "Variabel Acak yang Adil" ($W_1$ dan $W_2$).
    
    - Syarat: $W \ge 0$ dan $E[W] \le 1$.
        
- **Tujuan:** Penulis ingin memecahkan masalah matematika murni tentang bagaimana cara mengalahkan lawan dalam "adu nasib" menggunakan distribusi probabilitas, tanpa terganggu oleh detail pemilihan saham.
    

### 2. §3: Ekuivalensi Matematika (_The Key Proof_)

> _"§3 establishes the equivalence of $ES/S^{*}$... and $E \ln S/S^{*}\le0$..."* 3

Ini adalah "jantung" matematika dari paper ini. Penulis menyatakan bahwa jika himpunan variabel acak membentuk **keluarga konveks** (_convex family_), maka ada hubungan setara yang mengejutkan:

- Memaksimalkan Logaritma ($E \ln S$) $\iff$ Memenuhi pertidaksamaan linear ($E [S/S^*] \le 1$).
    
- **Kenapa ini penting?** Dalam fisika/matematika, seringkali sulit membuktikan sesuatu secara langsung (optimasi non-linear). Dengan membuktikan ekuivalensi ini, penulis bisa menggunakan sifat linear ($E \le 1$) yang lebih mudah dihitung untuk membuktikan sifat logaritmik ($E \ln$).
    

### 3. §4: Faktorisasi Solusi (_The Separation_)

> _"minimax strategies... are $W_{1}^{*}b^{*\prime}X$..."_

Di sini penulis menyatukan kembali Permainan Primitif (§2) dengan Pasar Saham. Hasilnya sangat cantik: **Pemisahan Variabel**.

Strategi optimal ternyata terpecah menjadi dua bagian independen:

1. **Bagian Game ($W^*$):** Strategi acak murni untuk mengalahkan lawan (diambil dari solusi §2). Bagian ini bergantung pada fungsi skor $\phi$.
    
2. **Bagian Investasi ($b^*$):** Alokasi saham (diambil dari maksimisasi Log). Bagian ini **tidak** bergantung pada $\phi$.
    

_Implikasi:_ Tidak peduli seberapa aneh aturan mainnya ($\phi$), cara Anda memilih saham ($b^*$) harus selalu sama: **Log-Optimal**.

### 4. §5 & §6: Dinamika Waktu (_Multistage_)

> _"These results hold up for multistage market games..."_

Penulis memperluas model dari statis (satu kali main) menjadi dinamis (berkali-kali main, $t=1, 2, ..., n$).

- Mereka mengklaim bahwa strategi $b^*$ ini tetap optimal bahkan jika dimainkan berulang-ulang dalam jangka panjang.
    

### 5. Referensi Raksasa

Paragraf ini ditutup dengan menyebutkan nama-nama besar: Thorp (penemu _card counting_ Blackjack), Breiman, Samuelson (ekonom Nobel), dll7. Ini menempatkan paper ini di tengah perdebatan sengit antara matematikawan (yang suka Log-Optimal) dan ekonom klasik (seperti Samuelson yang sering mengkritiknya).

Intisari Bagian Roadmap Ini:

Penulis berkata: "Kami akan memecah masalah ini. Pertama, kami selesaikan masalah judinya (§2). Kedua, kami siapkan alat matematikanya (§3). Ketiga, kami gabungkan kembali untuk membuktikan bahwa portofolio Log-Optimal adalah solusi universal untuk investasi kompetitif (§4), baik jangka pendek maupun panjang (§5-6)."

Apakah alur logika pembuktian yang mereka rencanakan ini masuk akal bagi Anda? Jika ya, kita siap masuk ke **Section 2: Pure Optimal Strategies** untuk melihat matematika "permainan primitif" tersebut.

---
---
---
# Pure Optimal Strategies for the Primitive $\phi$-Game

## 2.1

Mari kita masuk ke **Section 2: Pure Optimal Strategies for the Primitive $\phi$-Game**.

Di paragraf pertama bagian ini 1, penulis mendefinisikan "permainan dasar" atau **Primitive Game**. Ini adalah versi paling sederhana dari konflik antara dua investor, yang sengaja dibuat abstrak untuk memudahkan analisis matematika.

Berikut adalah komponen-komponen utamanya:

### 1. Medan Permainan: Tanpa Saham (_No Stock Market_)

Penulis menegaskan: _"As yet, there is no stock market or portfolio selection in the problem"_.

- Kita melupakan dulu tentang harga saham, tren pasar, atau portofolio.
    
- Fokusnya murni pada **pemilihan distribusi probabilitas**.
    

### 2. Aturan Main: Memilih $W$

Pemain 1 dan Pemain 2 masing-masing harus memilih "senjata" mereka, yaitu sebuah **Variabel Acak (Random Variable)**, yang disebut $W_1$ dan $W_2$.

- Anda tidak memilih saham, tapi Anda memilih "bentuk keberuntungan" Anda sendiri. Apakah Anda ingin hasil yang pasti (misal: selalu dapat 1), atau hasil yang berisiko (misal: 50% dapat 0, 50% dapat 2)?
    

### 3. Batasan Keadilan (_Set of Fair Random Variables_)

Pilihan $W$ tidak boleh sembarangan. $W$ harus termasuk dalam himpunan $\mathcal{W}$, yang disebut sebagai himpunan **Fair r.v.'s** (Variabel Acak Adil).

Syarat untuk menjadi "Adil" ada dua:

1. **Non-negatif ($W \ge 0$):** Anda tidak bisa kehilangan lebih dari apa yang Anda miliki (tidak ada utang).
    
2. **Mean $\le 1$ ($E[W] \le 1$):** Rata-rata nilai harapan dari variabel acak tersebut tidak boleh lebih dari 1.
    
    - _Penjelasan Fisika/Ekonomi:_ Ini adalah hukum "kekekalan modal" secara rata-rata. Anda tidak bisa menciptakan uang dari ketiadaan. Jika Anda ingin peluang menang besar, Anda harus menyeimbangkannya dengan peluang kalah, sehingga rata-ratanya tetap 1 (modal awal).
        

### 4. Tujuan: Fungsi Payoff

Tujuannya tetap sama seperti di pendahuluan: Memaksimalkan ekspektasi fungsi $\phi$ dari rasio modal Anda terhadap lawan5:

$$E~\phi(W_{1}/W_{2})$$

Ringkasan Paragraf Ini:

Bayangkan dua orang masuk ke kasino. Mereka tidak bermain melawan kasino, tapi melawan satu sama lain. Masing-masing boleh merancang permainan dadu atau koin sendiri, asalkan permainan itu "adil" (rata-rata hasilnya tidak menambah modal). Pertanyaannya: Distribusi probabilitas seperti apa ($W_1$) yang harus saya pilih agar saya bisa "mengalahkan" distribusi probabilitas lawan ($W_2$), jika kemenangan diukur dengan fungsi $\phi$?

Apakah konsep "bertarung menggunakan distribusi probabilitas" ini bisa dipahami? Jika ya, kita akan lanjut ke paragraf berikutnya di mana mereka mencari kondisi di mana strategi terbaik adalah _tidak berjudi sama sekali_.

---

Tentu, ini adalah cara terbaik untuk memahaminya. Mari kita buat sebuah analogi cerita berjudul **"Duel Kotak Ajaib"**.

Dalam cerita ini, kita tidak berada di pasar saham. Kita berada di sebuah ruangan tertutup dengan hukum fisika yang aneh.

### Babak 1: Persiapan (Definisi $W$ dan _Fairness_)

Ada dua kontestan: Anda (Player 1) dan Lawan (Player 2).

Wasit memberikan kalian masing-masing 1 keping emas sebagai modal awal.

Aturan Main:

Kalian tidak boleh menyimpan keping emas itu begitu saja. Kalian harus menukarnya dengan sebuah "Kotak Ajaib" ($W$). Kalian boleh merancang sendiri bagaimana kotak itu bekerja, tapi ada satu hukum kekekalan energi (syarat Fairness):

> "Secara rata-rata (_expectation_), kotak buatanmu harus mengeluarkan 1 keping emas. Tidak boleh lebih."

Kalian membuat strategi masing-masing:

- **Strategi Anda ($W_1$ - Si Stabil):** Anda membuat kotak yang membosankan. Kotak ini 100% pasti berisi **1 keping**. (Rata-rata = 1).
    
- **Strategi Lawan ($W_2$ - Si Penjudi):** Lawan membuat kotak yang berisiko. Kotak ini punya peluang 50% berisi **0 keping** (kosong), dan 50% berisi **2 keping**. (Rata-rata = $0.5 \times 0 + 0.5 \times 2 = 1$).
    

Kedua kotak ini sah ("Adil") menurut aturan. Sekarang, saatnya **Penilaian**.

---

### Babak 2: Sang Juri (Fungsi $\phi$)

Di sinilah fungsi $\phi$ masuk. $\phi$ adalah **"Kacamata Juri"**. Bagaimana cara Juri menentukan siapa pemenangnya tergantung pada kacamata ($\phi$) apa yang dia pakai.

Mari kita lihat 3 skenario Juri yang berbeda untuk melihat bagaimana hasil duel berubah:

#### Skenario A: Juri "Yang Penting Menang" (Indikator)

- **Kacamata ($\phi$):** Juri hanya melihat: "Siapa yang punya emas lebih banyak?"
    
    - Jika Emas Anda > Emas Lawan, skor = 1 (Anda Menang).
        
    - Jika Emas Anda < Emas Lawan, skor = 0 (Anda Kalah).
        
- **Hasil Duel:**
    
    - Jika kotak Lawan keluar 0 (Peluang 50%): Anda punya 1, Lawan 0. **Anda Menang**.
        
    - Jika kotak Lawan keluar 2 (Peluang 50%): Anda punya 1, Lawan 2. **Anda Kalah**.
        
- **Kesimpulan:** Peluangnya 50:50. Di mata Juri ini, strategi stabil Anda dan strategi judi Lawan sama kuatnya.
    

#### Skenario B: Juri "Linear" (Ekspektasi Rasio)

- **Kacamata ($\phi$):** Juri menghitung persis rasionya: $\phi(x) = x$. Skor Anda adalah $E[\text{Emas Anda} / \text{Emas Lawan}]$.
    
- **Hasil Duel:**
    
    - Jika kotak Lawan keluar 2: Rasio Anda = $1/2 = 0.5$.
        
    - Jika kotak Lawan keluar 0: Rasio Anda = $1/0 = \infty$ (Tak terhingga!).
        
- **Kesimpulan:** Rata-rata skor Anda menjadi sangat besar (karena pembagian dengan nol). Di mata Juri ini, Lawan yang mengambil risiko 0 (kebangkrutan) sangat bodoh karena memberi Anda skor tak terhingga.
    

#### Skenario C: Juri "Logaritma" (Pertumbuhan Aset)

- **Kacamata ($\phi$):** Juri ini sangat membenci kebangkrutan. Dia menggunakan fungsi Logaritma: $\phi(x) = \ln(x)$.
    
- **Analisis Matematis:**
    
    - Skor = $E[\ln(\text{Emas Anda} / \text{Emas Lawan})]$.
        
    - Skor = $E[\ln(\text{Emas Anda})] - E[\ln(\text{Emas Lawan})]$.
        
- **Hasil Duel:**
    
    - **Nilai Anda:** $\ln(1) = 0$. (Anda aman, skor nol).
        
    - **Nilai Lawan:** Mari hitung rata-rata logaritmanya.
        
        - Setengah waktu dia dapat 2: $\ln(2) \approx 0.69$.
            
        - Setengah waktu dia dapat 0: $\ln(0) = -\infty$ (Hancur total).
            
    - **Rata-rata Lawan:** $-\infty$.
        
- Kesimpulan:
    
    Skor Anda (0) jauh lebih tinggi daripada skor Lawan ($-\infty$).
    
    Di mata Juri Logaritma, Strategi Stabil (Tidak Berjudi) menang telak melawan Strategi Penjudi.
    

---

### Inti Pelajarannya

Kalimat _"jika kemenangan diukur dengan fungsi $\phi$"_ artinya:

Strategi mana yang "terbaik" ($W^*$ optimal) sepenuhnya bergantung pada siapa Jurinya (bentuk $\phi$).

- Jika Jurinya suka risiko (Fungsi Konveks), strategi terbaik mungkin adalah berjudi segila mungkin.
    
- Jika Jurinya benci risiko/kebangkrutan (Fungsi Konkaf seperti Logaritma), strategi terbaik adalah **diam dan jangan berjudi** ($W=1$).
    

Paper ini kemudian akan membuktikan (di Theorem 1) bahwa untuk fungsi Logaritma, strategi terbaik dalam _Primitive Game_ adalah menjadi "Si Stabil" (pegang $W=1$, jangan diacak-acak).

Apakah cerita ini membuat konsep "pengukuran kemenangan $\phi$" menjadi lebih masuk akal?

---
---
## 2.2

Bagus. Mari kita lanjut ke paragraf kedua di **Section 2** ini.

Di paragraf ini 1, penulis mulai menyusun pertanyaan kunci yang akan dijawab oleh teorema matematika mereka. Pertanyaannya sederhana namun mendalam:

**"Kapan strategi terbaik adalah TIDAK melakukan apa-apa?"**

Mari kita bedah kalimat per kalimat dari paragraf ini:

### 1. Mencari Kondisi "Tanpa Judi"

> _"We first wish to determine conditions on $\phi$ such that no randomization is needed to achieve the value of the game."_ 2

Penulis mencari tahu karakteristik apa yang harus dimiliki oleh fungsi $\phi$ (si Juri dalam cerita kita tadi) agar strategi optimal bagi kedua pemain adalah strategi murni (_pure strategy_), yaitu memilih $W=1$ secara pasti.

- **Dalam konteks cerita:** Penulis bertanya, "Seberapa 'benci risiko' si Juri harusnya, supaya strategi terbaik bagi Anda berdua adalah datang dengan kotak berisi 1 keping emas pas, tanpa dadu, tanpa acak-acakan?"
    
- **Kenapa ini penting?** Karena jika kita bisa membuktikan bahwa strategi terbaik adalah $W=1$ (tidak berjudi), maka nanti di pasar saham, "perjudian" kita hanya akan terbatas pada **pemilihan saham** ($b$), bukan pada taruhan sampingan yang aneh-aneh.
    

### 2. Definisi Formal Strategi ($G \in \mathcal{G}$)

> _"players 1 and 2 choose independent random variables $W_1 \sim G_1, W_2 \sim G_2$..."_ 3

Di sini penulis mendefinisikan ruang strategi secara matematis:

- Pemain memilih **Fungsi Distribusi** $G$.
    
- Syaratnya tetap sama: Ekspektasi nilai $\le 1$ dan tidak negatif.
    
- Distribusi $G_1$ dan $G_2$ bersifat independen. Artinya, saya tidak bisa mengintip hasil lemparan dadu Anda sebelum saya melempar dadu saya. Kita melempar bersamaan (simultan).
    

### 3. Persamaan Payoff (2.1)

Penulis menuliskan ulang skor rata-rata dalam bentuk integral ganda:

$$E\phi(W_{1}/W_{2}) = \iint \phi(w_{1}/w_{2}) dG_{1}(w_{1}) dG_{2}(w_{2})$$

Ini adalah representasi matematis dari "Duel Kotak Ajaib" tadi.

- **Integral Luar ($dG_2$):** Kita menjumlahkan semua kemungkinan hasil yang keluar dari kotak Lawan.
    
- **Integral Dalam ($dG_1$):** Kita menjumlahkan semua kemungkinan hasil yang keluar dari kotak Anda.
    
- **$\phi(w_1/w_2)$:** Di setiap kombinasi hasil, Juri memberikan skor berdasarkan rasio emas kalian.
    

Inti Paragraf Ini:

Penulis sedang menyiapkan panggung untuk Theorem 1. Mereka berkata: "Oke, ini rumus skor lengkapnya (integral ganda). Sekarang, mari kita cari tahu bentuk fungsi $\phi$ seperti apa yang membuat hasil integral ini paling optimal justru ketika kita membuang tanda integralnya (alias tidak ada variasi, $W$ konstan di angka 1)."

Jika bagian ini sudah jelas, kita akan masuk ke bagian **Saddlepoint Condition** (Persamaan 2.2) dan akhirnya ke **Theorem 1** yang menjawab pertanyaan tersebut. Siap lanjut?

---
---

## 2.3
Mari kita masuk ke bagian inti matematikanya: **Kondisi Optimalitas** dan **Theorem 1**.

Di sini, penulis mendefinisikan apa yang dimaksud dengan "Strategi Terbaik" menggunakan konsep **Titik Pelana (Saddlepoint)**.

### 1. Kondisi Titik Pelana (Persamaan 2.2)

Penulis menuliskan ketidaksamaan ganda ini1:

$$\iint\phi dG_{1}dG_{2}^{*} \le \iint\phi dG_{1}^{*}dG_{2}^{*} \le \iint\phi dG_{1}^{*}dG_{2}$$

Ini adalah definisi standar dari **Keseimbangan Nash** dalam _Zero-Sum Game_. Mari kita baca dari tengah ke luar:

- **Tengah ($\dots dG_{1}^{*}dG_{2}^{*}$):** Ini adalah skor jika **kedua pemain** bermain sempurna (optimal). Skor ini disebut **Nilai Permainan ($v_{\phi}$)**.
    
- **Sisi Kiri ($\le$):** Jika Lawan bermain sempurna ($G_2^*$), dan Anda mencoba mengubah strategi Anda (menjadi $G_1$ sembarangan), skor Anda akan **turun atau sama**. Artinya, Anda tidak punya insentif untuk mengubah strategi. $G_1^*$ sudah yang terbaik.
    
- **Sisi Kanan ($\le$):** Jika Anda bermain sempurna ($G_1^*$), dan Lawan mencoba mengubah strateginya (menjadi $G_2$ sembarangan), skor Anda akan **naik atau sama**. Ingat, Lawan ingin skor Anda sekecil mungkin. Jadi, jika dia mengubah strategi, dia justru membantu Anda (skor naik). Artinya, Lawan juga tidak punya insentif untuk berubah.
    

_Analogi Fisika:_ Ini seperti bola yang berada di dasar lembah (bagi Lawan) sekaligus di puncak bukit (bagi Anda). Posisi yang stabil.

---

### 2. Theorem 1: Syarat "Tanpa Judi"

Sekarang kita sampai pada teorema pertama. Penulis menjawab pertanyaan: __Kapan strategi terbaik adalah diam saja ($W^* \equiv 1$)?_*

Bunyi Teorema:

Permainan primitif ini memiliki strategi optimal murni $W_{1}^{*} = W_{2}^{*} = 1$ jika dan hanya jika:

1. Turunan pertama $\phi'(1)$ ada dan $\ge 0$.
    
2. Fungsi $\phi$ memenuhi ketidaksamaan berikut untuk semua $t > 0$:
    
    $$\left(\frac{t-1}{t}\right)\phi'(1) \le \phi(t)-\phi(1) \le (t-1)\phi'(1)$$
    

Apa Makna Fisis dari Rumus Ini?

Ketidaksamaan di atas pada dasarnya membatasi kelengkungan (kurvatur) fungsi $\phi$.

- Bentuk ini memaksa fungsi $\phi$ untuk bersifat **Konkaf (Cekung)** di sekitar titik 1.
    
- Bayangkan grafik fungsi Logaritma ($\ln t$) atau akar kuadrat ($\sqrt{t}$). Mereka melengkung ke bawah. Kenaikan dari 1 ke 2 memberikan manfaat yang lebih kecil daripada kerugian dari 1 ke 0.
    
- **Intinya:** Jika Juri menilai menggunakan fungsi yang "Cekung" (seperti Logaritma), maka "hukuman" dari resiko jatuh miskin jauh lebih berat daripada "hadiah" dari jadi kaya. Oleh karena itu, strategi terbaik adalah **tidak mengambil risiko sama sekali** ($W=1$).
    

### 3. Contoh Kasus (Remark)

Penulis memberikan contoh konkret di paragraf berikutnya3:

- Keluarga fungsi pangkat $\phi_{\alpha}(t) = t^{\alpha}$ memenuhi syarat ini jika **$0 \le \alpha \le 1$**.
    
- Fungsi Logaritma (kasus limit $\alpha \to 0$) juga memenuhi syarat ini.
    

Kesimpulan Bagian Ini:

Penulis telah membuktikan secara matematis bahwa jika tujuan Anda adalah Pertumbuhan Logaritmik (atau fungsi cekung lainnya), maka dalam permainan "adu nasib" murni, JANGAN BERJUDI. Simpan modal Anda utuh ($W=1$).

Ini akan menjadi basis argumen nanti: Perjudian (pengambilan risiko) hanya boleh dilakukan di pasar saham ($b$), bukan pada modal awal ($W$).

Apakah penjelasan mengenai _Saddlepoint_ dan makna ketidaksamaan di Theorem 1 ini cukup jelas?

---
---
## 2.4
Tentu, mari kita pecah bagian ini menjadi dua. Bagian pertama ini akan mencakup **Remark (Komentar)** dan **Persiapan Pembuktian (Setup)** hingga pendefinisian variabel $W_1$ dan $W_2$ 1.

Bagian ini penting karena penulis sedang membangun "jebakan matematika" untuk menguji teoremanya.

### 1. The Remark (Komentar tentang Fungsi Pangkat)

Penulis memberikan contoh konkret fungsi apa saja yang memenuhi syarat "Tanpa Judi" tadi.

> _"The family of functions $\phi_{\alpha}(t)=t^{\alpha}$... satisfies the conditions... if $0\le\alpha\le1$"_ 

- **Makna:** Fungsi pangkat $t^\alpha$ (seperti akar kuadrat $\sqrt{t}$ atau fungsi linear $t$) adalah fungsi yang melengkung ke bawah (cekung) atau lurus.
    
    - Jika $\alpha > 1$ (misal $t^2$), fungsinya melengkung ke atas (konveks). Dalam kasus ini, strategi terbaik justru **berjudi sekeras mungkin**.
        
    - Jika $0 \le \alpha \le 1$, strategi terbaik adalah **diam ($W=1$)**.
        
- **Contoh Kasino:** Penulis memberi ilustrasi: Jika dua penjudi masuk ke kasino dan sepakat bahwa Pemenang mendapat bayaran $E(W_1/W_2) - 1$ dari Pecundang, maka _"neither should gamble"_. Artinya, jika Anda membuat taruhan yang "adil" secara matematika, tapi fungsi kepuasannya cekung ($\alpha \le 1$), volatilitas (naik-turunnya uang) justru merugikan nilai rata-rata Anda.
    

### 2. Awal Pembuktian: Penyederhanaan Masalah

Sekarang masuk ke bagian **PROOF**. Penulis melakukan dua trik matematika untuk mempermudah pembuktian:

- Trik 1: Normalisasi $\phi(1)=0$
    
    Penulis mengasumsikan $\phi(1) = 0$. Ini tidak mengubah esensi permainan, hanya menggeser titik nol skornya. Jadi, jika rasio modal sama ($1/1$), skornya 0.
    
    - _Implikasi:_ Jika strategi terbaik adalah diam ($W=1$), maka skor rata-ratanya harus $E[\phi(1)] = 0$.
        
    - Oleh karena itu, penulis hanya perlu membuktikan bahwa untuk _setiap_ strategi acak $W$ yang lain, skornya pasti negatif ($E\phi(W) \le 0$).
        
- Trik 2: Fungsi Cermin ($\tilde{\phi}$)
    
    Penulis mendefinisikan $\tilde{\phi}(t) = -\phi(1/t)$.
    
    - Ini adalah perspektif Lawan. Jika Anda mencoba memaksimalkan $\phi(W_1/W_2)$, Lawan mencoba melakukan hal yang sama dari sisinya.
        
    - Pembuktian menjadi simetris: Kita harus membuktikan bahwa $E\phi(W_1) \le 0$ (Anda tidak bisa untung dengan berjudi) DAN $E\tilde{\phi}(W_2) \le 0$ (Lawan juga tidak bisa untung dengan berjudi).
        

### 3. Konstruksi "Variabel Uji" ($W_1$ dan $W_2$)

Ini adalah bagian paling cerdik 6. Penulis tidak menguji _semua_ kemungkinan variabel acak sekaligus. Mereka membangun sebuah **variabel acak biner** (dua kemungkinan hasil) yang sangat spesifik untuk menguji batas-batas fungsi $\phi$.

Bayangkan sebuah koin yang tidak seimbang (bias). Penulis mendefinisikan $W_1$ sebagai berikut:

$$W_{1}=\begin{cases}1-\delta, & \text{peluang } \frac{\eta}{\delta+\eta}\\ 1+\eta, & \text{peluang } \frac{\delta}{\delta+\eta}\end{cases}$$

- **Apa itu $\delta$ dan $\eta$?**
    
    - $\delta$ (delta) adalah kerugian kecil (turun sedikit di bawah 1).
        
    - $\eta$ (eta) adalah keuntungan kecil (naik sedikit di atas 1).
        
- Kenapa peluangnya aneh begitu?
    
    Peluang tersebut dipilih dengan sangat presisi agar rata-ratanya tetap 1 (syarat Fair Game).
    
    Mari kita cek:
    
    $$E[W_1] = (1-\delta)\frac{\eta}{\delta+\eta} + (1+\eta)\frac{\delta}{\delta+\eta} = 1$$
    
    (Jika dihitung, hasilnya pas 1).
    

Tujuan Konstruksi Ini:

Penulis sedang membuat "gangguan terkecil" (perturbation) di sekitar angka 1. Mereka ingin melihat: "Jika saya geser sedikit ke kiri ($\delta$) dan sedikit ke kanan ($\eta$), apakah fungsi $\phi$ akan memberi skor positif atau negatif?"

Jika $\phi$ cekung (seperti bukit), geseran ke kiri-kanan ini akan membuat Anda turun ke lereng, sehingga rata-ratanya lebih rendah dari puncak. Inilah yang akan dibuktikan secara aljabar di bagian selanjutnya (persamaan 2.4 ke atas).

Sampai di sini, apakah logika **"Membuat variabel uji biner untuk mengetes kelengkungan kurva"** ini bisa diterima? Jika ya, kita lanjut ke paruh kedua (aljabar pertidaksamaannya).

---
---
## 2.5
Mari kita lanjutkan ke paruh kedua pembuktian ini, yaitu **Aljabar Pertidaksamaan (Persamaan 2.4 hingga 2.9)**.

Di bagian sebelumnya, kita sudah membuat "koin bias" ($W_1$) yang kadang nilainya naik sedikit ($1+\eta$) dan kadang turun sedikit ($1-\delta$), tapi rata-ratanya tetap 1.

Sekarang, kita masukkan koin ini ke dalam syarat optimalitas: "Jika strategi diam ($W=1$) itu terbaik, maka berjudi dengan koin ini hasilnya harus **negatif atau nol** ($E\phi \le 0$)."

### 1. Menghitung Ekspektasi (Persamaan 2.4)

Kita hitung nilai harapan skor dari variabel $W_1$ tadi:

$$E\phi(W_1) = \left( \frac{\eta}{\delta+\eta} \right) \phi(1-\delta) + \left( \frac{\delta}{\delta+\eta} \right) \phi(1+\eta) \le 0$$

- Suku pertama adalah probabilitas turun dikali skor saat turun.
    
- Suku kedua adalah probabilitas naik dikali skor saat naik.
    
- Totalnya harus $\le 0$ (karena kita asumsi $\phi(1)=0$).
    

Penulis kemudian mengalikan kedua sisi dengan $(\delta+\eta)$ untuk membuang penyebut, menghasilkan1:

$$\eta\phi(1-\delta) + \delta\phi(1+\eta) \le 0$$

### 2. Membandingkan Kemiringan (Persamaan 2.8)

Ini adalah langkah paling krusial secara geometris. Penulis memindah-mindahkan ruas persamaan di atas agar bentuknya menjadi perbandingan "Rasio Perubahan" (Slope/Gradien) 2:

$$\frac{\phi(1+\eta)}{\eta} \le \frac{-\phi(1-\delta)}{\delta}$$

Mari kita artikan secara fisis:

- **Ruas Kiri ($\frac{\phi(1+\eta)}{\eta}$):** Ini adalah **Gradien Kanan**. Seberapa besar skor Anda _naik_ per unit langkah ke kanan ($\eta$).
    
- **Ruas Kanan ($\frac{-\phi(1-\delta)}{\delta}$):** Ini adalah **Gradien Kiri**. Seberapa besar skor Anda _turun_ per unit langkah ke kiri ($\delta$). (Ingat $\phi(1)=0$, jadi $-\phi(1-\delta)$ adalah besarnya penurunan).
    

Makna Fisis:

Persamaan ini mengatakan: "Kecepatan skor Anda naik (saat untung) harus lebih kecil daripada kecepatan skor Anda turun (saat rugi)."

Ini adalah definisi dari Hukum Hasil yang Semakin Berkurang (Diminishing Returns) atau kurva Cekung (Concave).

### 3. Jebakan Ganda (Sandwich)

Ingat kita juga punya Pemain 2? Penulis melakukan hal yang sama untuk Pemain 2 menggunakan fungsi $\tilde{\phi}$.

Hasilnya memberikan ketidaksamaan arah sebaliknya. Ketika digabungkan, kita mendapatkan "Jepitan" (Sandwich) yang terlihat di Persamaan (2.8):

$$\text{Gradien Kiri Tertentu} \le \text{Gradien Kanan} \le \text{Gradien Kiri Lainnya}$$

### 4. Limit Menuju Nol (Persamaan 2.9)

Sekarang penulis memperkecil langkah taruhannya sampai mendekati nol ($\eta \to 0$ dan $\delta \to 0$).

$$-\phi(1-\delta)/\delta + \dots \le \lim_{\eta \to 0} \frac{\phi(1+\eta)}{\eta} \le \dots$$

Dalam kalkulus, limit dari $\frac{\phi(1+\eta) - \phi(1)}{\eta}$ saat $\eta \to 0$ adalah definisi dari **Turunan Pertama ($\phi'(1)$)**.

- Karena gradien kiri dan gradien kanan "dijepit" semakin dekat, mereka harus bertemu di satu titik.
    
- Ini membuktikan bahwa turunan $\phi'(1)$ **harus ada** (fungsi harus mulus di titik 1) 4.
    
- Dan nilainya harus memenuhi syarat kelengkungan tertentu agar ketidaksamaan itu tetap konsisten untuk segala ukuran langkah ($t$).
    

Kesimpulan Akhir Section 2:

Melalui deretan aljabar ini, penulis berhasil membuktikan:

Agar strategi terbaik adalah "Jangan Berjudi", fungsi skor Anda ($\phi$) haruslah fungsi yang mulus dan cekung (seperti Logaritma).

Jika fungsi Anda tajam atau cembung (suka risiko), maka ketidaksamaan di atas akan runtuh, dan itu artinya Anda _seharusnya_ berjudi.

Apakah derivasi dari _probability_ menjadi _slope inequality_ ini sudah jelas? Jika ya, kita telah menyelesaikan fondasi teoritisnya dan siap masuk ke **Section 3**, di mana kita mulai bicara soal "Convex Families" dan portofolio saham sesungguhnya.

---
---
---

# Convex Families
## 3.1

Paragraf pertama di bagian ini adalah jembatan penghubung yang sangat krusial. Penulis menghubungkan dua dunia matematika yang berbeda: dunia **Logaritma** dan dunia **Linear**.

Mari kita bedah apa yang mereka sampaikan di paragraf pembuka ini:

### 1. Memperkenalkan Sang Juara: $b^*$ (Log Optimal)

Penulis memulai dengan mengingatkan kita pada portofolio $b^*$ yang sudah kita bahas sebelumnya.

- **Definisi:** $b^*$ adalah portofolio yang memaksimalkan $E \ln (b'X)$.
    
- Sifat Dominasi: Karena dia memaksimumkan log, maka secara matematis:
    
    $$E \ln \left(\frac{b^{*'}X}{b'X}\right) \ge 0$$
    
    Artinya, rata-rata selisih logaritma kekayaan $b^*$ dengan portofolio lain ($b$) selalu positif2.
    

### 2. Membutuhkan "Kunci" Baru: $b^{**}$

Untuk membuktikan teori permainan (Game Theory) di bab-bab selanjutnya, penulis mengaku bahwa sifat logaritma di atas belum cukup. Mereka membutuhkan sifat pertidaksamaan linear yang lebih kuat.

Mereka mencari portofolio (sebut saja $b^{**}$) yang memenuhi syarat:

$$E \left(\frac{b'X}{b^{**'}X}\right) \le 1$$

untuk semua portofolio $b$ lainnya.

- Apa arti fisis rumus ini?
    
    Rasio $S/S^{**}$ adalah variabel acak "kekayaan relatif". Jika nilai harapannya $\le 1$, ini berarti $b^{**}$ sangat dominan sehingga portofolio lain ($S$) tidak bisa tumbuh lebih cepat darinya secara rata-rata rasio. Ini disebut sifat Supermartingale atau Sub-Fair.
    

### 3. Penyatuan (The Unification)

Inilah poin terpenting di paragraf ini: Penulis mengklaim bahwa **$b^*$ dan $b^{**}$ adalah portofolio yang SAMA**.

> _"That the portfolios $b^{*}$ and $b^{**}$ are the same is a consequence of the following more general result on convex families of random variables."_

Penulis menyatakan: "Strategi yang memaksimalkan pertumbuhan logaritmik ($E \ln S$) ternyata secara otomatis juga memenuhi syarat dominasi linear ($E(S/S^*) \le 1$)."

Kenapa ini penting?

Ingat Section 2 tadi? Kita belajar bahwa jika kita punya variabel acak yang "Adil" ($E \le 1$) dan fungsi cekung, strategi terbaik adalah diam.

Dengan menyamakan $b^*$ dengan $b^{**}$, penulis bisa menggunakan seluruh matematika "tanpa judi" dari Section 2 untuk diterapkan pada portofolio saham Log-Optimal.

### 4. Syarat Utama: "Convex Family"

Penulis memberi catatan kaki bahwa kesamaan ini hanya berlaku jika himpunan variabel acak yang kita pilih membentuk **Keluarga Konveks** (_Convex Family_).

- **Definisi Konveks:** Jika strategi A valid, dan strategi B valid, maka campuran dari A dan B (misal 50% A + 50% B) juga harus valid.
    
- Di pasar saham, ini jelas berlaku (kita bisa mencampur portofolio).
    

Ringkasan Paragraf 1 Section 3:

Penulis berkata: "Kami punya jagoan bernama Log-Optimal ($b^*$). Kami butuh jagoan yang punya sifat linear ($E \le 1$) untuk memenangkan game theory. Kabar baiknya: Jagoan Log-Optimal ternyata punya sifat linear tersebut! Syaratnya cuma satu: arenanya harus konveks."

Cukup jelas bagian jembatan ini? Jika ya, kita akan melihat definisi formal "Convex Family" di paragraf berikutnya.

---
---
## 3.2
Mari kita masuk ke paragraf definisi dan contoh-contoh di **Section 3** 1.

Di sini penulis memastikan "alat matematika" mereka (yaitu _Convex Family_) benar-benar bisa dipakai di dunia nyata. Mereka memberikan definisi formal lalu menguji apakah berbagai jenis strategi investasi memenuhi syarat tersebut.

### 1. Definisi "Convex Family" (Keluarga Konveks)

Penulis mendefinisikan $\mathcal{S}$ sebagai keluarga konveks variabel acak jika:

Untuk setiap dua variabel acak $S_1$ dan $S_2$ yang ada di dalam keluarga tersebut, campuran linearnya juga harus ada di situ2.

Rumusnya:

$$\lambda S_1 + (1-\lambda)S_2 \in \mathcal{S}$$

untuk $0 \le \lambda \le 1$.

- **Analogi Fisika:** Ini adalah **Prinsip Superposisi**. Jika Gelombang A adalah solusi valid, dan Gelombang B adalah solusi valid, maka campuran $30\% A + 70\% B$ juga harus menjadi solusi yang valid.
    
- **Dalam Keuangan:** Ini berarti "Diversifikasi". Jika Anda punya dua strategi investasi yang sah, Anda harus diperbolehkan membagi modal Anda di antara kedua strategi itu.
    

---

### 2. Tiga Contoh Validitas

Penulis kemudian membuktikan bahwa hampir semua jenis investasi yang kita kenal memenuhi sifat superposisi ini.

Contoh 1: Portofolio Standar 3

- **Kasus:** Anda membeli saham biasa ($X_i$) dengan bobot $b$.
    
- **Analisis:** Jika Anda mencampur Portofolio A dan Portofolio B, hasilnya hanyalah Portofolio C dengan bobot baru.
    
- **Kesimpulan:** Valid.
    

Contoh 2: Portofolio dengan Batasan (Constrained) 4

- **Kasus:** Ada aturan tambahan, misalnya "Tidak boleh _short-selling_" ($b_i \ge 0$) atau "Maksimal investasi di sektor tambang 20%".
    
- **Analisis:** Selama himpunan batasan itu sendiri membentuk geometri cembung (_convex set_ $B_0$), maka campuran dua portofolio yang taat aturan pasti juga taat aturan.
    
    - _Contoh:_ Jika A tidak punya utang, dan B tidak punya utang, campuran A dan B juga pasti tidak punya utang.
        
- **Kesimpulan:** Valid.
    

Contoh 3: Portofolio Sekuensial / Berdasarkan Waktu 5

Ini adalah kasus yang paling sulit dan paling penting untuk strategi jangka panjang.

- **Kasus:** Anda berinvestasi selama $n$ hari. Keputusan Anda hari ini bergantung pada harga saham kemarin ($b_k(X_1, ..., X_{k-1})$).
    
- **Pertanyaan:** Bisakah kita mencampur dua "algoritma trading" yang rumit menjadi satu strategi baru yang valid?
    
- Bukti Penulis 6:
    
    Penulis mengakui bahwa kita tidak bisa sekadar merata-rata keputusan hariannya.
    
    - _Solusi:_ Cara mencampurnya adalah dengan **membagi modal di awal**.
        
    - Anda memecah $1 modal awal menjadi $\lambda$ (diserahkan ke Manajer Algoritma A) dan $1-\lambda$ (diserahkan ke Manajer Algoritma B).
        
    - Di akhir hari ke-$n$, Anda gabungkan hasilnya. Total kekayaan ini ($S$) adalah campuran linear dari $S^{(1)}$ dan $S^{(2)}$.
        
    - Karena strategi "pecah modal di awal" adalah strategi yang sah, maka himpunan hasil akhirnya membentuk keluarga konveks.
        

Mengapa Contoh 3 Sangat Penting?

Bagi fisikawan, Contoh 3 ini menegaskan bahwa teori ini berlaku untuk Sistem Dinamis. Tidak peduli seberapa rumit ketergantungan waktu atau feedback loop dalam strategi Anda, asalkan Anda bisa membagi modal awal, teori Log-Optimal ini tetap berlaku.

Apakah konsep "Konveksitas" dan pembuktian pada Contoh 3 (strategi waktu) ini bisa dipahami? Jika ya, kita siap masuk ke **Theorem 2**, teorema inti yang menghubungkan Logaritma dengan Linearitas.

---
---

## 3.3

Mari kita masuk ke **Theorem 2** 1.

Ini adalah **Mesin Utama** dari seluruh makalah ini. Teorema ini memberikan legitimasi matematika untuk mengubah masalah optimasi non-linear yang sulit (Logaritma) menjadi masalah pertidaksamaan linear yang lebih mudah dikelola.

### 1. Bunyi Teorema 2

Jika $\mathcal{S}$ adalah keluarga konveks, maka portofolio terbaik $S^*$ memiliki dua sifat yang **ekuivalen** (jika satu benar, yang lain pasti benar):

1. Sifat Logaritma (Log-Optimal):
    
    $$E \ln(S/S^*) \le 0$$
    
    (Rata-rata selisih logaritma portofolio lain terhadap $S^*$ selalu negatif. Artinya $S^*$ memberikan pertumbuhan tertinggi).
    
    **JIKA DAN HANYA JIKA**
    
2. Sifat Linear (Supermartingale/Sub-fair):
    
    $$E(S/S^*) \le 1$$
    
    (Rata-rata rasio kekayaan portofolio lain terhadap $S^*$ tidak pernah lebih dari 1).
    

---

### 2. Pembuktian Arah Kanan: Linear $\to$ Logaritma

Bagian ini menggunakan **Ketaksamaan Jensen** (_Jensen's Inequality_). Ini sangat familiar bagi fisikawan.

- **Logika:** Kita tahu fungsi $\ln(x)$ adalah fungsi cekung (_concave_).
    
- Menurut Jensen: Logaritma dari rata-rata selalu lebih besar daripada rata-rata dari Logaritma.
    
    $$\ln(E[X]) \ge E[\ln(X)]$$
    
- Jika kita asumsikan Sifat Linear benar ($E[S/S^*] \le 1$), maka:
    
    $$E \ln(S/S^*) \le \ln(E[S/S^*]) \le \ln(1) = 0$$
    
- **Kesimpulan:** Terbukti. Jika Anda menang secara rasio linear, Anda pasti menang secara logaritmik 2.
    

---

### 3. Pembuktian Arah Kiri: Logaritma $\to$ Linear (Bagian Sulit)

Bagian ini lebih menarik. Penulis menggunakan **Metode Kontradiksi** dengan teknik variasi (_Variational Method_), mirip seperti prinsip _Virtual Work_ dalam fisika.

**Langkah-langkah Pembuktian:**

1. **Asumsi Awal:** Anggap $S^*$ adalah raja logaritma ($E \ln S/S^* \le 0$ untuk semua $S$).
    
2. **Asumsi Kontradiksi:** Anggap ada satu "pemberontak" $S_1$ yang melanggar sifat linear, yaitu $E(S_1/S^*) > 1$ 3.
    
3. Menciptakan Campuran ($S_\lambda$):
    
    Karena $\mathcal{S}$ adalah keluarga konveks, kita bisa mencampur $S^*$ dengan si pemberontak $S_1$ sedikit saja (sebesar $\lambda$).
    
    $$S_\lambda = (1-\lambda)S^* + \lambda S_1 = S^* + \lambda(S_1 - S^*)$$
    
    Ini valid 4.
    
4. Analisis Perturbasi (Deret Taylor):
    
    Mari kita lihat logaritma dari campuran ini:
    
    $$\ln\left(\frac{S_\lambda}{S^*}\right) = \ln\left(1 + \lambda\left(\frac{S_1}{S^*} - 1\right)\right)$$
    
    Untuk $\lambda$ yang sangat kecil (limit mendekati 0), kita bisa pakai Deret Taylor orde pertama ($\ln(1+x) \approx x$):
    
    $$\approx \lambda \left(\frac{S_1}{S^*} - 1\right)$$
    
5. Menghitung Ekspektasi:
    
    $$E \ln(S_\lambda/S^*) \approx \lambda \left( E\left[\frac{S_1}{S^*}\right] - 1 \right)$$
    
6. Pukulan Mematikan (The Kill):
    
    Kita tadi berasumsi bahwa si pemberontak punya $E[S_1/S^*] > 1$.
    
    Maka, suku di dalam kurung $\left( E\left[\frac{S_1}{S^*}\right] - 1 \right)$ bernilai Positif.
    
    Akibatnya, $E \ln(S_\lambda/S^*) > 0$.
    
    Ini kontradiksi! Kita tadi sepakat $S^*$ adalah raja logaritma (maxima). Bagaimana mungkin ada campuran $S_\lambda$ yang memberikan nilai logaritma positif (lebih besar dari $S^*$)? 5.
    

Kesimpulan Fisis:

Karena asumsi adanya "pemberontak" menyebabkan kontradiksi matematika (melanggar kondisi stasioner di puncak bukit logaritma), maka si pemberontak itu tidak mungkin ada.

Maka terbuktilah: Jika Anda berada di puncak bukit Logaritma, maka gradien ke arah manapun (Linear) haruslah negatif atau nol.

### 4. Mengapa Teorema ini Penting?

Teorema ini memberi kita "Senjata Rahasia".

Nanti di bab selanjutnya, saat kita melawan musuh (Game Theory), kita tidak perlu menghitung integral logaritma yang rumit. Kita cukup menunjukkan bahwa $E(S_{musuh}/S_{kita}) \le 1$.

Pertidaksamaan linear ini jauh lebih mudah dipakai untuk membuktikan kemenangan.

Apakah alur pembuktian Logaritma $\to$ Linear menggunakan "Variasi Kecil" ($\lambda$) ini bisa dipahami? Ini sangat mirip dengan cara kita membuktikan prinsip Lagrangian ( $\delta S = 0$ ).

---
---

## 3.4
Bagus sekali Anda bisa melewati Theorem 2. Itu memang bagian terberat secara konseptual. Sekarang, **Corollary 1** dan **Corollary 2** adalah "hadiah"-nya. Ini adalah aplikasi praktis dari teorema berat tadi ke dunia nyata.

Mari kita bahas satu per satu.

### Corollary 1: Sang Juara Bertahan (Generalisasi)

Corollary 1 hanyalah penegasan ulang dari Theorem 2, tapi dengan bahasa "kemenangan".

- **Pernyataan:** Jika ada investasi $S^*$ yang mencapai nilai maksimum $E \ln S$, maka investasi tersebut otomatis mengalahkan investasi lain ($S$) dalam artian $E(S/S^*) \le 1$.
    
- **Makna Fisis:** Ini seperti hukum seleksi alam. Jika Anda adalah organisme (strategi) yang paling efisien dalam mengumpulkan energi (log growth), maka tidak ada organisme lain yang bisa mendominasi Anda secara rata-rata. Anda adalah "Apex Predator" di pasar.
    

---

### Corollary 2: Syarat Keseimbangan Pasar (Kuhn-Tucker)

Ini bagian yang sangat menarik bagi fisikawan. Penulis menerjemahkan kondisi optimal abstrak tadi menjadi **aturan praktis untuk memilih saham**.

Kita punya kumpulan saham $X_1, X_2, \dots, X_m$. Bagaimana kita tahu portofolio kita ($S^* = b^{*'}X$) sudah optimal atau belum tanpa menghitung ulang semuanya?

Corollary 2 memberikan dua kondisi (yang dikenal sebagai kondisi **Kuhn-Tucker** dalam optimasi):

#### 1. Kondisi Batas Atas (Inequality)

$$E \left( \frac{X_i}{S^*} \right) \le 1 \quad \text{untuk semua } i$$

- **Arti:** Ambil saham mana saja di pasar (misal saham $X_i$). Bandingkan kinerjanya terhadap portofolio optimal $S^*$. Rata-rata rasionya tidak boleh lebih dari 1.
    
- **Implikasi:** Bahkan saham individu terbaik pun tidak bisa mengalahkan portofolio optimal ini secara sistematis. Portofolio $S^*$ sudah menyerap semua "sari-sari keuntungan" dari pasar.
    

#### 2. Kondisi Seleksi (Complementary Slackness)

$$b_i^* = 0 \quad \text{jika } \quad E \left( \frac{X_i}{S^*} \right) < 1$$

- **Arti:** Jika ada saham $X_k$ yang performanya "lemah" (rata-rata rasionya terhadap portofolio $< 1$), maka Anda **tidak boleh** menaruh uang sepeser pun di sana ($b_k = 0$).
    
- **Implikasi:** Anda hanya menaruh uang ($b_i > 0$) pada saham-saham yang memenuhi persamaan ketat: $E(X_i/S^*) = 1$.
    

---

### Analogi Fisika: Prinsip Kerja Maya (Virtual Work)

Bayangkan Anda sedang mencari posisi keseimbangan sebuah sistem mekanik.

- $S^*$ adalah posisi keseimbangan energi minimum.
    
- $X_i$ adalah arah-arah gaya yang mungkin (saham).
    
- Syarat $E(X_i/S^*) \le 1$ mirip dengan mengatakan bahwa **gradien energi** ke arah mana pun tidak boleh positif (tidak bisa naik lebih tinggi lagi).
    
- Jika ada arah yang "menurun" ($<1$), kita tidak bergerak ke sana (bobot nol). Kita hanya mendistribusikan massa pada titik-titik tumpu yang memberikan gaya reaksi seimbang ($=1$).
    

### Ringkasan Pembuktian Corollary 2

Penulis membuktikan ini dengan logika sederhana 3:

1. Portofolio $S^*$ adalah rata-rata tertimbang dari saham-saham: $S^* = \sum b_i^* X_i$.
    
2. Maka rasionya terhadap diri sendiri adalah 1:
    
    $$E \left( \frac{S^*}{S^*} \right) = 1$$
    
3. Kita bisa memecah $S^*$ di pembilang:
    
    $$E \left( \frac{\sum b_i^* X_i}{S^*} \right) = \sum b_i^* E \left( \frac{X_i}{S^*} \right) = 1$$
    
4. Perhatikan persamaan di atas: Ini adalah penjumlahan bobot ($b_i^*$) dikalikan nilai harapan ($E$).
    
5. Karena kita tahu dari kondisi 1 bahwa **semua** nilai harapan itu $\le 1$, maka satu-satunya cara agar hasil penjumlahannya menjadi persis 1 adalah jika:
    
    - Saham yang kita beli ($b_i^* > 0$) harus memiliki nilai harapan **tepat sama dengan 1**.
        
    - Jika ada yang nilainya $< 1$, bobotnya harus 0. Kalau tidak, totalnya akan terseret menjadi kurang dari 1.
        

Kesimpulan Section 3:

Kita sekarang punya alat lengkap:

1. **Theorem 2:** Mengubah masalah Logaritma menjadi masalah Linear.
    
2. **Corollary 2:** Memberi kita cara mengecek apakah portofolio kita sudah optimal atau belum cukup dengan melihat performa masing-masing saham penyusunnya.
    

Apakah analogi keseimbangan gaya dan penjelasan matematika sederhana di Corollary 2 ini bisa diterima? Jika ya, kita siap masuk ke **Section 4**, di mana "perang" yang sesungguhnya dimulai (menggabungkan semua senjata ini untuk melawan musuh).

---
---
---

# The $\phi$-Game for the Stock Market
### 4.1
 Mari kita masuk ke **Section 4: The $\phi$-Game for the Stock Market**.

Paragraf pertama dan kedua di bagian ini 1 adalah momen "penggabungan kekuatan". Penulis menggabungkan hasil dari "Duel Kotak Ajaib" (Section 2) dengan hasil dari "Keluarga Konveks" (Section 3).

Berikut adalah penjelasan bertahapnya:

### 1. Klaim Utama: Robustness (Ketangguhan)

Penulis membuka dengan klaim berani:

> _"We now show that the log optimal portfolio $b^*$ has short-term robustness properties..."* 2

Biasanya, orang berargumen bahwa strategi Log-Optimal ($b^*$) hanya bagus untuk jangka panjang ($t \to \infty$). Namun, penulis akan membuktikan bahwa strategi ini juga optimal untuk **satu kali main (single play)** melawan musuh.

### 2. Definisi Ulang Pemain

Penulis mengingatkan kembali "senjata" yang dimiliki pemain 3:

Setiap pemain melakukan dua keputusan terpisah:

1. **Keputusan Judi ($W$):** Memilih distribusi probabilitas "adil" ($G_i$). Ini seperti memilih seberapa agresif Anda bertaruh (dari Section 2).
    
2. **Keputusan Pasar ($b$):** Memilih saham ($b_i$). Ini menghasilkan modal $S_i = b_i' X$.
    

Modal akhir Anda adalah kombinasi keduanya: $\text{Total} = W \times S$.

### 3. Theorem 3: Teorema Pemisahan Variabel

Ini adalah hasil utama di Section 4. Mari kita lihat bunyi teoremanya 4:

Untuk memenangkan permainan dengan skor $\phi$, strategi optimalnya adalah:

- **Strategi Judi ($W^*$):** Gunakan solusi optimal dari permainan primitif (Section 2). Solusi ini bergantung pada $\phi$.
    
- **Strategi Saham ($b^*$):** Gunakan Portofolio Log-Optimal. Solusi ini **SAMA** untuk kedua pemain, dan **TIDAK** bergantung pada $\phi$.
    

Analogi Fisika: Pemisahan Variabel

Anda pasti familiar dengan teknik Separation of Variables dalam persamaan diferensial (misal: persamaan Schrödinger untuk atom Hidrogen). Fungsi gelombang dipecah menjadi bagian Radial ($R$) dan bagian Angular ($Y$).

$$\Psi(r, \theta, \phi) = R(r) Y(\theta, \phi)$$

Di paper ini, Strategi Optimal ($\Psi$) dipecah menjadi:

- **Bagian Pasar ($b^*$):** Ini seperti bagian Radial. Solusinya selalu Log-Optimal, tidak peduli bentuk "potensial" luarnya seperti apa.
    
- **Bagian Judi ($W^*$):** Ini seperti bagian Angular. Solusinya menyesuaikan dengan bentuk "potensial" ($\phi$).
    

### 4. Pembuktian Theorem 3 (Logika Inti)

Bagaimana penulis membuktikan bahwa kita bisa memisahkannya? Mereka menggunakan trik substitusi variabel yang cerdik di paragraf pembuktian 5.

Mari kita ikuti alurnya pelan-pelan:

1. Definisi Lawan Gabungan:
    
    Misalkan Anda (Player 1) melawan Player 2 yang menggunakan strategi sembarang ($W_2$ dan $S_2$).
    
    Penulis mendefinisikan variabel acak baru, sebut saja $Z$:
    
    $$Z = \frac{W_2 S_2}{S^*}$$
    
    (Perhatikan: $S^*$ adalah portofolio Log-Optimal).*
    
2. Cek Validitas ($Z \in \mathcal{W}$?):
    
    Apakah $Z$ adalah variabel acak yang "Adil"?
    
    - $E[W_2] \le 1$ (karena $W_2$ adil).
        
    - $E[S_2/S^*] \le 1$ (Ingat **Theorem 2** dan **Section 3**! Karena $S^*$ adalah Log-Optimal, dia mendominasi semua portofolio lain).
        
    - Karena independen, maka $E[Z] = E[W_2] \cdot E[S_2/S^*] \le 1$.
        
    - **Kesimpulan:** Ya, $Z$ adalah variabel "judi" yang sah.
        
3. Transformasi Payoff:
    
    Sekarang lihat fungsi skornya. Kita ingin membandingkan modal kita ($W_1 S^*$) dengan modal lawan ($W_2 S_2$):
    
    $$\text{Rasio} = \frac{W_1 S^*}{W_2 S_2} = \frac{W_1}{(W_2 S_2 / S^*)} = \frac{W_1}{Z}$$
    
4. Reduksi Masalah:
    
    Lihat bentuk $\frac{W_1}{Z}$. Ini persis kembali ke masalah Permainan Primitif di Section 2 (duel $W_1$ lawan $Z$).
    
    - Karena kita sudah tahu cara menang di Section 2 (pilih $W_1^*$ yang sesuai $\phi$), maka kita tinggal pakai solusi itu.
        
    - Bagian saham ($S^*$) "hilang" dari persamaan karena sudah terserap ke dalam definisi $Z$.
        

Kesimpulan Section 4:

Penulis berhasil membuktikan bahwa Anda tidak perlu pusing memikirkan strategi saham yang aneh-aneh untuk mengalahkan lawan.

Cukup lakukan dua hal:

1. Beli portofolio Log-Optimal ($S^*$). Ini membuat rasio $S_{lawan}/S_{kita}$ menjadi kecil ($E \le 1$).
    
2. Lakukan manajemen risiko ($W^*$) pada modal Anda sesuai toleransi risiko Juri ($\phi$).
    

Apakah logika "menyerap portofolio lawan ke dalam variabel Z" ini bisa dipahami? Inilah alasan kenapa Section 3 (Theorem 2) sangat vital; tanpa sifat $E(S/S^*) \le 1$, trik ini tidak akan bekerja.

---
---
---
# Multistage Market Games
## 5.1

Mari kita masuk ke **Section 5: Multistage Market Games**.

Ini adalah tahap di mana teori ini menjadi sangat kuat untuk aplikasi dunia nyata. Di bagian-bagian sebelumnya, kita hanya membahas investasi "sekali main" (satu periode). Sekarang, penulis memperluasnya ke **dimensi waktu** ($n$ periode)1.

Mari kita bedah paragraf awal dan konsep intinya:

### 1. Dari Pertempuran ke Peperangan

Penulis menyatakan bahwa di bab sebelumnya, pasar hanya memberikan satu peluang investasi. Sekarang, kita melihat skenario **Multistage** (Bertahap) 2:

- **Compounding (Bunga-berbunga):** Keuntungan hari ini diinvestasikan kembali besok.
    
- **Reallocation (Rebalancing):** Di setiap akhir hari, Anda boleh merombak susunan portofolio Anda berdasarkan informasi harga saham yang baru saja terjadi.
    

### 2. Definisi Strategi Sekuensial (Berturut-turut)

Di sini penulis mendefinisikan strategi bukan sebagai satu vektor $b$, melainkan sebagai **serangkaian fungsi keputusan** 3:

- Hari 1: Pilih $b_1$.
    
- Hari 2: Pilih $b_2(X_1)$ — keputusan boleh bergantung pada apa yang terjadi di Hari 1.
    
- Hari ke-$k$: Pilih $b_k(X_1, ..., X_{k-1})$ — keputusan boleh bergantung pada seluruh sejarah pasar.
    

_Analogi Fisika:_ Ini seperti mengemudikan roket. Anda tidak hanya mengunci setir di awal peluncuran. Di setiap detik, Anda melakukan koreksi arah berdasarkan posisi terakhir Anda (_feedback loop_).

### 3. Theorem 4: Prinsip "Greedy" yang Cerdas

Penulis kemudian mengajukan Theorem 44.

Intinya: Bagaimana cara memenangkan perang jangka panjang ini? Apakah kita perlu strategi rumit yang mengorbankan hari ini demi masa depan?

**Jawabannya:** Tidak. Strategi optimalnya adalah **Myopic (Rabun Jauh)** dalam artian positif.

- Di setiap langkah ke-$k$, pilihlah portofolio yang memaksimalkan **Ekspektasi Logaritma Kondisional** saat itu juga ($E[\ln b_k' X_k | \text{Sejarah}]$).
    
- Lakukan yang terbaik untuk "hari ini", lupakan "besok". Jika Anda memenangkan setiap pertempuran harian, Anda otomatis memenangkan peperangan total.
    

### 4. Pembuktian: Kenapa Bisa Begitu?

Penulis menggunakan sifat matematika logaritma yang indah untuk membuktikan ini 5:

$$E \ln S_n = E \ln \left( \prod_{k=1}^n b_k' X_k \right) = \sum_{k=1}^n E(\ln b_k' X_k)$$

- Logaritma mengubah **Perkalian** (Compounding) menjadi **Penjumlahan**.
    
- Untuk memaksimalkan total penjumlahan ($\sum$), Anda cukup memaksimalkan setiap suku ($E \ln \dots$) secara terpisah.
    
- Oleh karena itu, Anda tidak perlu khawatir bahwa keputusan "maksimumkan log hari ini" akan merusak peluang Anda di masa depan. Matematikanya menjamin bahwa untung maksimal hari ini adalah kontribusi terbaik untuk total untung akhir.
    

Koneksi ke Section 3 (Convex Families):

Ingat Contoh 3 di Section 3 tadi? Penulis sudah membuktikan bahwa himpunan "Portofolio Sekuensial" adalah keluarga konveks6.

Karena konveks, maka Theorem 2 berlaku: Strategi yang memaksimalkan Log ($S_n^*$) pasti memenuhi $E(S_n/S_n^*) \le 1$.

Karena memenuhi syarat linear itu, maka Theorem 3 (pemisahan variabel) juga berlaku.

Kesimpulan Section 5:

Penulis menegaskan bahwa strategi Log-Optimal bersifat Universal terhadap Waktu.

Tidak peduli apakah Anda trading untuk 1 hari atau 10 tahun, dan tidak peduli seberapa fluktuatif pasarnya, resepnya tetap sama:

1. Lihat data masa lalu untuk memprediksi probabilitas hari ini.
    
2. Pilih portofolio yang memaksimalkan $E[\ln]$ untuk hari ini.
    
3. Ulangi besok.
    

Bagian ini cukup intuitif bagi fisikawan karena mirip dengan **Prinsip Hamilton** atau **Action Principle** di mana lintasan optimal seringkali bisa dipecah menjadi optimasi lokal di setiap segmen waktu (tergantung sistemnya, tapi di sini sifat aditif Logaritma membuatnya sangat bersih).

Apakah konsep "Optimasi Bertahap" ini bisa diterima? Jika ya, kita siap masuk ke **Section 6**, yang membahas skenario psikologis yang lebih rumit: Bagaimana jika kita melihat tumpukan uang lawan kita secara _real-time_?

---
---
---
# Example: Posterior Randomization Based on Relative Capital

## 6.1

Mari kita masuk ke **Section 6: Example: Posterior Randomization Based on Relative Capital**.

Ini adalah bagian yang paling psikologis dan "manusiawi". Di sinilah intuisi kita sebagai manusia sering bertentangan dengan matematika.

Mari kita bedah paragraf pembukanya 1:

### 1. Skenario Baru: "Mengintip Skor Lawan"

Hingga saat ini, strategi yang kita bahas bersifat "Pasang dan Lupakan". Anda menetapkan aturan ($b^*$ dan $W^*$), lalu membiarkan sistem berjalan.

Di Section 6, penulis mengubah aturannya menjadi **Observasi Penuh**:

> _"Now let us allow the players to observe each other's progress over many rounds..."_2.

- **Situasinya:** Anda sedang balapan investasi. Di tengah jalan (misal, ronde ke-5), Anda menengok ke sebelah.
    
- **Pengamatan:** Anda melihat lawan Anda (Player 2) sedang untung besar, sementara Anda sedang rugi. Rasio modal kalian ($S_1/S_2$) jatuh drastis.
    
- **Pertanyaannya:** _"How do competitive investment decisions change?"_3.
    
    - Apakah Anda harus panik?
        
    - Apakah Anda harus mengubah strategi menjadi lebih agresif (mengambil risiko tinggi) untuk mengejar ketertinggalan? ("Jockeying for position").
        
    - Atau apakah Anda tetap tenang dengan rencana awal?
        

### 2. Mekanisme Permainan (Ronde demi Ronde)

Penulis merinci urutan mainnya 4:

1. **Awal:** Randomisasi awal ($W^{(0)}$).
    
2. **Investasi:** Pilih portofolio ($b^{(1)}$).
    
3. **Pengungkapan:** Pasar ($X_1$) bergerak. Hasilnya terlihat.
    
4. **Observasi:** Kedua pemain melihat modal satu sama lain.
    
5. **Reaksi:** Pemain boleh melakukan randomisasi lagi atau mengubah portofolio ($b^{(2)}$) berdasarkan posisi mereka saat itu.
    

### 3. Intuisi vs Matematika

Secara intuitif, kita berpikir: _"Informasi adalah kekuatan. Kalau saya tahu saya sedang kalah, saya harus mengubah strategi untuk membalikkan keadaan."_

Namun, paragraf selanjutnya 5 langsung memberikan _spoiler_ (bocoran) yang mengejutkan:

> _"...we shall find that the obvious first guess at optimal play is minimax... all without regard to the opponent's fortunes."_

Penulis memberi isyarat bahwa strategi terbaik ternyata adalah **TIDAK PEDULI** pada nasib lawan.

- Meskipun Anda melihat lawan Anda menjadi kaya raya, matematika menyarankan Anda untuk tetap memegang portofolio Log-Optimal ($b^*$) dan tidak mengubah profil risiko judi Anda sembarangan.
    
- Penulis menyebut bahwa mencoba memanipulasi nasib berdasarkan posisi lawan (_conditional play_) seringkali justru menjadi bumerang.
    

Analogi Fisika:

Bayangkan dua partikel dalam sebuah wadah gas.

- Partikel A (Anda) ingin memiliki energi kinetik lebih tinggi dari Partikel B (Lawan).
    
- Strategi Section 6 bertanya: "Jika saya melihat Partikel B tiba-tiba melesat cepat, apakah saya harus mengubah lintasan saya secara drastis?"
    
- Jawabannya tampaknya: "Tidak. Ikuti saja jalur gradien termal yang paling efisien (Log-Optimal). Mencoba bermanuver aneh-aneh hanya akan membuang energi (friksi/sub-optimal)."
    

Apakah skenario "Psikologi Mengejar Ketertinggalan" ini bisa dipahami? Penulis akan membuktikan secara matematis mengapa intuisi "mengejar" itu salah di paragraf-paragraf berikutnya.

---
---
## 6.2
Tentu, mari kita lanjutkan ke bagian di mana penulis memberikan contoh konkret dari teori permainan judi murni untuk mengilustrasikan "intuisi" kita sebelum membantahnya di konteks saham.

Paragraf-paragraf ini 1 membahas **"Apa yang terjadi jika modal kita tidak seimbang?"**

### 1. Flashback: Kasus Judi Murni (Bell & Cover 1980)

Penulis merujuk ke paper mereka sebelumnya untuk memberikan konteks. Bayangkan dua penjudi yang hanya melempar dadu (tanpa saham) dengan tujuan memaksimalkan peluang menang $P(W_1 \ge W_2)$2.

- Jika Modal Sama (1 vs 1):
    
    Strategi optimalnya adalah menjadi "Agresif tapi Terukur". Keduanya memilih distribusi Uniform [0, 2].
    
    - _Analogi:_ Anda bertaruh sedemikian rupa sehingga uang Anda bisa jadi apa saja antara $0 sampai $2 secara acak. Ini strategi terbaik untuk mencegah lawan memprediksi Anda.
        
- Jika Modal Tidak Sama ($u$ vs 1):
    
    Di sini menariknya. Misalkan Anda (Player 1) punya modal $u > 1$ (Anda sedang memimpin/kaya), dan lawan punya 1 (dia tertinggal).
    
    Penulis menunjukkan solusinya menjadi asimetris 3:
    
    - **Si Pemimpin (Anda):** Tetap bermain standar (Uniform). Anda "mempertahankan posisi".
        
    - **Si Pengejar (Lawan):** Strateginya berubah drastis menjadi campuran antara **Bangkrut total (0)** atau **Menang Besar**.
        
        - _Kenapa?_ Karena dia tertinggal, bermain aman pasti kalah. Satu-satunya cara menang adalah mengambil risiko ekstrem ("Go Big or Go Home"). Distribusi probabilitasnya menjadi "cacat" (memiliki massa probabilitas di titik 0).
            

### 2. Penerapan ke Pasar Saham

Penulis kemudian membawa logika ini kembali ke pasar saham 4.

Bayangkan skenarionya:

1. Kalian memilih portofolio ($b_1, b_2$).
    
2. Pasar bergerak ($X$).
    
3. Hasilnya: Modal Anda $S_1$ dan modal lawan $S_2$.
    
4. Sekarang, kalian boleh melakukan "judi terakhir" ($W$) menggunakan informasi rasio modal tersebut ($S_1/S_2$).
    

Pertanyaan Inti:

Berdasarkan logika judi murni tadi, jika portofolio saya kalah (saya jadi "Si Pengejar"), bukankah seharusnya saya sekarang melakukan judi ekstrem ($W_{ekstrem}$) untuk membalikkan keadaan? Dan jika saya menang, bukankah saya harus main aman?

Inilah yang disebut **"Conditionally Randomized Market Game"** (Permainan Pasar dengan Randomisasi Bersyarat). Strategi judi Anda ($W$) sekarang bergantung pada fungsi $(x, S_1, S_2)$ 5.

### 3. Persiapan "Plot Twist"

Penulis menyusun persamaan payoff yang sangat rumit di persamaan (6.2) yang memperhitungkan semua ketergantungan ini6.

Namun, mereka memberi petunjuk (seperti yang kita bahas sebelumnya) bahwa meskipun secara intuisi "Si Pengejar" harusnya main gila, ternyata di pasar saham ada **mekanisme penyeimbang otomatis**.

Apa mekanisme itu? Itu adalah sifat Log-Optimal.

Karena portofolio Log-Optimal ($b^*$) selalu membuat $E(S_{lawan}/S_{kita}) \le 1$, maka secara statistik, lawan (si pengejar) tidak pernah benar-benar memiliki "peluang curang" yang cukup besar untuk membenarkan strategi judi ekstrem tersebut, asalkan Anda tetap setia pada $b^*$.

Ringkasan Bagian Ini:

Penulis berkata: "Di judi biasa, orang miskin harus main nekat lawan orang kaya. Mari kita lihat apakah di pasar saham orang yang portofolionya rugi juga harus main nekat. Kami sudah siapkan model matematikanya yang memperbolehkan 'main nekat' (conditional randomization)."

Selanjutnya, di Lemma dan Theorem 5, mereka akan membuktikan bahwa "main nekat" itu tidak perlu.

Apakah perbedaan perilaku antara "Si Pemimpin" dan "Si Pengejar" dalam contoh judi murni tadi bisa dipahami? Ini konsep _game theory_ klasik: perilaku pemain berubah tergantung posisi relatifnya.

## 6.3
Tentu, mari kita terjemahkan kedua persamaan matematika yang tampak rumit ini ke dalam bahasa manusia yang membumi. Keduanya menceritakan drama psikologis antara "Si Menang" dan "Si Kalah".

### Persamaan 6.1: Strategi "Kamikaze" Si Miskin

1

$$\text{Strategi Si Kalah} \approx \text{Sebagian Besar Bangkrut} + \text{Sedikit Peluang Kaya Raya}$$

Bayangkan Anda sedang bermain judi lempar koin melawan Sultan.

- **Kondisi:** Sultan punya uang **$10** ($u=10$), Anda hanya punya **$1**.
    
- **Masalah:** Kalau Anda main aman (taruhan kecil), Anda pasti kalah pelan-pelan karena modal Sultan jauh lebih besar.
    

Terjemahan Bahasa Sehari-hari Persamaan 6.1:

Rumus ini berkata kepada Anda: "Kawan, kau sudah kalah telak. Jangan main aman."

Strategi terbaik menurut rumus ini adalah:

1. **Peluang 90% (1 - 1/u):** Anda langsung **menyerah dan bangkrut** (uang jadi 0). Terima kekalahan.
    
2. **Peluang 10%:** Anda melakukan taruhan **"All-in" yang sangat nekat** dengan harapan uang Anda melonjak dari $1 menjadi $20 (2x lipat kekayaan Sultan).
    

**Intinya:** "Go Big or Go Home." Rumus ini adalah matematisasi dari keputusasaan. Daripada kalah perlahan, lebih baik ambil risiko kematian (kebangkrutan) yang tinggi demi peluang kecil untuk membalikkan keadaan secara drastis.

---

### Persamaan 6.2: Drama "Cuci Piring" Pasca Pasar

2

$$E\phi(\dots) = \iiint \text{Skor} \times \text{Peluang Pasar} \times \text{Reaksi Anda} \times \text{Reaksi Lawan}$$

Persamaan ini menjelaskan situasi permainan yang sudah berevolusi.

Konteks Cerita:

Bayangkan kita berdua sudah membeli saham pagi ini. Sore hari, pasar tutup.

- Saham Anda hancur (Rugi).
    
- Saham saya terbang (Untung).
    
- Kita berdua melihat saldo masing-masing di layar.
    

Terjemahan Bahasa Sehari-hari Persamaan 6.2:

Persamaan ini bertanya: "Setelah melihat nasib sahammu yang hancur sore ini, judi macam apa yang akan kau lakukan di malam hari untuk memperbaiki skor?"

Komponen kuncinya adalah: **$dG(w | x, S_1, S_2)$**.

- **Bahasa Matematis:** Distribusi probabilitas $w$ bersyarat terhadap $x$ (pasar) dan $S$ (modal).
    
- **Bahasa Manusia:** "Keputusan panik". Ini adalah strategi judi yang Anda pilih **SETELAH** Anda tahu Anda sedang kalah.
    

Intinya:

Ini adalah rumus yang menghitung skor akhir pertandingan, dengan memperhitungkan fakta bahwa pemain boleh mengubah taktik di tengah jalan (banting setir) berdasarkan posisi menang/kalah mereka saat itu.

Apakah terjemahan "Strategi Kamikaze" dan "Keputusan Panik" ini membantu memperjelas makna di balik simbol-simbol tersebut? Jika ya, kita bisa lanjut melihat bagaimana penulis menyelesaikan drama ini.

## 6.4
Tentu. Mari kita masuk ke resolusi dari drama psikologis ini: **Lemma dan Theorem 5**.

Di sini penulis mematahkan intuisi "Si Pengejar" (Kamikaze) yang kita bahas tadi dengan matematika yang sangat elegan.

### 1. Lemma: Hukum "Kepuasan yang Menurun"

Sebelum membuktikan teorema utama, penulis menyisipkan sebuah **Lemma** (teorema bantu)1.

> _"Lemma... $v_{\phi}(u)$ is a concave nondecreasing function of u."_

Mari kita terjemahkan:

- **$v_{\phi}(u)$:** Ini adalah "Nilai Kemenangan" jika Anda mulai dengan modal $u$ sementara musuh mulai dengan modal 1.
    
- **Concave (Cekung):** Ini berarti grafik nilai kemenangannya melengkung ke bawah.
    
    - Menambah modal dari 1 ke 2 memberikan kenaikan peluang menang yang besar.
        
    - Menambah modal dari 100 ke 101 memberikan kenaikan peluang menang yang sangat kecil.
        

Kenapa ini penting?

Sifat cekung ini adalah "rem" bagi keinginan untuk berjudi secara liar. Karena fungsi nilainya cekung, memecah modal menjadi taruhan berisiko (rata-rata terbobot) tidak akan memberikan nilai rata-rata yang lebih tinggi daripada memegang modal itu dengan stabil (Ingat ketidaksamaan Jensen: Rata-rata fungsi cekung $\le$ Fungsi dari rata-rata).

### 2. Theorem 5: Kemenangan Si "Buta"

Inilah hasil yang mengejutkan itu.

Penulis menyatakan bahwa untuk memenangkan permainan pasar yang rumit ini (di mana Anda boleh mengintip dan mengubah strategi), strategi terbaiknya adalah 2:

1. **Portofolio ($b^*$):** Tetap gunakan Log-Optimal. Jangan diganti.
    
2. **Judi ($W^*$):** Gunakan strategi randomisasi yang **sama persis** dengan strategi di Section 2 (permainan primitif). Gunakan distribusi yang disiapkan _sebelum_ melihat hasil pasar.
    

Terjemahan Bebas:

"Meskipun Anda melihat musuh Anda jadi kaya raya dan Anda tertinggal jauh, JANGAN PANIK. Jangan ubah strategi portofolio Anda menjadi agresif, dan jangan ubah strategi judi Anda menjadi nekat. Tutup mata Anda, dan tetaplah pada rencana awal ($b^*$ dan $W^*$). Itu sudah cukup untuk mencapai hasil optimal (Minimax)."

### 3. Mengapa Intuisi Kita Salah?

Penulis menjelaskan paradoks ini di paragraf diskusi 3.

Kenapa kita tidak perlu strategi "Kamikaze" (bersyarat) untuk mengejar ketertinggalan?

Jawabannya ada pada kekuatan Portofolio Log-Optimal ($S^*$).

- Jika **kedua pemain** rasional, mereka berdua akan memegang $S^*$.
    
- Akibatnya, rasio modal mereka akan selalu $S^*/S^* = 1$ (Modal bergerak bersamaan naik-turunnya).
    
- Karena rasio modal selalu 1, tidak ada yang "tertinggal" atau "memimpin". Mereka kembali ke permainan primitif seimbang (1 lawan 1). Jadi strategi "tanpa ngintip" sudah cukup.
    

Bagaimana jika musuh curang/bodoh?

Bagaimana jika musuh menyimpang dari $S^*$ untuk mencoba keberuntungan?

- Matematika di Section 3 sudah membuktikan $E(S_{musuh}/S^*) \le 1$.
    
- Musuh yang menyimpang dari $S^*$ justru sedang "bunuh diri" pelan-pelan (modal relatifnya menyusut secara statistik).
    
- Jadi, Anda tidak perlu bermanuver aneh-aneh. Cukup tetap di jalur $S^*$, dan biarkan musuh hancur sendiri oleh hukum matematika. Penulis menyebut: _"Any deviation from $S^*$ ... hurts the player."*4.
    

### 4. Catatan Kaki: Minimax vs Admissible

Di paragraf terakhir Section 6 5, penulis memberikan sedikit nuansa:

- Strategi "Buta" ($W_{\phi}^*$) adalah strategi **Minimax**. Artinya, ini adalah strategi pertahanan terbaik. Anda dijamin tidak kalah (nilai permainan terjaga).
    
- Namun, Strategi "Ngintip" ($W(x, S_1, S_2)$) secara teknis lebih **Tajam (Sharper)**.
    
    - Jika musuh main sempurna, hasilnya sama saja.
        
    - Tapi jika musuh main buruk, strategi "Ngintip" bisa menghukum musuh lebih sadis dan menang lebih banyak.
        
    - Jadi, strategi "Ngintip" _mendominasi_ strategi "Buta", tapi strategi "Buta" sudah cukup untuk _tidak kalah_.
        

Kesimpulan Section 6:

Drama psikologis selesai. Pesan moralnya bagi investor: Disiplin mengalahkan Emosi.

Ketika portofolio Anda merah dan portofolio teman Anda hijau, matematika menyarankan untuk tetap disiplin pada strategi pertumbuhan maksimal ($b^*$) daripada banting setir menjadi spekulan nekat.

Cukup jelas bagian anti-klimaks dari drama ini? Jika ya, kita bisa masuk ke **Section 7: Conclusions** untuk membungkus semua pemahaman ini.

---
---
## 6.5
Tentu, ini adalah bagian "dapur rekaman" di mana penulis membuktikan secara teknis kenapa strategi "Tutup Mata" (Unconditional) itu valid.

Mari kita bedah pembuktian di bawah Theorem 5 ini 1.

### 1. Tujuan Pembuktian: "Teknik Sandwich"

Penulis ingin membuktikan bahwa strategi pasangan $(b^*, W^*)$ adalah titik keseimbangan (**Saddlepoint**).

Cara membuktikannya adalah dengan menunjukkan bahwa strategi ini terjepit (di-sandwich) di antara dua kondisi ekstrem, seperti yang ditulis di **Persamaan (6.4)**:

$$E\phi(\text{Saya Curang}) \le \mathbf{v_{\phi}} \le E\phi(\text{Musuh Curang})$$

- **Tengah ($v_{\phi}$):** Nilai murni permainan jika kedua pihak main jujur dan optimal (Log-Optimal + Judi Standar).
    
- **Kiri:** Jika **Saya** mencoba "curang" (mengintip posisi lawan dan mengubah strategi $W$ secara licik), skor saya ternyata **tidak bisa lebih tinggi** dari $v_{\phi}$. (Artinya: Usaha curang saya percuma).
    
- **Kanan:** Jika **Musuh** mencoba "curang" (mengintip posisi saya dan mengubah strategi $W$ secara licik), skor saya **tidak bisa ditarik turun** di bawah $v_{\phi}$. (Artinya: Usaha curang musuh tidak mempan).
    

Jika Kiri $\le$ Tengah $\le$ Kanan terbukti, maka strategi "Tengah" (Diam/Standar) adalah yang terbaik.

---

### 2. Bedah Persamaan (6.5): Mengapa "Kecurangan" Tidak Berguna?

Penulis fokus membuktikan sisi Kiri persamaan sandwich tadi. Mari kita lihat **Persamaan (6.5)**:

$$E\left(\frac{W_{1}(X,S_{1},S^{*})S_{1}}{S^{*}}\right) \le 1$$

Mari terjemahkan simbol-simbol ini ke bahasa sehari-hari:

- **$S^*$ (Penyebut):** Ini adalah **Standar Emas**. Portofolio Log-Optimal yang dipegang oleh Musuh (yang main disiplin).
    
- **$S_1$ (Pembilang):** Ini portofolio sembarangan yang **Saya** pilih (mencoba menyimpang dari standar).
    
- **$W_1(\dots)$:** Ini adalah "Judi Canggih". Saya tidak asal lempar dadu. Saya melempar dadu setelah melihat kondisi pasar ($X$) dan membandingkan modal saya ($S_1$) dengan musuh ($S^*$). Saya mencoba merekayasa keberuntungan.
    

**Terjemahan Bahasa Sehari-hari Persamaan (6.5):**

> "Meskipun Anda mencoba menggabungkan **Portofolio Aneh ($S_1$)** dengan **Judi Licik yang Terukur ($W_1$)**, kekuatan gabungan 'senjata' Anda itu secara rata-rata tetap **LEBIH LEMAH atau SAMA** ($\le 1$) dibandingkan dengan musuh yang hanya diam memegang **Standar Emas ($S^*$)**."

Kenapa bisa begitu?

Penulis memecahnya menjadi dua fakta 2:

1. **Judi itu Adil:** Rata-rata dari $W_1$ (walaupun licik/bersyarat) tetaplah 1. Anda tidak bisa menciptakan probabilitas dari udara kosong.
    
2. Portofolio itu Lemah: Ingat Theorem 2 di Section 3. Rasio portofolio apapun ($S_1$) terhadap Log-Optimal ($S^*$) rata-ratanya $\le 1$.
    
    $$E[S_1/S^*] \le 1$$
    

Jadi: $(\text{Judi } 1) \times (\text{Portofolio } \le 1) = \text{Hasil } \le 1$.

---

### 3. Bedah Persamaan (6.6): Kesimpulan Akhir

Setelah membuktikan bahwa senjata "curang" tadi ternyata lemah ($\le 1$), penulis memasukkannya kembali ke fungsi skor $\phi$ di **Persamaan (6.6)**:

$$E\phi\left(\frac{\text{Senjata Curang Saya}}{\text{Judi Standar Musuh}}\right) \le v_{\phi}$$

**Terjemahan Bahasa Sehari-hari:**

> "Karena senjata racikan saya (gabungan portofolio + judi ngintip) terbukti secara statistik lebih lemah atau sama dengan 1, maka saat diadu melawan strategi judi standar musuh ($W_{2\phi}^*$), skor rata-rata saya **TIDAK MUNGKIN** menembus batas nilai wajar ($v_{\phi}$)."

Intisari Proof ini:

Proof ini adalah "pukulan telak" bagi trader yang merasa pintar (overconfident).

Matematika berkata:

"Hai Trader, kamu pikir dengan mengamati pasar ($X$) lalu mengubah-ubah taruhanmu ($W_{conditional}$) saat sedang rugi/untung, kamu bisa mengalahkan pasar?

Tidak. Karena apapun manuver yang kamu lakukan, selama portofoliomu bukan $S^*$, kamu sedang melawan arus gravitasi matematika ($E \le 1$). Manuver canggihmu tidak bisa menutupi kelemahan fundamental portofoliomu."

Inilah sebabnya penulis menyimpulkan: **Unconditional Randomization is sufficient.** (Main buta saja sudah cukup).

Apakah penjelasan "Senjata Curang yang tumpul" ini membantu memahami alur pembuktiannya? Jika ya, kita siap meluncur ke **Section 7 (Conclusions)**.

---
---
---
# Conclusions
Mari kita masuk ke bagian penutup, **Section 7: Conclusions**.

Ini adalah "bungkusan akhir" dari paper ini. Penulis merangkum temuan mereka menjadi satu filosofi investasi yang sangat kuat dan praktis.

Mari kita bedah tiga poin utama dari kesimpulan ini:

### 1. Resep Universal untuk Segala Situasi

Penulis menegaskan kembali kekuatan dari strategi Log-Optimal ($b^*$).

Bayangkan Anda adalah seorang manajer investasi. Bos Anda (Klien) mungkin punya keinginan yang aneh-aneh:

- "Saya ingin menang 2x lipat dari lawan."
    
- "Saya cuma ingin asal menang saja."
    
- "Permainannya mungkin berakhir besok, atau 10 tahun lagi."
    

Penulis menyimpulkan: **Anda TIDAK PERLU tahu apa keinginan Bos Anda dan kapan permainan berakhir.** 1

Strategi harian Anda tetap sama:

> _"The investor does not need to know $\phi$ or $n$ in order to choose his portfolio at each time."_ 2

Cukup bangun pagi, pilih portofolio yang memaksimalkan pertumbuhan logaritmik ($E \ln S$), lalu tidur nyenyak. Urusan "keinginan Bos" ($\phi$) hanya perlu dipikirkan nanti di tahap akhir lewat randomisasi (jika perlu), tapi itu tidak mengubah cara Anda memilih saham hari ini.

### 2. Kapan Perlu Berjudi, Kapan Tidak

Penulis membedakan dua skenario 3:

- **Skenario A (Fungsi Cekung/Linear):** Jika tujuan Bos Anda masuk akal (seperti fungsi $S_1/S_2$ atau Logaritma), maka **Tidak Ada Randomisasi ($W$) yang diperlukan**. Strategi murni Log-Optimal sudah cukup untuk mencapai nilai permainan.
    
- **Skenario B (Fungsi Sembarang):** Jika tujuan Bos Anda aneh (misal fungsi tangga/biner "Menang atau Mati"), Anda tetap pakai portofolio Log-Optimal, tapi di detik terakhir Anda tambahkan "bumbu" randomisasi ($W$) yang sesuai.
    

### 3. Alasan Fisis: "Jangkauan yang Adil" (_Fair Reach_)

Di paragraf terakhir, penulis memberikan intuisi fisik kenapa $S^*$ begitu dominan 4.

Mereka menggunakan argumen rasio:

$$E \left( \frac{S_n}{S_n^*} \right) \le 1$$

Penulis menyebut ini sebagai **"Fair Reach"** (Jangkauan yang Adil).

Analogi Fisika:

Bayangkan $S_n^*$ (Log-Optimal) sebagai sebuah "Planet Raksasa" dengan gravitasi yang kuat.

Strategi lain ($S_n$) adalah "Satelit".

- Satelit mungkin kadang-kadang terbang sedikit lebih tinggi dari orbit Planet (rasio > 1 sesaat).
    
- Tapi hukum gravitasi matematika ($E \le 1$) menjamin bahwa Satelit itu tidak akan pernah bisa lepas dari orbit dan terbang menjauh secara permanen meninggalkan Planet.
    
- Secara rata-rata, semua strategi lain akan selalu "tertarik" kembali ke bawah performa $S_n^*$.
    

Itulah sebabnya penulis menutup dengan kalimat:

> _"So it is not surprising that log optimal portfolios behave well in the competitive investment game."_ 5

---

### **Rangkuman Akhir Seluruh Paper untuk Anda**

Paper ini menjawab pertanyaan: **"Bagaimana cara mengalahkan investor lain?"**

1. **Mitos:** Anda harus mengambil risiko gila-gilaan atau mengubah strategi secara dinamis saat melihat lawan untung besar.
    
2. **Fakta:** Strategi terbaik adalah fokus pada diri sendiri.
    
3. **Metode:**
    
    - Anggap pasar sebagai sistem yang berkembang biak secara multiplikatif.
        
    - Satu-satunya cara memaksimalkan hasil jangka panjang adalah memaksimalkan **laju pertumbuhan logaritmik** ($E \ln S$).
        
    - Matematika membuktikan bahwa strategi ini ($S^*$) memiliki sifat "Supermartingale" ($E[S_{lain}/S^*] \le 1$).
        
    - Akibatnya, strategi ini secara otomatis menjadi strategi pertahanan terbaik (**Minimax**) melawan musuh manapun, dengan tujuan kemenangan apapun ($\phi$).
        

Saran Tindakan untuk Anda (Next Step):

Paper ini sangat teoritis. Jika Anda ingin menerapkannya, tantangannya adalah menghitung $b^*$ (vektor bobot) itu sendiri. Menghitung $E \ln (b'X)$ membutuhkan estimasi distribusi probabilitas saham $X$ yang akurat.

Apakah Anda ingin saya jelaskan sedikit tentang **Bagaimana cara menghitung/mengestimasi $b^*$ dalam prakteknya** (seperti yang disinggung di referensi Cover 1984), atau kita cukupkan pembahasan bedah paper ini sampai di sini?