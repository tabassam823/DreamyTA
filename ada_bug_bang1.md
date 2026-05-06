# Laporan Analisis Bug & Masalah — GTQuantumInvest

---

## Masalah 1 — Mengapa kode lambat meski hanya 2 qubit & depth 4?

### Akar masalah: LR Finder berjalan **sebelum** VQE di setiap window rebalancing

Di setiap periode rebalancing, `run_strategy_step` memanggil dua rutinitas besar secara berurutan:

```
find_optimal_lr_spsa(...)   ← menguji 15 nilai LR × (30 iterasi × 25 batch_size) sirkuit
run_vqe_adaptive(...)       ← menjalankan 4 depth × max 2000 iterasi × 25 batch_size sirkuit
```

### Hitung biaya evaluasi sirkuit per window:

| Tahap | Rumus | Hasil |
|---|---|---|
| LR Finder | 15 LR × 30 iter × 25 batch × 2 shot/step | **≈ 22.500 eval** |
| VQE depth 1–4 | 4 depth × 2000 iter × 25 batch × 2 shot/step | **≈ 400.000 eval** |
| **Total per window** | | **≈ 422.500 evaluasi kuantum** |

Dengan 36 window backtest (laporan N2) → **±15 juta** evaluasi sirkuit hanya untuk N=2.

### Masalah tambahan di `run_spsa_test.py` (baris 16-26)

```python
while total_iters < max_iters:       # max_iters = 30
    for _ in range(batch_size):      # batch_size = 25 (default)
        ...
        total_iters += 1
```

`total_iters` menghitung **tiap step** satu per satu, tetapi kondisi loop `< max_iters=30` baru tercapai setelah 30 langkah, padahal setiap langkah sudah memanggil `cost_circuit` **dua kali** (plus/minus). Jadi per satu kandidat LR, ada 30 × 2 = **60 evaluasi**, dan dikali 15 kandidat = **900 evaluasi** hanya untuk LR Finder.

Namun bottleneck terbesar tetap `run_vqe_adaptive` dengan `max_total_iter=2000` dan konvergensi yang sangat lambat (laporan menunjukkan banyak yang mencapai 2000 iter = tidak konvergen).

### Solusi yang disarankan

1. **Kurangi `test_iters` LR Finder** dari 30 → 15 atau hapus LR Finder jika `best_a` cukup dikalibrasi sekali di awal.
2. **Periksa konvergensi**: Hampir semua depth > 1 mencapai 2000 iterasi (tidak konvergen) → SPSA tidak efektif untuk depth tinggi, sebaiknya `max_depth` dikunci ke 2 atau 3 saja.
3. **Kurangi `batch_size`** dari 25 ke 5–10.
4. Pertimbangkan **caching Hamiltonian** agar tidak di-rebuild setiap kali.

---

## Masalah 2 — Mengapa energi depth berosilasi, bukan monoton turun lalu naik?

### Pola yang teramati di laporan (contoh 2021-04-06):
```
Depth 1: E = 0.994639  ← terbaik
Depth 2: E = 1.143539  ← naik drastis (+14.9%)
Depth 3: E = 1.009417  ← turun
Depth 4: E = 1.130503  ← naik lagi
```

Pola **naik-turun-naik-turun** (genap selalu lebih buruk dari ganjil) ini adalah gejala struktural, bukan acak.

### Akar masalah #1: Warm-start yang tidak kompatibel (baris 99–100 `run_vqe_adaptive.py`)

```python
if prev_params is not None and len(prev_params) < n_params:
    init_p = np.concatenate([prev_params, rng.uniform(-0.1, 0.1, n_params - len(prev_params))])
```

Saat depth naik dari `d` ke `d+1`, jumlah parameter bertambah dari `n_qubits * 2 * (d+1)` ke `n_qubits * 2 * (d+2)`. Parameter baru **ditempel di akhir** vektor.

Masalahnya adalah parameter `w` di-reshape sebagai `(depth+1, n_qubits, 2)`:
- Depth 1 → shape `(2, 2, 2)` = 8 parameter
- Depth 2 → shape `(3, 2, 2)` = 12 parameter

Ketika 8 parameter depth-1 dipakai untuk depth-2, layer baru (`layer[2]`) mendapat parameter random kecil (`±0.1`), **bukan di posisi layer terakhir yang logis**. Akibatnya setiap kenaikan depth memulai dari posisi yang "rusak".

### Akar masalah #2: Learning rate menyusut per depth

```python
# baris 110
params, energy, e_hist, n_iters = run_spsa(
    ..., a_base=best_a_base/depth, ...
)
```

Depth 2 memakai `LR/2`, depth 4 memakai `LR/4`. Semakin dalam ansatz, LR **makin kecil**, sehingga SPSA tidak punya "tenaga" untuk keluar dari local minimum yang buruk akibat warm-start yang salah di atas.

### Akar masalah #3: Tidak ada reset parameter saat warm-start gagal

Tidak ada mekanisme fallback ke inisialisasi random ketika energy depth baru **lebih buruk** dari depth sebelumnya. Harusnya jika energy naik, coba random restart.

### Solusi yang disarankan

1. **Padding yang benar**: Sisipkan parameter baru di **tengah** (setelah layer ke-`d`, sebelum layer terakhir), bukan di akhir.
2. **Pertahankan LR** antar depth atau naikkan sedikit saat depth bertambah (bukan dibagi).
3. **Tambahkan restart** jika `energy_depth_baru > energy_depth_sebelumnya`.

---

## Masalah 3 — Double counting pada `Q_off` di perhitungan `C_Ising`

### Temuan: Ada **dua inkonsistensi** sekaligus

#### Bug A — `Q_off` disimpan sebagai matriks simetris (baris 71–73)
```python
Q_val = (gamma * sigma_period_matrix[i, j]) / (2.0 * K_sq) + lam
Q_off[i, j] = Q_val
Q_off[j, i] = Q_val   # ← simetris, dihitung dua kali
```

#### Bug B — `C_Ising` menjumlahkan semua `i != j` (bukan hanya `i < j`) di baris 96–99:
```python
for i in range(n_assets):
    for j in range(n_assets):
        if i != j:
            sum_Q_ij_fourth_total += Q_off[i, j] / 4.0  # menghitung Q_ij DAN Q_ji
```

Karena `Q_off` simetris, suku ini menjumlahkan setiap pasang (i,j) **dua kali**. Rumus yang benar di README adalah:

$$C_{\text{Ising}} = \sum_i \frac{Q_{ii}}{2} + \sum_{i<j} \frac{Q_{ij}}{2} + \lambda K^2$$

Tapi kode mengimplementasikan `sum_{i≠j} Q_ij/4 = sum_{i<j} Q_ij/2` — **secara matematis setara!**

Jadi ada `bug semu`: meski loopnya `i != j` (menghitung dua kali), hasilnya dibagi 4, yang ekuivalen dengan menghitung `i < j` dibagi 2. **Jadi nilai `C_Ising` akhirnya benar.**

#### Namun ada bug nyata di `h_total` baris 81–84:
```python
sum_Q_ij_half = 0.0
for j in range(n_assets):
    if i != j:
        sum_Q_ij_half += Q_off[i, j] / 2.0  # menjumlahkan i dan j terbalik juga benar
```

Ini benar karena Q_off[i,j] = Q_off[j,i], dan yang dijumlahkan adalah seluruh baris ke-i (semua j ≠ i), konsisten dengan rumus $h_i = Q_{ii}/2 + \sum_{j \neq i} Q_{ij}/2$.

### Kesimpulan Masalah 3

**Tidak ada double-counting yang menyebabkan error nilai**. Ini "false alarm". Namun kode bisa disederhanakan agar lebih jelas:

```python
# Ganti loop i!=j dengan i<j dan bagi 2 (lebih eksplisit sesuai rumus):
for i in range(n_assets):
    for j in range(i + 1, n_assets):
        sum_Q_ij_fourth_total += Q_off[i, j] / 2.0   # i<j, dibagi 2 (sesuai README)
```

---

## Masalah 4 — Apakah iterasi per depth sudah benar?

### Pertanyaan inti: Apakah depth seharusnya jadi loop luar atau loop dalam?

Melihat kode `run_vqe_adaptive.py`:

```python
# Loop luar: depth (baris 95)
for depth in range(1, max_depth + 1):
    # Loop dalam: SPSA di dalam run_spsa (baris 64)
    while total_iters < max_total_iter:
        for _ in range(batch_size):
            ...
```

Ini berarti: untuk setiap depth, SPSA dijalankan hingga konvergen atau `max_total_iter`. Setelah depth-d selesai, baru lanjut ke depth-d+1. **Ini adalah Adaptive Depth VQE yang benar** sesuai Algorithm 2 di README.

### Namun ada masalah struktur di `backtest_runner.py` baris 50:

```python
selected_indices, depth_used, energy_final, best_history, depth_energies, lr_data, ne_bs, ne_utility = run_strategy_step(
    train_data, tickers, curr_date, K=K, penalty_A=penalty_A, max_depth=max_depth, maxiter=maxiter
)
```

Parameter `max_total_iter`, `batch_size`, `conv_window`, `conv_tol` **tidak diteruskan** dari `config` ke `run_strategy_step`. Mereka menggunakan nilai default di signature fungsi:

```python
def run_strategy_step(..., max_total_iter=2000, batch_size=25, conv_window=4, conv_tol=1e-4):
```

Ini bukan bug fatal, tapi artinya kamu tidak bisa mengontrol parameter konvergensi dari `config` di `main.py`.

### Masalah di `run_vqe_adaptive.py` baris 83:

```python
if total_iters >= maxiter and len(energy_history) >= conv_window:
```

Kondisi `total_iters >= maxiter` menggunakan `maxiter=100` (dari `run_strategy_step`). Tapi `total_iters` adalah hitungan **total kumulatif** sejak mulai iterasi, bukan per batch. Jadi untuk batch_size=25, cek konvergensi baru aktif setelah **4 batch** (100/25 = 4 kali). Ini OK.

### Kesimpulan Masalah 4

Struktur depth sebagai **loop luar** sudah **benar** secara algoritma (sesuai README). Yang perlu diperbaiki adalah meneruskan semua parameter konfigurasi dari `main.py → backtest_runner → run_strategy_step → run_vqe_adaptive`.

---

## Masalah 5 — Mengapa persamaan di README.md tidak render di GitHub?

### Diagnosis: GitHub hanya mendukung LaTeX **sejak Mei 2022**, dengan syarat tertentu

GitHub merender LaTeX via MathJax dengan sintaks:
- Inline: `$...$`  
- Block: `$$...$$` (dengan baris kosong sebelum dan sesudah)

### Masalah yang ditemukan di README.md:

#### Masalah A — HTML entities di antara formula (baris 61, 77, 78)
```markdown
$$\mathbf{x}^{q+1} \triangleq \arg \max_{\mathbf{x} \in \mathcal{S}(\mathbf{x}^q)} U(\mathbf{x})$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;di mana ...
$$\hat{g}_k(\boldsymbol{\theta}) \triangleq ...$$  
```
`&nbsp;` adalah HTML entity — di beberapa renderer GitHub, ini **memutus blok LaTeX** dan mencegah rendering.

#### Masalah B — Tanda `***` sebagai pemisah (baris 54, 56, 63, 69, 71, 81)
```markdown
***
**Algorithm 1. ...**
***
```
`***` di Markdown adalah `<hr>` (garis horizontal). Namun bila diapit teks tebal, beberapa parser memperlakukannya sebagai `italic+bold` marker yang gagal di-parse, sehingga blok di sekitarnya tidak dirender dengan benar.

#### Masalah C — Block formula tanpa baris kosong yang jelas
Beberapa `$$...$$` tidak memiliki **baris kosong di atas dan di bawahnya**, yang diperlukan GitHub agar memperlakukannya sebagai math block.

### Perbaikan yang diperlukan

1. Ganti `&nbsp;` dengan spasi/indentasi markdown biasa atau hapus.
2. Ganti `***` pemisah algoritma dengan `---` (horizontal rule standar).
3. Pastikan setiap `$$...$$` diawali dan diakhiri dengan **baris kosong**.
4. Untuk persamaan multi-baris, gunakan `$$\begin{aligned}...\end{aligned}$$`.

### Contoh perbaikan baris 77–78:

```markdown
<!-- SEBELUM (bermasalah) -->
$$\boldsymbol{\theta}_{d,k+1} = \boldsymbol{\theta}_{d,k} - a_k \hat{g}_k(\boldsymbol{\theta}_{d,k})$$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;di mana estimasi gradien $\hat{g}_k$ didefinisikan sebagai:
$$\hat{g}_k(\boldsymbol{\theta}) \triangleq \frac{E(...) - E(...)}{2 c_k \boldsymbol{\Delta}_k}$$  

<!-- SESUDAH (benar) -->
$$\boldsymbol{\theta}_{d,k+1} = \boldsymbol{\theta}_{d,k} - a_k \hat{g}_k(\boldsymbol{\theta}_{d,k})$$

di mana estimasi gradien $\hat{g}_k$ didefinisikan sebagai:

$$\hat{g}_k(\boldsymbol{\theta}) \triangleq \frac{E(\boldsymbol{\theta} + c_k \boldsymbol{\Delta}_k) - E(\boldsymbol{\theta} - c_k \boldsymbol{\Delta}_k)}{2 c_k \boldsymbol{\Delta}_k}$$
```

---

## Ringkasan

| # | Masalah | Tingkat Keparahan | Status |
|---|---|---|---|
| 1 | Kode lambat: LR Finder + VQE = ratusan ribu eval | 🔴 Tinggi | Perlu optimasi |
| 2 | Osilasi energi antar depth: warm-start salah + LR menyusut | 🔴 Tinggi | Perlu perbaikan padding & LR |
| 3 | Double counting Q_off di C_Ising | 🟡 Tidak berdampak numerik | Kode benar tapi perlu klarifikasi |
| 4 | Struktur iterasi depth sudah benar (loop luar) | 🟢 Benar | Parameter config perlu diteruskan |
| 5 | LaTeX tidak render di GitHub: `&nbsp;` + `***` + baris kosong | 🟡 Medium | Perlu revisi README.md |
