# Laporan Analisis & Perbaikan Exact Potential Game (EPG)

## 1. Identifikasi Masalah
Ditemukan inkonsistensi matematis pada implementasi Game Theory (Nash Equilibrium) yang menyebabkan performa *GT Warm Start* menurun secara signifikan pada portofolio berukuran besar ($N \ge 6$).

### A. Over-counting Risiko Interaksi (Covariance)
Pada versi sebelumnya, fungsi pencarian Nash menggunakan penjumlahan utilitas individual ($\sum u_i$). Karena utilitas individual pemain $i$ sudah mencakup interaksi dengan semua pemain $j$, maka saat dijumlahkan, suku kovariansi $\sigma_{ij}$ terhitung **dua kali**.
*   **Dampak:** Penalti risiko menjadi 2x lebih besar dari seharusnya, membuat Nash Equilibrium memilih aset yang terlalu konservatif.

### B. Inkonsistensi Skala ($1/K$ vs $1/K^2$)
Hamiltonian pada VQE menggunakan normalisasi berdasarkan jumlah aset terpilih ($K$):
*   Return dihitung dengan skala $1/K$.
*   Risk dihitung dengan skala $1/K^2$.
Pencarian Nash sebelumnya menggunakan nilai $\mu$ dan $\Sigma$ mentah tanpa skala ini.
*   **Dampak:** Pada $N=6, K=3$, Nash menganggap risiko 3x lebih dominan daripada yang dilihat oleh VQE. Hal ini mengakibatkan *warm-start* memberikan bitstring yang tidak relevan dengan lanskap energi VQE.

---

## 2. Perubahan Logika Matematis
Implementasi baru menggunakan **Fungsi Potensial ($\Phi$)** yang selaras dengan fungsi objektif portofolio Markowitz dan Hamiltonian VQE:

$$ \Phi(x) = \frac{1}{K} \sum_{i=1}^N \mu_i x_i - \frac{\gamma}{2K^2} \sum_{i=1}^N \sum_{j=1}^N \sigma_{ij} x_i x_j $$

Dalam *Exact Potential Game*, setiap perbaikan pada utilitas individual pemain akan meningkatkan nilai Potensial ($\Phi$) secara setara. Dengan memaksimalkan $\Phi$ melalui *Sequential Best Response* (SBR), kita dijamin mendapatkan Nash Equilibrium yang merupakan *local maximum* dari utilitas portofolio sebenarnya.

---

## 3. Detail Perubahan Kode

### `find_nash_sbr.py`
- Mengganti fungsi `calculate_total_utility` dengan `calculate_potential`.
- Menambahkan logika pemilihan subset matriks sigma (`np.ix_`) untuk efisiensi perhitungan risiko.
- Memastikan perhitungan risiko mencakup varians ($\sigma_{ii}$) dan kovarians ($\sigma_{ij}$) dengan bobot yang benar.

### `config.py`
- Menambahkan key `nash_history` pada dictionary `files`.
- Memastikan riwayat pencarian Nash disimpan per skenario $N$ (misal: `riwayat_nash_sbr_N6.csv`) untuk menghindari tumpang tindih data.

### `run_strategy_step.py`
- Menyesuaikan pemanggilan `find_nash_sbr` agar menggunakan konfigurasi file yang baru dan parameter yang konsisten.

---

## 4. Kesimpulan
Dengan perbaikan ini, Nash Equilibrium kini memberikan "titik awal" (warm-start) yang secara matematis valid bagi VQE. Pada $N \ge 6$, VQE tidak lagi harus mengoreksi bias risiko yang salah dari Nash, sehingga konvergensi diharapkan lebih cepat dan hasil *return* portofolio lebih optimal dibandingkan metode tanpa GT.
