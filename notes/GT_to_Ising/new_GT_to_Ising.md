# Derivasi Formal: Transformasi Matriks Game Theory ke Parameter Ising via Quantum Information

Dokumen ini menyajikan metodologi rujukan untuk mentransformasikan interaksi strategis dalam matriks permainan $4 \times 4$ ke dalam formalisme model *Ising*. Pendekatan ini merupakan *upgrade* struktural terhadap model Markowitz konvensional dengan mengintegrasikan *Quantum Mutual Information* (QMI) sebagai pengukur korelasi non-linear. Melalui derivasi ini, risiko portofolio tidak lagi dipandang sebagai statistik kovarians sederhana, melainkan sebagai manifestasi dari dinamika informasi dan keseimbangan strategis antar aset.

## 1. Pemetaan Isomorfik Strategi ke Ruang Konfigurasi Spin
Pemetaan isomorfik ini merupakan jembatan matematis yang menghubungkan domain *Game Theory* diskrit dengan ruang Hilbert dalam mekanika kuantum. Mengingat setiap pemain memiliki empat pilihan strategi, penggunaan dua *spin* biner ($\sigma \in \{-1, +1\}$) per pemain adalah syarat minimal untuk merepresentasikan seluruh ruang kemungkinan secara lengkap melalui aturan $2^n$ di mana $n=2$. Transformasi ini memastikan bahwa setiap keputusan strategis memiliki representasi *spin-encoded* yang unik, yang kemudian memungkinkan kita untuk menyusun operator Hamiltonian $\hat{H}$ yang bertindak atas *basis states* tersebut. Tanpa pemetaan yang presisi ini, interaksi strategis antar aset tidak dapat diterjemahkan ke dalam parameter fisik model *Ising* maupun diolah melalui sirkuit kuantum.

Representasi dalam bentuk tabel di bawah ini mengilustrasikan bagaimana 16 konfigurasi sistem mencakup seluruh dimensi matriks *payoff* $4 \times 4$. Setiap baris dalam tabel merepresentasikan satu "keadaan dunia" (*state of the world*) di mana pemain "Up" dan "Down" memilih kombinasi strategi tertentu secara simultan. Konfigurasi 4-spin ini membentuk *computational basis* yang memungkinkan algoritma optimasi kuantum untuk melakukan pencarian solusi melalui mekanisme superposisi dan intervensi interferensi. Dengan demikian, struktur energi sistem tidak hanya mencerminkan pengembalian aset secara terisolasi, melainkan juga seluruh dependensi kolektif yang tertanam dalam geometri ruang *spin* tersebut secara utuh.

| Strategi Up | $\sigma_1$ | $\sigma_2$ | Strategi Down | $\sigma_3$ | $\sigma_4$ | Konfigurasi $\boldsymbol\sigma$ |
| :---------: | :--------: | :--------: | :-----------: | :--------: | :--------: | :-----------------------------: |
|    **A**    |     -1     |     -1     |     **A**     |     -1     |     -1     |        (-1, -1, -1, -1)         |
|    **A**    |     -1     |     -1     |     **B**     |     -1     |     +1     |        (-1, -1, -1, +1)         |
|    **A**    |     -1     |     -1     |     **C**     |     +1     |     -1     |        (-1, -1, +1, -1)         |
|    **A**    |     -1     |     -1     |     **D**     |     +1     |     +1     |        (-1, -1, +1, +1)         |
|    **B**    |     -1     |     +1     |     **A**     |     -1     |     -1     |        (-1, +1, -1, -1)         |
|    **B**    |     -1     |     +1     |     **B**     |     -1     |     +1     |        (-1, +1, -1, +1)         |
|    **B**    |     -1     |     +1     |     **C**     |     +1     |     -1     |        (-1, +1, +1, -1)         |
|    **B**    |     -1     |     +1     |     **D**     |     +1     |     +1     |        (-1, +1, +1, +1)         |
|    **C**    |     +1     |     -1     |     **A**     |     -1     |     -1     |        (+1, -1, -1, -1)         |
|    **C**    |     +1     |     -1     |     **B**     |     -1     |     +1     |        (+1, -1, -1, +1)         |
|    **C**    |     +1     |     -1     |     **C**     |     +1     |     -1     |        (+1, -1, +1, -1)         |
|    **C**    |     +1     |     -1     |     **D**     |     +1     |     +1     |        (+1, -1, +1, +1)         |
|    **D**    |     +1     |     +1     |     **A**     |     -1     |     -1     |        (+1, +1, -1, -1)         |
|    **D**    |     +1     |     +1     |     **B**     |     -1     |     +1     |        (+1, +1, -1, +1)         |
| **D** | +1 | +1 | **C** | +1 | -1 | (+1, +1, +1, -1) |
| **D** | +1 | +1 | **D** | +1 | +1 | (+1, +1, +1, +1) |

Sebagai ilustrasi interpretatif, baris pertama merepresentasikan keadaan di mana kedua pemain secara simultan memilih strategi **A**, yang dalam representasi fisik setara dengan konfigurasi empat *spin* yang sejajar pada arah magnetisasi negatif $(-1, -1, -1, -1)$. Keadaan ini mencerminkan energi potensial yang dihasilkan dari sel $(A, A)$ pada matriks *payoff*, di mana utilitas sistem dihitung berdasarkan nilai probabilitas dan return pada titik tersebut. Sebaliknya, baris kedua menunjukkan pergeseran strategis di mana pemain "Down" beralih ke strategi **B**, mengakibatkan terjadinya *spin-flip* pada $\sigma_4$ menjadi $+1$. Perubahan konfigurasi ini mengubah simetri energi sistem, yang secara matematis menangkap dinamika respons pemain "Down" terhadap pilihan tetap pemain "Up" dalam ruang Hilbert.


## 2. Matriks Densitas Mixed State dan Global QMI
Dalam sistem keuangan yang dinamis, ketidakpastian informasi memaksa kita untuk memodelkan aset bukan sebagai *pure state*, melainkan sebagai *mixed state* yang direpresentasikan oleh matriks densitas $\rho_{AB}$. Matriks ini mengodekan seluruh distribusi probabilitas bersama $P(s_{\uparrow}, s_{\downarrow})$ dari tabel kontingensi ke dalam operator linear di ruang Hilbert 16-dimensi. Secara fisik, $\rho_{AB}$ mencerminkan ansambel statistik dari seluruh kemungkinan pasangan strategi yang dapat diambil oleh pemain "Up" dan "Down". Karena data yang digunakan bersifat klasik, matriks densitas gabungan ini berbentuk diagonal, di mana setiap elemen diagonalnya merepresentasikan probabilitas kemunculan konfigurasi *spin* tertentu.

Representasi matriks densitas gabungan $\rho_{AB}$ secara eksplisit didefinisikan sebagai matriks diagonal $16 \times 16$ sebagai berikut:

$$\rho_{AB} = \begin{pmatrix} 
P(A,A) & 0 & \cdots & 0 \\
0 & P(A,B) & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & P(D,D)
\end{pmatrix} \in \mathbb{C}^{16 \times 16} \quad (2)$$

Untuk menganalisis korelasi antar aset, kita perlu menurunkan matriks densitas tereduksi (*reduced density matrix*) melalui operasi *Partial Trace* terhadap subsistem lawan. Matriks $\rho_A$ merepresentasikan profil probabilitas marginal dari pemain "Up", sedangkan $\rho_B$ merepresentasikan profil marginal pemain "Down". Kedua matriks ini berbentuk diagonal $4 \times 4$ yang berisi probabilitas marginal $P(s_{\uparrow})$ dan $P(s_{\downarrow})$. Matriks-matriks ini menjadi basis bagi perhitungan *von Neumann Entropy* $S(\rho) = -\sum \lambda_i \ln \lambda_i$, yang selanjutnya digunakan untuk menguantifikasi *Quantum Mutual Information* (QMI) sebagai pengukur total dependensi informasional dalam sistem.

$$\rho_A = \text{Tr}_B(\rho_{AB}) = \begin{pmatrix} 
P(A) & 0 & 0 & 0 \\
0 & P(B) & 0 & 0 \\
0 & 0 & P(C) & 0 \\
0 & 0 & 0 & P(D)
\end{pmatrix}, \quad \rho_B = \text{Tr}_A(\rho_{AB}) = \begin{pmatrix} 
P(A) & 0 & 0 & 0 \\
0 & P(B) & 0 & 0 \\
0 & 0 & P(C) & 0 \\
0 & 0 & 0 & P(D)
\end{pmatrix} \quad (3)$$

## 3. Konstruksi Local Energy Landscape $\Phi(\boldsymbol\sigma)$
Kritik utama terhadap model sebelumnya adalah penggunaan nilai skalar global yang tidak terdefinisi per konfigurasi. Untuk memperbaikinya, kita mendefinisikan *energy landscape* $\Phi(\boldsymbol\sigma)$ secara eksplisit untuk setiap sel $(s_{\uparrow}, s_{\downarrow})$ yang berkorespondensi dengan konfigurasi $\boldsymbol\sigma$. Nilai energi per konfigurasi ini menggabungkan utilitas individu dan interaksi informasional lokal yang dimodulasi oleh QMI global:
$$\Phi(\boldsymbol\sigma) = (p_{s_{\uparrow}}\mu_{s_{\uparrow}} + p_{s_{\downarrow}}\mu_{s_{\downarrow}}) + \mathcal{I}_{local}(s_{\uparrow}, s_{\downarrow}) \quad (1)$$

Suku interaksi lokal $\mathcal{I}_{local}$ didefinisikan dengan mendistribusikan QMI global menggunakan bobot *Pointwise Mutual Information* (PMI). Formulasi ini adalah $\mathcal{I}_{local} = \xi \cdot I(A:B) \cdot \ln\left[ \frac{P(s_{\uparrow}, s_{\downarrow})}{P(s_{\uparrow})P(s_{\downarrow})} \right]$, di mana $\xi$ adalah konstanta normalisasi energi. Dengan pendekatan ini, setiap sel dalam matriks memiliki nilai energi yang unik dan asimetris, yang sangat penting agar transformasi ke parameter *Ising* tidak menghasilkan nilai nol. Hal ini secara ontologis konsisten karena mencampurkan besaran global informasi dengan dependensi lokal antar strategi.

## 4. Ekstraksi Parameter Ising via Transformasi Walsh-Hadamard
Parameter fisik $h_i$ (medan lokal) dan $J_{ij}$ (kopling interaksi) diekstraksi dari fungsi energi $\Phi(\boldsymbol\sigma)$ melalui transformasi linear yang ekuivalen dengan ekspansi *Walsh-Hadamard*. Proses ini mengonversi 16 nilai energi konfigurasi menjadi koefisien Hamiltonian yang merepresentasikan kontribusi linear dan kuadratik dari setiap *spin*. Karena $\Phi(\boldsymbol\sigma)$ telah didefinisikan secara unik untuk setiap strategi, asimetri dalam data $p$ dan $\mu$ akan secara langsung menghasilkan nilai $h_i$ dan $J_{ij}$ yang non-trivial.

Secara matematis, medan lokal dihitung melalui $h_i = \frac{1}{16} \sum_{\boldsymbol\sigma} \sigma_i \Phi(\boldsymbol\sigma)$, sedangkan kopling interaksi dihitung melalui $J_{ij} = \frac{1}{16} \sum_{\boldsymbol\sigma} \sigma_i \sigma_j \Phi(\boldsymbol\sigma)$. Koefisien $J_{ij}$ ini secara efektif menggantikan matriks kovarians dalam model Markowitz dengan menangkap interaksi strategis dan informasional yang lebih kaya. Melalui transformasi ini, masalah optimasi portofolio yang bersifat heuristik dalam *Game Theory* diterjemahkan secara presisi ke dalam masalah pencarian *ground state* pada sistem fisik *Ising*.

## 5. Minimisasi Hamiltonian dan Kestabilan Nash Equilibrium
Justifikasi utama penggunaan model *Ising* dalam optimasi ini terletak pada sifat sistem sebagai *Potential Game*. Dalam teori permainan, jika sebuah permainan memiliki fungsi potensial, maka titik minimum dari fungsi tersebut berkorespondensi langsung dengan *Pure Strategy Nash Equilibrium* (PSNE). Dengan mendesain $\Phi(\boldsymbol\sigma)$ sedemikian rupa sehingga mencerminkan utilitas gabungan dan keseimbangan informasi, minimisasi Hamiltonian $\hat{H}$ setara dengan mencari konfigurasi strategi yang paling stabil dan menguntungkan secara kolektif.

Implementasi Hamiltonian $\hat{H} = -\sum J_{ij} \hat{Z}_i \hat{Z}_j - \sum h_i \hat{Z}_i$ pada komputer kuantum memungkinkan pencarian solusi global melalui fenomena *Quantum Tunneling*. Berbeda dengan metode iteratif klasik yang sering terjebak dalam *local optima*, pendekatan ini memberikan probabilitas lebih tinggi untuk menemukan konfigurasi portofolio yang benar-benar optimal. Hasil akhirnya adalah sebuah portofolio yang tidak hanya efisien menurut batas Markowitz, tetapi juga memiliki ketahanan strategis yang tinggi berdasarkan prinsip-prinsip *Quantum Information Theory*.
