# Bab 2: Tinjauan Pustaka dan Dasar Teori

## 2.1 Formalisme Mekanika Kuantum untuk Pemodelan Informasi
Untuk membangun fondasi matematis yang diperlukan di dalam konsep Teori Permainan Kuantum dan Komputasi Kuantum, diberikan beberapa poin untuk memperdalam konsep yang linear dengan kosnsep utama **Fisika Kuantum** dan **Fisika Matematika**.

### 2.1.1 Ruang Hilbert, Superposisi, dan Sistem Qubit vs Qutrit

Dalam upaya **prediksi pasar saham secara *real-time*** (Bakshi & Srinivasan, 2025), kita dihadapkan pada dinamika pasar yang sangat kompleks, seperti fluktuasi indeks S&P500. Data pasar yang kaya ini menuntut representasi informasi yang padat. Namun, penggunaan sistem biner klasik atau bahkan sistem kuantum dua-level (**qubit**) sering kali mengalami keterbatasan. Keterbatasan utama muncul dari *discretization error* saat merepresentasikan data kontinu, menyebabkan hilangnya informasi signifikan.

Fenomena ini bisa dianalogikan sebagaimana pada kasus **Quantum Penny-Flip Game** (Meyer, 1999), di mana pemain klasik terhambat oleh strategi biner (membalik atau tidak membalik koin), sedangkan pemain kuantum meraih kemenangan dengan memanfaatkan ruang keadaan yang lebih luas melalui superposisi. Dalam konteks *financial forecasting*, untuk mengatasi keterbatasan representasi ini dan menangkap korelasi pasar yang kompleks dengan efisiensi komputasi yang lebih tinggi, kita membutuhkan kapasitas pemrosesan informasi yang lebih besar.

Solusi yang relevan adalah perluasan ruang keadaan dari qubit ke **qutrit** (sistem tiga-level). Qutrit menawarkan kepadatan informasi yang lebih tinggi ($\log_2 3 \approx 1.585$ bit per qutrit) dan fleksibilitas topologi sirkuit yang lebih baik dibandingkan jaringan saraf berbasis qubit (QQBN). Transisi ke qutrit ini merupakan langkah fundamental yang kompleks untuk meningkatkan kapasitas pemrosesan informasi dalam aplikasi keuangan tingkat lanjut.

Secara formal, sistem kuantum dijelaskan dalam ruang vektor kompleks yang dilengkapi dengan *inner product*, dikenal sebagai **Ruang Hilbert** ($\mathcal{H}$). Unit dasar informasi kuantum standar adalah **qubit**, dengan basis ortonormal $\{|0\rangle, |1\rangle\}$. State umum qubit dinyatakan sebagai:

$$ |\psi\rangle = \alpha|0\rangle + \beta|1\rangle $$

di mana $\alpha, \beta \in \mathbb{C}$ memenuhi $|\alpha|^2 + |\beta|^2 = 1$.

Selanjutnya, untuk sistem qutrit, yang beroperasi dalam ruang Hilbert tiga dimensi dengan basis komputasi $\{|0\rangle, |1\rangle, |2\rangle\}$, state superposisi qutrit dituliskan secara matematis sebagai:

$$ |\phi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle $$

dengan syarat normalisasi $\sum_{i=0}^2 |c_i|^2 = 1$.
### 2.1.2 Formalisme Teori Permainan Klasik

Sebelum membahas perluasan ke ranah kuantum, terdapat konsep penting yang perlu dibahas, yaitu mendefinisikan kerangka kerja teori permainan klasik secara formal. Sebuah permainan strategi murni dengan $n$-pemain didefinisikan oleh *tuple* ruang strategi $\mathcal{S}$ dan fungsi *payoff* $\pi$:

$$ \mathcal{S} = (S_1, S_2, \dots, S_n) $$

$$ \pi = (\pi_1, \pi_2, \dots, \pi_n) $$

di mana $S_i = \{s_i^1, s_i^2, \dots \}$ adalah himpunan strategi murni pemain ke-$i$. Secara umum, permainan dalam bentuk normal (*normal form*) dinyatakan sebagai *ordered triple* $(N, (S_i)_{i \in N}, (u_i)_{i \in N})$ di mana $N$ adalah himpunan pemain dan $u_i$ adalah fungsi *payoff* atau utilitas pemain $i$.

Solusi utama dalam teori permainan adalah **Nash Equilibrium**. Vektor strategi $s^* = (s_1^*, \dots, s_n^*)$ merupakan Nash Equilibrium jika tidak ada pemain yang dapat meningkatkan *payoff*-nya dengan mengubah strategi secara sepihak:

$$ u_i(s^*) \geq u_i(s_i, s^*_{-i}) \quad \forall s_i \in S_i, \forall i \in N $$

Dalam notasi matriks, hal ini berarti:

$$ \pi_i(s_1^*, \dots, s_i^*, \dots, s_n^*) \geq \pi_i(s_1^*, \dots, s_i, \dots, s_n^*) $$

Konsep lain yang relevan adalah **Pareto Optimality**. Sebuah keadaan permainan $\mathcal{P}$ dikatakan mendominasi $\mathcal{P}'$ secara Pareto jika $\pi_i(\mathcal{P}) \geq \pi_i(\mathcal{P}')$ untuk semua pemain, dengan pertidaksamaan ketat berlaku setidaknya untuk satu pemain.

Dalam aplikasi ekonomi makro seperti **Barro-Gordon Game** (Lowe, 2024), fungsi utilitas pembuat kebijakan ($U^{pol}$) sering dimodelkan sebagai fungsi dari inflasi ($\pi_t$) dan ekspektasi inflasi ($\pi_t^e$):

$$ U^{pol}_t = \theta b (\pi_t - \pi_t^e) - \frac{a \pi_t^2}{2} $$

Definisi-definisi klasik ini menjadi landasan untuk memahami bagaimana protokol kuantum memperluas ruang strategi dan keseimbangan yang dapat dicapai.

### 2.1.3 Formalisme Matriks Densitas

Dalam realitas pasar finansial, investor jarang memiliki informasi sempurna mengenai keadaan pasar. Pasar sering kali dipenuhi oleh *noise* dan ketidakpastian yang membuat representasi sistem sebagai vektor keadaan murni (*pure state*) $|\psi\rangle$ menjadi tidak realistis. Keadaan pasar lebih tepat digambarkan sebagai ansambel statistik dari berbagai kemungkinan keadaan, atau yang dikenal sebagai *mixed state*.

Untuk mengakomodasi ketidakpastian intrinsik ini secara matematis, kita menggunakan **Matriks Densitas** ($\rho$). Formalisme ini memungkinkan kita untuk mendeskripsikan sistem di mana kita hanya mengetahui probabilitas $p_i$ bahwa sistem berada dalam keadaan kuantum tertentu $|\psi_i\rangle$. Definisi formalnya adalah:

$$ \rho = \sum_i p_i |\psi_i\rangle\langle\psi_i| $$

dengan syarat normalisasi $\text{Tr}(\rho) = 1$. Dalam konteks ini, elemen non-diagonal (koherensi) merepresentasikan superposisi kuantum yang dapat dimanfaatkan untuk keuntungan strategis, sementara elemen diagonal merepresentasikan probabilitas klasik. Evolusi sistem pasar yang dimodelkan ini kemudian mengikuti persamaan uniter $\rho_f = U \rho U^\dagger$, yang menjaga total probabilitas tetap satu.

### 2.1.4 Protokol Kuantisasi Permainan

Untuk mengkuantisasi permainan klasik, berbagai protokol telah dikembangkan untuk memetakan elemen-elemen permainan klasik ke dalam domain kuantum. Proses umum dari protokol tersebut melibatkan beberapa tahapan:

1.  **Sistem Kuantum**: Ruang strategi dan *payoff* pemain klasik dipetakan ke dalam operator dan state dalam ruang Hilbert.
2.  **State Awal**: Permainan dimulai dengan state kuantum awal, seringkali merupakan state terjerat (*entangled*) untuk mengeksploitasi fitur kuantum.
3.  **Strategi Pemain**: Strategi pemain direpresentasikan oleh operator uniter yang bekerja pada state kuantum.
4.  **Pengukuran dan Payoff**: Hasil permainan ditentukan oleh pengukuran state akhir, dan *payoff* dihitung dari nilai ekspektasi operator *payoff*.

Berikut adalah dua protokol kuantisasi permainan yang umum:

#### 2.1.4.1 Skema Eisert-Wilkens-Lewenstein (EWL)

Protokol Eisert-Wilkens-Lewenstein (EWL) adalah salah satu kerangka kerja paling berpengaruh untuk mengkuantisasi permainan klasik. Protokol ini memperkenalkan operator *entanglement* $J$ yang bekerja pada state awal klasik (misalnya, $|00\rangle$) untuk menciptakan korelasi kuantum sebelum pemain menerapkan strategi mereka (Eisert et al., 1999; Samadi et al., 2017).

Langkah-langkah utamanya adalah:

1.  **State Awal Terjerat**: State awal sistem disiapkan dalam bentuk terjerat menggunakan operator $J$:
    $$ |\psi_{in}\rangle = J |00\rangle $$
    Di mana $J$ sering mengambil bentuk $J = e^{i\gamma \sigma_x \otimes \sigma_x / 2}$, dengan $\gamma$ mengukur tingkat keterikatan.
2.  **Strategi Pemain**: Setiap pemain memilih strategi yang direpresentasikan oleh operator uniter lokal (misalnya, $U_A$ dan $U_B$).
3.  **State Akhir**: Setelah pemain menerapkan strategi, operator *un-entanglement* $J^\dagger$ diterapkan untuk memisahkan state sebelum pengukuran:
    $$ |\psi_f\rangle = J^\dagger (U_A \otimes U_B) J |00\rangle $$
4.  **Payoff**: *Payoff* dihitung dari hasil pengukuran state akhir ini. Protokol EWL memungkinkan tercapainya Nash Equilibrium baru yang seringkali Pareto-superior dibandingkan ekuilibrium klasik, terutama dalam permainan seperti Dilema Tahanan.

#### 2.1.4.2 Skema Marinatto-Weber (MW)

Skema Marinatto-Weber (MW) menyediakan protokol standar lain untuk mengkuantisasi permainan klasik, yang relevan untuk situasi dengan *mixed state* atau ketika state awal tidak murni (Marinatto & Weber, 2000; Samadi et al., 2017). Protokol ini sangat cocok untuk menganalisis *Mixed Strategy Quantum Games*.

Langkah-langkah formalnya adalah:

1.  **State Awal**: Permainan dimulai dengan state awal $\rho_{in}$ pada ruang Hilbert gabungan $\mathcal{H}_A \otimes \mathcal{H}_B$, yang bisa berupa state terjerat (*entangled*) atau state campuran.
2.  **Strategi**: Pemain A dan B memilih strategi yang direpresentasikan oleh operator uniter $U_A$ dan $U_B$. Aksi gabungan pada sistem adalah $U = U_A \otimes U_B$.
3.  **State Akhir**: State sistem setelah aksi pemain berevolusi menjadi:
    $$ \rho_f = U \rho_{in} U^\dagger = (U_A \otimes U_B) \rho_{in} (U_A^\dagger \otimes U_B^\dagger) $$
4.  **Payoff**: Payoff yang diterima pemain $i$ (misal, A) adalah nilai ekspektasi dari operator *payoff* $P_A$:
        $$ \$_{A} = \text{Tr}(P_A \rho_f) $$

Dalam konteks *Quantum Barro-Gordon Game*, strategi klasik (inflasi tinggi/rendah) dipetakan ke operator Identitas ($I$) dan Pauli-X ($\sigma_x$) atau operator uniter lainnya, memungkinkan solusi *Nash Equilibrium* yang *time-consistent* melalui eksploitasi superposisi strategi.

### 2.1.5 Teori Permainan Bayesian dan Quantum Discord

Teori permainan klasik sering mengasumsikan informasi sempurna. Namun, dalam skenario nyata, pemain sering menghadapi ketidakpastian mengenai tipe lawan mereka. **Teori Permainan Bayesian** memodelkan situasi ini dengan menetapkan *prior belief*.

Berdasarkan Lowe (2024), payoff ekspektasi untuk pemain A dalam permainan Bayesian diberikan oleh:

$$ u_A = \sum_{\alpha, \beta} P_A(\alpha, \beta) \sum_{\sigma, \sigma'} P(\sigma \sigma' | \alpha \beta) u^{\alpha, \beta}_{\sigma, \sigma', A} $$

di mana $\alpha, \beta$ adalah tipe permainan/pemain, dan $\sigma, \sigma'$ adalah hasil pengukuran (aksi).

Keunggulan kuantum dalam skenario ini tidak hanya bergantung pada *entanglement*, tetapi juga pada **Quantum Discord**. Quantum discord mengukur korelasi kuantum total dikurangi korelasi klasik, dan didefinisikan melalui perbedaan antara *quantum mutual information* $I(\rho^{AB})$ dan korelasi klasik $J_A(\rho^{AB})$:

$$ D_A(\rho^{AB}) = I(\rho^{AB}) - J_A(\rho^{AB}) $$

$$ I(\rho^{AB}) = S(\rho^A) + S(\rho^B) - S(\rho^{AB}) $$

di mana $S(\rho)$ adalah entropi von Neumann. Quantum discord mampu menangkap korelasi kuantum non-lokal bahkan dalam *mixed separable states*, yang krusial untuk aplikasi di mana entanglement murni sulit dipertahankan (Lowe, 2024).

### 2.1.6 Kognisi Kuantum dan Pelanggaran Prinsip Rasionalitas

Teori keputusan klasik didasarkan pada aksioma rasionalitas, salah satunya adalah **Sure Thing Principle** dari Savage. Prinsip ini menyatakan bahwa jika seorang pengambil keputusan lebih memilih aksi $A$ daripada $B$ dalam keadaan $X$, dan juga lebih memilih $A$ daripada $B$ dalam keadaan bukan-$X$, maka ia harus memilih $A$ terlepas dari apakah $X$ terjadi atau tidak. Namun, eksperimen psikologi kognitif, seperti yang dilakukan oleh Tversky dan Shafir (1992) pada *Prisoner's Dilemma*, menunjukkan pelanggaran prinsip ini yang dikenal sebagai **disjunction effect**.

Kognisi kuantum (*Quantum Cognition*) memodelkan fenomena irasionalitas ini bukan sebagai kesalahan (error), melainkan sebagai manifestasi dari **Interferensi Kuantum**. Dalam formalisme ini, probabilitas total keputusan tidak mengikuti hukum aditivitas klasik (Hukum Total Probabilitas), melainkan mengandung suku interferensi:

$$ P(A) = | \psi_A + \psi_B |^2 = P(A) + P(B) + 2\sqrt{P(A)P(B)} \cos \theta $$

Di mana $\theta$ adalah fase relatif yang merepresentasikan bias kognitif atau ambiguitas. Jika $\cos \theta \neq 0$, probabilitas keputusan dapat menyimpang dari prediksi klasik, menjelaskan fenomena seperti *panic selling* atau *herd behavior* di pasar keuangan.

Untuk memetakan struktur keputusan kompleks ini, digunakan **Quantum-like Influence Diagrams (QLID)**. QLID memperluas *Bayesian Networks* klasik dengan mengganti probabilitas kondisional riil dengan amplitudo probabilitas kompleks, memungkinkan pemodelan superposisi keyakinan investor sebelum keputusan final (kolaps) diambil.

## 2.2 Fisika Statistik dalam Pemodelan Pasar dan Optimasi
Studi ekonomi modern semakin mengadopsi pendekatan dari fisika untuk memahami kompleksitas dan dinamika pasar. Oleh karena itu, pada bagian ini akan dihubungkan konsep termodinamika dan mekanika statistik dengan fenomena ekonomi. Dalam kerangka ini, pasar dipandang sebagai sistem banyak benda (*many-body system*) di mana agen-agen ekonomi berinteraksi satu sama lain, sebagaimana pada partikel dalam fisika. Ekuilibrium pasar kemudian dapat dipahami sebagai keadaan kesetimbangan termodinamika atau *ground state* dari sistem tersebut.

### 2.2.1 Model Ising dan Distribusi Boltzmann dalam Konteks Optimasi

Model Ising adalah model interaksi spin klasik yang awalnya dikembangkan untuk menjelaskan feromagnetisme, namun kini menjadi landasan penting dalam pemodelan masalah optimasi kombinatorial. Sistem didefinisikan oleh **Hamiltonian Ising** sebagai berikut (Layden et al., 2022):

$$ E(s) = - \sum_{j>k=1}^n J_{jk}s_j s_k - \sum_{j=1}^n h_j s_j $$

di mana $s_j \in \{+1, -1\}$ adalah variabel spin, $J_{jk}$ adalah koefisien kopling interaksi antar spin, dan $h_j$ adalah medan eksternal. Konfigurasi spin mengikuti **Distribusi Boltzmann** $\mu(s) = \frac{1}{Z} e^{-E(s)/T}$, di mana keadaan dasar (*ground state*) dengan energi terendah merepresentasikan solusi yang paling mungkin terjadi pada suhu rendah ($T \to 0$).

Relevansi model ini dalam teori permainan dan ekonomi terletak pada kemampuannya memetakan masalah optimasi, seperti **Travelling Salesman Problem (TSP)**, ke dalam pencarian *ground state*. Fungsi biaya (*cost function*) TSP, yang meminimalkan total jarak $w_{i,j}$, dapat dipetakan ke Hamiltonian Ising melalui transformasi variabel biner keputusan $x_{i,t} \in \{0, 1\}$ (apakah kota $i$ dikunjungi pada waktu $t$) ke variabel spin $\sigma_{i,j}^z$ (Pauli-Z) menggunakan relasi (Sinaga et al., 2023):

$$ x_{i,t} = \frac{I - \sigma_{i,j}^z}{2} $$

Dengan demikian, biaya Hamiltonian (*Cost Hamiltonian*) $H_C$ dikonstruksi sedemikian rupa sehingga meminimalkan energi sistem ekuivalen dengan meminimalkan biaya perjalanan sekaligus memenuhi batasan-batasan (*constraints*) perjalanan:

$$ H_C = \sum_{i} c_i \sigma_i^z + \sum_{i,j} c_{i,j} \sigma_i^z \sigma_j^z $$

Pendekatan ini menjadi dasar bagi algoritma kuantum seperti *Quantum Approximate Optimization Algorithm* (QAOA) dan *Quantum Annealing* untuk menyelesaikan masalah optimasi yang kompleks secara lebih efisien dibandingkan metode klasik.

### 2.2.2 Proses Stokastik: Dari Black-Scholes hingga Fraktal

Dasar bagi pemodelan fluktuasi harga aset yang bersifat acak sering kali menggunakan **Gerak Brown Geometris (Geometric Brownian Motion - GBM)**. Persamaan diferensial stokastik untuk GBM diberikan oleh:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

di mana $S_t$ adalah harga aset pada waktu $t$, $\mu$ adalah *drift*, $\sigma$ adalah volatilitas, dan $W_t$ adalah proses Wiener standar. Solusi analitik dari persamaan ini menghasilkan distribusi log-normal untuk harga aset:

$$ S_t = S_0 \exp\left( (\mu - \frac{1}{2}\sigma^2)t + \sigma W_t \right) $$

Berdasarkan asumsi bahwa harga aset mengikuti GBM ini, **Model Black-Scholes** dikembangkan sebagai standar untuk penetapan harga opsi Eropa (Schwert, 2003). Persamaan diferensial parsial Black-Scholes untuk harga opsi $V(S, t)$ adalah:

$$ \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0 $$

Solusi untuk harga opsi *call* Eropa diberikan oleh:

$$ C(S, t) = S N(d_1) - K e^{-r(T-t)} N(d_2) $$

di mana $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$, $d_2 = d_1 - \sigma\sqrt{T-t}$, dan $N(\cdot)$ adalah fungsi distribusi kumulatif normal standar.

Namun, model klasik ini memiliki keterbatasan fundamental karena mengasumsikan volatilitas konstan dan distribusi Gaussian, yang sering gagal menangkap fenomena pasar nyata seperti "fat tails", *long-range dependence* (memori jangka panjang), dan "volatility smile".

Untuk mengatasi hal ini, pendekatan **Black-Scholes Fraktal (Generalized BSE)** diperkenalkan (El-Nabulsi & Anukool, 2025). Model ini menggunakan operator turunan fraktal untuk memperhitungkan dimensi fraktal ruang ($S^\alpha$) dan waktu ($t^\beta$), serta parameter yang mengikuti *power-laws*:

$$ \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2(t)S^2 \frac{\partial^2 V}{\partial S^2} + (r(t) - D(t))S \frac{\partial V}{\partial S} - r(t)V = 0 $$

dengan volatilitas $\sigma^2(t) \propto t^\gamma$ dan suku bunga $r(S,t) \propto t^\xi S^{\alpha-1}$. Konsep dimensi fraktal ini sangat relevan untuk memodelkan "noise" atau ketidakpastian pasar yang lebih realistis dalam *mixed state* matriks densitas kuantum, di mana pasar tidak sepenuhnya acak murni tetapi memiliki struktur fraktal yang mendasari.

### 2.2.3 Fraktal dan Analisis Runtun Waktu (Time Series)
Analisis pasar keuangan modern sering menggunakan **konsep dimensi fraktal** untuk mengukur kekasaran dan kompleksitas data runtun waktu yang tidak dapat dijelaskan oleh model Gaussian standar. Dimensi fraktal ($D$) berkaitan erat dengan *Hurst Exponent* ($H$), parameter yang mengukur autokorelasi dalam runtun waktu (El-Nabulsi & Anukool, 2025).

Dalam konteks *Fractal Market Hypothesis*, dimensi fraktal memberikan indikator stabilitas pasar; aset berisiko tinggi cenderung memiliki dimensi fraktal yang lebih tinggi, sementara aset stabil memiliki dimensi fraktal mendekati satu. Operator derivatif fraktal, seperti $$\nabla^\alpha f(x) := (x/x_0)^{1-\alpha}(\nabla + \frac{1-\alpha}{2x})f(x)$$yang digunakan untuk memodelkan dinamika harga aset dalam dimensi fraktal, memberikan generalisasi yang lebih akurat daripada kalkulus standar untuk sistem yang tidak kontinu atau memiliki memori jangka panjang.

Secara empiris, nilai Hurst Exponent ($H$) diestimasi menggunakan metode **Analisis Rescaled Range (R/S)**. Metode ini, yang diperkenalkan oleh Harold Edwin Hurst, membandingkan rentang fluktuasi data ($R$) terhadap standar deviasinya ($S$) pada berbagai skala waktu ($n$). Hubungan skala ini mengikuti hukum pangkat:

$$ (R/S)_n = c \cdot n^H $$

Di mana $c$ adalah konstanta. Analisis ini mendeteksi keberadaan memori jangka panjang dalam data runtun waktu; nilai $H > 0.5$ menunjukkan persistensi (tren positif/negatif yang berlanjut), sedangkan $H < 0.5$ menunjukkan anti-persistensi (kembali ke rata-rata).

### 2.2.4 Dinamika Mean-Reverting dan Arbitrase Statistik
**Arbitrase statistik** adalah strategi perdagangan yang mengeksploitasi inefisiensi harga jangka pendek antara sekuritas yang saling terkait secara statistik. Strategi ini sering bergantung pada konsep **kointegrasi**, di mana kombinasi linear dari dua atau lebih deret waktu harga aset yang tidak stasioner menjadi stasioner (mean-reverting) (Li & Papanicolaou, 2022).

Misalkan $S_t^1$ dan $S_t^2$ adalah harga dua saham yang kointegrasi. Maka terdapat koefisien $\beta$ sehingga *spread* $Z_t = \ln S_t^1 - \beta \ln S_t^2$ bersifat stasioner. Dinamika *spread* ini sering dimodelkan menggunakan proses **Ornstein-Uhlenbeck (OU)**:

$$ dZ_t = \kappa (\theta - Z_t) dt + \eta dW_t $$

di mana $\kappa$ adalah kecepatan *mean-reversion*, $\theta$ adalah rata-rata jangka panjang, dan $\eta$ adalah volatilitas *spread*. Strategi perdagangan melibatkan pembelian portofolio *spread* ketika $Z_t$ menyimpang secara signifikan dari $\theta$ dan menutup posisi ketika kembali ke rata-rata, memanfaatkan sifat *mean-reverting* tersebut. Pendekatan ini memungkinkan konstruksi portofolio "market-neutral" yang kebal terhadap pergerakan pasar secara umum namun tetap menghasilkan *alpha*.

## 2.3 Metode Solusi Komputasi untuk Ekuilibrium Ekonomi
Setelah memodelkan interaksi pasar dan dinamika aset menggunakan formalisme kuantum dan statistik, tantangan berikutnya adalah menemukan solusi ekuilibrium atau harga derivatif yang adil. Seringkali, persamaan yang dihasilkan (seperti Hamiltonian sistem banyak benda atau SDE dimensi tinggi) tidak memiliki solusi analitik tertutup. Oleh karena itu, teknik simulasi dan komputasi numerik diperlukan untuk menyelesaikan persamaan kompleks tersebut, sesuai dengan konsep dari **Fisika Komputasi**.

### 2.3.1 Metode Monte Carlo dan Rantai Markov (MCMC)
Metode Monte Carlo adalah teknik sampling stokastik untuk menyelesaikan integral dimensi tinggi atau masalah optimasi. Dalam konteks **Libor Market Model (LMM)**, yang merupakan model standar untuk penetapan harga derivatif suku bunga, dinamika *forward Libor rates* $L_n(t)$ dimodelkan sebagai:

$$ dL_n(t) = \sigma_n(t, L_n(t)) dW^{n+1}(t) $$

di bawah ukuran forward $T_{n+1}$. Simulasi Monte Carlo digunakan untuk memproyeksikan lintasan suku bunga ini ke masa depan untuk menghitung nilai ekspektasi payoff derivatif (Wang et al., 2018).

### 2.3.2 Persamaan Diferensial Stokastik Mundur (BSDE) dan Deep Learning
Masalah penetapan harga opsi, terutama opsi gaya Amerika atau Bermudan yang memungkinkan eksekusi dini, sering kali diformulasikan sebagai **Persamaan Diferensial Stokastik Mundur (Backward Stochastic Differential Equations - BSDE)**. Bentuk umum BSDE untuk harga opsi $Y(t)$ diberikan oleh:

$$ dY(t) = -f(t, Y(t), Z(t)) dt + Z(t) dW(t), \quad Y(T) = \xi $$

di mana $\xi$ adalah payoff pada saat jatuh tempo $T$, $f$ adalah generator (misalnya, suku bunga bebas risiko), dan $Z(t)$ merepresentasikan strategi lindung nilai (*hedging strategy*).

Dalam model kompleks seperti **Libor Market Model (LMM)**, penetapan harga derivatif sering menghadapi tantangan **"Curse of Dimensionality"**, di mana metode numerik tradisional (seperti *finite difference*) gagal karena dimensi ruang keadaan yang sangat tinggi (misalnya, puluhan *rate* yang saling berkorelasi).

Untuk mengatasi hal ini, pendekatan berbasis **Deep Learning** telah dikembangkan (Wang et al., 2018). Solusi BSDE ($Y(t), Z(t)$) diaproksimasi menggunakan jaringan saraf tiruan (*Deep Neural Networks* - DNN). Algoritma ini memecah masalah menjadi sub-masalah yang lebih kecil dan menyelesaikannya secara mundur (*backward*) dari waktu $T$ ke $t_0$, memungkinkan solusi yang efisien dan akurat bahkan dalam dimensi tinggi yang sebelumnya sulit dijangkau.

### 2.3.3 Algoritma Optimasi Kuantum (QAOA)
Sebagai alternatif dari metode klasik seperti Monte Carlo, **Quantum Approximate Optimization Algorithm (QAOA)** menawarkan pendekatan kuantum untuk menemukan solusi optimal. Seperti yang telah dibahas pada sub-bab 2.2.1, banyak masalah optimasi ekonomi (seperti TSP atau penemuan Nash Equilibrium) dapat dipetakan ke dalam pencarian keadaan dasar (*ground state*) dari Hamiltonian Ising.

QAOA bekerja dengan menerapkan serangkaian gerbang kuantum yang diparameterisasi untuk memandu sistem kuantum menuju keadaan energi terendah tersebut. Dalam konteks *Quantum Game Theory*, ini berarti QAOA dapat digunakan untuk menemukan strategi optimal yang meminimalkan fungsi biaya atau memaksimalkan *payoff* pemain dalam ruang pencarian yang sangat besar, yang mungkin sulit dijangkau oleh algoritma klasik.

### 2.3.4 Jaringan Saraf Tiruan Kuantum (QNN)

Untuk mengatasi tantangan prediksi pada data finansial berdimensi tinggi, dikembangkan algoritma **Quantum Neural Networks (QNN)** atau sering disebut sebagai *Parameterized Quantum Circuits (PQC)*. QNN adalah algoritma hibrida klasik-kuantum yang memanfaatkan ruang Hilbert untuk memproses fitur data dengan cara yang sulit dilakukan oleh jaringan saraf klasik.

Langkah fundamental dalam QNN adalah **Data Encoding**, yaitu proses memetakan data klasik $\mathbf{x}$ ke dalam state kuantum $|\psi(\mathbf{x})\rangle$. Beberapa metode encoding yang relevan meliputi:

1.  **Angle Encoding:** Memetakan nilai fitur $x_i$ ke dalam sudut rotasi qubit, misalnya $R_y(x_i)|0\rangle$. Metode ini efisien dalam penggunaan gerbang tetapi membutuhkan $N$ qubit untuk $N$ fitur.
2.  **Amplitude Encoding:** Memetakan vektor data ternormalisasi $\mathbf{x}$ ke dalam amplitudo state kuantum $|\psi\rangle = \sum_{i} x_i |i\rangle$. Keunggulan utamanya adalah kompresi eksponensial, di mana $N$ fitur dapat direpresentasikan oleh $\log_2 N$ qubit.

Arsitektur QNN terdiri dari lapisan sirkuit kuantum yang memiliki parameter rotasi yang dapat dilatih ($\theta$). Proses pelatihan (*training*) dilakukan secara hibrida: sirkuit kuantum mengevaluasi fungsi biaya (misalnya berdasarkan **Fidelity** atau jarak antara output state dengan target), dan pengoptimal klasik (seperti *Gradient Descent*) memperbarui parameter $\theta$ untuk meminimalkan *loss* tersebut. Pendekatan ini diharapkan memberikan *quantum advantage* dalam hal kecepatan konvergensi dan kemampuan generalisasi pada data pasar yang kompleks.
