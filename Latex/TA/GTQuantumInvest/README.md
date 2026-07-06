# GTQuantumInvest

GTQuantumInvest adalah proyek optimasi portofolio menggunakan algoritma kuantum (VQE) dengan pendekatan Nash Strategic Best Response (SBR).

## Rumus Dasar

Berikut adalah rumus-rumus utama yang digunakan dalam perhitungan di `main.py` dan modul terkait:

### 1. Return Saham

- **Simple Return ($R_t$):**

$$R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$$

- **Log Return ($r_t$):**

$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

### 2. Expected Return & Volatility Drag

- **Expected Simple Return ($\mu_i$):**

$$\mu_i = \frac{1}{T} \sum_{t=1}^{T} R_{i,t}$$

- **Expected Log Return (dengan Volatility Drag):**

$$\mu_{r,i} = \mu_i - \frac{1}{2}\sigma_{r,i}^2$$

di mana $\sigma_{r,i}^2$ adalah varians dari log return.

### 3. Statistik Portofolio (Periodik)

Statistik dihitung berdasarkan deret waktu harga $P_{i,t}$ selama total waktu $T$:

- **Varians ($\sigma_i^2$):**

$$\sigma_i^2 = \left[ \frac{1}{T-1} \sum_{t=1}^{T} (r_{i,t} - \bar{r}_i)^2 \right] \times \Delta T$$

- **Kovarians ($\sigma_{ij}$):**

$$\sigma_{ij} = \left[ \frac{1}{T-1} \sum_{t=1}^{T} (r_{i,t} - \bar{r}_i)(r_{j,t} - \bar{r}_j) \right] \times \Delta T$$

Dalam proyek ini, $\Delta T = 126$ hari (lookback period) dan $r_{i,t}$ adalah log return.

### 4. Risk Aversion Endogen ($\gamma$)

Parameter risk aversion dihitung secara dinamis berdasarkan Sharpe Ratio agregat ($Z$):

$$\gamma = \frac{1}{1 + e^Z}, \quad Z = \frac{\text{mean}(|\mu_{\text{period}}|)}{\text{mean}(\sigma_{\text{period}})}$$

### 5. Matriks QUBO ($Q$)

Konstruksi matriks QUBO mencakup suku penalti $\lambda$ untuk pembatas kardinalitas $K$:

- **Diagonal ($Q_{ii}$):**

$$Q_{ii} = \frac{\gamma \sigma_{i}^2}{2K^2} - \frac{\mu_{i}}{K} + \lambda(1 - 2K)$$

- **Off-Diagonal ($Q_{ij}$):**

$$Q_{ij} = \frac{\gamma \sigma_{ij}}{2K^2} + \lambda$$

### 6. Parameter Ising & Hamiltonian

Transformasi dari QUBO ($x \in \{0, 1\}$) ke Ising ($s \in \{-1, 1\}$) melalui $x_i = \frac{1 - Z_i}{2}$:

- **Bias ($h_i$):**

$$h_i = \frac{Q_{ii}}{2} + \sum_{j \neq i} \frac{Q_{ij}}{2}$$

- **Interaksi ($J_{ij}$):**

$$J_{ij} = \frac{Q_{ij}}{4}$$

- **Konstanta Ising ($C_{\text{Ising}}$):**

$$C_{\text{Ising}} = \sum_i \frac{Q_{ii}}{2} + \sum_{i < j} \frac{Q_{ij}}{2} + \lambda K^2$$

## Nash Equilibrium

Pencarian Nash Equilibrium dilakukan menggunakan pendekatan **Sequential Best Response (SBR)** untuk menemukan kombinasi aset yang memaksimalkan utilitas finansial secara kolektif.

---

**Algorithm 1. Iterative Sequential Best Response (Nash SBR)**

---

**Data:** Inisialisasi bitstring awal $\mathbf{x}^0 \in \{0, 1\}^N$ dengan $\sum x_i = K$, dan set $q = 0$.

**Step 1:** Jika $\mathbf{x}^q$ memenuhi kriteria penghentian (tidak ada peningkatan utilitas): **STOP**.

**Step 2:** Perbarui $\mathbf{x}^{q+1}$ dengan melakukan evaluasi *swap* antara aset terpilih ($x_i=1$) dan aset tidak terpilih ($x_j=0$):

$$\mathbf{x}^{q+1} \triangleq \arg \max_{\mathbf{x} \in \mathcal{S}(\mathbf{x}^q)} U(\mathbf{x})$$

di mana $\mathcal{S}(\mathbf{x}^q)$ adalah himpunan semua bitstring yang dapat dicapai melalui satu kali pertukaran aset dari $\mathbf{x}^q$.

**Step 3:** Set $q \leftarrow q + 1$; dan kembali ke **Step 1**.

---

## Variational Quantum Eigensolver

Algoritma VQE digunakan untuk meminimalkan Hamiltonian portofolio dengan pendekatan **Adaptive Depth** dan optimasi berbasis gradien stokastik.

---

**Algorithm 2. Adaptive VQE with SPSA Optimization**

---

**Data:** Hamiltonian $H$, target kardinalitas $K$, kedalaman maksimum $D$, dan parameter awal $\boldsymbol{\theta}_{warm}$ dari Algorithm 1.

**Step 1:** Untuk setiap level kedalaman $d = 1, 2, \dots, D$, bangun ansatz sirkuit $\mathcal{U}_d(\boldsymbol{\theta})$.

**Step 2:** Inisialisasi $\boldsymbol{\theta}_{d,0}$ menggunakan hasil optimal dari $\boldsymbol{\theta}_{d-1}$ atau $\boldsymbol{\theta}_{warm}$ jika $d=1$.

**Step 3:** Perbarui parameter $\boldsymbol{\theta}_{d,k+1}$ menggunakan **SPSA** untuk $k = 0, 1, \dots, K_{max}$:

$$\boldsymbol{\theta}_{d,k+1} = \boldsymbol{\theta}_{d,k} - a_k \hat{g}_k(\boldsymbol{\theta}_{d,k})$$

di mana estimasi gradien $\hat{g}_k$ didefinisikan sebagai:

$$\hat{g}_k(\boldsymbol{\theta}) \triangleq \frac{E(\boldsymbol{\theta} + c_k \boldsymbol{\Delta}_k) - E(\boldsymbol{\theta} - c_k \boldsymbol{\Delta}_k)}{2 c_k \boldsymbol{\Delta}_k}$$

**Step 4:** Jika konvergensi tercapai $|E_k - E_{k-n}| < \epsilon$: Simpan $E_{d, opt}$ dan $\boldsymbol{\theta}_{d, opt}$.

**Step 5:** Pilih solusi terbaik $(\mathbf{x}^*, E^*) = \min_d E_{d, opt}$ melalui pengukuran probabilitas state yang valid.

---
