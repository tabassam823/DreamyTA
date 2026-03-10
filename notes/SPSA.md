# Simultaneous Perturbation Stochastic Approximation (SPSA)

Dokumen ini menjelaskan mekanisme optimasi SPSA yang dikembangkan oleh James C. Spall sebagai alternatif efisien bagi *Gradient Descent* dalam lingkungan yang berisik (*noisy*).

## 1. Urgensi Eksplorasi: Masalah Skalabilitas Gradien
Dalam optimasi VQE dengan $p$ parameter, metode *Finite Difference* membutuhkan $2p$ pengukuran untuk satu langkah gradien. Jika kita punya 100 parameter, kita butuh 200 kali tembakan ke QPU hanya untuk satu iterasi. **SPSA** memecahkan masalah ini dengan hanya membutuhkan **2 pengukuran** per iterasi, berapa pun jumlah parameternya.

---

## 2. Aksioma & Intuisi: Optimasi dalam Kegelapan
SPSA didasarkan pada dua kenyataan pahit dalam komputasi kuantum NISQ:
1.  **Noise:** Kita tidak pernah mendapatkan nilai energi murni $L(\theta)$, melainkan nilai yang terdistorsi oleh noise $y(\theta)$.
2.  **Dimensi Tinggi:** Menghitung turunan satu per satu untuk setiap parameter terlalu mahal.

**Jembatan Logika:** SPSA melakukan "perturbasi simultan", yaitu mengguncang seluruh parameter sekaligus ke arah acak, lalu melihat apakah energi total naik atau turun.

---

## 3. Derivasi Matematis: Model James C. Spall

### A. Model Pengukuran Berisik
Misalkan kita ingin meminimalkan fungsi kerugian (loss) $L(\theta)$. Namun, hardware hanya memberikan hasil observasi $y(\theta)$:
$$ y(\theta) = L(\theta) + \text{noise} \qquad (1) $$
Tujuan kita adalah mencari $\theta^*$ sedemikian sehingga gradien aslinya nol:
$$ g(\theta^*) = \left. \frac{\partial L(\theta)}{\partial \theta} \right|_{\theta=\theta^*} = 0 \qquad (2) $$

### B. Estimasi Gradien Simultan
SPSA tidak menghitung turunan per komponen $\frac{\partial L}{\partial \theta_i}$. Sebaliknya, SPSA mengestimasi seluruh vektor gradien $\hat{g}_k(\theta_k)$ menggunakan dua pengukuran:
$$ y_k^{(+)} = y(\theta_k + c_k \Delta_k) \quad \text{dan} \quad y_k^{(-)} = y(\theta_k - c_k \Delta_k) \qquad (3) $$
Di mana $\Delta_k$ adalah vektor perturbasi acak.

### C. Komponen Gradien SPSA
Komponen ke-$i$ dari estimasi gradien pada iterasi ke-$k$ diberikan oleh:
$$ \hat{g}_{ki}(\theta_k) = \frac{y_k^{(+)} - y_k^{(-)}}{2 c_k \Delta_{ki}} \qquad (4) $$

> **Visualisasi (4): Perhitungan Linear (Estimasi Gradien)**
> Bayangkan kita punya 2 parameter $(\theta_1, \theta_2)$ dan vektor acak $\Delta = (+1, -1)$.
> $$ \hat{g}_{k} = \frac{y^{(+)} - y^{(-)}}{2 c_k} \begin{pmatrix} 1/\Delta_1 \\ 1/\Delta_2 \end{pmatrix} = \frac{\Delta y}{2 c_k} \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$
> Perhatikan bahwa pembilang $(y^{(+)} - y^{(-)})$ sama untuk semua parameter. Inilah rahasia efisiensi SPSA!

---

## 4. Jembatan Logika: Mengapa SPSA Valid?
Secara statistik, Spall membuktikan bahwa jika vektor $\Delta_k$ dipilih dari distribusi Bernoulli ($\pm 1$ dengan probabilitas 0.5), maka nilai ekspektasi dari estimasi gradien SPSA akan mendekati gradien asli:
$$ E[\hat{g}_k(\theta_k) | \theta_k] \approx \nabla L(\theta_k) \qquad (5) $$
Noise pada persamaan (1) akan saling meniadakan seiring bertambahnya iterasi (hukum bilangan besar).

---

## 5. Algoritma Update & Makna Fisis Parameter
Update parameter dilakukan dengan rumus:
$$ \theta_{k+1} = \theta_k - a_k \hat{g}_k(\theta_k) \qquad (6) $$

Ada 5 parameter krusial dalam SPSA yang mengatur "perilaku belajar" sistem:

| Parameter | Nama Fisik | Makna dan Fungsi |
| :--- | :--- | :--- |
| **$a_k$** | *Learning Rate* | Menentukan seberapa jauh kita melangkah. Harus mengecil ($a_k = a/(k+1+A)^\alpha$) agar konvergen. |
| **$c_k$** | *Perturbation Size* | Menentukan seberapa keras kita "mengguncang" sistem ($c_k = c/(k+1)^\gamma$). |
| **$A$** | *Stability Constant* | "Rem" pada awal iterasi agar langkah tidak terlalu liar saat data masih sangat berisik. |
| **$\alpha, \gamma$** | *Decay Exponents* | Mengatur kecepatan pengecilan langkah. Standar Spall: $\alpha = 0.602, \gamma = 0.101$. |

---

## 6. Verifikasi & Parameter: SPSA vs Gradient Descent
| Kondisi | Gradient Descent | SPSA |
| :--- | :--- | :--- |
| **Jumlah Pengukuran** | $2 \times p$ per iterasi. | **Selalu 2 per iterasi.** |
| **Ketahanan Noise** | Rendah (butuh nilai presisi). | **Tinggi (noise dianggap bagian dari statistik).** |
| **Konvergensi** | Cepat di ruang mulus. | Lebih lambat, tapi sangat tangguh di ruang kasar/berisik. |

---

## 7. Analogi "Physical Insight": Berjalan di Tengah Badai
Bayangkan Anda ingin mencari dasar lembah (minimum energi) saat terjadi badai besar (*noise*).
- **Gradient Descent** adalah seperti mencoba menggunakan laser untuk mengukur kemiringan tanah. Badai membuat laser Anda bergetar dan tidak berguna.
- **SPSA** adalah seperti Anda melempar dua batu ke arah acak, satu ke depan-kanan-atas, satu ke belakang-kiri-bawah. Anda hanya mendengarkan suara jatuhnya batu. Jika suara batu pertama terdengar lebih "rendah" dari batu kedua, Anda melompat ke arah itu. Meskipun satu lompatan mungkin salah karena tiupan angin, setelah 100 kali lompatan, Anda pasti sampai di dasar lembah.

---

## 8. Kesimpulan
SPSA adalah algoritma **pencari jalan stokastik**. Dengan mengorbankan ketepatan langkah individual, SPSA mendapatkan efisiensi luar biasa dalam dimensi tinggi. Dalam VQE portofolio, SPSA memungkinkan kita mengoptimalkan ratusan parameter aset tanpa harus menguras kuota *runtime* hardware kuantum.
