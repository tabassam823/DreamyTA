Tentu, mari kita dalami Bagian 1, yaitu bagaimana membangun Operator Ansatz $\hat{U}(\theta)$. Kita akan membedahnya secara matematis dengan bentuk matriks lengkap, contoh numerik, dan analisis sensitivitas untuk melihat bagaimana perubahan variabel ekstrem memengaruhi sirkuit.

### 1. Dekomposisi Matriks: Gerbang $R_y$ dan $R_z$

Seperti yang telah kita bahas, rotasi dilakukan oleh dua gerbang utama:

- **Gerbang $R_y(\theta)$:** Memutar status di sepanjang sumbu Y pada Bola Bloch. Ini mengubah amplitudo (probabilitas). Matriksnya adalah:
    
    $$R_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$
    
- **Gerbang $R_z(\theta)$:** Memutar status di sepanjang sumbu Z pada Bola Bloch. Ini memberikan fase relatif tanpa mengubah probabilitas pengukurannya pada basis komputasional (sumbu Z). Matriksnya adalah:
    
    $$R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$$
    

Dalam arsitektur _EfficientSU2_ (lapisan rotasi tunggal), gerbang-gerbang ini diaplikasikan secara berurutan pada satu qubit. Misalnya, $R_y$ lalu $R_z$:

$$U_{1q}(\theta_y, \theta_z) = R_z(\theta_z) \cdot R_y(\theta_y)$$

Mari kita kalikan matriksnya:

$$U_{1q}(\theta_y, \theta_z) = \begin{pmatrix} e^{-i\theta_z/2} & 0 \\ 0 & e^{i\theta_z/2} \end{pmatrix} \begin{pmatrix} \cos(\theta_y/2) & -\sin(\theta_y/2) \\ \sin(\theta_y/2) & \cos(\theta_y/2) \end{pmatrix}$$

$$U_{1q}(\theta_y, \theta_z) = \begin{pmatrix} e^{-i\theta_z/2} \cos(\theta_y/2) & -e^{-i\theta_z/2} \sin(\theta_y/2) \\ e^{i\theta_z/2} \sin(\theta_y/2) & e^{i\theta_z/2} \cos(\theta_y/2) \end{pmatrix}$$

### 2. Contoh Numerik dan Sensitivitas (1 Qubit)

Mari kita asumsikan status awal qubit kita adalah $|0\rangle$, dan kita aplikasikan operator $U_{1q}$:

$$|\psi\rangle = U_{1q}(\theta_y, \theta_z) \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} e^{-i\theta_z/2} \cos(\theta_y/2) \\ e^{i\theta_z/2} \sin(\theta_y/2) \end{pmatrix}$$

Probabilitas untuk mengukur status $|0\rangle$ adalah:

$$P(|0\rangle) = |e^{-i\theta_z/2} \cos(\theta_y/2)|^2 = \cos^2(\theta_y/2)$$

Probabilitas untuk mengukur status $|1\rangle$ adalah:

$$P(|1\rangle) = |e^{i\theta_z/2} \sin(\theta_y/2)|^2 = \sin^2(\theta_y/2)$$

Mari kita lakukan Analisis Sensitivitas pada variabel ekstrem:

**Sensitivitas terhadap $\theta_y$ (Amplitudo):**

- **Kasus Ekstrem 1 ($\theta_y = 0$):** $P(|0\rangle) = \cos^2(0) = 1$, $P(|1\rangle) = 0$. Rotasi 0 radian tidak memberikan perubahan. Sistem tertahan di status awal.
    
- **Kasus Ekstrem 2 ($\theta_y = \pi$):** $P(|0\rangle) = \cos^2(\pi/2) = 0$, $P(|1\rangle) = 1$. Rotasi $180^\circ$ di sumbu Y sepenuhnya membalikkan amplitudo. Ini adalah titik sensitivitas maksimum terhadap perubahan _bitstring_ hasil.
    
- **Kasus Ekstrem 3 ($\theta_y = \pi/2$):** $P(|0\rangle) = 0.5$, $P(|1\rangle) = 0.5$. Rotasi $90^\circ$ menciptakan superposisi seimbang yang sempurna.
    

**Sensitivitas terhadap $\theta_z$ (Fase):**

Perhatikan bahwa parameter rotasi sumbu Z ($\theta_z$) **tidak muncul sama sekali** dalam persamaan probabilitas akhir $P(|0\rangle)$ atau $P(|1\rangle)$.

- Jika Anda merotasi $\theta_z$ secara ekstrem dari $0$ hingga $2\pi$, probabilitas pengukurannya pada perangkat keras _tetap 100% identik_.
    
- **Lalu mengapa $\theta_z$ penting?** Fase rotasi $\theta_z$ menyimpan "informasi tersembunyi" (fase kompleks) yang baru akan berguna saat qubit ini diikat (_entangled_) dengan qubit lain menggunakan gerbang CNOT, atau saat diukur dalam basis non-diagonal (seperti rotasi $\hat{X}$ atau $\hat{Y}$). Dalam ranah ansazt Ising diagonal yang kita gunakan (karena masalah portofolio ini tidak memiliki suku non-komutatif), fase $\theta_z$ praktis **tidak berkontribusi apa pun terhadap energi objektif**. Ini adalah salah satu temuan penting: ansazt _EfficientSU2_ dengan $R_z$ sering kali terlalu over-parameterized untuk _Quadratic Unconstrained Binary Optimization_ (QUBO).
    

### 3. Ekstensi ke N Qubit

Saat kita memperluas sistem dari 1 qubit ke banyak qubit (Sistem $N$), kita menggunakan operasi perkalian tensor ($\otimes$). Matriks rotasi tunggal berukuran $2 \times 2$ menjadi matriks rotasi komposit berukuran $2^N \times 2^N$.

Misalnya, untuk 2 qubit ($N=2$) pada lapisan pertama ($l=0$):

$$U_{rot}^{(0)}(\boldsymbol{\theta}_0) = U_{1q}(\theta_{0,0,y}, \theta_{0,0,z}) \otimes U_{1q}(\theta_{0,1,y}, \theta_{0,1,z})$$

Perkalian tensor dua matriks $2 \times 2$ akan menghasilkan satu buah matriks diagonal blok raksasa berukuran $4 \times 4$ yang setiap elemen pembantunya diisi oleh fungsi $\sin(\theta)$ dan $\cos(\theta)$ yang sangat panjang. Inilah esensi analitis dari mengapa optimasi multi-parameter secara simultan (SPSA) seringkali lebih disukai daripada penurunan satu per satu (Gradient Descent) dalam skenario ini.

Apakah visual ini membantu Anda memahami jawaban dengan lebih baik?

YaTidak


$\vec{R}$