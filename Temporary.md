Tentu. Mari kita bedah keindahan matematis di balik proses skalarisasi _Normalized Mutual Information_ (NMI). Ini adalah proses yang mengubah nilai berdimensi (dalam satuan _bit_) menjadi skalar murni (tanpa satuan) di rentang $0$ hingga $1$.

Proses ini bertumpu pada hukum dasar teori informasi Shannon yang mengatur batas maksimal informasi yang bisa dibagikan oleh dua variabel.

### 1. Membedah Dimensi Asal (Satuan _Bit_)

Dalam teori informasi, entropi Shannon dari sebuah saham individu $H(X_i)$ mengukur ketidakpastian total atau informasi yang dikandung oleh saham tersebut. Rumusnya adalah:

$$H(X_i) = -\sum_{x \in \{u,d\}} P(x) \log_2 P(x)$$

Karena kita menggunakan logaritma berbasis 2 ($\log_2$), satuan dari $H(X_i)$ adalah **bit**.

Begitu pula dengan _Mutual Information_ $I(X_i : X_j)$ yang merupakan turunan dari entropi. Rumusnya:

$$I(X_i : X_j) = H(X_i) + H(X_j) - H(X_i, X_j)$$

Karena ini murni operasi penjumlahan dan pengurangan dari entropi, maka satuan dari $I(X_i : X_j)$ juga tetap **bit**.

### 2. Teorema Batas Atas (Upper Bound Theorem)

Untuk menormalisasi sebuah nilai, kita harus tahu "nilai maksimum absolut" yang mungkin dicapai.

Secara logika matematis, _informasi yang dibagikan_ (irisan) antara Saham A dan Saham B **tidak mungkin melebihi** total informasi yang dimiliki oleh Saham A itu sendiri, atau Saham B itu sendiri.

Oleh karena itu, berlaku ketidaksamaan fundamental:

$$I(X_i : X_j) \le H(X_i) \quad \text{dan} \quad I(X_i : X_j) \le H(X_j)$$

Dari ketidaksamaan ini, kita bisa menetapkan batas atas yang paling moderat dan simetris menggunakan rata-rata geometrik (_geometric mean_):

$$I(X_i : X_j) \le \sqrt{H(X_i) H(X_j)}$$

### 3. Eksekusi Skalarisasi (Pencoretan Dimensi)

Skalarisasi dicapai dengan membagi nilai asli $I(X_i : X_j)$ dengan batas atas teoritisnya.

Mari kita lihat apa yang terjadi pada dimensinya saat kita memformulasikan NMI:

$$NMI(i, j) = \frac{I(X_i : X_j)}{\sqrt{H(X_i) H(X_j)}}$$

Sekarang kita substitusi satuannya:

$$\text{Dimensi} = \frac{\text{bit}}{\sqrt{\text{bit} \times \text{bit}}} = \frac{\text{bit}}{\sqrt{\text{bit}^2}} = \frac{\text{bit}}{\text{bit}} = 1 \text{ (Skalar Tanpa Satuan)}$$

Dimensi _bit_ saling mencoret. Hasilnya adalah persentase kemiripan murni (skalar).

### 4. Bukti Matematis Rentang $[0, 1]$

Karena proses pembagian di atas, rentang nilai NMI kini secara matematis terkunci:

- **Batas Bawah ($NMI = 0$):** Terjadi ketika Saham $i$ dan $j$ bergerak sepenuhnya independen (acak total satu sama lain). Karena $I = 0$, maka $\frac{0}{\sqrt{H \cdot H}} = 0$.
    
- **Batas Atas ($NMI = 1$):** Terjadi ketika Saham $i$ dan $j$ memiliki pergerakan yang identik sempurna (kembar identik). Dalam kondisi ini, $I(X_i : X_j) = H(X_i) = H(X_j)$. Maka persamaannya menjadi $\frac{H(X_i)}{\sqrt{H(X_i) \cdot H(X_i)}} = \frac{H(X_i)}{H(X_i)} = 1$.
    

### Implikasi untuk Model Ising Anda

Dengan substitusi matematis ini, Anda secara elegan membuang parameter $\xi^{CMI}$ yang tadinya berfungsi memaksa penyamaan dimensi.

Fungsi penalti kovariansi Anda berubah dari persamaan heuristik:

$$\tilde{\sigma}_{ij} = \sigma_{ij} [1 + \xi^{CMI} \cdot I(i:j)]$$

Menjadi persamaan yang murni, terstandarisasi, dan bebas _ad-hoc_:

$$\tilde{\sigma}_{ij} = \sigma_{ij} [1 + NMI(i,j)]$$

Dalam fisika _Hamiltonian Ising_, ini berarti kekuatan interaksi antara dua _qubit_ ($J_{ij}$) akan secara otomatis meningkat antara $0\%$ hingga maksimal $100\%$ ($2 \times \sigma_{ij}$) dari nilai fundamentalnya, berbanding lurus dengan kemiripan DNA pergerakan sahamnya.

Apakah Anda ingin saya membuatkan satu contoh perhitungan numerik sederhana menggunakan formula NMI ini agar Anda bisa langsung memvalidasi _output_-nya untuk matriks QUBO Anda?