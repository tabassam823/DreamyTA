# Penurunan Model Markowitz ke Ising Hamiltonian (Pendekatan QMI & Game Theory)

Dokumen ini menjelaskan modifikasi model Markowitz menggunakan parameter berbasis informasi kuantum dan teori permainan untuk optimasi portofolio pada perangkat kuantum.

## 1. Pendahuluan: Formulasi Energi Baru
Dalam pendekatan ini, fungsi energi tidak lagi hanya menggunakan statistik klasik (mean-variance), melainkan mengintegrasikan korelasi total (Quantum Mutual Information) dan strategi marginal dari payoff matrix.

Secara matematis, Hamiltonian target dinyatakan sebagai:
$$ \hat{H} = \sum_{i < j} J_{ij} \hat{Z}_i \hat{Z}_j + \sum_i h_i \hat{Z}_i + A \left(\sum_i \hat{x}_i - K \right)^2 $$

Dimana:
- $J_{ij}$: Interaksi antar aset berbasis **Quantum Mutual Information**.
- $h_i$: Bias individu berbasis **Marginal Payoff** dari Game Theory.
- $A$: Penalti batasan jumlah aset $K$.

---

## 2. Detail Komponen Berbasis Data

### A. Interaksi Aset: Quantum Mutual Information (QMI)
Alih-alih menggunakan kovarians klasik ($\Sigma_{ij}$), kita menggunakan QMI untuk menangkap korelasi total (klasik + kuantum) antar aset. Jika kita merepresentasikan dinamika aset dalam density matrix $\rho_{ij}$:

$$ J_{ij} \propto \mathcal{I}(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) $$

Dimana:
- $S(\rho) = -\text{Tr}(\rho \log \rho)$ adalah Entropi Von Neumann.
- $\mathcal{I}(i:j)$ mengukur seberapa banyak informasi yang dibagikan antar aset. Nilai QMI yang tinggi menunjukkan dependensi yang kuat yang harus diminimalkan untuk diversifikasi.

### B. Bias Aset: Marginal Payoff (Game Theory)
Penentuan parameter linear ($h_i$) dilakukan dengan memodelkan pemilihan aset sebagai permainan (*game*). Misalkan terdapat matriks payoff $M$ yang merepresentasikan keuntungan relatif aset $i$ terhadap kondisi pasar $j$:

1. Kita hitung probabilitas kondisi pasar (Nash Equilibrium atau distribusi empiris) $p_j$.
2. Kita hitung **Marginal Payoff** untuk setiap aset $i$:
   $$ \pi_i = \sum_j M_{ij} p_j $$
3. Parameter bias $h_i$ ditentukan berbanding terbalik dengan payoff (karena kita meminimalkan energi):
   $$ h_i = -\lambda \pi_i $$

---

## 3. Transformasi ke Ising Hamiltonian
Dengan parameter $J_{ij}$ (dari QMI) dan $h_i$ (dari Game Theory), kita membentuk QUBO yang kemudian dikonversi ke Ising melalui substitusi biner ke spin ($x_i \to \frac{1-s_i}{2}$).

Format akhir Hamiltonian Ising untuk 2 aset ($K=1$):
$$ \hat{H} = J_{12} \hat{Z}_1 \hat{Z}_2 + (h_1 + P_{bias1}) \hat{Z}_1 + (h_2 + P_{bias2}) \hat{Z}_2 + \text{offset} $$
Dimana $P_{bias}$ adalah kontribusi linear dari ekspansi penalti batasan $A(\sum x_i - K)^2$.

---

## 4. Optimasi Variasional: SPSA
Untuk menemukan ground state (bobot portofolio optimal), kita menggunakan ansatz $|\psi(\theta)\rangle$ dan mengoptimalkan parameter $\theta$ menggunakan **Simultaneous Perturbation Stochastic Approximation (SPSA)**.

### Mengapa SPSA?
Berbeda dengan Gradient Descent (GD) yang memerlukan $2N$ evaluasi sirkuit untuk gradien, SPSA hanya memerlukan **2 evaluasi** per iterasi, terlepas dari jumlah parameter, sehingga sangat efisien untuk perangkat kuantum berderau (NISQ).

### Algoritma SPSA:
1. **Perturbasi Simultan:** Bangkitkan vektor acak $\Delta_k$ dari distribusi Bernoulli.
2. **Estimasi Gradien:**
   $$ \hat{g}_k(\theta_k) = \frac{E(\theta_k + c_k \Delta_k) - E(\theta_k - c_k \Delta_k)}{2 c_k \Delta_k} $$
3. **Update Parameter:**
   $$ \theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k) $$
   Dimana $a_k$ dan $c_k$ adalah *learning rates* yang mengecil seiring bertambahnya iterasi $k$.

---

## 5. Ekspektasi Energi
Nilai yang diminimalkan oleh SPSA adalah:
$$ \min_{\theta} \langle E(\theta) \rangle = \langle \psi(\theta) | \hat{H}_{QMI+Game} | \psi(\theta) \rangle $$

Output akhir adalah distribusi probabilitas dari state $|x_1 x_2 \dots x_N\rangle$. State dengan probabilitas tertinggi yang memenuhi batasan $\sum x_i = K$ adalah portofolio optimal hasil integrasi Game Theory dan Quantum Information.
