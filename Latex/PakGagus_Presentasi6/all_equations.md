# Formalisme Matematika dalam Penentuan Harga Derivatif Finansial menggunakan Komputer Kuantum IBM

## I. Pendahuluan dan Faktor Volatilitas

Dalam konteks pemodelan dinamika suku bunga, kerangka kerja *Heath-Jarrow-Morton* (HJM) sangat bergantung pada spesifikasi faktor volatilitas untuk menangkap korelasi antar berbagai *forward rates*. Penentuan faktor-faktor ini secara akurat menjadi krusial karena volatilitas menentukan evolusi temporal dari kurva imbal hasil di bawah ukuran probabilitas *risk-neutral*. Melalui pendekatan statistik, faktor volatilitas ini dapat diekstraksi dari matriks kovarians data historis untuk memberikan representasi yang lebih efisien terhadap gangguan stokastik dalam pasar finansial.

Secara formal, faktor volatilitas $\bar{\sigma}_i$ untuk tenor $\tau_j$ dapat dinyatakan sebagai fungsi dari nilai eigen dan vektor eigen dari matriks kovarians. Representasi matematisnya adalah sebagai berikut:
$$\bar{\sigma}_i (\tau_j) = \sqrt{\lambda_i} (\vec{v}_i)_j \quad (1)$$
Di sini, $\lambda_i$ merepresentasikan nilai eigen ke-$i$ dan $(\vec{v}_i)_j$ adalah komponen ke-$j$ dari vektor eigen yang bersesuaian. Penggunaan dekomposisi ini memungkinkan reduksi dimensi melalui *Principal Component Analysis* (PCA), di mana hanya komponen utama dengan nilai eigen terbesar yang dipertahankan untuk meminimalkan kompleksitas komputasi tanpa mengorbankan akurasi model secara signifikan.

## II. Algoritma Quantum Principal Component Analysis (qPCA)

Implementasi algoritma *quantum Principal Component Analysis* (qPCA) pada sirkuit kuantum memerlukan representasi matriks densitas yang sesuai dengan matriks kovarians data finansial. Langkah awal melibatkan normalisasi matriks kovarians $\sigma_N$ agar memiliki *trace* bernilai satu, sehingga dapat dipetakan ke dalam status kuantum. Matriks densitas ini didefinisikan pada ruang Hilbert $\mathbb{R}^N \times \mathbb{R}^N$ dengan syarat normalisasi sebagai berikut:
$$\text{tr}[\sigma_N]=1 \quad (2)$$
Setelah normalisasi, operator uniter $U$ dikonstruksi untuk memfasilitasi evolusi waktu pada sistem kuantum. Operator ini sering kali dinyatakan dalam bentuk eksponensial matriks:
$$U = e^{it\sigma_N} \quad (3)$$

Dekomposisi spektral dari matriks $\sigma_N$ memberikan informasi fundamental mengenai struktur eigen dari sistem yang diamati. Matriks tersebut dapat diekspansi menjadi jumlahan dari proyeksi vektor eigen $\ket{u_j}$ yang dibobot oleh nilai eigen $\lambda_j$:
$$\sigma_N = \sum_{j=1}^{N} \lambda_j \ket{u_j} \bra{u_j} \quad (4)$$
di mana berlaku syarat $0 \le \lambda_j \le 1$ dan $\sum_{j=1}^N \lambda_j=1$. Dalam skenario praktis, kita sering kali melakukan aproksimasi menggunakan matriks rank rendah $\rho_r$ dengan $r \ll N$ untuk mengidentifikasi komponen yang paling dominan:
$$\rho_r = \sum_{j=1}^{r} \lambda_j \ket{u_j} \bra{u_j} \quad (5)$$

Untuk mengekstraksi nilai eigen menggunakan teknik *Quantum Phase Estimation* (QPE), sistem diinisialisasi pada status acak $\ket{b}$. Status ini merupakan superposisi dari basis eigen $\ket{u_j}$ dengan koefisien $\beta_j$ yang tidak diketahui secara apriori:
$$\ket{b} = \sum_{j=1}^N \beta_j \ket{u_j} \quad (6)$$
Setelah penerapan transformasi uniter dan *Quantum Fourier Transform* (QFT), keadaan sistem berubah menjadi keterikatan (*entanglement*) antara register nilai eigen dan register status eigen:
$$\ket{\psi_b} = \sum_{j=1}^N \beta_j \ket{\Lambda_j^{(n)}} \otimes \ket{u_j} \quad (7)$$
Di sini, $\ket{\Lambda_j^{(n)}}$ merepresentasikan estimasi biner $n$-bit dari nilai eigen ke-$j$, yang secara matematis dihubungkan dengan representasi fraksional:
$$\frac{1}{r} \approx \sum_{k=1}^n y_k 2^{-k} \quad (8)$$

Identifikasi vektor eigen yang bersesuaian dengan nilai eigen maksimum ($\lambda_{max}$) dilakukan melalui proyeksi pada register eigenvalue. Jika proyeksi dilakukan pada status biner $\bra{y^{(n)}}$, maka status sisa pada register kedua akan mendekati vektor eigen dominan:
$$\bra{y^{(n)}} \otimes \mathbb{1} \ket{\Psi_b} \approx \ket{u_{max}} \quad (9)$$
Dalam kondisi di mana resolusi bit terbatas, proyeksi mungkin menghasilkan superposisi dalam *subspace* berdimensi-$K$ yang berisi komponen-komponen yang tidak dapat dibedakan:
$$\bra{y^{(n)}} \otimes \mathbb{1} \ket{\Psi_b} \approx \sum_{j=1}^{K} \bar{\beta}_j \ket{u_j} \quad (10)$$
di mana $\bar{\beta}_j$ merupakan koefisien $\beta$ yang telah ternormalisasi di dalam *subspace* tersebut.

Karena ketidaktahuan *a priori* mengenai dimensi *subspace* (apakah $K > 1$), prosedur dapat diinisialisasi ulang menggunakan status acak yang berbeda $\ket{c}$ untuk memverifikasi keunikan vektor eigen yang diperoleh. Status acak baru ini didefinisikan sebagai:
$$\ket{c} = \sum_{j=1}^K \gamma_j \ket{u_j} \quad (11)$$
sehingga menghasilkan evolusi sistem pada ruang register sebagai berikut:
$$\ket{\Psi_c} = \sum_{j=1}^N \gamma_j \ket{\Lambda_j^{(n)}} \otimes \ket{u_j} \quad (12)$$
Setelah dilakukan proyeksi pada status $\ket{y^{(n)}}$, ekspektasi keadaan akhirnya akan menjadi bentuk superposisi yang berbeda, yang membantu dalam mendeteksi apakah vektor eigen yang dominan telah berhasil diisolasi:
$$\sum_{j=1}^L \tilde{\gamma}_j \ket{u_j} \quad (13)$$

## III. Analisis Hasil dan Metrik Performa

Validasi algoritma dilakukan dengan mengukur *fidelity* antara vektor eigen yang diperoleh dari sirkuit kuantum ($u_{QPE}$) dengan vektor eigen teoretis ($u_{max}$). Metrik ini memberikan kuantifikasi terhadap keberhasilan proses konvergensi dan dampak dari derau (*noise*) pada perangkat keras kuantum. Nilai *fidelity* didefinisikan melalui modulus kuadrat dari produk dalam kedua vektor tersebut:
$$F=|\langle u_{QPE}| u_{max}\rangle|^2 \quad (14)$$
Untuk sistem $2 \times 2$, inisialisasi sering kali menggunakan status superposisi merata sebagai *initial state* untuk memastikan eksplorasi ruang Hilbert yang komprehensif:
$$\ket{b_0} = \frac{1}{2}(\ket{00} + \ket{01} + \ket{10} + \ket{11}) \quad (15)$$

Estimasi nilai eigen maksimum $\Lambda_{max}$ dalam representasi biner $3$-bit memungkinkan penentuan parameter stokastik dengan presisi yang memadai untuk simulasi tingkat awal. Representasi biner ini dinyatakan sebagai:
$$\Lambda_{max} = 0.b_1b_2b_3 \quad (16)$$
Proses ini dilakukan secara iteratif, di mana keluaran dari satu iterasi digunakan sebagai *initial state* pada iterasi berikutnya untuk memperbaiki estimasi vektor eigen secara bertahap hingga mencapai kestabilan nilai.

## Lampiran A: Kerangka Kerja Heath-Jarrow-Morton (HJM)

Dalam model HJM, nilai dari akun pasar uang (*money market account*) pada waktu $t$ ditentukan oleh akumulasi dari *short rate* $r(s)$ secara kontinu. Akun ini berfungsi sebagai *numéraire* dasar dalam penilaian aset derivatif untuk memastikan konsistensi dalam perhitungan nilai sekarang. Definisi matematis dari nilai akun $B(t)$ adalah:
$$B(t) = \exp{\left( \int_0^t r(s)ds\right)} \quad (A1)$$
Hubungan antara harga obligasi *zero-coupon* $P(t,T)$ dan *short rate* di bawah ukuran *risk-neutral* $\mathbb{Q}_B$ diberikan oleh ekspektasi bersyarat dari kebalikan akun pasar uang:
$$P(t,T) = \mathbb{E}^{\mathbb{Q}_B} \left[ \left. \frac{B(t)}{B(T)} \right| \mathcal{F}_t \right] = \mathbb{E}^{\mathbb{Q}_B} \left[ \left. e^{-\int_t^T r(s)ds} \right| \mathcal{F}_t \right] \quad (A2)$$

Dinamika *forward rate* $f(t,T)$ secara intrinsik terikat dengan harga obligasi melalui derivatif logaritmik terhadap waktu jatuh tempo $T$. Selain itu, harga obligasi dapat dinyatakan kembali sebagai fungsi integral dari *forward rate* saat ini:
$$f(t,T) = -\frac{\partial}{\partial T} \log{P(t,T)} \quad (A3)$$
$$P(t,T) = e^{-\int_t^T f(t,s)ds} \quad (A4)$$
Transformasi ini memungkinkan kita untuk beralih dari pemodelan harga ke pemodelan tingkat suku bunga secara langsung, yang lebih intuitif dalam manajemen risiko portofolio pendapatan tetap.

Evolusi temporal dari harga obligasi *zero-coupon* dalam model HJM multifaktor mengikuti persamaan diferensial stokastik yang melibatkan drift dan komponen volatilitas difusif. Persamaan evolusi harga obligasi tersebut adalah:
$$dP(t, T) = P(t, T) \left\{r(t)dt + \sum_{i=1}^N \left(\int_t^T \sigma_i(t, s) ds \right) dW_i(t) \right\} \quad (A5)$$
Sedangkan dinamika untuk *forward rate* itu sendiri diberikan oleh:
$$df(t, T) = \alpha(t, T)dt + \sum_{i=1}^N \sigma_i(t, T) dW_i(t) \quad (A6)$$
dengan parameter *drift* $\alpha(t, T)$ yang memenuhi kondisi tanpa arbitrase:
$$\alpha(t, T) = \sum_{i=1}^N \sigma_i(t, T) \int_t^T \sigma_i(t, s)ds \quad (A7)$$

## Lampiran B: Estimasi Galat dan Rotasi Basis

Analisis galat pada komputer kuantum NISQ (*Noisy Intermediate-Scale Quantum*) sangat dipengaruhi oleh fidelitas gerbang dua-qubit. Galat total $\delta$ dapat diestimasi melalui akumulasi kontribusi galat dari setiap operasi uniter yang dilakukan. Rumus untuk mengestimasi galat total adalah:
$$\delta = \sum \frac{1 - \text{Fidelity}}{\text{jumlah gerbang dua-qubit}} \quad (B1)$$
di mana galat per gerbang didefinisikan secara spesifik sebagai:
$$\delta_{\text{two-qubit gate}} = \frac{1 - \text{Fidelity}}{\text{jumlah gerbang dua-qubit}} \quad (B2)$$

Untuk meningkatkan akurasi estimasi vektor eigen, pengukuran dilakukan pada berbagai basis melalui rotasi uniter. Penggunaan gerbang *Hadamard* memungkinkan transformasi ke basis diagonal, sedangkan operator rotasi arbiter $r$ digunakan untuk mengevaluasi fase relatif antar komponen:
$$\ket{+} = \frac{1}{\sqrt{2}} (\ket{0} + \ket{1}) \quad (B3)$$
Matriks rotasi arbiter $r$ untuk menentukan fase relatif didefinisikan sebagai:
$$r = \begin{pmatrix} \cos \alpha & -e^{i\beta} \sin \alpha \\ e^{i\beta} \sin \alpha & e^{i\gamma} \cos \alpha \end{pmatrix} \quad (B4)$$
Metode ini sangat efektif untuk memitigasi galat sistematis dan memastikan bahwa vektor eigen yang dihasilkan memiliki koherensi yang sesuai dengan target teoretis.
