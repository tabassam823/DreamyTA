# Rencana Backtest Strategi HE-VQE

Dokumen ini berisi panduan teknis dan strategis untuk melakukan pengujian *backtest* pada strategi optimasi portofolio berbasis *Hardware-Efficient Variational Quantum Eigensolver* (HE-VQE).

## 1. Implementasi Metode "Sliding Window" atau "Rolling Basis"
Saat ini, kode mengambil data statis dari Januari 2025 hingga Januari 2026. Untuk *backtest* yang valid:
*   **Window Training:** Gunakan data historis (misal: 6 bulan) untuk menghitung *payoff matrix*, $\lambda$ pasar, dan parameter Hamiltonian ($h_i$ dan $J_{ij}$).
*   **Window Testing:** Terapkan portofolio yang dipilih oleh VQE pada periode berikutnya (misal: 1 bulan ke depan).
*   **Geser Jendela:** Ulangi proses ini secara berkala (bulanan atau triwulanan) untuk melihat bagaimana strategi beradaptasi dengan perubahan volatilitas pasar.

## 2. Gunakan Benchmark yang Relevan
Bandingkan hasil seleksi VQE (misal: ASII & TLKM) dengan:
*   **Equally Weighted Portfolio:** Portofolio dengan bobot sama untuk semua aset input (BBCA, ASII, TLKM, UNVR).
*   **Indeks Harga Saham Gabungan (IHSG):** Atau indeks LQ45 sebagai representasi pasar.
*   **Markowitz Klasik:** Gunakan optimasi rata-rata varians standar tanpa pendekatan kuantum untuk melihat apakah VQE memberikan *alpha* (keunggulan) tambahan.

## 3. Analisis Stabilitas Parameter Hamiltonian
Dalam file Anda, parameter $J_{ij}$ dihitung melalui *Quantum Mutual Information* (QMI). Lakukan pengujian sensitivitas terhadap:
*   **Panjang Data:** Apakah nilai $J_{ij}$ berubah drastis jika menggunakan data 3 bulan vs 12 bulan?
*   **Korelasi vs QMI:** Bandingkan apakah korelasi Pearson biasa memberikan hasil seleksi aset yang sama dengan QMI.

## 4. Pengujian Efek Penalti dan Kedalaman Sirkuit (Ansatz Depth)
Anda menetapkan `penalty_A = 10.0` dan `depth = 2`.
*   **Convergence Check:** Lakukan pengujian apakah sirkuit dengan `depth=3` atau `depth=4` menghasilkan energi yang lebih dekat ke *Exact Energy*.
*   **Penalty Tuning:** Jika hasil VQE sering memilih jumlah aset yang tidak sesuai dengan $K=2$, naikkan nilai penalti secara dinamis.

## 5. Metrik Evaluasi Selain Sharpe Ratio
Tambahkan metrik berikut untuk mengukur risiko:
*   **Maximum Drawdown (MDD):** Penurunan maksimum portofolio dari titik tertinggi ke terendah.
*   **Sortino Ratio:** Fokus pada risiko volatilitas negatif.
*   **Turnover Rate:** Hitung seberapa sering aset dalam portofolio berubah untuk memperhitungkan biaya transaksi.

## 6. Simulasi Noise (Realistik untuk Komputer Kuantum)
Tambahkan *Noise Model* (seperti *depolarizing noise* atau *amplitude damping*) pada sirkuit HE-VQE untuk melihat ketahanan strategi di perangkat NISQ.

---

# Langkah Kerja Backtest (Simulasi Modal 100 Juta)

Berikut adalah *workflow* terstruktur untuk mensimulasikan perkembangan modal (*equity curve*) dengan modal awal 100 juta IDR dan *rebalancing* bulanan.

## 1. Inisialisasi Data & Parameter
*   **Aset Fokus:** `['BBCA.JK', 'ASII.JK', 'TLKM.JK', 'UNVR.JK']`.
*   **Periode Historis:** Ambil data 3-5 tahun ke belakang (misal: 2021 – 2026) menggunakan `yfinance`.
*   **Modal Awal ($P_0$):** Tetapkan `balance_vqe = 100,000,000` dan `balance_bench = 100,000,000`.
*   **Lookback Window:** Tetapkan jendela data 6 bulan (126 hari bursa) untuk menghitung parameter Hamiltonian.

## 2. Loop Rebalancing Bulanan (Strategi Aktif)
Gunakan *loop* yang berpindah setiap satu bulan:

### A. Tahap Training (In-Sample)
*   Ambil data *log returns* dari 6 bulan terakhir sebelum tanggal *rebalancing*.
*   Hitung $\lambda_{market}$ (endogen), matriks *payoff* Markowitz, dan $J_{ij}$ melalui QMI.

### B. Tahap Optimasi (VQE)
*   Bangun Hamiltonian Ising dengan penalti $K=2$.
*   Jalankan HE-VQE dengan *optimizer* SPSA untuk mencari *ground state*.
*   Ekstrak 2 aset dengan probabilitas tertinggi dari hasil *sampling bitstring*.

### C. Tahap Trading (Out-of-Sample)
*   Alokasikan modal bulan berjalan: 50% ke Aset A dan 50% ke Aset B yang terpilih.
*   Hitung performa (*return*) kedua aset tersebut selama 1 bulan ke depan.
*   **Pembaruan Modal:** `Modal = Modal * (1 + Return Bulanan)`.
*   Simpan nilai modal ke dalam list `equity_curve_vqe`.

## 3. Simulasi Benchmark (Indexing)
*   Bagi modal 100 juta menjadi 4 bagian sama rata (25% per aset).
*   Hitung *return* rata-rata dari keempat aset tersebut setiap bulan.
*   **Pembaruan Modal:** `Modal = Modal * (1 + Return Rata-rata 4 Aset)`.
*   Simpan ke dalam list `equity_curve_bench`.

## 4. Penanganan Biaya Transaksi
Asumsikan biaya beli 0.15% dan biaya jual 0.25% setiap kali terjadi perubahan komposisi portofolio (*rebalancing*) agar hasil lebih realistis.

## 5. Analisis Hasil & Visualisasi
*   **Grafik Perkembangan Modal:** Plot `equity_curve_vqe` vs `equity_curve_bench`.
*   **Metrik Kumulatif:**
    *   *Total Return* (%)
    *   *Annualized Sharpe Ratio*
    *   *Maximum Drawdown*
    *   *Win Rate* (berapa bulan VQE mengalahkan benchmark)

## 6. Ringkasan Strategi (Pseudo-logic)
```python
# Pseudo-logic untuk eksekusi
start_date = "2021-01-01"
rebalance_dates = pd.date_range(start=start_date, end="2026-01-01", freq='BMS')

for i in range(len(rebalance_dates)-1):
    current_date = rebalance_dates[i]
    next_date = rebalance_dates[i+1]
    
    # 1. Ambil data 6 bulan sebelum current_date
    # 2. Jalankan fungsi VQE -> dapatkan 2 aset terpilih
    # 3. Hitung return 2 aset tersebut antara current_date & next_date
    # 4. Update modal VQE (kurangi biaya transaksi jika ada perubahan aset)
    # 5. Update modal Benchmark (rata-rata 4 aset)
```

**Saran Tambahan:** Karena proses VQE menggunakan optimasi SPSA yang memakan waktu, pertimbangkan untuk menyimpan hasil optimasi VQE ke dalam file `.csv` atau *cache* agar Anda tidak perlu mengulang proses sirkuit kuantum yang berat jika hanya ingin mengubah visualisasi grafiknya saja.
