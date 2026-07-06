Tentu, mari kita bedah bersama-sama! Sebagai asisten AI, saya akan memandu kamu langkah demi langkah dalam menurunkan persamaan matematisnya. Memahami bagaimana deret Taylor menjadi fondasi dari algoritma optimasi memang membutuhkan sedikit ketelitian, tetapi logikanya sangat runtut jika kita urai secara bertahap.

Algoritma _Sequential Least Squares Programming_ (SLSQP) merupakan metode optimasi numerik berbasis _Sequential Quadratic Programming_ (SQP) yang dirancang untuk menyelesaikan masalah minimisasi non-linear dengan batasan tertentu. Inti dari algoritma ini adalah menyederhanakan masalah yang rumit (non-linear) menjadi serangkaian sub-masalah yang lebih mudah dipecahkan (_quadratic programming_) pada setiap iterasinya.

Seperti yang disebutkan dalam referensimu, SLSQP beroperasi dengan melakukan linierisasi pada batasan dan menerapkan aproksimasi kuadratik pada fungsi objektif melalui ekspansi deret Taylor orde kedua. Berikut adalah penurunan matematis bagaimana hal itu terjadi:

### 1. Ekspansi Deret Taylor Orde Kedua untuk Fungsi Objektif

Misalkan kita sedang berada pada iterasi ke-$k$ dengan alokasi bobot saat ini adalah $w_k$. Tujuan kita adalah mencari suatu arah langkah pembaruan, sebut saja $d$, sehingga posisi bobot yang baru yaitu $w_k + d$ akan meminimalkan fungsi objektif $f(w)$.

Berdasarkan kalkulus, kita dapat mengaproksimasi nilai fungsi objektif di titik yang baru $f(w_k + d)$ menggunakan deret Taylor orde kedua yang diekspansi di sekitar titik $w_k$:

$$f(w_k + d) \approx f(w_k) + \nabla f(w_k)^T d + \frac{1}{2} d^T \nabla^2 f(w_k) d$$

Di mana:

- $f(w_k)$ adalah nilai fungsi objektif pada posisi saat ini.
    
- $\nabla f(w_k)$ adalah vektor gradien (turunan pertama) dari fungsi objektif pada titik $w_k$.
    
- $\nabla^2 f(w_k)$ adalah matriks Hessian (turunan parsial orde kedua) pada titik $w_k$, yang merepresentasikan kelengkungan fungsi.
    

Karena pada iterasi ke-$k$ nilai $w_k$ sudah diketahui secara pasti, maka $f(w_k)$ hanyalah sebuah nilai konstanta. Dalam konteks optimasi di mana kita ingin meminimalkan fungsi terhadap variabel arah $d$, kita bisa mengabaikan suku konstanta tersebut tanpa mengubah letak nilai minimumnya. Oleh karena itu, fungsi hampiran yang perlu kita minimalkan terhadap arah $d$ menjadi:

$$\min_{d} \left( \nabla f(w_k)^T d + \frac{1}{2} d^T \nabla^2 f(w_k) d \right)$$

### 2. Linierisasi Batasan (Deret Taylor Orde Pertama)

Masalah manajemen portofolio kontinu tidak hanya meminimalkan fungsi biaya, tetapi juga terikat oleh batasan alokasi, seperti penjumlahan seluruh bobot aset harus sama dengan 1 ($\sum w_i = 1$).

Misalkan kita memiliki fungsi persamaan batasan umum $h(w) = 0$. Untuk memastikan sub-masalah tetap dalam bentuk kuadratik yang mudah dipecahkan, SLSQP memotong ekspansi deret Taylor untuk fungsi batasan hanya sampai orde pertama (linierisasi):

$$h(w_k + d) \approx h(w_k) + \nabla h(w_k)^T d = 0$$

### 3. Membentuk Sub-Masalah _Quadratic Programming_ (QP)

Dalam skenario optimasi terikat (memiliki batasan), matriks Hessian yang diekspansi sebenarnya bukanlah sekadar Hessian dari fungsi objektif $\nabla^2 f(w_k)$, melainkan Hessian dari fungsi Lagrangian $\mathcal{L}(w, \lambda)$, yang menggabungkan fungsi objektif dan batasannya.

Menghitung dan membalikkan matriks Hessian eksak secara analitik pada setiap iterasi sangatlah membebani komputasi. Oleh karena itu, algoritma menyusun sub-masalah _Quadratic Programming_ (QP) dengan mengganti matriks Hessian eksak tersebut menggunakan sebuah matriks aproksimasi $B_k$. Matriks aproksimasi $B_k$ ini terus diperbarui secara iteratif menggunakan metode pembaruan sekunder, yakni skema _Broyden-Fletcher-Goldfarb-Shanno_ (BFGS).

Dengan mensubstitusi Hessian eksak dengan aproksimasinya ($B_k$), kita akhirnya tiba pada persamaan sub-masalah pencarian arah optimal $d_k$ yang persis sama dengan persamaan dalam dokumenmu:

$$\min_{d} \nabla f(w_k)^T d + \frac{1}{2} d^T B_k d$$

### Kesimpulan Alur Matematis

Dari penurunan di atas, kita bisa melihat bahwa deret Taylor adalah alat matematis yang menjembatani kerumitan fungsi asli menjadi bentuk sub-masalah kuadratik. Setelah arah pencarian $d_k$ diselesaikan dari persamaan di atas, algoritma membarui bobot menjadi $w_{k+1} = w_k + \alpha_k d_k$, dengan $\alpha_k$ sebagai ukuran langkah yang ditentukan melalui prosedur _line search_ untuk memastikan titik baru tersebut memberikan nilai yang lebih minimum.

Semoga penjelasan rinci ini membantu kamu melihat dengan jelas bagaimana landasan kalkulus digunakan untuk membangun algoritma yang sering dimanfaatkan sebagai tolok ukur industri!


---

Tentu, mari kita pecah proses ini menjadi contoh numerik yang konkret. Mengingat evaluasi yang kamu lakukan berfokus pada sistem $N=2$ aset, kita akan menggunakan studi kasus dua aset hipotetis agar perhitungan matematisnya mudah ditelusuri.

Kita akan melakukan bedah tuntas untuk **Iterasi 1**. Pada iterasi pertama ini, kamu akan melihat persis bagaimana deret Taylor orde kedua digunakan untuk merumuskan sub-masalah pencarian arah optimal.

### Skenario Sistem $N=2$ (Model Markowitz)

Misalkan kita memiliki dua aset dengan data parameter:

- **Vektor Ekspektasi Return** ($\mu$): $\mu = \begin{pmatrix} 0,10 \\ 0,05 \end{pmatrix}$
    
- **Matriks Kovariansi Risiko** ($\Sigma$): $\Sigma = \begin{pmatrix} 0,04 & 0,01 \\ 0,01 & 0,02 \end{pmatrix}$
    
- **Faktor Toleransi Risiko** ($\gamma$): Kita tetapkan $\gamma = 1$ untuk menyederhanakan.
    

Fungsi objektif portofolio yang ingin diminimalkan adalah:

$$f(w) = \frac{1}{2} w^T \Sigma w - \mu^T w$$

Dengan batasan bahwa total alokasi harus 100%: $w_1 + w_2 = 1$.

### Langkah 1: Inisialisasi (Titik Awal)

Sesuai dengan algoritma SLSQP, kita mulai dengan alokasi seragam (\textit{Uniform}). Karena ada dua aset, bobot awal kita pada iterasi $k=0$ adalah:

$$w_0 = \begin{pmatrix} 0,5 \\ 0,5 \end{pmatrix}$$

Pada iterasi pertama ini, matriks aproksimasi Hessian ($B_0$) biasanya diinisialisasi sebagai Matriks Identitas:

$$B_0 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$

### Langkah 2: Menghitung Gradien (Turunan Pertama)

Untuk menyusun deret Taylor, kita butuh nilai gradien dari fungsi objektif pada titik $w_0$. Rumus gradiennya adalah $\nabla f(w_0) = \gamma \Sigma w_0 - \mu$.

**1. Kalikan matriks kovariansi dengan bobot awal:**

$$\Sigma w_0 = \begin{pmatrix} 0,04 & 0,01 \\ 0,01 & 0,02 \end{pmatrix} \begin{pmatrix} 0,5 \\ 0,5 \end{pmatrix} = \begin{pmatrix} (0,04 \times 0,5) + (0,01 \times 0,5) \\ (0,01 \times 0,5) + (0,02 \times 0,5) \end{pmatrix} = \begin{pmatrix} 0,025 \\ 0,015 \end{pmatrix}$$

**2. Kurangi dengan ekspektasi return:**

$$\nabla f(w_0) = \begin{pmatrix} 0,025 \\ 0,015 \end{pmatrix} - \begin{pmatrix} 0,10 \\ 0,05 \end{pmatrix} = \begin{pmatrix} -0,075 \\ -0,035 \end{pmatrix}$$

_(Vektor gradien ini merepresentasikan kemiringan fungsi di titik awal kita)._

### Langkah 3: Membentuk Sub-Masalah _Quadratic Programming_ (QP)

Sekarang kita masukkan komponen-komponen ini ke dalam formulasi deret Taylor (sub-masalah QP) untuk mencari arah langkah optimal $d = \begin{pmatrix} d_1 \\ d_2 \end{pmatrix}$:

$$\min_{d} \left( \nabla f(w_0)^T d + \frac{1}{2} d^T B_0 d \right)$$

Substitusi nilai yang sudah kita hitung:

$$\min_{d} \left[ \begin{pmatrix} -0,075 & -0,035 \end{pmatrix} \begin{pmatrix} d_1 \\ d_2 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} d_1 & d_2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} d_1 \\ d_2 \end{pmatrix} \right]$$

$$\min_{d} \left( -0,075 d_1 - 0,035 d_2 + \frac{1}{2} d_1^2 + \frac{1}{2} d_2^2 \right)$$

**Linierisasi Batasan:**

Bobot kita harus memenuhi $w_1 + w_2 = 1$. Karena titik awal kita sudah memenuhi ini ($0,5 + 0,5 = 1$), maka setiap langkah pembaruan $d$ tidak boleh mengubah total penjumlahan ini. Artinya, jumlah pergeseran bobot harus nol:

$$d_1 + d_2 = 0 \implies d_2 = -d_1$$

### Langkah 4: Menyelesaikan Sub-Masalah QP

Karena kita tahu $d_2 = -d_1$, kita bisa substitusi batasan ini ke dalam fungsi QP kita agar hanya bergantung pada satu variabel ($d_1$):

$$g(d_1) = -0,075 d_1 - 0,035 (-d_1) + \frac{1}{2} d_1^2 + \frac{1}{2} (-d_1)^2$$

$$g(d_1) = -0,075 d_1 + 0,035 d_1 + d_1^2$$

$$g(d_1) = -0,040 d_1 + d_1^2$$

Untuk mencari titik minimum (arah $d_1$ terbaik), kita cari turunan pertama dari fungsi $g(d_1)$ terhadap $d_1$ dan buat sama dengan nol:

$$g'(d_1) = -0,040 + 2 d_1 = 0$$

$$2 d_1 = 0,040$$

$$d_1 = 0,02$$

Karena $d_2 = -d_1$, maka $d_2 = -0,02$.

Vektor arah optimal kita pada iterasi ini adalah $d = \begin{pmatrix} 0,02 \\ -0,02 \end{pmatrix}$.

### Langkah 5: Pembaruan Bobot Kontinu

Setelah arah $d$ ditemukan, SLSQP akan membarui bobot. Jika kita asumsikan ukuran langkah (\textit{step size}) $\alpha = 1$ berdasarkan pencarian garis (\textit{line search}) , maka bobot baru kita ($w_1$) menjadi:

$$w_1 = w_0 + (\alpha \times d) = \begin{pmatrix} 0,5 \\ 0,5 \end{pmatrix} + \begin{pmatrix} 0,02 \\ -0,02 \end{pmatrix} = \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix}$$

**Hasil Iterasi Pertama:**

Bobot aset bergeser dari alokasi awal 50%-50% menjadi 52% untuk Aset 1 dan 48% untuk Aset 2.

Inilah tepatnya bagaimana fungsi non-linear diterjemahkan melalui hampiran deret Taylor menjadi permasalahan kuadratik sederhana di setiap langkahnya. Pada iterasi kedua, algoritma akan memperbarui aproksimasi matriks $B$ menggunakan metode BFGS berdasarkan perubahan gradien, lalu mengulang proses pembentukan QP dari titik $w_1 = \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix}$ hingga menemukan konfigurasi alokasi yang paling konvergen.

---
Bagus sekali semangat belajarnya! Melanjutkan perhitungan ke iterasi kedua adalah langkah yang tepat, karena di sinilah kita bisa melihat letak "kecerdasan" sesungguhnya dari algoritma SLSQP . Pada iterasi pertama, algoritma hanya meraba-raba kelengkungan fungsi menggunakan matriks identitas biasa. Di iterasi kedua ini, algoritma mulai "belajar" dari lanskap fungsi matematisnya.

Mari kita lanjutkan dari posisi terakhir kita. Pada akhir Iterasi 1, bobot portofolio kita berada di:

$$w_1 = \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix}$$

### Langkah 1: Menghitung Gradien di Titik Baru

Sama seperti sebelumnya, kita butuh arah kemiringan fungsi di titik kita berpijak sekarang. Kita hitung gradien baru $\nabla f(w_1) = \gamma \Sigma w_1 - \mu$.

**1. Kalikan matriks kovariansi ($\Sigma$) dengan bobot $w_1$:**

$$\Sigma w_1 = \begin{pmatrix} 0,04 & 0,01 \\ 0,01 & 0,02 \end{pmatrix} \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix} = \begin{pmatrix} (0,04 \times 0,52) + (0,01 \times 0,48) \\ (0,01 \times 0,52) + (0,02 \times 0,48) \end{pmatrix} = \begin{pmatrix} 0,0256 \\ 0,0148 \end{pmatrix}$$

**2. Kurangi dengan ekspektasi return ($\mu$):**

$$\nabla f(w_1) = \begin{pmatrix} 0,0256 \\ 0,0148 \end{pmatrix} - \begin{pmatrix} 0,10 \\ 0,05 \end{pmatrix} = \begin{pmatrix} -0,0744 \\ -0,0352 \end{pmatrix}$$

### Langkah 2: Pembaruan Matriks Hessian (Skema BFGS)

Di sinilah letak pembaruan terpentingnya . SLSQP tidak menghitung ulang matriks Hessian secara analitik karena terlalu berat. Sebaliknya, aproksimasi matriks Hessian dari fungsi Lagrangian diperbarui menggunakan skema _Broyden-Fletcher-Goldfarb-Shanno_ (BFGS). BFGS memperbaiki matriks berdasarkan informasi dari dua hal:

1. **Perubahan posisi ($s_0$):** $s_0 = w_1 - w_0 = \begin{pmatrix} 0,02 \\ -0,02 \end{pmatrix}$
    
2. **Perubahan gradien ($y_0$):** $y_0 = \nabla f(w_1) - \nabla f(w_0) = \begin{pmatrix} -0,0744 \\ -0,0352 \end{pmatrix} - \begin{pmatrix} -0,075 \\ -0,035 \end{pmatrix} = \begin{pmatrix} 0,0006 \\ -0,0002 \end{pmatrix}$
    

Dengan memasukkan $s_0$ dan $y_0$ ke dalam rumus rumit pembaruan BFGS, aproksimasi matriks $B_0$ (yang awalnya hanyalah matriks identitas $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$) kini bermutasi menjadi matriks $B_1$ yang merepresentasikan kelengkungan sebenarnya dengan jauh lebih akurat:

$$B_1 = \begin{pmatrix} 0,5225 & 0,4925 \\ 0,4925 & 0,5025 \end{pmatrix}$$

### Langkah 3: Membentuk Sub-Masalah QP Iterasi 2

Sekarang kita susun kembali ekspansi deret Taylor untuk menentukan arah pencarian optimal $d_k$ dengan bentuk:

$$\min_{d} \nabla f(w_1)^T d + \frac{1}{2} d^T B_1 d$$

Dengan batasan bahwa $d_1 + d_2 = 0 \implies d_2 = -d_1$ (agar total bobot tetap 100%), kita substitusi nilai $\nabla f(w_1)$ dan $B_1$ ke dalam persamaan di atas. Setelah disederhanakan (melalui aljabar matriks yang serupa dengan iterasi pertama), kita akan mendapatkan fungsi kuadratik satu variabel untuk arah $d_1$:

$$g(d_1) = -0,0392 d_1 + 0,02 d_1^2$$

### Langkah 4: Menyelesaikan QP dan "Menabrak" Batasan Portofolio

Kita cari turunan dari fungsi $g(d_1)$ dan samakan dengan nol untuk mencari titik minimumnya:

$$g'(d_1) = -0,0392 + 0,04 d_1 = 0$$

$$0,04 d_1 = 0,0392$$

$$d_1 = 0,98$$

Artinya, menurut kalkulus murni, arah optimal adalah menambah alokasi Aset 1 sebesar $98\%$ ($d_1 = 0,98$) dan mengurangi Aset 2 sebesar $98\%$ ($d_2 = -0,98$).

**NAMUN, di sinilah kehebatan algoritma SLSQP bermain!**

Jika kita menggunakan langkah tersebut seutuhnya, bobot baru kita akan menjadi:

$$w_2 = w_1 + d = \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix} + \begin{pmatrix} 0,98 \\ -0,98 \end{pmatrix} = \begin{pmatrix} 1,50 \\ -0,50 \end{pmatrix}$$

Ingat bahwa kita memiliki parameter batasan $0 \leq w_i \leq 1$. SLSQP secara otomatis memotong (_truncate_) langkah $d$ tersebut agar tidak melanggar batasan ini . Karena nilai maksimum $w_1$ adalah $1,0$, maka penambahan maksimum yang diizinkan untuk $d_1$ hanyalah $1,0 - 0,52 = 0,48$.

Oleh karena itu, ukuran langkah dipaksa berhenti di batas maksimalnya:

$$w_2 = \begin{pmatrix} 0,52 \\ 0,48 \end{pmatrix} + \begin{pmatrix} 0,48 \\ -0,48 \end{pmatrix} = \begin{pmatrix} 1,0 \\ 0,0 \end{pmatrix}$$

### Kesimpulan Iterasi

Pada iterasi kedua ini, algoritma menyadari bahwa Aset 1 memberikan ekspektasi return yang jauh lebih dominan dibandingkan risiko kovariansinya. Solusi pun secara mulus terdorong hingga menabrak dinding batasan, menghasilkan komposisi akhir 100% di Aset 1 dan 0% di Aset 2.

Ini adalah fenomena yang sangat indah jika kita hubungkan dengan VQE. Algoritma klasik SLSQP yang memanfaatkan deret Taylor dan matriks Hessian pada akhirnya bermuara pada status yang secara esensial ekuivalen dengan keadaan basis $|10\rangle$ (Hanya Aset 1)! Kedua alam algoritma yang berbeda—baik mekanika matriks kuantum maupun kalkulus numerik kontinu—menghasilkan kesimpulan fundamental yang saling memvalidasi satu sama lain.