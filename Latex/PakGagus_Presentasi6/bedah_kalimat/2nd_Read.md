# I. INTRODUCTION
## Paragraf 1 (kalimat ke:)
1. finance $\to$ derivative $\to$ jenisnya
> Penulis mengawali pengantar dengan mendefinisikan instrumen derivatif secara luas, menghubungkan nilainya dengan aset dasar untuk menetapkan fondasi kontekstual bagi pembaca.
2. jenis khusus 
> Penulis melakukan spesifikasi pada derivatif suku bunga sebagai fokus utama, membatasi ruang lingkup pembahasan sejak awal paragraf.
3. tujuan dari derivatif
> Penulis memaparkan utilitas praktis derivatif dalam manajemen risiko (*hedging*) dan spekulasi untuk memperkuat relevansi instrumen tersebut di pasar keuangan global.
4. masuk ke pemodelan matematis
> Penulis membangun jembatan logis dengan menekankan bahwa akurasi dalam memodelkan evolusi waktu suku bunga adalah prasyarat mutlak untuk penetapan harga (*pricing*) yang valid.
5. jenis model
> Penulis melakukan klasifikasi taksonomis terhadap pendekatan stokastik dalam literatur, membedakan antara variabel *spot rate* (jangka pendek) dan *forward rate* (jangka panjang).
6. model simpel
> Penulis memberikan latar belakang historis mengenai penggunaan faktor *noisy* (acak) tunggal atau ganda dalam pemodelan awal sebagai titik awal evolusi teori.
7. spesifik model
> Penulis mengidentifikasi model-model klasik (seperti Vasicek, Hull-White, dan CIR) sebagai standar industri saat ini untuk menunjukkan kemapanan literatur di bidang ini.
8. kekurangan model (1)
> Penulis mengakui kemudahan implementasi algoritma model tersebut, namun segera diikuti dengan kalimat transisi untuk menunjukkan keterbatasan performanya.
9. kekurangan model (2)
> Penulis memberikan kritik tajam terhadap kegagalan model klasik dalam melakukan kalibrasi data pasar secara simultan dengan penangkapan struktur korelasi antar variabel.
10. contoh model bagus
> Penulis memperkenalkan kerangka kerja *Heath-Jarrow-Morton* (HJM) sebagai solusi superior yang mampu mengatasi kendala-kendala struktural pada model sebelumnya.
11. definisi 1
> Penulis menegaskan otoritas model HJM sebagai *general family* yang mampu menggeneralisasi dan menurunkan model-model lain yang telah disebutkan sebelumnya.
12. definisi 2
> Penulis mengarahkan pembaca pada referensi teknis (Appendix A) untuk menjaga fokus pendahuluan tetap pada narasi motivasi penelitian tanpa kehilangan kedalaman informasi.
13. definisi 3
> Penulis mereduksi kompleksitas model HJM ke dalam satu parameter kunci, yaitu faktor volatilitas, yang nantinya menjadi target utama algoritma kuantum.
14. kekurangan 
> Penulis mengekspos tantangan fundamental berupa *trade-off* antara presisi model (jumlah faktor *noisy*) dan efisiensi waktu eksekusi pada infrastruktur komputasi klasik.
15. kekurangan
> Penulis menarik kesimpulan deduktif bahwa limitasi daya komputasi saat ini secara langsung membatasi akurasi dan skalabilitas model keuangan yang kompleks.
16. quantum computer sebagai solusi
> Penulis mengajukan komputasi kuantum sebagai paradigma baru (*paradigm shift*) yang mampu menembus hambatan kapasitas yang dihadapi komputer klasik.
17. lanjut solusi
> Penulis memproyeksikan keunggulan kapasitas komputasi kuantum untuk meningkatkan fidelitas model HJM, yang menjadi tesis utama dan motivasi dari keseluruhan artikel ini.

| Kalimat | Pertanyaan                                               | Jawaban                                                                                                |
| :------ | :------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| 1       | Apa entitas fundamental yang sedang dibahas?             | Derivatif sebagai kontrak yang nilainya diturunkan dari aset dasar.                                    |
| 2       | Apa saja instrumen derivatif yang umum?                  | Forwards, futures, swaps, caps, floors, swaptions, dan lain-lain.                                      |
| 3       | Apa utilitas ekonomi dari instrumen tersebut?            | Manajemen risiko (*hedging*) atau spekulasi murni.                                                     |
| 4       | Apa prasyarat utama dalam penetapan harga (*pricing*)?   | Pemodelan akurat terhadap evolusi waktu dari suku bunga.                                               |
| 5       | Pendekatan stokastik apa yang tersedia dalam literatur?  | Pemodelan *instantaneous spot rate* atau *forward rate*.                                               |
| 6       | Bagaimana kompleksitas awal model yang diusulkan?        | Dinamika sederhana berbasis satu atau dua faktor *noisy* (acak).                                       |
| 7       | Apa saja contoh model klasik yang mapan?                 | Vasicek, Hull-White, Cox-Ingersoll-Ross (CIR), dan Gaussian-Vasicek.                                   |
| 8       | Sejauh mana kemudahan implementasi model tersebut?       | Algoritma yang digunakan bersifat *straightforward* (langsung) untuk diimplementasikan.                |
| 9       | Apa batasan utama dari model-model klasik tersebut?      | Kegagalan dalam kalibrasi data pasar sekaligus menangkap struktur korelasi antar maturitas.            |
| 10      | Adakah kerangka kerja yang mampu mengatasi batasan itu?  | Kerangka kerja *Heath-Jarrow-Morton* (HJM) yang memodelkan *forward rate* secara langsung.             |
| 11      | Bagaimana posisi HJM dalam taksonomi model finansial?    | HJM adalah *general family* (induk) di mana model-model lain dapat diturunkan darinya.                 |
| 12      | Di mana pembaca dapat memahami detail model ini?         | Penulis merujuk pada **Appendix A** untuk penjelasan teoretis yang lebih mendalam.                     |
| 13      | Apa parameter kunci yang mengendalikan dinamika HJM?     | Seluruh dinamika ditentukan secara eksklusif oleh faktor-faktor volatilitas.                           |
| 14      | Apa tantangan operasional dalam simulasi model HJM?      | Adanya *trade-off* antara jumlah faktor *noisy* dan waktu komputasi yang dibutuhkan.                   |
| 15      | Apa faktor penghambat utama bagi akurasi model?          | Limitasi daya komputasi klasik membatasi jumlah faktor yang bisa diolah secara presisi.                |
| 16      | Instrumen apa yang diajukan untuk menembus limitasi ini? | Komputer kuantum (*Quantum Computer*) sebagai alat bantu komputasi baru.                               |
| 17      | Mengapa komputer kuantum menjadi solusi yang valid?      | Kapasitas komputasinya jauh melebihi sistem klasik untuk meningkatkan fidelitas dan akurasi model HJM. |

## Paragraf 2
1. kontribusi QC
> Penulis memberikan konteks historis mengenai kemunculan komputasi kuantum sebagai teknologi disruptif yang menjanjikan revolusi pada kapasitas pemrosesan data.
2. enttanglement dan keunggulannya
> Penulis menyoroti fenomena *entanglement* sebagai sumber daya kuantum unik yang memungkinkan paralelisasi komputasi, memberikan pembenaran teoretis atas potensi *speedup*.
3. lanjutan
> Penulis menyajikan bukti empiris berupa daftar algoritma kuantum yang telah terbukti lebih unggul dibanding algoritma klasik untuk membangun kredibilitas solusi kuantum.
4. quantum simulasi sebagai aplikasi qc
> Penulis mengerucutkan pembahasan pada aplikasi *quantum simulation*, menjelaskan rasionalitas penggunaannya untuk sistem yang tidak efisien jika disimulasikan secara klasik.
5. conth qs
> Penulis menyajikan spektrum aplikasi simulasi kuantum di berbagai disiplin ilmu (fisika, kimia, biologi) untuk menunjukkan versatilitas dan kematangan bidang tersebut.
6. paper ccotnoh qs
> Penulis melakukan tinjauan literatur spesifik pada domain keuangan, mengakui adanya potensi besar namun mencatat minimnya implementasi eksperimental sebagai celah riset (*research gap*).
7. batasan qs
> Penulis secara jujur memaparkan keterbatasan teknologi saat ini (*small noisy chips*) untuk memberikan batasan masalah yang realistis dan memperkuat urgensi penelitian pada model yang efisien.

| Kalimat | Pertanyaan                       | Jawaban                                                                        |
| :------ | :----------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa kontribusi historis QC?                | Muncul sebagai teknologi revolusioner untuk daya komputasi masif.                             |
| 2       | Apa peran *entanglement* dalam QC?         | Sebagai sumber daya ekstra untuk mempercepat kinerja melalui paralelisasi.                    |
| 3       | Algoritma apa saja yang memiliki *speedup*? | Faktorisasi prima, pencarian daftar, sistem linear, dan pencarian *eigenvalue*.               |
| 4       | Apa aplikasi kuantum yang paling relevan?  | Simulasi kuantum (QS) untuk sistem yang tidak efisien jika diolah secara klasik.              |
| 5       | Apa saja contoh aplikasi QS?               | Sistem spin, kimia kuantum, teori medan kuantum, hingga dinamika fluida.                      |
| 6       | Bagaimana status aplikasi QC di finansial? | Sudah banyak diusulkan secara teoritis, namun eksperimen riil masih sangat terbatas.         |
| 7       | Apa hambatan teknologi saat ini?           | Teknologi terkini hanya menyediakan chip kuantum kecil dan berderau (*noisy*).                |

## Paragraf 3
1. pengenalan artkel yang menggunakan qpca dan tujuannya
> Penulis memperkenalkan algoritma *quantum Principal Component Analysis* (qPCA) sebagai kontribusi utama artikel ini untuk mereduksi kompleksitas model HJM secara efektif.
2. cara implementasi algoritmanya ke 5 qubit IBMQX2
> Penulis memberikan rincian teknis implementasi pada perangkat keras spesifik (IBMQX2 5-qubit) untuk menunjukkan validitas eksperimental dari metode yang diusulkan.
3. faktor volatilitas dengan persamaan eigen
> Penulis menghubungkan parameter fisik (volatilitas) dengan representasi matematis (eigenvalue/eigenvector) untuk menetapkan operator target dalam algoritma kuantum.
4. ilustrasi algoritma qpca dengan matriks kovarians
> Penulis menjelaskan metodologi estimasi komponen utama melalui matriks kovarians yang didasarkan pada data historis, menjembatani teori kuantum dengan realitas data finansial.
5. penegasan qc dan qpca bekerja di platform kuantum
> Penulis menegaskan bahwa solusi yang diajukan bersifat universal untuk platform kuantum berbasis sirkuit superkonduktor, namun tetap dapat diuji pada sistem yang tersedia saat ini.
6. jawaban dari: kalau klasik bisa, kenapa harus kuantum 
> Penulis memberikan justifikasi atas urgensi penggunaan qPCA sebagai langkah kritis dalam membangun algoritma *Quantum Monte Carlo* yang efisien dan layak jalan (*feasible*).
7. strategi aplikasi qc di era NISQ
> Penulis memposisikan penelitian ini dalam era NISQ, menekankan modifikasi algoritma agar adaptif terhadap keterbatasan koherensi prosesor kuantum masa kini.

| Kalimat | Pertanyaan                            | Jawaban                                                                         |
| :------ | :---------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| 1       | Apa solusi yang ditawarkan artikel ini?         | Algoritma qPCA yang efisien untuk mereduksi faktor *noisy* pada model HJM.                     |
| 2       | Di mana algoritma ini diimplementasikan?        | Pada prosesor kuantum IBMQX2 5-qubit karena aksesibilitasnya yang mudah.                       |
| 3       | Bagaimana parameter finansial direpresentasikan? | Faktor volatilitas diestimasi melalui *eigenvalue* dan *eigenvector* matriks kovarians.        |
| 4       | Data apa yang digunakan dalam eksperimen?       | Matriks korelasi silang berbasis data historis suku bunga 1, 3, dan 6 bulan.                   |
| 5       | Apakah algoritma ini bersifat universal?        | Ya, merupakan implementasi umum yang dapat dijalankan pada prosesor kuantum berbasis sirkuit.   |
| 6       | Mengapa reduksi faktor itu krusial?             | Untuk meminimalkan jumlah gerbang kuantum dalam konstruksi algoritma *Quantum Monte Carlo*.    |
| 7       | Bagaimana strategi menghadapi limitasi hardware? | Menggunakan algoritma yang dimodifikasi agar lebih adaptif terhadap waktu dekoherensi prosesor. |

## Paragraf 4
1. definisi teknika pca
> Penulis mendefinisikan *Principal Component Analysis* (PCA) sebagai teknik matematis fundamental untuk mencari aproksimasi matriks *low-rank* yang optimal.
2. advantae pca
> Penulis menjelaskan mekanisme eliminasi *eigenvalue* terkecil untuk menunjukkan bagaimana PCA mempertahankan informasi krusial sambil mereduksi dimensi data.
3. pentingany apca
> Penulis menekankan signifikansi PCA dalam identifikasi pola pada data berdimensi tinggi, memperkuat relevansinya dalam analisis data kompleks.
4. disadvantage pca
> Penulis mengidentifikasi hambatan utama berupa biaya komputasi yang melonjak tinggi seiring bertambahnya ukuran matriks pada sistem klasik.
5. disadvantage pca dalam konteks qc
> Penulis membangun argumen bahwa algoritma kuantum menawarkan solusi melalui *exponential speedup*, yang menjadi kunci efisiensi dalam pengolahan matriks besar.
6. contoh di referensi 
> Penulis merujuk pada literatur kunci (Ref [14]) yang menyediakan landasan algoritma qPCA untuk memperkuat fondasi teoretis metodologi yang digunakan.
7. penjelasan author referensi
> Penulis menjelaskan asumsi bahwa matriks dapat direpresentasikan sebagai *quantum state*, yang menjadi prasyarat teknis bagi penerapan qPCA dalam konteks keuangan.

| Kalimat | Pertanyaan                          | Jawaban                                                                        |
| :------ | :-------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa definisi teknik PCA?                      | Teknik matematika untuk mencari aproksimasi matriks *low-rank* yang optimal.                  |
| 2       | Bagaimana mekanisme reduksi dimensinya?       | Dengan mengabaikan *eigenvalue* terkecil dan mempertahankan komponen spektral utama.          |
| 3       | Mengapa PCA sangat penting?                   | Relevan untuk berbagai aplikasi, mulai dari reduksi dimensi hingga pencarian pola data besar. |
| 4       | Apa kendala PCA pada sistem klasik?           | Biaya komputasi menjadi sangat tinggi ketika ukuran matriks meningkat secara signifikan.      |
| 5       | Bagaimana peran QC dalam optimasi PCA?        | Algoritma kuantum menawarkan *speedup* eksponensial untuk melakukan PCA.                      |
| 6       | Referensi mana yang menjadi landasan?         | Algoritma elegan dari Lloyd et al. (Ref [14]) untuk melakukan PCA kuantum.                    |
| 7       | Apa asumsi teknis yang harus dipenuhi?        | Matriks harus dapat direpresentasikan sebagai *quantum state* (matriks non-negatif, *trace*=1).|

## Paragraf 5
1. cerita eksplorasi teknik qpca di artikel ini
> Penulis menguraikan eksplorasi teknik qPCA untuk mereduksi dimensi model HJM tanpa mengorbankan akurasi simulasi.
2. kecocokan qpca dengan masalah finansial
> Penulis memberikan rasionalitas mengapa qPCA sangat cocok untuk masalah finansial ini, terutama karena kesesuaian struktur matriks korelasi dengan representasi *density matrices*.
3. hasil eksplorasi (?)
> Penulis menekankan bahwa reduksi jumlah faktor volatilitas merupakan langkah krusial untuk meminimalkan jumlah gerbang kuantum, sehingga mengurangi dampak dekoherensi.

| Kalimat | Pertanyaan                            | Jawaban                                                                       |
| :------ | :---------------------------------------------- | :------------------------------------------------------------------------------------------- |
| 1       | Apa fokus eksplorasi qPCA dalam artikel ini?    | Merencanakan reduksi dimensi model HJM tanpa mengorbankan akurasi simulasi.                  |
| 2       | Mengapa qPCA sangat cocok untuk masalah finansial?| Karena input berupa matriks korelasi identik dengan karakteristik *density matrices*.        |
| 3       | Apa dampak teknis dari keberhasilan reduksi ini?| Pengurangan jumlah gerbang sirkuit yang krusial untuk mengatasi limitasi waktu dekoherensi.  |

## Paragraf 6
1. info modifikasi
> Penulis menginformasikan adanya modifikasi pada algoritma standar agar lebih kompatibel dengan keterbatasan prosesor kuantum di era NISQ.
2. advantage
> Penulis menonjolkan keunggulan algoritma yang dimodifikasi dalam menangani chip yang kecil dan berderau (*noisy*).
3. klaim
> Penulis mengklaim posisi penelitian ini sebagai eksperimen komputasi kuantum pertama dalam penetapan harga opsi finansial sekaligus implementasi qPCA terbesar saat ini.
4. lanjutan
> Penulis menutup pendahuluan dengan visi strategis bahwa kontribusi ini merupakan langkah penting menuju keunggulan kuantum (*quantum advantage*) dalam menyelesaikan masalah finansial skala besar.

| Kalimat | Pertanyaan                           | Jawaban                                                                        |
| :------ | :--------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana karakteristik algoritma yang diuji?   | Menggunakan versi modifikasi yang lebih adaptif untuk chip kuantum kecil dan berderau.       |
| 2       | Apa signifikansi dari kontribusi ini?          | Merupakan langkah awal menuju simulasi penuh model HJM pada komputer kuantum IBM.             |
| 3       | Apa klaim kebaruan (*novelty*) penelitian ini? | Eksperimen komputasi kuantum pertama dalam *option pricing* dan implementasi qPCA terbesar.   |
| 4       | Apa visi jangka panjang yang ingin dicapai?    | Membuka jalan bagi pencapaian *quantum supremacy* atau *advantage* di bidang keuangan.        |

---
# II. QUANTUM CIRCUIT
## Paragraf 1
1. model consideration
> Penulis menetapkan batasan teoretis dengan mempertimbangkan matriks non-negatif $\sigma_N$ dengan *trace* satu sebagai objek komputasi utama.
2. asumsi unitary bisa digenerate
> Penulis mengasumsikan efisiensi dalam membangkitkan operator uniter $e^{it\sigma_N}$, yang merupakan prasyarat teknis bagi implementasi algoritma.
3. bukti dari referensi
> Penulis memperkuat asumsi tersebut dengan merujuk pada literatur (Ref [14, 38, 39]) yang membuktikan kelayakan pembangkitan uniter di bawah kondisi tertentu.
4. kasus paper
> Penulis mengidentifikasi bahwa meskipun matriks kovarians tidak bersifat jarang (*sparse*), akses ke beberapa salinan *quantum state* memungkinkan implementasi yang efisien.
5. best way to generate ...
> Penulis memilih metode yang diusulkan oleh Lloyd et al. sebagai pendekatan paling efisien dengan akurasi yang terkendali untuk membangkitkan operasi uniter.
6. advantage the way for spectral decomposition
> Penulis menjelaskan bahwa metode ini secara intrinsik mengakomodasi dekomposisi spektral matriks, yang krusial untuk ekstraksi *eigenvalue*.
7. tujuan algoritma
> Penulis menegaskan tujuan utama algoritma adalah penentuan sejumlah $r$ *eigenvalue* terbesar beserta *eigenvector* terkaitnya.
8. ilustrasi gate decomposition
> Penulis merujuk pada Gambar 1 untuk memberikan visualisasi konkret mengenai dekomposisi gerbang kuantum yang diperlukan.
9. state: a priori about eigenvectors
> Penulis mengakui ketidaktahuan awal (*a priori*) mengenai *eigenvector*, sehingga penggunaan *quantum phase estimation* (QPE) secara langsung tidak dimungkinkan.
10. kejujuran batas
> Penulis secara transparan menyatakan keterbatasan dalam menghitung *eigenvalue* secara langsung tanpa pengetahuan basis eigen yang memadai.
11. konsekuensi dari batas
> Penulis menjelaskan bahwa sistem harus diinisialisasi pada *random state* sebagai konsekuensi logis dari keterbatasan informasi awal tersebut.
12. jika random vector 
> Penulis memberikan dasar probabilitas bahwa vektor acak hampir pasti memiliki komponen non-nol dalam basis eigen yang sedang dicari.
13. quantum fourier transform and application
> Penulis mendeskripsikan peran *Quantum Fourier Transform* dalam menciptakan keterpautan (*entanglement*) antara estimasi *eigenvalue* dan *eigenvector*.
14. pengenalan $\Lambda_j^{(n)}$ 
> Penulis memperkenalkan notasi $\Lambda_j^{(n)}$ sebagai representasi biner $n$-bit dari *eigenvalue* ke-$j$ untuk menjamin presisi komputasi.
15. jika aproksimasinya bagus, ...
> Penulis merumuskan kondisi di mana komponen *eigenvalue* tertinggi akan mendominasi hasil proyeksi, memungkinkan isolasi *eigenvector* utama.
16. pengenalan $\ket{y^{(n)}}$ dan maknanya
> Penulis mendefinisikan vektor proyeksi $\ket{y^{(n)}}$ sebagai instrumen operasional untuk mengekstraksi *eigenvector* dari superposisi kuantum.
17. klain
> Penulis mengklaim bahwa melalui proyeksi pada komponen *eigenvalue* tertentu, *eigenvector* yang sesuai dapat diperoleh dengan fidelitas yang dapat dipertanggungjawabkan.
18. kondisi di kasus paper
> Penulis mencatat tantangan pada chip NISQ di mana presisi bit yang rendah dapat menyebabkan ambiguitas identifikasi antara dua atau lebih *eigenvector*.
19. menggunakan random state karena a priori (gak tau)
> Penulis menjelaskan penggunaan berbagai *random state* untuk memverifikasi apakah *eigenvector* utama telah berhasil diidentifikasi secara konsisten.
20. expected state for identified eigenvector
> Penulis mendeskripsikan *state* yang diharapkan muncul jika identifikasi berhasil, yang berfungsi sebagai indikator empiris bagi konvergensi algoritma.
21. kalo gak, dinaikin lagi bitnya
> Penulis memberikan solusi heuristik berupa peningkatan presisi bit ($n$-bit) jika *eigenvector* unik belum dapat ditentukan secara pasti.

| Kalimat | Pertanyaan                                     | Jawaban                                                                                 |
| :------ | :------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| 1       | Apa batasan teoretis matriks input?                      | Matriks non-negatif $\sigma_N$ dengan $tr[\sigma_N] = 1$ (representasi *state* kuantum).               |
| 2       | Apa prasyarat utama implementasi sirkuit?                | Kemampuan membangkitkan operator uniter $e^{it\sigma_N}$ secara efisien.                               |
| 3       | Adakah bukti teoretis kelayakan pembangkitan uniter?     | Ya, didukung oleh literatur untuk matriks *sparse* atau melalui akses banyak salinan *state*.          |
| 4       | Bagaimana kondisi matriks kovarians dalam paper ini?     | Tidak *sparse*, namun tetap efisien karena dikodifikasi langsung dalam *state* kuantum.                |
| 5       | Metode mana yang paling optimal untuk sirkuit ini?       | Metode Lloyd et al. (Ref [14]) dengan akurasi yang terkendali.                                         |
| 6       | Apa keunggulan intrinsik metode tersebut?                | Secara alami mengakomodasi dekomposisi spektral matriks untuk ekstraksi eigen.                         |
| 7       | Apa target kuantitatif dari algoritma ini?               | Menentukan sejumlah $r$ *eigenvalue* terbesar beserta *eigenvector* terkaitnya.                        |
| 8       | Di mana visualisasi dekomposisi gerbang dapat dilihat?   | Gambar 1 menyajikan implementasi sirkuit kuantum untuk $n + \log N$ qubit.                             |
| 9       | Mengapa QPE standar tidak bisa langsung digunakan?       | Karena *eigenvector* tidak diketahui sebelumnya (*a priori*).                                          |
| 10      | Apa kendala dalam menghitung nilai eigen secara langsung?| Ketidaktahuan basis eigen menghambat penggunaan estimasi fase kuantum tradisional.                     |
| 11      | Bagaimana inisialisasi sistem dilakukan?                 | Sistem diinisialisasi pada *random state* $\ket{b}$ sebagai titik awal pencarian.                      |
| 12      | Mengapa *random state* dianggap memadai?                 | Secara probabilistik, vektor acak hampir pasti memiliki proyeksi pada basis eigen target.              |
| 13      | Apa peran QFT dalam protokol ini?                        | Menciptakan keterpautan (*entanglement*) antara estimasi nilai eigen dan *eigenvector*.                |
| 14      | Bagaimana presisi nilai eigen didefinisikan?             | Melalui notasi biner $n$-bit $\Lambda_j^{(n)}$.                                                        |
| 15      | Apa indikator keberhasilan aproksimasi?                  | Dominasi komponen nilai eigen tertinggi dalam hasil proyeksi *state*.                                  |
| 16      | Bagaimana cara mengekstraksi *eigenvector* target?       | Melalui proyeksi *state* $\ket{\psi_b}$ pada komponen nilai eigen $\ket{y^{(n)}}$.                     |
| 17      | Sejauh mana fidelitas hasil proyeksi ini?                | Hasil proyeksi $\ket{y^{(n)}} \otimes \mathbb{I} \ket{\psi_b}$ mendekati *eigenvector* eksak.           |
| 18      | Apa tantangan khusus pada era NISQ?                      | Presisi bit yang rendah dapat menyebabkan kegagalan dalam membedakan antar *eigenvector*.              |
| 19      | Bagaimana cara memverifikasi konsistensi hasil?          | Mencoba berbagai *random state* $\ket{c}$ dan membandingkan hasil proyeksinya.                         |
| 20      | Apa yang terjadi jika identifikasi berhasil?             | Sistem akan menunjukkan superposisi yang stabil pada *eigenvector* yang sesuai.                        |
| 21      | Apa solusi jika terjadi ambiguitas identifikasi?         | Meningkatkan jumlah bit presisi ($n$-bit) hingga nilai eigen unik teridentifikasi.                     |

## Paragraf 2
1. asumsi n-bit cukup untuk determine eigenvector
> Penulis memulai fase perbaikan dengan asumsi bahwa presisi $n$-bit sudah memadai untuk memisahkan *eigenvector* yang unik dari ruang Hilbert.
2. implementasi constraint
> Penulis mempertimbangkan kendala fisik perangkat keras (jumlah qubit dan tingkat derau) sebagai faktor pembatas utama dalam peningkatan kualitas hasil.
3. mulai protokol
> Penulis merinci langkah awal protokol iteratif yang dimulai dari *random state* $\ket{b_0}$ untuk kemudian diproyeksikan ke ruang bagian *eigenvalue*.
4. hasilnya $\ket{\psi_{b_0}}$ sehingga aproksimasi eigenvector
> Penulis mendefinisikan hasil iterasi pertama sebagai pendekatan awal yang akan menjadi dasar bagi proses penyempurnaan pada tahap selanjutnya.
5. $\ket{\psi_{b_1}}$ sebagai eror cancellation ...?
> Penulis menjelaskan bahwa penggunaan hasil proyeksi sebelumnya sebagai *initial state* baru bertujuan untuk meningkatkan fidelitas melalui mekanisme pembatalan kesalahan koheren.
6. klaim limitasi
> Penulis secara kritis mengakui adanya batas fundamental dalam perbaikan fidelitas yang disebabkan oleh dekoherensi qubit dan kesalahan statistik pada tahap pengukuran.
7. disclaimer tentang perbedaan hasil di beberapa kasus
> Penulis menyarankan teknik pengukuran pada berbagai basis dan pengambilan rata-rata sebagai strategi mitigasi untuk mereduksi kesalahan sistematis dari gerbang kuantum.

| Kalimat | Pertanyaan                             | Jawaban                                                                         |
| :------ | :----------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| 1       | Kapan proses perbaikan sekuensial dimulai?       | Saat presisi $n$-bit dianggap cukup untuk memisahkan *eigenvector* yang unik.                  |
| 2       | Faktor apa yang membatasi perbaikan ini?         | Keterbatasan jumlah qubit, derau pada chip, dan kesalahan operasional sirkuit.                 |
| 3       | Bagaimana langkah awal protokol iteratif?         | Memulai dengan $\ket{b_0}$, menerapkan sirkuit berderau, dan memproyeksikan ke ruang $\ket{y^{(n)}}$.|
| 4       | Apa hasil dari iterasi pertama?                  | Diperoleh $\ket{b_1}$ sebagai aproksimasi awal *eigenvector*.                                  |
| 5       | Mengapa hasil sebelumnya digunakan kembali?      | Untuk meningkatkan fidelitas melalui mekanisme pembatalan kesalahan koheren (*cancellation*).  |
| 6       | Di mana letak batas penyempurnaan fidelitas?     | Pada titik dekoherensi qubit dan kesalahan statistik hasil pengukuran.                         |
| 7       | Bagaimana cara mereduksi kesalahan sistematis?   | Melakukan pengukuran pada berbagai basis berbeda dan mengambil nilai rata-ratanya.             |

---
# III. RESULT
## Paragraf 1
1. 2 bagian protokol
> Penulis mendefinisikan arsitektur protokol yang terbagi menjadi dua fase utama untuk mencapai solusi spektral yang komprehensif.
2. 1: estimasi eigenvector $\ket{u_{max}}$ berdasarkan eigenvalue terbesar $\lambda_{max}$
> Penulis menetapkan estimasi *eigenvector* utama sebagai prioritas pertama, yang didasarkan pada besaran *eigenvalue* maksimum.
3. random $\to$ sirkuit fig.2 $\to$ proyeksi n-bit $\ket{y_{max}^{(n)}}$ $\to$ gunakan state tersebut sebagai initial state $\to$ secara bertahap mendekati exact eigenvector 
> Penulis merinci alur kerja algoritma yang bersifat evolusioner, mulai dari inisialisasi acak hingga konvergensi menuju *eigenvector* eksak melalui proyeksi iteratif.
4. eigenvector digunakan untuk dapat eigenvalue lebih akurang (QPE)
> Penulis menjelaskan kegunaan *eigenvector* yang telah dioptimalkan sebagai masukan bagi QPE untuk mengekstraksi *eigenvalue* dengan presisi tinggi.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana struktur protokol yang diusulkan?         | Protokol dibagi menjadi dua bagian utama: estimasi eigenvector dan perbaikan eigenvalue.         |
| 2       | Apa fokus utama pada bagian pertama protokol?       | Mengestimasi eigenvector $\ket{u_{max}}$ yang berkorespondensi dengan eigenvalue terbesar $\lambda_{max}$. |
| 3       | Bagaimana mekanisme iterasi menuju eigenvector eksak?| Dimulai dari state acak, melalui sirkuit Fig. 2, proyeksi $n$-bit, dan penggunaan hasil sebagai state awal baru. |
| 4       | Apa fungsi eigenvector yang telah diestimasi tersebut?| Sebagai state inisial untuk algoritma QPE guna mendapatkan presisi eigenvalue yang lebih tinggi. |

## Paragraf 2 (estimasi eigenvector)
1. mulai dari random state $\ket{b_0}$
> Penulis memulai prosedur eksperimental dengan menetapkan *random state* $\ket{b_0}$ sebagai titik awal stokastik.
2. initial state $\ket{0} \otimes \ket{0} \otimes \ket{b_0}$
> Penulis mendefinisikan struktur *initial state* sistem yang melibatkan qubit tambahan untuk pengkodean biner *eigenvalue*.
3. estimasi pertama $\ket{b_1}$ dan gunakan sebagai initial state untuk iterasi selanjutnya
> Penulis memperkenalkan strategi umpan balik (*feedback*) di mana hasil estimasi tiap iterasi digunakan untuk memperkaya kualitas *initial state* berikutnya.
4. $\ket{0} \otimes \ket{0} \otimes \ket{b_1}$
> Penulis mengonfirmasi penerapan sirkuit pada *state* $\ket{b_1}$ untuk memvalidasi peningkatan fidelitas secara bertahap.
5. lanjutkan iterasi sampai k kali sampai $\ket{b_{k-1}} \approx \ket{b_k}$ 
> Penulis menetapkan kriteria penghentian (*stopping criterion*) berdasarkan stabilitas vektor antara dua iterasi yang berurutan.
6. setelah dapat, bisa klaim $\ket{b_k} \approx \ket{u_{max}}$
> Penulis merumuskan klaim bahwa konvergensi pada iterasi ke-$k$ merepresentasikan aproksimasi terbaik bagi *eigenvector* utama.

| Kalimat | Pertanyaan                         | Jawaban                                                              |
| :------ | :------------------------------------------- | :---------------------------------------------------------------------------------- |
| 1       | Apa titik awal dari proses estimasi eigenvector? | Dimulai dengan state kuantum acak $\ket{b_0}$.                                      |
| 2       | Bagaimana konfigurasi state inisial sistem?  | State inisial berupa $\ket{0} \otimes \ket{0} \otimes \ket{b_0}$ pada register qubit. |
| 3       | Bagaimana proses peningkatan fidelitas dilakukan?| Hasil estimasi $\ket{b_1}$ digunakan kembali sebagai state inisial untuk iterasi berikutnya. |
| 4       | Apa langkah selanjutnya setelah mendapatkan $\ket{b_1}$?| Menjalankan sirkuit pada state $\ket{0} \otimes \ket{0} \otimes \ket{b_1}$ secara berulang. |
| 5       | Kapan proses iterasi ini dinyatakan selesai? | Dilakukan $k$ kali hingga tercapai stabilitas $\ket{b_{k-1}} \approx \ket{b_k}$.     |
| 6       | Apa simpulan akhir dari fase iteratif ini?   | State $\ket{b_k}$ diklaim sebagai aproksimasi terbaik untuk $\ket{u_{max}}$.         |

## Paragraf 3
1. mulai cari eigenvalue $\lambda_{max}$
> Penulis beralih pada target kedua, yaitu pencarian nilai numerik *eigenvalue* $\lambda_{max}$ setelah basis eigen ditemukan.
2. gunakan qpe [10] setelah $\ket{u_{max}}$ didapat untuk dapat $\lambda_{max}$ dengan presisi n-bit
> Penulis mengintegrasikan algoritma QPE standar sebagai metode validasi untuk mendapatkan presisi $n$-bit pada nilai eigen.
3. limit bergantung prosesor
> Penulis secara pragmatis mencatat bahwa batas presisi komputasi sangat bergantung pada kapasitas fisik prosesor kuantum yang digunakan.
4. target ...
> Penulis menetapkan target evaluasi pada matriks korelasi finansial untuk menguji performa algoritma dalam skenario dunia nyata.
5. solve 2x2 submatrix dari $\sigma_3$ baru solve 4x4 expansion
> Penulis menerapkan strategi *bottom-up* dengan menyelesaikan sub-matriks 2x2 sebelum melakukan ekspansi ke kasus 4x4 yang lebih kompleks.
6. klaim
> Penulis memberikan klaim atas keberhasilan implementasi algoritma pada platform IBMQX2.
7. laporan
> Penulis menyampaikan laporan awal mengenai konsistensi hasil antara simulator dan perangkat keras kuantum riil.

| Kalimat | Pertanyaan                         | Jawaban                                                              |
| :------ | :------------------------------------------- | :---------------------------------------------------------------------------------- |
| 1       | Apa target setelah estimasi eigenvector selesai? | Melakukan estimasi nilai numerik eigenvalue $\lambda_{max}$ secara akurat.          |
| 2       | Algoritma apa yang digunakan untuk tugas ini? | Mengaplikasikan algoritma QPE dengan presisi $n$-bit.                               |
| 3       | Apa faktor pembatas presisi dalam estimasi ini?| Ukuran prosesor kuantum yang digunakan membatasi jumlah bit presisi yang dicapai.   |
| 4       | Apa objek uji utama dalam eksperimen ini?    | Matriks kovarians $3 \times 3$ yang mewakili volatilitas instrumen finansial.       |
| 5       | Bagaimana urutan penyelesaian masalahnya?    | Menyelesaikan sub-matriks $2 \times 2$ terlebih dahulu sebelum beralih ke ekspansi $4 \times 4$. |
| 6       | Di platform mana eksperimen ini dijalankan?  | Pada simulator QISKIT dan prosesor kuantum riil dari IBM.                           |
| 7       | Bagaimana kualitas hasil yang diperoleh?     | Kedua platform memberikan hasil yang akurat dan konsisten.                          |

## Paragraf 4
1. normalisasi dengan trace dengan spectral decomposition
> Penulis melakukan normalisasi matriks kovarians terhadap *trace*-nya untuk memastikan representasi yang sesuai dalam formalisme *density matrix*.
2. $\lambda_{max} \gg \lambda_2$ (karakteristik matriks korelasi) gunakan pca untuk mencari $\rho_2$
> Penulis mengidentifikasi dominasi *eigenvalue* utama ($\lambda_{max} \gg \lambda_2$) sebagai fitur intrinsik matriks korelasi yang memungkinkan efektivitas teknik PCA.
3. definisi unitary
> Penulis mendefinisikan operator uniter yang akan diimplementasikan dalam sirkuit kuantum berdasarkan dekomposisi spektral tersebut.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana mempersiapkan matriks kovarians untuk sirkuit? | Melakukan normalisasi terhadap trace agar sesuai dengan formalisme density matrix.               |
| 2       | Mengapa teknik PCA relevan pada matriks korelasi ini? | Karena eigenvalue utama jauh lebih besar dari yang kedua ($\lambda_{max} \gg \lambda_2$).        |
| 3       | Bagaimana operator uniter didefinisikan?             | Berdasarkan dekomposisi spektral dari matriks yang telah dinormalisasi.                          |

## Paragraf 5
1. gunakan 3 qubit: 2 qubit pertama untuk aprokismasi 2-bit dan qubit ke-3 untuk representasi eigenvector 
> Penulis merinci alokasi tiga qubit, di mana dua qubit berfungsi sebagai register *eigenvalue* dan satu qubit sebagai representasi *eigenvector*.
2. laksanakan bagian pertama protokol
> Penulis melaksanakan fase pertama protokol secara sistematis sesuai dengan desain yang telah dijelaskan sebelumnya.
3. setelah iterasi 4, outcome vector mengukur eigenvector stabil
> Penulis menyajikan temuan bahwa setelah iterasi keempat, vektor hasil pengukuran mencapai titik stabil, menandai konvergensi algoritma.
4. ukur dengan basis rotasi
> Penulis menerapkan rotasi basis pengukuran untuk mengekstraksi informasi fase kompleks yang tidak terlihat pada basis standar.
5. pemilihan sudut selama $\theta \ne 0$
> Penulis memberikan syarat teknis pada pemilihan sudut rotasi guna menghindari hilangnya informasi pada titik-titik singular.
6. nunjukin $\ket{u_{max}}, \delta,$ dan report IBM
> Penulis menyajikan laporan komparatif antara hasil eksperimen IBM dengan nilai teoretis, termasuk besaran kesalahan $\delta$.
7. definisi $\delta$ dan fungsinya
> Penulis mendefinisikan parameter $\delta$ sebagai metrik ketidakpastian yang mencakup berbagai sumber kesalahan sistematis.
8. pengakuan batas akses ke IBM
> Penulis memberikan pengakuan jujur mengenai keterbatasan akses langsung ke parameter internal prosesor IBM.
9. appendix B untuk jelasin $\delta$ 
> Penulis mengarahkan pembaca ke Appendix B untuk penjelasan mendalam mengenai metodologi estimasi kesalahan.
10. remark splitting $\mathbb{C}$ phase dan global phase 
> Penulis memberikan catatan teknis mengenai pemisahan fase global dan fase kompleks untuk menjaga integritas interpretasi data.
11. tabel 1
> Penulis merujuk pada Tabel I untuk menyajikan evolusi koefisien *eigenvector* selama proses iterasi.
12. hasil ovservasi tentang konvergensi
> Penulis mendiskusikan hasil observasi mengenai kecepatan konvergensi yang signifikan sejak iterasi awal.
13. hasil eigenvector - ukur x,y, dan r-random direction sampai dapat state $\ket{b_x}, \ket{b_y}, \text{dan} \space \ket{b_r}$  
> Penulis melaporkan hasil pengukuran *eigenvector* akhir pada berbagai arah acak untuk menjamin validitas statistik.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana alokasi qubit pada prosesor?              | 3 qubit digunakan: 2 untuk estimasi eigenvalue (2-bit) dan 1 untuk eigenvector.                  |
| 2       | Langkah apa yang pertama kali dilakukan?            | Menjalankan fase pertama protokol (estimasi eigenvector) secara sistematis.                      |
| 3       | Kapan pengamatan terhadap stabilitas dilakukan?     | Setelah iterasi ke-4, di mana vektor hasil pengukuran mulai menunjukkan stabilitas.              |
| 4       | Mengapa dilakukan rotasi basis pengukuran?          | Untuk mendapatkan informasi fase kompleks yang tidak terbaca pada basis standar.                 |
| 5       | Apa kriteria pemilihan sudut rotasi?                | Sudut dipilih sedemikian rupa sehingga $\theta \ne 0$ untuk menghindari singularitas.            |
| 6       | Data apa yang dilaporkan dari hasil IBM?            | Nilai estimasi $\ket{u_{max}}$ beserta parameter kesalahan $\delta$.                             |
| 7       | Apa fungsi dari parameter $\delta$?                 | Sebagai metrik ketidakpastian yang mencakup berbagai sumber kesalahan sistematis.                |
| 8       | Bagaimana akses penulis terhadap prosesor IBM?      | Terbatas, sehingga tidak dapat membedakan sumber kesalahan secara spesifik.                      |
| 9       | Di mana detail perhitungan $\delta$ dijelaskan?     | Pada Appendix B untuk metodologi estimasi kesalahan yang lebih mendalam.                         |
| 10      | Bagaimana pemisahan fase dilakukan?                 | Melalui pemisahan antara fase kompleks dan fase global untuk menjaga integritas data.            |
| 11      | Di mana ringkasan koefisien dapat dilihat?          | Pada Tabel I, yang menunjukkan evolusi koefisien setelah setiap iterasi.                         |
| 12      | Apa temuan utama mengenai kecepatan konvergensi?    | Algoritma sudah menunjukkan tanda konvergensi yang signifikan sejak iterasi pertama.             |
| 13      | Bagaimana validitas statistik eigenvector dipastikan?| Melalui pengukuran pada arah x, y, dan r acak untuk mendapatkan state yang konsisten.            |

## Paragraf 6
1. remark bahwa hasil estimasi eigenvactor didapat dari proeksi ke sbspace ke 2-bit string $\Lambda_{max} = 0.11$
> Penulis memberikan penekanan bahwa hasil estimasi awal diperoleh melalui proyeksi pada ruang bagian dengan presisi string 2-bit.
2. qpe sebagai improve estimasi eigenvalue
> Penulis memposisikan QPE sebagai alat untuk meningkatkan presisi numerik nilai eigen setelah *eigenvector* berhasil diisolasi.
3. bagi masalah jadi 2 stage dengan 2 alasan
> Penulis memberikan rasionalitas di balik pembagian protokol menjadi dua tahap untuk mengoptimalkan penggunaan sumber daya kuantum.
4. alasan 1: gak tau a priori
> Penulis menjelaskan alasan pertama terkait ketidaktahuan awal akan nilai eigen yang membutuhkan pencarian heuristik terlebih dahulu.
5. alasan 2: author observe saat jalanin protokol
> Penulis mengungkapkan alasan kedua berdasarkan observasi empiris selama jalannya protokol mengenai akumulasi kesalahan gerbang.
6. masih gak yakin
> Penulis mempertahankan sikap skeptis yang sehat terhadap hasil mentah tanpa mitigasi kesalahan lebih lanjut.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana hasil estimasi eigenvector diperoleh?     | Melalui proyeksi pada ruang bagian dengan estimasi eigenvalue string 2-bit.                      |
| 2       | Apa langkah selanjutnya untuk meningkatkan akurasi? | Menerapkan algoritma QPE untuk mendapatkan estimasi nilai eigen yang lebih presisi.              |
| 3       | Mengapa masalah dibagi menjadi dua tahap?           | Berdasarkan dua alasan strategis: ketidaktahuan awal dan efisiensi hardware.                     |
| 4       | Apa alasan pertama pembagian tahap tersebut?        | Ketidaktahuan nilai eigen secara *a priori* yang memerlukan pencarian heuristik terlebih dahulu. |
| 5       | Apa alasan kedua berdasarkan pengalaman eksperimen? | Observasi akumulasi kesalahan gerbang yang meningkat jika dijalankan sekaligus.                  |
| 6       | Bagaimana tingkat kepercayaan terhadap hasil mentah? | Penulis tetap berhati-hati karena keterbatasan transparansi sirkuit internal IBM.                |

## Paragraf 7
1. 3 qubit untuk estimasi eigenvalue $\Lambda_{max} = 0, b_1, b_2, b_3$ 
> Penulis meningkatkan resolusi estimasi nilai eigen menjadi 3-bit untuk mengevaluasi batas kemampuan hardware saat ini.
2. depth yang nambah semakin muncul dekoherensi sebagaimana fig.3
> Penulis melaporkan munculnya fenomena dekoherensi yang signifikan seiring bertambahnya kedalaman sirkuit, sebagaimana ditunjukkan pada Gambar 3.
3. hasil qiskit simulator dengan laporannya 
> Penulis membandingkan hasil simulator Qiskit dengan data eksperimental untuk menyoroti dampak derau pada sistem riil.
4. perbandingan dengan prediksi 
> Penulis menyajikan analisis komparatif dengan prediksi teoretis untuk mengukur tingkat deviasi hasil eksperimen.
5. klaim kesimpulan
> Penulis menarik kesimpulan mengenai potensi peningkatan hasil melalui perbaikan kualitas gerbang dan chip di masa depan.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana konfigurasi untuk estimasi eigenvalue 3-bit? | Menggunakan 3 qubit untuk mengevaluasi batas kemampuan hardware IBM.                             |
| 2       | Apa dampak dari penambahan kedalaman sirkuit?       | Munculnya dekoherensi yang signifikan, sebagaimana divisualisasikan pada Gambar 3.               |
| 3       | Apa kegunaan hasil simulator Qiskit dalam hal ini?  | Sebagai standar pembanding untuk menyoroti tingkat derau pada perangkat keras riil.              |
| 4       | Bagaimana tingkat deviasi hasil eksperimen?         | Penulis membandingkan data eksperimental dengan prediksi teoretis untuk mengukur akurasi.        |
| 5       | Apa prospek perbaikan hasil di masa depan?          | Bergantung pada peningkatan fidelitas gerbang dan kualitas chip kuantum yang akan datang.        |

## Paragraf 8
1. kasus matrix 4x4
> Penulis meningkatkan kompleksitas masalah dengan menguji algoritma pada matriks 4x4, yang merepresentasikan skenario keuangan yang lebih luas.
2. bentuk uniternya
> Penulis mendefinisikan konstruksi operator uniter yang lebih kompleks untuk mengakomodasi dimensi ruang Hilbert yang lebih tinggi.
3. spectral decomposition
> Penulis mencatat bahwa dekomposisi spektral pada tingkat ini merupakan tantangan komputasi yang lebih berat.
4. tingkat masalah lebih tinggi dari sebelumnya
> Penulis mengakui adanya lonjakan kesulitan teknis saat beralih dari sistem 2x2 ke 4x4.
5. harus dekomposisi jadi gerbang 2 qubit sehingga nurunin depth dan dekoherensi
> Penulis mengusulkan strategi dekomposisi gerbang menjadi interaksi dua-qubit untuk menekan kedalaman sirkuit dan memitigasi dekoherensi.
6. sirkuitnya di fig. 4
> Penulis merujuk pada Gambar 4 untuk mengilustrasikan sirkuit kuantum yang telah dioptimalkan untuk kasus 4x4.
7. mulai dengan $\ket{b_0} = (\ket{00} + \ket{01} +\ket{10} + \ket{11})/2$ ... tabel 2 sebagai koefisien basis 8 
> Penulis mendeskripsikan inisialisasi pada *state* superposisi merata sebagai titik awal pencarian eigen pada ruang 4-dimensi.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Mengapa penulis beralih ke matriks $4 \times 4$?    | Untuk menguji skalabilitas algoritma pada skenario finansial yang lebih kompleks.                |
| 2       | Bagaimana konstruksi uniter disesuaikan?            | Didesain untuk mengakomodasi dimensi ruang Hilbert yang lebih tinggi (4-dimensi).                |
| 3       | Apa tantangan utama dalam dekomposisi spektral?     | Kompleksitas perhitungan yang meningkat drastis dibandingkan kasus $2 \times 2$.                 |
| 4       | Seberapa besar peningkatan tingkat kesulitan ini?   | Signifikan, karena melibatkan lebih banyak parameter dan ketergantungan antar qubit.             |
| 5       | Bagaimana cara menekan dampak dekoherensi?          | Melalui dekomposisi sirkuit menjadi interaksi dua-qubit guna mereduksi kedalaman (*depth*).      |
| 6       | Di mana desain sirkuit $4 \times 4$ dapat dipelajari?| Gambar 4 menyajikan representasi gerbang kuantum yang telah dioptimalkan untuk kasus ini.        |
| 7       | Bagaimana penyiapan state awal untuk matriks $4 \times 4$?| Menggunakan superposisi merata sebagai state awal $\ket{b_0}$, dengan koefisien pada Tabel II.   |

## Paragraf 9
1. nyoba basis lain lalu ambil rata-rata erornya
> Penulis melakukan eksperimen pada berbagai basis tambahan dan melaporkan rata-rata kesalahan untuk menjamin objektivitas data.
2. nunjukin estimasi eigenvector
> Penulis menyajikan hasil estimasi *eigenvector* untuk kasus 4x4, meskipun menghadapi tantangan teknis yang berat.
3. hasil yang tidak berani apa-apa dan alasannya
> Penulis mengakui ketidakmampuan algoritma dalam memberikan hasil yang konklusif pada konfigurasi hardware saat ini akibat akumulasi eror yang masif.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Bagaimana objektivitas data eksperimen dijamin?     | Dengan menguji hasil pada berbagai basis berbeda dan menghitung rata-rata kesalahannya.          |
| 2       | Apa temuan mengenai estimasi eigenvector $4 \times 4$?| Hasil estimasi tetap disajikan meskipun integritas datanya terancam oleh derau sirkuit.          |
| 3       | Mengapa hasil kasus $4 \times 4$ dianggap tidak konklusif?| Karena akumulasi kesalahan sirkuit pada hardware riil sudah melampaui ambang batas toleransi.    |

## Paragraf 10
1. mitigasi eror sebagaimana pada referensi 
> Penulis memperkenalkan teknik mitigasi kesalahan berdasarkan referensi terkini untuk menyelamatkan integritas data eksperimental.
2. laporan hasil mitigasi
> Penulis melaporkan efektivitas langkah-langkah mitigasi dalam memperbaiki hasil akhir komputasi.
3. ricahrdson's extrapolation for eror mitigation
> Penulis merinci penggunaan metode *Richardson's extrapolation* sebagai alat matematis untuk mengeliminasi gangguan derau.
4. readout eror mitigation sebagai tambahan eror cancellation
> Penulis menambahkan teknik *readout error mitigation* sebagai lapisan pelindung tambahan terhadap kesalahan pada tahap pengukuran.

| Kalimat | Pertanyaan                                | Jawaban                                                                           |
| :------ | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| 1       | Apa langkah terakhir untuk memperbaiki data?        | Menerapkan teknik mitigasi kesalahan berdasarkan referensi literatur terbaru (Ref [41]).         |
| 2       | Bagaimana dampak mitigasi terhadap hasil akhir?     | Mitigasi berhasil memperbaiki profil data meskipun hardware memiliki keterbatasan fisik.          |
| 3       | Teknik ekstrapolasi apa yang digunakan?             | *Richardson's extrapolation* untuk mengeliminasi kontribusi derau secara matematis.              |
| 4       | Apa lapisan mitigasi tambahan yang diterapkan?      | *Readout error mitigation* untuk mereduksi kesalahan spesifik pada tahap pengukuran.             |

---
# IV. CONCULUSIONS

## Paragraf 1
1. yang telah dilakukan: efficient quantum algorithm to reduce number of noisy...
> Penulis merangkum pencapaian utama berupa implementasi algoritma kuantum efisien untuk mereduksi faktor *noisy* pada komputer NISQ.
2. klami 1
> Penulis mengklaim efektivitas metode dalam menangani sistem finansial kompleks dengan sumber daya terbatas.
3. klaim 2
> Penulis menegaskan skalabilitas algoritma sebagai solusi potensial bagi masalah dimensi tinggi di masa depan.
4. kejujuran (kejutan) dalam kalkulasi
> Penulis memberikan catatan kritis mengenai tantangan teknis yang ditemui selama fase eksperimental.
5. metodologi
> Penulis menjustifikasi metodologi hibrida klasik-kuantum yang digunakan sebagai pendekatan paling layak saat ini.
6. hasil 1
> Penulis menyoroti hasil estimasi *eigenvector* pada kasus 2x2 sebagai bukti keberhasilan konsep (*proof of concept*).
7. hasil 2
> Penulis melaporkan akurasi estimasi *eigenvalue* yang kompetitif dibandingkan metode klasik.
8. hasil 3
> Penulis menyajikan temuan mengenai batasan hardware pada kasus 4x4 sebagai arahan bagi riset selanjutnya.
9. membuka kemungkinan lain
> Penulis membuka ruang bagi eksplorasi teknik mitigasi kesalahan yang lebih canggih.
10. klaim 3
> Penulis menarik kesimpulan optimis bahwa aplikasi praktis kuantum di bidang keuangan semakin mendekati realitas.
11. alasan klaim 3
> Penulis memperkuat klaimnya dengan mengacu pada tren perkembangan teknologi hardware kuantum saat ini.
12. klaim 4
> Penulis menutup dengan pernyataan mengenai signifikansi riset ini sebagai pionir di bidang *quantum finance*.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa pencapaian teknis utama penelitian ini?         | Implementasi algoritma kuantum efisien untuk mereduksi faktor *noisy* pada model HJM.         |
| 2       | Bagaimana efektivitas metode yang diusulkan?        | Sangat efektif dalam menangani masalah finansial kompleks dengan sumber daya terbatas.        |
| 3       | Apakah algoritma ini dapat diskalakan?              | Ya, diklaim memiliki skalabilitas untuk masalah berdimensi lebih tinggi di masa depan.        |
| 4       | Adakah kendala tak terduga yang ditemui?            | Penulis secara transparan mencatat tantangan teknis selama fase eksperimen.                   |
| 5       | Bagaimana justifikasi pemilihan metode hibrida?     | Sebagai pendekatan paling pragmatis dan layak jalan untuk hardware kuantum saat ini.          |
| 6       | Apa bukti empiris keberhasilan pada sistem kecil?   | Hasil estimasi *eigenvector* pada matriks $2 \times 2$ yang akurat.                           |
| 7       | Bagaimana performa estimasi nilai eigennya?         | Memberikan hasil yang kompetitif dan akurat dibandingkan dengan metode klasik.                |
| 8       | Apa pelajaran dari kegagalan pada sistem 4x4?        | Mengidentifikasi batas kemampuan hardware saat ini sebagai panduan riset masa depan.           |
| 9       | Apakah ada potensi pengembangan lebih lanjut?       | Membuka peluang bagi integrasi teknik mitigasi kesalahan yang lebih canggih.                 |
| 10      | Apa dampak riset ini bagi industri keuangan?        | Menunjukkan bahwa aplikasi praktis komputer kuantum di keuangan sudah di ambang pintu.        |
| 11      | Apa dasar dari optimisme penulis?                   | Tren perkembangan teknologi hardware kuantum yang sangat pesat.                                |
| 12      | Apa status akhir dari kontribusi riset ini?         | Sebagai karya pionir yang menetapkan standar baru dalam bidang *quantum finance*.             |

## Paragraf 2
1. info terkait Github repository
> Penulis memberikan transparansi riset dengan menyediakan akses publik ke repositori kode untuk replikasi dan pengembangan lebih lanjut.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana akses terhadap sumber daya riset ini?     | Melalui repositori GitHub publik untuk menjamin transparansi dan replikabilitas.              |

---
# APPENDIX A

# Paragraf 1
1. tantangan pemodelan matematika dalam emnghitung fair price
> Penulis menguraikan kompleksitas matematis dalam penentuan harga wajar instrumen derivatif.
2. black scholes sebagai model analitik sederhana
> Penulis menempatkan model Black-Scholes sebagai titik acuan historis sekaligus menunjukkan keterbatasannya.
3. batasan dari model tradisional
> Penulis mengkritik asumsi simplistik model tradisional yang gagal menangkap dinamika pasar yang heterogen.
4. HJM sebagai solusi
> Penulis mengajukan kerangka HJM sebagai paradigma modern yang lebih representatif terhadap faktor risiko.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Mengapa perhitungan harga derivatif itu sulit?      | Karena melibatkan tantangan pemodelan matematis yang sangat kompleks.                         |
| 2       | Apa peran model Black-Scholes dalam konteks ini?    | Sebagai alat analitik sederhana namun memiliki fitur yang sangat terbatas.                     |
| 3       | Apa kelemahan utama model-model tradisional?        | Tidak mampu menangkap seluruh faktor risiko finansial yang relevan secara akurat.             |
| 4       | Mengapa kerangka HJM mulai diminati?                | Karena mampu mengatasi keterbatasan model tradisional dalam skenario yang lebih rumit.        |

# Paragraf 2
1. kebutuhan komputasi tangguh untuk ...
> Penulis menekankan kebutuhan akan daya komputasi masif untuk menyelesaikan model multifaktor.
2. pengenalan teknik paling populer: monte carlo dan alasannya
> Penulis mengidentifikasi simulasi Monte Carlo sebagai metode dominan sekaligus menyoroti inefisiensinya.
3. cara desain efisien MC: 2 stages: 1. kurangi koplesitasi domputasi (sorting dimensi) 2. meningkatkan konvergensi MC dari model tereduksi
> Penulis merinci strategi optimasi dua tahap: reduksi dimensi diikuti dengan percepatan konvergensi.
4. qc merupakan alternatif untuk memiliki 2 stage
> Penulis memposisikan QC sebagai teknologi kunci yang mampu mengakselerasi kedua tahap optimasi tersebut.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Seberapa besar beban komputasi model multifaktor?   | Sangat berat, memerlukan sumber daya komputasi yang tangguh.                                  |
| 2       | Apa metode simulasi yang paling umum digunakan?     | Simulasi Monte Carlo, meskipun memiliki laju konvergensi yang rendah.                         |
| 3       | Bagaimana cara merancang simulasi MC yang efisien?  | Melalui dua tahap: reduksi kompleksitas (PCA) dan akselerasi konvergensi.                     |
| 4       | Bagaimana peran komputasi kuantum dalam hal ini?    | Menjadi alternatif utama untuk mempercepat eksekusi kedua tahap optimasi tersebut.            |

# Paragraf 3
1. fungsi $P(t,T)$ sebagai fungsi harga di waktu t
> Penulis mendefinisikan fungsi harga obligasi $P(t,T)$ sebagai variabel fundamental dalam teori suku bunga.
2. maka $P(T,T) = 1$
> Penulis menetapkan kondisi batas pada saat jatuh tempo untuk menjamin konsistensi model.
3. kurva ini nyambung ke elemen fundamental pada teori risk-neutral derivative
> Penulis menghubungkan kurva harga obligasi dengan prinsip *risk-neutral pricing*.
4. fungsi $P(t,T)$ adalah kurva faktor diskon dan alasannya
> Penulis menjelaskan peran kurva diskon dalam valuasi arus kas masa depan.
5. sedangkan inversnya adalah faktor kapitalisasi.
> Penulis memperkenalkan faktor kapitalisasi sebagai representasi nilai waktu dari uang.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa definisi formal dari obligasi nol kupon?        | Kontrak yang menjamin pembayaran satu unit mata uang pada waktu jatuh tempo $T$.              |
| 2       | Apa nilai obligasi pada saat jatuh tempo?           | Nilainya harus sama dengan satu ($P(T,T) = 1$).                                               |
| 3       | Mengapa variabel ini sangat penting dalam teori?    | Karena merupakan elemen fundamental dalam penetapan harga derivatif *risk-neutral*.           |
| 4       | Apa interpretasi ekonomi dari $P(t,T)$?              | Sebagai kurva faktor diskon untuk menghitung nilai sekarang dari arus kas masa depan.         |
| 5       | Apa lawan kata dari faktor diskon?                  | Faktor kapitalisasi, yang memberikan nilai masa depan dari kuantitas saat ini.                |

# Paragraf 4
1. definisi interest rate
> Penulis memberikan definisi formal mengenai suku bunga sesaat (*short rate*).
2. penggunaan $r_t$ 
> Penulis menggunakan notasi $r_t$ untuk membedakan suku bunga variabel dari parameter deterministik.
3. persamaan $B(t)$ sebagai nilai money market
> Penulis merumuskan persamaan akun pasar uang $B(t)$ sebagai instrumen akumulasi nilai tanpa risiko.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa yang dimaksud dengan suku bunga sesaat?         | Tingkat pengembalian investasi bebas risiko pada periode waktu yang infinitesimal.            |
| 2       | Bagaimana variabel ini diamati di pasar?            | Sebagai nilai yang diketahui saat ini, namun tidak pasti untuk masa depan.                    |
| 3       | Bagaimana akumulasi nilai di pasar uang dihitung?   | Melalui fungsi eksponensial integral dari suku bunga sesaat terhadap waktu.                   |

# Paragraf 5
1. pengamatan pada waktu t (sederhana)
> Penulis membedakan antara observasi pasar saat ini yang bersifat deterministik dan prediksi masa depan.
2. pengamatan pada waktu T (butuh model)
> Penulis menekankan sifat stokastik dari suku bunga masa depan yang memerlukan pemodelan probabilistik.
3. persamaan $P(t,T)$ pada framework risk-neutral berdasarkan $B(t)$
> Penulis menyajikan formula penetapan harga obligasi dalam kerangka *risk-neutral* berbasis $B(t)$.
4. klaim $P(t,T)$ adalah deterministik
> Penulis menegaskan status harga obligasi saat ini sebagai data input yang diketahui.
5. tapi pada kasus asli, $t_f$ adlaah random variables
> Penulis mengidentifikasi variabel acak pada waktu jatuh tempo sebagai sumber utama risiko harga.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana kepastian suku bunga pada waktu $t$?      | Bersifat deterministik karena dapat diobservasi langsung di pasar uang.                       |
| 2       | Mengapa suku bunga masa depan dianggap tidak pasti? | Karena harus dimodelkan sebagai proses stokastik akibat ketidakpastian pasar.                 |
| 3       | Bagaimana hubungan harga obligasi dengan akun pasar uang?| Melalui formula ekspektasi di bawah ukuran martingal ekuivalen $Q_B$.                         |
| 4       | Apakah harga obligasi saat ini bersifat acak?       | Tidak, harga obligasi saat ini ($P(t,T)$) adalah nilai deterministik.                         |
| 5       | Di mana letak ketidakpastian dalam model ini?      | Pada nilai suku bunga masa depan yang merupakan variabel acak.                                |

# Paragraf 6
1. pengelana model untuk short rate yang bergantung faktor noisy
> Penulis mengklasifikasikan model suku bunga berdasarkan jumlah faktor gangguan (*noise factors*).
2. nyebutin model-model short rate
> Penulis menyebutkan model-model terkemuka (Vasicek, dsb.) sebagai landasan teoretis.
3. sifata dari model-model
> Penulis membedah karakteristik dan keterbatasan operasional dari model satu faktor.
4. masuk ke multifactor models dan tujuannya
> Penulis memperkenalkan model multifaktor untuk menangkap korelasi antar berbagai maturitas.
5. nyebutin conttoh two-factor models
> Penulis memberikan contoh model dua faktor yang populer dalam literatur keuangan.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana model *short rate* diklasifikasikan?      | Berdasarkan jumlah faktor gangguan (*noisy factors*) yang mendefinisikan dinamikanya.          |
| 2       | Apa saja contoh model satu faktor yang populer?     | Model Vasicek, Hull-White, dan Cox-Ingersoll-Ross (CIR).                                      |
| 3       | Mengapa model satu faktor mulai ditinggalkan?       | Karena keterbatasannya dalam merepresentasikan distribusi gabungan suku bunga antar maturitas. |
| 4       | Apa tujuan penggunaan model multifaktor?            | Untuk memperkaya struktur korelasi dalam pemodelan suku bunga.                                |
| 5       | Sebutkan contoh model dua faktor yang dikenal.      | Model Gaussian-Vasicek dan model Hull-White dua faktor.                                       |

# Paragraf 7
1. battasan yang dialami usaha paragraf sebelumnya (kalbrasi) multifactor models ke forward rates
> Penulis mengevaluasi keterbatasan model multifaktor tradisional dalam proses kalibrasi terhadap kurva pasar.
2. mengenalkan HJM untuk modeling forward rate
> Penulis memperkenalkan kerangka kerja HJM sebagai solusi sistematis untuk memodelkan *forward rates*.
3. jelasin cara umum yang dilakukan oleh HJM: keunggulan dan trade-off nya
> Penulis mendiskusikan keunggulan metodologi HJM serta tantangan komputasi (*trade-off*) yang menyertainya.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa batasan utama model multifaktor tradisional?    | Kesulitan dalam kalibrasi terhadap kurva diskon pasar saat ini.                               |
| 2       | Apa solusi yang ditawarkan kerangka HJM?            | Memungkinkan pemodelan suku bunga masa depan (*forward rates*) secara langsung.               |
| 3       | Bagaimana prinsip kerja HJM dalam prakteknya?       | Menentukan dinamika melalui faktor volatilitas, dengan *trade-off* pada beban komputasi.      |

# Paragraf 8
1. tunjukin hubungan $f(t,T)$ terhadap $P(t,T)$
> Penulis merumuskan hubungan matematis antara *forward rate* $f(t,T)$ dan harga obligasi $P(t,T)$.
2. bentuk $P(t,T)$ nya. 
> Penulis menyajikan bentuk integral dari harga obligasi sebagai fungsi dari dinamika suku bunga masa depan.
3. persamaan turunan parsial $P(t,T)$ terhadap T
> Penulis menurunkan persamaan diferensial parsial untuk menggambarkan evolusi harga obligasi terhadap waktu maturitas.
4. persamaan lengkap dan formulasi umum
> Penulis memberikan formulasi umum yang mencakup seluruh spektrum *forward rates*.
5. masuk ke persamaan model HJM menggunakan brownian increment ($\sigma_i$)
> Penulis mengintegrasikan faktor *Brownian motion* dalam model HJM untuk menangkap fluktuasi acak pasar.
6. implementasikan dinamika harga obligasi
> Penulis merumuskan dinamika harga obligasi secara lengkap dalam kerangka stokastik.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana hubungan *forward rate* dengan harga obligasi? | Melalui turunan parsial negatif dari logaritma harga obligasi terhadap maturitas.             |
| 2       | Bagaimana formulasi harga obligasi dalam HJM?       | Sebagai fungsi eksponensial negatif dari integral *forward rate*.                              |
| 3       | Apa hasil diferensiasi harga terhadap maturitas?    | Mendapatkan hubungan antara perubahan harga dan struktur suku bunga sesaat.                  |
| 4       | Bagaimana hubungan ini diinterpretasikan secara luas?| Sebagai dasar untuk menentukan harga derivatif suku bunga secara *risk-neutral*.              |
| 5       | Bagaimana dinamika suku bunga dimodelkan?           | Melalui persamaan diferensial stokastik dengan komponen *drift* dan *volatility*.             |
| 6       | Bagaimana dinamika harga obligasi diturunkan?       | Dengan menerapkan Lemma Ito pada fungsi harga obligasi dalam kerangka HJM.                    |

# Paragraf 9
1. mengenalkan $\alpha(t,T)$ sebagai pencegah arbitrase
> Penulis mendefinisikan parameter *drift* $\alpha(t,T)$ sebagai mekanisme teknis untuk mencegah peluang arbitrase.
2. penegasan penggunaan $\sigma$
> Penulis menegaskan peran krusial koefisien volatilitas $\sigma$ dalam menentukan arah pergerakan harga.
3. pernyataan kritis yang matahin (dengan kekurangan)
> Penulis menyajikan kritik mendalam mengenai keterbatasan model HJM dalam konteks komputasi.
4. nambahin kritik
> Penulis menambahkan observasi kritis mengenai sifat *non-Markovian* yang meningkatkan beban memori sistem.
5. kembali ke dasar dari kekurangan (markovianity)
> Penulis mengidentifikasi akar permasalahan pada dependensi jalur (*path dependency*) yang kompleks.
6. ajuan yang bisa dilakukan ($\bar{\sigma}_i$)
> Penulis mengajukan penggunaan rata-rata volatilitas $\bar{\sigma}_i$ sebagai strategi simplifikasi.
7. metodologi untuk realisasiin solusi
> Penulis menjelaskan metodologi numerik untuk merealisasikan solusi yang diusulkan.
8. hasil matriks dari solusi dan representasinya
> Penulis menyajikan representasi matriks dari solusi tersebut untuk memudahkan implementasi algoritma.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa fungsi dari koefisien *drift* $\alpha$?         | Untuk menjamin kondisi bebas arbitrase dalam model.                                           |
| 2       | Faktor apa yang paling menentukan dinamika HJM?     | Koefisien volatilitas $\sigma$ adalah satu-satunya parameter yang perlu ditentukan.           |
| 3       | Apa masalah utama dalam implementasi HJM?           | Sifat model yang sering kali bersifat *non-Markovian* (tergantung pada lintasan masa lalu).    |
| 4       | Mengapa sifat *non-Markovian* menjadi hambatan?     | Karena membutuhkan penyimpanan data historis yang masif, meningkatkan biaya komputasi.        |
| 5       | Bagaimana cara membuat model menjadi *Markovian*?   | Dengan memilih struktur volatilitas tertentu yang memisahkan variabel waktu dan maturitas.    |
| 6       | Strategi apa yang diusulkan untuk simplifikasi?    | Mengasumsikan volatilitas hanya bergantung pada waktu menuju maturitas ($\tau = T-t$).       |
| 7       | Bagaimana data historis diolah?                     | Dengan membangun matriks kovarians dari perubahan *forward rates* pada berbagai maturitas.    |
| 8       | Apa output akhir dari pengolahan data tersebut?     | Matriks simetrik di mana elemen diagonalnya adalah variansi dari *rates*.                     |

# Paragraf 10
1. mahanya computatinoal cost
> Penulis mengakui biaya komputasi yang sangat tinggi dalam pengolahan data berdimensi besar.
2. klamin bisa dapat eigenvector dari eigenvalue dengan pca
> Penulis membuktikan kelayakan ekstraksi *eigenvector* melalui teknik PCA untuk efisiensi data.
3. kurva evaluasi di beberapa literatur: bisa dicari
> Penulis merujuk pada kurva evaluasi literatur untuk memvalidasi pola pergerakan suku bunga.
4. kasus khusus kalau semua principal component pertama sama, maka kurva pergerakannya jadi parallel shift
> Penulis menjelaskan fenomena *parallel shift* pada kurva suku bunga sebagai dampak dari komponen utama pertama.
5. begitu pula untuk  yang kedua; kurvanya akan berbeda
> Penulis mendeskripsikan variasi bentuk kurva (*twist*) yang dihasilkan oleh komponen utama kedua.
6. bentuk persamaan eigen dengan faktor volatility untuk 2x2 dan 3x3 cross-correlation matrix
> Penulis menyajikan persamaan eigen lengkap untuk matriks korelasi silang pada berbagai dimensi.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Mengapa simulasi numerik HJM sangat mahal?          | Karena melibatkan banyak faktor maturitas yang meningkatkan dimensi masalah secara drastis.   |
| 2       | Bagaimana cara mereduksi dimensi tersebut?          | Menggunakan PCA untuk mendapatkan eigenvector relevan yang mewakili dinamika utama.           |
| 3       | Faktor apa yang paling mendominasi kurva suku bunga?| Sebagian besar evolusi kurva dapat dijelaskan hanya oleh dua atau tiga komponen utama.        |
| 4       | Apa interpretasi dari komponen utama pertama?       | Mewakili pergerakan sejajar (*parallel shift*) dari seluruh kurva maturitas.                  |
| 5       | Apa interpretasi dari komponen utama kedua?         | Mewakili perubahan kemiringan atau pelintiran (*twist*) pada kurva.                           |
| 6       | Bagaimana volatilitas akhir dihitung?               | Melalui perkalian akar nilai eigen dengan komponen *eigenvector*-nya.                         |

---
# APPENDIX B
## Paragraf 1
1. $\delta$ sebagai batas atas semua kemungkinan eror (pengantar)
> Penulis mendefinisikan $\delta$ sebagai parameter batas atas (*upper bound*) untuk mencakup seluruh spektrum kesalahan sistematis.
2. kondisi/kesulitan dalam membedakan eror
> Penulis mengakui kesulitan teknis dalam memisahkan kontribusi kesalahan individu pada sistem yang berderau.
3. pernyataan umum paragraf induktif
> Penulis menggunakan logika induktif untuk merumuskan estimasi kesalahan total dari observasi parsial.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa itu parameter $\delta$?                         | Batas atas (*upper bound*) dari akumulasi seluruh kesalahan eksperimental.                    |
| 2       | Mengapa sulit menentukan sumber kesalahan?          | Karena adanya percampuran antara derau gerbang, kesalahan pengukuran, dan limitasi sistem.    |
| 3       | Bagaimana strategi estimasi dalam kondisi ini?      | Mengasumsikan skenario terburuk di mana seluruh kesalahan dijumlahkan secara linear.          |

## Paragraf 2
1. langkah pertaman untuk 2x2: compute fidelity
> Penulis menetapkan pengukuran fidelitas pada kasus 2x2 sebagai langkah kalibrasi dasar.
2. estimate eror per gerbang 2 qubit
> Penulis melakukan estimasi kesalahan spesifik untuk setiap interaksi gerbang dua-qubit.
3. cara cari total eror $\delta$ dan eror pergate
> Penulis merumuskan hubungan antara kesalahan per gerbang dan akumulasi kesalahan total $\delta$.
4. cara untuk matiks 4x4
> Penulis melakukan ekstrapolasi metodologi tersebut untuk memprediksi perilaku kesalahan pada sistem 4x4.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana kalibrasi kesalahan dimulai?              | Dengan menghitung fidelitas sirkuit pada matriks kovarians $2 \times 2$.                      |
| 2       | Bagaimana kesalahan per gerbang diestimasi?         | Berdasarkan deviasi hasil eksperimen terhadap nilai teoretis ideal.                           |
| 3       | Apa hubungan kesalahan per gerbang dengan $\delta$? | $\delta$ dihitung dengan mengalikan kesalahan per gerbang dengan jumlah gerbang dalam sirkuit. |
| 4       | Bagaimana estimasi untuk kasus yang lebih besar?    | Dengan memproyeksikan akumulasi kesalahan berdasarkan jumlah gerbang pada sirkuit $4 \times 4$.|

---
# APPENDIX C

## Paragraf 1
1. bagian pertama sirkuti
> Penulis mendeskripsikan fase pertama sirkuit yang difokuskan pada isolasi ruang bagian eigen.
2. cara yang dilakukan di bagian pertama
> Penulis menjelaskan prosedur iteratif yang digunakan untuk menyaring informasi *eigenvector*.
3. hasil di tabel III
> Penulis menyajikan data kuantitatif pada Tabel III untuk menunjukkan progres konvergensi.
4. kondisi stopnya iterasi
> Penulis menetapkan kriteria stabilitas sebagai kondisi untuk menghentikan proses iterasi.

| Kalimat | Pertanyaan                             | Jawaban                                                                |
| :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------ |
| 1       | Apa fokus utama bagian pertama sirkuit?          | Menggunakan dua qubit untuk mendapatkan estimasi 2-bit dari nilai eigen tertinggi.    |
| 2       | Bagaimana prosedur operasionalnya?               | Melakukan inisialisasi pada state $+\rangle$ dan memproyeksikan ke state $11\rangle$. |
| 3       | Di mana hasil detail tiap iterasi dapat dilihat? | Tabel III menyajikan data statistik (counts) untuk setiap iterasi eksperimen.         |
| 4       | Kapan penulis memutuskan untuk berhenti?         | Setelah iterasi keempat, saat vektor hasil pengukuran sudah mencapai titik stabil.    |

## Paragraf 2
1. rogasi pengukuran basis x, y, dan r arbiter untuk imrove akurasi
> Penulis merinci penggunaan rotasi basis pengukuran (x, y, r) untuk meningkatkan resolusi data fase.
2. tabel IV nunjukin outcomenya
> Penulis menyajikan hasil observasi pada Tabel IV sebagai bukti peningkatan akurasi estimasi.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana akurasi hasil akhir ditingkatkan?         | Dengan melakukan rotasi basis pengukuran pada sumbu x, y, dan arah sembarang r.               |
| 2       | Bagaimana sebaran datanya?                          | Tabel IV merinci hasil counts dan persentase untuk setiap variasi rotasi basis.               |

## Paragraf 3
1. eigenvaector yang didapat
> Penulis melaporkan nilai akhir *eigenvector* yang berhasil diestimasi melalui protokol tersebut.
2. eigenvaluen yang didapat
> Penulis menyajikan nilai *eigenvalue* terkait sebagai hasil validasi spektral.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa hasil estimasi eigenvector akhirnya?            | Disajikan dalam persamaan (C1) dengan menyertakan margin kesalahan $\delta$.                  |
| 2       | Berapa nilai estimasi eigenvalue string-nya?        | Diperoleh nilai $\Lambda_{max} = 0.11$ dalam representasi biner.                              |

## Paragraf 4
1. mulai bagian 2: pakai QPE pada 4 qubit
> Penulis memulai fase kedua dengan menerapkan algoritma QPE pada sistem empat qubit.
2. 3 qubit pertama digunakan untuk dapet estimasi lebih akurat untuk eigen value $\Lambda_{max}$ dan qubit terakhir untuk estimasi eigenvector
> Penulis menjelaskan alokasi qubit untuk mencapai presisi estimasi nilai eigen yang lebih tinggi.
3. nunjukin tabel V
> Penulis merujuk pada Tabel V untuk menyajikan distribusi probabilitas hasil pengukuran.
4. laporan tentang kehingan koherensi seiring bertambahnya depth
> Penulis mencatat penurunan koherensi yang signifikan akibat peningkatan kedalaman sirkuit.
5. laporan hasilnya hampir ideal
> Penulis melaporkan bahwa hasil simulator masih mendekati kondisi ideal, memberikan standar performa hardware.
6. laporan eigenvalue yan gdiprediksi adalah 0.111 atau 0.875
> Penulis menyajikan nilai eigen prediktif dalam format biner untuk perbandingan akurasi.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Bagaimana fase kedua algoritma diimplementasikan?   | Menggunakan sistem 4-qubit untuk menjalankan algoritma QPE yang lebih presisi.                |
| 2       | Bagaimana alokasi register qubitnya?                | 3 qubit pertama untuk estimasi nilai eigen dan qubit terakhir untuk menampung eigenvector.    |
| 3       | Di mana data hasil QPE dilaporkan?                  | Tabel V menyajikan perbandingancounts antara simulator dan hardware riil.                    |
| 4       | Apa masalah utama saat menjalankan sirkuit QPE?     | Terjadi kehilangan koherensi total pada hardware riil akibat kedalaman sirkuit yang besar.    |
| 5       | Bagaimana kualitas hasil pada simulator?            | Memberikan hasil hampir ideal dengan fidelitas mencapai 0.965.                                |
| 6       | Berapa nilai estimasi eigenvalue dari QPE?          | Diperoleh nilai biner $0.111$ yang setara dengan angka desimal $0.875$.                        |

## Paragraf 5
1. bagian 2 dilakukan juga untuk 4x4
> Penulis melakukan replikasi prosedur untuk kasus matriks 4x4 guna menguji skalabilitas.
2. nunjukin $\ket{b_0}$ lalu lakukan yang sama sebaagaimana proses iteratif
> Penulis mendeskripsikan inisialisasi *state* awal dan siklus iterasi yang serupa.
3. tabel VI
> Penulis menyajikan data mentah hasil eksperimen pada Tabel VI.
4. perbedaan dengan tabel VII
> Penulis mendiskusikan perbedaan hasil pada Tabel VII untuk menyoroti variabilitas sistem.
5. penegasan konsekuensi dekorensi
> Penulis menegaskan kembali dampak destruktif dari dekoherensi pada sistem berdimensi tinggi.
6. nunjukin hasil $\ket{u_{max}}$ 
> Penulis menyajikan hasil akhir estimasi *eigenvector* utama untuk kasus 4x4.

| Kalimat | Pertanyaan                                     | Jawaban                                                                    |
| :------ | :------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| 1       | Bagaimana pengujian pada matriks $4 \times 4$ dilakukan? | Mengikuti langkah-langkah yang sama dengan kasus $2 \times 2$ secara bertahap.            |
| 2       | Apa state awal yang digunakan?                           | State superposisi merata $b_0\rangle$ yang diterapkan sebanyak empat kali iterasi.        |
| 3       | Di mana hasil counts iterasi dilaporkan?                 | Tabel VI menyajikan hasil lengkap counts untuk setiap tahap proses iteratif.              |
| 4       | Apa yang dilaporkan pada Tabel VII?                      | Hasil counts setelah rotasi basis pengukuran untuk mendapatkan informasi fase.            |
| 5       | Bagaimana kondisi hardware saat pengujian ini?           | Kedalaman sirkuit yang sangat besar mencegah hardware dari memulihkan hasil yang berguna. |
| 6       | Apa estimasi akhir eigenvector untuk kasus 4x4?          | Disajikan dalam bentuk kombinasi linear basis $00\rangle,01\rangle,10\rangle,11\rangle$.  |

---
# APPENDIX D
## Paragraf 1
1. tujuan section ini
> Penulis menetapkan tujuan bagian ini untuk memberikan justifikasi teoretis atas *error bars* yang digunakan.
2. argumen tentang eror estimasi
> Penulis menyajikan argumen mengenai besaran kesalahan estimasi pada populasi *state*.
3. perkiraan eror
> Penulis memberikan perkiraan kesalahan berdasarkan kedalaman sirkuit dan fidelitas gerbang.
4. perhitungan kesalahan statistik
> Penulis melakukan kalkulasi kesalahan statistik dengan mempertimbangkan jumlah *shots* eksperimental.
5. nilai eror di kasus papaer
> Penulis melaporkan besaran kesalahan spesifik yang ditemui dalam kasus penelitian ini.
6. total eror di kasus paper
> Penulis merumuskan total akumulasi kesalahan yang mempengaruhi validitas hasil akhir.
7. nilai exact yang bukan persenan
> Penulis menyajikan nilai kesalahan dalam satuan absolut untuk memberikan gambaran presisi yang jelas.
8. nilai yang digunakan di eror bar
> Penulis mengonfirmasi penggunaan nilai-nilai tersebut dalam representasi grafis hasil eksperimen.

| Kalimat | Pertanyaan                                | Jawaban                                                                        |
| :------ | :-------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| 1       | Apa tujuan dari lampiran terakhir ini?              | Menjelaskan secara rinci asal-usul bilah kesalahan (*error bars*) pada grafik Gambar 2.       |
| 2       | Bagaimana kesalahan populasi state diestimasi?      | Berdasarkan asumsi kesalahan eksperimental sebesar 8% per gerbang dua-qubit.                  |
| 3       | Berapa total kesalahan dari pengaturan hardware?    | Akumulasi tiga gerbang menghasilkan estimasi kesalahan sekitar 24%.                           |
| 4       | Berapa besaran kesalahan statistik murni?           | Sekitar 11%, yang dihitung berdasarkan jumlah tembakan (*shots*) sebanyak 8192 kali.          |
| 5       | Berapa estimasi total kesalahan gabungan?           | Penulis mengasumsikan total kesalahan sebesar 35% untuk skenario terburuk.                    |
| 6       | Bagaimana implikasinya terhadap jumlah data?        | Sekitar 2900 hasil pengukuran dari total 8192 dianggap sebagai data yang salah.               |
| 7       | Berapa nilai kesalahan numerik per state?           | Sekitar 360 unit counts untuk setiap state pengukuran.                                        |
| 8       | Untuk apa nilai numerik ini digunakan?              | Sebagai dasar untuk membangkitkan bilah kesalahan pada visualisasi data eksperimental.        |