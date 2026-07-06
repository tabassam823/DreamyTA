# Derivasi Formal: Transformasi Markowitz-Ising Berbasis Strategi Biner dan Quantum Information

Dokumen ini menyajikan metodologi rujukan untuk mentransformasikan masalah optimasi portofolio (seleksi 2 dari 4 saham) ke dalam formalisme model *Ising*. Pendekatan ini merupakan *upgrade* struktural terhadap model Markowitz konvensional dengan mengintegrasikan probabilitas strategi biner (*Up/Down*) dan *Quantum Mutual Information* (QMI). Melalui derivasi ini, setiap aset dipandang sebagai pemain dalam sistem *Game Theory* yang keputusannya didasarkan pada dinamika harga historis dan interaksi informasional non-linear.

## 1. Pemetaan Strategi Biner dan Probabilitas Pergerakan Harga
Dalam kerangka kerja ini, setiap aset $i \in \{A, B, C, D\}$ memiliki dua strategi biner pada setiap waktu $t$: *Up* ($S_u$) jika $C_t > O_t$ dan *Down* ($S_d$) jika $C_t \leq O_t$. Selama rentang waktu $T$, perilaku aset diringkas dalam distribusi probabilitas marginal $P(S_i = u)$ dan $P(S_i = d)$. Probabilitas ini berfungsi sebagai basis untuk melihat "alasan" sebuah aset cenderung dipilih, melampaui sekadar statistik *return* rata-rata.

### 1.1 Tabel Payoff Strategi Individual ($Q_{ii}$)
Setiap pemain (aset) memiliki ekspektasi *payoff* yang bergantung pada strategi yang dominan selama rentang waktu $T$. Utilitas individual $V_{i,s}$ dihitung secara kondisional berdasarkan strategi yang terjadi:

| Strategi $S_{i,t}$ | Kondisi Realitas | Probabilitas | Ekspektasi Payoff ($V_{i,s}$) |
| :--- | :--- | :--- | :--- |
| **$u$ (Up)** | $C_t > O_t$ | $P(S_i = u)$ | $\mu_{i,u} - \lambda \sigma^2_{i,u}$ |
| **$d$ (Down)** | $C_t \leq O_t$ | $P(S_i = d)$ | $\mu_{i,d} - \lambda \sigma^2_{i,d}$ |

Nilai $Q_{ii}$ didefinisikan sebagai total ekspektasi utilitas: $Q_{ii} = \mathbb{E}[V_i] = \sum_{s \in \{u,d\}} P(S_i = s) V_{i,s}$.

Di mana $V_{i,s}$ merupakan utilitas *risk-adjusted* aset $i$ yang dikondisikan pada strategi $s$ (Up atau Down), dengan formulasi:
$$V_{i,s} = \mu_{i,s} - \lambda \sigma^2_{i,s} \quad (1)$$
Dalam konteks ini, $\mu_{i,s}$ adalah *conditional expected return* dan $\sigma^2_{i,s}$ adalah *conditional variance* aset $i$ saat strategi $s$ teramati selama rentang waktu $T$. Parameter $\lambda$ merepresentasikan koefisien *risk aversion* yang menyeimbangkan antara profitabilitas dan stabilitas strategi.

### 1.2 Tabel Interaksi Strategi Pairwise ($Q_{ij}$)
Interaksi antar aset dimodelkan sebagai permainan koordinasi. Payoff bersama bergantung pada sinkronisasi strategi antara dua pemain. Nilai dalam sel merepresentasikan kontribusi terhadap risiko sistemik dan keterikatan informasi (QMI):

| Aset $i \downarrow$ \ Aset $j \rightarrow$ | **$S_j = u$** | **$S_j = d$** |
| :--- | :--- | :--- |
| **$S_i = u$** | $\text{High Risk (Synch)}$ | $\text{Low Risk (Hedge)}$ |
| **$S_i = d$** | $\text{Low Risk (Hedge)}$ | $\text{Residual Interaction}$ |

Strategi ini dipetakan ke dalam variabel keputusan biner $x_i \in \{0, 1\}$, di mana $x_i = 1$ menyatakan aset dipilih masuk ke dalam portofolio. Untuk pemrosesan kuantum, variabel ini ditransformasikan ke operator Pauli-Z melalui pemetaan $x_i \mapsto \frac{1 - \hat{Z}_i}{2}$. Konfigurasi sistem total direpresentasikan oleh 4 *spin* biner yang mencakup $2^4 = 16$ kemungkinan kombinasi portofolio.

## 2. Refinisi Matriks QUBO melalui Ekspektasi Strategis dan QMI
Tujuan utama optimasi tetap mengikuti fungsi biaya Markowitz: $\min \mathcal{L}_{pure} = x^T \Sigma x - \lambda \mu^T x$. Namun, elemen matriks bobot $Q$ ditingkatkan untuk menangkap dinamika strategi:

1.  **Elemen Diagonal ($Q_{ii}$):** Merepresentasikan utilitas mandiri aset $i$.
    $$Q_{ii} = \sigma_i^2 - \lambda \mathbb{E}[\mu_i]$$
    Di mana $\mathbb{E}[\mu_i] = P(S_i = u)\mu_{i,u} + P(S_i = d)\mu_{i,d}$ adalah ekspektasi *return* yang dibobot oleh probabilitas strategi selama waktu $T$.
2.  **Elemen Off-Diagonal ($Q_{ij}$):** Merepresentasikan interaksi dan diversifikasi.
    $$Q_{ij} = 2 \cdot \text{Cov}(i, j) \cdot [1 + \xi I(i:j)]$$
    Di mana $I(i:j)$ adalah *Quantum Mutual Information* yang mengukur keterikatan informasional antar pergerakan harga aset $i$ dan $j$, memberikan penalti lebih tinggi pada aset yang memiliki sinkronisasi strategi yang merugikan.

## 3. Transformasi QUBO ke Hamiltonian Ising (VQE)
Untuk mengimplementasikan kendala kardinalitas (memilih tepat $K=2$ saham dari $N=4$ pilihan), kita menambahkan suku penalti $A(\sum x_i - K)^2$. Transformasi dari ruang QUBO ke Hamiltonian *Ising* menghasilkan operator energi final:

$$\hat{H}_{final} = \sum_{i<j} J_{ij}^{total} \hat{Z}_i \hat{Z}_j + \sum_i h_i^{total} \hat{Z}_i + C$$

Dengan parameter fisik sebagai berikut:
- **Kopling Interaksi ($J_{ij}^{total}$):**
  $$J_{ij}^{total} = \frac{Q_{ij} + A}{2}$$
- **Medan Lokal ($h_i^{total}$):**
  $$h_i^{total} = -\frac{Q_{ii}}{2} - \sum_{j \neq i} \frac{Q_{ij}}{2} - A K'$$
  Di mana $K' = K - \frac{N}{2}$ (untuk kasus ini, $K'= 2 - 2 = 0$).

## 4. Analisis Dinamika Strategi dan Optimasi VQE
Penggunaan Hamiltonian ini dalam algoritma *Variational Quantum Eigensolver* (VQE) memungkinkan kita untuk mencari konfigurasi portofolio yang tidak hanya optimal secara numerik, tetapi juga stabil secara strategis. Dengan memasukkan probabilitas $P(S_i)$, kita dapat menganalisis apakah pemilihan sebuah saham didorong oleh konsistensi strategi *Up* atau oleh *return* ekstrem pada momen tertentu.

Suku interaksi $J_{ij}^{total}$ memastikan bahwa sistem menghindari pemilihan dua saham yang "bermain" dengan strategi yang sama secara informasional (QMI tinggi). Melalui evolusi sirkuit kuantum $|\psi(\theta)\rangle$, sistem akan konvergen pada *ground state* yang memenuhi syarat $\sum x_i = 2$ sambil meminimalkan risiko gabungan yang telah diperkaya oleh data strategi *Up/Down*.

## 5. Justifikasi Teoretis: Potential Games dalam Pasar Finansial
Justifikasi penggunaan model *Ising* ini terletak pada sifat sistem sebagai *Potential Game*. Dengan mendesain $Q_{ii}$ dan $Q_{ij}$ berbasis utilitas riil, setiap penurunan energi dalam sistem fisik berkorespondensi dengan peningkatan stabilitas portofolio. Minimisasi Hamiltonian $\hat{H}_{final}$ setara dengan mencari konfigurasi strategi yang paling efisien menurut prinsip-prinsip *Quantum Information Theory* dan ekonomi Markowitz, memberikan solusi yang lebih resilien terhadap anomali pasar jangka pendek.
