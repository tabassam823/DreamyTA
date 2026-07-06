# Integrasi Game Theory dan Quantum Mutual Information dalam Optimasi Portofolio Ising

Dokumen ini menyajikan kerangka kerja komprehensif yang menggabungkan formalisme *Exact Potential Game* dengan *Quantum Mutual Information* (QMI) untuk mentransformasikan masalah seleksi portofolio Markowitz ke dalam Hamiltonian Ising yang siap dioptimasi menggunakan algoritma *Variational Quantum Eigensolver* (VQE).

## 1. Landasan Teoretis: Optimasi Portofolio Mean-Variance Markowitz
### 1.1. Formulasi Klasik Risiko dan Return
Dalam semesta pasar yang terdiri dari $N$ aset finansial, setiap aset $i \in \{1, \dots, N\}$ didefinisikan oleh variabel keputusan biner $x_i \in \{0, 1\}$, di mana vektor profil strategi dinyatakan sebagai $\mathbf{x} \in \mathbb{B}^N$. Optimasi portofolio klasik Markowitz bertujuan untuk meminimalkan risiko varians sistemik sembari mengoptimalkan ekspektasi imbal hasil melalui fungsi Lagrangian murni $\mathcal{L}_{pure}$:
$$\min_{\mathbf{x} \in \mathbb{B}^N} \mathcal{L}_{pure}(\mathbf{x}) = \mathbf{x}^T \Sigma \mathbf{x} - \lambda \mu^T \mathbf{x} \quad (1)$$
dengan parameter sebagai berikut:
*   $\mu = [\mu_1, \dots, \mu_N]^T \in \mathbb{R}^N$ adalah vektor ekspektasi *return*.
*   $\Sigma \in \mathbb{R}^{N \times N}$ adalah matriks kovariansi simetris positif semi-definit ($M \succeq 0$).
*   $\lambda \in \mathbb{R}^+$ adalah koefisien toleransi risiko.

> Definisi matematis parameter internal:
> *   $\mu_i = \mathbb{E}[R_{i,t}] = \frac{1}{T} \sum_{t=1}^T R_{i,t}$
> *   $\sigma_{ij} = \text{Cov}(R_i, R_j) = \mathbb{E}[(R_i - \mu_i)(R_j - \mu_j)]$

Sebagai inovasi dalam pemodelan adaptif, koefisien penghindaran risiko (*risk aversion*) $\gamma$ diformulasikan sebagai fungsi *sigmoid* yang bergantung pada rasio efisiensi aset ($\mu/\sigma$):
$$\gamma(\mu_i, \sigma_{ii}) = \frac{1}{1 + e^{-(\mu_i/\sqrt{\sigma_{ii}})}} \quad (2)$$
Integrasi antara ekspektasi linear dan penalti kuadratik tersebut menghasilkan fungsi objektif global yang dalam konteks *Game Theory* akan bertindak sebagai Fungsi Potensial $\Phi(\mathbf{x})$:
$$\Phi(\mathbf{x}) = \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j \quad (3)$$

### 1.2. Limitasi Komputasional dan Urgensi Transformasi
Permasalahan pada Persamaan (1) dan (3) diklasifikasikan sebagai *Quadratic Constrained Binary Optimization* yang bersifat *NP-Hard*. Secara formal, ruang pencarian solusi $\Omega$ memiliki kardinalitas $|\Omega| = 2^N$. Untuk sistem dengan $N$ yang besar, eksplorasi global menggunakan algoritma deterministik klasik mengalami hambatan eksponensial:
$$\mathcal{O}(2^N) \implies \lim_{N \to \infty} t_{comp} = \infty \quad (4)$$
Urgensi transformasi ke model *Ising* didasarkan pada pemetaan isomorfis antara variabel keputusan $\mathbf{x}$ dengan keadaan *spin* magnetik $s \in \{-1, 1\}^N$. Melalui pemanfaatan prinsip superposisi dan *quantum tunneling* pada algoritma kuantum, pencarian *Ground State* dari Hamiltonian sistem dapat dilakukan secara paralel dalam ruang Hilbert, memberikan potensi percepatan komputasi yang signifikan bagi optimasi finansial kompleks.


## 2. Formalisme Game Theory dalam Sistem Finansial
### 2.1. Representasi Aset sebagai Pemain Egoistis
Dalam kerangka kerja pasar terdesentralisasi, masalah seleksi portofolio dipetakan ke dalam model teori permainan non-kooperatif di mana setiap aset finansial dimodelkan sebagai agen otonom. Representasi ini mengasumsikan bahwa setiap pemain $i \in N$, dengan $N = \{1, \dots, N\}$, memiliki ruang strategi biner $X_i = \{0, 1\}$, di mana $x_i=1$ menandakan inklusi aset ke dalam portofolio dan $x_i=0$ menandakan eksklusi. Interaksi kolektif dari para agen ini membentuk profil strategi $\mathbf{x} = (x_1, \dots, x_N) \in \mathbb{B}^N$, yang secara fundamental menentukan lanskap risiko dan imbal hasil pasar global. Dengan memberikan *agency* pada aset individual, model ini menangkap kompetisi intrinsik dan sinergi antar instrumen finansial yang berbeda secara lebih granular.

Perilaku setiap aset diatur oleh prinsip maksimasi utilitas egoistis, di mana keputusan diambil berdasarkan lingkungan lokal yang didefinisikan oleh strategi pemain lain $\mathbf{x}_{-i} = (x_1, \dots, x_{i-1}, x_{i+1}, \dots, x_N)$. Dalam paradigma ini, aset $i$ berusaha mengoptimalkan *payoff* individunya sendiri tanpa pertimbangan langsung terhadap objektif global, mencerminkan sifat desentralisasi dari partisipan pasar. Permainan ini secara formal didefinisikan oleh tripel $\mathcal{G} = (N, \{X_i\}_{i \in N}, \{u_i\}_{i \in N})$, di mana $\{u_i\}$ adalah himpunan fungsi utilitas yang akan diturunkan. Pergeseran dari optimasi terpusat ke dinamika multi-agen memungkinkan analisis mengenai bagaimana aset spesifik berkontribusi terhadap stabilitas sistemik dan mencapai keseimbangan melalui interaksi strategis.

### 2.2. Konstruksi Fungsi Utilitas Individual ($u_i$)
Fungsi utilitas individual $u_i$ dikonstruksi untuk mencerminkan manfaat marginal bersih yang diterima suatu aset dari partisipasinya dalam portofolio. Formulasi ini mengintegrasikan ekspektasi *return* $\mu_i$ sebagai insentif utama, yang selanjutnya dipenalti oleh volatilitas internal dan korelasi eksternal. Secara spesifik, utilitas mempertimbangkan varians mandiri aset $\sigma_{ii}$ dan kovariansi dengan aset lain $j$ yang berstatus aktif ($x_j=1$). Struktur ini memastikan bahwa *payoff* sangat sensitif terhadap komposisi portofolio saat ini, menciptakan loop umpan balik dinamis antara pilihan individual dan risiko kolektif.

Secara matematis, utilitas untuk pemain $i$ yang diberikan strategi pemain lain $\mathbf{x}_{-i}$ dirumuskan sebagai ekspresi linier-kuadratik dari variabel keputusan biner. Jika aset memilih untuk berada di luar portofolio ($x_i=0$), maka utilitas yang diperoleh adalah nol, $u_i(0, \mathbf{x}_{-i}) = 0$. Sebaliknya, jika $x_i=1$, aset tersebut memperoleh imbal hasil namun menyerap penalti risiko yang dibobot oleh parameter *risk aversion* $\gamma$. Formulasi formal untuk fungsi utilitas adalah sebagai berikut:
$$u_i(x_i, \mathbf{x}_{-i}) = x_i \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \right) \quad (5)$$
dengan parameter sebagai berikut:
*   $u_i: \mathbb{B}^N \to \mathbb{R}$ adalah fungsi utilitas pemain $i$.
*   $\gamma \in \mathbb{R}^+$ adalah koefisien penalti risiko sesuai Persamaan (2).

> Detail komponen utilitas:
> *   $x_i \mu_i$ : Kontribusi *return* linier.
> *   $x_i (\frac{\gamma}{2} \sigma_{ii})$ : Penalti varians internal (*self-interaction*).
> *   $x_i (\gamma \sum_{j \neq i} \sigma_{ij} x_j)$ : Penalti kovariansi sistemik (*pairwise interaction*).


## 3. Karakterisasi Exact Potential Game dan Stabilitas Nash
### 3.1. Derivasi Fungsi Potensial Global ($\Phi$)
Sebuah permainan strategis $\mathcal{G}$ diklasifikasikan sebagai *Exact Potential Game* jika terdapat fungsi potensial $\Phi: \mathbb{B}^N \to \mathbb{R}$ sedemikian rupa sehingga perubahan utilitas setiap pemain $i$ akibat perubahan strategi unilateral secara presisi direfleksikan oleh perubahan nilai $\Phi$. Dalam konteks seleksi portofolio, fungsi potensial global didefinisikan sebagai representasi akumulatif dari imbal hasil dan risiko sistemik:
$$\Phi(\mathbf{x}) = \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j \quad (6)$$
Untuk membuktikan properti potensial, suku kuadratik pada Persamaan (6) dijabarkan menjadi komponen varians diagonal dan kovariansi *off-diagonal*:
$$\sum_{i,j} \sigma_{ij} x_i x_j = \sum_{i=1}^N \sigma_{ii} x_i^2 + 2 \sum_{i < j} \sigma_{ij} x_i x_j \quad (7)$$

> Identitas Matematis Variabel Biner:
> *   $\forall x_i \in \{0, 1\} \implies x_i^2 = x_i$ (Sifat *Idempotensi*).
> *   $\sigma_{ij} = \sigma_{ji}$ (Simetri Matriks Kovariansi).

Substitusi sifat idempotensi ke dalam Persamaan (6) menghasilkan bentuk potensial tereduksi yang memisahkan kontribusi linier dan interaksi antar-pemain:
$$\Phi(\mathbf{x}) = \sum_{i=1}^N \left( \mu_i - \frac{\gamma}{2} \sigma_{ii} \right) x_i - \gamma \sum_{i < j} \sigma_{ij} x_i x_j \quad (8)$$
Perubahan potensial marginal $\Delta \Phi_i$ saat pemain $i$ beralih dari $x_i = 0$ ke $x_i = 1$ dihitung melalui operator selisih:
$$\Delta \Phi_i = \Phi(1, \mathbf{x}_{-i}) - \Phi(0, \mathbf{x}_{-i}) = \mu_i - \frac{\gamma}{2} \sigma_{ii} - \gamma \sum_{j \neq i} \sigma_{ij} x_j \quad (9)$$
Hasil pada Persamaan (9) terbukti identik dengan ekspansi utilitas marginal individu $u_i$ pada Persamaan (5). Karena $\Delta \Phi_i = \Delta u_i$ untuk setiap pemain dan setiap transisi strategi, maka sistem ini secara formal tervalidasi sebagai *Exact Potential Game*.

### 3.2. Pembuktian Nash Equilibrium (NE)
Dalam kerangka *Potential Game*, keberadaan *Pure Strategy Nash Equilibrium* (PSNE) dijamin melalui eksistensi ekstremum lokal dari fungsi potensial. Profil strategi $\mathbf{x}^* \in \mathbb{B}^N$ didefinisikan sebagai Nash Equilibrium jika tidak ada pemain $i$ yang dapat meningkatkan utilitasnya melalui deviasi unilateral:
$$u_i(x_i^*, \mathbf{x}_{-i}^*) \geq u_i(x_i, \mathbf{x}_{-i}^*) \quad \forall x_i \in X_i, \forall i \in N \quad (10)$$
Secara formal, hubungan antara fungsi potensial dan keseimbangan Nash dinyatakan dalam teorema berikut: setiap titik yang merupakan lokal maksimum dari fungsi $\Phi(\mathbf{x})$ dalam ruang diskrit $\mathbb{B}^N$ adalah PSNE dari permainan $\mathcal{G}$.

Bukti formal didasarkan pada sifat $\Delta u_i = \Delta \Phi_i$. Jika $\mathbf{x}^*$ adalah maksimum lokal dari $\Phi$, maka untuk setiap perubahan strategi $x_i^* \to x_i$, berlaku:
$$\Phi(x_i^*, \mathbf{x}_{-i}^*) - \Phi(x_i, \mathbf{x}_{-i}^*) \geq 0 \quad (11)$$
Karena perubahan potensial identik dengan perubahan utilitas, maka:
$$u_i(x_i^*, \mathbf{x}_{-i}^*) - u_i(x_i, \mathbf{x}_{-i}^*) \geq 0 \implies u_i(x_i^*, \mathbf{x}_{-i}^*) \geq u_i(x_i, \mathbf{x}_{-i}^*) \quad (12)$$
Konsekuensi matematis ini memastikan bahwa optimasi global pada Hamiltonian (yang merepresentasikan $-\Phi$) akan selalu konvergen pada konfigurasi yang stabil secara strategis. Dengan demikian, *Ground State* dari sistem Ising bukan hanya solusi optimal bagi Markowitz, tetapi juga merupakan titik keseimbangan stabil di mana dinamika egoistis antar aset mencapai konsensus risiko-imbal hasil yang minimum.


## 4. Integrasi Quantum Mutual Information (QMI) dan Dinamika Strategi
### 4.1. Probabilitas Strategi Biner Up/Down
Untuk menangkap dinamika mikro-struktural pasar, setiap aset $i$ diasumsikan memiliki profil strategi biner $S_{i,t} \in \{u, d\}$ pada setiap titik waktu $t$. Strategi ini ditentukan oleh pergerakan harga relatif antara harga penutupan (*Close*) dan harga pembukaan (*Open*). Selama jendela observasi $T$, perilaku strategis aset diringkas dalam distribusi probabilitas marginal $P(S_i)$.

> Definisi Formal Strategi Biner:
> *   $S_{i,t} = u$ (Up) jika $C_{i,t} > O_{i,t}$
> *   $S_{i,t} = d$ (Down) jika $C_{i,t} \le O_{i,t}$
> *   Probabilitas Marginal: $P(S_i = s) = \frac{1}{T} \sum_{t=1}^T \mathbb{I}(S_{i,t} = s), \quad s \in \{u, d\}$

Ekspektasi imbal hasil $\mu_i$ pada Persamaan (3) diredefinisi menjadi ekspektasi strategis $\tilde{\mu}_i$ yang membobot imbal hasil kondisional terhadap probabilitas terjadinya strategi $u$ atau $d$. Hal ini memungkinkan model untuk membedakan antara aset yang memiliki *return* tinggi akibat volatilitas ekstrem dengan aset yang memiliki konsistensi strategi positif:
$$\tilde{\mu}_i = \sum_{s \in \{u,d\}} P(S_i = s) \mu_{i,s} \quad (13)$$
di mana $\mu_{i,s}$ adalah *conditional expected return* aset $i$ saat strategi $s$ teramati. Parameter ini memberikan landasan bagi Fungsi Potensial untuk mengevaluasi stabilitas keuntungan berdasarkan perilaku historis yang lebih granular.

### 4.2. Redefinisi Interaksi melalui Keterikatan Informasi
Interaksi antar aset dalam matriks kovariansi $\Sigma$ seringkali gagal menangkap ketergantungan non-linear dan sinkronisasi informasional yang kompleks. Oleh karena itu, elemen interaksi $\sigma_{ij}$ diperluas menggunakan *Quantum Mutual Information* (QMI) yang dilambangkan dengan $I(i:j)$. QMI mengukur jumlah informasi yang dibagikan antar dua aset dalam ruang Hilbert, yang dalam konteks ini dipetakan dari entropi distribusi strategi bersama.

Elemen kovariansi yang diperkaya ($\tilde{\sigma}_{ij}$) dirumuskan sebagai modifikasi dari kovariansi standar dengan faktor penalti informasional:
$$\tilde{\sigma}_{ij} = \sigma_{ij} [1 + \xi I(i:j)] \quad (14)$$
dengan parameter sebagai berikut:
*   $I(i:j) = H(i) + H(j) - H(i, j)$ adalah Mutual Information.
*   $H(\cdot)$ adalah entropi (Shannon atau Von Neumann) dari distribusi strategi.
*   $\xi \in \mathbb{R}^+$ adalah koefisien kopling informasi.

> Interpretasi Fisik Penalti QMI:
> *   Jika $I(i:j)$ tinggi, kedua aset memiliki keterikatan informasi yang kuat (sinkron).
> *   Penalti $\xi I(i:j)$ akan meningkatkan nilai risiko efektif $\tilde{\sigma}_{ij}$.
> *   Dalam minimasi Hamiltonian, sistem akan cenderung menghindari pemilihan pasangan aset dengan QMI tinggi untuk mencapai diversifikasi informasional yang optimal.

Dengan mensubstitusikan $\tilde{\mu}_i$ dan $\tilde{\sigma}_{ij}$ ke dalam Persamaan (8), Fungsi Potensial yang telah diperkaya secara strategis dan informasional menjadi:
$$\Phi_{enriched}(\mathbf{x}) = \sum_{i=1}^N \left( \tilde{\mu}_i - \frac{\gamma}{2} \sigma_{ii} \right) x_i - \gamma \sum_{i < j} \tilde{\sigma}_{ij} x_i x_j \quad (15)$$


## 5. Pemetaan ke Domain Quadratic Unconstrained Binary Optimization (QUBO)
### 5.1. Formulasi Pure QUBO
Transisi dari kerangka kerja *Potential Game* ke komputasi kuantum memerlukan restrukturisasi fungsi objektif dari maksimasi potensial menjadi minimasi energi biaya. Masalah *Quadratic Unconstrained Binary Optimization* (QUBO) didefinisikan sebagai pencarian vektor biner $\mathbf{x}^*$ yang meminimalkan fungsi kuadratik dalam ruang diskrit $\mathbb{B}^N$. Secara formal, biaya murni (*pure cost*) diturunkan sebagai negatif dari Fungsi Potensial yang telah diperkaya pada Persamaan (15):
$$H_{pure}(\mathbf{x}) = -\Phi_{enriched}(\mathbf{x}) = \sum_{i=1}^N \left( \frac{\gamma}{2} \sigma_{ii} - \tilde{\mu}_i \right) x_i + \gamma \sum_{i < j} \tilde{\sigma}_{ij} x_i x_j \quad (16)$$

Dalam representasi matriks, fungsi ini dinyatakan dalam bentuk kuadratik $\mathbf{x}^T Q \mathbf{x}$, di mana $Q \in \mathbb{R}^{N \times N}$ adalah matriks QUBO simetris. Dengan memanfaatkan sifat idempotensi $x_i^2 = x_i$, koefisien linier pada Persamaan (16) dipetakan langsung ke elemen diagonal matriks $Q$:
$$Q_{ii} = \frac{\gamma}{2} \sigma_{ii} - \tilde{\mu}_i, \quad Q_{ij} = \frac{\gamma}{2} \tilde{\sigma}_{ij} \quad (17)$$

> Karakteristik Struktur Matriks $Q$:
> *   Elemen Diagonal ($Q_{ii}$): Merepresentasikan bias energi individu yang ditentukan oleh rasio *return-risk* strategis.
> *   Elemen Off-Diagonal ($Q_{ij}$): Merepresentasikan kekuatan interaksi antar aset yang berfungsi sebagai penalti diversifikasi informasional.

### 5.2. Inkorporasi Kendala Kardinalitas melalui Suku Penalti
Dalam aplikasi finansial nyata, portofolio seringkali dibatasi oleh jumlah aset yang dapat dikelola, yang dinyatakan melalui kendala kardinalitas $\sum x_i = K$. Untuk mempertahankan format tanpa kendala (*unconstrained*) pada QUBO, batasan ini diintegrasikan melalui fungsi penalti kuadratik $P(\mathbf{x})$ yang memberikan biaya energi tinggi pada setiap deviasi dari target $K$:
$$P(\mathbf{x}) = \lambda \left( \sum_{i=1}^N x_i - K \right)^2 \quad (18)$$
di mana $\lambda \in \mathbb{R}^+$ adalah pengali Lagrange (*penalty factor*) yang besarnya harus melampaui rentang nilai pada biaya murni guna menjamin kepatuhan kendala. Ekspansi aljabar dari Persamaan (18) menghasilkan:
$$P(\mathbf{x}) = \lambda \left[ \sum_{i=1}^N x_i^2 + 2\sum_{i < j} x_i x_j - 2K \sum_{i=1}^N x_i + K^2 \right] \quad (19)$$

Dengan mensubstitusikan kembali sifat $x_i^2 = x_i$, fungsi penalti dikonsolidasikan ke dalam format QUBO standar:
$$P(\mathbf{x}) = \lambda (1 - 2K) \sum_{i=1}^N x_i + 2\lambda \sum_{i < j} x_i x_j + \text{const} \quad (20)$$
Hamiltonian QUBO total ($H_{total}$) diperoleh melalui superposisi linier antara biaya murni dan fungsi penalti, $H_{total} = H_{pure} + P(\mathbf{x})$. Parameter matriks QUBO akhir ($Q^{total}$) yang menyatukan seluruh komponen sistem didefinisikan sebagai:
$$Q_{ii}^{total} = \left( \frac{\gamma}{2} \sigma_{ii} - \tilde{\mu}_i \right) + \lambda(1 - 2K) \quad (21)$$
$$Q_{ij}^{total} = \gamma \tilde{\sigma}_{ij} + 2\lambda \quad (22)$$


## 6. Derivasi Hamiltonian Ising dan Operator Kuantum
### 6.1. Transformasi Affine ke Variabel Spin
Untuk mengimplementasikan model pada prosesor kuantum atau algoritma berbasis sirkuit seperti VQE, variabel biner $x_i \in \{0, 1\}$ harus dipetakan ke dalam variabel *spin* Ising $s_i \in \{-1, 1\}$. Transformasi ini dilakukan melalui pemetaan *affine* yang menghubungkan domain keputusan biner dengan nilai *eigen* dari operator Pauli-Z ($\hat{Z}$). Sesuai dengan konvensi komputasi kuantum standar, nilai $x_i=1$ (aset terpilih) dipetakan ke status $|1\rangle$ dengan nilai *eigen* $-1$, sedangkan $x_i=0$ dipetakan ke status $|0\rangle$ dengan nilai *eigen* $+1$. Secara matematis, transformasi ini dinyatakan sebagai:
$$x_i \mapsto \frac{1 - \hat{Z}_i}{2} \quad (23)$$
Substitusi operator ini ke dalam fungsi objektif QUBO pada Persamaan (16) dan (20) akan mengubah lanskap energi biner menjadi operator Hamiltonian kuantum. Proses ini menyebabkan munculnya interaksi antar-qubit ($J_{ij}$) yang merepresentasikan korelasi strategis dan medan magnet lokal ($h_i$) yang merepresentasikan bias individu setiap aset. Konstanta energi yang muncul dari ekspansi aljabar dapat diabaikan dalam proses optimasi karena tidak mengubah lokasi *Ground State*.

### 6.2. Ekstraksi Parameter Kopling ($J_{ij}$) dan Medan Lokal ($h_i$)
Hamiltonian Ising final dirumuskan sebagai operator linier dalam ruang Hilbert $N$-qubit, yang terdiri dari jumlahan interaksi *pairwise* dan medan *transverse*. Berdasarkan substitusi Persamaan (23) ke dalam profil energi total $H_{total}$, parameter fisik Hamiltonian didefinisikan melalui koefisien matriks QUBO $Q^{total}$. Kekuatan kopling antar-qubit $J_{ij}$ diturunkan dari elemen *off-diagonal* yang mencakup penalti interaksi dan QMI, sementara medan lokal $h_i$ merupakan akumulasi dari kontribusi diagonal dan normalisasi interaksi.

Secara formal, parameter Hamiltonian Ising total didefinisikan sebagai:
$$J_{ij}^{total} = \frac{Q_{ij}^{total}}{4} = \frac{\gamma \tilde{\sigma}_{ij} + 2\lambda}{4} \quad (24)$$
$$h_i^{total} = -\frac{Q_{ii}^{total}}{2} - \sum_{j \neq i} \frac{Q_{ij}^{total}}{4} \quad (25)$$
dengan substitusi nilai $Q_{ii}^{total}$ dari Persamaan (21) dan (22), diperoleh ekspresi eksplisit:
$$h_i^{total} = -\frac{1}{2} \left[ \left( \frac{\gamma}{2} \sigma_{ii} - \tilde{\mu}_i \right) + \lambda(1 - 2K) \right] - \sum_{j \neq i} \frac{\gamma \tilde{\sigma}_{ij} + 2\lambda}{4} \quad (26)$$
Hamiltonian kuantum final $\hat{H}_{Ising}$ yang akan dieksekusi pada algoritma VQE dinyatakan sebagai:
$$\hat{H}_{Ising} = \sum_{i < j} J_{ij}^{total} (\hat{Z}_i \otimes \hat{Z}_j) + \sum_{i=1}^N h_i^{total} \hat{Z}_i \quad (27)$$
Operator pada Persamaan (27) menyatukan seluruh dimensi riset: utilitas *Game Theory*, diversifikasi QMI, dan kendala kardinalitas ke dalam satu operator energi tunggal yang keadaan dasarnya (*Ground State*) merupakan solusi portofolio optimal.


## 7. Optimasi melalui Variational Quantum Eigensolver (VQE)
### 7.1. Evolusi State dan Pencarian Ground State
Algoritma *Variational Quantum Eigensolver* (VQE) merupakan metode hibrida kuantum-klasik yang dirancang untuk mengestimasi nilai *eigen* terendah dari operator Hamiltonian $\hat{H}_{Ising}$. Proses optimasi didasarkan pada prinsip variasional dalam mekanika kuantum, yang menyatakan bahwa nilai ekspektasi energi dari setiap *trial state* $|\psi(\theta)\rangle$ akan selalu lebih besar atau sama dengan energi keadaan dasar $E_0$. Status kuantum diparameterisasi menggunakan sirkuit kuantum (*ansatz*) $U(\theta)$, di mana $\theta$ adalah vektor parameter klasik yang diatur secara iteratif:
$$|\psi(\theta)\rangle = U(\theta) |0\rangle^{\otimes N} \quad (28)$$
Fungsi biaya yang diminimalkan oleh pengoptimal klasik didefinisikan sebagai nilai ekspektasi Hamiltonian terhadap *state* yang berevolusi:
$$E(\theta) = \langle \psi(\theta) | \hat{H}_{Ising} | \psi(\theta) \rangle \quad (29)$$

Pencarian *Ground State* dilakukan melalui loop optimasi hibrida, di mana perangkat keras kuantum bertugas menghitung $E(\theta)$ melalui pengukuran berulang pada basis komputasi, sementara rutin klasik (seperti COBYLA atau SPSA) memperbarui parameter $\theta$ untuk menurunkan energi sistem. Konvergensi algoritma tercapai ketika sistem mencapai titik stasioner $\theta^*$, di mana $|\psi(\theta^*)\rangle$ merepresentasikan aproksimasi terbaik bagi *eigenstate* energi terendah. Dalam konteks ruang Hilbert $2^N$, VQE memungkinkan eksplorasi efisien terhadap lanskap energi yang kompleks, menghindari jebakan minimum lokal melalui pemanfaatan efek interferensi kuantum.

### 7.2. Interpretasi Solusi dan Validasi Finansial
Setelah konvergensi tercapai, pengukuran akhir pada sirkuit optimal $|\psi(\theta^*)\rangle$ memberikan distribusi probabilitas atas profil strategi biner $\mathbf{x} \in \mathbb{B}^N$. *State* dengan probabilitas tertinggi berkorespondensi dengan konfigurasi portofolio yang memiliki energi terendah, yang secara matematis identik dengan profil strategi yang memaksimalkan Fungsi Potensial diperkaya $\Phi_{enriched}$. Berdasarkan teorema pada Bagian 3.2, solusi ini secara fundamental merupakan *Pure Strategy Nash Equilibrium* (PSNE) dari sistem finansial yang dimodelkan. Dengan demikian, portofolio yang terpilih tidak hanya optimal dalam paradigma Markowitz, tetapi juga stabil terhadap deviasi strategis unilateral oleh aset manapun.

Interpretasi finansial dari solusi VQE mencakup validasi terhadap kepatuhan kendala kardinalitas dan diversifikasi informasional. Keberadaan penalti $\lambda$ memastikan bahwa *Ground State* yang ditemukan berada pada sub-ruang dengan tepat $K$ aset yang aktif. Lebih lanjut, integrasi QMI dalam parameter $J_{ij}$ menjamin bahwa aset yang dipilih memiliki tingkat sinkronisasi informasi yang rendah, sehingga meningkatkan resiliensi portofolio terhadap guncangan pasar sistemik. Hasil akhir ini memberikan sintesis antara presisi matematis *Game Theory*, kedalaman analisis informasi kuantum, dan efisiensi komputasi *Variational Quantum Algorithms*, yang secara kolektif mendefinisikan standar baru dalam optimasi portofolio kuantum modern.

