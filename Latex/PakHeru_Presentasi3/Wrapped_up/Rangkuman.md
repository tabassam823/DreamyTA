# **1. Econophysics & Discrete State Representation**

### 1.1 Dinamika Stokastik Return Aset
Dalam econophysics, harga aset pada waktu $t$, dinyatakan sebagai $S(t)$, sering dimodelkan sebagai proses stokastik. Namun, variabel fundamental yang dianalisis adalah *log-return* atau *percentage return* $r(t)$, yang memberikan ukuran invarian terhadap skala harga:

$$ r(t) = \frac{S(t) - S(t-1)}{S(t-1)} \approx \ln\left(\frac{S(t)}{S(t-1)}\right) \tag{1.1} $$

Di mana $r(t) \in \mathbb{R}$. Distribusi statistik dari $r(t)$ sering kali menunjukkan *heavy tails* (non-Gaussian), yang memotivasi pendekatan non-klasik [[Penurunan_1.1]].

### 1.2 Kuantisasi Ruang Keadaan (Hilbert Space Construction)
Untuk memetakan dinamika pasar kontinu ke dalam formalisme mekanika kuantum, kita melakukan **diskretisasi biner**. Kita mendefinisikan ruang Hilbert dua dimensi $\mathcal{H} \cong \mathbb{C}^2$ (isomorfik dengan sistem Qubit spin-1/2).

Operator proyeksi ke basis komputasi didefinisikan berdasarkan tanda dari $r(t)$:

$$
\ket{\psi(t)} = 
\begin{cases} 
\ket{0} \equiv \begin{pmatrix} 1 \\ 0 \end{pmatrix}, & \text{jika } r(t) \ge 0 \quad (\text{Bull/Up State}) \\
\ket{1} \equiv \begin{pmatrix} 0 \\ 1 \end{pmatrix}, & \text{jika } r(t) < 0 \quad (\text{Bear/Down State})
\end{cases} \tag{1.2}
$$

Dalam representasi ini, $\ket{0}$ dan $\ket{1}$ adalah vektor basis ortonormal yang memenuhi kondisi ortogonalitas:
$$ \langle i | j \rangle = \delta_{ij} \tag{1.3} $$
(jika Ortogonal; dua keadaan yang berbeda secara fisik (misalnya, spin atas dan spin bawah) harus bersifat saling lepas. Artinya, jika sistem berada dalam keadaan $\ket{j}$, probabilitas untuk menemukannya dalam keadaan $\ket{i}$ adalah nol. Secara matematis: $\langle i | j \rangle = 0$.) [[Penurunan_1.3]]
### 1.3 Sistem Majemuk dan Produk Tensor
Untuk sistem yang terdiri dari dua aset, *Leader* ($L$) dan *Follower* ($F$), ruang keadaan gabungan didefinisikan sebagai produk tensor dari ruang Hilbert masing-masing aset:

$$ \mathcal{H}_{sys} = \mathcal{H}_L \otimes \mathcal{H}_F \cong \mathbb{C}^4 \tag{1.4} $$

Basis komputasi untuk sistem ini direntang oleh empat vektor basis ortonormal:
$$
\begin{aligned}
\ket{00} &= \ket{0}_L \otimes \ket{0}_F = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \quad (\text{Keduanya Naik}) \\
\ket{01} &= \ket{0}_L \otimes \ket{1}_F = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \quad (\text{Leader Naik, Follower Turun}) \\
\ket{10} &= \ket{1}_L \otimes \ket{0}_F = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \quad (\text{Leader Turun, Follower Naik}) \\
\ket{11} &= \ket{1}_L \otimes \ket{1}_F = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} \quad (\text{Keduanya Turun})
\end{aligned} \tag{1.5}
$$

### 1.4 Korespondensi Statistik-Kuantum (Born Rule)
Fungsi gelombang superposisi umum untuk sistem ini pada interval pengamatan $T$ dapat ditulis sebagai:

$$ \ket{\Psi} = \sum_{i,j \in \{0,1\}} \alpha_{ij} \ket{ij} \tag{1.6} $$

Di mana $\alpha_{ij} \in \mathbb{C}$ adalah amplitudo probabilitas. Berdasarkan **Aturan Born**, probabilitas menemukan sistem dalam keadaan $\ket{ij}$ adalah kuadrat modulus dari amplitudonya:

$$ P(i,j) = |\langle ij | \Psi \rangle|^2 = |\alpha_{ij}|^2 \tag{1.7} $$

Secara empiris, probabilitas ini diestimasi menggunakan pendekatan *Frequentist* dari data historis dengan $N$ titik data (jumlah hari pengamatan), di mana $n_{ij}$ adalah frekuensi kejadian state $ij$:

$$ P(i,j)_{empiris} = \frac{n_{ij}}{N} \tag{1.8} $$

Sehingga, kita mengonstruksi amplitudo probabilitas (dengan asumsi fase $\phi_{ij} = 0$ untuk simplifikasi awal, sehingga $\alpha_{ij} \in \mathbb{R}^+$):

$$ \alpha_{ij} = \sqrt{P(i,j)} = \sqrt{\frac{n_{ij}}{N}} \tag{1.9} $$

Kondisi normalisasi fungsi gelombang terpenuhi secara otomatis:
$$ \langle \Psi | \Psi \rangle = \sum_{i,j} |\alpha_{ij}|^2 = \sum_{i,j} \frac{n_{ij}}{N} = 1 \tag{1.10} $$

Formalisme ini [[Penurunan_1.10]] mengubah masalah korelasi statistik klasik menjadi masalah interferensi dan superposisi keadaan kuantum, yang menjadi landasan bagi bab-bab selanjutnya (Entanglement & Hamiltonian).
# **2. Stackelberg Game Theory & Payoff Matrix Construction**

### 2.1 Definisi Formal Permainan
Sistem dimodelkan sebagai permainan non-kooperatif dua agen $\mathcal{G} = (\mathcal{P}, \mathcal{S}, \mathcal{U})$, di mana:
*   $\mathcal{P} = \{L, F\}$ adalah himpunan pemain (*Leader* dan *Follower*).
*   $\mathcal{S}_k = \{\ket{0}, \ket{1}\}$ adalah ruang strategi diskrit untuk setiap pemain $k \in \mathcal{P}$, yang berkorespondensi dengan *state* pasar (Naik/Turun).
*   $\mathcal{U}_k : \mathcal{S}_L \times \mathcal{S}_F \to \mathbb{R}$ adalah fungsi utilitas (*payoff*) yang memetakan profil strategi bersama ke bilangan riil.

Dalam model Stackelberg, diasumsikan terdapat asimetri informasi atau kekuatan pasar di mana Pemain $L$ berkomitmen pada suatu strategi terlebih dahulu, dan Pemain $F$ merespons secara optimal $s_F^*(s_L)$.

### 2.2 Konstruksi Fungsi [[Payoff]] (Conditional Expectation)
Dalam formalisme ini, utilitas atau payoff tidak ditentukan secara *a priori* melalui fungsi utilitas spekulatif, melainkan diderivasi secara *a posteriori* dari akumulasi data historis yang telah diobservasi. Secara statistik, nilai ekspektasi dari variabel acak $R_k$ yang bergantung pada suatu kejadian (event) $A$ didefinisikan melalui formulasi ekspektasi diskret:

$$ \mathbb{E}[R|A] = \sum r \cdot P(R=r|A) \tag{2.1} $$

Dalam konteks pasar, **Event $A$** adalah sistem berada pada keadaan kuantum $\ket{ij}$. Oleh karena itu, payoff didefinisikan sebagai **ekspektasi return kondisional** terhadap *state* bersama tersebut. Misalkan $R_k(t)$ adalah return aset $k$ pada waktu $t$, maka fungsi utilitas empiris untuk keadaan gabungan $\ket{ij}$ adalah [[Penurunan_2.1]]:

$$ u_{ij}^k = \mathbb{E}[R_k | \text{State} = \ket{ij}] \tag{2.2} $$

Penurunan dari data historis dilakukan dengan mengidentifikasi himpunan waktu $\mathcal{T}_{ij}$, yaitu kumpulan hari di mana sistem tercatat berada dalam keadaan $\ket{ij}$ dari total $N$ hari pengamatan:

$$ \mathcal{T}_{ij} = \{t \in \{1, \dots, N\} \mid \text{State}_t = \ket{ij}\} \tag{2.3} $$

Estimasi *a posteriori* untuk ekspektasi return tersebut kemudian dihitung sebagai rata-rata aritmetika dari $R_k$ pada himpunan $\mathcal{T}_{ij}$:

$$ u_{ij}^k \approx \frac{1}{n_{ij}} \sum_{t \in \mathcal{T}_{ij}} R_k(t) \tag{2.4} $$

Di mana $n_{ij} = |\mathcal{T}_{ij}|$ adalah kardinalitas dari himpunan waktu tersebut. Secara probabilistik, berdasarkan hukum Bayes, hubungan ini merepresentasikan nilai pusat (*mean*) dari distribusi return yang telah difilter oleh informasi keadaan:

$$ P(R_k | \ket{ij}) = \frac{P(R_k \cap \ket{ij})}{P(\ket{ij})} \tag{2.5} $$

Pendekatan ini menjamin bahwa setiap elemen dalam matriks payoff memiliki dasar empiris yang kuat, memetakan topologi informasi pasar langsung ke dalam estimasi keuntungan strategis.

### 2.3 Regularisasi Laplace (Laplace Smoothing)
Untuk menangani masalah *sparse data* (di mana $n_{ij} \to 0$ untuk kejadian langka) dan menghindari singularitas atau varians tak terbatas pada estimasi payoff, diterapkan teknik *Laplace Smoothing* (atau *Additive Smoothing*).
Metode ini secara efektif memperkenalkan *prior* uniform (Bayesian perspective), menggeser penyebut sebesar $\lambda$:

$$ \hat{u}_{ij}^k = \frac{\sum_{t \in \mathcal{T}_{ij}} R_k(t)}{n_{ij} + \lambda} \tag{2.6} $$

Dalam model ini digunakan $\lambda = 1$. Hal ini memastikan bahwa matriks payoff tetap terdefinisi dengan baik (well-posed) meskipun $n_{ij}=0$.

### 2.4 Representasi Bimatrix (Normal Form)
Permainan direpresentasikan dalam bentuk matriks normal $2 \times 2$. Elemen matriks $(A, B)$ merepresentasikan tuple payoff $(u^L, u^F)$:

$$
\begin{pmatrix}
(a, b) & (c, d) \\
(e, f) & (g, h)
\end{pmatrix}
=
\begin{pmatrix}
(\hat{u}_{00}^L, \hat{u}_{00}^F) & (\hat{u}_{01}^L, \hat{u}_{01}^F) \\
(\hat{u}_{10}^L, \hat{u}_{10}^F) & (\hat{u}_{11}^L, \hat{u}_{11}^F)
\end{pmatrix} \tag{2.7}
$$

Di mana elemen payoff spesifik dipetakan sebagai berikut:
*   **Keadaan $\ket{00}$ (Bull-Bull):** $a = \hat{u}_{00}^L$, $b = \hat{u}_{00}^F$
*   **Keadaan $\ket{01}$ (Bull-Bear):** $c = \hat{u}_{01}^L$, $d = \hat{u}_{01}^F$
*   **Keadaan $\ket{10}$ (Bear-Bull):** $e = \hat{u}_{10}^L$, $f = \hat{u}_{10}^F$
*   **Keadaan $\ket{11}$ (Bear-Bear):** $g = \hat{u}_{11}^L$, $h = \hat{u}_{11}^F$

### 2.5 Ekuilibrium Strategis dan Klasifikasi Permainan
Analisis matriks ini bertujuan mencari **Nash Equilibrium** murni, yaitu profil strategi $(s_L^*, s_F^*)$ sedemikian rupa sehingga tidak ada pemain yang dapat meningkatkan payoff-nya dengan mengubah strategi secara sepihak (unilateral deviation):

$$ \forall s_L \in \mathcal{S}_L, \quad \mathcal{U}_L(s_L^*, s_F^*) \ge \mathcal{U}_L(s_L, s_F^*) \tag{2.8} $$
$$ \forall s_F \in \mathcal{S}_F, \quad \mathcal{U}_F(s_L^*, s_F^*) \ge \mathcal{U}_F(s_L^*, s_F) \tag{2.9} $$

Berdasarkan distribusi nilai payoff $(a, \dots, h)$, hubungan strategis antar aset dapat diklasifikasikan ke dalam beberapa model fundamental:

1.  **Coordination Game**: Terjadi jika payoff tertinggi berada pada keadaan diagonal $(a, b)$ dan $(g, h)$.
    *   **Kondisi**: $a > e, b > f$ dan $g > c, h > d$.
    *   **Interpretasi**: Aset cenderung bergerak searah (korelasi positif kuat). Perak mendapatkan keuntungan maksimal dengan mengikuti tren Emas.
2.  **Anti-Coordination (Hawk-Dove)**: Terjadi jika payoff tertinggi berada pada keadaan off-diagonal $(c, d)$ atau $(e, f)$.
    *   **Kondisi**: $c > a, d > h$ atau $e > g, f > b$.
    *   **Interpretasi**: Menunjukkan hubungan substitusi atau *hedging*. Keuntungan maksimal dicapai saat kedua aset bergerak berlawanan arah.
3.  **Prisoner's Dilemma**: Terjadi jika terdapat insentif bagi satu aset untuk "mengkhianati" arah tren demi return individu yang lebih tinggi, meskipun merugikan stabilitas bersama.
    *   **Kondisi**: $e > a, d > h$ (dominasi strategi untuk "membelot" dari tren utama).
    *   **Interpretasi**: Menunjukkan adanya volatilitas asimetris di mana satu aset mencoba mengambil keuntungan dari *lag* harga aset lainnya, yang sering kali mengarah pada ekuilibrium sub-optimal $\ket{11}$ (keduanya turun).

Penentuan model ini sangat krusial karena menentukan parameter interaksi $J$ dalam Hamiltonian kuantum pada bab selanjutnya.
# **3. Bayesian Game Theory & Incomplete Information**

### 3.1 Permainan dengan Informasi Tidak Sempurna
Model diperluas menjadi *Bayesian Game* $\mathcal{G}_{Bayes} = (\mathcal{P}, \mathcal{S}, \Theta, p, \mathcal{U})$, untuk mengakomodasi ketidakpastian mengenai kondisi internal pasar yang tidak teramati secara langsung (*hidden variables*).
*   $\mathcal{P}$: Himpunan pemain (Leader, Follower).
*   $\Theta_k$: Ruang tipe (*type space*) untuk pemain $k$, merepresentasikan "informasi privat" atau sentimen pasar intrinsik (misal: $\Theta = \{\theta_{bull}, \theta_{bear}\}$).
*   $p \in \Delta(\Theta_L \times \Theta_F)$: Distribusi probabilitas gabungan (*common prior*) atas tipe-tipe pemain.

### 3.2 Transformasi Harsanyi dan Beliefs
Masalah informasi tidak sempurna ditransformasikan menjadi permainan informasi imperfektif menggunakan kerangka Harsanyi. Setiap agen $k$ mengetahui tipe aktualnya $\theta_k$, tetapi memiliki ketidakpastian mengenai tipe lawan $\theta_{-k}$.
Agen membentuk *posterior belief* menggunakan **Aturan Bayes**:

$$ p(\theta_{-k} | \theta_k) = \frac{p(\theta_k, \theta_{-k})}{\sum_{\theta'_{-k} \in \Theta_{-k}} p(\theta_k, \theta'_{-k})} \tag{3.1} $$

Dalam model ini, distribusi probabilitas empiris $P(i,j)$ yang diperoleh di Bab 1 berfungsi sebagai *Common Prior* $p(\theta)$ yang objektif.

### 3.3 Bayesian Nash Equilibrium (BNE)
Solusi permainan adalah profil strategi $s_k: \Theta_k \to \mathcal{S}_k$, di mana setiap tipe pemain memilih tindakan untuk memaksimumkan ekspektasi utilitas interimnya (*Interim Expected Utility Maximization*):

$$ s_k^*(\theta_k) \in \arg \max_{s'_k \in \mathcal{S}_k} \sum_{\theta_{-k} \in \Theta_{-k}} p(\theta_{-k} | \theta_k) \cdot \mathcal{U}_k(s'_k, s_{-k}^*(\theta_{-k}), \theta_k, \theta_{-k}) \tag{3.2} $$

Persamaan ini [[Penurunan_3.2]] menyatakan bahwa strategi optimal $s_k^*$ adalah respon terbaik terhadap rata-rata strategi lawan, dibobot oleh keyakinan pemain $k$ terhadap tipe lawan.

### 3.4 Interpretasi Fisik: Quantum Beliefs
Metodologi ini menjembatani teori permainan klasik dan kuantum melalui interpretasi amplitudo $\alpha_{ij}$. Dalam *Quantum Bayesianism* (QBism), fungsi gelombang $\ket{\psi}$ dipandang bukan sebagai realitas fisik objektif, melainkan sebagai representasi matematis dari *belief* agen pengamat.

$$ \ket{\psi} = \sum_{ij} \alpha_{ij} \ket{ij} \implies p(i,j) = |\alpha_{ij}|^2 \tag{3.3} $$

Superposisi koheren $\sum \alpha_{ij}\ket{ij}$ mengizinkan adanya interferensi probabilitas yang tidak mungkin terjadi dalam *Bayesian Game* klasik standar, memberikan derajat kebebasan lebih dalam memodelkan irasionalitas pasar atau korelasi non-klasik.
# **4. Quantum Information Theory & Density Matrices**

### 4.1 Konstruksi Matriks Densitas (Density Operator)
Meskipun sistem awalnya dideskripsikan oleh vektor keadaan murni $\ket{\Psi}$, realitas pasar keuangan yang penuh *noise* sering kali lebih tepat dideskripsikan sebagai *mixed state* (campuran statistik). Formalisme paling umum adalah menggunakan **Operator Densitas** $\rho$.

Untuk *ensemble* keadaan $\{\ket{\psi_k}\}$ dengan probabilitas klasik $p_k$, matriks densitas didefinisikan sebagai:
$$ \rho = \sum_k p_k \ket{\psi_k}\bra{\psi_k} \tag{4.1} $$

Operator ini harus memenuhi tiga sifat fundamental:
1.  **Hermitian**: $\rho^\dagger = \rho$ (observable real).
2.  **Positif Semi-definit**: $\langle \phi | \rho | \phi \rangle \ge 0, \forall \ket{\phi}$.
3.  **Trace Unity**: $\text{Tr}(\rho) = 1$ (Konservasi probabilitas total).

Dalam penelitian ini, kita memulai dengan asumsi *pure state* $\ket{\Psi}$ yang dikonstruksi dari amplitudo $\alpha_{ij}$ data historis, sehingga:
$$ \rho_{sys} = \ket{\Psi}\bra{\Psi} \tag{4.2} $$
Dalam basis komputasi $\{\ket{00}, \ket{01}, \ket{10}, \ket{11}\}$, ini menghasilkan matriks $4 \times 4$. Elemen diagonal $\rho_{ii}$ merepresentasikan populasi (probabilitas klasik), sedangkan elemen non-diagonal $\rho_{ij}$ ($i \neq j$) merepresentasikan **koherensi kuantum** atau interferensi antar kemungkinan sejarah harga.

### 4.2 Reduced Density Matrix (Partial Trace)
Untuk menganalisis properti satu aset (misalnya Leader $L$) tanpa mempedulikan derajat kebebasan aset lainnya (Follower $F$), kita menggunakan operasi **Partial Trace**. Ini adalah satu-satunya operasi pemetaan linear yang konsisten secara fisik untuk menurunkan deskripsi statistik subsistem dari sistem komposit.

Reduced Density Matrix untuk subsistem $L$ didefinisikan sebagai trace parsial terhadap basis $F$:
$$ \rho_L = \text{Tr}_F(\rho_{sys}) = \sum_{k \in \{0,1\}_F} \bra{k}_F \rho_{sys} \ket{k}_F \tag{4.3} $$

Secara eksplisit [[Penurunan_4.3]], jika $\rho_{sys}$ memiliki elemen matriks $\rho_{ij, mn} = \alpha_{ij}\alpha_{mn}^*$ (indeks ganda merepresentasikan basis produk tensor), maka elemen matriks $\rho_L$ (dimensi $2 \times 2$) adalah:

$$
\rho_L = 
\begin{pmatrix}
\rho_{00,00} + \rho_{01,01} & \rho_{00,10} + \rho_{01,11} \\
\rho_{10,00} + \rho_{11,01} & \rho_{10,10} + \rho_{11,11}
\end{pmatrix} \tag{4.4}
$$

Diagonal utama $\rho_L$ ($\rho_{00}^L, \rho_{11}^L$) merepresentasikan probabilitas marjinal aset $L$ untuk naik atau turun.

### 4.3 Koherensi dan Purity
Keadaan subsistem $\rho_L$ dapat diuji tingkat "ketercampurannya" menggunakan parameter **Purity** $\gamma$:
$$ \gamma = \text{Tr}(\rho_L^2) \tag{4.5} $$

*   Jika $\gamma = 1$, subsistem berada dalam *pure state*. Artinya, $L$ tidak ter-entangle dengan $F$.
*   Jika $\gamma < 1$, subsistem berada dalam *mixed state*. Semakin kecil $\gamma$ (minimum $0.5$ untuk sistem 2-dimensi), semakin besar informasi $L$ yang hilang ke (atau terikat dengan) $F$.

Dalam konteks pasar, jika $\rho_L$ menjadi *mixed* meskipun $\rho_{sys}$ murni, ini bukti matematis bahwa harga aset $L$ tidak independen, melainkan merupakan bagian dari fenomena pasar global yang ter-entangle.
# **5. Quantum Entanglement & Entropy Metrics**

### 5.1 Entropi Von Neumann
Ukuran ketidakpastian informasi dalam sistem kuantum diberikan oleh **Entropi Von Neumann**, yang merupakan perluasan dari Entropi Shannon ke dalam domain operator densitas. Untuk matriks densitas $\rho$, entropi didefinisikan sebagai:

$$ S(\rho) = -\text{Tr}(\rho \ln \rho) = -\sum_i \lambda_i \ln \lambda_i \tag{5.1} $$

Di mana $\lambda_i$ adalah nilai eigen (eigenvalues) dari matriks $\rho$. Karena $0 \le \lambda_i \le 1$ dan $\sum \lambda_i = 1$, entropi ini selalu non-negatif.
*   Jika $\rho$ adalah *pure state*, $\lambda = \{1, 0, \dots, 0\}$, sehingga $S(\rho) = 0$.
*   Jika $\rho$ adalah *maximally mixed state*, $S(\rho)$ mencapai maksimum ($\ln d$, di mana $d$ adalah dimensi Hilbert space).
### 5.2 Entanglement Entropy
Untuk sistem bipartit murni $\ket{\Psi}_{LF}$, *Entanglement Entropy* didefinisikan sebagai entropi Von Neumann dari subsistem tereduksinya:

$$ E(\ket{\Psi}) = S(\rho_L) = S(\rho_F) \tag{5.2} $$

Sifat unik sistem kuantum adalah $S(\rho_{sys})$ bisa nol (jika sistem total murni), sementara $S(\rho_L) > 0$. Ini kontras dengan sistem klasik di mana ketidakpastian subsistem tidak bisa melebihi ketidakpastian sistem total. $S(\rho_L) > 0$ menandakan bahwa informasi tidak terlokalisasi pada $L$ saja, tetapi terbagi (shared non-locally) dengan $F$.

### 5.3 Quantum Mutual Information (QMI)
Untuk mengukur total korelasi (baik klasik maupun kuantum) antara Leader dan Follower, digunakan **Quantum Mutual Information**:

$$ I(L:F) = S(\rho_L) + S(\rho_F) - S(\rho_{LF}) \tag{5.3} $$

Dalam econophysics, metrik ini lebih unggul daripada koefisien korelasi Pearson ($\rho_{pearson}$) karena:
1.  **Non-Linearitas**: QMI menangkap hubungan non-linear.
2.  **Basis Independent**: QMI tidak bergantung pada skala harga.
3.  **Super-Additivity**: QMI bisa mendeteksi korelasi yang lebih kuat daripada yang diizinkan statistik klasik.

Secara spesifik, korelasi kuantum (diskordansi) ada jika:
$$ I_{quantum}(L:F) > I_{classic}(L:F) \tag{5.4} $$
Di mana kelebihan informasi ini merepresentasikan *Quantum Entanglement* atau *Quantum Discord*—fenomena di mana pergerakan pasar "terkopel" sedemikian rupa sehingga perubahan pada satu aset secara instan mereduksi ketidakpastian pada aset lainnya melebihi batas informasi Shannon.

### 5.4 Interpretasi Finansial
*   **$I(L:F) \approx 0$**: Pasar efisien dalam bentuk lemah (Random Walk), aset bergerak independen.
*   **$I(L:F)$ Tinggi**: Pasar tidak efisien, terdapat arbitrase informasi atau manipulasi struktural di mana "nasib" kedua aset terikat erat. Kondisi ini sering muncul saat krisis (*market crash*), di mana diversifikasi portofolio gagal karena semua aset menjadi ter-entangle (korelasi $\to 1$).
# **6. Network Theory & Quantum Financial Networks**

### 6.1 Konstruksi Graf Jaringan (QFN)
Pasar dimodelkan sebagai graf berbobot tak berarah $G = (V, E)$, di mana:
*   $V = \{1, \dots, N\}$ adalah himpunan simpul (aset/ticker).
*   $E$ adalah himpunan sisi yang merepresentasikan hubungan informasi.

Bobot sisi $w_{ij}$ antara aset $i$ dan $j$ tidak menggunakan korelasi linear, melainkan **Quantum Mutual Information** yang telah dihitung sebelumnya:
$$ w_{ij} = I(i:j) \tag{6.1} $$
Ini membentuk *Quantum Financial Network* (QFN) yang menangkap topologi aliran informasi non-linear dan ketergantungan kuantum di pasar.

### 6.2 Matriks Adjasensi Spektral
Struktur jaringan direpresentasikan oleh Matriks Adjasensi $A \in \mathbb{R}^{N \times N}$:
$$ A_{ij} = \begin{cases} I(i:j) & \text{jika } i \neq j \\ 0 & \text{jika } i = j \end{cases} \tag{6.2} $$
Matriks ini simetris ($A_{ij} = A_{ji}$) dan real, menjamin bahwa spektrum nilai eigennya bersifat real, yang penting untuk interpretasi fisik.

### 6.3 Sentralitas Eigenvector (Identifikasi Market Leader)
Untuk mengidentifikasi aset yang paling berpengaruh (Leader Global), digunakan metrik **Eigenvector Centrality**. Konsepnya adalah simpul menjadi penting jika terhubung dengan simpul lain yang juga penting. Sentralitas $x_i$ dari node $i$ didefinisikan sebagai:

$$ x_i = \frac{1}{\lambda} \sum_{j \in V} A_{ij} x_j \tag{6.3} $$

Dalam notasi matriks, persamaan ini menjadi masalah nilai eigen:
$$ A \mathbf{x} = \lambda \mathbf{x} \tag{6.4} $$

Berdasarkan **Teorema Perron-Frobenius**, untuk matriks tak-negatif terhubung (irreducible), terdapat nilai eigen terbesar (dominan) $\lambda_{max}$ yang unik dan positif. Vektor eigen utama $\mathbf{v}_{max}$ yang berkorespondensi dengannya memiliki komponen yang semuanya non-negatif.
Komponen $v_i$ dari vektor $\mathbf{v}_{max}$ merepresentasikan "bobot pengaruh" aset $i$. Aset dengan nilai $v_i$ tertinggi diidentifikasi sebagai **Market Leader** atau pusat gravitasi informasi dalam jaringan.

### 6.4 Topologi Minimum Spanning Tree (MST)
Untuk memvisualisasikan "tulang punggung" pasar dan mereduksi kompleksitas topologi, graf lengkap direduksi menjadi MST.
Transformasi metrik jarak dilakukan dengan memetakan QMI ke ruang metrik Euklidian:
$$ d_{ij} = \sqrt{2(1 - I'_{ij})} \tag{6.5} $$
Di mana $I'_{ij}$ adalah QMI yang dinormalisasi ke $[0,1]$.

Algoritma optimasi (seperti Prim atau Kruskal) digunakan untuk mencari himpunan sisi $E_{MST} \subset E$ yang menghubungkan semua simpul dengan total jarak minimum:
$$ \min \sum_{(i,j) \in E_{MST}} d_{ij} \tag{6.6} $$
Struktur MST ini mengungkapkan hierarki taksonomi alami aset (misal: pengelompokan sektor secara otomatis) tanpa pengawasan eksternal (*unsupervised clustering*).
# **7. Hamiltonian Mechanics & Quantum Dynamics**

### 7.1 Model Ising Finansial
Dinamika sistem keuangan dipetakan ke dalam **Model Ising Transversal** atau Hamiltonian Spin-1/2 umum. Hamiltonian total $H$ merepresentasikan "Energi Pasar" (Cost Function), di mana keadaan energi rendah berkorespondensi dengan konfigurasi pasar yang stabil.
$$ H = H_{local} + H_{int} $$

### 7.2 Pemetaan Parameter (Inverse Problem)
Tantangan utama adalah merekonstruksi operator $H$ dari data statistik (*Inverse Ising Problem*). Kita memetakan variabel payoff dan informasi menjadi koefisien fisik:

1.  **External Field ($h_i$):** Merepresentasikan bias intrinsik atau sentimen fundamental aset $i$.
    $$ h_i \propto \frac{1}{2} (\bar{u}_{i,\uparrow} - \bar{u}_{i,\downarrow}) $$
    Di mana $\bar{u}$ adalah rata-rata payoff marjinal. Dalam representasi operator tensor product:
    $$ H_{local} = -h_L (\sigma_z \otimes I) - h_F (I \otimes \sigma_z) $$

2.  **Exchange Interaction ($J_{ij}$):** Merepresentasikan kekuatan koupling strategis antar aset.
    $$ J_{ij} = \text{sgn}(Corr_{ij}) \cdot I(i:j) $$
    Di mana $I(i:j)$ adalah Quantum Mutual Information.
    $$ H_{int} = -J_{LF} (\sigma_z \otimes \sigma_z) $$
    *   $J > 0$ (Ferromagnetik): *Coordination Game* (aset bergerak searah, energi diminimalkan saat spin sejajar).
    *   $J < 0$ (Antiferromagnetik): *Hedging/Substitution* (aset bergerak berlawanan).

### 7.3 Spektrum Energi & Ground State
Melalui diagonalisasi matriks $H$ (eigendecomposition), kita memperoleh spektrum energi:
$$ H \ket{\psi_n} = E_n \ket{\psi_n} $$

State dengan energi terendah, $\ket{\psi_g}$ (**Ground State**), merepresentasikan **Ekuilibrium Pasar Global**.
*   Jika sistem berada di $\ket{\psi_g}$, pasar dalam kondisi stabil paling optimal.
*   Selisih energi $\Delta E = E_1 - E_g$ (gap energi) mengukur ketahanan pasar terhadap eksitasi (stabilitas terhadap guncangan).

### 7.4 Evolusi Waktu (Persamaan Schrödinger)
Untuk memprediksi dinamika probabilitas pasar di masa depan ($t > 0$), kita menerapkan operator evolusi uniter $U(t)$ pada state saat ini $\ket{\psi(0)}$:

$$ \ket{\psi(t)} = e^{-iHt/\hbar} \ket{\psi(0)} $$

Probabilitas menemukan pasar dalam konfigurasi $\ket{k}$ pada waktu $t$ adalah:
$$ P_k(t) = |\bra{k} e^{-iHt/\hbar} \ket{\psi(0)}|^2 $$
Ini memungkinkan prediksi non-linear tentang bagaimana probabilitas bersama (joint probability) berevolusi seiring waktu.

### 7.5 Interpretasi Termodinamika
Dalam kondisi ekuilibrium termal (pasar efisien), probabilitas okupansi state mengikuti **Distribusi Boltzmann**:
$$ P_n = \frac{1}{Z} e^{-E_n / k_B T_{mkt}} $$
Di mana $T_{mkt}$ adalah "Suhu Pasar" yang berbanding lurus dengan volatilitas sistemik, dan $Z = \text{Tr}(e^{-\beta H})$ adalah Fungsi Partisi.
Krisis pasar dapat dipandang sebagai *Phase Transition* di mana $T_{mkt}$ meningkat drastis, menyebabkan sistem tereksitasi dari Ground State ke keadaan energi tinggi yang lebih acak namun sangat ter-entangle.
