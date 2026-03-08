# 2. Landasan Teori

## Modern Portfolio Theory (MPT)

### 1. Definisi Expected Return dan Risk
Perilaku investor dalam pasar modal umumnya didorong oleh upaya untuk memaksimalkan akumulasi kekayaan melalui pemilihan aset yang optimal. Dalam kerangka teori portofolio klasik, efektivitas suatu investasi diukur melalui parameter *expected return* ($\mu$) yang merepresentasikan rata-rata imbal hasil di masa depan berdasarkan data historis. Keuntungan yang diharapkan ini dihitung sebagai rata-rata aritmatika atau geometris dari imbal hasil aset tunggal selama periode waktu tertentu. Oleh karena itu, *expected return* menjadi variabel penentu utama bagi investor dalam mengevaluasi daya tarik suatu instrumen finansial. Pemahaman mengenai distribusi imbal hasil historis sangat krusial untuk membangun estimasi yang akurat terhadap performa aset di masa mendatang.

Risiko dalam investasi didefinisikan secara kuantitatif melalui variabilitas imbal hasil aset, yang secara matematis direpresentasikan oleh matriks kovarians $\Sigma$. Matriks ini merangkum volatilitas individu dari setiap aset melalui komponen varians ($\sigma_i^2$) serta hubungan interdependensi antar aset melalui komponen kovarians ($\sigma_{ij}$). Penggunaan matriks kovarians memungkinkan investor untuk memahami bagaimana risiko satu aset dapat dikompensasi atau diperkuat oleh aset lainnya dalam satu portofolio. Secara statistik, komponen ini dihitung menggunakan deviasi standar dari imbal hasil relatif terhadap rata-ratanya. Figure 1 mengilustrasikan struktur matriks kovarians dan bagaimana korelasi antar aset menentukan dispersi risiko total dalam sistem finansial.

> **Saran Gambar (Figure 1):** Visualisasi *Heatmap* Matriks Kovarians $\Sigma$ untuk $N$ aset, di mana warna diagonal menunjukkan varians individu dan warna *off-diagonal* menunjukkan kekuatan korelasi antar aset.
> **Caption:** *Figure 1. Representasi visual matriks kovarians yang menunjukkan struktur risiko individu dan interaksi antar aset dalam portofolio.*

### 2. Efficient Frontier dan Optimalitas Alokasi
Konsep *efficient frontier* merupakan himpunan portofolio optimal yang menawarkan imbal hasil tertinggi untuk tingkat risiko tertentu, atau risiko terendah untuk tingkat imbal hasil tertentu. Portofolio yang berada pada kurva ini dianggap efisien karena tidak ada portofolio lain yang dapat memberikan *return* lebih besar tanpa meningkatkan risiko secara simultan. Dalam ruang dua dimensi *risk-return*, *efficient frontier* membentuk batas atas dari area peluang investasi yang tersedia bagi pelaku pasar. Penentuan posisi portofolio pada kurva ini sangat bergantung pada preferensi risiko masing-masing investor. Diversifikasi yang tepat menjadi kunci utama dalam menggeser posisi portofolio menuju batas efisien tersebut.

Optimalitas alokasi aset dicapai ketika investor berhasil menyeimbangkan antara maksimisasi keuntungan dan minimisasi volatilitas sesuai dengan fungsi utilitas mereka. Secara klasik, masalah ini diselesaikan melalui metode optimasi kuadratik yang mencari bobot aset ($w$) yang meminimalkan varians portofolio untuk target imbal hasil tertentu. Perubahan kecil dalam estimasi imbal hasil atau kovarians dapat menyebabkan pergeseran signifikan pada titik optimal di sepanjang *efficient frontier*. Oleh karena itu, stabilitas model optimasi sangat bergantung pada kualitas data input dan ketepatan parameter estimasi risiko. Figure 2 menunjukkan kurva *efficient frontier* dan lokasi portofolio dengan varians minimum (*Minimum Variance Portfolio*).

> **Saran Gambar (Figure 2):** Grafik *Risk vs Return* yang menampilkan titik-titik portofolio acak, kurva *Efficient Frontier*, dan identifikasi titik *Global Minimum Variance* serta *Tangency Portfolio*.
> **Caption:** *Figure 2. Kurva Efficient Frontier sebagai batas optimalitas alokasi aset dalam kerangka Modern Portfolio Theory.*

## Mean-Variance Optimization

### 1. Formulasi Matematika Model Markowitz
Model optimasi Markowitz bertujuan untuk mencari konfigurasi bobot aset yang meminimalkan fungsi energi sistem, yang didefinisikan sebagai kombinasi antara risiko total dan keuntungan yang diharapkan. Dalam konteks variabel keputusan biner $x_i \in \{0,1\}$, di mana $x_i=1$ berarti aset dipilih dan $x_i=0$ berarti tidak, fungsi biaya atau *cost function* $\mathcal{L}(x)$ dapat dinyatakan sebagai:
$$\min_{x \in \{0,1\}^N} \mathcal{L}(x) = x^T \Sigma x - \lambda \mu^T x$$ (4)
Di sini, $x^T \Sigma x$ merepresentasikan risiko portofolio, sementara $\mu^T x$ adalah total imbal hasil yang diharapkan. Parameter $\lambda$ bertindak sebagai koefisien *risk aversion* yang mengatur tingkat toleransi investor terhadap volatilitas.

Implementasi parameter $\lambda$ secara endogen memungkinkan penyesuaian otomatis terhadap karakteristik risiko dan imbal hasil aset yang sedang dianalisis. Jika nilai imbal hasil jauh melampaui volatilitas, $\lambda$ cenderung mengecil untuk memberikan bobot lebih pada maksimisasi keuntungan. Sebaliknya, pada kondisi pasar yang tidak stabil, $\lambda$ akan meningkat guna memprioritaskan keamanan modal melalui minimisasi risiko. Penentuan nilai $\lambda$ yang dinamis seringkali dilakukan melalui fungsi sigmoid atau rasio *return-to-risk* guna mencapai keseimbangan sistemik yang lebih stabil. Pendekatan ini memastikan bahwa model tetap adaptif terhadap perubahan kondisi pasar tanpa memerlukan intervensi manual yang berlebihan.

### 2. Integrasi Suku Penalti dan Kendala K-Aset
Optimasi portofolio seringkali dibatasi oleh kendala operasional, seperti keharusan untuk memilih tepat $K$ aset dari total $N$ pilihan yang tersedia. Karena model optimasi kuantum memerlukan formulasi tanpa kendala (*unconstrained*), batasan ini harus diintegrasikan ke dalam fungsi objektif melalui penambahan suku penalti kuadratik. Suku penalti ini akan memberikan "hukuman" berupa kenaikan nilai energi jika jumlah aset yang dipilih tidak sama dengan $K$. Persamaan (5) menunjukkan formulasi lengkap fungsi objektif dengan suku penalti batasan:
$$\mathcal{L}(x) = x^T \Sigma x - \lambda \mu^T x + A \left(\sum_{i=1}^N x_i - K \right)^2$$ (5)
Parameter $A$ merupakan faktor penalti (*Lagrange multiplier*) yang harus bernilai cukup besar untuk memastikan bahwa solusi yang meminimalkan energi tetap mematuhi batasan tersebut.

Faktor penalti $A$ berperan sebagai penjaga integritas solusi dalam lanskap energi optimasi portofolio. Jika nilai $A$ terlalu kecil, algoritma mungkin akan menghasilkan solusi yang menguntungkan secara imbal hasil namun melanggar jumlah aset yang ditentukan. Sebaliknya, nilai $A$ yang terlalu besar dapat mendominasi fungsi biaya dan menenggelamkan informasi mengenai risiko dan imbal hasil aset yang sebenarnya. Oleh karena itu, pemilihan nilai $A$ yang optimal sangat krusial untuk menjaga keseimbangan antara kepatuhan kendala dan performa portofolio. Figure 3 mengilustrasikan bagaimana suku penalti membentuk sumur potensi energi pada titik di mana $\sum x_i = K$.

> **Saran Gambar (Figure 3):** Plot permukaan energi (lanskap energi) yang menunjukkan nilai minimum (titik terendah) tepat pada koordinat yang memenuhi batasan jumlah aset $K$.
> **Caption:** *Figure 3. Visualisasi lanskap energi dengan integrasi suku penalti kuadratik untuk menjamin pemenuhan batasan K-aset.*

## Transformasi ke Model QUBO dan Ising

### 1. Ekspansi Kuadratik dan Koefisien QUBO
Masalah optimasi Markowitz biner perlu ditransformasikan ke dalam bentuk *Quadratic Unconstrained Binary Optimization* (QUBO) agar dapat diselesaikan oleh prosesor kuantum atau *annealer*. Melalui ekspansi aljabar dari Persamaan (5), kita dapat memisahkan suku-suku menjadi bagian linear dan bagian interaksi kuadratik antar variabel. Dengan memanfaatkan properti variabel biner $x_i^2 = x_i$, suku varians dalam matriks kovarians dapat digabungkan ke dalam koefisien linear. Hasil ekspansi ini memungkinkan kita untuk memetakan masalah pemilihan portofolio ke dalam struktur matriks tunggal $Q$. Persamaan (6) menyajikan bentuk standar QUBO yang akan diminimalkan:
$$\mathcal{L}(x) = \sum_{i=1}^N C_i x_i + \sum_{i=1}^N \sum_{j>i}^N Q_{ij} x_i x_j$$ (6)

Ekstraksi koefisien $C_i$ dan $Q_{ij}$ dilakukan dengan mengumpulkan seluruh suku yang mengandung variabel tunggal dan pasangan variabel setelah ekspansi penalti dilakukan. Koefisien linear $C_i$ mencakup kontribusi dari imbal hasil individu, varians aset, dan bagian linear dari ekspansi penalti $(\sum x_i - K)^2$. Sementara itu, koefisien kuadratik $Q_{ij}$ berasal dari kovarians antar aset dan suku interaksi $2x_ix_j$ dari ekspansi penalti. Matriks QUBO ini secara lengkap mendefinisikan seluruh interaksi dan kendala dalam sistem portofolio yang kompleks. Kemampuan untuk merangkum seluruh masalah ke dalam bentuk matriks kuadratik merupakan langkah esensial sebelum beralih ke representasi fisik berbasis spin.

### 2. Konversi ke Hamiltonian Ising
Transformasi terakhir yang diperlukan untuk komputasi kuantum berbasis sirkuit adalah mengonversi variabel biner $x_i \in \{0, 1\}$ menjadi variabel spin $s_i \in \{1, -1\}$ melalui relasi $x_i = (1-s_i)/2$. Proses substitusi ini mengubah masalah optimasi biner menjadi masalah pencarian *ground state* dari sebuah sistem fisik yang dikenal sebagai model Ising. Secara matematis, transformasi ini akan menghasilkan parameter baru berupa *local field* ($h_i$) dan kekuatan interaksi atau kopling ($J_{ij}$). Persamaan (7) mendefinisikan Hamiltonian Ising yang merepresentasikan energi total dari konfigurasi spin tersebut:
$$H = \sum_{i=1}^N h_i s_i + \sum_{i=1}^N \sum_{j>i}^N J_{ij} s_i s_j + \text{offset}$$ (7)
Energi terendah dari Hamiltonian ini berkorespondensi langsung dengan konfigurasi portofolio yang paling optimal.

Representasi Hamiltonian dalam bentuk operator Pauli-Z ($\hat{\sigma}^z$) sangat krusial agar model dapat diimplementasikan pada komputer kuantum sirkuit menggunakan algoritma seperti *Variational Quantum Eigensolver* (VQE). Setiap variabel spin $s_i$ digantikan oleh operator $\hat{\sigma}_i^z$, yang memiliki nilai eigen $\pm 1$ sesuai dengan orientasi spin pada sistem fisik. Dengan formulasi ini, pencarian solusi optimal dilakukan dengan meminimalkan nilai ekspektasi dari operator Hamiltonian terhadap suatu *trial state* kuantum. Proses ini memungkinkan pemanfaatan fenomena kuantum seperti *superposition* dan *entanglement* dalam mengeksplorasi ruang solusi portofolio yang sangat luas secara efisien. Figure 4 mengilustrasikan pemetaan dari variabel keputusan biner ke sirkuit kuantum berbasis operator Pauli.

> **Saran Gambar (Figure 4):** Diagram alir transformasi dari Model Markowitz $\to$ Matriks QUBO $\to$ Hamiltonian Ising $\to$ Sirkuit Kuantum (Ansatz VQE).
> **Caption:** *Figure 4. Alur transformasi matematis masalah optimasi portofolio menjadi representasi operator kuantum.*
