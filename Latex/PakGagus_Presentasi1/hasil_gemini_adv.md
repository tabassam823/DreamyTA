# INTRODUCTION
## 1.1

Analisis terhadap karya ilmiah dilakukan secara bertahap untuk memastikan pemahaman yang mendalam terhadap setiap bagian materi. Pembahasan dimulai pada paragraf pertama bagian Pendahuluan (Introduction) yang berfungsi sebagai landasan untuk mengidentifikasi permasalahan utama serta urgensi penggunaan komputasi kuantum dalam penyelesaiannya. Terdapat empat konsep utama yang diidentifikasi dalam paragraf tersebut beserta kontribusinya terhadap penelitian ini.

Pertama, optimisasi portofolio diposisikan sebagai masalah fundamental dalam bidang keuangan yang bertujuan untuk mengalokasikan modal ke berbagai aset guna memaksimalkan keuntungan sekaligus meminimalkan risiko [1]. Dalam penelitian ini, optimisasi portofolio digunakan sebagai studi kasus utama di mana algoritma yang diusulkan diuji menggunakan data pasar riil, termasuk saham China A-shares dan pasar Amerika Serikat [2]. Kedua, permasalahan portofolio tersebut diformulasikan ke dalam model Quadratic Unconstrained Binary Optimization (QUBO) [3]. Formulasi QUBO melibatkan fungsi matematika kuadratik dengan variabel biner (0 atau 1) tanpa batasan eksplisit, di mana batasan tersebut biasanya diintegrasikan ke dalam fungsi objektif sebagai penalti [4]. QUBO berfungsi sebagai jembatan untuk menerjemahkan permasalahan keuangan ke dalam format fisik, seperti model Ising, yang dapat diselesaikan oleh algoritma kuantum [5].

Ketiga, klasifikasi masalah QUBO sebagai kategori NP-hard menjadi motivasi utama penelitian ini. Kompleksitas komputasi yang meningkat secara eksponensial seiring bertambahnya jumlah aset menyebabkan komputer klasik mengalami kesulitan dalam menemukan solusi optimal dalam waktu yang wajar [6]. Oleh karena itu, penggunaan komputasi kuantum diusulkan sebagai alternatif solusi untuk mengatasi hambatan tersebut. Keempat, teknologi komputasi kuantum yang memanfaatkan prinsip mekanika kuantum menawarkan potensi efisiensi yang lebih tinggi dalam menyelesaikan masalah QUBO [7]. Secara spesifik, penelitian ini mengeksplorasi penggunaan algoritma Variational Quantum Eigensolver (VQE) untuk memberikan solusi berkualitas tinggi terhadap permasalahan yang memiliki tingkat kesulitan tinggi tersebut [8]. Secara keseluruhan, alur argumen yang dibangun menegaskan bahwa kompleksitas optimisasi portofolio yang bersifat NP-hard memerlukan pendekatan komputasi kuantum melalui formulasi QUBO.

---
---
## 1.2
Paragraf kedua dalam bagian Pendahuluan mendefinisikan instrumen komputasi yang tersedia untuk menyelesaikan permasalahan yang telah dipaparkan sebelumnya. Fokus utama diarahkan pada algoritma *Variational Quantum Eigensolver* (VQE) dan *Quantum Approximate Optimization Algorithm* (QAOA), yang dipandang sebagai kandidat potensial untuk dijalankan pada perangkat *Noisy Intermediate-Scale Quantum* (NISQ) [1].

Kedua algoritma tersebut diklasifikasikan sebagai algoritma hibrida yang memanfaatkan sinergi antara komputer kuantum dan komputer klasik. Dalam mekanisme kerjanya, komputer kuantum digunakan untuk menangani tugas-tugas komputasi yang kompleks, seperti perhitungan energi sistem, sementara komputer klasik melakukan optimisasi parameter secara iteratif hingga mencapai hasil yang optimal [2]. Pemilihan VQE sebagai fokus utama dalam penelitian ini didasarkan pada karakteristik algoritma tersebut yang dianggap lebih relevan dalam penyelesaian masalah optimisasi portofolio. Selain itu, penggunaan perangkat NISQ memberikan konteks realitas terhadap keterbatasan perangkat keras kuantum saat ini. Meskipun perangkat NISQ masih memiliki tingkat gangguan (*noise*) yang signifikan dan jumlah qubit yang terbatas untuk koreksi kesalahan sempurna, VQE dinilai memiliki ketahanan yang memadai untuk beroperasi dalam kondisi tersebut guna menghasilkan solusi praktis pada era sekarang.

---
---
## 1.3
Tantangan teknis utama dalam penerapan VQE untuk masalah optimisasi portofolio dijelaskan pada paragraf ketiga. Ditekankan bahwa penyelesaian masalah QUBO memiliki perbedaan signifikan dibandingkan dengan pencarian *ground state* pada Hamiltonian kimia tradisional. Perbedaan ini berakar pada struktur matematika dari masalah yang dihadapi.

Dalam konteks keuangan, model yang digunakan adalah Hamiltonian Ising di mana seluruh komponen operatornya bersifat komutatif. Sifat komutativitas ini menyebabkan *ground state* dari sistem selalu berupa *computational basis state*, yaitu representasi biner murni (0 dan 1). Kondisi ini berbeda dengan sistem kimia yang sering kali melibatkan superposisi kuantum yang sangat kompleks. Lebih lanjut, penggunaan nilai ekspektasi energi tradisional (*traditional expectation value*) sebagai fungsi biaya dinilai tidak ideal untuk masalah QUBO. Penggunaan rata-rata energi dianggap kurang efektif dalam mengidentifikasi solusi optimal yang spesifik, karena nilai rata-rata tersebut cenderung mengaburkan keberadaan status energi terendah yang dicari. Oleh karena itu, diperlukan modifikasi pada fungsi biaya agar algoritma dapat lebih fokus dalam menemukan solusi biner yang tepat.

---
---
## 1.4
Paragraf terakhir pada bagian Pendahuluan memperkenalkan solusi inovatif yang ditawarkan dalam penelitian ini untuk mengatasi keterbatasan nilai ekspektasi standar. Konsep *Conditional Value-at-Risk* (CVaR) diadopsi dari bidang keuangan sebagai dasar perhitungan fungsi biaya yang baru. Berbeda dengan perhitungan rata-rata sistem secara keseluruhan, CVaR berfokus pada rata-rata dari ekor distribusi (*tail distribution*) energi terendah, yang memungkinkan algoritma untuk lebih berkonsentrasi pada kandidat solusi terbaik [1].

Sebagai kontribusi utama, penelitian ini mengusulkan pengembangan metode tersebut menjadi *Weighted CVaR* (WCVaR). Melalui metode WCVaR, bobot yang berbeda diberikan kepada setiap kandidat solusi dalam distribusi ekor, di mana solusi dengan peringkat lebih tinggi mendapatkan prioritas yang lebih besar untuk mempercepat konvergensi menuju solusi optimal [2]. Untuk menangani landskap pencarian yang bersifat *non-smooth* akibat penggunaan WCVaR, algoritma *Covariance Matrix Adaptation Evolution Strategy* (CMA-ES) dipilih sebagai pengoptimasi (*optimizer*). Kombinasi antara WCVaR dan CMA-ES diusulkan sebagai pendekatan yang tangguh karena tidak memerlukan perhitungan gradien matematika. Hasil eksperimen melalui simulasi klasik pada platform *Wuyue QuantumAI* menunjukkan bahwa integrasi metode ini memberikan peningkatan performa yang signifikan dibandingkan dengan metode konvensional [3, 4]. Secara keseluruhan, bagian ini menegaskan bahwa sinergi antara pengembangan fungsi biaya WCVaR dan penggunaan pengoptimasi CMA-ES merupakan kunci utama dalam mencapai efisiensi tinggi pada optimisasi portofolio berbasis kuantum.

---
---
---
# BACKGROUND

## 2.1
Bagian II.A membahas optimisasi portofolio dengan fokus pada tahap prapemrosesan data. Sebelum diimplementasikan pada komputer kuantum, data mentah dari pasar pasar modal ditransformasikan menjadi parameter statistik yang dapat diukur. Data pasar direpresentasikan melalui matriks harga $P$ berukuran $M \times N$, di mana $N$ menyatakan jumlah aset dan $M$ menyatakan periode waktu pengamatan [1, 2].

Transformasi data dilakukan dengan menghitung tingkat pengembalian (*return*) $r_{ki}$ pada Persamaan (1), yang menstandarisasi perubahan harga antar periode [3]. Selanjutnya, ekspektasi tingkat pengembalian $\mu_i$ dihitung sebagai rata-rata dari *return* harian aset tersebut untuk merepresentasikan potensi keuntungan [4]. Langkah terakhir dalam prapemrosesan data adalah penghitungan kovariansi $\sigma_{ij}$ sesuai Persamaan (3), yang digunakan untuk mengukur risiko portofolio berdasarkan fluktuasi harga dan korelasi pergerakan antar aset [5]. Parameter $\mu$ dan $\sigma$ inilah yang menjadi komponen utama dalam penyusunan model optimisasi.

---
---
## 2.2
Model matematika portofolio disusun berdasarkan parameter statistik yang telah diperoleh sebelumnya untuk mendefinisikan tujuan dan batasan optimisasi. Terdapat tiga komponen utama yang diidentifikasi, yaitu kendala modal, pemaksimalan keuntungan, dan peminimalan risiko. Kendala modal, sebagaimana dinyatakan dalam Persamaan (4), membatasi alokasi dana $b_i$ untuk setiap aset agar total belanja tidak melebihi anggaran $B$ yang tersedia [1, 2].

Tujuan pertama dalam model ini adalah memaksimalkan ekspektasi keuntungan portofolio $C_1(b)$, yang merupakan fungsi linear dari alokasi dana dan rata-rata *return* aset [3, 4]. Tujuan kedua adalah meminimalkan risiko portofolio $C_2(b)$ yang diukur melalui varians portofolio pada Persamaan (6). Berbeda dengan fungsi keuntungan, fungsi risiko bersifat kuadratik karena melibatkan interaksi kovariansi $\sigma_{ij}$ antar aset. Hal ini mencerminkan bahwa risiko portofolio dapat meningkat secara non-linear akibat korelasi antar aset yang dipilih [5, 6]. Model ini secara eksplisit menunjukkan adanya tarik-ulur (*trade-off*) antara keinginan untuk mencapai keuntungan maksimal dan keharusan untuk menekan risiko minimal.

---
---
## 2.3
Strategi penggabungan tujuan dilakukan untuk menangani masalah optimisasi multi-objektif, di mana tidak terdapat satu solusi tunggal yang optimal untuk seluruh parameter secara simultan. Dalam konteks ini, konsep *Pareto Front* atau *Efficient Frontier* digunakan untuk merepresentasikan sekumpulan solusi efisien yang mencerminkan keseimbangan antara keuntungan dan risiko. Untuk memungkinkan pemrosesan oleh algoritma optimisasi, kedua tujuan tersebut disatukan menjadi fungsi objektif tunggal $C'$ melalui metode skalarisasi dengan memperkenalkan faktor pembobot $\lambda$.

Fungsi objektif gabungan pada Persamaan (7), $C'(b) = -\lambda C_1(b) + (1-\lambda)C_2(b)$, dirancang untuk meminimalkan biaya total yang merepresentasikan preferensi risiko investor. Nilai $\lambda$ yang berkisar antara 0 hingga 1 berfungsi sebagai pengatur proporsi antara pengejaran keuntungan dan penghindaran risiko. Tanda negatif pada komponen keuntungan $-\lambda C_1$ digunakan agar algoritma yang berbasis minimisasi dapat secara efektif memaksimalkan keuntungan [1]. Dengan demikian, minimisasi terhadap fungsi $C'$ secara otomatis akan mencari titik optimal yang memenuhi batasan anggaran dan preferensi risiko yang telah ditetapkan.

---
---
## 2.4
Tahap selanjutnya adalah transformasi masalah portofolio ke dalam format *Quadratic Unconstrained Binary Optimization* (QUBO). Proses penerjemahan ini penting agar masalah keuangan dapat dipahami oleh algoritma optimisasi standar dan komputer kuantum. Bentuk umum QUBO pada Persamaan (8) melibatkan variabel biner $x_i \in \{0, 1\}$ dengan interaksi kuadratik yang merepresentasikan risiko serta bias linear yang merepresentasikan keuntungan [1, 2].

Untuk menyesuaikan dengan keterbatasan qubit pada komputer kuantum saat ini, dilakukan penyederhanaan variabel alokasi dana dari bilangan riil menjadi keputusan biner untuk memilih atau tidak memilih suatu aset [3, 4]. Dalam model ini, ditetapkan batasan bahwa portofolio harus terdiri dari tepat $N/2$ aset dari total $N$ aset yang tersedia [5, 6]. Karena format QUBO bersifat tanpa batasan (*unconstrained*), batasan tersebut diintegrasikan ke dalam fungsi objektif melalui metode penalti kuadratik sebagaimana ditunjukkan pada Persamaan (10) [7]. Implementasi penalti ini menciptakan "sumur energi" pada konfigurasi yang mematuhi aturan, sehingga peminimalan fungsi pada Persamaan (12) secara otomatis akan mengarah pada solusi yang valid. Secara keseluruhan, Persamaan (12) merangkum komponen keuntungan, risiko, dan penalti menjadi satu fungsi biaya tunggal yang siap dikonversi ke dalam sistem energi fisik.

---
---
Analogi fisik dari suku penalti dijelaskan melalui prinsip mekanika klasik, khususnya menggunakan model osilator harmonik sederhana. Suku penalti dalam Persamaan (12) memiliki bentuk matematis $(x - x_0)^2$ yang identik dengan rumus energi potensial pegas $U(x) = \frac{1}{2} k (x - x_0)^2$. Dalam konteks ini, jumlah aset yang dipilih dianalogikan sebagai posisi partikel, target jumlah aset $N/2$ sebagai posisi setimbang, dan koefisien penalti $p$ sebagai konstanta kekakuan pegas. Tanpa adanya suku penalti, sistem bebas bergerak mencari energi terendah tanpa batasan, namun penerapan penalti menciptakan hambatan energi yang memaksa sistem untuk berada pada kondisi yang mematuhi aturan jumlah aset.

Secara visual, metode penalti ini melakukan rekayasa terhadap lanskap potensial (*potential landscape*) sehingga titik energi terendah (*ground state*) berada pada koordinat yang valid. Hal ini dapat diilustrasikan melalui simulasi grafik di mana penalti mengubah fungsi linear menjadi kurva parabola yang curam. Semakin besar nilai koefisien penalti $p$, semakin tajam lembah energi yang terbentuk pada titik target, sehingga memastikan algoritma VQE menemukan solusi yang memenuhi batasan anggaran dan jumlah aset.


---
---
Bagian II.C menguraikan mekanisme implementasi *Variational Quantum Eigensolver* (VQE) dalam penyelesaian masalah optimisasi. Proses ini dimulai dengan transformasi variabel biner $x_i \in \{0, 1\}$ menjadi variabel spin $s_i \in \{+1, -1\}$ melalui pemetaan $s_i = 1 - 2x_i$ pada Persamaan (13). Hasil dari pemetaan ini mengubah masalah QUBO menjadi model energi Ising klasik. Selanjutnya, variabel tersebut dikonversi menjadi operator Pauli-Z ($\hat{Z}_i$) untuk membangun Hamiltonian sistem ($\hat{H}$) sebagaimana ditunjukkan pada Persamaan (14).

Penyelesaian masalah optimisasi portofolio kemudian didefinisikan sebagai upaya untuk menemukan *ground state* dari Hamiltonian tersebut. Mengingat kompleksitas pencarian *ground state* secara umum masuk dalam kategori *QMA-complete*, pendekatan heuristik menggunakan algoritma VQE diterapkan secara hibrida antara unit pemroses kuantum (QPU) dan unit pemroses klasik (CPU). Mekanisme kerja VQE melibatkan penyiapan fungsi gelombang coba-coba (*ansatz*) $|\psi(\theta)\rangle$ pada QPU, yang kemudian energinya diukur dan dioptimalkan secara iteratif oleh CPU menggunakan parameter $\theta$. Fungsi objektif yang diminimalkan dalam proses ini adalah nilai ekspektasi energi sesuai dengan Persamaan (15).

---
---

Struktur Hamiltonian pada Persamaan (13) dirancang dengan tanda negatif pada seluruh sukunya untuk menyelaraskan masalah keuangan dengan konvensi minimisasi energi dalam fisika. Dalam model Ising ferromagnetik, konfigurasi spin yang sejajar menghasilkan energi yang lebih rendah, sehingga penggunaan tanda negatif memastikan bahwa keuntungan maksimal dalam portofolio setara dengan energi terendah dalam sistem fisik. Koefisien $h_i$ merepresentasikan medan magnet eksternal lokal yang mencakup informasi mengenai ekspektasi tingkat pengembalian aset dan suku linear dari penalti. Sementara itu, koefisien $J_{ij}$ merepresentasikan kekuatan interaksi antar spin yang menampung data risiko atau kovariansi portofolio serta interaksi kuadratik dari suku penalti.

Transformasi variabel klasik $s_i$ menjadi operator operator kuantum $\hat{Z}$ didasarkan pada postulat kuantisasi. Operator Pauli-Z dipilih karena memiliki nilai eigen $(+1, -1)$ yang koresponden dengan nilai variabel spin klasik. Pemetaan ini memungkinkan substitusi langsung variabel dalam persamaan energi menjadi operator dalam fungsional Hamiltonian. Secara teknis, operator $\hat{Z}_i$ bekerja pada qubit tertentu dengan identitas pada qubit lainnya dalam sistem multikuantum. Dengan demikian, pengukuran nilai ekspektasi terhadap Hamiltonian pada Persamaan (14) secara matematis identik dengan evaluasi energi pada model Ising klasik yang merepresentasikan kualitas solusi portofolio.

---
---
Evaluasi terhadap efektivitas algoritma VQE standar dalam konteks optimisasi portofolio mengungkapkan keterbatasan pada penggunaan nilai ekspektasi tradisional ($\langle \hat{H} \rangle$). Berbeda dengan simulasi molekul yang mencari superposisi kompleks, *ground state* dari Hamiltonian Ising pada masalah keuangan merupakan *computational basis state* yang merepresentasikan kombinasi biner pasti. Penggunaan rata-rata energi sering kali memberikan indikasi yang menyesatkan bagi pengoptimasi karena nilai rata-rata dapat mengaburkan keberadaan solusi optimal yang memiliki probabilitas rendah namun energi yang sangat menguntungkan.

Sebagai solusi untuk mengatasi masalah tersebut, diadopsi metode *Conditional Value-at-Risk* (CVaR) sebagai fungsi biaya pengganti pada Persamaan (19). Mekanisme ini dilakukan dengan melakukan pengukuran atau sampling sebanyak $K$ kali untuk memperoleh distribusi energi dari berbagai status bitstring. Alih-alih merata-ratakan seluruh sampel, CVaR hanya menghitung rata-rata dari fraksi $\alpha$ sampel dengan energi terendah. Parameter $\alpha$ berfungsi untuk mengatur keseimbangan antara eksplorasi solusi terbaik dan stabilitas perhitungan. Pemilihan $\alpha$ yang moderat direkomendasikan untuk menghindari kekasaran pada lanskap fungsi biaya yang dapat menghambat konvergensi algoritma pengoptimasi.

---
---
---
# DESIGN OF OUR VQE ALGORITHM
Bagian III.A memaparkan inovasi utama dalam penelitian ini, yaitu pengembangan metode *Weighted CVaR* (WCVaR). Konsep ini diajukan sebagai penyempurnaan terhadap metode CVaR standar yang memberikan bobot seragam (*uniform weights*) kepada seluruh sampel dalam fraksi $\alpha$ terbaik. Diterangkan bahwa perlakuan bobot yang setara tersebut kurang optimal karena tidak memberikan prioritas lebih tinggi pada kandidat solusi dengan tingkat energi yang paling ekstrem atau mendekati optimal [1, 2].

Melalui implementasi WCVaR, setiap sampel diberikan bobot $w_k$ yang berbeda berdasarkan peringkat energinya sesuai dengan Persamaan (21). Penentuan bobot dirancang agar solusi dengan peringkat tertinggi mendapatkan nilai bobot yang lebih besar untuk memberikan sinyal yang lebih kuat bagi pengoptimasi dalam melakukan konvergensi. Seluruh bobot yang dialokasikan harus memenuhi syarat normalisasi pada Persamaan (22) di mana total nilai bobot berjumlah satu [3, 4]. Penggunaan fungsi eksponensial dalam penentuan bobot, sebagaimana dijelaskan lebih lanjut dalam Lampiran A, bertujuan untuk meningkatkan sensitivitas fungsi biaya terhadap solusi kelompok elit. Dengan demikian, integrasi WCVaR dalam alur algoritma VQE diharapkan dapat mempercepat identifikasi solusi portofolio terbaik tanpa terhambat oleh nilai rata-rata sampel yang kurang relevan.

---
---
## 3.2
Bagian III.B menguraikan penggunaan *Covariance Matrix Adaptation Evolution Strategy* (CMA-ES) sebagai mekanisme pengoptimasi (*optimizer*) dalam algoritma VQE. Pemilihan CMA-ES didasarkan pada karakteristik fungsi biaya WCVaR yang cenderung menghasilkan lanskap energi yang bersifat kasar (*non-smooth*) dan berisik (*noisy*), sehingga menyulitkan implementasi pengoptimasi berbasis gradien konvensional [1, 2]. CMA-ES diklasifikasikan sebagai algoritma evolusioner yang tidak memerlukan turunan matematika (*derivative-free*) sehingga lebih tangguh terhadap gangguan dan jebakan minima lokal [3].

Mekanisme kerja CMA-ES melibatkan penyebaran sekumpulan kandidat solusi atau populasi pada area pencarian, diikuti dengan seleksi berdasarkan tingkat energi terendah yang dihasilkan [4]. Proses adaptasi dilakukan melalui pembaruan matriks kovariansi untuk menggeser pusat populasi serta menyesuaikan bentuk sebaran menuju area solusi yang menjanjikan [5, 6]. Penggunaan CMA-ES dalam penelitian ini dibandingkan dengan algoritma COBYLA yang merupakan standar umum dalam literatur VQE sebelumnya [7]. Strategi ini dirancang untuk membuktikan keunggulan pendekatan evolusioner dalam menavigasi fungsi biaya yang kompleks guna mencapai konvergensi yang lebih cepat dan stabil.

---
---
## 3.3
Bagian III.C mendeskripsikan perancangan sirkuit kuantum atau *ansatz* yang digunakan untuk merepresentasikan fungsi gelombang coba-coba $|\psi(\theta)\rangle$. Penulis mengajukan dua variasi desain sebagai alternatif terhadap struktur sirkuit rotasi acak konvensional guna memastikan hasil yang lebih deterministik dan stabil [1]. Desain pertama adalah *Two-Local Ansatz* (Gambar 1.a) yang menggunakan kombinasi gerbang rotasi qubit tunggal ($R_y, R_z$) dan gerbang keterbelitan (*entanglement*) CNOT [2, 3]. Gerbang rotasi memungkinkan eksplorasi superposisi pada bola Bloch, sementara gerbang CNOT digunakan untuk mensimulasikan interaksi risiko antar aset melalui keterbelitan kuantum.

Desain kedua yang diujikan adalah *Block Ansatz* (Gambar 1.b) yang mengadopsi struktur modul blok fungsional. Modul ini terdiri dari serangkaian gerbang CNOT dan rotasi yang dirancang untuk melakukan operasi *controlled-unitary* secara fleksibel [4, 5]. Penggunaan *Block Ansatz* bertujuan untuk memberikan fleksibilitas yang lebih tinggi dalam pembentukan fungsi gelombang yang kompleks dibandingkan dengan sirkuit *Two-Local* standar. Kedua jenis *ansatz* ini diuji kinerjanya dalam menemukan status energi terendah untuk menentukan desain sirkuit yang paling efisien dalam konteks optimisasi portofolio.

---
---
## 3.4
Alur kerja sirkuit kuantum pada Gambar 1 digambarkan sebagai proses transformasi informasi kuantum secara bertahap dari status awal $|0\rangle$. Pada sirkuit *Two-Local* (Gambar 1.a), qubit melewati lapisan rotasi qubit tunggal ($R_y, R_z$) untuk pembentukan status superposisi awal, diikuti oleh lapisan keterbelitan yang menggunakan gerbang CNOT secara berurutan [1, 2]. Proses ini diulang melalui beberapa blok repetisi untuk memperkuat korelasi sistem sebelum dilakukan pengukuran pada ujung akhir sirkuit.

Sebaliknya, *Block Ansatz* (Gambar 1.b) menerapkan modul blok besar yang memproses pasangan qubit secara intensif melalui serangkaian gerbang rotasi dan CNOT ganda. Mekanisme ini dirancang untuk menciptakan pengadukan informasi yang mendalam antara dua qubit dalam modul yang sama sebelum informasi tersebut diteruskan ke blok berikutnya [3]. Struktur ini memungkinkan pembentukan korelasi yang lebih kompleks antar qubit, sehingga mampu merepresentasikan pola gelombang fungsi yang lebih spesifik. Perbedaan mendasar antara kedua desain terletak pada metode pengolahan informasinya, di mana desain *Two-Local* berbasis pada pemrosesan lapisan secara serentak, sementara desain *Block* berbasis pada integrasi fungsional dalam modul yang terstruktur.

---
---
# NUMERICAL RESULTS
Bagian IV memaparkan hasil numerik dari pengujian yang dilakukan terhadap algoritma yang diusulkan. Eksperimen dilakukan menggunakan data pasar saham riil yang terdiri dari 12 aset aktif sepanjang tahun kalender 2024. Pemilihan jumlah aset sebanyak 12 didasarkan pada pertimbangan kompleksitas komputasi yang memadai untuk pembuktian konsep tanpa membebani sumber daya komputasi secara berlebihan. Portofolio yang disusun bersifat terdiversifikasi secara geografis dan industri, mencakup enam saham dari pasar China A-shares dan enam saham dari pasar Amerika Serikat (AS). Data harga penutupan harian tersebut kemudian diproses menjadi matriks kovariansi dan tingkat pengembalian yang menjadi parameter masukan bagi Hamiltonian sistem.

Kinerja algoritma dievaluasi berdasarkan kriteria *Top-10 Hit Rate* untuk mengakomodasi sifat probabilistik dari VQE. Dalam setiap iterasi, fungsi gelombang yang dihasilkan diukur untuk menentukan probabilitas kemunculan berbagai status basis komputasi. Iterasi dianggap berhasil apabila status dasar (*ground state*) eksak, yang diperoleh melalui perhitungan *brute force*, ditemukan dalam sepuluh kandidat status dengan probabilitas tertinggi. Skor performa akhir ditentukan oleh total akumulasi iterasi yang berhasil selama proses optimisasi berlangsung.

---
---
Analisis terhadap hasil komputasi pada Gambar 2 menunjukkan bahwa kombinasi WCVaR dan CMA-ES memberikan performa yang paling konsisten dan unggul. Ditemukan bahwa metode WCVaR memiliki ketahanan yang tinggi terhadap perubahan parameter fraksi $\alpha$, di mana keberhasilan pencarian solusi optimal tetap stabil baik pada nilai $\alpha$ yang besar maupun kecil. Sebaliknya, performa CVaR standar sangat dipengaruhi oleh pemilihan nilai $\alpha$, di mana efektivitasnya menurun drastis pada $\alpha$ tinggi dan hanya mampu menyamai performa WCVaR ketika $\alpha$ diatur pada nilai yang sangat rendah. Selain itu, pengoptimasi CMA-ES terbukti jauh lebih efektif dibandingkan COBYLA dalam hal kecepatan konvergensi dan kemampuan menghindari titik minima lokal.

Evaluasi terhadap berbagai varian pembobotan pada Gambar 4 menunjukkan bahwa resep *Piecewise Exponential* (W4) memberikan hasil terbaik, diikuti secara ketat oleh pembobotan berbasis peringkat (*Rank-based*, W3). Pembobotan berbasis energi (W2) ditemukan memiliki performa terendah, kemungkinan disebabkan oleh ketidakstabilan nilai energi absolut selama proses optimisasi. Secara keseluruhan, pengujian ini menegaskan bahwa pemilihan jenis *ansatz* (baik *Two-local* maupun *Block*) tidak memberikan perbedaan performa yang signifikan. Kesimpulan utama dari hasil numerik ini adalah bahwa sinergi antara pengoptimasi CMA-ES dan fungsi biaya WCVaR merupakan faktor penentu utama dalam meningkatkan probabilitas penemuan portofolio saham yang optimal.

---
---
---
# Appendix 
Lampiran A merinci formulasi matematis dari empat varian pembobotan yang digunakan dalam fungsi biaya WCVaR. Varian pertama adalah pembobotan standar CVaR (A1) yang memberikan bobot seragam kepada seluruh sampel yang masuk dalam fraksi $\alpha$ terbaik. Varian kedua adalah pembobotan berbasis energi (A2) yang mengadopsi prinsip hukum Boltzmann di mana bobot ditentukan secara eksponensial berdasarkan nilai energi absolut relatif terhadap energi minimum. Meskipun terinspirasi secara fisik, varian ini ditemukan kurang efektif karena sensitivitasnya terhadap fluktuasi nilai energi selama iterasi.

Varian ketiga menggunakan pendekatan berbasis peringkat (*Rank-based*, A3), di mana bobot meluruh secara eksponensial murni berdasarkan urutan peringkat sampel tanpa bergantung pada nilai energi absolut. Pendekatan ini dinilai lebih stabil dan efektif dibandingkan metode berbasis energi. Varian terakhir adalah pembobotan *Piecewise Exponential* (A4) yang membagi distribusi sampel menjadi tiga zona dengan tingkat peluruhan yang berbeda untuk memberikan kontrol yang lebih granular terhadap sensitivitas fungsi biaya. Meskipun varian A4 memberikan hasil terbaik, varian A3 diakui sebagai alternatif yang kompetitif karena kesederhanaan parameternya. Secara keseluruhan, pemaparan dalam lampiran ini melengkapi pemahaman teknis mengenai optimalisasi portofolio menggunakan algoritma VQE yang diintegrasikan dengan strategi pembobotan dinamis.