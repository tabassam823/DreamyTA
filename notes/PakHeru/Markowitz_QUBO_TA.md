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

### A. Interaksi Aset: Quantum Mutual Information ([[QMI]])
Alih-alih menggunakan kovarians klasik ($\Sigma_{ij}$), kita menggunakan QMI untuk menangkap korelasi total (klasik + kuantum) antar aset. Jika kita merepresentasikan dinamika aset dalam density matrix $\rho_{ij}$:

$$ J_{ij} \propto \mathcal{I}(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij}) $$

Dimana:
- $S(\rho) = -\text{Tr}(\rho \log \rho)$ adalah Entropi Von Neumann.
- $\mathcal{I}(i:j)$ mengukur seberapa banyak informasi yang dibagikan antar aset. Nilai QMI yang tinggi menunjukkan dependensi yang kuat yang harus diminimalkan untuk diversifikasi.

### B. Bias Aset: Marginal Payoff (Game Theory)
Dalam Tugas Akhir ini, penentuan parameter bias ($h_i$) dilakukan dengan memodelkan interaksi aset sebagai permainan strategi. Langkah-langkahnya adalah:

1. **Definisi Utilitas (Payoff):**
   Kita menggunakan fungsi utilitas risk-return yang disesuaikan dengan parameter risk-aversion $\lambda$:
   $$ u_i(t) = (1 - \lambda) R_{i,t} - \lambda |R_{i,t}| $$
   Dimana $R_{i,t}$ adalah return tahunan pada waktu $t$.

2. **Matriks Payoff Pasangan:**
   Untuk setiap pasangan aset $(i, j)$, kita membentuk matriks payoff berdasarkan kondisi pasar biner ($0$: Up, $1$: Down). Elemen matriks $M_{i,j}(s_i, s_j)$ adalah rata-rata utilitas aset $i$ ketika aset $i$ berada pada kondisi $s_i$ dan aset $j$ pada kondisi $s_j$.

3. **Perhitungan Bias Marginal ($h_i$):**
   Bias untuk aset $i$ dihitung sebagai selisih rata-rata utilitas (Marginal Utility Difference) antara kondisi "Down" dan "Up", yang dirata-ratakan terhadap seluruh pasangan aset lain:
   $$ h_i = \frac{1}{N-1} \sum_{j \neq i} \left[ \mathbb{E}(u_i | s_i = 1) - \mathbb{E}(u_i | s_i = 0) \right] $$
   Secara spesifik di kode:
   $$ h_i = \frac{1}{N-1} \sum_{j \neq i} \left[ (M_{i,j}(1,0) + M_{i,j}(1,1)) - (M_{i,j}(0,0) + M_{i,j}(0,1)) \right] $$
   
Parameter $h_i$ ini menangkap "ketahanan strategis" aset terhadap perubahan kondisi pasar, yang kemudian digunakan sebagai koefisien untuk operator $\hat{Z}_i$ dalam Hamiltonian Ising.

---

## 3. Transformasi ke Ising Hamiltonian
Dengan parameter $J_{ij}$ (dari QMI) dan $h_i$ (dari Game Theory), kita membentuk QUBO yang kemudian dikonversi ke Ising melalui substitusi biner ke spin ($x_i \to \frac{1-s_i}{2}$).

Format akhir Hamiltonian Ising untuk 2 aset ($K=1$):
$$ \hat{H} = J_{12} \hat{Z}_1 \hat{Z}_2 + (h_1 + P_{bias1}) \hat{Z}_1 + (h_2 + P_{bias2}) \hat{Z}_2 + \text{offset} $$
Dimana $P_{bias}$ adalah kontribusi linear dari ekspansi penalti batasan $A(\sum x_i - K)^2$.

---

## 4. Ekspektasi Energi dan Variational Kuantum
Untuk mencari solusi (ground state), kita menggunakan ansatz state $|\psi(\theta)\rangle$ sebagai representasi state portofolio:
$$ |\psi(\theta_1, \theta_2)\rangle = R_y(\theta_1)|0\rangle \otimes R_y(\theta_2)|0\rangle $$
Dimana $R_y(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ adalah gerbang rotasi kuantum yang parameternya akan dioptimasi.

Nilai ekspektasi energi (objektif) yang dihitung pada sirkuit kuantum adalah:
$$ \langle E(\theta) \rangle = \langle \psi(\theta) | \hat{H} | \psi(\theta) \rangle $$
$$ \langle E(\theta) \rangle = J_{12}\langle \hat{Z}_1\hat{Z}_2 \rangle + h_1\langle \hat{Z}_1 \rangle + h_2\langle \hat{Z}_2 \rangle + \text{const} $$

Karena untuk operator Pauli-Z, $\langle \hat{Z} \rangle = \cos(2\theta)$, maka nilai ekspektasi untuk 2 aset adalah:
$$ \langle E(\theta) \rangle = J_{12}\cos(2\theta_1)\cos(2\theta_2) + h_1\cos(2\theta_1) + h_2\cos(2\theta_2) + \text{const} $$

---

## 5. Optimasi Variasional: SPSA
Setelah mendapatkan fungsi ekspektasi energi $\langle E(\theta) \rangle$, kita perlu mencari parameter $\theta$ yang meminimalkan nilai tersebut. Dalam Tugas Akhir ini, digunakan algoritma **Simultaneous Perturbation Stochastic Approximation (SPSA)**.

### Mengapa SPSA?
Berbeda dengan Gradient Descent (GD) yang memerlukan $2N$ evaluasi sirkuit untuk estimasi gradien, SPSA hanya memerlukan **2 evaluasi** per iterasi, terlepas dari jumlah parameter. Hal ini sangat efisien untuk perangkat kuantum berderau (NISQ).

### Algoritma SPSA:
1. **Perturbasi Simultan:** Bangkitkan vektor acak $\Delta_k$ dari distribusi Bernoulli.
2. **Estimasi Gradien:**
   $$ \hat{g}_k(\theta_k) = \frac{E(\theta_k + c_k \Delta_k) - E(\theta_k - c_k \Delta_k)}{2 c_k \Delta_k} $$
3. **Update Parameter:**
   $$ \theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k) $$
   Dimana $a_k$ dan $c_k$ adalah *learning rates* yang mengecil seiring bertambahnya iterasi $k$.

Output akhir setelah konvergensi adalah distribusi probabilitas dari state $|x_1 x_2 \dots x_N\rangle$. State dengan probabilitas tertinggi yang memenuhi batasan $\sum x_i = K$ dinyatakan sebagai konfigurasi portofolio optimal.
