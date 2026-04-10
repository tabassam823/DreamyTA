# Catatan Teknis: *Normalized Mutual Information* (NMI) dan Formulasi Kopling dalam Sistem Portofolio

## 1. Fundamen Teori Informasi Shannon: Entropi sebagai Ukuran Ketidakpastian

Entropi Shannon ($H$) merupakan metrik fundamental dalam teori informasi yang mengukur tingkat ketidakpastian atau rata-rata isi informasi dari suatu variabel acak. Dalam konteks aset finansial, entropi menguantifikasi derajat acak dari pergerakan harga atau status imbal hasil yang dinyatakan dalam satuan *bits*. Formulasi ini memungkinkan peneliti untuk memetakan distribusi probabilitas marginal ke dalam besaran skalar yang merepresentasikan volatilitas informasional sistem. Penggunaan logaritma basis dua dalam perhitungan ini menegaskan bahwa informasi dipandang sebagai proses reduksi ketidakpastian biner.

Secara matematis, entropi Shannon untuk sebuah aset $X_i$ didefinisikan melalui nilai harapan dari isi informasinya. Jika $p(x)$ merepresentasikan probabilitas marginal kemunculan status $x$ (misalnya, kondisi *up* atau *down*), maka formulasi entropinya adalah:
$$H(X_i) = -\sum_{x \in \{u, d\}} p(x) \log_2 p(x) \qquad(1)$$
Persamaan (1) menunjukkan bahwa nilai entropi akan mencapai maksimum ketika probabilitas antar status setara, yang mengindikasikan ketidakpastian total. Sebaliknya, jika satu status mendominasi secara absolut, entropi akan meluruh menuju nol karena tidak ada informasi baru yang dihasilkan. Pemahaman mengenai entropi individual ini menjadi fondasi krusial sebelum melakukan analisis ketergantungan antar-variabel dalam sistem yang lebih kompleks.

## 2. Informasi Interaksi (*Interaction Information*) dan Dependensi Orde Tinggi

Dalam sistem yang melibatkan multitivariat seperti portofolio dengan $N=4$ aset ($X_1, X_2, X_3, X_4$), redundansi informasi tidak lagi bersifat biner sederhana. Teori informasi orde tinggi memperkenalkan konsep *Interaction Information* untuk menangkap dependensi yang muncul secara simultan di antara tiga aset atau lebih. Metrik ini sangat krusial dalam ekonomi-fisika karena korelasi pasar sering kali bersifat non-linear dan tidak dapat dijelaskan hanya melalui pasangan variabel (*pairwise*). Integrasi informasi multisistem ini memberikan gambaran mikroskopis yang lebih akurat mengenai struktur ketergantungan sistemik dalam pasar modal.

Formulasi informasi bersama untuk sistem dengan empat variabel mengikuti prinsip inklusi-eksklusi entropi Shannon. Hubungan tersebut dinyatakan dalam persamaan berikut:
$$\begin{aligned}
I(X_1 : X_2 : X_3 : X_4) = &\sum_i H(X_i) - \sum_{i<j} H(X_i, X_j) \\
&+ \sum_{i<j<k} H(X_i, X_j, X_k) - H(X_1, X_2, X_3, X_4)
\end{aligned} \qquad(2)$$
Melalui Persamaan (2), terlihat bahwa informasi interaksi merupakan hasil penyeimbangan antara entropi individu, entropi gabungan biner, dan entropi orde lebih tinggi. Nilai positif pada $I(\cdot)$ mengindikasikan adanya redundansi informasi, sementara nilai negatif menunjukkan efek sinergi di mana gabungan variabel memberikan informasi lebih banyak daripada jumlah bagian-bagiannya. Pendekatan ini memastikan bahwa seluruh spektrum korelasi non-linear tetap terakomodasi dalam analisis risiko portofolio sebelum dilakukan simplifikasi fisis.

## 3. Mekanisme Keruntuhan Orde (*Order Collapse*) melalui Kendala Kardinalitas

Meskipun teori informasi mengizinkan interaksi orde tinggi, struktur masalah optimasi portofolio di bawah kendala fisik tertentu sering kali memaksa sistem untuk melakukan penyederhanaan secara alami. Fenomena ini muncul secara eksplisit ketika diterapkan kendala kardinalitas $K=2$, di mana sistem hanya diizinkan untuk memilih tepat dua aset dari semesta empat aset yang tersedia. Secara matematis, kendala ini dinyatakan sebagai $\sum_{i=1}^4 x_i = 2$, yang bertindak sebagai filter ketat terhadap ruang konfigurasi Hamiltonian. Akibatnya, interaksi yang melibatkan lebih dari dua variabel aktif secara simultan menjadi mustahil secara struktural.

Bukti matematis dari lenyapnya interaksi orde tinggi ini berakar pada analisis nilai variabel biner $x_i \in \{0, 1\}$. Berdasarkan *Pigeonhole Principle* (Prinsip Sarang Merpati), jika total variabel yang aktif dibatasi hanya dua, maka dalam setiap himpunan bagian yang terdiri dari tiga variabel, setidaknya satu variabel pasti bernilai nol. Kondisi ini berimplikasi langsung pada seluruh suku interaksi orde-3 dan orde-4, yang mana hasil kali variabel-variabel tersebut akan selalu bernilai nol:
$$\forall (i, j, k) \in \{1, \dots, 4\} \implies x_i x_j x_k = 0 \qquad(3)$$
Melalui mekanisme *order collapse* ini, kompleksitas informasi interaksi tinggi yang didefinisikan pada bagian sebelumnya secara definitif runtuh menjadi interaksi biner. Hal ini menjamin bahwa model tetap kompatibel dengan struktur Ising Hamiltonian standar yang hanya mengakomodasi kopling pasangan variabel.

## 4. Skalarisasi *Normalized Mutual Information* (NMI) sebagai Metrik Korelasi Non-linear

Setelah terjadi reduksi orde, korelasi non-linear yang tersisa diintegrasikan ke dalam matriks risiko melalui transformasi *Normalized Mutual Information* (NMI). Prosedur skalarisasi ini sangat penting untuk menjamin konsistensi dimensional antara satuan informasi (*bits*) dan besaran kovariansi. NMI didefinisikan sebagai rasio informasi bersama terhadap rata-rata geometrik entropi masing-masing variabel berdasarkan *Upper Bound Theorem*. Dengan skema normalisasi ini, metrik informasi menjadi besaran nirdimensi yang lebih mudah dioperasikan dalam perhitungan matriks QUBO.

Definisi matematis NMI untuk pasangan aset $(i, j)$ dinyatakan sebagai berikut:
$$NMI(i, j) = \frac{I(X_i : X_j)}{\sqrt{H(X_i)H(X_j)}} \qquad(4)$$
Hasil dari formulasi pada Persamaan (4) adalah skalar yang berada pada rentang $[0, 1]$. Nilai $NMI = 0$ merepresentasikan independensi statistik yang sempurna, sedangkan $NMI = 1$ menunjukkan identitas informasi yang identik antar-aset. Penggunaan akar rata-rata geometrik sebagai penyebut memastikan bahwa NMI bersifat simetris dan tangguh terhadap variasi magnitudo entropi individu, sehingga memberikan representasi korelasi yang lebih objektif dibandingkan koefisien korelasi linier Pearson.

## 5. Integrasi NMI ke dalam Formulasi Hamiltonian Ising dan Matriks Kovariansi

Tahap akhir dari formulasi ini adalah penguatan (*amplification*) elemen matriks kovariansi tradisional menggunakan skalar NMI yang telah diperoleh. Redefinisi elemen matriks kovariansi ini bertujuan untuk menggabungkan metrik risiko berbasis varians dengan metrik redundansi berbasis informasi. Melalui skema ini, kontribusi informasional diintegrasikan secara intrinsik ke dalam struktur risiko $\tilde{\sigma}_{ij}$, sehingga model tetap *robust* terhadap anomali pasar. Rumusan penguatan tersebut dinyatakan sebagai berikut:
$$\tilde{\sigma}_{ij} = \sigma_{ij} [1 + NMI(i, j)] \qquad(5)$$

Berdasarkan matriks kovariansi yang telah diperkuat ($\tilde{\sigma}_{ij}$), parameter kopling ($J_{ij}$) dalam Hamiltonian Ising dapat diekstraksi dari elemen *off-diagonal* matriks QUBO. Parameter ini mengintegrasikan risiko sistemik $\gamma$ dan kekuatan penalti kardinalitas $\lambda_{pen}$ ke dalam satu koefisien interaksi fisik. Formulasi akhir bagi koefisien kopling tersebut adalah:

$$J_{ij} = \frac{Q_{ij}}{4} = \frac{\gamma \sigma_{ij} [1 + NMI(i, j)] + 2\lambda_{pen}}{4} \qquad(6)$$

Penggunaan NMI dalam Persamaan (6) memastikan bahwa konfigurasi *ground state* yang dihasilkan oleh komputer kuantum akan merepresentasikan titik kesetimbangan ekonomi yang lebih stabil. Hal ini dikarenakan lanskap energi portofolio telah mengakomodasi redundansi informasi yang lebih komprehensif, melampaui statistik biner standar.
