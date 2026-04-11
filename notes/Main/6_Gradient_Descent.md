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
