# I. INTRODUCTION
factor volatilitas
$$\bar{\sigma}_i (\tau_j) = \sqrt{\lambda_i} (\vec{v}_i)_j \quad (1)$$
# II. QUANTUM CIRCUIT
$$\sigma_N \in \mathbb{R}^N \times \mathbb{R}^N$$
$$\text{tr}[\sigma_N]=1$$
$$U = e^{it\sigma_N}$$
spectral decomposition
$$\sigma_N = \sum_{j=1}^{N} \lambda_j \ket{u_j} \bra{u_j}$$
dengan $0 \le \lambda_j \le 1$ dan $\sum_{j=1}^N \lambda_j=1$. bisa dibuat matriks
$$\rho_r = \sum_{j=1}^{N} \lambda_j \ket{u_j} \bra{u_j}$$
dengan $r \ll N$ 

random state
$$\ket{b} = \sum_{j=1}^N \beta_j \ket{u_j}$$

keadaan kuantum setelah QFT
$$\ket{\psi_b} = \sum_{j=1}^N \beta_j \ket{\Lambda_j^{(n)}} \otimes \ket{u_j}$$

$$\frac{1}{r} \approx \sum_{k=1}^n y_k 2^{-k}$$

$$\bra{y^{(n)}} \otimes \mathbb{1} \ket{\Psi_b} \approx \ket{u_{max}}$$

$$\bra{y^{(n)}} \otimes \mathbb{1} \ket{\Psi_b} \approx \sum_{j=1}^K \bar{\beta}_j \ket{u_j}$$
di mana $\bar{\beta}$ adalah $\beta$ yang ternormalisasi di dalam subspace

karena ketidaktahuan ap priori apakah $K \gt 1$ atau tidak, maka dapat dimulai dengan random state yang berbeda:
$$\ket{c} = \sum_{j=1}^K \gamma_i \ket{u_j}$$
sehingga
$$\ket{\Psi_c} = \sum_{j=1}^N \gamma_j \ket{\Lambda_J^{(n)}} \otimes \ket{u_j}$$
setelah proyeksi ke $\ket{y^{(n)}}$, ekspektasi keadaannya menjadi superposisi yang berbeda:
$$\sum_{j=1}^L \tilde{\gamma}_j \ket{u_j}$$

# III RESULTS

initial state
$$\ket{0} \otimes \ket{0} \otimes \ket{b_0}$$

untuk mengkodifikasi matriks kovarians ke keadaan kuantum, perlu normalisasi
$$\rho_n=\frac{\sigma_n}{\text{tr}(\sigma_n)}$$
dengan dekomposisi spektral $\lambda_n$ dan $\ket{u_2}$ 
> mengapa matriks kovarians harus dikodifikasi ke keadaan kuantum? dan mengapa harus menggunakan normalisasi dengan trace matriksnya

rumus fidelity QPE terhadap nilai max
$$F=|\langle u_{QPE}| u_{max}\rangle|^2$$

keadaan awal
$$\ket{b_0} = (\ket{00} + \ket{01} + \ket{10} + \ket{11})$$ nilai eigen estimasi
$$\Lambda_{max} = 0.b_1b_2b_3$$ 
# APPENDIX A
rumus nilai pasar uang terhadap waktu
$$B(t) = \exp{\left( -\int_0^t r(s)ds\right)}$$ hubungan short rate dan zero coupon dengan persamaan risk-neutral pricing
$$\begin{split}P(t,T) &= \mathbb{E}^{\mathbb{Q}_B} \left[\frac{B(t)}{B(T)} \times 1|\mathcal{F}_t \right] \\ &= \mathbb{E}^{\mathbb{Q}_B} \left[e^{-\int_t^T r(s)ds} |\mathcal{F}_t\right]\end{split}$$
hubungan antara forward rates dan short rate dibangun dari
$$\begin{split}f(t,T) &=-\frac{\partial}{\partial T} \log{P(t,T)} \\ 
P(t,T) &= e^{-\int_t^T f(t,s)ds}\\
-\frac{\partial P(t,T)}{\partial T} &= \mathbb{E}^{\mathbb{Q}_B} \left[\exp{\left(-\int_t^T r(s)ds\right)} r(T)|\mathcal{F}_t\right] \\
&= \mathbb{E}^{\mathbb{Q}_B} \left[\left.\exp{\left(-\int_t^T r(s)ds\right)} r(T) \frac{P(t,T)}{\exp{\left(-\int_t^T r(s)ds \right)}} \right| \mathcal{F}_t\right] \\
&= P(t,T) \mathbb{E}^{\mathbb{Q}_T} [r(T) | \mathcal{F}_t]
\end{split}$$
sehingga pada model HJM, evolusi risk-neutral zero-coupon harga obligasi didapat dari persamaan
$$dP(r,T) = P(t,T) \left\{r(t)dt + \sum_{i=1}^N \left(\int_t^T \sigma_i(t,s) dW_i(t) \right) \right\}
$$
jika menggunakan fungsi dinamika harga obligasi
$$df(t,T) = \alpha(t,T)dt + \sum_{i=1}^N \sigma_i(t,T) dW_i(t)
$$
dimana
$$\alpha(t,T) = \sum_{i=1}^N \sigma_i(t,T) \int_t^T \sigma_i(t,s)ds
$$

faktor volatilitas
$$\bar{\sigma_i}(\tau_j) = \sqrt{\lambda_i}(\mathbf{v}_i)_j
$$

rumus eror total dari eror per gerbang 2 qubit
$$\delta= \sum \frac{\text{Fidelity}}{\text{number of two-qubit gates}}
$$
dimana eror per gerbang
$$\delta_{\text{two-qubit gate}} = \frac{\text{Fidelity}}{\text{number of two-qubit gates}}
$$

vektor yang digunakan
$$\ket{+} = 1/\sqrt{2} (\ket{0} + \ket{1})
$$
yang diproyeksikan ke
$$\ket{y^{(n)}} = \ket{111}
$$
arah arbiter 
$$r = \begin{pmatrix}\cos \alpha &-e^{i\beta} \sin \alpha \\ e^{i\beta} \sin \alpha & e^{i\gamma}\cos\alpha \end{pmatrix}
$$