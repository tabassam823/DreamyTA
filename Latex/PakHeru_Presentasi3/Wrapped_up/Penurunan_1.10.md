Persamaan **(1.10)** merupakan pembuktian bahwa fungsi gelombang $|\Psi\rangle$ ternormalisasi (total probabilitas sama dengan 1). Penurunannya memanfaatkan definisi dari persamaan **(1.6)**, **(1.7)**, dan **(1.9)**.

Berikut adalah langkah-langkah penurunan detailnya:

---

### 1. Definisi Produk Dalam $\langle\Psi|\Psi\rangle$

Berdasarkan persamaan **(1.6)**, kita memiliki:

$$|\Psi\rangle = \sum_{i,j} \alpha_{ij} |ij\rangle$$

Untuk mendapatkan Bra $\langle\Psi|$, kita melakukan konjugat Hermitian (seperti yang kita bahas sebelumnya):

$$\langle\Psi| = \sum_{i',j'} \alpha_{i'j'}^* \langle i'j'|$$

Maka, produk dalam $\langle\Psi|\Psi\rangle$ adalah:

$$\langle\Psi|\Psi\rangle = \left( \sum_{i',j'} \alpha_{i'j'}^* \langle i'j'| \right) \left( \sum_{i,j} \alpha_{ij} |ij\rangle \right)$$

---

### 2. Menggunakan Sifat Ortonormalitas

Karena basis $|ij\rangle$ bersifat ortonormal ($\langle i'j' | ij \rangle = \delta_{i'i}\delta_{j'j}$), maka perkalian silang antar basis yang berbeda akan bernilai nol. Persamaan di atas menyederhanakan menjadi:

$$\langle\Psi|\Psi\rangle = \sum_{i,j} \alpha_{ij}^* \alpha_{ij} = \sum_{i,j} |\alpha_{ij}|^2$$

Ini adalah bagian pertama dari persamaan **(1.10)**.

---

### 3. Substitusi dengan Data Empiris

Sekarang kita hubungkan dengan probabilitas empiris. Dari persamaan **(1.9)**, kita tahu bahwa:

$$\alpha_{ij} = \sqrt{\frac{n_{ij}}{N}}$$

Jika kita kuadratkan kedua sisi:

$$|\alpha_{ij}|^2 = \frac{n_{ij}}{N}$$

Substitusikan nilai $|\alpha_{ij}|^2$ ini ke dalam deret penjumlahan di langkah sebelumnya:

$$\sum_{i,j} |\alpha_{ij}|^2 = \sum_{i,j} \frac{n_{ij}}{N}$$

---

### 4. Pembuktian Normalisasi

Karena $N$ adalah jumlah total seluruh kejadian (total hari pengamatan) dan $n_{ij}$ adalah frekuensi kejadian untuk state spesifik $ij$, maka jumlah dari semua frekuensi $n_{ij}$ pastilah sama dengan $N$:

$$\sum_{i,j} n_{ij} = N$$

Sehingga:

$$\sum_{i,j} \frac{n_{ij}}{N} = \frac{1}{N} \sum_{i,j} n_{ij} = \frac{N}{N} = 1$$

---

### Kesimpulan

Secara ringkas, alur logikanya adalah:

1. **$\langle\Psi|\Psi\rangle$** secara matematis sama dengan jumlah kuadrat amplitudo ($\sum |\alpha_{ij}|^2$).
    
2. **$|\alpha_{ij}|^2$** didefinisikan sebagai probabilitas ($n_{ij}/N$).
    
3. **Jumlah seluruh probabilitas** dalam satu sistem tertutup haruslah **1**.
    

Itulah mengapa kondisi normalisasi pada persamaan **(1.10)** terpenuhi secara otomatis melalui pendekatan _Frequentist_ ini.

Apakah Anda ingin saya membantu menghitungkan contoh angka jika diketahui nilai $n_{ij}$ untuk sistem 2-qubit?