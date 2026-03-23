# Pemetaan Game Theory ke Model Ising untuk Optimasi Portofolio Kuantum

## 1. Transformasi Data Finansial ke dalam Kerangka Multi-Agent Game

Proses pemodelan dimulai dengan ekstraksi variabel dasar dari semesta pasar yang terdiri dari $N$ aset finansial. Data deret waktu harga penutupan (*closing price*) diambil selama rentang waktu $T$ untuk menghitung dua parameter fundamental, yaitu ekspektasi *return* ($\mu_i$) dan matriks kovariansi ($\Sigma$). Ekspektasi *return* merepresentasikan nilai rata-rata keuntungan historis, sementara elemen $\sigma_{ij}$ pada matriks kovariansi menggambarkan hubungan risiko antar aset. 

Sebagai inovasi dalam pemodelan risiko, parameter $\gamma$ (*risk aversion*) tidak lagi dianggap sebagai konstanta statis, melainkan sebuah variabel adaptif yang bergantung pada performa relatif aset. Tingkat penghindaran risiko ini diformulasikan menggunakan fungsi *sigmoid* yang memetakan rasio *return* terhadap risiko ($\mu/\sigma$) ke dalam rentang kontinu $(0, 1)$. Secara matematis, $\gamma$ didefinisikan sebagai:
$$\gamma(\mu, \sigma) = \frac{1}{1 + e^{-(\mu/\sigma)}} \quad (1)$$
Formulasi pada Persamaan (1) memastikan bahwa ketika suatu aset memiliki performa yang sangat dominan terhadap risikonya, sistem akan memberikan bobot penalti risiko yang lebih tinggi untuk menjaga kestabilan portofolio secara egoistis.

Struktur pasar tersebut kemudian ditransformasikan ke dalam model permainan terdesentralisasi di mana setiap aset $i$ bertindak sebagai pemain (*players*). Ruang strategi bersifat biner, di mana variabel $x_i \in \{0, 1\}$ menentukan apakah suatu aset masuk ($x_i = 1$) atau keluar ($x_i = 0$) dari portofolio. Konfigurasi keseluruhan aset dinyatakan dalam vektor profil strategi $\mathbf{x} = (x_1, x_2, \dots, x_N)$. Dalam perspektif ini, keputusan setiap pemain sangat dipengaruhi oleh strategi pemain lain, yang dilambangkan dengan $\mathbf{x}_{-i}$.

## 2. Analisis Fungsi Utilitas dan Bukti Exact Potential Game

Fungsi utilitas atau *payoff* individual $u_i$ dirumuskan untuk mencerminkan keuntungan bersih yang diperoleh aset $i$ saat bergabung ke dalam portofolio. Formulasi ini mempertimbangkan *return* mandiri, risiko bawaan, dan dampak interaksi dengan aset lain yang telah terpilih. Secara matematis, fungsi *payoff* untuk pemain $i$ didefinisikan sebagai:
$$u_i(x_i, \mathbf{x}_{-i}) = x_i \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right) \quad (2)$$
Persamaan (2) menunjukkan bahwa jika aset $i$ memilih untuk tidak berpartisipasi ($x_i = 0$), maka *payoff* yang diterima adalah nol. Sebaliknya, partisipasi aset akan memberikan imbalan $\mu_i$ yang dikurangi oleh penalti risiko mandiri $\frac{\gamma}{2} \sigma_{ii}$ dan penalti interaksi $\gamma \sum \sigma_{ij} x_j$.

Permainan ini diklasifikasikan sebagai *Exact Potential Game* karena terdapat fungsi skalar global $\Phi(\mathbf{x})$ yang melacak perubahan utilitas individu secara presisi. Fungsi potensial yang digunakan dalam konteks ini adalah objektif Markowitz standar:
$$\Phi(\mathbf{x}) = \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j \quad (3)$$
Untuk membuktikan syarat *Potential Game*, suku risiko kuadratik ganda pada Persamaan (3) diekspansi menjadi komponen diagonal dan *off-diagonal*:
$$\sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j = \sum_{i=1}^N \sigma_{ii} x_i^2 + 2 \sum_{i < j} \sigma_{ij} x_i x_j \quad (4)$$
Dengan memanfaatkan sifat *idempotensi* ($x_i^2 = x_i$) dan simetri matriks kovariansi, perubahan Fungsi Potensial $\Delta \Phi$ saat pemain $i$ beralih dari $x_i=0$ ke $x_i=1$ terbukti identik dengan perubahan utilitas individu $\Delta u_i$, yaitu:
$$\Delta \Phi = \Delta u_i = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \quad (5)$$

### 2.1. Ilustrasi Spesifik dan Ekspansi Potensial pada Sistem Empat Aset

Penerapan formulasi utilitas pada sistem yang terdiri dari empat aset ($N=4$), yaitu aset $A, B, C,$ dan $D$, memberikan gambaran yang lebih konkret mengenai mekanisme interaksi antar pemain. Dalam skenario ini, profil strategi pemain lain $\mathbf{x}_{-i}$ dieksplisitkan menjadi variabel keputusan dari aset-aset mitra di dalam pasar. Sebagai contoh, bagi aset $A$, nilai utilitas sangat bergantung pada apakah aset $B, C,$ dan $D$ aktif di dalam portofolio, yang secara matematis merepresentasikan kontribusi risiko sistemik dari seluruh anggota *semesta* aset tersebut.

Berdasarkan definisi umum pada Persamaan (2), fungsi utilitas untuk masing-masing aset dalam sistem empat pemain ini dapat diturunkan sebagai berikut:
$$u_A = x_A \left( \mu_A - \frac{\gamma}{2} \sigma_{AA} - \gamma (\sigma_{AB} x_B + \sigma_{AC} x_C + \sigma_{AD} x_D) \right) \quad (6)$$
$$u_B = x_B \left( \mu_B - \frac{\gamma}{2} \sigma_{BB} - \gamma (\sigma_{BA} x_A + \sigma_{BC} x_C + \sigma_{BD} x_D) \right) \quad (7)$$
$$u_C = x_C \left( \mu_C - \frac{\gamma}{2} \sigma_{CC} - \gamma (\sigma_{CA} x_A + \sigma_{CB} x_B + \sigma_{CD} x_D) \right) \quad (8)$$
$$u_D = x_D \left( \mu_D - \frac{\gamma}{2} \sigma_{DD} - \gamma (\sigma_{DA} x_A + \sigma_{DB} x_B + \sigma_{DC} x_C) \right) \quad (9)$$

Untuk membuktikan syarat keseimbangan secara global, Fungsi Potensial $\Phi(\mathbf{x})$ pada Persamaan (3) dan ekspansi risiko pada Persamaan (4) dijabarkan secara eksplisit untuk semesta empat aset. Penjabaran ini menunjukkan integrasi antara *return* kumulatif dan total risiko portofolio:
$$
\begin{aligned}
\Phi(\mathbf{x}) = &(\mu_A x_A + \mu_B x_B + \mu_C x_C + \mu_D x_D) \\
&- \frac{\gamma}{2} \Big[ (\sigma_{AA} x_A^2 + \sigma_{BB} x_B^2 + \sigma_{CC} x_C^2 + \sigma_{DD} x_D^2) \\
&+ 2(\sigma_{AB} x_A x_B + \sigma_{AC} x_A x_C + \sigma_{AD} x_A x_D \\
&+ \sigma_{BC} x_B x_C + \sigma_{BD} x_B x_D + \sigma_{CD} x_C x_D) \Big]
\end{aligned} \quad (10)
$$
secara umum, bentuknya akan menjadi
$$
\Phi (\mathbf{x})= x_i^T \mu_i - \frac{\gamma}{2} \left[x_i^T\sigma_{ii} x_i + \left(\sum_{i\neq j}x_i^T \sigma_{ij} x_j\right)\right]
$$

Perubahan potensial marginal $\Delta \Phi$ yang terjadi saat sebuah aset (misalnya aset $A$) mengubah statusnya dari keluar menjadi masuk portofolio ($x_A: 0 \rightarrow 1$) dapat dihitung dengan mengambil selisih nilai $\Phi$ pada kedua kondisi tersebut. Hasilnya menunjukkan kesamaan presisi dengan utilitas marginal individu pada Persamaan (5):
$$
\begin{aligned}
\Delta \Phi_A &= \Phi(x_A=1, \mathbf{x}_{-A}) - \Phi(x_A=0, \mathbf{x}_{-A}) \\
&= \mu_A - \frac{\gamma}{2} \sigma_{AA} - \gamma (\sigma_{AB} x_B + \sigma_{AC} x_C + \sigma_{AD} x_D)
\end{aligned} \quad (11)
$$
Hasil pada Persamaan (11) identik dengan isi dalam kurung pada fungsi utilitas $u_A$ (Persamaan 6), yang secara empiris memvalidasi bahwa sistem ini adalah sebuah *Exact Potential Game*.

## 3. Formulasi Hamiltonian Ising dari Model QUBO

Dalam implementasi pada algoritma kuantum seperti *Variational Quantum Eigensolver* (VQE), tujuan optimasi harus diubah dari maksimasi menjadi minimasi energi terendah (*Ground State*). Hamiltonian energi ($H$) didefinisikan sebagai negatif dari Fungsi Potensial, $H(\mathbf{x}) = -\Phi(\mathbf{x})$. Berdasarkan penurunan sebelumnya, bentuk fungsi energi dalam domain *Quadratic Unconstrained Binary Optimization* (QUBO) adalah:
$$H(\mathbf{x}) = \sum_{i=1}^N \left( \frac{\gamma}{2} \sigma_{ii} - \mu_i \right) x_i + \gamma \sum_{i < j} \sigma_{ij} x_i x_j \quad (12)$$
Variabel biner $x_i$ kemudian dipetakan ke variabel *spin* $s_i \in \{-1, 1\}$ menggunakan transformasi *affine* $x_i = (1 + s_i)/2$. Proses ini secara efektif mengubah domain keputusan diskrit menjadi representasi fisika sistem kuantum.

Transformasi tersebut menghasilkan parameter model Ising yang terdiri dari kopling antar *qubit* ($J_{ij}$) dan medan magnet lokal ($h_i$). Kekuatan kopling dirumuskan sebagai $J_{ij} = \frac{\gamma}{4} \sigma_{ij}$, sementara medan magnet lokal yang merepresentasikan bias individu setiap aset didefinisikan sebagai $h_i = \frac{1}{2} (\frac{\gamma}{2} \sigma_{ii} - \mu_i) + \frac{\gamma}{4} \sum \sigma_{ij}$. Hamiltonian kuantum final dinyatakan sebagai operator Pauli-Z ($\hat{Z}$) yang siap dioperasikan pada perangkat keras kuantum:
$$\hat{H}_{GT} = \sum_{i < j} J_{ij} (\hat{Z}_i \otimes \hat{Z}_j) + \sum_{i=1}^N h_i \hat{Z}_i \quad (13)$$

### 3.1. Penjabaran Eksplisit QUBO pada Sistem Empat Aset

Untuk memberikan pemahaman mendalam mengenai struktur energi sistem, Persamaan (12) dapat dijabarkan secara eksplisit dengan mensubstitusikan seluruh indeks aset ($A, B, C, D$). Penjabaran ini mengungkapkan bagaimana setiap suku linier dan kuadratik berkontribusi pada total energi Hamiltonian sistem. Suku-suku linier mencerminkan *bias* energi dari masing-masing aset berdasarkan profil *return-risk* mandirinya, sementara suku-suku kuadratik merepresentasikan korelasi antar aset yang harus diminimalkan untuk mencapai diversifikasi optimal.

Berdasarkan struktur sistem empat aset tersebut, penjabaran lengkap dari fungsi objektif $H(\mathbf{x})$ adalah sebagai berikut:
$$
\begin{aligned}
H(\mathbf{x}) = &\left( \frac{\gamma}{2} \sigma_{AA} - \mu_A \right) x_A + \left( \frac{\gamma}{2} \sigma_{BB} - \mu_B \right) x_B \\
& + \left( \frac{\gamma}{2} \sigma_{CC} - \mu_C \right) x_C + \left( \frac{\gamma}{2} \sigma_{DD} - \mu_D \right) x_D \\
& + \gamma (\sigma_{AB} x_A x_B + \sigma_{AC} x_A x_C + \sigma_{AD} x_A x_D) \\
& + \gamma (\sigma_{BC} x_B x_C + \sigma_{BD} x_B x_D + \sigma_{CD} x_C x_D)
\end{aligned} \quad (14)
$$
Melalui bentuk eksplisit pada Persamaan (14), terlihat jelas bahwa meminimalkan $H(\mathbf{x})$ setara dengan mencari konfigurasi biner $\mathbf{x}$ yang menyeimbangkan antara perolehan *return* (suku negatif $\mu_i$) dan pengurangan risiko varians serta kovariansi. Model QUBO ini merupakan jembatan matematis utama yang menghubungkan data finansial mentah dengan Hamiltonian Ising yang akan dieksekusi oleh algoritma VQE.

## 4. Implementasi Kendala Kardinalitas melalui Suku Penalti

Aplikasi praktis seringkali membutuhkan batasan jumlah aset yang dipilih, yang dikenal sebagai kendala kardinalitas $\sum x_i = K$. Kendala ini diintegrasikan ke dalam model melalui fungsi penalti kuadratik $P(\mathbf{x}) = \lambda (\sum x_i - K)^2$, di mana $\lambda$ merupakan faktor penalti bernilai besar. Penggunaan kuadrat memastikan bahwa setiap deviasi dari target $K$ akan meningkatkan energi sistem secara signifikan, memaksa algoritma untuk mematuhi batasan tersebut sebagai prioritas utama dalam pencarian solusi.

Ekspansi aljabar dari fungsi penalti ini dalam domain QUBO menghasilkan suku linier dan suku kuadratik tambahan yang harus digabungkan ke dalam Hamiltonian utama. Dengan memanfaatkan properti $(\sum x_i)^2 = \sum x_i + 2 \sum_{i < j} x_i x_j$, fungsi penalti secara umum didefinisikan sebagai:
$$P(\mathbf{x}) = \lambda (1 - 2K) \sum_{i=1}^N x_i + 2\lambda \sum_{i < j} x_i x_j + \lambda K^2 \quad (15)$$
Suku interaksi $2\lambda x_i x_j$ memberikan penalti pada pasangan aset yang menyala secara bersamaan, sementara suku linier memberikan kompensasi hingga batas $K$ tercapai. Mekanisme tarik-menarik antar suku ini secara matematis mengunci sistem pada keadaan di mana tepat $K$ aset terpilih dalam konfigurasi optimal.

### 4.1. Penjabaran Eksplisit Penalti pada Target Kardinalitas K=2

Dalam skenario pemilihan portofolio dengan target tepat dua aset ($K=2$) dari semesta empat aset ($N=4$), konstanta pengali pada suku linier berubah menjadi $(1 - 2(2)) = -3$. Penurunan ini memberikan "hadiah" energi negatif yang lebih kuat bagi setiap aset yang aktif untuk mengimbangi tekanan dari suku interaksi kuadratik. Konstanta penalti $\lambda K^2$ juga berubah menjadi $4\lambda$, yang berfungsi sebagai pergeseran energi dasar dalam spektrum Hamiltonian penalti tersebut.

Berdasarkan parameter $K=2$, penjabaran lengkap fungsi penalti $P(\mathbf{x})$ untuk aset $A, B, C, D$ dapat dituliskan sebagai berikut:
$$
\begin{aligned}
P(\mathbf{x}) = &\lambda (-3x_A - 3x_B - 3x_C - 3x_D) \\
& + 2\lambda (x_A x_B + x_A x_C + x_A x_D + x_B x_C + x_B x_D + x_C x_D) \\
& + 4\lambda
\end{aligned} \quad (16)
$$
Melalui Persamaan (16), terlihat bahwa konfigurasi dengan tepat dua variabel bernilai 1 akan menghasilkan nilai energi penalti terendah (nol). Sebagai contoh, jika $x_A=1$ dan $x_B=1$, maka $P(\mathbf{x}) = \lambda(-3-3) + 2\lambda(1) + 4\lambda = -6\lambda + 2\lambda + 4\lambda = 0$. Sebaliknya, jika hanya satu aset yang terpilih ($x_A=1$), energi penalti menjadi $\lambda(-3) + 4\lambda = \lambda > 0$, membuktikan efektivitas penalti kuadratik dalam mengunci jumlah aset.

## 5. Parameterisasi Final Hamiltonian Kuantum

Langkah terakhir dalam konstruksi model adalah mentransformasikan suku penalti ke dalam format Ising dan menjumlahkannya dengan parameter dari kerangka *Game Theory*. Melalui substitusi variabel *spin*, parameter penalti Ising diturunkan sebagai berikut:
$$J^{pen}_{ij} = \frac{\lambda}{2}, \quad h^{pen}_i = \frac{\lambda}{2} (N - 2K) \quad (17)$$
Parameter ini bersifat seragam dan memberikan tekanan struktural pada seluruh sistem *qubit* untuk mematuhi kendala kardinalitas secara global.

Integrasi total dari seluruh komponen menghasilkan parameter final yang akan menjadi input bagi algoritma VQE. Operator interaksi total dan medan lokal total didefinisikan sebagai penjumlahan dari komponen *Game Theory* dan penalti:
$$J^{total}_{ij} = \frac{\gamma}{4} \sigma_{ij} + \frac{\lambda}{2} \quad (18)$$
$$h^{total}_i = \left[ \frac{1}{2} \left( \frac{\gamma}{2} \sigma_{ii} - \mu_i \right) + \frac{\gamma}{4} \sum_{j \neq i} \sigma_{ij} \right] + \frac{\lambda}{2} (N - 2K) \quad (19)$$

Untuk memperjelas implementasi fisik pada sistem empat aset ($N=4$) dengan target kardinalitas $K=2$, parameter di atas dapat dieksplisitkan untuk masing-masing indeks. Sebagai contoh, medan magnet lokal total untuk aset $A$ dan kekuatan interaksi antara aset $A$ dan $B$ dirumuskan sebagai berikut:
$$h^{total}_A = \frac{1}{2} \left( \frac{\gamma}{2} \sigma_{AA} - \mu_A \right) + \frac{\gamma}{4} (\sigma_{AB} + \sigma_{AC} + \sigma_{AD}) + \frac{\lambda}{2} (4 - 2(2)) \quad (20)$$
$$J^{total}_{AB} = \frac{\gamma}{4} \sigma_{AB} + \frac{\lambda}{2} \quad (21)$$
Penurunan indeks serupa berlaku untuk aset $B, C,$ dan $D$ serta seluruh pasangan interaksi yang mungkin dalam sistem tersebut. Hamiltonian kuantum final $\hat{H}_{final} = \sum J^{total}_{ij} (\hat{Z}_i \otimes \hat{Z}_j) + \sum h^{total}_i \hat{Z}_i$ merepresentasikan sintesis lengkap antara teori portofolio, dinamika permainan, dan komputasi kuantum yang siap dijalankan pada infrastruktur VQE.
