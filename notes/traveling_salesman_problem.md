# Traveling Salesman Problem (TSP) dan Pemetaan Ising

Dokumen ini menjelaskan tentang **Traveling Salesman Problem (TSP)**, kompleksitasnya, dan bagaimana masalah ini dipetakan ke dalam bentuk **Ising Hamiltonian** (atau QUBO) sebagaimana disebutkan dalam konteks optimasi sistem.

## 1. Apa itu Traveling Salesman Problem (TSP)?

TSP adalah salah satu masalah optimasi kombinatorial yang paling terkenal dalam matematika dan ilmu komputer. 

**Definisi Masalah:**
Seorang pedagang (salesman) harus mengunjungi $N$ buah kota. Syaratnya adalah:
1. Setiap kota harus dikunjungi **tepat satu kali**.
2. Pedagang tersebut harus kembali ke kota awal (membentuk rute tertutup/siklus).
3. Tujuannya adalah mencari rute dengan **total jarak (biaya) terpendek**.

## 2. Mengapa TSP Sangat Sulit?

TSP termasuk dalam kategori masalah **[[NP-hard]]**. 
- Untuk $N$ kota, jumlah kemungkinan rute adalah $(N-1)! / 2$.
- Jika ada 10 kota, ada sekitar 181.440 rute.
- Jika ada 30 kota, jumlah rutenya melampaui jumlah atom di alam semesta.
Komputer konvensional akan membutuhkan waktu yang sangat lama (eksponensial) untuk mencoba satu per satu rute jika jumlah kota bertambah banyak.

## 3. Pemetaan TSP ke Ising Hamiltonian (QUBO)

Agar TSP bisa diselesaikan oleh metode seperti *Simulated Annealing* atau *Quantum Annealing*, kita harus mengubah masalah ini menjadi sebuah fungsi energi (**Hamiltonian**). Tujuannya adalah membuat rute yang valid memiliki energi rendah, dan rute yang tidak valid atau jauh memiliki energi tinggi.

Kita menggunakan variabel biner $x_{i,p}$ di mana:
- $x_{i,p} = 1$ jika kota $i$ dikunjungi pada urutan ke-$p$.
- $x_{i,p} = 0$ jika tidak.

Hamiltonian total ($H$) untuk TSP terdiri dari dua bagian: **Constraint** (Kendala) dan **Cost** (Biaya).

### A. Penalty/Constraint (H_penalty)
Kita harus memberikan hukuman (penalti) energi jika aturan dilanggar:
1. **Satu kota hanya dikunjungi satu kali:** $\sum_{i} (\sum_{p} x_{i,p} - 1)^2$
2. **Satu urutan waktu hanya boleh ada satu kota:** $\sum_{p} (\sum_{i} x_{i,p} - 1)^2$

Jika jumlah kota di satu waktu bukan 1, maka nilai fungsi ini akan positif (energi naik), sehingga sistem akan berusaha menghindarinya.

### B. Objective/Cost (H_cost)
Bagian ini menghitung total jarak:
$$H_{cost} = \sum_{p} \sum_{i,j} D_{ij} x_{i,p} x_{j,p+1}$$
Di mana $D_{ij}$ adalah jarak antara kota $i$ dan kota $j$. Sistem akan mencari konfigurasi di mana $x_{i,p}$ dan $x_{j,p+1}$ bernilai 1 hanya jika jarak $D_{ij}$ di antara mereka kecil.

### C. Total Hamiltonian
$$H_{total} = A \cdot H_{penalty} + B \cdot H_{cost}$$
Di sini $A$ harus jauh lebih besar daripada $B$ ($A \gg B$) untuk memastikan bahwa sistem memprioritaskan rute yang **valid** (mengikuti aturan) sebelum mencari rute yang **pendek**.

## 4. Hubungan dengan Parameter Bias (h_i) dan Interaksi (J_ij)

Dalam bentuk Ising ($s_i \in \{1, -1\}$), pemetaan di atas akan berubah menjadi:
- **Parameter Bias ($h_i$):** Menentukan kecenderungan sebuah kota untuk berada di urutan tertentu berdasarkan batasan awal.
- **Parameter Interaksi ($J_{ij}$):** Menghubungkan variabel-variabel tersebut. Interaksi ini mewakili "biaya" perpindahan antar kota. Jika jarak antar kota sangat jauh, interaksi $J$ akan dibuat sangat negatif (anti-feromagnetik) agar kedua spin tersebut tidak aktif secara bersamaan di urutan yang berdekatan.

## 5. Aplikasi TSP di Dunia Nyata

Meskipun namanya "Salesman", TSP digunakan untuk:
1. **Logistik & Pengiriman:** Optimasi rute kurir (seperti JNE, Gojek, atau Amazon).
2. **Manufaktur:** Gerakan lengan robot saat menyolder titik-titik pada papan sirkuit (PCB).
3. **DNA Sequencing:** Menyusun potongan-potongan kode genetik.
4. **Perencanaan Satelit:** Mengatur urutan pengambilan gambar bumi oleh satelit agar hemat bahan bakar.

## 6. Kesimpulan
TSP adalah masalah "pencarian jalur" yang menjadi dasar pengujian algoritma optimasi modern. Dengan mengubahnya menjadi **Ising Hamiltonian**, kita bisa memanfaatkan sifat fisika (mencari energi terendah) untuk menemukan solusi rute terbaik di tengah miliaran kemungkinan yang ada.
