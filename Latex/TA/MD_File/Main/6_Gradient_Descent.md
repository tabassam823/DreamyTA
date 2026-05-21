# Algoritma *Gradient Descent* dalam Optimasi Portofolio

## 1. Prinsip Dasar *Gradient Descent*
*Gradient Descent* (GD) merupakan algoritma optimasi orde pertama yang bekerja dengan cara memperbarui variabel secara iteratif ke arah negatif dari gradien fungsi tujuan. Dalam konteks optimasi portofolio, tujuan utamanya adalah menemukan vektor bobot $\mathbf{w}$ yang meminimalkan fungsi biaya Markowitz yang telah dimodifikasi dengan suku penalti (*EPG*). Algoritma ini didasarkan pada asumsi bahwa jika fungsi biaya $L(\mathbf{w})$ didefinisikan dan dideferensialkan dalam lingkungan titik $\mathbf{w}$, maka $L(\mathbf{w})$ akan berkurang paling cepat jika kita melangkah ke arah negatif gradien.

Proses iterasi dimulai dengan inisialisasi bobot secara acak atau seragam, kemudian dilakukan pembaruan terus-menerus hingga mencapai kriteria konvergensi tertentu. Kriteria konvergensi biasanya ditentukan berdasarkan nilai gradien yang mendekati nol atau perubahan fungsi biaya yang sudah tidak signifikan lagi. GD sangat populer dalam masalah optimasi skala besar karena efisiensi komputasinya yang hanya membutuhkan informasi turunan pertama, sehingga sangat cocok untuk diintegrasikan dengan pemodelan portofolio aset yang melibatkan matriks kovariansi kompleks.

## 2. Formulasi Aturan Pembaruan (*Update Rule*)
Aturan pembaruan bobot portofolio dalam setiap iterasi $t$ didefinisikan melalui pengurangan posisi saat ini dengan hasil perkalian antara *learning rate* ($\eta$) dan vektor gradien. Berdasarkan fungsi biaya $L$ yang telah menyertakan suku penalti kesamaan, aturan pembaruan untuk setiap elemen $w_k$ adalah sebagai berikut:
$$\begin{equation}
w_k^{(t+1)} = w_k^{(t)} - \eta \frac{\partial L}{\partial w_k^{(t)}}
\end{equation}$$
Substitusi derivasi gradien dari formulasi EPG ke dalam persamaan (1) menghasilkan:
$$\begin{equation}
w_k^{(t+1)} = w_k^{(t)} - \eta \left[ \left( \sum_{j=1}^n \sigma_{kj} w_j^{(t)} - q \mu_k \right) + \lambda \left( \sum_{i=1}^n w_i^{(t)} - 1 \right) \right]
\end{equation}$$

Komponen pertama di dalam kurung siku merepresentasikan arah menuju minimisasi risiko dan maksimisasi imbal hasil, sedangkan komponen kedua merepresentasikan arah menuju pemenuhan kendala anggaran. Parameter *learning rate* $\eta$ (juga dikenal sebagai *step size*) memegang peranan krusial dalam menentukan kecepatan konvergensi. Jika $\eta$ terlalu besar, sistem dapat melampaui titik minimum dan menyebabkan divergensi; sebaliknya, jika $\eta$ terlalu kecil, proses optimasi akan berjalan sangat lambat dan berisiko terjebak pada titik stasioner yang tidak optimal.

## 3. Dinamika Konvergensi dan Jalur Gradien
Visualisasi jalur gradien dalam ruang bobot memberikan wawasan mendalam mengenai bagaimana algoritma menavigasi permukaan fungsi biaya (*loss landscape*). Pada awal iterasi, vektor gradien biasanya memiliki magnitudo yang besar, yang menyebabkan perubahan bobot yang signifikan menuju area dengan energi rendah. Seiring dengan mendekatnya solusi ke titik optimal, magnitudo gradien akan mengecil secara asimtotik, yang mencerminkan stabilitas sistem dalam mencapai kesetimbangan antara risiko, imbal hasil, dan kendala.

Gambar 1 mengilustrasikan kontur fungsi biaya Markowitz dalam ruang dua dimensi beserta jalur konvergensi algoritma GD. Garis kontur yang berbentuk elips merepresentasikan permukaan varians portofolio, di mana pusat elips adalah titik minimum tanpa kendala. Jalur gradien yang dihasilkan oleh EPG akan menunjukkan pergerakan melengkung yang awalnya tegak lurus terhadap kontur varians, namun kemudian ditarik oleh gradien penalti menuju garis lurus $\sum w_i = 1$. Koherensi antara narasi matematis dan representasi visual ini sangat penting untuk memvalidasi bahwa algoritma bekerja sesuai dengan prinsip-prinsip kalkulus vektor yang mendasarinya.

## 4. Limitasi dan Variasi Stokastik
Meskipun *Gradient Descent* standar (atau *Batch Gradient Descent*) sangat stabil, ia memiliki limitasi ketika dihadapkan pada permukaan fungsi biaya yang sangat non-konveks atau memiliki banyak minimum lokal. Pada sistem keuangan dengan volatilitas tinggi, permukaan biaya mungkin memiliki noise yang signifikan. Hal ini mendorong penggunaan variasi algoritma seperti *Stochastic Gradient Descent* (SGD) atau *Simultaneous Perturbation Stochastic Approximation* (SPSA) untuk meningkatkan peluang menemukan minimum global melalui eksplorasi ruang parameter yang lebih luas.

Selain itu, pemilihan skema *learning rate* yang adaptif seperti *Adam* atau *RMSprop* dapat membantu mengatasi masalah skala gradien yang berbeda antar aset. Dalam implementasi hibrida klasik-kuantum seperti VQE, algoritma optimasi klasik (GD atau variasinya) digunakan untuk memperbarui parameter sirkuit kuantum berdasarkan pengukuran energi. Integrasi ini menunjukkan bahwa pemahaman mendalam tentang *Gradient Descent* klasik tetap menjadi fondasi yang tak tergantikan dalam pengembangan teknologi keuangan berbasis kuantum di masa depan.

## 5. Penurunan Rumus
$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle
$$
jika dimisalkan
$$
\begin{split}
\psi(\theta) &= \hat{U}_B \hat{U}(\theta) \hat{U}_A \ket{\phi} 
\quad \text{di mana} \quad \hat{U}{\theta} = e^{-i\frac{\theta}{2}\sigma} \\
\end{split}
$$
maka
$$
\begin{split}
E(\theta) &= \bra{0} \hat{U}_A^\dagger \hat{U}(\theta) \hat{U}_B^\dagger \hat{H} \hat{U}_B \hat{U}(\theta) \hat{U}_A \ket{0} \\
&= \bra{\phi} \hat{U}^\dagger (\theta) \hat{U}_B^\dagger \hat{H} \hat{U}_B \hat{U} (\theta) \ket{\phi} \\
&= \bra{\phi} \hat{U}^\dagger (\theta) \hat{M} \hat{U} (\theta) \ket{\phi}
\end{split}
$$
dengan $\hat{M} = \hat{U}_B^\dagger \hat{H} \hat{U}_B$

ekspektasi energi adalah ekspektasi dari hamiltonian  sebagai matriks $M$
$$\begin{split}
\langle E(\theta)\rangle &= \bra{\phi} U^{\dagger}(\theta) M U(\theta) \ket{\phi} \\

\frac{\partial \langle E(\theta)\rangle}{\partial \theta}&= \bra{\phi} \frac{\partial U^{\dagger}(\theta)}{\partial \theta} M U(\theta) \ket{\phi} + \bra{\phi} U^{\dagger}(\theta) M \frac{\partial U(\theta)}{\partial \theta} \ket{\phi}
\end{split}$$
karena $U(\theta) = e^{-i\frac{\theta}{2}\sigma}$ , sehingga
$$
\frac{\partial U (\theta)}{\partial \theta}=-\frac{i}{2}\sigma U(\theta) \quad; \frac{\partial U^{\dagger}(\theta)}{\partial \theta} = \frac{i}{2}\sigma U^{\dagger}(\theta)
$$

sehingga dengan persamaan $\ket{\psi(\theta)}=U(\theta) \ket{\phi}$ dan seterunsya, maka
$$\begin{split}
\frac{\partial \langle E(\theta)\rangle}{\partial \theta}
&= \bra{\phi} \left(\frac{i}{2}\sigma U^{\dagger}(\theta)\right) M U(\theta) \ket{\phi} + \bra{\phi} U^{\dagger}(\theta) M \left(-\frac{i}{2}\sigma U(\theta)\right) \ket{\phi} \\
&= \frac{i}{2} \bra{\psi(\theta)} \sigma M \ket{\psi(\theta)} - \frac{i}{2} \bra{\psi(\theta)} M \sigma \ket{\psi(\theta)} \\
&= \frac{i}{2} \bra{\psi(\theta)} \sigma M - M \sigma \ket{\psi(\theta)} \\
&= \frac{i}{2} \bra{\psi(\theta)} [\sigma, M] \ket{\psi(\theta)}
\end{split}$$

lalu kita berikan pergeseran $\theta$ sebesar $s$ sehingga
$$\begin{split}
U(\theta + s) &= \exp\left(-i\left(\frac{\theta + s}{2}\right)\right) \\

&= \exp\left(-i\left(\frac{\theta}{2}\right)\right) \exp\left(-i\left(\frac{s}{2}\right)\right) \\

&= U(s) U(\theta)
\end{split}$$
begitu pula dengan pergeseran ke kiri
$$\begin{split}
U(\theta + s) &= \exp\left(-i\left(\frac{\theta - s}{2}\right)\right) \\

&= \frac{\exp\left(-i\left(\frac{\theta}{2}\right)\right)} {\exp\left(-i\left(\frac{s}{2}\right)\right)} \\

&= \frac{U(s)}{U(\theta)}
\end{split}$$

Dengan demikian pergeseran ke kanan bisa diproses:
$$\begin{align}
\langle E(\theta+s)\rangle &= \bra{\phi}U^{\dagger}(\theta)U^{\dagger}(s) M U(\theta)U(s) \ket{\phi} \\
&= \bra{\psi(\theta)} U^{\dagger}(s) M U(s) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right) I + i \sin\left(\frac{s}{2}\right) \sigma \right) M \left( \cos\left(\frac{s}{2}\right) I - i \sin\left(\frac{s}{2}\right) \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right) I + i \sin\left(\frac{s}{2}\right) \sigma \right) \left( \cos\left(\frac{s}{2}\right) M - i \sin\left(\frac{s}{2}\right) M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right)I \cos\left(\frac{s}{2}\right) M -  \cos\left(\frac{s}{2}\right) I i\sin\left(\frac{s}{2}\right) M \sigma + i \sin\left(\frac{s}{2}\right) \sigma \cos\left(\frac{s}{2}\right) M - i^2 \sin\left(\frac{s}{2}\right)\sigma \sin\left(\frac{s}{2}\right)  M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M - i \cos\left(\frac{s}{2}\right) \sin\left(\frac{s}{2}\right) M \sigma + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \sigma M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) (\sigma M - M \sigma) \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) [\sigma, M] \right) \ket{\psi(\theta)} \\
&= \cos^2\left(\frac{s}{2}\right) \bra{\psi(\theta)} M \ket{\psi(\theta)} + \sin^2\left(\frac{s}{2}\right) \bra{\psi(\theta)} \sigma M \sigma \ket{\psi(\theta)} + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \bra{\psi(\theta)} [\sigma, M] \ket{\psi(\theta)} \\
&= \cos^2\left(\frac{s}{2}\right) \langle M \rangle + \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle \\
\end{align}
$$

dengan cara yang sama, pergeseran ke kiri bisa diproses:
$$\begin{align}
\langle E(\theta-s)\rangle &= \bra{\phi}U^{\dagger}(\theta)U^{\dagger -1}(s) M U(\theta)U^{-1}(s) \ket{\phi} \\
&= \bra{\psi(\theta)} U^{\dagger -1}(s) M U^{-1}(s) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right) I - i \sin\left(\frac{s}{2}\right) \sigma \right) M \left( \cos\left(\frac{s}{2}\right) I + i \sin\left(\frac{s}{2}\right) \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right) I - i \sin\left(\frac{s}{2}\right) \sigma \right) \left( \cos\left(\frac{s}{2}\right) M + i \sin\left(\frac{s}{2}\right) M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos\left(\frac{s}{2}\right)I \cos\left(\frac{s}{2}\right) M +  \cos\left(\frac{s}{2}\right) I i\sin\left(\frac{s}{2}\right) M \sigma - i \sin\left(\frac{s}{2}\right) \sigma \cos\left(\frac{s}{2}\right) M - i^2 \sin\left(\frac{s}{2}\right)\sigma \sin\left(\frac{s}{2}\right)  M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M + i \cos\left(\frac{s}{2}\right) \sin\left(\frac{s}{2}\right) M \sigma - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \sigma M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) (M \sigma - \sigma M) \right) \ket{\psi(\theta)} \\
&= \bra{\psi(\theta)} \left( \cos^2\left(\frac{s}{2}\right) M + \sin^2\left(\frac{s}{2}\right) \sigma M \sigma - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) [\sigma, M] \right) \ket{\psi(\theta)} \\
&= \cos^2\left(\frac{s}{2}\right) \bra{\psi(\theta)} M \ket{\psi(\theta)} + \sin^2\left(\frac{s}{2}\right) \bra{\psi(\theta)} \sigma M \sigma \ket{\psi(\theta)} - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \bra{\psi(\theta)} [\sigma, M] \ket{\psi(\theta)} \\
&= \cos^2\left(\frac{s}{2}\right) \langle M \rangle + \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle \\
\end{align}
$$

sekarang dihitung selisih di antara kedua ekspektasi energi tersebut:
$$
\begin{split}
\langle E(\theta+s)\rangle - \langle E(\theta-s)\rangle &= \cos^2\left(\frac{s}{2}\right) \langle M \rangle + \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle - \left( \cos^2\left(\frac{s}{2}\right) \langle M \rangle + \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle - i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle \right) \\
&= \cos^2\left(\frac{s}{2}\right) \langle M \rangle + \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle - \cos^2\left(\frac{s}{2}\right) \langle M \rangle - \sin^2\left(\frac{s}{2}\right) \langle\sigma M \sigma\rangle + i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle \\
&= 2 i \sin\left(\frac{s}{2}\right) \cos\left(\frac{s}{2}\right) \langle [\sigma, M] \rangle \\
&= i \sin(s) \langle [\sigma, M] \rangle
\end{split}
$$

sehingga bisa didapatkan parameter shift rule;
$$\begin{align}
2 \frac{\partial \langle E(\theta)\rangle}{\partial \theta} &= i \langle [\sigma, M]\rangle \\
\frac{\partial \langle E(\theta)\rangle}{\partial \theta} &= \langle E(\theta+s)\rangle - \langle E(\theta-s)\rangle \\
&= \frac{1}{2} \left[\langle E(\theta+s)\rangle - \langle E(\theta-s)\rangle\right]
\end{align}
$$

---
---
## 6. dengan depth 4

$$
\begin{aligned}
U_{ent} &= CNOT_{0,1} \cdot CNOT_{1,0} \\
U_{ent} &= \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{pmatrix}
= \begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0
\end{pmatrix}
\end{aligned}
$$
$$
\ket{\psi (\theta)} = U_{rot}^{(4)} U_{ent} U_{rot}^{(3)} U_{ent} U_{rot}^{(2)} U_{ent} U_{rot}^{(1)} U_{ent} U_{rot}^{(0)} \ket{00} 
$$