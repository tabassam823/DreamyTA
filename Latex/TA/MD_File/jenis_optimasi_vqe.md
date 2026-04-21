# Gradient Descent

Gradient Descent (Penurunan Gradien) adalah algoritma optimasi orde pertama yang paling mendasar. Dalam konteks VQE, ia digunakan untuk menemukan parameter ansatz $\theta$ yang meminimalkan nilai ekspektasi energi.

### 1. Konsep Dasar
Ide utamanya adalah mengambil langkah iteratif ke arah yang berlawanan dengan gradien fungsi biaya (energi) pada titik saat ini. Karena gradien menunjukkan arah peningkatan tercepat, maka arah negatifnya adalah arah penurunan tercepat.

### 2. Detail Matematis
Misalkan kita memiliki fungsi energi $E(\theta)$ yang didefinisikan sebagai:
$$E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle$$

**Langkah-langkah Penurunan Rumus:**
1.  **Ekspansi Taylor**: Di sekitar titik $\theta_t$, fungsi $E(\theta)$ dapat didekati dengan:
    $$E(\theta) \approx E(\theta_t) + \nabla E(\theta_t)^T (\theta - \theta_t)$$
2.  **Arah Penurunan**: Kita ingin memilih perubahan $\Delta \theta = \theta - \theta_t$ sedemikian rupa sehingga $E(\theta) < E(\theta_t)$. Nilai terkecil tercapai jika $\Delta \theta$ sejajar namun berlawanan arah dengan gradien $\nabla E(\theta_t)$.
3.  **Aturan Update**:
    $$\theta_{t+1} = \theta_t - \eta \nabla E(\theta_t)$$
    Di mana $\eta$ (eta) adalah *learning rate* atau ukuran langkah.

**Penghitungan Gradien di VQE:**
Pada hardware kuantum, gradien $\nabla E(\theta)$ dihitung menggunakan **[[Parameter_Shift_Rule]]**:
$$\frac{\partial E}{\partial \theta_j} = \frac{E(\theta + \frac{\pi}{2}e_j) - E(\theta - \frac{\pi}{2}e_j)}{2}$$

### 3. Cara Penggunaan (Qiskit)
Dalam Qiskit, Gradient Descent dapat digunakan melalui modul `qiskit_algorithms.optimizers`.

```python
from qiskit_algorithms.optimizers import GradientDescent

# Inisialisasi optimizer dengan learning rate 0.05
optimizer = GradientDescent(maxiter=100, learning_rate=0.05)

# Digunakan dalam VQE
# vqe = VQE(estimator, ansatz, optimizer)
```

### 4. Karakteristik
*   **Kelebihan**: Stabil dan konvergen menuju local minimum pada fungsi konveks.
*   **Kekurangan**: Sensitif terhadap pemilihan *learning rate* $\eta$. Jika terlalu besar, bisa melewati minimum; jika terlalu kecil, konvergensi sangat lambat. Selain itu, mudah terjebak di *local minima* atau *saddle points*.

---
# Adam Gradient

**ADAM (Adaptive Moment Estimation)** adalah algoritma optimasi yang menggabungkan konsep *Momentum* dan *RMSProp*. Ini adalah salah satu optimizer paling populer dalam machine learning dan VQE karena kemampuannya menangani gradien yang berisik (*noisy gradients*).

### 1. Konsep Dasar
Adam menyesuaikan *learning rate* untuk setiap parameter secara individu. Ia menyimpan estimasi rata-rata bergerak (*moving average*) dari gradien (momen pertama) dan kuadrat gradien (momen kedua).

### 2. Detail Matematis
Misalkan $g_t = \nabla E(\theta_t)$ adalah gradien pada langkah $t$.

**Langkah-langkah Penurunan:**
1.  **Update Momen Pertama (Mean)**:
    $$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$
    (Mengumpulkan momentum dari langkah sebelumnya).
2.  **Update Momen Kedua (Uncentered Variance)**:
    $$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$
    (Menyesuaikan langkah berdasarkan besarnya variansi gradien).
3.  **Koreksi Bias**: Karena $m_t$ dan $v_t$ diinisialisasi dengan nol, mereka cenderung bias ke arah nol pada langkah awal. Maka dilakukan koreksi:
    $$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
4.  **Aturan Update**:
    $$\theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$
    Di mana:
    *   $\beta_1, \beta_2$: Faktor peluruhan (default: 0.9 dan 0.999).
    *   $\epsilon$: Konstanta kecil untuk menghindari pembagian dengan nol ($10^{-8}$).

### 3. Cara Penggunaan (Qiskit)
```python
from qiskit_algorithms.optimizers import ADAM

# Konfigurasi standar
optimizer = ADAM(maxiter=100, lr=0.001, beta1=0.9, beta2=0.999)
```

### 4. Keunggulan untuk VQE
Dalam VQE yang dijalankan pada simulator dengan *shot noise* atau hardware asli, nilai energi yang dihasilkan memiliki fluktuasi statistik. Adam sangat efektif di sini karena:
*   **Adaptif**: Tidak perlu mencari satu *learning rate* yang sempurna untuk semua parameter.
*   **Robust terhadap Noise**: Momen kedua ($v_t$) membantu meredam fluktuasi gradien yang disebabkan oleh noise pengukuran.

---
# SPSA

**SPSA (Simultaneous Perturbation Stochastic Approximation)** adalah algoritma optimasi yang sangat efisien untuk sistem dengan banyak parameter dan noise yang tinggi. Ini adalah optimizer standar yang direkomendasikan IBM untuk hardware kuantum asli.

### 1. Konsep Dasar
Berbeda dengan Gradient Descent konvensional yang menghitung gradien satu per satu untuk setiap parameter (membutuhkan $2n$ evaluasi), SPSA mengestimasi gradien dengan menggeser **semua** parameter secara bersamaan ke arah acak. SPSA hanya membutuhkan **2 evaluasi** per langkah iterasi, berapapun jumlah parameternya.

### 2. Detail Matematis
**Langkah-langkah Estimasi Gradien:**
1.  **Vektor Acak ($\Delta_t$)**: Bangun vektor acak $\Delta_t$ (biasanya berdistribusi Bernoulli $\pm 1$) dengan dimensi yang sama dengan jumlah parameter.
2.  **Evaluasi Energi**: Hitung energi pada dua titik yang digeser:
    $$E_+ = E(\theta_t + c_t \Delta_t)$$
    $$E_- = E(\theta_t - c_t \Delta_t)$$
    Di mana $c_t$ adalah skala perturbasi yang mengecil seiring waktu.
3.  **Estimasi Gradien ($\hat{g}_t$)**:
    $$\hat{g}_t = \frac{E_+ - E_-}{2 c_t \Delta_t}$$
    (Setiap elemen gradien $j$ dihitung sebagai $\frac{E_+ - E_-}{2 c_t \Delta_{t,j}}$).
4.  **Aturan Update**:
    $$\theta_{t+1} = \theta_t - a_t \hat{g}_t$$
    Di mana $a_t$ adalah *learning rate* yang juga mengecil seiring iterasi.

**Skala Penurunan (Schedules):**
Agar konvergen, $a_t$ dan $c_t$ biasanya mengikuti rumus:
$$a_t = \frac{a}{(A + t + 1)^\alpha}, \quad c_t = \frac{c}{(t + 1)^\gamma}$$

### 3. Cara Penggunaan (Qiskit)
```python
from qiskit_algorithms.optimizers import SPSA

# SPSA secara otomatis menyesuaikan parameter a dan c jika tidak ditentukan
optimizer = SPSA(maxiter=100)
```

### 4. Mengapa SPSA sangat penting untuk VQE?
1.  **Sangat Cepat**: Jika anda memiliki 100 parameter, Gradient Descent butuh 200 sirkuit per iterasi, sedangkan SPSA tetap butuh **hanya 2**.
2.  **Noise Resilience**: Karena menggunakan perturbasi acak dan pendekatan stokastik, SPSA sangat tahan terhadap *shot noise* dan noise termal pada chip kuantum nyata.

---
# COBYLA

**COBYLA (Constrained Optimization By Linear Approximation)** adalah optimizer numerik yang tidak memerlukan informasi gradien (*derivative-free*). Ini adalah salah satu optimizer yang paling sering digunakan dalam VQE karena kesederhanaannya.

### 1. Konsep Dasar
COBYLA bekerja dengan membangun pendekatan linear (interpolasi) dari fungsi tujuan menggunakan sekumpulan titik dalam ruang parameter yang membentuk **Simplex** (misal: segitiga untuk 2D, tetrahedron untuk 3D).

### 2. Detail Matematis
**Langkah-langkah Utama:**
1.  **Inisialisasi Simplex**: Pilih $n+1$ titik di sekitar titik awal $\theta_0$.
2.  **Interpolasi Linear**: Di setiap langkah, COBYLA menghitung nilai fungsi pada titik-titik simplex dan membentuk model linear $L(\theta) \approx E(\theta)$.
3.  **Trust Region**: Algoritma mencari titik minimum dari model linear $L(\theta)$ di dalam sebuah "daerah kepercayaan" (*trust region*) berupa bola dengan radius $\rho$.
4.  **Update**: Jika titik baru memberikan hasil yang lebih baik, simplex diperbarui dan radius $\rho$ mungkin diperkecil untuk memperhalus pencarian (konvergensi).

Karena tidak menggunakan gradien, COBYLA tidak memerlukan *Parameter Shift Rule*, yang berarti ia melakukan evaluasi energi secara langsung pada titik-titik parameter.

### 3. Cara Penggunaan (Qiskit)
```python
from qiskit_algorithms.optimizers import COBYLA

# COBYLA sangat populer karena hanya membutuhkan sedikit parameter tuning
optimizer = COBYLA(maxiter=100, rhobeg=1.0)
```

### 4. Karakteristik
*   **Kelebihan**: Sangat tangguh jika fungsi tujuan tidak memiliki turunan yang jelas atau sangat berisik. Tidak memerlukan $2n$ evaluasi untuk gradien.
*   **Kekurangan**: Konvergensi bisa sangat lambat untuk jumlah parameter yang besar ($n > 20$) dibandingkan dengan metode berbasis gradien.

---
# SLSQP

**SLSQP (Sequential Least SQuares Programming)** adalah algoritma optimasi berbasis gradien yang sangat efisien untuk masalah optimasi dengan kendala (*constrained optimization*).

### 1. Konsep Dasar
SLSQP menggunakan teknik *Successive Quadratic Programming* (SQP). Di setiap langkah, algoritma ini mencoba mendekati fungsi tujuan dengan fungsi kuadrat dan kendala-kendalanya dengan fungsi linear.

### 2. Detail Matematis
**Langkah-langkah Penurunan:**
1.  **Pendekatan Kuadratik**: Fungsi energi $E(\theta)$ didekati menggunakan ekspansi Taylor orde kedua (melibatkan gradien dan perkiraan Hessian $H$):
    $E(\theta_t + d) \approx E(\theta_t) + \nabla E(\theta_t)^T d + \frac{1}{2} d^T H_t d$
2.  **Subproblem QP**: Algoritma menyelesaikan masalah *Quadratic Programming* (QP) untuk menemukan arah langkah $d$ yang meminimalkan pendekatan kuadratik tersebut.
3.  **Line Search**: Setelah arah $d$ ditemukan, SLSQP melakukan pencarian garis (*line search*) untuk menentukan ukuran langkah $\alpha$ yang optimal:
    $\theta_{t+1} = \theta_t + \alpha d$

### 3. Cara Penggunaan (Qiskit)
```python
from qiskit_algorithms.optimizers import SLSQP

optimizer = SLSQP(maxiter=100)
```

### 4. Karakteristik
*   **Kelebihan**: Sangat cepat konvergen untuk fungsi yang mulus. Mendukung batasan parameter (misal: $\theta \in [0, 2\pi]$) secara efisien.
*   **Kekurangan**: Memerlukan estimasi gradien yang akurat. Jika gradien sangat berisik (seperti pada hardware kuantum tanpa error mitigation), SLSQP mungkin gagal menemukan titik minimum yang presisi.

---
# Nelder-Mead

**Nelder-Mead** (juga dikenal sebagai *Amoeba Method*) adalah optimizer *derivative-free* yang bekerja dengan cara memanipulasi bentuk geometris (Simplex) di ruang parameter.

### 1. Konsep Dasar
Algoritma ini tidak menghitung gradien. Sebaliknya, ia "merayap" di sepanjang permukaan energi dengan memantulkan, mengembangkan, atau menyusutkan simplex berdasarkan nilai fungsi di titik-titik sudutnya.

### 2. Detail Matematis
Misalkan kita memiliki $n$ parameter, maka simplex memiliki $n+1$ titik sudut $\{x_1, x_2, \dots, x_{n+1}\}$. Titik-titik ini diurutkan berdasarkan nilai energinya: $E(x_1) \leq E(x_2) \leq \dots \leq E(x_{n+1})$.

**Operasi Utama:**
1.  **Reflection (Refleksi)**: Mencoba memantulkan titik terburuk ($x_{n+1}$) melalui pusat massa titik lainnya. Jika hasilnya lebih baik, ganti titik terburuk dengan titik refleksi.
2.  **Expansion (Ekspansi)**: Jika refleksi sangat bagus, coba melangkah lebih jauh ke arah tersebut.
3.  **Contraction (Kontraksi)**: Jika refleksi tidak memberikan perbaikan, coba langkah yang lebih pendek di dalam atau di luar simplex.
4.  **Shrinkage (Penyusutan)**: Jika semua langkah di atas gagal, perkecil seluruh simplex ke arah titik terbaik ($x_1$).

### 3. Cara Penggunaan (Qiskit)
```python
from qiskit_algorithms.optimizers import NelderMead

optimizer = NelderMead(maxiter=100)
```

### 4. Karakteristik
*   **Kelebihan**: Sangat sederhana dan tidak memerlukan asumsi tentang kelancaran (*smoothness*) fungsi. Bagus untuk landscape energi yang sangat kasar.
*   **Kekurangan**: Bisa terjebak di local minima dengan sangat mudah dan skalabilitasnya buruk untuk jumlah parameter yang besar ($n > 10$). Seringkali lebih lambat dibandingkan COBYLA untuk masalah VQE.