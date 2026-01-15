# INTRODUCTION
## 1.1

Tentu, ide yang sangat bagus. Membaca _paper_ akademis secara bertahap adalah cara terbaik untuk benar-benar memahami isinya.

Mari kita mulai bedah **Paragraf Pertama dari Bagian I. INTRODUCTION**.

Paragraf ini berfungsi sebagai fondasi yang menjelaskan **"Apa masalahnya?"** dan **"Mengapa kita butuh komputer kuantum untuk menyelesaikannya?"**. Berikut adalah penjelasan perlahan mengenai setiap konsep yang muncul di paragraf ini dan kontribusinya terhadap keseluruhan _paper_:

### 1. Optimisasi Portofolio (_Portfolio Optimization_)

- **Konsep:** Ini adalah masalah mendasar di dunia keuangan. Tujuannya adalah mengalokasikan modal ke berbagai aset (saham, obligasi, dll.) sedemikian rupa sehingga keuntungan (_return_) menjadi maksimal, sementara risiko (_risk_) menjadi minimal1111.
    
- **Kontribusi di Paper:** Ini adalah **kasus studi utama**. Paper ini tidak hanya berbicara teori kuantum abstrak, tetapi menerapkannya untuk memecahkan masalah nyata ini. Nanti di dalam paper, penulis akan menggunakan data saham sungguhan (saham China A-shares dan saham AS) untuk menguji algoritma mereka2.
    

### 2. QUBO (_Quadratic Unconstrained Binary Optimization_)

- **Konsep:** Paragraf ini menyatakan bahwa masalah portofolio bisa diformulasikan menjadi masalah QUBO3.
    
    - **Quadratic:** Fungsi matematikanya melibatkan variabel kuadrat (pangkat dua).
        
    - **Unconstrained:** Tidak ada batasan "keras" (biasanya batasan dimasukkan ke dalam fungsi tujuan sebagai penalti).
        
    - **Binary:** Variabelnya hanya bernilai 0 atau 1. Dalam konteks portofolio, ini sering kali berarti "beli" (1) atau "tidak beli" (0) aset tertentu4.
        
- **Kontribusi di Paper:** QUBO adalah **jembatan penerjemah**. Komputer kuantum (khususnya yang menggunakan prinsip fisika Hamiltonian) tidak "mengerti" konsep "uang" atau "saham" secara langsung. Mereka mengerti energi dan spin. Dengan mengubah masalah keuangan menjadi rumus matematika QUBO, masalah ini nantinya bisa diubah lagi menjadi _Ising Model_ (sistem spin fisika) yang bisa diselesaikan oleh algoritma kuantum5.
    

### 3. NP-hard & Intraktabilitas Komputasi (_Computational Intractability_)

- **Konsep:** Masalah QUBO dikategorikan sebagai _NP-hard_. Artinya, semakin banyak jumlah aset (saham) yang ingin dioptimalkan, waktu yang dibutuhkan komputer klasik untuk menemukan solusi terbaik akan meningkat secara eksponensial. Untuk jumlah aset yang sangat besar, komputer biasa (klasik) hampir mustahil menyelesaikannya dalam waktu wajar6.
    
- **Kontribusi di Paper:** Ini adalah **motivasi penelitian**. Jika komputer klasik bisa menyelesaikan masalah ini dengan mudah, paper ini tidak akan diperlukan. Fakta bahwa masalah ini sulit bagi komputer klasik menjadi alasan kuat mengapa penulis mengusulkan penggunaan metode alternatif (kuantum).
    

### 4. Komputasi Kuantum (_Quantum Computing_)

- **Konsep:** Teknologi yang menggunakan prinsip mekanika kuantum untuk melakukan perhitungan. Paragraf ini menyebutkan bahwa kuantum menawarkan potensi untuk menyelesaikan masalah QUBO secara lebih efisien7.
    
- **Kontribusi di Paper:** Ini adalah **solusi yang ditawarkan**. Paper ini secara spesifik akan mengeksplorasi algoritma kuantum tertentu (VQE) untuk mengatasi kesulitan (_NP-hard_) yang disebutkan di atas. Penulis mengklaim bahwa pendekatan mereka bisa memberikan solusi berkualitas tinggi untuk masalah yang sulit ini8.
    

Ringkasan Paragraf 1:

Penulis sedang membangun argumen: "Ada masalah keuangan penting (Portofolio) -> Kita bisa tulis masalah ini dalam bahasa matematika (QUBO) -> Tapi matematika ini terlalu sulit dihitung komputer biasa jika datanya banyak (NP-hard) -> Maka, kita butuh Komputer Kuantum."

Apakah penjelasan untuk paragraf pertama ini sudah cukup jelas? Jika sudah, kita bisa lanjut ke paragraf kedua di mana mereka mulai membahas algoritma spesifiknya (VQE dan QAOA).

---
---
## 1.2
Tentu, mari kita lanjut membedah **Paragraf Kedua dari Bagian Introduction**.

Jika paragraf pertama mendefinisikan "Masalah" (Portofolio & QUBO), paragraf kedua ini mendefinisikan **"Alat"** yang tersedia untuk menyelesaikannya saat ini.

Kalimat kuncinya ada di sini:

> _"Among the quantum algorithms, the Variational Quantum Eigensolver (VQE) and the Quantum Approximate Optimization Algorithm (QAOA) are two promising candidates particularly well-suited for execution on Noisy Intermediate-Scale Quantum (NISQ) devices."_ 1

Berikut adalah penjelasan perlahan untuk konsep-konsep "alat" ini:

### 1. VQE (Variational Quantum Eigensolver) & QAOA (Quantum Approximate Optimization Algorithm)

- **Konsep:** Ini adalah dua jenis **algoritma kuantum** yang paling populer saat ini.
    
    - Bayangkan mereka sebagai "resep" pemrograman. Tidak seperti algoritma kuantum murni (seperti algoritma Shor untuk faktorisasi) yang membutuhkan komputer kuantum sempurna, VQE dan QAOA bersifat **Hibrida (Hybrid)**.
        
    - **Cara kerja:** Mereka menggunakan komputer kuantum untuk bagian yang sulit (menghitung energi sistem), lalu memberikan hasilnya ke komputer klasik (biasa) untuk dioptimalkan, lalu dikembalikan lagi ke komputer kuantum. Proses ini berulang-ulang (looping) sampai ketemu hasil terbaik.
        
- **Kontribusi di Paper:** Penulis secara spesifik memilih **VQE** sebagai fokus utama penelitian ini2222. Mereka menyebutkan QAOA sebagai pembanding atau alternatif yang populer, tetapi paper ini akan mendalami VQE untuk menyelesaikan masalah portofolio tersebut.
    

### 2. NISQ (Noisy Intermediate-Scale Quantum)

- **Konsep:** Ini adalah istilah untuk menyebut **era komputer kuantum saat ini** (sekarang).
    
    - **Noisy (Berisik):** Komputer kuantum yang kita punya sekarang belum stabil. Mereka rentan terhadap gangguan lingkungan (noise) yang bisa membuat perhitungan jadi error.
        
    - **Intermediate-Scale (Skala Menengah):** Jumlah qubit-nya (unit pemrosesannya) sudah lumayan banyak (puluhan hingga ratusan), tapi belum cukup banyak untuk melakukan koreksi error yang sempurna.
        
- **Kontribusi di Paper:** Konsep ini memberikan **konteks realitas**. Penulis menyadari bahwa kita belum punya komputer kuantum yang canggih dan sempurna. Oleh karena itu, mereka memilih algoritma (VQE) yang "tahan banting" dan bisa berjalan di mesin NISQ yang tidak sempurna ini. Paper ini berusaha mencari solusi praktis yang bisa jalan _hari ini_, bukan menunggu masa depan.
    

Ringkasan Paragraf 2:

Penulis sedang berkata: "Oke, untuk menyelesaikan masalah susah tadi, kita punya dua kandidat kuat: VQE dan QAOA. Kenapa mereka dipilih? Karena mereka cocok dijalankan di komputer kuantum jaman sekarang (NISQ) yang masih 'berisik' dan belum sempurna."

Sampai di sini, apakah penjelasan mengenai algoritma dan kondisi hardware (NISQ) ini bisa dipahami? Selanjutnya, di paragraf berikutnya, penulis akan mulai masuk ke tantangan teknis spesifik: kenapa cara biasa (standar) tidak cukup bagus untuk masalah ini.

---
---
## 1.3
Bagus, mari kita lanjutkan ke **Paragraf Ketiga dari Introduction**.

Paragraf ini sangat krusial karena menjelaskan **"Tantangan Teknis"** utama. Penulis menjelaskan mengapa kita tidak bisa begitu saja menempelkan metode kuantum standar ke masalah ini.

Kalimat pembukanya:

> _"However, solving the QUBO problem differs significantly from finding the ground state of a typical chemical Hamiltonian."_

Berikut adalah bedahan konsepnya:

### 1. Asal-Usul VQE (Kimia vs. Keuangan)

- **Konsep:** Algoritma VQE awalnya diciptakan untuk ilmu kimia (menghitung energi molekul). Dalam kimia, struktur elektron sangat rumit dan melibatkan fenomena kuantum yang "aneh" (superposisi yang kompleks).
    
- **Masalah:** Penulis menekankan bahwa masalah keuangan (QUBO) ini sifatnya berbeda dengan masalah kimia.
    

### 2. Hamiltonian Ising & Istilah yang "Komut" (_Commute_)

- **Konsep:**
    
    - **Ising Hamiltonian:** Ini adalah model fisika yang digunakan untuk merepresentasikan masalah keuangan tadi.
        
    - **Commute (Komut):** Dalam matematika kuantum, jika dua hal "komut", artinya mereka tidak saling mengganggu saat diukur.
        
    - Penulis menjelaskan bahwa dalam masalah ini, semua bagian dari persamaannya "saling komut". Ini menyederhanakan masalah secara drastis dibandingkan masalah kimia.
        
- **Implikasi:** Karena sifat ini, solusi terbaiknya (ground state) pasti berbentuk **"Computational Basis State"**.
    

### 3. _Computational Basis State_

- **Konsep:** Ini berarti jawaban akhirnya adalah deretan angka biner sederhana, seperti `010110` (yang berarti: Beli Saham A, Jangan Beli B, Beli C, dst).
    
- **Kontribusi di Paper:** Ini penting karena artinya kita tidak mencari keadaan kuantum yang aneh atau abstrak. Kita mencari satu kombinasi bit (0 dan 1) yang spesifik dan nyata.
    

### 4. Masalah pada "Nilai Ekspektasi" (_Expectation Value_)

- **Konsep:** Cara kerja standar VQE biasanya adalah mencari rata-rata energi (_expectation value_) dari seluruh sistem.
    
- **Tantangan:** Penulis bilang: _"Using the traditional expectation value of energy as the cost function is therefore not ideal."_
    
- **Analogi:** Bayangkan Anda mencari satu jarum di tumpukan jerami. Metode standar (rata-rata) akan memberi tahu Anda "rata-rata berat tumpukan jerami ini", padahal Anda hanya ingin tahu di mana letak jarumnya yang tajam (solusi terbaik). Menggunakan rata-rata justru bisa menyembunyikan solusi terbaik yang kita cari.
    

Ringkasan Paragraf 3:

Penulis berargumen: "VQE itu aslinya buat kimia. Tapi masalah keuangan ini beda strukturnya (lebih sederhana, jawabannya pasti berupa deretan 0 dan 1). Karena itu, cara hitung standar VQE (pakai rata-rata) jadi tidak efektif buat masalah ini. Kita butuh cara hitung baru."

Ini menjadi landasan untuk paragraf berikutnya, di mana mereka akan memperkenalkan solusi untuk masalah "cara hitung" ini. Apakah penjelasan mengenai tantangan teknis ini bisa dipahami?

---
---
## 1.4
Bagus, kita lanjut ke **Paragraf Keempat (terakhir) dari Bagian Introduction**.

Paragraf ini adalah inti dari **"Solusi & Kebaruan (Novelty)"** yang ditawarkan oleh paper ini. Setelah penulis menjelaskan bahwa "rata-rata biasa" itu jelek (di paragraf sebelumnya), di sini mereka memperkenalkan solusinya.

Berikut adalah konsep-konsep kuncinya:

### 1. CVaR (Conditional Value-at-Risk)

- **Konsep Asal:** Di dunia keuangan, CVaR biasanya dipakai untuk mengukur risiko kerugian ekstrem (misalnya: "Berapa rata-rata kerugian saya dalam 5% hari terburuk?").
    
- **Penerapan di Kuantum:** Peneliti sebelumnya (Barkoutsos et al.) punya ide cerdas: "Daripada menghitung rata-rata seluruh energi (yang mencampur solusi bagus dan jelek), ayo kita hitung rata-rata dari **ekor (tail)** distribusi energi terendah saja."
    
- **Analogi:** Jika Anda mencari siswa terpintar di kelas, jangan hitung rata-rata nilai satu kelas. Hitunglah rata-rata nilai dari "Top 10 siswa" saja. Itu akan memberi gambaran lebih baik tentang potensi maksimal kelas tersebut.
    
- **Kontribusi:** Ini adalah metode yang _sudah ada_ yang diadopsi penulis sebagai dasar pijakan1.
    

### 2. Weighted CVaR (WCVaR) - _Inovasi Paper Ini_

- **Konsep:** Penulis merasa CVaR biasa masih bisa ditingkatkan. Mereka memperkenalkan **Weighted CVaR (WCVaR)**.
    
- **Bedanya:** Kalau CVaR biasa menganggap semua solusi di "Top 10" itu sama pentingnya, WCVaR memberikan **bobot (weight)** yang berbeda. Solusi yang _paling_ bagus (Ranking 1) diberi bobot lebih besar daripada solusi Ranking 10.
    
- **Kontribusi:** Ini adalah **ide baru** dari paper ini. Mereka mengklaim cara ini membuat algoritma lebih cepat menemukan solusi terbaik2.
    

### 3. CMA-ES (Covariance Matrix Adaptation Evolution Strategy)

- **Konsep:** Ini adalah jenis **Optimizer** (alat pencari solusi).
    
- **Masalah:** Menggunakan CVaR atau WCVaR membuat "peta pencarian" menjadi kasar (_non-smooth_) atau bergelombang tajam. Optimizer standar (berbasis gradien/turunan) sering tersesat atau macet di peta seperti ini.
    
- **Solusi:** Penulis memilih **CMA-ES**. Ini adalah algoritma evolusi (mirip seleksi alam) yang tidak butuh turunan matematika (_derivative-free_). Ia menyebarkan "populasi" kandidat solusi, melihat mana yang bagus, lalu memusatkan pencarian di area tersebut.
    
- **Kontribusi:** Penulis mengusulkan kombinasi **WCVaR + CMA-ES** sebagai resep rahasia untuk performa tinggi3333.
    

### 4. Pembuktian (Eksperimen)

- **Konsep:** Penulis menyatakan bahwa mereka tidak cuma berteori, tapi sudah mengujinya lewat simulasi klasik di platform _Wuyue QuantumAI_.
    
- **Hasil:** Mereka mengklaim kombinasi baru mereka (WCVaR + CMA-ES) terbukti meningkatkan performa secara signifikan dibanding metode lain4.
    

Ringkasan Paragraf 4:

"Solusi untuk masalah 'rata-rata' tadi adalah pakai CVaR (fokus ke solusi terbaik saja). Tapi kami (penulis) bikin lebih canggih lagi jadi Weighted CVaR (kasih prioritas lebih ke yang terbaik). Karena metode ini bikin perhitungan jadi susah bagi optimizer biasa, kami pakai optimizer CMA-ES yang tangguh. Hasil tes kami menunjukkan ini resep yang jitu."

---

Kesimpulan Bagian Introduction (I):

Sekarang Anda sudah memahami alur pikir keseluruhan Bab 1:

1. **Masalah:** Optimisasi Portofolio itu penting tapi susah (NP-hard).
    
2. **Alat:** Kita pakai VQE (algoritma kuantum hibrida).
    
3. **Tantangan:** VQE standar (rata-rata) nggak cocok buat masalah ini.
    
4. **Solusi Paper Ini:** Pakai **WCVaR** (biar fokus ke solusi terbaik) + **CMA-ES** (biar pencariannya stabil).
    

Apakah Anda siap untuk masuk ke **Bagian II. BACKGROUND**? Di sana mereka akan mulai masuk ke matematika dan rumus-rumus detailnya (Portofolio & QUBO).

---
---
---
# BACKGROUND

## 2.1
Tentu, mari kita bedah bagian awal **Section II.A Portfolio Optimization**.

Di bagian ini, penulis sedang melakukan **"Data Pre-processing"**. Sebelum masuk ke komputer kuantum, data mentah dari pasar saham harus diubah menjadi parameter statistik yang bisa dihitung.

Berikut adalah penjelasan bertahap untuk setiap variabel dan persamaannya:

### 1. Data Mentah: Matriks Harga ($P$)

Penulis memulai dengan mendefinisikan input utamanya:

> _"The market data is represented as a matrix $P$ of size $M \times N$..."_ 1

- **$N$ (Aset/Saham):** Jumlah saham yang ingin kita analisis. Misalnya, jika portofolio kita terdiri dari BBCA, BBRI, dan TLKM, maka $N=3$.
    
- **$M$ (Waktu):** Jumlah periode waktu pengamatan. Misalnya, kita mengambil data harga penutupan harian selama satu tahun (sekitar 252 hari perdagangan), maka $M=252$.
    
- **$P_{ki}$ (Harga):** Ini adalah harga saham ke-$i$ pada waktu ke-$k$2.
    
    - Contoh: Harga BBCA ($i$) pada hari Senin tanggal 1 ($k$).
        

**Kontribusi:** Ini adalah bahan bakunya. Tanpa matriks ini, kita tidak punya data untuk diolah.

---

### 2. Menghitung _Return_ ($r_{ki}$) - Persamaan (1)

Dalam keuangan, harga absolut (misalnya Rp 5.000 vs Rp 50.000) tidak terlalu penting untuk analisis kinerja. Yang penting adalah **perubahan harganya**. Oleh karena itu, penulis mengubah harga menjadi _return_ (tingkat pengembalian).

$$r_{ki} = \frac{P_{ki} - P_{k-1, i}}{P_{k-1, i}}$$

3

- **Konsep:** Ini adalah rumus persentase keuntungan/kerugian sederhana.
    
    - $(Harga\_Sekarang - Harga\_Kemarin) / Harga\_Kemarin$.
        
- **Kontribusi:** Menstandarisasi data. Dengan mengubah harga menjadi _return_, kita bisa membandingkan kinerja saham murah dan saham mahal secara adil. Data $r_{ki}$ inilah yang akan menjadi dasar perhitungan selanjutnya.
    

---

### 3. Menghitung Ekspektasi _Return_ ($\mu_i$) - Persamaan (2)

Sekarang kita punya deretan data keuntungan harian. Kita butuh satu angka yang mewakili seberapa "menguntungkan" saham ini secara rata-rata.

$$\mu_i = \frac{1}{M} \sum_{k=1}^{M} r_{ki}$$

4

- **Konsep ($\mu_i$):** Ini adalah **Rata-rata (Mean)** dari _return_ harian tadi. Simbol $\mu$ (mu) sering dipakai di statistik untuk rata-rata populasi.
    
- **Kontribusi di Paper:** Variabel $\mu_i$ ini merepresentasikan faktor **KEUNTUNGAN (Reward)**.
    
    - Dalam optimisasi nanti, tujuan kita adalah mencari kombinasi saham yang membuat nilai total $\mu$ ini setinggi mungkin.
        

---

### 4. Menghitung Kovariansi ($\sigma_{ij}$) - Persamaan (3)

Ini adalah parameter yang paling penting untuk mengukur risiko.

$$\sigma_{ij} = \frac{1}{M-1} \sum_{k=1}^{M} (r_{ki} - \mu_i)(r_{kj} - \mu_j)$$

5

- **Konsep ($\sigma_{ij}$):** Ini adalah rumus **Kovariansi (Covariance)**.
    
    - Jika $i = j$ (asetnya sama), ini menjadi **Varians** (seberapa fluktuatif/naik-turun saham tersebut). Semakin tinggi nilainya, semakin berisiko.
        
    - Jika $i \neq j$ (aset beda, misal BBCA dan TLKM), ini mengukur **Korelasi** (hubungan pergerakan).
        
        - Nilai positif tinggi: Jika BBCA naik, TLKM ikut naik (Risiko tinggi karena kalau jatuh, jatuh bareng).
            
        - Nilai negatif: Jika BBCA naik, TLKM turun (Bagus untuk diversifikasi/pengaman).
            
- **Kontribusi di Paper:** Matriks $\sigma_{ij}$ ini merepresentasikan faktor **RISIKO (Risk)**.
    
    - Dalam optimisasi nanti, tujuan kita adalah meminimalkan nilai total risiko ini.
        

---

**Ringkasan Langkah Ini:**

1. Ambil harga saham ($P$).
    
2. Ubah jadi persentase untung/rugi harian ($r$).
    
3. Hitung rata-ratanya ($\mu$) $\rightarrow$ Ini target **Keuntungan**.
    
4. Hitung hubungan pergerakan antar saham ($\sigma$) $\rightarrow$ Ini target **Risiko**.
    

Sekarang penulis sudah punya dua "senjata" matematika: vektor $\mu$ (keuntungan) dan matriks $\sigma$ (risiko).

Apakah penjelasan mengenai transformasi data harga menjadi parameter $\mu$ dan $\sigma$ ini sudah jelas? Jika ya, kita bisa lanjut melihat bagaimana mereka menyusun "Budget" di paragraf selanjutnya.

---
---
## 2.2
Baik, mari kita lanjutkan bedah bagian **Model Matematika Portofolio**.

Setelah kita punya data statistik ($\mu$ dan $\sigma$) dari langkah sebelumnya, sekarang penulis mendefinisikan "Aturan Main" dan "Tujuan Permainan".

Bagian ini (dari "Suppose we have..." hingga Persamaan 6) menjelaskan tiga komponen penting: **Modal**, **Target Keuntungan**, dan **Target Risiko**.

### 1. Kendala Modal (Constraint) - Persamaan (4)

Penulis memulai dengan batasan paling dasar: Uang kita terbatas.

> _"Suppose we have a total budget $B$ that we wish to allocate among $N$ assets... Let $b_i$ be the portion of the budget allocated to asset $A_i$."_ 1

Rumusnya:

$$\sum_{i} b_i \le B$$

2

- **$B$ (Budget):** Total uang yang Anda miliki.
    
- **$b_i$ (Alokasi):** Berapa banyak uang yang Anda taruh di saham ke-$i$.
    
- **Maknanya:** Jumlah total uang yang Anda belanjakan untuk semua saham ($\sum b_i$) tidak boleh melebihi uang yang Anda punya di dompet ($B$). Sederhana, bukan?
    

---

### 2. Tujuan Pertama: Maksimalkan Keuntungan - Persamaan (5)

Ini adalah tujuan "Keserakahan" (Greed). Kita ingin portofolio yang menghasilkan uang paling banyak.

> _"The first objective function to maximize is the expected return..."_ 3

Rumusnya:

$$C_1(b) = \sum_{i=1}^{N} \mu_i b_i$$

4

- **Penjelasan:** Ini adalah penjumlahan sederhana (linear).
    
    - (Rata-rata untung saham 1 $\times$ Jumlah uang di saham 1) + (Rata-rata untung saham 2 $\times$ Jumlah uang di saham 2) + ... dst.
        
- **Sifat Matematis:** Perhatikan bahwa pangkat variabel $b_i$ di sini adalah **1** (linear). Ini penting karena bagian ini mudah dihitung.
    

---

### 3. Tujuan Kedua: Minimalkan Risiko - Persamaan (6)

Ini adalah tujuan "Ketakutan" (Fear). Kita ingin portofolio yang paling aman (tidak fluktuatif).

> _"The risk of the portfolio is typically measured by its volatility... the second objective function to minimize is the portfolio variance:"_ 5

Rumusnya:

$$C_2(b) = \sum_{ij} \sigma_{ij} b_i b_j$$

6

- **Penjelasan:** Ini adalah bagian yang membuat perhitungan jadi berat.
    
    - Perhatikan ada perkalian **$b_i$ dikali $b_j$**. Ini berarti variabelnya berpangkat **2** (Kuadratik).
        
    - Inilah asal kata **"Quadratic"** dalam **QUBO**.
        
- **Mengapa Kuadratik?** Risiko portofolio bukan sekadar penjumlahan risiko masing-masing saham. Risiko muncul dari **interaksi** antar saham (kovariansi $\sigma_{ij}$).
    
    - Jika Anda punya banyak uang di Saham A ($b_i$ besar) DAN banyak uang di Saham B ($b_j$ besar), DAN kedua saham ini punya korelasi tinggi ($\sigma_{ij}$ besar), maka risiko portofolio Anda meledak secara kuadratik.
        

---

Ringkasan Langkah Ini:

Kita sekarang punya situasi dilematis (Trade-off):

1. Kita ingin **Menaikkan** nilai $C_1$ (Linear).
    
2. Kita ingin **Menurunkan** nilai $C_2$ (Kuadratik).
    
3. Semua itu harus dilakukan tanpa melanggar batas budget ($B$).
    

Di paragraf selanjutnya (Persamaan 7), penulis akan menjelaskan cara menggabungkan dua keinginan yang bertolak belakang ini menjadi satu rumus tunggal.

Apakah penjelasan mengenai konflik antara $C_1$ (Return) dan $C_2$ (Risk) ini sudah cukup jelas?

---
---
## 2.3
Tentu, mari kita lanjutkan ke paragraf yang membahas **Strategi Penggabungan Tujuan** (mulai dari "The portfolio optimization..." hingga persamaan 7).

Di bagian sebelumnya, kita punya dua "tuan" yang harus dilayani: Keuntungan ($C_1$) yang ingin dimaksimalkan, dan Risiko ($C_2$) yang ingin diminimalkan. Paragraf ini menjelaskan bagaimana cara melayani keduanya sekaligus.

### 1. Masalah Multi-Objektif & Pareto Front

Penulis menyatakan bahwa ini adalah _multi-objective optimization problem_.

- **Konsep:** Tidak ada satu solusi "sempurna" yang paling untung sekaligus paling aman. Biasanya, saham untung besar itu risikonya besar. Saham aman itu untungnya kecil.
    
- **Pareto Front (Efficient Frontier):** Karena tidak ada satu juara tunggal, kita mencari sekumpulan solusi terbaik yang disebut _Pareto Front_.
    
    - Contoh: Jika Anda ingin untung 10%, ini adalah portofolio teramannya. Jika Anda berani ambil risiko level 5, ini adalah portofolio paling untungnya. Solusi di garis depan ini adalah solusi yang "efisien".
        

### 2. Metode Skalarisasi (Penyatuan)

Komputer (termasuk komputer kuantum) biasanya hanya bisa mengejar satu angka target (_single objective_). Jadi, kita harus menggabungkan dua tujuan tadi menjadi satu rumus tunggal.

> _"In this method, the two objectives are combined into a single objective function by introducing a weighting factor $\lambda$."_

### 3. Fungsi Objektif Gabungan ($C'$) - Persamaan (7)

Inilah rumus penggabungannya:

$$C'(b) = -\lambda C_1(b) + (1-\lambda)C_2(b)$$

Mari kita bedah komponennya secara perlahan:

- **$\lambda$ (Lambda):** Ini adalah "tombol pengatur selera risiko" Anda. Nilainya antara 0 sampai 1.
    
    - Jika $\lambda = 1$: Anda hanya peduli keuntungan ($C_1$). Anda seorang pengambil risiko ekstrem.
        
    - Jika $\lambda = 0$: Anda hanya peduli keamanan ($C_2$). Anda sangat menghindari risiko.
        
    - Biasanya orang memilih nilai di tengah-tengah (misal 0.5) untuk seimbang.
        
- **Tanda Negatif pada $-\lambda C_1$:** Ini sangat penting!
    
    - Kita ingin **Memaksimalkan** Keuntungan ($C_1$).
        
    - Tapi algoritma optimisasi biasanya bekerja dengan cara **Meminimalkan** "Cost" (Biaya/Energi).
        
    - Secara matematika: **Memaksimalkan $X$** itu sama dengan **Meminimalkan $-X$** (Negatif X).
        
    - Jadi, penulis memberi tanda minus pada bagian keuntungan supaya komputer bisa meminimalkan seluruh persamaan ini.
        
- **Tanda Positif pada $(1-\lambda)C_2$:**
    
    - Kita ingin **Meminimalkan** Risiko ($C_2$).
        
    - Karena tujuannya sudah "minimalkan", tandanya tetap positif.
        

Ringkasan Langkah Ini:

Sekarang kita punya satu misi tunggal: Minimalkan nilai $C'$.

Dengan meminimalkan $C'$, secara otomatis kita akan mencari Keuntungan setinggi mungkin (karena tanda negatif tadi) dan Risiko serendah mungkin, sesuai dengan proporsi selera risiko ($\lambda$) yang kita atur1.

Kalimat penutup paragraf ini mengingatkan kita: "Oke, minimalkan rumus $C'$ tadi, **tapi jangan lupa** syarat modalnya (constraint) di Persamaan 4 tadi harus tetap dipenuhi."

Apakah penjelasan mengenai penggabungan rumus dan trik tanda negatif ini bisa dipahami? Jika ya, kita bisa lanjut ke bagian di mana mereka mengubah masalah ini menjadi format biner (QUBO) yang sesungguhnya.

---
---
## 2.4
Tentu, mari kita masuk ke sub-bagian **B. Quadratic Unconstrained Binary Optimization (QUBO)**.

Ini adalah tahap **"Penerjemahan"**. Penulis mengubah masalah keuangan yang kita bahas sebelumnya menjadi format matematika standar yang dimengerti oleh algoritma optimisasi (dan nantinya komputer kuantum).

Mari kita bedah langkah demi langkah dari konsep umum hingga menjadi Persamaan 12.

### 1. Apa itu QUBO? (Persamaan 8)

Penulis memperkenalkan bentuk umum dari masalah QUBO:

$$Q(x) = \sum_{i<j} q_{ij} x_i x_j + \sum_{i} q_i x_i + c$$

1

- **$x_i$ (Variabel Biner):** Ini adalah tombol "On/Off". Nilainya hanya boleh **0** atau **1**2.
    
- **$q_{ij} x_i x_j$ (Interaksi Kuadratik):** Bagian ini menghitung hubungan antara dua variabel. Dalam konteks saham, ini akan menampung data **Risiko/Kovariansi** ($\sigma_{ij}$).
    
- **$q_i x_i$ (Bias Linear):** Bagian ini menghitung efek variabel sendirian. Ini akan menampung data **Keuntungan** ($\mu_i$).
    
- **Unconstrained:** Rumus ini tidak punya syarat "harus sama dengan X". Ia bebas. Tugas kita nanti adalah memanipulasi rumus ini agar syarat "Budget" masuk ke dalamnya secara otomatis.
    

---

### 2. Penyederhanaan Masalah: Dari "Berapa Banyak" ke "Pilih Mana"

Di sini penulis melakukan penyederhanaan yang sangat penting (dan cerdik) agar masalahnya muat di komputer kuantum saat ini.

- **Masalah Asli:** Variabel $b_i$ (alokasi dana) adalah bilangan riil (misal: beli 10.5% saham A, 20.3% saham B). Mengubah bilangan desimal ini menjadi biner butuh **banyak sekali qubit**3.
    
- **Solusi Penulis:** Mereka menyederhanakan masalahnya menjadi: **"Kita hanya memilih APAKAH akan membeli saham ini atau tidak."**4.
    
    - $x_i = 1$: Saham $A_i$ dipilih masuk portofolio.
        
    - $x_i = 0$: Saham $A_i$ tidak dipilih.
        
- **Asumsi Budget:** Mereka menetapkan aturan main: Kita harus memilih tepat **$N/2$** saham dari total $N$ saham yang tersedia5.
    
    - Contoh: Jika ada 12 saham, kita harus memilih 6 terbaik.
        

---

### 3. Masalah Constraint (Persamaan 10)

Sekarang kita punya aturan baru:

$$\sum_{i=1}^{N} x_i = N/2$$

6

Artinya: Jumlah angka "1" di dalam solusi kita harus persis separuh dari total aset.

Tapi ingat, QUBO itu "Unconstrained" (Tanpa Batasan). Algoritma VQE tidak mengerti perintah "Hei, tolong pilih tepat 6 saham." VQE hanya mengerti "Cari energi terendah".

Bagaimana cara memaksa VQE menuruti aturan ini tanpa memberinya perintah langsung? Jawabannya adalah **Metode Penalti**.

---

### 4. Metode Penalti (Penalty Method)

Penulis menambahkan suku baru ke dalam persamaan matematika untuk "menghukum" solusi yang melanggar aturan.

$$Penalty = p \left( \sum_{i=1}^{N} x_i - \frac{N}{2} \right)^2$$

7

Mari kita bayangkan cara kerjanya:

- **$p$ (Koefisien Penalti):** Angka yang sangat besar (misal: 1.000.000).
    
- **Jika kita patuh (Pilih $N/2$):** Hasil dalam kurung jadi 0. $0^2 = 0$. Penalti = 0. Tidak ada masalah.
    
- **Jika kita melanggar (Misal pilih $N/2 + 1$):** Hasil dalam kurung jadi 1. $1^2 = 1$. Penalti = $1 \times p$ (1 Juta!).
    
- **Efeknya:** Karena algoritma VQE ingin mencari nilai **terendah**, dia akan sekuat tenaga menghindari penalti besar ini. Secara otomatis, dia akan terdorong ke solusi yang jumlah sahamnya pas ($N/2$).
    

---

### 5. Rumus Akhir QUBO (Persamaan 12)

Inilah "Raja Terakhir" dari pemodelan matematika di paper ini. Penulis menggabungkan **Keuntungan**, **Risiko**, dan **Penalti** menjadi satu persamaan raksasa:

$$C(x) = \underbrace{-\lambda \sum_{i=1}^{N} \mu_i x_i}_{\text{1. Keuntungan}} + \underbrace{(1-\lambda) \sum_{i=1}^{N} \sum_{j=i+1}^{N} \sigma_{ij} x_i x_j}_{\text{2. Risiko}} + \underbrace{p \left( \sum_{i=1}^{N} x_i - \frac{N}{2} \right)^2}_{\text{3. Penalti}}$$


Mari kita rangkum peran setiap bagian:

1. **Keuntungan (Linear):** Kita pakai tanda minus ($-\lambda$) supaya algoritma yang mencari nilai _minimum_ justru akan mencari keuntungan _maksimum_.
    
2. **Risiko (Kuadratik):** Bagian ini ($\sigma_{ij} x_i x_j$) menghitung interaksi risiko antar saham. Kita ingin ini sekecil mungkin.
    
3. **Penalti (Kuadratik):** "Tembok listrik" yang menjaga agar jumlah saham yang dipilih tetap sesuai aturan ($N/2$).
    

Kontribusi Persamaan 12:

Persamaan inilah yang nanti akan dikonversi menjadi Hamiltonian (sistem energi fisika) di sub-bagian C, supaya bisa diproses oleh sirkuit kuantum.

Apakah penjelasan mengenai transformasi dari aturan keuangan menjadi persamaan penalti ini sudah cukup jelas? Jika ya, kita siap masuk ke dunia Kuantum di sub-bagian C.

---
---
## 2.5
Tentu, pertanyaan yang sangat bagus. Sebagai mahasiswa fisika, sebenarnya kamu sudah sangat akrab dengan bentuk matematika ini, hanya saja konteksnya berbeda.

Mari kita bahas menggunakan analogi **Fisika Klasik** dan simulasi grafik **Desmos**.

### 1. Analogi Fisika Murni: Potensial Osilator Harmonik

Coba perhatikan kembali suku penalti di Persamaan (12) paper tersebut1:

$$p \left( \sum x_i - \frac{N}{2} \right)^2$$

Bentuk matematika ini $(x - x_0)^2$ identik dengan rumus Energi Potensial Pegas (Osilator Harmonik Sederhana):

$$U(x) = \frac{1}{2} k (x - x_0)^2$$

Di mana:

- $x$: Posisi partikel saat ini (dalam paper: jumlah saham yang dipilih).
    
- $x_0$: Posisi setimbang/target (dalam paper: target jumlah saham $N/2$).
    
- $k$: Konstanta pegas atau kekakuan (dalam paper: koefisien penalti $p$).
    

Logika Fisikanya:

Bayangkan kamu punya sebuah partikel (sistem portofolio) yang bergerak di atas lintasan energi.

1. **Tanpa Penalti:** Partikel bebas menggelinding ke mana saja untuk mencari energi terendah (profit maksimal). Dia mungkin menggelinding jauh sekali ke posisi "pilih semua saham" atau "tidak pilih saham sama sekali".
    
2. **Dengan Penalti:** Kamu memasang sebuah **pegas yang sangat kaku** (nilai $p$ sangat besar) yang ditambatkan tepat di posisi $x_0 = N/2$.
    
3. **Akibatnya:** Jika partikel mencoba bergerak menjauh dari posisi $N/2$, pegas akan menariknya kembali dengan energi potensial yang melonjak drastis secara kuadratik.
    
4. **Ground State:** Karena VQE mencari _Ground State_ (energi terendah), sistem akan "terpaksa" diam di posisi di mana pegasnya tidak tegang, yaitu tepat di $x = N/2$.
    

Jadi, metode penalti ini sebenarnya adalah **rekayasa _Potential Landscape_** (medan potensial) agar sumur energi terendahnya berada tepat di koordinat yang mematuhi aturan.

---

### 2. Simulasi Grafik Desmos

Untuk memahaminya secara visual, kamu bisa membuka kalkulator grafik **Desmos** (atau bayangkan grafiknya).

Mari kita buat model sederhana:

- Tujuan kita: Mencari nilai $x$ sekecil mungkin (kita ingin ke kiri).
    
- Fungsi Objektif: $y = x$ (Garis lurus naik). Tanpa batasan, nilai minimumnya adalah $-\infty$.
    
- Batasan (Constraint): Kita ingin jawabannya harus $x = 2$.
    
- Penalti: $P(x) = 100(x - 2)^2$.
    

Instruksi Eksperimen:

Jika kamu memasukkan persamaan ini ke Desmos:

$$f(x) = x + p(x - 2)^2$$

Dan kamu mainkan nilai $p$ (slider):

1. Saat $p = 0$ (Tanpa Penalti):
    
    Grafiknya adalah garis lurus ($y=x$). Minimumnya tidak ada (menuju negatif tak hingga). Algoritma akan lari ke kiri terus dan melanggar aturan $x=2$.
    
2. Saat $p = 0.5$ (Pegas Lemah):
    
    Grafiknya mulai melengkung jadi parabola, tapi titik terendahnya (minimum) mungkin masih di $x = 1$. Masih meleset dari target.
    
3. Saat $p = 100$ (Pegas Sangat Kaku / Penalti Besar):
    
    Grafiknya menjadi parabola yang sangat curam/tajam.
    
    Meskipun fungsi aslinya ($y=x$) ingin menarik partikel ke kiri, curamnya dinding parabola memaksa titik minimum globalnya berada **sangat dekat dengan $x=2$**.
    

Kesimpulan Visual:

Metode penalti mengubah grafik "perosotan lurus" menjadi "lembah curam". Di dasar lembah itulah solusi yang valid berada.

Apakah analogi pegas dan visualisasi lembah ini membantu pemahamanmu tentang kenapa rumus kuadratik $(...)^2$ itu digunakan?


---
---
## 2.6
Tentu, bagus sekali kamu sudah memvisualisasikan konsep penalti tersebut. Sekarang kita masuk ke **Bagian C. Variational Quantum Eigensolver (VQE)**.

Sesuai permintaanmu, kita akan membagi ini menjadi dua. Bagian pertama ini (dari awal sub-bab hingga Persamaan 15) membahas **"Mekanisme Penerjemahan ke Kuantum"** dan **"Prinsip Dasar VQE"**.

Karena kamu mahasiswa fisika, bagian ini akan terasa sangat familiar karena penuh dengan terminologi Mekanika Kuantum standar.

### 1. Transformasi Variabel: Dari Bit ke Spin (Persamaan 13)

Masalah QUBO sebelumnya masih menggunakan variabel biner $x_i \in \{0, 1\}$.

Sistem kuantum (seperti elektron atau qubit) bekerja dengan prinsip Spin.

Penulis melakukan pemetaan variabel (mapping) sederhana:

$$s_i = 1 - 2x_i$$

- **Jika $x_i = 0$ (Saham tidak dibeli):** $s_i = 1 - 0 = +1$ (Spin Up $\uparrow$)
    
- **Jika $x_i = 1$ (Saham dibeli):** $s_i = 1 - 2 = -1$ (Spin Down $\downarrow$)
    

**Hasilnya:** Persamaan QUBO matematika tadi berubah menjadi persamaan **Energi Ising Klasik** ($E(s)$)1.

### 2. Membangun Hamiltonian ($\hat{H}$) - (Persamaan 14)

Ini langkah krusial. Agar komputer kuantum bisa memprosesnya, variabel klasik $s_i$ diganti dengan **Operator Pauli-Z** ($\hat{Z}_i$).

$$\hat{H} = -\sum h_i \hat{Z}_i - \sum J_{ij} \hat{Z}_i \hat{Z}_j$$

- **Konsep Fisika:** Ini adalah **Ising Hamiltonian**. Suku pertama ($\hat{Z}_i$) adalah interaksi dengan medan luar, dan suku kedua ($\hat{Z}_i \hat{Z}_j$) adalah interaksi antar spin (coupling)2.
    
- **Maknanya:**
    
    - Sekarang, masalah "Mencari Portofolio Terbaik" telah resmi berubah menjadi masalah fisika murni: **"Mencari Ground State (Keadaan Dasar) dari Hamiltonian ini."**
        
    - Jika kita menemukan konfigurasi spin dengan energi terendah, itu otomatis adalah portofolio dengan profit maksimal dan risiko minimal3.
        

### 3. VQE: Algoritma Hibrida (Hybrid)

Penulis menjelaskan bahwa mencari _Ground State_ secara umum itu sangat sulit (_QMA-complete_, analogi kuantum untuk NP-complete)4. Karena itu, kita menggunakan metode pendekatan (heuristik) bernama **VQE**.

VQE bekerja layaknya kerjasama tim antara Komputer Kuantum (QPU) dan Komputer Klasik (CPU)5:

1. **QPU (Quantum):** Menyiapkan fungsi gelombang coba-coba (_Ansatz_) $|\psi(\theta)\rangle$ dan mengukur energinya.
    
2. **CPU (Klasik):** Menerima hasil ukur, lalu mengupdate parameter $\theta$ (putar sedikit knob-nya) supaya energinya makin turun.
    
3. Proses ini berulang (looping) sampai energi minimum ditemukan.
    

### 4. Fungsi Objektif VQE (Persamaan 15)

Inilah rumus yang dihitung berulang-ulang oleh komputer kuantum. Penulis menyebutnya sebagai fungsi biaya atau _Rayleigh Quotient_:

$$E(\theta) = \frac{\langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle}{\langle \psi(\theta) | \psi(\theta) \rangle}$$

- **Penjelasan Fisika:** Ini adalah definisi standar dari **Nilai Ekspektasi Energi** (Expectation Value) dalam mekanika kuantum6.
    
- **Penyederhanaan:** Karena komputer kuantum biasanya menghasilkan state yang sudah ternormalisasi ($\langle \psi | \psi \rangle = 1$), penyebutnya bisa diabaikan. Jadi fokusnya hanya meminimalkan pembilangnya: $\langle \hat{H} \rangle$.
    

---

**Ringkasan Bagian C (Part 1):**

1. Ubah masalah Saham (0/1) jadi masalah Spin (+1/-1).
    
2. Ubah rumus Keuangan jadi Operator Hamiltonian ($\hat{H}$).
    
3. Gunakan algoritma VQE untuk mencari energi terendah ($\langle H \rangle$) dari Hamiltonian tersebut.
    

Apakah transisi dari persamaan matematika ke operator Hamiltonian ini bisa dipahami? Jika ya, kita bisa lanjut ke paruh kedua sub-bab C, di mana penulis mulai mengkritik kenapa Persamaan 15 (Nilai Ekspektasi) itu sebenarnya **kurang bagus** untuk kasus ini.

---
---

## 2.7
Pertanyaan yang sangat kritis dan sangat khas mahasiswa fisika! Mari kita bedah satu per satu.

### 1. Mengapa Persamaan 13 Semua Sukunya Negatif?

Persamaan 13 ditulis sebagai:

$$E(s) = -\sum h_i s_i - \sum J_{ij} s_i s_j$$

Alasannya adalah **Konvensi Fisika untuk Minimisasi Energi**.

1. **Tujuan VQE:** Kita ingin mencari **Ground State** (keadaan dengan energi _minimum_ / paling negatif).
    
2. **Analogi Ferromagnetisme:**
    
    - Dalam model Ising fisika standar, interaksi ferromagnetik (di mana spin ingin searah) ditandai dengan konstanta kopling $J > 0$.
        
    - Jika dua spin searah ($s_i = +1, s_j = +1$ atau $s_i = -1, s_j = -1$), hasil kalinya $s_i s_j = +1$.
        
    - Agar keadaan "searah" ini memiliki energi **rendah**, kita perlu memberi tanda negatif di depannya.
        
    - $E_{interaksi} = - J (+1) = -J$ (Energi rendah/stabil).
        
3. **Konteks Paper:**
    
    - Penulis ingin mempertahankan bentuk standar Hamiltonian Ising fisik ini1.
        
    - Nilai $h_i$ dan $J_{ij}$ dihitung sedemikian rupa dari data keuangan sehingga konfigurasi portofolio yang **optimal** (profit tinggi, risiko rendah, sesuai budget) akan menghasilkan nilai energi total yang **paling negatif**.
        

Jadi, tanda negatif itu hanyalah "wadah" agar saat kita memaksimumkan profit (di dunia keuangan), itu setara dengan meminimumkan energi (di dunia fisika).

---

### 2. Apa Maksud Fisik dari $h_i$ dan $J_{ij}$?

Setelah transformasi dari variabel biner $x$ (0/1) ke spin $s$ (+1/-1), parameter keuangan ($\mu, \sigma$) dan penalti ($p$) akan teraduk dan masuk ke dalam dua koefisien baru ini2:

**A. $h_i$ (Medan Magnet Eksternal Lokal)**

- **Di Fisika:** Ini adalah bias eksternal yang memaksa spin ke-$i$ untuk menunjuk ke atas atau ke bawah.
    
- **Di Paper Ini:** Koefisien $h_i$ berisi akumulasi dari semua **suku linear** dalam persamaan QUBO awal.
    
    - Ini mengandung informasi **Expected Return ($\mu_i$)** dari saham tersebut.
        
    - Ini juga mengandung sebagian dari suku penalti (bagian linear dari kuadrat penalti).
        
    - _Intinya:_ $h_i$ menentukan seberapa besar keinginan individu saham tersebut untuk dibeli (atau tidak), terlepas dari hubungannya dengan saham lain.
        

**B. $J_{ij}$ (Interaksi Pertukaran / Coupling)**

- **Di Fisika:** Ini adalah kekuatan interaksi antara spin $i$ dan spin $j$.
    
- **Di Paper Ini:** Koefisien $J_{ij}$ berisi akumulasi dari semua **suku kuadratik (interaksi)**.
    
    - Ini mengandung informasi **Risiko/Kovariansi ($\sigma_{ij}$)**. Jika saham $i$ dan $j$ punya korelasi tinggi yang berbahaya, itu tercermin di sini.
        
    - Ini juga mengandung interaksi dari suku penalti (karena $( \sum x_i )^2$ akan menghasilkan suku $x_i x_j$).
        
    - _Intinya:_ $J_{ij}$ menentukan apakah saham $i$ dan $j$ sebaiknya "hidup bersama" dalam satu portofolio atau saling tolak.
        

---

### 3. Apakah Ada Rumus Khusus Konversi $s_i$ Menjadi $\hat{Z}$?

Tidak ada "rumus hitungan" dalam artian kalkulus atau aljabar biasa, melainkan ini adalah **Postulat Kuantisasi** (promosi variabel ke operator).

Dalam mekanika kuantum, variabel klasik digantikan oleh **Operator Hermitian** yang memiliki nilai eigen (eigenvalues) yang sama dengan nilai variabel klasiknya.

**Logika Konversinya:**

1. Variabel Klasik ($s_i$):
    
    Nilainya hanya boleh $+1$ atau $-1$.
    
2. Operator Pauli-Z ($\hat{Z}$):
    
    Dalam basis komputasi standar ($|0\rangle, |1\rangle$), operator Pauli-Z adalah matriks:
    
    $$\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
    
    Perhatikan persamaan nilai eigennya:
    
    - $\hat{Z} |0\rangle = \mathbf{+1} |0\rangle$
        
    - $\hat{Z} |1\rangle = \mathbf{-1} |1\rangle$
        
3. Pemetaan (Mapping):
    
    Karena nilai eigen dari operator $\hat{Z}$ persis sama dengan kemungkinan nilai variabel klasik $s_i$ ($+1$ dan $-1$), kita bisa langsung mensubstitusi variabel $s_i$ dalam persamaan energi dengan operator $\hat{Z}_i$ dalam persamaan Hamiltonian3.
    
    $$s_i \longrightarrow \hat{Z}_i$$
    
    Secara teknis, untuk sistem banyak partikel (N qubit), $\hat{Z}_i$ berarti operator Z bekerja pada qubit ke-$i$ dan identitas ($I$) pada qubit lainnya:
    
    $$\hat{Z}_i = I_1 \otimes I_2 \otimes \dots \otimes \sigma_z^{(i)} \otimes \dots \otimes I_N$$
    

Kesimpulan:

Persamaan 14 ($\hat{H} = -\sum h \hat{Z} \dots$) adalah bentuk operator kuantum dari Persamaan 13. Saat kita mengukur nilai ekspektasi operator ini, hasilnya secara matematis identik dengan menghitung energi pada model Ising klasik.

Apakah penjelasan mengenai peran $h_i, J_{ij}$ dan jembatan antara variabel klasik ke operator kuantum ini sudah jelas? Jika ya, kita bisa lanjut ke bagian di mana paper ini membahas _ansatz_ dan _cost function_ barunya.

---
---
## 2.8
Bagus. Mari kita selesaikan **Bagian II.C (Paruh Kedua)**, mulai dari pembahasan "Kenapa cara hitung energi biasa itu bermasalah" hingga Persamaan 20.

Di sini penulis membongkar kelemahan algoritma VQE standar jika diterapkan langsung untuk masalah portofolio ini.

### 1. Masalah "Rata-Rata" (Expectation Value)

Kamu ingat Persamaan 15 tadi? Itu menghitung **Nilai Ekspektasi** ($\langle \hat{H} \rangle$) atau rata-rata energi.

Penulis berargumen:

> _"The Ising Hamiltonian represents a special case, as its eigenstates are the computational basis states."_ 1

**Penjelasan Fisika:**

- Dalam simulasi kimia (molekul), _Ground State_ yang dicari biasanya berupa superposisi kuantum yang kompleks dan terbelit (_entangled_). Di sana, menghitung rata-rata seluruh fungsi gelombang itu masuk akal.
    
- Tapi untuk masalah Portofolio ini, _Ground State_-nya pasti berupa satu kombinasi bit yang pasti (misalnya `101100`). Itu adalah **Basis Komputasi**2.
    
- **Masalahnya:** Jika VQE menghasilkan superposisi (campuran berbagai jawaban), menghitung "rata-rata energi" bisa menyesatkan.
    
    - Contoh: Misal VQE menebak dua kemungkinan:
        
        1. Jawaban A (Energi -100, Sangat Bagus). Peluang 50%.
            
        2. Jawaban B (Energi +100, Sangat Buruk). Peluang 50%.
            
    - **Rata-ratanya:** $0$.
        
    - Optimizer akan mengira ini solusi "biasa saja". Padahal di dalamnya ada jawaban emas (-100)! Optimizer mungkin akan membuang solusi ini dan mencari yang lain, padahal kita sudah dekat sekali dengan jawaban benar3.
        

---

### 2. Solusi: CVaR (Conditional Value at Risk)

Karena kita mencari satu jawaban terbaik (bukan rata-rata populasi), penulis mengusulkan penggunaan **CVaR** sebagai fungsi biaya (Cost Function) pengganti4.

**Algoritmanya (Sampling):**

1. Jalankan sirkuit kuantum dan lakukan pengukuran (measurement) sebanyak $K$ kali.
    
2. Kamu akan dapat sekumpulan string bit (hasil sampling).
    
3. Hitung energi klasik untuk setiap bit string tersebut.
    
4. Urutkan energi dari yang terkecil (paling negatif) ke terbesar:
    
    $E_{(1)}, E_{(2)}, \dots, E_{(K)}$5.
    

Rumus CVaR (Persamaan 19):

$$CVaR_{\alpha}(E) = \frac{1}{\lceil \alpha K \rceil} \sum_{k=1}^{\lceil \alpha K \rceil} E_{(k)}$$

(Catatan: Rumus di teks asli 6 mungkin terpotong, tapi ini bentuk lengkapnya: Rata-rata dari sejumlah $\alpha K$ sampel terendah).

- **Parameter $\alpha$ (Alpha):** Ini adalah persentase sampel yang kita ambil ("Top X%"). Nilainya antara 0 dan 1.
    
- **Cara Kerjanya:** Alih-alih merata-rata seluruh $K$ sampel, kita potong ekornya. Kita hanya ambil $\alpha$-persen sampel dengan energi terendah, lalu rata-ratakan _hanya_ kelompok elit itu.
    

---

### 3. Peran Parameter $\alpha$ (Alpha)

Penulis menjelaskan perilaku rumus ini pada dua kondisi ekstrem 7:

- Jika $\alpha = 1$ (100%):
    
    Kita merata-ratakan semua sampel.
    
    $$CVaR_{1} \approx \text{Expectation Value Biasa}$$
    
    Ini kembali ke metode lama yang "bermasalah" tadi8.
    
- Jika $\alpha \to 0$ (Sangat Kecil):
    
    Kita hanya mengambil 1 sampel terbaik (minimum absolut).
    
    $$CVaR_{min} = \min(E)$$
    
    Ini terlihat ideal karena langsung menunjuk ke solusi terbaik. Tapi, ini membuat grafik fungsi biaya menjadi kasar, tajam, dan sulit dituruni oleh optimizer (seperti berjalan di lantai penuh paku tajam, sulit mencari arah landai)9.
    

Kesimpulan Penulis:

Biasanya, kita memilih $\alpha$ di tengah-tengah (moderat) untuk menyeimbangkan antara "Mencari solusi terbaik" (eksplorasi) dan "Kestabilan perhitungan" (stabilitas)10.

---

Ringkasan Akhir Bagian II:

Kita sudah punya:

1. Masalah Portofolio $\rightarrow$ Ising Hamiltonian.
    
2. Alat Ukur $\rightarrow$ Jangan pakai rata-rata biasa, pakailah **CVaR** (Rata-rata dari ekor distribusi terbaik).
    

Sekarang, penulis siap masuk ke **Bagian III**, di mana mereka akan memodifikasi CVaR ini menjadi **Weighted CVaR (WCVaR)**, inovasi utama mereka.

Apakah konsep CVaR sebagai "filter sampel terbaik" ini bisa dipahami? Jika ya, kita bisa lanjut ke Bagian III.

---
---
---
# DESIGN OF OUR VQE ALGORITHM
## 3.1
Tentu, mari kita masuk ke jantung inovasi paper ini: **Bagian III.A Weighted CVaR (WCVaR)**.

Setelah di bagian sebelumnya kita sepakat bahwa "rata-rata biasa" itu buruk dan "rata-rata ekor" (CVaR) itu lebih baik, di sini penulis menyempurnakan konsep tersebut.

Mari kita bedah pelan-pelan.

### 1. Kritik terhadap CVaR Standar (Uniform Weights)

Penulis memulai dengan mengakui kehebatan CVaR, tapi kemudian menunjukkan satu kelemahan logisnya:

> _"Standard CVaR assumes that all outcomes within the worst $\alpha$-fraction ... contribute equally to the average, assigning them uniform weights."_ 1

Analogi Kelas Unggulan:

Bayangkan kita punya 100 siswa. Kita ambil "Top 10" siswa terbaik (Rank 1 sampai 10) untuk menghitung nilai rata-rata kelas unggulan.

- **Cara CVaR:** Nilai Juara 1 dan Nilai Juara 10 dianggap **sama pentingnya** dalam perhitungan rata-rata.
    
- **Masalahnya:** Padahal, Juara 1 mungkin jauh lebih jenius daripada Juara 10. Kita seharusnya memberi perhatian lebih pada si Juara 1 karena dialah "solusi emas" yang sebenarnya kita cari.
    

Penulis berpendapat bahwa dalam prakteknya, kita sangat peduli pada hasil yang paling ekstrem (paling ujung kiri), jadi memperlakukan semua sampel di ekor secara sama rata itu kurang optimal2.

---

### 2. Solusi: Memberi Bobot (Weighted CVaR) - Persamaan (21)

Untuk memperbaiki ini, penulis memperkenalkan bobot ($w_k$) yang berbeda-beda untuk setiap sampel yang terpilih.

Rumus WCVaR:

$$WCVaR_{\alpha}(E) = \sum_{k=1}^{\lceil \alpha K \rceil} w_k E_{(k)}$$

3

Mari kita bedah komponennya:

- **$E_{(k)}$:** Energi sampel ke-$k$ yang sudah diurutkan (dari terkecil/terbaik).
    
    - $E_{(1)}$ adalah sampel terbaik (Minimum).
        
    - $E_{(\alpha K)}$ adalah sampel terburuk yang masih masuk kualifikasi.
        
- **$w_k$ (Bobot):** Seberapa penting sampel ke-$k$ ini.
    
    - Penulis merancang agar $w_1$ (bobot untuk juara 1) nilainya **besar**.
        
    - Dan $w_k$ untuk ranking bawah nilainya semakin **mengecil**.
        

Syarat Normalisasi (Persamaan 22):

Agar hitungannya adil, total seluruh bobot harus sama dengan 1.

$$\sum_{k=1}^{\lceil \alpha K \rceil} w_k = 1$$

4

---

### 3. Mengapa Ini Lebih Baik? (Intuisi Fisika)

Dengan metode WCVaR ini, fungsi biaya (Cost Function) menjadi lebih "sensitif" terhadap solusi-solusi elit.

- Jika algoritma menemukan satu saja solusi yang sangat bagus ($E_{(1)}$ rendah sekali), nilai WCVaR akan turun drastis (karena bobot $w_1$ besar).
    
- Ini memberikan sinyal yang sangat kuat ("Hadiah Besar") kepada optimizer: _"Hei! Kamu ada di jalan yang benar! Kejar arah ini!"_
    
- Bandingkan dengan CVaR biasa: satu solusi bagus mungkin "tenggelam" karena dirata-rata dengan teman-temannya yang biasa saja.
    

### 4. Bagaimana Menentukan Nilai Bobotnya?

Di akhir sub-bagian ini, penulis menyebutkan bahwa mereka menggunakan fungsi **Eksponensial** untuk menentukan bobotnya (detailnya ada di Appendix A).

Intinya: Bobot meluruh secara eksponensial seiring turunnya ranking.

- Ranking 1: Bobot sangat besar.
    
- Ranking 2: Bobot agak besar.
    
- ...
    
- Ranking terakhir: Bobot sangat kecil (hampir diabaikan).
    

---

Ringkasan Sub-bagian III.A:

Penulis mengubah logika "Demokrasi" (satu orang satu suara, seperti di CVaR) menjadi logika "Meritokrasi" (yang terbaik suaranya paling didengar, WCVaR). Tujuannya supaya sinyal solusi terbaik tidak tenggelam dalam rata-rata.

Apakah konsep pergeseran dari bobot rata ke bobot bertingkat ini bisa dipahami? Jika ya, kita bisa lanjut melihat "mesin penggerak" bobot ini di sub-bagian B (CMA-ES).

---
---
## 3.2
Baik, mari kita lanjut ke **Bagian III.B Covariance Matrix Adaptation Evolution Strategy (CMA-ES)**.

Bagian ini membahas **"Mesin Pencari"** (Optimizer). Setelah kita menetapkan peta (Cost Function WCVaR) yang ingin dijelajahi, kita butuh kendaraan yang tepat untuk menelusurinya.

Penulis menjelaskan bahwa peta yang kita buat tadi (WCVaR) itu punya karakteristik yang menyulitkan optimizer biasa.

### 1. Masalah: Landscape yang Kasar dan Berisik

Penulis mengakui adanya _trade-off_ (kompromi). Meskipun CVaR dan WCVaR bagus untuk menemukan energi terendah, mereka membuat medan energi menjadi tidak mulus.

- **Non-smooth & Noisy:** Fungsi biaya ini tajam-tajam, tidak kontinyu, dan berisik1.
    
- **Masalah Gradient:** Optimizer standar (seperti _Gradient Descent_ yang biasa dipakai di Machine Learning) bekerja dengan menghitung kemiringan (turunan/gradien). Jika permukaannya kasar atau berundak-undak, gradiennya tidak bisa dihitung atau kacau. Akibatnya, optimizer bisa macet2.
    

### 2. Solusi: CMA-ES (Strategi Evolusi)

Karena kita tidak bisa mengandalkan gradien (turunan), penulis memilih optimizer jenis **Derivative-free** (Bebas Turunan) yang bernama CMA-ES3.

Konsep CMA-ES:

Ini adalah algoritma yang meniru proses evolusi biologi (Survival of the Fittest).

1. **Populasi:** Alih-alih hanya menggerakkan satu titik (single agent), CMA-ES menyebar sekumpulan titik ("populasi") sekaligus di area pencarian4.
    
2. **Seleksi:** Ia melihat titik mana yang menghasilkan energi terendah.
    
3. **Adaptasi (Covariance Matrix):**
    
    - Pusat populasi digeser ke arah titik-titik bagus tadi.
        
    - Bentuk sebarannya (distribusi) diubah. Jika solusi bagus membentuk garis lurus, sebarannya akan dipipihkan memanjang ke arah sana. Inilah yang dimaksud "Adaptasi Matriks Kovariansi".
        

### 3. Keunggulan CMA-ES di Paper Ini

Penulis memilih CMA-ES karena dua alasan utama:

- **Robust terhadap Noise:** Karena dia melihat rata-rata populasi, satu titik data yang _error_ atau berisik tidak akan langsung menyesatkan seluruh pencarian5.
    
- **Non-Convex Friendly:** Dia jago mencari jalan di medan yang berbukit-bukit dan banyak jebakan lokal (_local minima_)6.
    

### 4. Pembanding: COBYLA

Sebagai kontrol eksperimen, penulis juga akan menggunakan **COBYLA**7.

- COBYLA adalah optimizer klasik yang sangat sering dipakai di paper-paper VQE sebelumnya.
    
- Penulis ingin membuktikan: "Apakah CMA-ES (pilihan kami) bisa mengalahkan COBYLA (standar industri)?"
    

Ringkasan Sub-bagian III.B:

"Karena peta WCVaR itu kasar dan susah didaki dengan cara biasa, kami menggunakan strategi 'pasukan terjun payung' (CMA-ES) yang menyebar banyak agen dan berevolusi, alih-alih pendaki tunggal. Kami akan mengadunya melawan juara bertahan (COBYLA)."

Apakah analogi strategi evolusi ini bisa dipahami? Jika sudah jelas, kita bisa lanjut ke sub-bagian C untuk melihat desain sirkuit kuantumnya.

---
---
## 3.3
Tentu, mari kita masuk ke **Bagian III.C VQE Ansatz**.

Bagi seorang mahasiswa fisika, ini adalah bagian di mana kita merakit "eksperimen" kita. Jika Hamiltonian adalah "sistem yang ingin diukur", maka Ansatz adalah "keadaan kuantum yang kita siapkan" untuk diukur.

Dalam VQE, Ansatz adalah fungsi gelombang coba-coba $|\psi(\theta)\rangle$ yang memiliki parameter yang bisa diputar-putar.

### 1. Masalah pada Ansatz Standar (Pauli Two-Design)

Penulis mengawalinya dengan sedikit kritik. Banyak penelitian sebelumnya menggunakan sirkuit bernama _Pauli two-design_.

- **Masalahnya:** Sirkuit ini menggunakan gerbang rotasi acak (_random_). 1
    
- **Akibatnya:** Sulit untuk melakukan _benchmarking_ (uji banding) yang reliabel. Karena acak, hasilnya bisa beda-beda tiap kali dijalankan. Penulis menginginkan struktur yang deterministik dan stabil.
    

### 2. Ansatz Pertama: Two-Local Ansatz (Gambar 1.a)

Ini adalah struktur "pekerja keras" yang sangat umum di komputasi kuantum NISQ.

- **Rotasi Single-Qubit ($R_y, R_z$):**
    
    - Setiap qubit diberikan gerbang rotasi $R_y(\theta)$ dan $R_z(\theta)$. 2
        
    - **Fisika-nya:** Ini memutar arah spin elektron di bola Bloch. Ini memungkinkan kita mengeksplorasi superposisi antara keadaan $|0\rangle$ dan $|1\rangle$.
        
    - Parameter $\theta$ di sinilah yang akan "diputar-putar" oleh optimizer CMA-ES nanti.
        
- **Entanglement (CNOT):**
    
    - Qubit-qubit dihubungkan dengan gerbang CNOT secara berantai (linear entanglement). 3
        
    - **Fisika-nya:** Ini menciptakan keterbelitan (_entanglement_) antar qubit. Ingat suku interaksi $J_{ij} \hat{Z}_i \hat{Z}_j$ di Hamiltonian tadi? Kita butuh sirkuit yang bisa menghasilkan korelasi antar partikel untuk merepresentasikan interaksi risiko antar saham tersebut.
        

### 3. Ansatz Kedua: Block Ansatz (Gambar 1.b)

Penulis juga mencoba desain alternatif yang terinspirasi dari literatur lain4.

- Struktur Blok:
    
    Mereka menggunakan "blok bangunan" khusus yang berisi dua gerbang CNOT dan beberapa rotasi. 5
    
- Kelebihan:
    
    Blok ini diklaim bisa melakukan operasi controlled-unitary yang sembarang (arbitrary). Ini memberikan fleksibilitas lebih tinggi dalam membentuk fungsi gelombang yang kompleks dibandingkan sekadar rantai CNOT biasa.
    

---

Ringkasan Sub-bagian III.C:

Penulis menyiapkan dua jenis "senter" untuk mencari harta karun di gua gelap:

1. **Senter A (Two-Local):** Senter standar, strukturnya jelas (putar spin, lalu kaitkan dengan tetangga).
    
2. **Senter B (Block Ansatz):** Senter modifikasi yang lebih canggih, bisa membentuk pola cahaya (korelasi) yang lebih rumit.
    

Mereka akan mengadu kedua sirkuit ini: mana yang lebih baik dalam menemukan energi terendah?

Apakah fungsi dari rotasi ($R_y, R_z$) dan entanglement (CNOT) dalam membentuk fungsi gelombang coba-coba ini sudah cukup jelas? Jika ya, kita bisa lanjut ke **Bagian IV. NUMERICAL RESULTS** untuk melihat siapa pemenangnya.

---
---
## 3.4
Tentu, mari kita bayangkan sirkuit kuantum di **Gambar 1** sebagai sebuah jalur perakitan (assembly line) atau sebuah koreografi tarian. Data (informasi kuantum) bergerak dari kiri (awal) ke kanan (akhir).

Mari kita ikuti perjalanan para "penari" kita, yaitu **Qubit** ($q_0, q_1, q_2, q_3$). Di awal cerita (paling kiri), semua qubit berdiri diam dalam posisi netral (state $|0\rangle$).

---

### Cerita 1: Petualangan di Jalur "Two-Local" (Gambar 1a)

Ini adalah jalur yang lebih sederhana dan terstruktur lapis demi lapis.

Babak 1: Pemanasan Solo (Rotasi Awal)

Perjalanan dimulai. Keempat qubit ($q_0$ sampai $q_3$) pertama-tama melakukan gerakan solo masing-masing.

- Mereka melewati gerbang **$R_y$** dan **$R_z$** (kotak merah dan biru di kolom pertama).
    
- **Ceritanya:** Setiap qubit diputar arah spin-nya. Ini seperti memberi mereka "kepribadian" awal. Parameter $\theta$ menentukan seberapa jauh mereka harus berputar. Sekarang, mereka tidak lagi netral, tapi berada dalam posisi superposisi (campuran 0 dan 1) yang unik1111.
    

Babak 2: Bergandengan Tangan (Entanglement Layer)

Setelah pemanasan solo, mereka mulai berinteraksi dengan tetangganya lewat gerbang CNOT (garis vertikal dengan simbol + dan titik hitam).

- **Ceritanya:**
    
    - $q_0$ memegang tangan $q_1$. Jika $q_0$ berputar, $q_1$ harus ikut bereaksi.
        
    - Kemudian $q_1$ memegang $q_2$, dan $q_2$ memegang $q_3$.
        
    - Lalu pola ini bergeser (di kolom berikutnya), menghubungkan pasangan yang berbeda.
        
- **Efeknya:** Sekarang nasib mereka terikat (_entangled_). Informasi tidak lagi milik satu qubit sendirian, tapi tersebar di antara mereka berempat2.
    

Babak 3: Pengulangan (Repetisi Blok)

Proses ini diulang kembali di blok tengah (kotak putus-putus).

- Mereka melakukan rotasi solo lagi ($R_y, R_z$) untuk mengubah arah berdasarkan kondisi baru mereka.
    
- Lalu mereka bergandengan tangan (CNOT) lagi untuk memperkuat ikatan tim.
    
- Di ujung kanan, mereka melakukan satu rotasi terakhir sebelum "panggung ditutup" (diukur).
    

---

### Cerita 2: Masuk ke dalam "Kotak Misterius" (Gambar 1b - Block Ansatz)

Jalur ini sedikit berbeda. Alih-alih lapisan tipis yang berulang, qubit masuk ke dalam modul-modul besar yang disebut **Block**.

Babak 1: Masuk ke Blok Pertama

Lihat kotak putus-putus besar di kiri yang melingkupi $q_0$ dan $q_1$. Ini adalah satu "Block".

- **Di dalam Blok:**
    
    1. $q_0$ dan $q_1$ masuk dan langsung diputar ($R_z, R_y$).
        
    2. Mereka langsung diikat dengan **CNOT** pertama.
        
    3. Setelah terikat, salah satu dari mereka ($q_1$) diputar lagi ($R_y, R_z$) di tengah-tengah.
        
    4. Mereka diikat lagi dengan **CNOT** kedua.
        
    5. Terakhir, mereka diputar lagi sebelum keluar dari blok.
        
- **Intinya:** Di dalam blok ini terjadi pengadukan informasi yang sangat intensif antara dua qubit tersebut. Ini seperti mereka masuk ke "ruang diskusi privat" dan keluar dengan kesepakatan yang sangat kuat 3333.
    

Babak 2: Estafet ke Blok Berikutnya

Setelah keluar dari blok pertama, perhatikan bahwa garis $q_1$ berlanjut ke kanan dan masuk ke blok lain (kotak merah bertuliskan "Block").

- Kali ini, $q_1$ mungkin akan berpasangan dengan $q_2$.
    
- Informasi yang dibawa $q_1$ dari hasil diskusinya dengan $q_0$ tadi, sekarang dibawa masuk untuk diaduk bersama $q_2$.
    

Babak 3: Hasil Akhir

Data mengalir melewati serangkaian blok ini. Setiap kali keluar dari satu blok, qubit membawa korelasi yang makin kompleks, menciptakan pola gelombang fungsi yang sangat spesifik di ujung kanan jalur.

---

**Ringkasan Perbedaan Cerita:**

- **Gambar 1a:** Seperti senam massal. Semua baris bergerak bersamaan: Putar $\rightarrow$ Pegang Tangan $\rightarrow$ Putar $\rightarrow$ Pegang Tangan.
    
- **Gambar 1b:** Seperti kerja kelompok. Dua orang masuk ruang diskusi (Block), bicara intensif, lalu keluar dan salah satunya pindah ke kelompok lain untuk menyebarkan hasil diskusi.

---
---
# NUMERICAL RESULTS
## 4.1
Tentu, mari kita masuk ke **Bagian IV. NUMERICAL RESULTS**.

Setelah merancang teori dan sirkuitnya, sekarang penulis melakukan uji coba "lapangan". Dua paragraf pertama ini menjelaskan **"Bahan Baku Eksperimen"** dan **"Aturan Penilaian"**.

### 1. Bahan Baku: Portofolio Lintas Negara (Paragraf 1)

Penulis tidak menggunakan data acak, melainkan data pasar saham sungguhan. Berikut rinciannya:

- Ukuran Sistem ($N=12$):
    
    Mereka membangun portofolio yang terdiri dari 12 saham1.
    
    - _Catatan Fisika:_ Mengapa 12? Dalam simulasi kuantum (menggunakan komputer klasik), setiap penambahan 1 qubit melipatgandakan memori yang dibutuhkan ($2^N$). Angka 12 ($2^{12} = 4096$ kemungkinan) cukup kompleks untuk membuktikan konsep, tapi masih ringan untuk disimulasikan di laptop/server klasik tanpa memakan waktu tahunan.
        
- Komposisi "Gado-Gado" (Diversifikasi):
    
    Penulis sengaja mencampur dua pasar berbeda untuk melihat apakah algoritma bisa menangani korelasi yang kompleks:
    
    - **6 Saham China (A-shares):** Mewakili berbagai sektor (Keuangan, konsumsi, teknologi, energi)2.
        
    - **6 Saham Amerika (US Equities):** Terutama perusahaan teknologi besar (_large-cap_)3.
        
    - _Tujuannya:_ Menciptakan portofolio yang terdiversifikasi secara geografis dan industri4.
        
- Data Waktu:
    
    Menggunakan harga penutupan harian sepanjang tahun kalender 20245. Data ini kemudian diolah menjadi matriks kovariansi dan return harian 6 yang menjadi input Hamiltonian di persamaan (14) tadi.
    

---

### 2. Aturan Penilaian: "Top-10 Hit Rate" (Paragraf 2)

Ini bagian penting. Bagaimana kita mendefinisikan "Sukses"? Apakah harus selalu tepat sasaran 100%?

Karena VQE adalah algoritma probabilistik (hasilnya berupa peluang), penulis membuat aturan main yang pragmatis:

- Proyeksi ke Basis Komputasi:
    
    Setiap kali VQE selesai satu putaran (iterasi), ia menghasilkan fungsi gelombang $|\psi\rangle$. Penulis "mengukur" fungsi gelombang ini untuk melihat peluang munculnya setiap bitstring (misal: peluang 1010... muncul 30%, peluang 0011... muncul 15%, dst)7.
    
- Kriteria Sukses (The Top 10 Rule):
    
    Penulis sudah tahu jawaban kuncinya (Ground State eksak) karena mereka menghitungnya pakai brute force (karena cuma 12 saham, komputer biasa bisa menghitung jawaban pastinya untuk contekan).
    
    Aturannya:
    
    > _"The algorithm was deemed successful in that iteration if the exact ground state ... was found among the top 10 states ranked by their measurement probabilities."_8.
    
    - **Analogi:** Bayangkan VQE adalah peserta kuis. Dia tidak harus langsung menjawab "Jawabannya A!". Dia boleh bilang "Saya rasa jawabannya mungkin A, B, C, D, ... atau J".
        
    - Jika jawaban yang benar (Kunci Jawaban) ada di dalam daftar **10 tebakan teratas** peserta tersebut, maka iterasi itu dianggap **SUKSES**.
        
- Skor Akhir:
    
    Total performa dihitung dari berapa jumlah iterasi yang sukses selama proses optimisasi berjalan9.
    

Ringkasan Dua Paragraf Ini:

"Kami mengambil 12 saham campuran China-AS dari tahun 2024. Lalu kami menyuruh algoritma VQE menebak kombinasi terbaik. Kalau tebakan benar masuk dalam 'Top 10 Kandidat' yang diajukan VQE, kami anggap itu satu poin sukses."

Apakah penjelasan mengenai setup data dan cara penilaian (skoring) ini bisa dipahami? Selanjutnya kita akan melihat grafik hasil pertandingannya.

---
---
## 4.2
Tentu, mari kita selesaikan petualangan di **Bagian IV. NUMERICAL RESULTS** ini.

Setelah penulis menetapkan aturan main ("Top 10 Hit Rate"), sisa bagian ini membahas hasil pertandingan antara berbagai kombinasi strategi. Mari kita bedah grafik demi grafik (Gambar 2, 3, dan 4) untuk melihat siapa juaranya.

### 1. Analisis Grafik "Balapan" (Figure 2) - Siapa yang Paling Cepat?

Grafik ini menunjukkan **Success Rate** (seberapa sering algoritma menemukan jawaban benar) pada berbagai iterasi. Bayangkan ini sebagai laporan hasil balapan mobil dengan mesin dan bahan bakar berbeda.

**Peserta Lomba:**

- **Mesin (Optimizer):** CMA-ES (Evolusi) vs COBYLA (Klasik).
    
- **Bahan Bakar (Cost Function):** CVaR (Rata-rata ekor) vs WCVaR (Bobot bertingkat).
    
- **Setelan Mesin (Alpha $\alpha$):** 1.0 (pakai semua data), 0.5, 0.25, dan 0.1 (hanya pakai 10% data terbaik).
    

**Hasil Temuan Utama:**

- Keajaiban WCVaR (Bahan Bakar Super):
    
    Penulis menemukan sesuatu yang mengejutkan: Performa WCVaR sangat stabil dan tidak peduli berapapun nilai $\alpha$-nya1.
    
    - Mau $\alpha=1$ (pakai semua data) atau $\alpha=0.1$ (pakai sedikit data), WCVaR tetap ngebut dan sukses menemukan solusi2.
        
    - _Maknanya:_ Ini sangat memudahkan pengguna. Kita tidak perlu pusing melakukan _tuning_ parameter $\alpha$. Tinggal pasang $\alpha=1$ saja sudah bagus.
        
- Kelemahan CVaR (Bahan Bakar Lama):
    
    Sebaliknya, CVaR standar sangat sensitif/rewel.
    
    - Saat $\alpha=1$ atau $0.5$, performanya hancur (kalah jauh dari WCVaR)3.
        
    - Dia baru bisa menyamai WCVaR kalau $\alpha$-nya dikecilkan sekali ke 0.25 atau 0.14.
        
- Kemenangan Mutlak CMA-ES (Mesin Evolusi):
    
    Mesin CMA-ES terbukti jauh lebih unggul daripada COBYLA5.
    
    - COBYLA sering macet dan gagal mencapai performa maksimal meskipun diberi waktu (iterasi) lebih banyak.
        
    - CMA-ES lebih cepat konvergen (grafiknya cepat naik ke angka sukses tinggi).
        

---

### 2. Analisis "Jenis Bobot" (Figure 4) - Resep Mana yang Paling Enak?

Setelah tahu WCVaR itu bagus, penulis bertanya: _"Oke, tapi cara memberi bobotnya (weighting) yang paling bagus seperti apa?"_. Mereka menguji 4 resep bobot (dijelaskan di Appendix A tapi hasilnya dibahas di sini):

- **W1 (CVaR Standar):** Bobot rata. Hanya bagus kalau $\alpha$ kecil6.
    
- **W2 (Energy-based):** Bobot berdasarkan nilai energi. Ternyata ini **paling buruk**7.
    
- **W3 (Rank-based):** Bobot berdasarkan ranking (Juara 1 dapat sekian, Juara 2 dapat sekian). Ini **bekerja sangat baik**, terutama saat $\alpha$ besar8.
    
- **W4 (Piecewise Exponential):** Ini resep andalan penulis (gabungan beberapa kurva eksponensial).
    

Kesimpulan Eksperimen Bobot:

Resep W4 (Piecewise) adalah yang terbaik, sedikit mengalahkan W39. Tapi penulis mencatat, kalau mau rumus yang simpel, pakai W3 (Rank-based) saja sudah cukup bagus dan efektif10.

---

### 3. Kesimpulan Akhir Bagian IV (Paragraf Terakhir)

Dari semua eksperimen ini, penulis menarik kesimpulan tegas untuk menutup bab Hasil:

1. **Ansatz Tidak Ngaruh:** Pilihan bentuk sirkuit (Two-local vs Block) ternyata tidak memberikan perbedaan performa yang signifikan11. Dua-duanya oke.
    
2. Kombinasi Juara: Kunci kemenangan ada di Optimizer + Cost Function. Kombinasi terbaik yang direkomendasikan paper ini adalah:
    
    **CMA-ES (Optimizer) + WCVaR (Cost Function)**12.
    

Kombinasi inilah yang memberikan probabilitas tertinggi untuk menemukan portofolio saham yang paling optimal.

---

Dengan ini, kita sudah selesai membedah seluruh isi teknis paper mulai dari masalah keuangan, teori kuantum, hingga hasil eksperimennya. Bagian V hanyalah kesimpulan umum yang merangkum apa yang sudah kita bahas.

Apakah ada bagian tertentu dari hasil eksperimen ini yang ingin kamu diskusikan lebih dalam, atau sudah cukup jelas?

---
---
---
# Appendix 
## A
Tentu, mari kita bedah **Appendix A: Weights in WCVaR cost function**.

Jika bagian sebelumnya adalah "Hasil Masakan", Appendix A ini adalah **"Resep Rahasia Saus-nya"**. Di sini penulis menjelaskan secara detail matematika di balik pembobotan (weighting) yang mereka sebutkan di Bagian III.A tadi.

Mereka mendefinisikan himpunan energi yang sudah diurutkan dari terkecil (terbaik) ke terbesar: $E = (E_{(1)}, E_{(2)}, ..., E_{(K)})$1.

Penulis memperkenalkan **4 Varian Resep Bobot**:

### 1. Resep "Demokrasi" (Standard CVaR) - Persamaan (A1)

Ini adalah pembanding dasar (CVaR biasa).

$$w_k = \begin{cases} 1 & \text{jika } k \le \lceil \alpha K \rceil \\ 0 & \text{lainnya} \end{cases}$$

- **Konsep:** Semua sampel yang masuk dalam daftar "Top $\alpha$" diberi bobot sama rata (nilai 1), dan sisanya 0 2.
    
- **Analogi:** Seperti pemilu, suara profesor jenius (Rank 1) dan mahasiswa baru (Rank terakhir yang lolos) dihitung sama, satu suara.
    

---

### 2. Resep "Fisika Boltzmann" (Energy-based Exponential) - Persamaan (A2)

Resep ini terinspirasi langsung dari **Hukum Boltzmann** di fisika statistik atau fungsi **Softmax** di _machine learning_3.

$$w_k = \exp[-\beta(E_{(k)} - E_0)]$$

- **$E_0$:** Energi minimum (Ground State yang ditemukan).
    
- **$\beta$:** _Inverse temperature_ (seperti $1/k_BT$). Mengontrol seberapa tajam kurvanya.
    
- **Konsep:** Semakin rendah energi suatu sampel (makin dekat ke $E_0$), bobotnya makin besar secara eksponensial 4.
    
- **Hasil:** Ternyata resep ini **performanya paling buruk** (disebutkan di pembahasan Fig 4)5.
    
    - _Analisis:_ Kemungkinan karena nilai absolut energi ($E_{(k)}$) dalam VQE bisa berubah-ubah secara drastis dan "berisik" selama optimisasi, membuat bobotnya jadi tidak stabil.
        

---

### 3. Resep "Sistem Ranking" (Rank-based Exponential) - Persamaan (A3)

Penulis mencoba menghilangkan ketergantungan pada nilai energi absolut. Mereka hanya peduli pada **urutan (ranking)**.

$$w_k = \exp(-\beta k)$$

- **$k$:** Nomor urut ranking (1, 2, 3, ...).
    
- **Konsep:**
    
    - Juara 1 (Rank $k=1$) dapat bobot terbesar ($e^{-\beta}$).
        
    - Juara 2 (Rank $k=2$) dapat bobot lebih kecil ($e^{-2\beta}$).
        
    - Bobot meluruh murni berdasarkan posisi urutan 6.
        
- **Hasil:** Ini jauh lebih stabil dan efektif daripada resep basis energi7.
    

---

### 4. Resep "Kustom Tiga Tingkat" (Piecewise Exponential) - Persamaan (A4)

Ini adalah resep "Spesial Koki" yang paling rumit tapi memberikan hasil terbaik. Penulis membagi distribusi sampel menjadi **tiga zona** dengan kecepatan peluruhan ($\beta$) yang berbeda-beda 8:

$$w_k = \begin{cases} \exp(-\beta_1 k) & \text{Zona Elit (Awal)} \\ W_{N1} \cdot \exp(-\beta_2 (k - N_1)) & \text{Zona Menengah} \\ W_{N2} \cdot \exp(-\beta_3 (k - N_2)) & \text{Zona Ekor (Akhir)} \end{cases}$$

- **Zona Elit ($k < N_1$):** Menggunakan $\beta_1$. Mungkin disetel agar bobotnya sangat sensitif (turun cepat) untuk membedakan yang "Sangat Baik" dari yang "Cukup Baik".
    
- **Zona Ekor:** Menggunakan $\beta_3$. Peluruhannya mungkin lebih landai.
    
- **Kontinuitas:** Rumus ini dirancang agar sambungan antar zona mulus (kontinyu)9.
    

Kesimpulan Appendix A:

Meskipun resep Piecewise (A4) adalah yang paling canggih, penulis mengakui bahwa resep Rank-based (A3) adalah alternatif yang sangat menarik karena lebih sederhana (lebih sedikit parameter yang harus diatur) namun performanya sudah sangat bagus 10.

Ini mengakhiri seluruh bedah _paper_ "Achieving High-Quality Portfolio Optimization with VQE".

Dari Introduction hingga Appendix, Anda sekarang sudah memahami:

1. **Masalah:** Portofolio Saham (QUBO/Ising).
    
2. **Solusi:** VQE + CMA-ES + WCVaR.
    
3. **Detail Teknis:** Sirkuit kuantum, penalti, dan rumus bobot ranking.
    

Apakah ada bagian manapun dari keseluruhan _paper_ ini yang ingin Anda ulas kembali atau diskusikan lebih dalam?