Energi - representasi matematis dari risk-return trade-off

dalam model 2, model markowitz dinyatakan sebagai $$ E = \text{Resiko total} - \text{Bobot return} + \text{Batas penalti} $$

tugas kita adalah meminimalkan energi lewat mencari ground state. Meminimalkan energi dapat diperoleh dengan 
- meminimalkan resiko
- memaksimalkan return
- meminimalkan penalti (?)

secara matematis, model markowitz dinyatakan dengan persamaan: $$ \min_{x_i \in \{0,1\}} x^T \Sigma x - \lambda \mu^T x + A \left(\sum_{i=1}^N x_i - K \right)$$
 diman $N$ adalah jumlah aseet, $x_i$ adalah keputusan investasi (beli atau jual), $\mu$ adalah expected return, $\lambda$ adalah risk aversion, $\sigma$ adalah resiko total, dan $K$  adalah aset yang dibeli dari pilihan aset yang ada. 

## untuk suku pertama; 
$$
\begin{equation}
\begin{split}
x^T \Sigma x &= \sum_{ij} \Sigma_{ij} x_i x_j \\\\
&= \sum_i \Sigma_{ii} xi + \sum_{i \ne j} \Sigma_{ij} x_i x_j \\\\
\end{split}
\end{equation}
$$
dimana $\Sigma_{ii}$ adalah volatilitas individu dan $\Sigma_{ij}$ adalah korelasi antar aset. Untuk masing-masing $\Sigma$, $$ \Sigma = \begin{pmatrix} \sigma_A^2 & \sigma_{AB} \\ \sigma_{AB} & \sigma_B^2 \end{pmatrix} $$
dengan untuk masing-masing $\sigma$, $$
\begin{equation}
\begin{split}
\sigma_A &= \sqrt{\mathrm{Var}(A)}\\\\
\sigma_A &= \sqrt{\mathrm{Var}(B)} \\\\
\sigma_{AB} &= \frac{\mathrm{Cov}(A,B)}{\sigma_A \sigma_B}
\end{split}
\end{equation}
$$
dimana $$\mathrm{Cov}(A,B) = \frac{1}{T-1} \sum_{t=2}^T(R_{A,t} - \bar{R}_A)(R_{B,t} - \bar{R}_B)$$
dengan $R_{A,t}, R_{B,t}$ merupakan return harian dengan rumus $$R_{A,t}=\frac{P_{A,t}-P_{A,t-1}}{P_{A,t}}$$ dimana $P_{A,t}$ adalah harga aset A pada waktu t

## untuk suku kedua;
$$\lambda \mu^Tx$$ dimana $\lambda$ adalah risk aversion endogen dengan rumus $$\lambda=\frac{1}{1+e^{\frac{\mu}{\Sigma}}}$$ dan dengan rumus $\mu$ $$\mu=\frac{1}{T-1}\sum_{t=2}^N R_At$$

# Markowitz ke QUBO
$$\mathcal{L}(x)=x^T \Sigma x - \lambda \mu^T x + A \left(\sum_{i=1}^N x_i - K \right)$$

misal 2 aset dipilih salah satu ($K=1$):
$$
\begin{equation}
\begin{split}
\mathcal{L}(x) &= \begin{pmatrix}x_1 & x_2 \end{pmatrix} \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{pmatrix}  \begin{pmatrix}x_1 \\ x_2 \end{pmatrix} - \lambda \begin{pmatrix}\mu_1 & \mu_2 \end{pmatrix} \begin{pmatrix}x_1 \\ x_2 \end{pmatrix} + A \left(x_1 + x_2  - 1 \right)^2\\\\
&= (\sigma_1^2 x_1^2 + 2\sigma_{12}x_1x_2 + \sigma_2^2 x_2^2) - (\lambda \mu_1 x_1 + \lambda \mu_2 x_2) + A (x_1^2 + x_2^2 + 1 + 2x_1x_2 - 2x_1 - 2x_2)\\\\
&= \sigma_1^2 x_1 + 2\sigma_{12}x_1x_2 + \sigma_2^2 x_2 - \lambda \mu_1 x_1 - \lambda \mu_2 x_2 + A (x_1 + x_2 + 1 + 2x_1x_2 - 2x_1 - 2x_2)\\\\
&= (2\sigma_{12} + 2A)x_1x_2 + (\sigma_1^2 - \lambda\mu_1 - A)x_1 + (\sigma_2^2 - \lambda \mu_2 - A)x_2 + A
\end{split}
\end{equation}
$$
maka dapat dimisalkan:
$$\begin{split}
Q_{12} &= 2\sigma_{12} + 2A \\\\
C_1 &= \sigma_1^2 - \lambda\mu_1 - A \\\\
C_2 &= \sigma_2^2 - \lambda\mu_2 - A
\end{split}$$
sehingga persamaan menjadi:
$$\mathcal{L}(x_1,x_2) = Q_{12} x_1x_2 + C_1x_1 +C_2x_2 + A$$

### untuk $x_1 = 1, x_2 = 1$;
$$\mathcal{L} = \sigma_1^2 + \sigma_2^2 + 2\sigma_{12} - \lambda(\mu_1 + \mu_2) + A$$
### untuk $x_1 = 1, x_2 = 0$;
$$\mathcal{L} = \sigma_1^2 - \lambda\mu_1$$
### untuk $x_1 = 0, x_2 = 1$;
$$\mathcal{L} = \sigma_2^2 - \lambda\mu_2$$
### untuk $x_1 = 0, x_2 = 0$;
$$\mathcal{L} = A$$

## Markowitz ke QUBO ke Ising

prinsipnya adalah mengonversi sistem bilangan biner dari keputusan investasi aset menjadi bilangan spin di mana $$x_i = \frac{1-s_i}{2}$$ atau  $$s_i = -2x_i+1$$ namun jika disubstitusikan; $$
\begin{split}
E(s_1, s_2) &= Q_{12} \frac{1-s_i}{2}\frac{1-s_i}{2} + C_1\frac{1-s_i}{2} + C_2 \frac{1-s_i}{2} + \text{const} \\\\
&= Q_{12} \frac{1}{4} (1-s_1-s_2+s_1s_2) + \frac{1}{2} C_1 - \frac{1}{2}C_1s_1 + \frac{1}{2}C_2 - \frac{1}{2}C_2s_2 + \text{const} \\\\
&=\frac{1}{4} Q_{12}s_1s_2 - \left(\frac{1}{4}Q_{12} + \frac{1}{2}C_1\right)s_1 - \left(\frac{1}{4}Q_{12}+\frac{1}{2}C_2\right)s_2 + \frac{1}{4}Q_{12} +\frac{1}{2}C_1 + \frac{1}{2}C_2 + \text{const}
\end{split}
$$
dan jika dimisalkan $$
\begin{split}
J_{12} &= \frac{1}{4}Q_{12}
h_1 &= \frac{1}{4}Q_{12} + \frac{1}{2}C_1
h_2 &= \frac{1}{4}Q_{12} + \frac{1}{2}C_2
\end{split}
$$
maka persamaannya menjadi $$E(s_1,s_2) = J_{12} - h_1s_1 - h_2s_2 + \text{const}$$
.
.
.

sehingga hamiltoniannya menjadi $$H = J_{12}\sigma_1^2\sigma_2^2 - h_1 \sigma_1^2 - h_1\sigma_2^2 + \text{const}$$


## Ekspketasi dari energi
$$
\langle E \rangle = \bra{\psi(\theta_1\theta_2)} \hat{H} \ket{\psi(\theta_1\theta_2)}
$$
dimana untuk masing-masing ket
$$\ket{\psi(\theta_1\theta_2)} = \begin{pmatrix} 
\cos\theta_1 & -\sin\theta_1 \\ \sin\theta_1 & \cos\theta_1
\end{pmatrix} \otimes \begin{pmatrix} 
\cos\theta_2 & -\sin\theta_2 \\ \sin\theta_2 & \cos\theta_2
\end{pmatrix} \ket{00}$$ dimana $$\ket{00} = \begin{pmatrix} 1\\0\\0\\0 \end{pmatrix}$$
maka $$\frac{\partial\langle E\rangle}{\partial \theta} = ...$$