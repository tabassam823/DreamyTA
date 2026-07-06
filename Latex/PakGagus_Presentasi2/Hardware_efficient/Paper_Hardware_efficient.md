# 1. Pendahuluan dan Latar Belakang

## Masalah Utama: Struktur Elektronik dan Fermion

Penulis memulai dengan menyatakan bahwa komputer kuantum dapat digunakan untuk memecahkan **masalah struktur elektronik** dan fisika materi terkondensasi yang dirumuskan sebagai "masalah fermion yang saling berinteraksi".

- **Penjelasan:** Materi (molekul, material) tersusun dari elektron, yang dalam fisika kuantum dikategorikan sebagai partikel _fermion_. Sifat-sifat kimia suatu molekul ditentukan oleh bagaimana elektron-elektron ini berinteraksi satu sama lain.
- **Kontribusi di Paper:** Ini menetapkan **tujuan akhir** dari eksperimen paper ini. Paper ini tidak hanya menguji komputer kuantum secara abstrak, tetapi mencoba menyelesaikan masalah kimia nyata (mencari energi dasar molekul).

## Batasan Komputer Klasik: Skala Eksponensial dan "Sign Problem"

Paper menjelaskan bahwa mencari solusi eksak untuk masalah fermion ini di komputer klasik memiliki biaya komputasi yang **berskala secara eksponensial** dengan ukuran sistem. Selain itu, metode aproksimasi klasik seperti _Monte Carlo_ tidak cocok karena adanya **fermionic sign problem**.

- **Penjelasan:** Semakin besar molekulnya, semakin mustahil bagi superkomputer terkuat sekalipun untuk mensimulasikannya secara akurat. Metode statistik biasa gagal karena sifat matematika mekanika kuantum elektron yang kompleks (tanda positif/negatif pada fungsi gelombang yang saling meniadakan).
- **Kontribusi di Paper:** Ini memberikan **justifikasi** mengapa kita membutuhkan metode yang ditawarkan paper ini. Keterbatasan klasik inilah yang membuat penggunaan komputer kuantum "berukuran sedang" menjadi menarik dan penting untuk diteliti.

## Celah Penelitian (Research Gap): Terbatas pada Molekul Kecil

Penulis menyoroti bahwa implementasi eksperimental sebelumnya pada komputer kuantum sangat terbatas, hanya pada molekul yang sangat sederhana seperti Hidrogen dan Helium.

- **Penjelasan:** Sebelum paper ini terbit, demonstrasi kimia kuantum hanya berhasil pada sistem yang sangat kecil dan sepele.
- **Kontribusi di Paper:** Ini menetapkan standar yang ingin dilampaui oleh penulis. Mereka ingin membuktikan bahwa metode mereka bisa menangani molekul yang lebih besar, yaitu hingga **BeH2 (Berilium Dihidrida)**, yang merupakan lompatan kompleksitas signifikan dibanding Hidrogen.

## Solusi Paper: Pendekatan "Hardware-Efficient"

Di akhir paragraf, penulis merangkum "resep rahasia" keberhasilan mereka dalam mencapai simulasi molekul yang lebih besar (hingga 6 qubit dan lebih dari 100 istilah Pauli). Resep tersebut adalah kombinasi dari tiga elemen:

1. **Variational Quantum Eigensolver (VQE):** Algoritma hibrida (kuantum-klasik).
2. **Trial States yang Efisien secara Hardware:** Keadaan awal kuantum yang disesuaikan secara khusus dengan kemampuan perangkat keras (prosesor) yang mereka miliki, bukan sekadar teori abstrak.
3. **Encoding yang Kompak & Optimasi Stokastik:** Cara memetakan masalah kimia ke qubit secara efisien dan algoritma optimasi yang tahan terhadap gangguan (noise).

- **Kontribusi di Paper:** Ini adalah **inti inovasi** paper. Penulis tidak menggunakan gerbang kuantum standar yang mungkin terlalu "mahal" (banyak error) untuk perangkat saat itu. Sebaliknya, mereka merancang sirkuit yang "memeluk" keterbatasan hardware mereka untuk mendapatkan hasil yang akurat.

# 2. Definisi Masalah dan Tantangan

## Tujuan Utama: Energi "Ground-State"

Penulis menyatakan bahwa tujuan fundamental dalam masalah struktur elektronik adalah menyelesaikan **energi keadaan dasar (ground-state energy)** dari Hamiltonian fermionik yang saling berinteraksi.

- **Penjelasan:** Di alam semesta, molekul selalu ingin berada di tingkat energi terendah agar stabil. Keadaan terendah ini disebut _ground state_. Jika kita tahu energi ini, kita bisa memprediksi reaksi kimia dan sifat material.
- **Kontribusi di Paper:** Seluruh eksperimen di paper ini pada dasarnya adalah upaya untuk menemukan satu angka ini (energi terendah) untuk berbagai molekul (H2, LiH, BeH2). Grafik hasil eksperimen nanti akan membandingkan angka yang didapat komputer kuantum dengan angka teoretis yang sebenarnya.

## Tantangan Penerjemahan: Mapping (Pemetaan)

Kalimat berikutnya menjelaskan bahwa untuk menyelesaikan masalah ini di komputer kuantum, kita harus mengandalkan **pemetaan (mapping) antara operator fermion dan operator qubit**.

- **Penjelasan:**
    - **Fermion (Elektron):** Memiliki aturan fisika yang unik (misalnya, dua elektron tidak boleh berada di posisi dan keadaan kuantum yang sama persis).
    - **Qubit:** Adalah sistem dua level sederhana (0 dan 1).
    - Komputer kuantum tidak secara "alami" memahami elektron. Kita butuh "kamus penerjemah" (algoritma matematika) untuk mengubah perilaku elektron menjadi instruksi yang dimengerti qubit.
- **Kontribusi di Paper:** Konsep ini menjadi dasar bagi teknik yang mereka gunakan nanti (disebut _parity mapping_ atau _binary tree encoding_). Mereka harus mengubah masalah kimia menjadi rangkaian gerbang qubit.

## Hamiltonian Lokal (Local Hamiltonian)

Masalah ini kemudian dirumuskan ulang sebagai masalah **Hamiltonian lokal-k (k-local Hamiltonian)**.

- **Penjelasan:**
    - **Hamiltonian ($H$):** Operator matematika yang mewakili total energi sistem.
    - **Lokal ($k$-local):** Artinya, interaksi energi tidak terjadi antara _semua_ partikel sekaligus secara acak. Sebaliknya, interaksi hanya melibatkan sejumlah kecil ($k$) qubit sekaligus (misalnya, qubit A hanya berinteraksi dengan qubit B di sebelahnya).
- **Kontribusi di Paper:** Ini sangat penting karena perangkat keras (hardware) yang mereka gunakan, superkonduktor IBM, memiliki keterbatasan konektivitas. Qubit hanya bisa "berbicara" dengan tetangganya. Dengan merumuskan masalah sebagai "lokal", mereka memastikan masalah ini _bisa_ dijalankan di chip fisik mereka.

## Persamaan Eigen (Eigenvalue Problem)

Paragraf ini ditutup dengan persamaan matematika inti: $$H |\Phi_G\rangle = E_G |\Phi_G\rangle$$ Di mana tujuannya adalah menemukan **Nilai Eigen ($E_G$)** dan **Keadaan Eigen ($|\Phi_G\rangle$)**.

- **Penjelasan:** Ini adalah persamaan Schrödinger versi ringkas.
    - $H$ adalah pertanyaannya (sistem molekul).
    - $|\Phi_G\rangle$ adalah jawabannya (posisi/keadaan elektron).
    - $E_G$ adalah nilai (energi) yang kita cari.
- **Kontribusi di Paper:** Paper ini menggunakan algoritma bernama **VQE (Variational Quantum Eigensolver)**. Kata "Eigensolver" dalam nama algoritma tersebut merujuk langsung pada tugas menyelesaikan persamaan matematika ini.

## Tingkat Kesulitan: QMA-Complete

Penulis menyatakan bahwa untuk $k \ge 2$, masalah Hamiltonian lokal ini diketahui bersifat **QMA-complete**.

- **Penjelasan:** Dalam ilmu komputer teoritis, _QMA-complete_ adalah versi kuantum dari _NP-complete_. Ini adalah kelas masalah yang paling sulit. Secara matematis, tidak ada algoritma efisien yang diketahui bisa memecahkan masalah ini dalam bentuk umumnya.
- **Kontribusi di Paper:** Penulis jujur mengenai kesulitan masalah ini. Namun, mereka membuat pengecualian penting: meskipun masalah _umum_ itu mustahil, sistem _fisik_ (seperti molekul nyata di alam) memiliki struktur khusus yang diharapkan bisa diselesaikan secara efisien oleh komputer kuantum, meskipun tetap sulit bagi komputer klasik.

## Pendekatan "Textbook": Quantum Phase Estimation (QPE)

Penulis merujuk pada ide awal Richard Feynman tentang simulasi kuantum dan menyebutkan algoritma standar yang biasanya diajarkan untuk masalah ini: **Quantum Phase Estimation (QPE)**.

- **Penjelasan:** QPE adalah algoritma kuantum murni yang sangat kuat. Jika Anda memiliki komputer kuantum yang sempurna, QPE adalah cara terbaik untuk menemukan energi molekul. Namun, QPE memiliki syarat: Anda harus mulai dengan "tebakan awal" (initial state) yang cukup bagus (memiliki _overlap_ besar dengan jawaban yang benar).
- **Kontribusi di Paper:** Ini menetapkan "kompetitor" atau metode standar. Penulis memberi tahu kita bagaimana seharusnya masalah ini diselesaikan secara teori.

## Masalah dengan QPE: Koherensi Hardware

Di akhir paragraf ketiga (dan awal kalimat paragraf selanjutnya), penulis menjelaskan mengapa mereka **tidak** menggunakan QPE. Meskipun QPE sangat akurat, algoritma ini memiliki **"stringent requirements on the coherence"** (persyaratan ketat pada koherensi).

- **Penjelasan:**
    - **Koherensi:** Kemampuan qubit untuk mempertahankan informasi kuantumnya sebelum rusak oleh gangguan lingkungan (noise).
    - Algoritma QPE membutuhkan rangkaian gerbang kuantum yang sangat panjang. Pada tahun 2017 (saat paper ini ditulis), dan bahkan sekarang, komputer kuantum memiliki waktu koherensi yang pendek. Jika kita menjalankan QPE, qubit akan "rusak" (error) sebelum perhitungannya selesai.
- **Kontribusi di Paper:** Ini adalah titik balik yang krusial. Penulis berargumen bahwa metode standar (QPE) **gagal** diterapkan pada perangkat keras masa kini (NISQ - _Noisy Intermediate-Scale Quantum_).

# 3. Variational Quantum Eigensolver (VQE) dan Ansatz

## Solusi: Variational Quantum Eigensolver (VQE)

Penulis memperkenalkan pendekatan alternatif menggunakan "pengoptimal kuantum" yang dikenal sebagai **VQE**.

- **Penjelasan:** VQE adalah algoritma hibrida. Berbeda dengan algoritma kuantum murni yang berjalan 100% di dalam prosesor kuantum (seperti QPE), VQE membagi tugas antara komputer kuantum dan komputer klasik (laptop biasa).
- **Kontribusi di Paper:** Penulis memilih VQE karena algoritma ini **mengurangi persyaratan koherensi**. Artinya, VQE tidak membutuhkan rangkaian gerbang kuantum yang sangat panjang, sehingga cocok untuk prosesor yang "berisik" (mudah error) seperti yang digunakan dalam eksperimen ini.

## Prinsip Matematika: Ritz’s Variational Principle

Dasar teori dari VQE adalah **Prinsip Variasional Ritz**.

- **Penjelasan:** Prinsip ini menyatakan sebuah aturan sederhana namun kuat: _Energi rata-rata dari sembarang keadaan gelombang percobaan (trial state) akan selalu lebih besar atau sama dengan energi keadaan dasar (ground state) yang sebenarnya._
    - Artinya: Kita tidak perlu tahu jawabannya di awal. Kita cukup membuat tebakan, menghitung energinya, dan jika kita bisa membuat energinya semakin rendah, berarti tebakan kita semakin mendekati jawaban yang benar.
- **Kontribusi di Paper:** Ini adalah "kompas" yang digunakan dalam eksperimen. Selama energi yang diukur terus turun, penulis tahu mereka berada di jalan yang benar menuju solusi struktur elektronik molekul tersebut.

## Cara Kerja: Loop Umpan Balik (Feedback Loop)

Paragraf ini menjelaskan mekanisme teknis bagaimana VQE bekerja dalam langkah-langkah berulang:

1. **Quantum:** Komputer kuantum menyiapkan "trial state" (keadaan coba-coba) yang bergantung pada sekumpulan **parameter** (angka-angka pengatur).
2. **Quantum:** Mengukur nilai ekspektasi energi dari keadaan tersebut.
3. **Klasik:** Nilai energi dikirim ke komputer klasik (optimizer). Komputer klasik menghitung cara mengubah parameter agar energi turun, lalu mengirim parameter baru ke komputer kuantum.

- **Kontribusi di Paper:** Mekanisme ini memungkinkan eksperimen dilakukan secara iteratif. Grafik hasil nanti akan menunjukkan bagaimana energi "turun" perlahan-lahan seiring bertambahnya iterasi (loop) ini.

## Keunggulan VQE (Quantum Advantage)

Penulis menutup paragraf ini dengan menjelaskan mengapa kita tetap butuh komputer kuantum jika komputer klasik juga ikut bekerja.

- **Penjelasan:** Komputer klasik tidak bisa mensimulasikan "trial state" yang sangat kompleks secara efisien. Namun, komputer kuantum bisa menyiapkan keadaan kompleks tersebut dengan mudah.
- **Kontribusi di Paper:** Ini menegaskan bahwa VQE bisa menyiapkan keadaan kuantum yang **tidak dapat dijangkau oleh perhitungan numerik klasik**. Ini adalah argumen utama mengapa metode ini memiliki masa depan yang cerah untuk masalah kimia yang sangat besar.

## Masalah pada Metode Standar: "Unitary Coupled Cluster (UCC)"

Penulis memulai dengan mengkritik metode standar yang biasa digunakan untuk membuat "tebakan awal" (trial state) dalam kimia kuantum, yang disebut _Unitary Coupled Cluster (UCC) ansatz_.

- **Penjelasan:**
    - **Ansatz:** Ini adalah istilah Jerman yang berarti "pendekatan" atau "tebakan terpelajar". Dalam konteks ini, _ansatz_ adalah rumus matematika yang kita gunakan untuk menebak bentuk gelombang elektron.
    - **Masalah UCC:** Meskipun UCC sangat akurat secara teori kimia, ia sangat rumit. Jumlah parameter yang harus diatur berskala secara **kuartik** (pangkat empat) dengan ukuran sistem. Artinya, jika sistem sedikit membesar, kerumitan sirkuitnya meledak drastis.
- **Kontribusi di Paper:** Penulis menunjukkan bahwa metode "textbook" ini terlalu mahal dan lambat untuk komputer kuantum saat ini.

## Tantangan Teknis: Error Trotterisasi

Selain jumlah parameter yang banyak, penerapan UCC juga menghadapi masalah teknis bernama **Trotterization errors**.

- **Penjelasan:** Persamaan UCC bersifat kontinu (seperti waktu yang mengalir), tetapi komputer kuantum bekerja dengan gerbang diskrit (langkah demi langkah). Untuk mengubah UCC menjadi gerbang kuantum, kita harus memotong-motongnya (metode Trotter). Proses ini membutuhkan rangkaian gerbang yang sangat panjang (deep circuits).
- **Kontribusi di Paper:** Karena komputer kuantum saat ini "berisik" (noise), rangkaian yang terlalu panjang akan mengakibatkan hasil yang hancur karena error sebelum perhitungan selesai. Ini memperkuat alasan mengapa UCC tidak bisa dipakai di eksperimen ini.

## Inovasi Utama: "Hardware-Efficient Ansatz"

Inilah inti dari judul paper ini. Penulis memperkenalkan solusi mereka: **Hardware-efficient ansatz preparation**.

- **Penjelasan:** Alih-alih memaksakan rumus kimia yang rumit (UCC) ke dalam hardware, penulis melakukan hal sebaliknya. Mereka merancang _ansatz_ (tebakan) yang **disesuaikan dengan gerbang yang tersedia secara alami** di perangkat keras mereka.
    - Mereka menggunakan gerbang logika yang "murah" dan mudah dilakukan oleh chip prosesor mereka, asalkan gerbang tersebut cukup untuk menciptakan _entanglement_ (keterikatan kuantum).
- **Kontribusi di Paper:** Ini adalah strategi pragmatis. Dengan menggunakan pendekatan yang "ramah hardware", mereka bisa menjaga sirkuit tetap pendek (shallow), sehingga mengurangi dampak _noise_ (gangguan) dan memungkinkan simulasi molekul yang lebih besar.

## Bukti Keberhasilan: H2, LiH, BeH2, dan Magnetisme

Paragraf ini ditutup dengan klaim keberhasilan eksperimen mereka menggunakan metode baru tersebut.

- **Penjelasan:** Mereka tidak hanya berteori. Mereka membuktikan metode _hardware-efficient_ ini pada prosesor superkonduktor untuk mensimulasikan:
    - **Hidrogen (H2)** dan **Litium Hidrida (LiH)** (molekul kecil).
    - **Berilium Dihidrida (BeH2)** (molekul terbesar yang pernah disimulasikan di komputer kuantum saat itu).
    - **Model Heisenberg Antiferromagnetik:** Masalah magnetisme untuk menunjukkan fleksibilitas metode ini di luar kimia.
- **Kontribusi di Paper:** Ini adalah ringkasan hasil yang akan dibahas secara detail di grafik-grafik selanjutnya (Figur 2, 3, dan 4).

# 4. Visualisasi Eksperimen (Figur 1)

**Figur 1** adalah "peta jalan" visual yang merangkum seluruh eksperimen, mulai dari teori kimia hingga ke perangkat keras fisik.

## Panel A: Dari Kimia ke Qubit (Mapping)

Gambar bola-bola berwarna biru dan merah di sebelah kiri atas merepresentasikan **orbital elektron** (tempat elektron berada dalam atom).

- **Masalah Awal:** Untuk molekul yang mereka teliti (seperti BeH2), terdapat 8 _spin orbitals_ (bola-bola tersebut).
- **Reduksi Qubit:** Secara naif, kita butuh 8 qubit (1 qubit per orbital). Namun, penulis menggunakan teknik matematika bernama **Parity Mapping** dan memanfaatkan simetri fisika (seperti kekekalan jumlah partikel).
- **Hasil:** Dengan memanfaatkan simetri tersebut, mereka bisa membuang 2 qubit yang informasinya sudah diketahui, sehingga masalah 8-orbital ini dipadatkan menjadi **6 qubit** saja.

## Panel B: Perangkat Keras (The Chip)

Gambar di kanan atas adalah foto mikroskop elektron dari **chip prosesor kuantum** yang digunakan.

- **Qubit Transmon:** Anda melihat kotak-kotak kecil yang diberi label Q1, Q2, hingga Q7. Ini adalah qubit superkonduktor jenis _transmon_. Meskipun ada 7 qubit di chip, eksperimen ini hanya menggunakan **6 qubit** (Q1–Q6).
- **Koneksi (Bus):** Garis bergelombang berwarna ungu (violet) adalah _waveguide resonators_. Ini berfungsi sebagai "kabel penghubung" yang memungkinkan qubit saling berkomunikasi (entanglement). Perhatikan bahwa tidak semua qubit terhubung langsung satu sama lain.

## Panel C: Sirkuit Kuantum (The Ansatz)

Gambar di kiri bawah adalah "partitur musik" atau **sirkuit algoritma** yang dijalankan. Ini adalah implementasi visual dari **Hardware-Efficient Ansatz**.

1. **State Awal ($|0\rangle$):** Semua qubit dimulai dari keadaan dasar (0).
2. **Rotasi Single-Qubit ($U_{q,0}(\theta)$):** Kotak-kotak kuning/biru di awal. Ini adalah operasi memutar masing-masing qubit secara individu. Sudut putarannya ($\theta$) adalah **parameter** yang akan ditebak dan diperbaiki terus-menerus oleh komputer klasik.
3. **Entangler ($U_{ENT}$):** Blok besar berwarna abu-abu/ungu. Ini adalah operasi yang membuat semua qubit saling terikat (_entangled_) secara bersamaan atau berurutan sesuai koneksi fisik di Panel B.
4. **Pengulangan (Depth $d$):** Pola "Rotasi -> Entangler" ini bisa diulang beberapa kali (disebut kedalaman atau _depth_ $d$).
5. **Pengukuran (Post-rotations):** Di ujung paling kanan, qubit diukur untuk mendapatkan nilai energi.

## Panel D: Sinyal Fisik (Pulse)

Gambar kecil di kanan bawah menunjukkan apa yang sebenarnya terjadi di level mesin.

- Kotak-kotak logika di Panel C diterjemahkan menjadi **gelombang mikrogelombang** (sinyal listrik) yang dikirim ke chip.
- Penulis menggunakan gerbang _cross-resonance_ (CR) untuk menciptakan _entanglement_ antar qubit.

# 5. Implementasi Teknis dan Fisik

## Spesifikasi Perangkat Keras (The Device)

- **Jenis Qubit:** Prosesor superkonduktor dengan **enam qubit transmon** frekuensi tetap (fixed-frequency).
- **Suhu:** Chip ini didinginkan dalam _dilution refrigerator_ hingga suhu **25 mK** (sangat dingin, mendekati nol mutlak) untuk meminimalkan gangguan termal.
- **Konektivitas:** Qubit-qubit ini tidak terhubung sembarangan, melainkan dikopel melalui _waveguide resonators_. Ini membatasi qubit mana yang bisa berinteraksi langsung dengan qubit mana.

## Strategi "Hardware-Efficient" dan Drift Hamiltonian ($H_0$)

- **Entangler Alami:** Alih-alih memaksakan gerbang logika standar (seperti CNOT), mereka menggunakan interaksi alami yang dimiliki perangkat keras tersebut (_drift Hamiltonian_) untuk menciptakan _entanglement_ ($U_{ENT}$).
- **Drift Hamiltonian ($H_0$):** $H_0$ adalah representasi matematika dari interaksi fisik yang terjadi antar-qubit jika kita membiarkan mereka "mengalir" (drift) begitu saja.
- **Persamaan Entangler ($U_{ENT}$):** $$U_{ENT} = \exp(-i H_0 \tau)$$ Di mana $\tau$ adalah waktu evolusi.

## Rotasi Euler Satu-Qubit ($U_{q,i}(\theta)$)

Entanglement saja tidak cukup; kita butuh cara untuk mengontrol atau "menyetir" qubit. Penulis menggunakan rotasi Euler yang disisipkan di antara entangler: $$U_{q,i}(\theta)$$ Yang diimplementasikan sebagai kombinasi gerbang **Z** dan **X**.
- Simbol $\theta$ (theta) adalah **sudut putaran**. Inilah "tombol volume" yang akan diputar-putar oleh komputer klasik untuk mencari jawaban yang benar.

## Persamaan Utama "Trial State" ($|\Phi\rangle$)

Gabungan dari kedua komponen di atas menghasilkan persamaan besar:
$$|\Phi(\theta)\rangle = \underbrace{\left( \prod_{d} U_{ENT} \times U_{rotasi} \right)}_{\text{Diulang d kali}} \times |00...0\rangle$$

- Kita mulai dari keadaan dasar $|00...0\rangle$.
- Lalu kita tumpuk lapisan-lapisan: **Satu lapis Rotasi ($\theta$), lalu satu lapis Entangler ($U_{ENT}$)**.
- **Kedalaman ($d$):** Huruf $d$ menunjukkan berapa lapis kue yang kita buat.

## Strategi Parameter dan Kontrol Fisik

1. **Pengurangan Parameter:** Rotasi Z awal dibuang karena tidak mengubah keadaan $|0\rangle$. Jumlah parameter menjadi $p = N(3d + 2)$.
2. **Kunci Waktu, Putar Sudut:** Mereka menetapkan durasi entangler ($\tau$) sebagai nilai tetap, dan hanya mengubah-ubah sudut $\theta$ sebagai parameter variasional.
3. **Trik Rotasi Z (Frame Changes):** Rotasi Z dilakukan secara **virtual** dengan mengubah "jam referensi" di software, sehingga instan dan nol error.
4. **Rotasi X:** Dilakukan dengan pulsa mikrogelombang waktu tetap (**100 ns**), amplitudo diatur sesuai sudut $\theta$.
5. **Gerbang Dua-Qubit (Cross-Resonance):** Menggunakan pulsa **150 ns** yang dikalibrasi untuk menghasilkan entanglement maksimal.

# 6. Pengukuran dan Optimasi

## Tantangan Pengukuran: Fluktuasi Stokastik

- Dalam mekanika kuantum, kita tidak bisa mendapatkan jawaban pasti hanya dengan satu kali pengukuran. Kita harus mengukur berulang kali (sampling).
- Karena proses ini melibatkan peluang, hasil pengukuran akan selalu sedikit bergoyang-goyang atau tidak stabil. Inilah yang disebut **"stochastic fluctuations due to finite sampling"**.

## Trik Efisiensi: Pengelompokan (Grouping)

- Mendapatkan nilai Hamiltonian molekul membutuhkan pengukuran ratusan operator Pauli.
- Penulis mengelompokkan suku-suku yang kompatibel (_commuting_) agar bisa diukur secara **bersamaan**, mengurangi overhead waktu secara drastis.

## Otak Algoritma: SPSA

Penulis menggunakan algoritma **SPSA (Simultaneous Perturbation Stochastic Approximation)**.
- SPSA bisa memperkirakan gradien hanya dengan **dua kali pengukuran** energi, tidak peduli berapapun jumlah parameternya ($p=30$ atau lebih).
- Ini krusial untuk mengatasi noise dan mempercepat konvergensi eksperimen.

# 7. Pemetaan Molekul dan Hasil BeH2 (Figur 2)

## Pemetaan Masalah Kimia
Teknik **"Binary Tree Encoding"** (Parity Mapping) digunakan untuk memadatkan masalah:
1. **Hidrogen (H2):** 4 orbital $\rightarrow$ dipadatkan menjadi **2 qubit**.
2. **Litium Hidrida (LiH):** Dipadatkan menjadi **4 qubit**.
3. **Berilium Dihidrida (BeH2):** 10 orbital. Menggunakan aproksimasi _frozen core_ (mengabaikan elektron dalam) $\rightarrow$ dipadatkan manjadi **6 qubit**.

## Figur 2: Proses Optimasi BeH2
- **Konteks:** Molekul BeH2 pada jarak 1.7 Å, menggunakan 6 qubit.
- **Sumbu:** Grafik menunjukkan Energi (sumbu Y) vs Iterasi (sumbu X).
- **Hasil:** Awan titik-titik data (merah/biru) yang awalnya tinggi perlahan turun berkat algoritma SPSA. Garis hijau (hasil akhir) berhimpitan dengan garis hitam (teori), membuktikan bahwa VQE berhasil menemukan energi dasar.
- **Kedalaman ($d=1$):** Penulis memilih sirkuit pendek ($d=1$) sebagai kompromi. Sirkuit pendek mengurangi akumulasi noise, meskipun secara teori kurang ekspresif (_trade-off Depth vs Noise_). Ada **30 parameter** yang dioptimalkan dalam eksperimen ini.

# 8. Kurva Energi Potensial (Figur 3)

**Figur 3** menunjukkan kurva energi potensial untuk tiga molekul berbeda saat atom-atomnya ditarik menjauh.

## Panel A: Hidrogen (H2) - 2 Qubit
- Hasil eksperimen sangat akurat dan menempel pada garis teori. $d=1$ cukup untuk model ini.

## Panel B: Litium Hidrida (LiH) - 4 Qubit
- Terdapat penyimpangan ("bengkokan") pada jarak 2.5–3.0 Å.
- **Analisis:** Penyimpangan ini bukan karena noise, melainkan karena sirkuit $d=1$ terlalu dangkal untuk menangkap kompleksitas LiH pada jarak tersebut (secara teori butuh $d=8$). Penulis tidak meningkatkan $d$ karena keterbatasan hardware (noise).

## Panel C: Berilium Dihidrida (BeH2) - 6 Qubit
- Titik-titik eksperimen berhasil mengikuti tren kurva teori.
- Ini adalah pencapaian terbesar, membuktikan simulasi molekul 3-atom dengan 6 qubit di hardware NISQ.

## Validasi Noise
Area berwarna (shading) di grafik adalah hasil simulasi komputer klasik yang sengaja diberi noise. Karena data eksperimen jatuh di dalam area ini, penulis mengonfirmasi bahwa mereka memahami karakteristik error pada mesin mereka dengan baik.

# 9. Aplikasi Magnetisme Kuantum (Figur 4)

Penulis mendemonstrasikan fleksibilitas chip dengan mensimulasikan **Model Heisenberg Antiferomagnetik** pada 4 qubit.

## Model Fisika
Persamaan Hamiltonian:
$$H = \sum_{\langle ij \rangle} J (X_i X_j + Y_i Y_j + Z_i Z_j) + \sum_i B Z_i$$
- Suku pertama ($J$): Interaksi antar qubit (mendorong entanglement).
- Suku kedua ($B$): Medan magnet luar (mendorong qubit mandiri/searah).

## Analisis Hasil
- **Jika $J=0$ (Medan Magnet Menang):** Sirkuit sederhana **$d=0$** (tanpa entangler) memberikan hasil terbaik.
- **Jika $J$ Tinggi (Interaksi Menang):** Sirkuit **$d=2$** (dua lapis entangler) diperlukan dan memberikan hasil lebih akurat, meskipun lebih berisik. Sirkuit $d=0$ gagal total di sini.
- Ini membuktikan bahwa kompleksitas sirkuit ($d$) harus disesuaikan dengan fisika masalah yang dihadapi.

# 10. Kesimpulan dan Replikasi

## Kesimpulan Paper
1. **Fleksibilitas Terbukti:** Metode _Hardware-Efficient Ansatz_ berhasil untuk kimia dan magnetisme.
2. **Pemahaman Noise:** Hasil sangat cocok dengan model simulasi noise.
3. **Masa Depan:** Untuk molekul lebih besar, diperlukan konektivitas qubit yang lebih baik dan waktu koherensi yang lebih panjang untuk memungkinkan sirkuit yang lebih dalam.

## Panduan Replikasi
Paper ini sangat detail dan memungkinkan replikasi metodologi:
- **Sirkuit:** Bangun sirkuit dengan lapisan selang-seling $U_{ENT}$ (drift) dan Rotasi Euler.
- **Kontrol:** Gunakan Virtual-Z dan rotasi X waktu-tetap.
- **Optimasi:** Gunakan algoritma SPSA dengan sampling yang dikelompokkan.
- **Mapping:** Gunakan Parity Mapping dan _frozen core_ approximation.
- **Data:** Matriks Hamiltonian tersedia di Supplementary Information paper asli.