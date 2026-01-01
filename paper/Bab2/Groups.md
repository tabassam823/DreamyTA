  1. Definisi Formal Permainan (Tuple) & Ruang Strategi
  Referensi terbaik ditemukan pada file `2305.00368v1.pdf` (Introduction to Quantum Game Theory) dan
  `On_Correlated_Equilibria...pdf`.

   * Definisi Game sebagai Tuple:
       * Dari 2305.00368v1.pdf (Eq. 1-2):
          Sebuah permainan strategi murni dengan $n$-pemain didefinisikan oleh tuple ruang strategi $\mathcal{S}$ dan fungsi
  payoff $\pi$:
          $$ \mathcal{S} = (S_1, S_2, \dots, S_n) $$
          $$ \pi = (\pi_1, \pi_2, \dots, \pi_n) $$
          Di mana $S_i = \{s_i^1, s_i^2, \dots \}$ adalah himpunan strategi murni pemain ke-$i$.
       * Dari On_Correlated_Equilibria...pdf (Definisi 1):
          Permainan dalam bentuk strategis (normal) adalah ordered triple $(N, (S_i)_{i \in N}, (u_i)_{i \in N})$ di mana $N$
  adalah himpunan pemain, $S_i$ adalah himpunan strategi, dan $u_i$ adalah fungsi payoff.

  2. Nash Equilibrium (Definisi Matematis)
  Kedua paper di atas memberikan pertidaksamaan formal yang Anda butuhkan untuk mendefinisikan Nash Equilibrium secara ketat.

   * Formulasi Umum:
      Dari On_Correlated_Equilibria...pdf (Definisi 2, Eq. 2):
      Vektor strategi $s^ = (s_1^, \dots, s_r^*)$ adalah Nash Equilibrium jika untuk setiap pemain $i$ dan setiap strategi
  $s_i \in S_i$:
      $$ u_i(s^*) \geq u_i(s_i, s^*_{-i}) $$
      *(Artinya: Payoff pemain tidak akan meningkat jika ia mengubah strateginya sendiri $s_i$ sementara pemain lain
  $s^*_{-i}$ tetap).*

   * Formulasi dalam Konteks Matriks Payoff:
      Dari 2305.00368v1.pdf:
      $$ \pi_i(s_1^{e_1}, \dots, s_i^{e_i}, \dots, s_n^{e_n}) \geq \pi_i(s_1^{e_1}, \dots, s_i^{\alpha_i}, \dots, s_n^{e_n})
  $$
      untuk semua $s_i^{\alpha_i} \in S_i$.

  3. Konsep Pareto Optimality & Dominant Strategy
  Ditemukan di `2305.00368v1.pdf`.

   * Dominant Strategy: Strategi $s_i^D$ yang memaksimalkan payoff pemain $i$ apa pun yang dilakukan pemain lain.
   * Pareto Dominance:
      Sebuah permainan (play) $\mathcal{P}$ dikatakan Pareto-Dominate $\mathcal{P}'$ jika:
      $$ \pi_i(\mathcal{P}) \geq \pi_i(\mathcal{P}') \quad \forall i $$
      dan pertidaksamaan ketat berlaku setidaknya untuk satu pemain.

  4. Teori Permainan Bayesian & Payoff Tensor
  Ditemukan di `Linking_quantum_discord_with_Bayesian_game_theory.pdf`.

  Ini relevan jika Anda ingin memperluas definisi permainan ke situasi dengan informasi tidak lengkap (ketidakpastian tipe
  pemain).
   * Expected Payoff ($u_A$):
      $$ u_A = \sum_{\sigma, \sigma', \alpha, \beta} P_A(\alpha, \beta) P(\sigma \sigma' | \alpha \beta) u^{\alpha,
  \beta}_{\sigma, \sigma', A} $$
      Di mana $P_A$ adalah prior belief, dan $u^{\dots}$ adalah payoff tensor.

  5. Aplikasi Ekonomi (Barro-Gordon Game)
  Ditemukan di `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`.

  Memberikan contoh konkret fungsi utilitas (payoff) dalam ekonomi makro:
   * Fungsi Utilitas Pembuat Kebijakan ($U^{pol}$):
      $$ U^{pol}_t = \theta b (\pi_t - \pi_t^e) - \frac{a \pi_t^2}{2} $$
      Ini adalah contoh bagus untuk menunjukkan bagaimana "permainan" diterapkan dalam variabel ekonomi nyata (inflasi).

  ---
  1. Protokol Kuantisasi Marinatto-Weber (MW)
  Referensi utama: `On_Correlated_Equilibria...pdf` (halaman 4, 10) dan `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf`
  (halaman 6-7).

   * Ruang Hilbert Keadaan Awal ($|\Psi_{in}\rangle$):
      Dalam skema MW, keadaan awal sistem gabungan didefinisikan sebagai:
      $$ |\Psi_{in}\rangle = \sum_{i,j} \alpha_{ij} |i\rangle_A \otimes |j\rangle_B $$
      Di mana $|i\rangle_A$ dan $|j\rangle_B$ adalah basis komputasi untuk pemain A dan B. $\alpha_{ij}$ adalah amplitudo
  probabilitas kompleks.

   * Strategi Pemain (Operator Identitas & Flip):
      Pemain A dan B menerapkan strategi mereka, yang diwakili oleh operator uniter $U_A$ dan $U_B$, pada qubit masing-masing.
  Dalam kasus sederhana (permainan $2 \times 2$), strategi seringkali terbatas pada:
      $$ \mathcal{S} = \{I, \sigma_x, \dots \} $$
      Keadaan akhir setelah strategi diterapkan adalah:
      $$ |\Psi_f\rangle = (U_A \otimes U_B) |\Psi_{in}\rangle $$

   * Operator Payoff (Pengukuran):
      Payoff pemain $k$ ($u_k$) dihitung sebagai nilai ekspektasi dari operator payoff $M_k$:
      $$ u_k = \text{Tr}(|\Psi_f\rangle\langle\Psi_f| M_k) $$
      Operator payoff $M_k$ didefinisikan berdasarkan matriks payoff klasik. Misalnya untuk pemain 1:
      $$ M_1 = \sum_{i,j} a_{ij} |ij\rangle\langle ij| $$
      Di mana $a_{ij}$ adalah elemen matriks payoff klasik.

  2. Protokol Eisert-Wilkens-Lewenstein (EWL)
  Referensi utama: `Introduction_to_Quantum_Game_Theory.pdf` (halaman 13-15).

   * Operator Entanglement ($J$):
      Protokol EWL menggunakan operator entangling $J$ pada keadaan awal $|00\rangle$ untuk menciptakan korelasi kuantum sebelum permainan dimulai:
      $$ |\psi_{in}\rangle = J |00\rangle $$
      Biasanya $J = e^{i\gamma \sigma_x \otimes \sigma_x / 2}$.

   * Strategi Unitary ($U(\theta, \phi)$):
      Pemain memilih strategi dari kumpulan operator uniter 1-qubit yang diparameterisasi:
      $$ U(\theta, \phi) = \begin{pmatrix} e^{i\phi}\cos(\theta/2) & i e^{i\phi}\sin(\theta/2) \\ i e^{-i\phi}\sin(\theta/2) &
  e^{-i\phi}\cos(\theta/2) \end{pmatrix} $$

   * Keadaan Akhir & Disentanglement ($J^\dagger$):
      Setelah strategi diterapkan, operator inverse $J^\dagger$ diterapkan sebelum pengukuran:
      $$ |\psi_f\rangle = J^\dagger (U_A \otimes U_B) J |00\rangle $$

  3. Matriks Densitas dalam Permainan
  Referensi utama: `Quantum_Barro-Gordon_Game_in_Monetary_Economics.pdf` (halaman 7) dan
  `Introduction_to_Quantum_Game_Theory.pdf` (halaman 18-19).

   * Evolusi Keadaan Campuran:
      Jika keadaan awal adalah matriks densitas $\rho_{in}$ (bukan vektor murni $|\psi\rangle$), evolusi sistem menjadi:
      $$ \rho_f = (U_A \otimes U_B) \rho_{in} (U_A^\dagger \otimes U_B^\dagger) $$
      Ini sangat relevan untuk memodelkan pasar dengan noise atau informasi tidak lengkap.

