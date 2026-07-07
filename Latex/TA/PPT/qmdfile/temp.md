# OPTIMASI PORTOFOLIO BERBASIS MODEL MARKOWITZ MENGGUNAKAN METODE VARIATIONAL QUANTUM EIGENSOLVER
Putra Naufal Tabassam

<!-- include Fase_0.qmd -->
<!-- include Fase_1.qmd -->
<!-- include Fase_2.qmd -->
<!-- include Fase_3.qmd -->
<!-- include Fase_4.qmd -->
<!-- include Fase_5.qmd -->
<!-- include Fase_6.qmd -->
<!-- include Fase_7.qmd -->
<!-- include Fase_8.qmd -->
<!-- include Fase_9.qmd -->

# Fase Latar Belakang

## Ekonomi dan Investasi

<img src="../Gambar/nixxon_shock.png" style="width:100.0%" />
<img src="../Gambar/212_Inflasi.png" style="width:100.0%" />

Inflasi & Guncangan Ekonomi

<img src="../Gambar/213_Investasi.png" style="width:100.0%" />

Urgensi Investasi

<img src="../Gambar/Diversifikasi.png" style="width:100.0%" />

Diversifikasi Portofolio

------------------------------------------------------------------------

## Model Markowitz dan Ising

**Model Markowitz & Pareto Optimum**

- **Mean-Variance:** ::: {style=“font-size: 0.85em;”}
  ℒ(**ω**) = ∑<sub>*i*, *j*</sub>*σ*<sub>*i**j*</sub>*ω*<sub>*i*</sub>*ω*<sub>*j*</sub> − *λ*∑<sub>*i*</sub>*μ*<sub>*i*</sub>*ω*<sub>*i*</sub>

- Investor mencari portofolio pada *Efficient Frontier* (Pareto Optimum)
  untuk memaksimalkan *return* pada tingkat risiko tertentu.

<img src="../Gambar/224_Efficient_Frontier.png" style="width:55.0%" />

Grafik Efficient Frontier

**Formulasi ke Hamiltonian Ising**

- Model Markowitz diubah menjadi variabel biner (beli/tidak beli), lalu
  dipetakan ke *spin* {−1, 1}.
- **Hamiltonian Ising Umum:**
  $$ \hat{\mathcal{H}} = - \sum\_{i=1}^N h_i \hat{Z}\_i - \sum\_{i\<j}^N J\_{ij} \hat{Z}\_i \hat{Z}\_j + C $$
- *h*<sub>*i*</sub> merepresentasikan kecenderungan harga pasar, dan
  *J*<sub>*i**j*</sub> menggambarkan korelasi antar aset.

:::

------------------------------------------------------------------------

## Pengenalan Komputer Kuantum: Qubit

**Qubit dan Superposisi**

- Qubit memanfaatkan prinsip superposisi, memungkinkan representasi
  kombinasi linear state 0 dan 1 sekaligus.
  |*ψ*⟩ = *α*|0⟩ + *β*|1⟩

- **Geometri Qubit (Bola Bloch):**

  Status qubit dapat divisualisasikan dalam *Bloch Sphere* dengan sudut
  polar *θ* (probabilitas basis) dan azimuthal *ϕ* (fase kuantum).

<iframe src="bloch_interactive.html" width="100%" height="450px" style="border:none;">
</iframe>

Visualisasi status Qubit

------------------------------------------------------------------------

## Hamiltonian Ising ke Komputer Kuantum

- **Variational Quantum Eigensolver (VQE):** Algoritma hibrida
  kuantum-klasik untuk mencari konfigurasi energi terendah (*ground
  state*).
- **Proses Pengerjaan:**
  1.  Hamiltonian Ising $\hat{\mathcal{H}}$ yang mewakili masalah
      portofolio digunakan sebagai *observable* kuantum.
  2.  Sirkuit Kuantum Berparameter menyiapkan status *ansatz*
      |*ψ*(*θ*)⟩.
  3.  Komputer kuantum mengukur nilai ekspektasi energi
      $\langle\psi(\theta)|\hat{\mathcal{H}}|\psi(\theta)\rangle$.
  4.  Komputer klasik mengoptimalkan parameter rotasi *θ* secara
      iteratif untuk meminimalkan energi, yang berkorespondensi dengan
      konfigurasi portofolio terbaik.

------------------------------------------------------------------------

## Tantangan Efisiensi dan Solusi *Nash Equilibrium*

**Masalah Efisiensi (*Barren Plateau*)**

- Inisialisasi parameter acak pada sirkuit kuantum rentan terjebak di
  area datar (*Barren Plateau*), menghambat VQE mencapai solusi optimal.

**Solusi: *Warm-Start Strategy***

- Memanfaatkan kondisi **Nash Equilibrium** dari konsep *Game Theory*
  (dalam skema *Exact Potential Game*).
- Titik Nash bertindak sebagai tebakan awal (*warm-start*) yang sudah
  efisien secara rasional, mempercepat optimasi kuantum.

<img src="../Gambar/barren_plateau.png" style="width:70.0%" />
<img src="../Gambar/nasheq.png" style="width:60.0%" />

------------------------------------------------------------------------

## Metode Evaluasi Performa (Backtesting)

![](../Gambar/backtest.png)

Simulasi riwayat harga dan rebalance portofolio secara periodik

![](../Gambar/backtest_data.png)

Data backtesting pada sebuah strategi trading

------------------------------------------------------------------------

## Tujuan Penelitian

1.  Menganalisis formulasi bias aset sebagai parameter medan lokal
    (*h*<sub>*i*</sub>) dan interaksi antar aset sebagai koefisien
    kopling (*J*<sub>*i**j*</sub>) melalui pendekatan fungsi potensial
    dalam sistem Hamiltonian berbasis *Exact Potential Game* (EPG).
2.  Mengevaluasi kontribusi strategi *warm-start* berbasis *Nash
    Equilibrium* dalam meningkatkan efisiensi pencarian solusi optimal
    pada algoritma VQE.
3.  Menguji kapabilitas algoritma VQE yang menggunakan optimasi SPSA dan
    *Ansatz EfficientSU(2)* untuk menghasilkan keputusan alokasi aset
    yang optimal dalam kondisi pasar yang kompleks.

------------------------------------------------------------------------

## Batasan Masalah (1/2)

1.  Portofolio yang dianalisis dibatasi pada pemilihan 1 aset dari 2
    pilihan aset pada sistem *N* = 2 dan 2 aset dari 4 pilihan aset pada
    sistem *N* = 4.
2.  Model permainan yang digunakan adalah skema *non zero-sum game*
    dalam kerangka *Exact Potential Game*.
3.  Simulasi dan implementasi algoritma dilakukan menggunakan simulator
    *Pennylane* tanpa mempertimbangkan *noise*.

------------------------------------------------------------------------

## Batasan Masalah (2/2)

1.  Tugas akhir ini hanya merupakan *proof-of-concept* dari implementasi
    *warm-start* ekuilibrium Nash terhadap performa algoritma VQE dalam
    menemukan solusi *ground state* pada model portofolio hibrida.
2.  Analisis Entropi Von Neumann dibatasi sebagai indikator perubahan
    distribusi probabilitas keadaan kuantum selama proses optimasi VQE
    dan tidak digunakan sebagai kajian mendalam mengenai sifat
    keterbelitan dari *ansatz*.
3.  Analisis berfokus pada pengaruh *warm-start* ekuilibrium Nash
    terhadap proses optimasi VQE, bukan untuk membuktikan keunggulan
    komputasi kuantum terhadap metode klasik.

# Fase Metodologi

## Diagram Alir Utama

<img src="../Gambar/31_Dialir.png" style="width:45.0%"
data-fig-align="center" />

------------------------------------------------------------------------

## Analisis Kuantitatif

- **Simple Return (*R*):**
  $$ R_t = \frac{P_t - P\_{t-1}}{P\_{t-1}} $$
- **Expected Return (*R̄*):**
  $$ \bar{R} = \frac{1}{n} \sum\_{t=1}^n R_t $$
- **Variance (*σ*<sup>2</sup>):**
  $$ \sigma^2 = \frac{1}{n-1} \sum\_{t=1}^n (R_t - \bar{R})^2 $$
- **Covariance (*σ*<sub>*i**j*</sub>):**
  $$ \sigma\_{ij} = \frac{1}{n-1} \sum\_{t=1}^n (R\_{i,t} - \bar{R}\_i)(R\_{j,t} - \bar{R}\_j) $$

- **Log Return (*r*):**
  $$ r_t = \ln\left(\frac{P_t}{P\_{t-1}}\right) $$
- **Expected Return (*r̄*):**
  $$ \bar{r} = \frac{1}{n} \sum\_{t=1}^n r_t $$
- **Variance (*σ*<sup>2</sup>):**
  $$ \sigma^2 = \frac{1}{n-1} \sum\_{t=1}^n (r_t - \bar{r})^2 $$
- **Covariance (*σ*<sub>*i**j*</sub>):**
  $$ \sigma\_{ij} = \frac{1}{n-1} \sum\_{t=1}^n (r\_{i,t} - \bar{r}\_i)(r\_{j,t} - \bar{r}\_j) $$

<img src="../Gambar/223_Price_log.png" style="width:100.0%" />

Transformasi pergerakan harga saham.

- *P*<sub>*t*</sub>: Harga pada waktu *t*

------------------------------------------------------------------------

## Model Markowitz

### Rumus Utama

**Mean-Variance:**
ℒ(**ω**) = ∑<sub>*i*, *j*</sub>*σ*<sub>*i**j*</sub>*ω*<sub>*i*</sub>*ω*<sub>*j*</sub> − *λ*∑<sub>*i*</sub>*μ*<sub>*i*</sub>*ω*<sub>*i*</sub>

**Binerisasi:**
$$ \mathcal{L}(\mathbf{x}) = \sum\_{i,j} \sigma\_{ij} \frac{x_i x_j}{K^2} - \lambda \sum_i \mu_i \frac{x_i}{K} $$

<hr style="width: 50%; margin: 20px auto;">

*μ*<sub>*i*</sub>: Imbal hasil rata-rata aset ke-*i*   |  
*σ*<sub>*i**j*</sub>: Kovarians antara aset *i* dan *j*<br>
*ω*<sub>*i*</sub>: Proporsi bobot kontinu aset ke-*i*   |   *λ*:
Parameter toleransi risiko

::: <br>

### Penurunan Rumus

**Langkah 1 — Formulasi Lagrangian Kontinu (Markowitz):**

Fungsi biaya Markowitz dalam domain bobot *ω*<sub>*i*</sub>:

ℒ(**ω**) = ∑<sub>*i*, *j*</sub>*σ*<sub>*i**j*</sub>*ω*<sub>*i*</sub>*ω*<sub>*j*</sub> − *λ*∑<sub>*i*</sub>*μ*<sub>*i*</sub>*ω*<sub>*i*</sub>

dengan syarat ∑<sub>*i*</sub>*ω*<sub>*i*</sub> = 1 dan
*ω*<sub>*i*</sub> ≥ 0.

<hr>

**Langkah 2 — Substitusi Variabel Biner:**

Variabel bobot kontinu *ω*<sub>*i*</sub> diubah menjadi variabel biner
*x*<sub>*i*</sub> ∈ {0, 1} melalui hubungan:

$$\omega_i = \frac{x_i}{K}$$

di mana *K* adalah jumlah aset yang dipilih dari total *N* kandidat.

<hr>

**Langkah 3 — Substitusi ke Lagrangian:**

Substitusi *ω*<sub>*i*</sub> = *x*<sub>*i*</sub>/*K* ke dalam fungsi
Lagrangian:

$$\mathcal{L}(\mathbf{x}) = \sum\_{i,j} \sigma\_{ij} \frac{x_i}{K} \frac{x_j}{K} - \lambda \sum_i \mu_i \frac{x_i}{K}$$

$$\therefore \mathcal{L}(\mathbf{x}) = \sum\_{i,j} \sigma\_{ij} \frac{x_i x_j}{K^2} - \lambda \sum_i \mu_i \frac{x_i}{K}$$

Nilai *x*<sub>*i*</sub> = 1 merepresentasikan **beli**, sedangkan
*x*<sub>*i*</sub> = 0 merepresentasikan **tidak membeli**.

<hr>

<table>
<thead>
<tr>
<th style="text-align: center;">Simbol</th>
<th style="text-align: center;">Domain Kontinu</th>
<th style="text-align: center;">Domain Biner</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Variabel keputusan</td>
<td style="text-align: center;"><span
class="math inline"><em>ω</em><sub><em>i</em></sub> ∈ [0, 1]</span></td>
<td style="text-align: center;"><span
class="math inline"><em>x</em><sub><em>i</em></sub> ∈ {0, 1}</span></td>
</tr>
<tr>
<td style="text-align: center;">Kendala</td>
<td style="text-align: center;"><span
class="math inline">∑<em>ω</em><sub><em>i</em></sub> = 1</span></td>
<td style="text-align: center;"><span
class="math inline">∑<em>x</em><sub><em>i</em></sub> = <em>K</em></span></td>
</tr>
</tbody>
</table>

<br><br><br>

:::

:::

------------------------------------------------------------------------

## Exact Potential Game (EPG)

- **Definisi:** Model permainan yang memiliki fungsi potensial global
  (*Φ*), di mana setiap perubahan utilitas individu akibat perubahan
  strategi sepenuhnya tercermin oleh perubahan nilai *Φ*.
- **Makna “Potensial” & “Global”:**
  - **Potensial:** Sistem agen berdinamika menuju nilai ekuilibrium
    (maksimalisasi utilitas), yang secara fundamental ekuivalen dengan
    prinsip minimisasi energi (*H* = −*Φ*) dalam fisika fisis.
  - **Global:** *Φ* merangkum seluruh utilitas individu ke dalam satu
    fungsi skalar tunggal untuk merepresentasikan kualitas konfigurasi
    strategi permainan secara keseluruhan.

- **Kondisi *Nash Equilibrium*:** Perubahan utilitas lokal
  (*Δ**u*<sub>*i*</sub>) sebanding persis dengan perubahan potensial
  global (*Δ**Φ*).
  *Δ**Φ* = *Φ*(*s*<sub>*i*</sub><sup>′</sup>, *s*<sub>−*i*</sub>) − *Φ*(*s*<sub>*i*</sub>, *s*<sub>−*i*</sub>) = *u*<sub>*i*</sub>(*s*<sub>*i*</sub><sup>′</sup>, *s*<sub>−*i*</sub>) − *u*<sub>*i*</sub>(*s*<sub>*i*</sub>, *s*<sub>−*i*</sub>)
- Dinamika sistem akan terhenti dan mencapai *Nash Equilibrium* ketika
  tidak ada lagi strategi yang menghasilkan peningkatan potensial
  (*Δ**Φ* \< 0).

------------------------------------------------------------------------

## EPG pada Alokasi Portofolio

### Rumus Utama

- Transformasi persamaan utilitas Markowitz biner menjadi fungsi
  potensial global EPG:
  $$ \Phi(\mathbf{x}) = \sum\_{l=1}^N \mu_l \frac{x_l}{K} - \frac{\gamma}{2}\sum\_{i=1}^N\sum\_{j=1}^N \sigma\_{ij} \frac{x_i}{K} \frac{x_j}{K} $$
- dengan *γ* mendefinisikan faktor penghindaran risiko (*risk aversion*)
  pada fungsi utilitas agen.

### Penurunan Rumus

**Penurunan: Dari Model Markowitz Biner ke Fungsi Potensial EPG**

**Langkah 1 — Lagrangian Biner Markowitz:**

Dari transformasi *ω*<sub>*i*</sub> = *x*<sub>*i*</sub>/*K*, diperoleh
fungsi Lagrangian biner:

$$\mathcal{L}(\mathbf{x}) = \sum\_{i,j} \sigma\_{ij} \frac{x_i x_j}{K^2} - \lambda \sum_i \mu_i \frac{x_i}{K}$$

<hr>

**Langkah 2 — Konversi ke Fungsi Utilitas:**

Definisikan faktor penghindaran risiko *γ* = 2/*λ*, sehingga:

$$U(\mathbf{x}) = - \frac{1}{\lambda} \mathcal{L}(\mathbf{x})$$

$$U(\mathbf{x}) = \sum_i \frac{\mu_i}{K} x_i - \frac{\gamma}{2K^2} \sum\_{i,j} \sigma\_{ij} x_i x_j$$

<hr>

**Langkah 3 — Utilitas Individu Agen ke-*i*:**

$$u_i(\mathbf{x}) = \frac{\mu_i}{K} x_i - \frac{\gamma}{2K^2} x_i \left( \sum\_{j \neq i} \sigma\_{ij} x_j \right)$$

Jika varians dipisah dari matriks kovarians:

$$u_i(\mathbf{x}) = \frac{\mu_i}{K} x_i - \frac{\gamma}{2K^2} x_i \left( \sigma\_{ii} + 2\sum\_{j \neq i} \sigma\_{ij} x_j \right)$$

<hr>

**Langkah 4 — Fungsi Potensial Global *Φ*:**

Dari utilitas sistem, fungsi potensial EPG:

$$\Phi(\mathbf{x}) = \sum\_{l=1}^N \mu_l \frac{x_l}{K} - \frac{\gamma}{2}\sum\_{i=1}^N\sum\_{j=1}^N \sigma\_{ij} \frac{x_i}{K} \frac{x_j}{K}$$

<hr>

**Langkah 5 — Dekomposisi untuk Verifikasi
*Δ**u*<sub>*i*</sub> = *Δ**Φ*:**

Dekomposisi suku yang mengandung *x*<sub>*i*</sub> (dengan
*x*<sub>*i*</sub><sup>2</sup> = *x*<sub>*i*</sub>):

$$\Phi(\mathbf{x}) = \frac{\mu_i}{K}x_i - \frac{\gamma}{2} \left( \frac{\sigma\_{ii}}{K^2}x_i + \frac{2}{K^2}x_i \sum\_{j \neq i} \sigma\_{ij}x_j \right) + \underbrace{\sum\_{l \neq i} \frac{\mu_l}{K}x_l - \frac{\gamma}{2} \sum\_{l \neq i} \sum\_{m \neq i} \frac{\sigma\_{lm}}{K^2}x_l x_m}\_{\text{tidak bergantung pada } x_i}$$

<hr>

**Langkah 6 — Insentif Marginal:**

$$\Delta \Phi = \Phi(1, \mathbf{x}\_{-i}) - \Phi(0, \mathbf{x}\_{-i}) = \frac{\mu_i}{K} - \frac{\gamma \sigma\_{ii}}{2K^2} - \frac{\gamma}{K^2} \sum\_{j \neq i} \sigma\_{ij} x_j$$

Karena *Δ**u*<sub>*i*</sub> = *Δ**Φ* terjamin ⇒ **terbukti** sebagai
*Exact Potential Game*.

<hr>

**Langkah 7 — Risk Aversion Endogen:**

$$\gamma = \frac{1}{1 + e^{(\bar{\mu}\_l/\bar{\sigma}\_l)}}$$

dengan *μ̄*<sub>*l*</sub> dan *σ̄*<sub>*l*</sub> dari *log returns*.

<br><br><br>

:::

:::

------------------------------------------------------------------------

## Transformasi EPG ke Model Ising

### Transformasi QUBO

**Fungsi Energi dari Potensial (Markowitz Biner):**
$$E(\mathbf{x}) = \frac{\gamma}{2K^2}\sum\_{i=1}^N\sum\_{j=1}^N \sigma\_{ij} x_i x_j - \sum\_{i=1}^N \frac{\mu_i}{K} x_i$$

**Penambahan Fungsi Penalti (QUBO):** Penalti untuk memastikan tepat *K*
aset yang dipilih:
$$P(\mathbf{x}) = A\left(\sum\_{i=1}^N x_i - K\right)^2$$

**Bentuk Total Hamiltonian QUBO:**
*E*<sub>*t**o**t**a**l*</sub>(**x**) = ∑<sub>*i*</sub>*Q*<sub>*i**i*</sub>*x*<sub>*i*</sub> + ∑<sub>*i* ≠ *j*</sub>*Q*<sub>*i**j*</sub>*x*<sub>*i*</sub>*x*<sub>*j*</sub> + *A**K*<sup>2</sup>

**Hamiltonian Ising Akhir:** Setelah memetakan variabel biner
*x*<sub>*i*</sub> ∈ {0, 1} ke variabel spin *s*<sub>*i*</sub> ∈ {−1, 1}:
$$\boxed{\hat{\mathcal{H}} = - \sum\_{i=1}^N h_i \hat{Z}\_i - \sum\_{i\<j}^N J\_{ij} \hat{Z}\_i \hat{Z}\_j + C}$$

### Penurunan Rumus

**Penurunan: Dari Fungsi Potensial Game ke Hamiltonian Ising**

**Langkah 1 — Fungsi Energi dari Potensial:**

Konversi dari maksimasi potensial ke minimasi energi:

*E*(**x**) = −*Φ*(**x**)

Substitusi *Φ* dari fungsi potensial Markowitz:

$$E(\mathbf{x}) = \frac{\gamma}{2K^2}\sum\_{i=1}^N\sum\_{j=1}^N \sigma\_{ij} x_i x_j - \sum\_{i=1}^N \frac{\mu_i}{K} x_i$$

<hr>

**Langkah 2 — Dekomposisi dengan
*x*<sub>*i*</sub><sup>2</sup> = *x*<sub>*i*</sub>:**

$$E(\mathbf{x}) = \frac{\gamma}{2K^2}\left(\sum\_{i=1}^N\sigma\_{ii} x_i^2 + \sum\_{i\ne j}\sigma\_{ij} x_ix_j\right) -\sum\_{i=1}^N \frac{\mu_i}{K} x_i$$

$$= \frac{\gamma}{2K^2}\sum\_{i=1}^N\sigma\_{ii} x_i + \frac{\gamma}{2K^2}\sum\_{i\ne j}\sigma\_{ij} x_ix_j - \sum\_{i=1}^N \frac{\mu_i}{K} x_i$$

$$\therefore E(\mathbf{x}) = \sum\_{i=1}^N\left(\frac{\gamma \sigma\_{ii}}{2K^2} - \frac{\mu_i}{K}\right)x_i + \sum\_{i\ne j}\frac{\gamma \sigma\_{ij}}{2K^2} x_ix_j$$

<hr>

**Langkah 3 — Penambahan Fungsi Penalti:**

Penalti kuadratik untuk memenuhi kendala ∑*x*<sub>*i*</sub> = *K*:

$$P(\mathbf{x}) = A\left(\sum\_{i=1}^N x_i - K\right)^2$$

Penjabaran:

$$P(\mathbf{x}) = A\sum\_{i=1}^N x_i^2 + A\sum\_{i\ne j} x_ix_j - 2AK\sum\_{i=1}^N x_i + AK^2$$

<hr>

**Langkah 4 — Energi Total (QUBO):**

*E*<sub>*t**o**t**a**l*</sub>(**x**) = *E*(**x**) + *P*(**x**)

$$\therefore E\_{total}(\mathbf{x}) = \sum_i \left(\frac{\gamma \sigma\_{ii}}{2K^2} + A - \frac{\mu_i}{K} - 2AK\right)x_i + \sum\_{i\ne j}\left(\frac{\gamma \sigma\_{ij}}{2K^2} + A\right) x_ix_j + AK^2$$

<hr>

**Langkah 5 — Notasi Koefisien QUBO:**

$$Q\_{ii} = \frac{\gamma \sigma\_{ii}}{2K^2}+A-\frac{\mu_i}{K}-2AK$$

$$Q\_{ij} = \frac{\gamma \sigma\_{ij}}{2K^2}+A$$

Sehingga:

*E*<sub>*t**o**t**a**l*</sub>(**x**) = ∑<sub>*i*</sub>*Q*<sub>*i**i*</sub>*x*<sub>*i*</sub> + ∑<sub>*i* ≠ *j*</sub>*Q*<sub>*i**j*</sub>*x*<sub>*i*</sub>*x*<sub>*j*</sub> + *A**K*<sup>2</sup>

<hr>

**Langkah 6 — Transformasi Affine ke Domain Spin:**

Pemetaan biner *x*<sub>*i*</sub> ∈ {0, 1} ke *spin*
*s*<sub>*i*</sub> ∈ {−1, 1}:

$$x_i = \frac{(1 - s_i)}{2}, \quad x_ix_j = \frac{(1-s_i)(1-s_j)}{4}$$

Substitusi:

$$E\_{total}(\mathbf{s}) = \sum_i Q\_{ii} \frac{1-s_i}{2} + \sum\_{i\ne j} Q\_{ij} \frac{1 - s_i - s_j + s_is_j}{4} + AK^2$$

$$\therefore E\_{total}(\mathbf{s}) = \sum_i \left(- \frac{Q\_{ii}}{2} - \sum\_{j \neq i} \frac{Q\_{ij}}{2}\right) s_i + \sum\_{i\ne j} \frac{Q\_{ij}}{4} s_i s_j + \left(\sum_i \frac{Q\_{ii}}{2} + \sum\_{i\ne j} \frac{Q\_{ij}}{4} + AK^2\right)$$

<hr>

**Langkah 7 — Identifikasi Parameter Hamiltonian:**

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 35%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Parameter</th>
<th style="text-align: center;">Definisi</th>
<th style="text-align: left;">Makna Fisis</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span
class="math inline"><em>h</em><sub><em>i</em></sub></span></td>
<td style="text-align: center;"><span class="math inline">$-
\frac{Q_{ii}}{2} - \sum_{j \neq i} \frac{Q_{ij}}{2}$</span></td>
<td style="text-align: left;">Medan bias lokal</td>
</tr>
<tr>
<td style="text-align: center;"><span
class="math inline"><em>J</em><sub><em>i</em><em>j</em></sub></span></td>
<td style="text-align: center;"><span
class="math inline">$\frac{Q_{ij}}{4}$</span></td>
<td style="text-align: left;">Kopling antar <em>spin</em></td>
</tr>
<tr>
<td style="text-align: center;"><span
class="math inline"><em>C</em></span></td>
<td style="text-align: center;"><span class="math inline">$\sum_i
\frac{Q_{ii}}{2} + \sum_{i\ne j} \frac{Q_{ij}}{4} + AK^2$</span></td>
<td style="text-align: left;">Konstanta energi</td>
</tr>
</tbody>
</table>

**Hasil Akhir — Hamiltonian Ising:**

$$\boxed{\hat{\mathcal{H}} = - \sum\_{i=1}^N h_i \hat{Z}\_i - \sum\_{i\<j}^N J\_{ij} \hat{Z}\_i \hat{Z}\_j + C}$$

<br><br>

:::

:::

------------------------------------------------------------------------

## Desain Sirkuit Kuantum

### Arsitektur Sirkuit

<img src="../Gambar/rangkaian1depth.png" style="width:80.0%"
data-fig-align="center" />

Arsitektur *Hardware-Efficient Ansatz* dengan *depth* *D* = 1

### Gerbang Rotasi Total

**Matriks Rotasi *U*<sub>*q*</sub>(*θ*) untuk 2 Qubit**

Berdasarkan definisi gerbang rotasi *R*<sub>*y*</sub>(*θ*) dan
*R*<sub>*z*</sub>(*θ*):
$$
\begin{align}
U\_{1q}(\theta) &= R_z(\theta\_{1z}) R_y(\theta\_{1y}) \\
&= \begin{pmatrix} e^{-i\theta\_{1z}/2} & 0 \\ 0 & e^{i\theta\_{1z}/2} \end{pmatrix} \begin{pmatrix} \cos(\theta\_{1y}/2) & -\sin(\theta\_{1y}/2) \\ \sin(\theta\_{1y}/2) & \cos(\theta\_{1y}/2) \end{pmatrix} \\
&= \begin{pmatrix} e^{-i\theta\_{1z}/2} \cos(\theta\_{1y}/2) & -e^{-i\theta\_{1z}/2} \sin(\theta\_{1y}/2) \\ e^{i\theta\_{1z}/2} \sin(\theta\_{1y}/2) & e^{i\theta\_{1z}/2} \cos(\theta\_{1y}/2) \end{pmatrix}
\end{align}
$$

Maka untuk sistem 2 qubit:
$$
\begin{align}
U\_{q}(\theta) &= \[R_z(\theta\_{1z}) R_y(\theta\_{1y})\] \otimes \[R_z(\theta\_{2z}) R_y(\theta\_{2y})\]\\
&= \begin{pmatrix} e^{-i\theta\_{1z}/2} \cos(\theta\_{1y}/2) & -e^{-i\theta\_{1z}/2} \sin(\theta\_{1y}/2) \\ e^{i\theta\_{1z}/2} \sin(\theta\_{1y}/2) & e^{i\theta\_{1z}/2} \cos(\theta\_{1y}/2) \end{pmatrix} \otimes \begin{pmatrix} e^{-i\theta\_{2z}/2} \cos(\theta\_{2y}/2) & -e^{-i\theta\_{2z}/2} \sin(\theta\_{2y}/2) \\ e^{i\theta\_{2z}/2} \sin(\theta\_{2y}/2) & e^{i\theta\_{2z}/2} \cos(\theta\_{2y}/2) \end{pmatrix} \\
&= \begin{pmatrix} e^{-i(\theta\_{1z}+\theta\_{2z})/2} c_1c_2 & e^{-i(\theta\_{1z}+\theta\_{2z})/2} c_1s_2 & e^{-i(\theta\_{1z}+\theta\_{2z})/2} s_1c_2 & e^{-i(\theta\_{1z}+\theta\_{2z})/2}  s_1s_2  \\ e^{-i\theta\_{1z}/2}e^{i\theta\_{2z}/2} c_1s_2& e^{-i\theta\_{1z}/2}e^{i\theta\_{2z}/2}  c_1c_2& e^{-i\theta\_{1z}/2}e^{i\theta\_{2z}/2}  s_1s_2& e^{-i\theta\_{1z}/2}e^{i\theta\_{2z}/2}  s_1c_2  \\ e^{i\theta\_{1z}/2}e^{-i\theta\_{2z}/2} s_1c_2& e^{i\theta\_{1z}/2}e^{-i\theta\_{2z}/2} s_1s_2& e^{i\theta\_{1z}/2}e^{-i\theta\_{2z}/2} c_1c_2& e^{i\theta\_{1z}/2}e^{-i\theta\_{2z}/2}  c_1s_2  \\ e^{i(\theta\_{1z}+\theta\_{2z})/2}  s_1s_2& e^{i(\theta\_{1z}+\theta\_{2z})/2}  s_1c_2& e^{i(\theta\_{1z}+\theta\_{2z})/2}  c_1s_2& e^{i(\theta\_{1z}+\theta\_{2z})/2} c_1c_2 \end{pmatrix} \end{align}
$$
dengan
$$ c_i=\cos\frac{\theta\_{iy}}2,\qquad s_i=\sin\frac{\theta\_{iy}}2.  $$
<br><br><br><br>

### Gerbang CNOT Total

**Matriks Gerbang Keterbelitan (*U*<sub>*e**n**t*</sub>) untuk 2 Qubit**

Untuk lapisan keterbelitan, secara umum didefinisikan:
$$
U\_{ent} = CNOT\_{(N-1,0)} \prod\_{q=0}^{N-2} CNOT\_{(q,q+1)}
$$

Untuk sistem 2 qubit, hal ini mereduksi menjadi:
*U*<sub>*e**n**t*</sub> = *C**N**O**T*<sub>(1, 0)</sub> ⋅ *C**N**O**T*<sub>(0, 1)</sub>

di mana matriks untuk masing-masing gerbang adalah:
$$
CNOT\_{(1,0)} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \quad CNOT\_{(0,1)} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
$$

Sehingga matriks total keterbelitannya adalah:
$$
U\_{ent} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \end{pmatrix}
$$
<br><br><br><br>

------------------------------------------------------------------------

## Optimizer SPSA

### Rumus Utama

**SPSA (Simultaneous Perturbation Stochastic Approximation)**

- **Inovasi:** Mengestimasi gradien *seluruh* parameter secara simultan
  hanya menggunakan dua pengukuran (satu vektor perturbasi acak *Δ*).
  $$ \hat{g}\_k = \frac{E(\theta_k + c_k \Delta_k) - E(\theta_k - c_k \Delta_k)}{2 c_k \Delta_k} $$
- Dengan ekspektasi estimasi gradien yang terbukti ekuivalen dengan
  gradien eksak:
  𝔼\[*ĝ*<sub>*k*</sub>\] = ∇*E*(*θ*<sub>*k*</sub>)

### Penurunan Rumus

**Penurunan: Estimator Gradien SPSA**

**Langkah 1 — Vektor Perturbasi Acak:**

$$\Delta_k = (\Delta\_{k,1}, \Delta\_{k,2}, \ldots, \Delta\_{k,p}), \quad \Delta\_{k,i} = \begin{cases} +1, & P = 1/2 \\ -1, & P = 1/2 \end{cases}$$

Setiap komponen mengikuti distribusi *Rademacher*.

<hr>

**Langkah 2 — Evaluasi Fungsi Biaya:**

*E*<sub>+</sub> = *E*(**θ**<sub>*k*</sub> + *c*<sub>*k*</sub>*Δ*<sub>*k*</sub>),  *E*<sub>−</sub> = *E*(**θ**<sub>*k*</sub> − *c*<sub>*k*</sub>*Δ*<sub>*k*</sub>)

<hr>

**Langkah 3 — Ekspansi Taylor:**

$$E\_+ = E(\boldsymbol{\theta}\_k) + c_k \sum\_{j=1}^{p} \Delta_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2}c_k^2 \sum\_{j=1}^{p} \Delta_j^2 \frac{\partial^2 E}{\partial \theta_j^2} + O(c_k^3)$$

$$E\_- = E(\boldsymbol{\theta}\_k) - c_k \sum\_{j=1}^{p} \Delta_j \frac{\partial E}{\partial \theta_j} + \frac{1}{2}c_k^2 \sum\_{j=1}^{p} \Delta_j^2 \frac{\partial^2 E}{\partial \theta_j^2} + O(c_k^3)$$

<hr>

**Langkah 4 — Selisih (suku genap saling hilang):**

$$E\_+ - E\_- = 2c_k \sum\_{j=1}^{p} \Delta_j \frac{\partial E}{\partial \theta_j} + O(c_k^3)$$

<hr>

**Langkah 5 — Estimator Gradien:**

$$\hat{g}\_i = \frac{E\_+ - E\_-}{2c_k \Delta_i} = \frac{\partial E}{\partial \theta_i} + \sum\_{j \neq i} \frac{\Delta_j}{\Delta_i} \frac{\partial E}{\partial \theta_j}$$

<hr>

**Langkah 6 — Bukti Tak-Bias:**

Karena *Δ*<sub>*j*</sub> independen dan
$\mathbb{E}\left\[\frac{\Delta_j}{\Delta_i}\right\] = 0$ untuk
*j* ≠ *i*:

$$\mathbb{E}\[\hat{g}\_i\] = \frac{\partial E}{\partial \theta_i} + \sum\_{j \neq i} \underbrace{\mathbb{E}\left\[\frac{\Delta_j}{\Delta_i}\right\]}\_{= 0} \frac{\partial E}{\partial \theta_j} = \frac{\partial E}{\partial \theta_i}$$

$$\therefore \boxed{\mathbb{E}\[\hat{\mathbf{g}}\_k\] = \nabla E(\boldsymbol{\theta}\_k)}$$

<hr>

**Langkah 7 — Pembaruan Parameter & Peluruhan:**

$$\boldsymbol{\theta}\_{k+1} = \boldsymbol{\theta}\_k - a_k \hat{\mathbf{g}}\_k$$

dengan hiperparameter peluruhan:

$$a_k = \frac{a}{(A+k+1)^\alpha}, \quad c_k = \frac{c}{(k+1)^\gamma}$$

<br><br><br>

:::

:::

------------------------------------------------------------------------

## Evaluasi Distribusi Probabilitas (Entropi)

### Evolusi Entropi: Studi Kasus Numerik

Pemanfaatan Entropi Von Neumann dalam memantau jejak persebaran
probabilitas di titik konvergensi akhir VQE.

**Sistem *N* = 2**

<table>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: center;">Nilai</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Probabilitas mayoritas (<span
class="math inline"><em>p</em><sub>1</sub></span>)</td>
<td style="text-align: center;"><span
class="math inline">0, 98</span></td>
</tr>
<tr>
<td style="text-align: left;">Sisa probabilitas (<span
class="math inline"><em>p</em><sub>rest</sub></span>)</td>
<td style="text-align: center;"><span
class="math inline">0, 02</span></td>
</tr>
</tbody>
</table>

**Kalkulasi:**
*S* = −(0, 98 ⋅ log<sub>2</sub>(0, 98) + 0, 02 ⋅ log<sub>2</sub>(0, 02)) ≈ 0, 1414 bit
→ Probabilitas sangat tersentralisasi dan stabil.

**Sistem *N* = 4**

<table>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: center;">Nilai</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Prob. Optimal (<span
class="math inline"><em>p</em><sub>1</sub></span>)</td>
<td style="text-align: center;"><span
class="math inline">0, 94</span></td>
</tr>
<tr>
<td style="text-align: left;">Prob. Alternatif (<span
class="math inline"><em>p</em><sub>2</sub>, <em>p</em><sub>3</sub>, <em>p</em><sub>4</sub></span>)</td>
<td style="text-align: center;">@ <span
class="math inline">0, 02</span></td>
</tr>
</tbody>
</table>

**Kalkulasi:**
*S* = −(0, 94log<sub>2</sub>(0, 94) + 3 × (0, 02log<sub>2</sub>(0, 02))) ≈ 0, 4225 bit
→ Jauh di bawah batas entropi maksimum log<sub>2</sub>(4) = 2 bit →
deteksi *ground state* handal.

### Penurunan Rumus

**Generalisasi: Dari Entropi Shannon ke Entropi Von Neumann**

**Langkah 1 — Entropi Shannon (Klasik):**

Untuk distribusi probabilitas diskrit *p*<sub>*i*</sub>, entropi
informasi didefinisikan sebagai:

*H* = −∑<sub>*i*</sub>*p*<sub>*i*</sub>log<sub>2</sub>(*p*<sub>*i*</sub>)

<hr>

**Langkah 2 — Definisi Entropi Von Neumann:**

Dalam mekanika kuantum, probabilitas digantikan oleh operator densitas
*ρ*. Entropi Von Neumann didefinisikan langsung melalui fungsi operator
tersebut:

*S*(*ρ*) = −Tr(*ρ*log<sub>2</sub>*ρ*)

<hr>

**Langkah 3 — Teorema Spektral:**

Karena operator densitas *ρ* bersifat Hermitian, ia selalu dapat
didiagonalisasi (dekomposisi spektral):

*ρ* = *U**Λ**U*<sup>†</sup>

dengan *Λ* adalah matriks diagonal yang berisi nilai eigen
*λ*<sub>*i*</sub>, dan *U* adalah matriks uniter.

<hr>

**Langkah 4 — Logaritma Matriks:**

Berdasarkan definisi fungsi matriks, logaritma diterapkan pada nilai
eigennya:

log<sub>2</sub>(*ρ*) = *U*(log<sub>2</sub>*Λ*)*U*<sup>†</sup>

<hr>

**Langkah 5 — Operasi *Trace* dan Invariansi:**

Kita kalikan *ρ* dengan log<sub>2</sub>(*ρ*):

*ρ*log<sub>2</sub>(*ρ*) = (*U**Λ**U*<sup>†</sup>)(*U*(log<sub>2</sub>*Λ*)*U*<sup>†</sup>) = *U*(*Λ*log<sub>2</sub>*Λ*)*U*<sup>†</sup>

Gunakan sifat invariansi *trace* (Tr(*U**A**U*<sup>†</sup>) = Tr(*A*)):

*S*(*ρ*) = −Tr(*U*(*Λ*log<sub>2</sub>*Λ*)*U*<sup>†</sup>) = −Tr(*Λ*log<sub>2</sub>*Λ*)

Karena *Λ* adalah matriks diagonal, perhitungan *trace*-nya hanyalah
jumlahan dari elemen diagonal:

$$\boxed{S(\rho) = -\sum_i \lambda_i \log_2 (\lambda_i)}$$

<hr>

**Langkah 6 — Reduksi ke Bentuk Klasik:**

Jika *ρ* sudah dalam bentuk diagonal murni di mana matriksnya mewakili
campuran klasik murni, maka nilai eigen *λ*<sub>*i*</sub> akan sama
dengan probabilitas *p*<sub>*i*</sub>, sehingga rumusnya akan mereduksi
secara identik menjadi Entropi Shannon biasa.

<br><br>

:::

:::::

------------------------------------------------------------------------

## Algoritma Evaluasi: *Backtesting*

**Skema *Rolling Window Backtesting*:**

``` pseudocode
Procedure BacktestLoop(Data, K)
  1. For t in Timeline:
  2.    mu, Sigma, gamma <- DataPreprocessing(t)
  3.    H <- BuildHamiltonian(mu, Sigma, gamma)
  4.    x_NE <- NashSBR(H) // Pencarian Titik Ekuilibrium
  5.    x_best_t <- AdaptiveVQE(H, x_NE) // GT-VQE Optimization
  6.    R_t <- ExecuteRebalance(x_best_t) // Pindah Aset Berdasarkan Sinyal
  7. Return PerformanceMetrics
EndProcedure
```

- Siklus dieksekusi secara iteratif melalui jendela waktu berjalan
  (*sliding window*) untuk mengevaluasi adaptabilitas model terhadap
  fluktuasi riil data historis pasar.

------------------------------------------------------------------------

## Perhitungan Metrik Performa Finansial

### Metrik Finansial

Untuk membandingkan performa model GT-VQE dengan *Equal Weight* dan
optimasi klasik (SLSQP), parameter evaluasi yang dihitung mencakup:

- **Return Kumulatif:** Mengukur total pertumbuhan persentase modal
  selama periode simulasi.
  $$ R\_{cum} = \prod\_{t=1}^T (1 + R_t) - 1 $$
- **Sharpe Ratio:** Rasio antara *return* ekspektasi terhadap risiko
  volatilitas portofolio (*σ*<sub>*p*</sub>).
  $$ \text{Sharpe} = \frac{\bar{R}\_p - R_f}{\sigma_p} $$

- **Maximum Drawdown (MDD):** Risiko kerugian maksimal dari puncak
  historis portofolio.
  $$ MDD = \max \frac{P\_{peak} - P\_{t}}{P\_{peak}} $$
- **Equal Weight & SLSQP:** Sebagai *benchmark*, nilai metrik juga
  dievaluasi untuk portofolio *w*<sub>*i*</sub> = 1/*K* (*Equal Weight*)
  dan penyelesaian Lagrangian kontinu berbasis *Sequential Least Squares
  Programming* (SLSQP).

### Optimasi Klasik SLSQP

Algoritma *Sequential Least Squares Programming* untuk menyelesaikan
sub-masalah pemrograman kuadratik sebagai standar komparasi.

``` pseudocode
Procedure SLSQPOptimizer(mu, Sigma, gamma)
  1. w_0 <- InitialWeights(1/N)
  2. B_0 <- I // Inisialisasi Hessian Identitas
  3. For k = 0, 1, 2, ... until converged:
  4.     g_k <- gamma * Sigma * w_k - mu // Hitung Gradien
  5.     Solve Sub-QP: min(g_k^T d + 0.5 d^T B_k d) s.t. constraints
  6.     a_k <- LineSearch(w_k, d)
  7.     w_{k+1} <- w_k + a_k * d
  8.     s_k <- w_{k+1} - w_k, y_k <- g_{k+1} - g_k
  9.     B_{k+1} <- UpdateBFGS(B_k, s_k, y_k)
  10. Return w_final
EndProcedure
```

# Fase Hasil dan Pembahasan

## Simulasi Interaktif Konvergensi VQE

<iframe src="interactive_vqe.html" width="100%" height="600px" style="border:none; border-radius:15px; background:transparent;">
</iframe>

Silakan sesuaikan parameter bias dan interaksi (*h*<sub>*i*</sub>,
*J*<sub>*i**j*</sub>) lalu klik <b>Mulai SPSA</b> untuk melihat simulasi
konvergensi.

------------------------------------------------------------------------

## Analisis Entropi Von Neumann

**Entropi Tinggi (Solusi Tidak Optimal)** ::: {style=“text-align:
center; margin-top: 10px;”}
<img src="../Gambar/Entropi_tinggi.png" style="width:100.0%" />

Probabilitas (*state*) tersebar merata. Hal ini menunjukkan indikasi
*barren plateau* atau kondisi di mana VQE belum menemukan *ground
state*.

**Entropi Rendah (Solusi Optimal)** ::: {style=“text-align: center;
margin-top: 10px;”}
<img src="../Gambar/Entropi_rendah.png" style="width:100.0%" />

Probabilitas mengkristal di satu *state* dominan. Solusi telah konvergen
ke titik minimum energi global.

::::

:::::

------------------------------------------------------------------------

## Pergerakan Harga Saham (*N* = 4)

Kombinasi saham BBCA, ADRO, TLKM, dan SMGR (2021-2023) dievaluasi dengan
mekanisme *rebalancing* bulanan.

![](../Gambar/pergerakan_harga_asli_N4.png)

------------------------------------------------------------------------

## Perbandingan Pertumbuhan Modal Benchmark (*N* = 2)

Perbandingan performa *backtesting* antara Portofolio Nash murni (tanpa
VQE) dan optimasi portofolio klasik SLSQP untuk 2 aset.

**Portofolio Nash Murni** ![](../Gambar/hasil_backtest_nash_N2.png)

**Optimasi Klasik (SLSQP)** ![](../Gambar/slsqp_vs_benchmarks_N2.png)

------------------------------------------------------------------------

## Perbandingan Pertumbuhan Modal Benchmark (*N* = 4)

Perbandingan performa *backtesting* antara Portofolio Nash murni (tanpa
VQE) dan optimasi portofolio klasik SLSQP untuk 4 aset.

**Portofolio Nash Murni** ![](../Gambar/hasil_backtest_nash_N4.png)

**Optimasi Klasik (SLSQP)** ![](../Gambar/slsqp_vs_benchmarks_N4.png)

------------------------------------------------------------------------

## Perbandingan Pertumbuhan Modal (*N* = 2)

Perbandingan antara VQE Murni (Tanpa GT) dan Algoritma GT-VQE (Hibrida)
untuk 2 aset.

**VQE Murni (Tanpa GT)** ![](../Gambar/NoGT_hasil_backtest_vqe_N2.png)

**GT-VQE (Hibrida)** ![](../Gambar/GT_hasil_backtest_vqe_N2.png)

------------------------------------------------------------------------

## Perbandingan Pertumbuhan Modal (*N* = 4)

Perbandingan antara VQE Murni (Tanpa GT) dan Algoritma GT-VQE (Hibrida)
untuk 4 aset.

**VQE Murni (Tanpa GT)** ![](../Gambar/NoGT_hasil_backtest_vqe_N4.png)

**GT-VQE (Hibrida)** ![](../Gambar/GT_hasil_backtest_vqe_N4.png)

------------------------------------------------------------------------

## Ringkasan Performa Simulasi Finansial

Tabel perbandingan *backtesting* strategi Kuantum, SLSQP, dan *Equal
Weight* untuk Sistem *N* = 2 dan *N* = 4.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Strategi Algoritma</th>
<th style="text-align: center;">Return (<span
class="math inline"><em>N</em> = 2</span>)</th>
<th style="text-align: center;">Sharpe (<span
class="math inline"><em>N</em> = 2</span>)</th>
<th style="text-align: center;">MDD (<span
class="math inline"><em>N</em> = 2</span>)</th>
<th style="text-align: center;">Return (<span
class="math inline"><em>N</em> = 4</span>)</th>
<th style="text-align: center;">Sharpe (<span
class="math inline"><em>N</em> = 4</span>)</th>
<th style="text-align: center;">MDD (<span
class="math inline"><em>N</em> = 4</span>)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>GT-VQE (Hibrida)</strong></td>
<td style="text-align: center;"><strong>145,07%</strong></td>
<td style="text-align: center;"><strong>1,0185</strong></td>
<td style="text-align: center;">30,33%</td>
<td style="text-align: center;"><strong>73,15%</strong></td>
<td style="text-align: center;"><strong>1,0107</strong></td>
<td style="text-align: center;"><strong>16,68%</strong></td>
</tr>
<tr>
<td style="text-align: left;">VQE (Tanpa GT)</td>
<td style="text-align: center;">121,30%</td>
<td style="text-align: center;">0,9331</td>
<td style="text-align: center;">30,33%</td>
<td style="text-align: center;">16,89%</td>
<td style="text-align: center;">0,3592</td>
<td style="text-align: center;">20,89%</td>
</tr>
<tr>
<td style="text-align: left;">SLSQP (Klasik)</td>
<td style="text-align: center;">51,34%</td>
<td style="text-align: center;">0,6736</td>
<td style="text-align: center;"><strong>15,91%</strong></td>
<td style="text-align: center;">12,91%</td>
<td style="text-align: center;">0,2810</td>
<td style="text-align: center;">21,12%</td>
</tr>
<tr>
<td style="text-align: left;"><em>Equal Weight</em></td>
<td style="text-align: center;">97,88%</td>
<td style="text-align: center;">0,9764</td>
<td style="text-align: center;">27,49%</td>
<td style="text-align: center;">35,57%</td>
<td style="text-align: center;">0,6790</td>
<td style="text-align: center;">18,42%</td>
</tr>
</tbody>
</table>

**Catatan:** GT-VQE mendominasi performa pengembalian maupun rasio
*Sharpe* karena inisialisasi *Nash Equilibrium* berhasil mengeksploitasi
informasi struktural pasar.

------------------------------------------------------------------------

## Kesimpulan

### Formulasi EPG

Formulasi model Markowitz ke dalam kerangka <i>Exact Potential Game</i>
(EPG) telah berhasil memetakan utilitas ekonomi menjadi sistem
Hamiltonian fisis secara akurat. Penggunaan <i>log return</i> efektif
menjaga simetri interaksi risiko tanpa distorsi, sementara implementasi
suku penalti mencegah sirkuit kuantum terjebak pada status portofolio
yang melanggar diversifikasi.

➜

### Warm-Start Nash

Penerapan <i>Pure Strategy Nash Equilibrium</i> (PSNE) terbukti
meningkatkan efisiensi algoritma VQE. Injeksi solusi Nash memandu
sirkuit melewati area <i>barren plateaus</i> dan memicu keruntuhan
entropi <i>Von Neumann</i>, memungkinkan pencapaian <i>ground state</i>
pada kedalaman sirkuit yang sangat dangkal (*L* = 2 hingga *L* = 3).

➜

### Performa GT-VQE

Kombinasi arsitektur <i>Hardware-Efficient Ansatz</i> dengan optimasi
SPSA memungkinkan sistem merespons volatilitas pasar melalui mekanisme
rebalancing dinamis. Hasil <i>backtesting</i> memvalidasi bahwa
algoritma GT-VQE menghasilkan pertumbuhan modal superior dibandingkan
VQE murni dan metode klasik dengan <i>Sharpe Ratio</i> 1,0107 (*N* = 4).

------------------------------------------------------------------------

## Saran Pengembangan

### Noise Sirkuit

Mempertimbangkan parameter <i>noise</i> sirkuit, seperti dekoherensi
qubit dan <i>gate fidelity</i> dalam mengeksekusi algoritma ini agar
divalidasi dan diaplikasikan pada infrastruktur perangkat keras kuantum
sesungguhnya.

➜

### Variasi Ansatz

Menggunakan variasi struktur <i>ansatz</i> lain (seperti
<i>Qubit-Efficient</i> atau <i>Variational Quantum Circuit</i>) serta
membandingkan performa berbagai algoritma optimasi klasik lainnya untuk
menemukan kombinasi hibrida dengan laju konvergensi paling efisien.

➜

### Black Swan

Menggunakan rentang periode data historis yang lebih panjang dan
melakukan pengujian pada periode fenomena <i>Black Swan</i> atau krisis
ekonomi untuk mengevaluasi agilitas dan reliabilitas algoritma dalam
mempertahankan stabilitas portofolio di pasar ekstrem.

------------------------------------------------------------------------

<br><br> ::: {style=“text-align: center;”}
<h1>
Terima Kasih
</h1>
<p>
Ada Pertanyaan?
</p>

:::
