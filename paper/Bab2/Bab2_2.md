# Bab 2: Tinjauan Pustaka dan Dasar Teori

Bab ini menguraikan landasan teori yang mendasari penelitian tesis, mengintegrasikan konsep-konsep dari Fisika Murni (Kuantum dan Statistik) dengan aplikasinya dalam Ekonomi dan Teori Permainan. Struktur bab ini disusun berdasarkan relevansi dengan mata kuliah yang telah ditempuh serta literatur terkini yang dikaji.

## 2.1 Formalisme Mekanika Kuantum untuk Pemodelan Informasi
Sub-bab ini membangun fondasi matematis yang diperlukan untuk Teori Permainan Kuantum dan Komputasi Kuantum, memperdalam konsep yang telah dipelajari dalam mata kuliah **Fisika Kuantum** dan **Fisika Matematika**.

### 2.1.1 Ruang Hilbert, Superposisi, dan Sistem Qubit vs Qutrit

Sebagai pengantar induktif untuk memahami kebutuhan akan sistem kuantum berdimensi tinggi, kita dapat meninjau kasus **prediksi pasar saham secara *real-time*** (Bakshi & Srinivasan, 2025). Dalam memodelkan dinamika pasar yang kompleks (seperti data indeks NIFTY 50), penggunaan sistem biner klasik atau bahkan sistem kuantum dua-level (**qubit**) sering kali menghadapi keterbatasan dalam merepresentasikan data kontinu tanpa kehilangan informasi signifikan akibat *discretization error*. Struktur data pasar yang kaya memerlukan kapasitas representasi yang lebih padat daripada yang dapat ditawarkan oleh qubit tunggal.

Keterbatasan ini analog dengan kasus **Quantum Penny-Flip Game** (Meyer, 1999), di mana pemain klasik terbatas pada strategi *flip* atau *no-flip*, sementara pemain kuantum memenangkan permainan dengan memanfaatkan ruang keadaan yang lebih luas melalui superposisi. Dalam konteks *financial forecasting*, perluasan ruang keadaan dari qubit ke **qutrit** (sistem tiga-level) memberikan "keunggulan kuantum" serupa: qutrit menawarkan kepadatan informasi yang lebih tinggi ($\log_2 3 \approx 1.585$ bit per qutrit) dan fleksibilitas topologi sirkuit yang lebih baik, sehingga mampu menangkap korelasi pasar yang kompleks dengan efisiensi komputasi yang lebih tinggi dibandingkan jaringan saraf berbasis qubit (QQBN).

Secara formal, sistem kuantum dijelaskan dalam ruang vektor kompleks yang dilengkapi dengan *inner product*, dikenal sebagai **Ruang Hilbert** ($\mathcal{H}$). Unit dasar informasi kuantum standar adalah **qubit**, dengan basis ortonormal $\{|0\rangle, |1\rangle\}$. State umum qubit dinyatakan sebagai:

$$ |\psi\rangle = \alpha|0\rangle + \beta|1\rangle $$

di mana $\alpha, \beta \in \mathbb{C}$ memenuhi $|\alpha|^2 + |\beta|^2 = 1$.

Untuk mengatasi keterbatasan representasi pada kasus kompleks di atas, **qutrit** didefinisikan dalam ruang Hilbert tiga dimensi dengan basis komputasi $\{|0\rangle, |1\rangle, |2\rangle\}$. State superposisi qutrit dituliskan secara matematis sebagai:

%%kurang ditambahkan kasus sederhana (contoh seperti permainan *penny flip*)%%
$$ |\phi\rangle = c_0|0\rangle + c_1|1\rangle + c_2|2\rangle $$

dengan syarat normalisasi $\sum_{i=0}^2 |c_i|^2 = 1$. Transisi dari qubit ke qutrit ini merupakan langkah fundamental dalam meningkatkan kapasitas pemrosesan informasi untuk aplikasi keuangan tingkat lanjut.

### 2.1.2 Formalisme Matriks Densitas dan Skema Marinatto-Weber

Untuk sistem yang berada dalam *mixed state* atau ensemble statistik, deskripsi vektor state tidak lagi memadai. Kita menggunakan **Matriks Densitas** ($\rho$), yang didefinisikan sebagai:

$$ \rho = \sum_i p_i |\psi_i\rangle\langle\psi_i| $$

di mana $p_i$ adalah probabilitas sistem berada dalam state $|\psi_i\rangle$.

Dalam teori permainan kuantum, skema **Marinatto-Weber (MW)** (Marinatto & Weber, 2000; Samadi et al., 2017) menyediakan protokol standar untuk mengkuantisasi permainan klasik. Protokol ini sangat relevan dalam analisis *Quantum Barro-Gordon Game* untuk memodelkan kebijakan moneter. Langkah-langkah formalnya adalah:

1.  **State Awal**: Permainan dimulai dengan state awal $\rho_{in}$ pada ruang Hilbert gabungan $\mathcal{H}_A \otimes \mathcal{H}_B$, yang bisa berupa state terjerat (*entangled*).
2.  **Strategi**: Pemain A dan B memilih strategi yang direpresentasikan oleh operator uniter $U_A$ dan $U_B$. Aksi gabungan pada sistem adalah $U = U_A \otimes U_B$.
3.  **State Akhir**: State sistem setelah aksi pemain berevolusi menjadi:
    $$ \rho_f = U \rho_{in} U^\dagger = (U_A \otimes U_B) \rho_{in} (U_A^\dagger \otimes U_B^\dagger) $$
4.  **Payoff**: Payoff yang diterima pemain $i$ (misal, A) adalah nilai ekspektasi dari operator payoff $P_A$:
    $$ \$_{A} = \text{Tr}(P_A \rho_f) $$

Dalam konteks *Quantum Barro-Gordon Game*, strategi klasik (inflasi tinggi/rendah) dipetakan ke operator Identitas ($I$) dan Pauli-X ($\sigma_x$) atau operator uniter lainnya, memungkinkan solusi *Nash Equilibrium* yang time-consistent melalui eksploitasi superposisi strategi.

### 2.1.3 Teori Permainan Bayesian dan Quantum Discord

Teori permainan klasik sering mengasumsikan informasi sempurna. Namun, dalam skenario nyata, pemain sering menghadapi ketidakpastian mengenai tipe lawan mereka. **Teori Permainan Bayesian** memodelkan situasi ini dengan menetapkan *prior belief*.

Berdasarkan Lowe (2024), payoff ekspektasi untuk pemain A dalam permainan Bayesian diberikan oleh:

$$ u_A = \sum_{\alpha, \beta} P_A(\alpha, \beta) \sum_{\sigma, \sigma'} P(\sigma \sigma' | \alpha \beta) u^{\alpha, \beta}_{\sigma, \sigma', A} $$

di mana $\alpha, \beta$ adalah tipe permainan/pemain, dan $\sigma, \sigma'$ adalah hasil pengukuran (aksi).

Keunggulan kuantum dalam skenario ini tidak hanya bergantung pada *entanglement*, tetapi juga pada **Quantum Discord**. Quantum discord mengukur korelasi kuantum total dikurangi korelasi klasik, dan didefinisikan melalui perbedaan antara *quantum mutual information* $I(\rho^{AB})$ dan korelasi klasik $J_A(\rho^{AB})$:

$$ D_A(\rho^{AB}) = I(\rho^{AB}) - J_A(\rho^{AB}) $$

$$ I(\rho^{AB}) = S(\rho^A) + S(\rho^B) - S(\rho^{AB}) $$

di mana $S(\rho)$ adalah entropi von Neumann. Quantum discord mampu menangkap korelasi kuantum non-lokal bahkan dalam *mixed separable states*, yang krusial untuk aplikasi di mana entanglement murni sulit dipertahankan (Lowe, 2024).

## 2.2 Fisika Statistik dan Sistem Kompleks
Sub-bab ini menghubungkan termodinamika dan mekanika statistik dengan fenomena ekonomi, memanfaatkan dasar dari mata kuliah **Fisika Statistik** dan **Termodinamika**.

### 2.2.1 Model Ising dan Distribusi Boltzmann
Model Ising adalah model interaksi spin klasik yang awalnya dikembangkan untuk menjelaskan feromagnetisme, namun kini diterapkan luas dalam pemodelan masalah optimasi kombinatorial. Sistem didefinisikan oleh **Hamiltonian Ising** sebagai berikut (Layden et al., 2022):

$$ E(s) = - \sum_{j>k=1}^n J_{jk}s_j s_k - \sum_{j=1}^n h_j s_j $$

di mana $s_j \in \{+1, -1\}$ adalah variabel spin, $J_{jk}$ adalah koefisien kopling interaksi antar spin, dan $h_j$ adalah medan eksternal.

Konfigurasi spin mengikuti **Distribusi Boltzmann** $\mu(s) = \frac{1}{Z} e^{-E(s)/T}$, di mana $T$ adalah suhu dan $Z = \sum_s e^{-E(s)/T}$ adalah fungsi partisi. Dalam konteks optimasi masalah seperti *Travelling Salesman Problem (TSP)*, fungsi biaya dipetakan ke dalam Hamiltonian Ising, di mana keadaan dasar (ground state) dengan energi terendah merepresentasikan solusi optimal (Sinaga et al., 2023).

### 2.2.2 Proses Stokastik dan Gerak Brown Geometris
Dasar bagi pemodelan fluktuasi harga aset yang bersifat acak sering kali menggunakan **Gerak Brown Geometris (Geometric Brownian Motion - GBM)**. Persamaan diferensial stokastik untuk GBM diberikan oleh:

$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

di mana $S_t$ adalah harga aset pada waktu $t$, $\mu$ adalah drift (tingkat pengembalian yang diharapkan), $\sigma$ adalah volatilitas, dan $W_t$ adalah proses Wiener standar. Solusi analitik dari persamaan ini adalah:

$$ S_t = S_0 \exp\left( (\mu - \frac{1}{2}\sigma^2)t + \sigma W_t \right) $$

Namun, model ini memiliki keterbatasan dalam menangkap fenomena pasar yang kompleks ("rough volatility") dan ketergantungan jangka panjang (long-memory dependence), yang sering kali memerlukan pendekatan fraktal atau *fractional Brownian motion* (El-Nabulsi & Anukool, 2025; Wang et al., 2018).

### 2.2.3 Fraktal dan Analisis Runtun Waktu (Time Series)
Analisis pasar keuangan modern sering menggunakan **konsep dimensi fraktal** untuk mengukur kekasaran dan kompleksitas data runtun waktu yang tidak dapat dijelaskan oleh model Gaussian standar. Dimensi fraktal ($D$) berkaitan erat dengan *Hurst Exponent* ($H$), parameter yang mengukur autokorelasi dalam runtun waktu (El-Nabulsi & Anukool, 2025).

Dalam konteks *Fractal Market Hypothesis*, dimensi fraktal memberikan indikator stabilitas pasar; aset berisiko tinggi cenderung memiliki dimensi fraktal yang lebih tinggi, sementara aset stabil memiliki dimensi fraktal mendekati satu. Operator derivatif fraktal, seperti $\nabla^\alpha f(x) := (x/x_0)^{1-\alpha}(\nabla + \frac{1-\alpha}{2x})f(x)$, digunakan untuk memodelkan dinamika harga aset dalam dimensi fraktal, memberikan generalisasi yang lebih akurat daripada kalkulus standar untuk sistem yang tidak kontinu atau memiliki memori jangka panjang.

## 2.3 Metode Komputasi dan Numerik
Menjabarkan teknik simulasi yang digunakan untuk menyelesaikan persamaan kompleks yang tidak memiliki solusi analitik, sesuai dengan kompetensi dari **Fisika Komputasi** dan **Pengantar Fisika Komputasi**.

### 2.3.1 Metode Monte Carlo dan Rantai Markov (MCMC)
Metode Monte Carlo adalah teknik sampling stokastik untuk menyelesaikan integral dimensi tinggi atau masalah optimasi. Dalam konteks **Libor Market Model (LMM)**, yang merupakan model standar untuk penetapan harga derivatif suku bunga, dinamika *forward Libor rates* $L_n(t)$ dimodelkan sebagai:

$$ dL_n(t) = \sigma_n(t, L_n(t)) dW^{n+1}(t) $$

di bawah ukuran forward $T_{n+1}$. Simulasi Monte Carlo digunakan untuk memproyeksikan lintasan suku bunga ini ke masa depan untuk menghitung nilai ekspektasi payoff derivatif (Wang et al., 2018).

### 2.3.2 Persamaan Diferensial Stokastik Mundur (BSDE)
Masalah penetapan harga opsi, terutama opsi gaya Amerika atau Bermudan yang memungkinkan eksekusi dini, sering kali diformulasikan sebagai **Persamaan Diferensial Stokastik Mundur (Backward Stochastic Differential Equations - BSDE)**. Bentuk umum BSDE untuk harga opsi $Y(t)$ diberikan oleh:

$$ dY(t) = -f(t, Y(t), Z(t)) dt + Z(t) dW(t), \quad Y(T) = \xi $$

di mana $\xi$ adalah payoff pada saat jatuh tempo $T$, $f$ adalah generator (misalnya, suku bunga bebas risiko), dan $Z(t)$ merepresentasikan strategi lindung nilai (*hedging strategy*).

### 2.3.3 Kutukan Dimensi (Curse of Dimensionality)
Metode numerik tradisional seperti *finite difference* atau *finite element* sering gagal ketika diterapkan pada masalah LMM karena dimensi ruang keadaan yang sangat tinggi (misalnya, 60 dimensi untuk *swaption* 10 tahun dengan tenor 20 tahun). Fenomena ini dikenal sebagai **"Curse of Dimensionality"**, di mana kompleksitas komputasi tumbuh secara eksponensial seiring dengan peningkatan dimensi.

Untuk mengatasi hal ini, pendekatan berbasis *Deep Learning* telah dikembangkan, di mana solusi BSDE ($Y(t), Z(t)$) diaproksimasi menggunakan jaringan saraf tiruan (Deep Neural Networks - DNN). Algoritma **Deep BSDE** (Wang et al., 2018) memecah masalah menjadi sub-masalah yang lebih kecil dan menyelesaikannya secara mundur (*backward*) dari waktu $T$ ke $t_0$, memungkinkan solusi yang efisien bahkan dalam dimensi tinggi.

### 2.3.4 Algoritma Optimasi Kuantum (QAOA)
Algoritma hibrida klasik-kuantum untuk masalah optimasi kombinatorial.
*   *Relevansi Paper:* Dijelaskan dalam *Important Quantum Gates for Quantum Algorithms of TSP*.

## 2.4 Ekonofisika dan Teori Permainan
Sintesis dari konsep fisika yang diterapkan pada masalah ekonomi, sesuai dengan minat spesifik tesis dan mata kuliah **Matematika Finansial**.

### 2.4.1 Model Black-Scholes dan Derivatif Finansial
**Model Black-Scholes** adalah model matematika standar untuk penetapan harga opsi Eropa. Model ini didasarkan pada asumsi bahwa harga aset dasar mengikuti gerak Brown geometris dengan volatilitas konstan dan suku bunga bebas risiko yang konstan (Schwert, 2003). Persamaan diferensial parsial Black-Scholes untuk harga opsi $V(S, t)$ adalah:

$$ \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0 $$

Solusi untuk harga opsi *call* Eropa diberikan oleh:

$$ C(S, t) = S N(d_1) - K e^{-r(T-t)} N(d_2) $$

di mana $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}$, $d_2 = d_1 - \sigma\sqrt{T-t}$, dan $N(\cdot)$ adalah fungsi distribusi kumulatif normal standar. Meskipun model ini sangat berpengaruh, asumsi volatilitas konstan sering dilanggar dalam praktik ("volatility smile"), yang mendorong pengembangan model volatilitas stokastik dan fraktal.

### 2.4.2 Teori Permainan Klasik vs Kuantum
Teori permainan klasik mempelajari interaksi strategis antara agen rasional. Konsep solusi utamanya adalah **Nash Equilibrium**, di mana tidak ada pemain yang dapat meningkatkan *payoff*-nya dengan mengubah strategi secara sepihak. Dalam **Teori Permainan Kuantum**, ruang strategi diperluas menggunakan superposisi keadaan kuantum dan *entanglement* (Samadi et al., 2017).

Pemain dapat menggunakan operator uniter $U$ pada keadaan awal $|\psi_{in}\rangle$ untuk menghasilkan keadaan akhir $|\psi_f\rangle$. *Payoff* dihitung berdasarkan hasil pengukuran keadaan akhir. Strategi kuantum memungkinkan pemain untuk mencapai *Nash Equilibrium* baru yang seringkali Pareto-superior dibandingkan ekuilibrium klasik. Contoh klasiknya adalah dalam dilema tahanan kuantum, di mana kerjasama dapat menjadi strategi ekuilibrium yang stabil, mengatasi dilema yang ada pada versi klasik.

### 2.4.3 Arbitrase Statistik dan Kointegrasi
**Arbitrase statistik** adalah strategi perdagangan yang mengeksploitasi inefisiensi harga jangka pendek antara sekuritas yang saling terkait secara statistik. Strategi ini sering bergantung pada konsep **kointegrasi**, di mana kombinasi linear dari dua atau lebih deret waktu harga aset yang tidak stasioner menjadi stasioner (mean-reverting) (Li & Papanicolaou, 2022).

Misalkan $S_t^1$ dan $S_t^2$ adalah harga dua saham yang kointegrasi. Maka terdapat koefisien $\beta$ sehingga *spread* $Z_t = \ln S_t^1 - \beta \ln S_t^2$ bersifat stasioner. Dinamika *spread* ini sering dimodelkan menggunakan proses **Ornstein-Uhlenbeck (OU)**:

$$ dZ_t = \kappa (\theta - Z_t) dt + \eta dW_t $$

di mana $\kappa$ adalah kecepatan *mean-reversion*, $\theta$ adalah rata-rata jangka panjang, dan $\eta$ adalah volatilitas *spread*. Strategi perdagangan melibatkan pembelian portofolio *spread* ketika $Z_t$ menyimpang secara signifikan dari $\theta$ dan menutup posisi ketika kembali ke rata-rata, memanfaatkan sifat *mean-reverting* tersebut. Pendekatan ini memungkinkan konstruksi portofolio "market-neutral" yang kebal terhadap pergerakan pasar secara umum namun tetap menghasilkan *alpha*.
