## Grup 1: Formalisme Teori Permainan Klasik
**Tujuan:** Menemukan definisi matematika yang ketat untuk "Game", "Strategy Space", dan "Nash Equilibrium".

### 1. Definisi Formal Permainan (Tuple) & Ruang Strategi
*Sumber: `Introduction_to_Quantum_Game_Theory.pdf` & `On_Correlated_Equilibria...pdf`*

*   **Definisi Tuple (Pure Strategy):**
    Sebuah permainan strategi murni dengan $n$-pemain didefinisikan oleh tuple ruang strategi $\mathcal{S}$ dan fungsi payoff $\pi$:
    $$ \mathcal{S} = (S_1, S_2, \dots, S_n) $$
    $$ \pi = (\pi_1, \pi_2, \dots, \pi_n) $$
    Di mana $S_i = \{s_i^1, s_i^2, \dots \}$ adalah himpunan strategi murni pemain ke-$i$.

*   **Definisi Bentuk Strategis (Normal Form):**
    Permainan adalah *ordered triple* $(N, (S_i)_{i \in N}, (u_i)_{i \in N})$ di mana:
    *   $N$: Himpunan pemain.
    *   $S_i$: Himpunan strategi pemain $i$.
    *   $u_i$: Fungsi payoff pemain $i$.

### 2. Nash Equilibrium (Definisi Matematis)
*Sumber: `On_Correlated_Equilibria...pdf` & `Introduction_to_Quantum_Game_Theory.pdf`*

*   **Formulasi Umum:**
    Vektor strategi $s^* = (s_1^*, \dots, s_n^*)$ adalah Nash Equilibrium jika untuk setiap pemain $i$ dan setiap strategi $s_i \in S_i$:
    $$ u_i(s^*) \geq u_i(s_i, s^*_{-i}) $$
    *(Artinya: Payoff pemain $i$ tidak meningkat jika ia mengubah strateginya secara sepihak).*

*   **Formulasi Matriks Payoff:**
    $$ \pi_i(s_1^{e_1}, \dots, s_i^{e_i}, \dots, s_n^{e_n}) \geq \pi_i(s_1^{e_1}, \dots, s_i^{\alpha_i}, \dots, s_n^{e_n}) $$
    untuk semua $s_i^{\alpha_i} \in S_i$.

### 3. Konsep Pareto Optimality & Dominant Strategy
*Sumber: `Introduction_to_Quantum_Game_Theory.pdf`*

*   **Dominant Strategy:** Strategi $s_i^D$ yang memaksimalkan payoff pemain $i$ terlepas dari strategi pemain lain.
*   **Pareto Dominance:**
    Sebuah permainan $\mathcal{P}$ dikatakan *Pareto-Dominate* $\mathcal{P}'$ jika:
    $$ \pi_i(\mathcal{P}) \geq \pi_i(\mathcal{P}') \quad \forall i $$
    dengan pertidaksamaan ketat berlaku minimal untuk satu pemain.

### 4. Teori Permainan Bayesian
*Sumber: `Linking_quantum_discord_with_Bayesian_game_theory.pdf`*

*   **Expected Payoff ($u_A$):**
    Relevan untuk situasi dengan informasi tidak lengkap (ketidakpastian tipe pemain).
    $$ u_A = \sum_{\sigma, \sigma', \alpha, \beta} P_A(\alpha, \beta) P(\sigma \sigma' | \alpha \beta) u^{\alpha, \beta}_{\sigma, \sigma', A} $$
    *   $P_A$: Prior belief.
    *   $u^{\dots}$: Payoff tensor.

### 5. Aplikasi Ekonomi (Barro-Gordon Game)
*Sumber: `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`*

*   **Fungsi Utilitas Pembuat Kebijakan:**
    $$ U^{pol}_t = \theta b (\pi_t - \pi_t^e) - \frac{a \pi_t^2}{2} $$
    Contoh konkret penerapan fungsi payoff dalam variabel ekonomi makro (inflasi).

---

## Grup 2: Protokol Kuantisasi (EWL & Marinatto-Weber)
**Tujuan:** Menemukan persamaan evolusi state, operator unitary, dan operator payoff untuk Sub-bab "Protokol Permainan Kuantum".

### 1. Protokol Marinatto-Weber (MW)
*Sumber: `On_Correlated_Equilibria...pdf` & `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`*

*   **Keadaan Awal ($|\Psi_{in}\rangle$):**
    $$ |\Psi_{in}\rangle = \sum_{i,j} \alpha_{ij} |i\rangle_A \otimes |j\rangle_B $$
    Di mana $\alpha_{ij}$ adalah amplitudo probabilitas kompleks pada basis komputasi.

*   **Strategi Pemain:**
    Pemain menerapkan strategi melalui operator uniter $U_A$ dan $U_B$.
    $$ |\Psi_f\rangle = (U_A \otimes U_B) |\Psi_{in}\rangle $$
    Contoh himpunan strategi: $\mathcal{S} = \{I, \sigma_x, \dots \}$.

*   **Operator Payoff (Pengukuran):**
    $$ u_k = \text{Tr}(|\Psi_f\rangle\langle\Psi_f| M_k) $$
    Di mana $M_k = \sum_{i,j} a_{ij} |ij\rangle\langle ij|$ adalah operator payoff yang dibangun dari matriks payoff klasik.

### 2. Protokol Eisert-Wilkens-Lewenstein (EWL)
*Sumber: `Introduction_to_Quantum_Game_Theory.pdf`*

*   **Initial State dengan Entanglement ($J$):**
    Protokol ini menggunakan operator entangling $J$ pada keadaan awal $|00\rangle$.
    $$ |\psi_{in}\rangle = J |00\rangle $$
    Umumnya, $J = e^{i\gamma \sigma_x \otimes \sigma_x / 2}$.

*   **Strategi Unitary ($U(\theta, \phi)$):**
    Strategi parametrik 1-qubit:
    $$ U(\theta, \phi) = \begin{pmatrix} e^{i\phi}\cos(\theta/2) & i e^{i\phi}\sin(\theta/2) \\ i e^{-i\phi}\sin(\theta/2) & e^{-i\phi}\cos(\theta/2) \end{pmatrix} $$

*   **State Akhir & Disentanglement:**
    $$ |\psi_f\rangle = J^\dagger (U_A \otimes U_B) J |00\rangle $$

### 3. Matriks Densitas dalam Permainan
*Sumber: `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`*

*   **Evolusi Mixed State:**
    Penting untuk memodelkan pasar dengan *noise* atau informasi tidak lengkap.
    $$ \rho_f = (U_A \otimes U_B) \rho_{in} (U_A^\dagger \otimes U_B^\dagger) $$
## Grup 3: Koneksi Model Ising & Optimasi
**Tujuan:** Menemukan narasi atau persamaan yang secara eksplisit menghubungkan pencarian Ground State pada Hamiltonian Ising dengan pencarian solusi optimal (biaya terendah) dalam ekonomi/game theory.

### 1. Pemetaan Travelling Salesman Problem (TSP) ke Model Ising
*Sumber: `Important_Quantum_Gates_for_Quantum_Algorithms_of_Travelling_Salesman_Problem.pdf` (Sinaga et al., 2023)*

*   **Fungsi Biaya (Cost Function) TSP:**
    Dinyatakan sebagai total jarak atau bobot perjalanan $w_{i,j}$ untuk mengunjungi $N$ kota:
    $$ C_{cost} = \sum_{0 \leq i,j < N} w_{i,j} \sum_{t=0}^{N-1} x_{i,t} x_{j,t+1} $$
    Di mana $x_{i,t} = 1$ jika kota $i$ dikunjungi pada waktu $t$, dan 0 sebaliknya.

*   **Pemetaan ke Variabel Spin:**
    Untuk mengonstruksi Hamiltonian Ising, variabel biner $x_{i,t}$ dipetakan ke variabel spin $\sigma_{i,j}^z$ (Pauli-Z) menggunakan transformasi:
    $$ x_{i,t} = \frac{I - \sigma_{i,j}^z}{2} $$

*   **Hamiltonian Biaya (Cost Hamiltonian):**
    Menggabungkan fungsi biaya dan penalti (untuk memastikan batasan TSP terpenuhi):
    $$ H_C = H_{TSP} = H_{cost} + H_{penalty} = \sum_{i} c_i \sigma_i^z + \sum_{i,j} c_{i,j} \sigma_i^z \sigma_j^z $$
    Mencari solusi optimal TSP ekuivalen dengan mencari keadaan dasar (ground state) yang meminimalkan ekspektasi nilai Hamiltonian ini.

### 2. Hamiltonian Ising & Distribusi Boltzmann
*Sumber: `Quantum-enhanced Markov chain Monte Carlo.pdf` (Layden et al., 2022)*

*   **Definisi Model Ising Klasik:**
    Didefinisikan oleh konfigurasi spin $s = (s_1, \dots, s_n)$ dengan $s_j = \pm 1$. Energi dari konfigurasi spin diberikan oleh Hamiltonian:
    $$ E(s) = - \sum_{j>k=1}^n J_{jk} s_j s_k - \sum_{j=1}^n h_j s_j $$
    *   $J_{jk}$: Kopling interaksi antar spin (Couplings).
    *   $h_j$: Medan eksternal (Fields).

*   **Distribusi Boltzmann:**
    Probabilitas menemukan sistem dalam konfigurasi $s$ pada suhu $T$ adalah:
    $$ \mu(s) = \frac{1}{Z} e^{-E(s)/T} $$
    Dalam limit suhu rendah ($T \to 0$), sampling dari distribusi ini ekuivalen dengan meminimalkan $E(s)$, yang merupakan masalah NP-hard (seperti pada *spin glasses* atau masalah optimasi kombinatorial lainnya).

*   **Koneksi ke Optimasi:**
    Banyak masalah optimasi kombinatorial dapat dipetakan ke minimisasi energi model Ising. Algoritma kuantum (seperti QAOA atau Quantum MCMC) bertujuan untuk menemukan keadaan energi terendah ini lebih efisien daripada metode klasik.

## Grup 4: Dinamika Stokastik (GBM/BSDE) sebagai Konteks Pasar
**Tujuan:** Menemukan persamaan yang mendeskripsikan dinamika pasar (seperti Gerak Brown) yang bisa kita bingkai sebagai "lingkungan yang bising" atau "state awal" dalam permainan kuantum.

### 1. Libor Market Model (LMM) & Dinamika Forward Rate
*Sumber: `Deep_Learning-Based_BSDE_Solver_for_Libor.pdf` (Wang et al., 2018)*

*   **Dinamika Forward Libor Rate:**
    Laju forward Libor $L_n(t)$ dimodelkan sebagai proses stokastik yang mengikuti SDE (Stochastic Differential Equation) di bawah *forward measure* $Q^{T_{n+1}}$:
    $$ dL_n(t) = \sigma_n(t, L_n(t)) dW^{n+1}(t) $$ 
    Di mana $W^{n+1}(t)$ adalah Gerak Brown standar berdimensi $d$.

*   **Struktur Korelasi:**
    Model LMM sering menggunakan struktur korelasi antar rate yang dimodelkan dengan fungsi eksponensial, misal $\rho_{ij} = \exp(-\beta|i-j|)$, yang mencerminkan ketergantungan antar tenor yang berbeda.

*   **Persamaan BSDE (Backward SDE) untuk Pricing:**
    Penetapan harga opsi (seperti Swaption) dapat diformulasikan sebagai masalah BSDE:
    $$ dY(t) = Z(t)\Sigma(t, L(t))dW(t) $$ 
    $$ Y(T) = g(L(T)) $$ 
    Di mana $Y(t)$ adalah harga opsi terdiskonto, dan $Z(t)$ terkait dengan strategi lindung nilai (hedging/Greeks). Pendekatan *Deep Learning* digunakan untuk memecahkan BSDE dimensi tinggi ini, mengatasi "Curse of Dimensionality".

### 2. Model Black-Scholes Fraktal
*Sumber: `Qualitative_financial_modelling_in_fractal_dimensions.pdf` (El-Nabulsi & Anukool, 2025)*

*   **Keterbatasan Black-Scholes Klasik:**
    Model klasik mengasumsikan volatilitas konstan dan distribusi normal (Gaussian), yang gagal menangkap fenomena "fat tails" dan *long-range dependence* (memori jangka panjang) di pasar nyata.

*   **Persamaan Black-Scholes Fraktal (Generalized BSE):**
    Menggunakan operator turunan fraktal (fractal derivative) untuk memperhitungkan dimensi fraktal ruang dan waktu ($S^\alpha, t^\beta$). Bentuk umum persamaan ini:
    $$ \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2(t)S^2 \frac{\partial^2 V}{\partial S^2} + (r(t) - D(t))S \frac{\partial V}{\partial S} - r(t)V = 0 $$ 
    Namun dengan parameter yang mengikuti *power-laws*:
    *   Volatilitas: $\sigma^2(t) = \sigma_0^2 t^\gamma$
    *   Suku bunga: $r(S,t) = r_0 t^\xi S^{\alpha-1}$
    *   Dimensi fraktal ($\alpha, \beta$) mempengaruhi solusi harga opsi secara signifikan, terutama untuk *out-of-the-money options*.

*   **Relevansi:**
    Konsep dimensi fraktal dan *power-laws* ini sangat relevan untuk memodelkan "noise" atau ketidakpastian pasar yang lebih realistis dalam *mixed state* matriks densitas kuantum, di mana pasar tidak sepenuhnya acak (acak murni) tetapi memiliki struktur fraktal.