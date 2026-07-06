# Evaluasi Performa & Strategi Optimasi: Kode Lokal vs PDF Reference

Dokumen ini memberikan analisis mendalam mengenai penyebab perbedaan kecepatan eksekusi antara kode lokal yang berbasis PennyLane dan kode referensi pada `Hamiltonian_Markowitz.pdf` yang berbasis Numba, serta memberikan saran konkret untuk perbaikan.

---

## 1. Perbandingan Arsitektur Komputasi

| Fitur | Kode Lokal (`main.py` & `run_vqe_adaptive.py`) | Kode PDF (`Hamiltonian_Markowitz.pdf`) | Dampak Performa |
| :--- | :--- | :--- | :--- |
| **Engine Simulasi** | **PennyLane (`default.qubit`)** | **NumPy + Numba (`@njit`)** | **Sangat Tinggi**. PennyLane memiliki overhead framework; Numba mengkompilasi ke bahasa mesin. |
| **Metode Gate** | Abstraksi QNode (Objek Python) | Manual Matrix Multiplication (`@`, `np.kron`) | **Tinggi**. Untuk $N=2$, overhead objek QNode > waktu kalkulasi matriks itu sendiri. |
| **Optimasi SPSA** | Iteratif per Depth (1 s/d 6) | Iteratif per Depth (Fixed array 28 params) | **Sedang**. Kode lokal melakukan inisialisasi ulang array di setiap depth. |
| **Limit Iterasi** | `max_total_iter = 2000` | `n_iterations = 500` | **Tinggi**. Kode lokal melakukan 4x lebih banyak iterasi jika tidak konvergen. |
| **Proses Tambahan** | LR Finder (8 x 30 iterasi SPSA) | Tidak ada (Fixed Hyperparameters) | **Sedang**. LR Finder menambah beban di setiap jendela backtest. |

---

## 2. Identifikasi Bottleneck Utama

### A. Framework Overhead (The "PennyLane Cost")
Pada sistem kecil ($N=2$, $N=4$), waktu yang dibutuhkan komputer untuk "mempersiapkan" sirkuit di PennyLane (parsing sirkuit, manajemen memori, tracking gradien) jauh lebih lama daripada waktu untuk mengalikan matriks $4 \times 4$. PDF menggunakan Numba yang menghilangkan lapisan persiapan ini.

### B. Iterasi Berlebihan pada Backtesting
Dalam backtesting, optimasi VQE dijalankan setiap kali ada jendela rebalancing (misal setiap 21 hari).
*   Jika backtest berjalan 3 tahun $\approx$ 36 jendela.
*   Total simulasi lokal: $36 \text{ jendela} \times 6 \text{ depth} \times 2000 \text{ iterasi} = 432.000$ panggilan sirkuit.
*   Dengan PennyLane, ini bisa memakan waktu berjam-jam. Dengan Numba, ini selesai dalam hitungan detik.

---

## 3. Saran Perubahan (Action Plan)

### Opsi 1: Optimasi "Hard" (Migrasi ke Numba)
*Jika kecepatan adalah prioritas utama dan jumlah aset ($N$) kecil.*

1.  **Ganti PennyLane dengan NumPy Manual**: Implementasikan fungsi `get_psi_theta` menggunakan matriks rotasi manual seperti pada halaman 16 PDF.
2.  **Gunakan Dekorator `@njit`**: Bungkus fungsi `cost_function`, `get_psi_theta`, dan `run_SPSA` dengan Numba.
3.  **Hapus Objek QNode**: Gunakan perkalian matriks standar (`@`) untuk operasi gate.

### Opsi 2: Optimasi "Soft" (Tuning PennyLane)
*Jika ingin tetap menggunakan PennyLane agar mudah diupgrade ke hardware quantum nantinya.*

1.  **Ganti Device**: Gunakan `lightning.qubit` bukan `default.qubit`.
    ```python
    dev = qml.device("lightning.qubit", wires=n_qubits)
    ```
2.  **Gunakan `qml.Snapshot` atau JIT**: Jika memungkinkan, gunakan `jax` atau `torch` sebagai interface PennyLane untuk kompilasi JIT.
3.  **Turunkan Limit Iterasi**:
    *   Ubah `max_total_iter` dari 2000 menjadi **500**.
    *   Ubah `batch_size` SPSA dari 25 menjadi **10** atau **5**.
4.  **Optimasi LR Finder**:
    *   LR Finder tidak perlu dijalankan di setiap jendela backtest. Cari LR optimal sekali saja di awal, lalu gunakan nilai tersebut untuk seluruh periode.

### Opsi 3: Efisiensi Algoritma
1.  **Early Stopping yang Lebih Agresif**: Tingkatkan `conv_tol` (misal dari `1e-4` ke `1e-3`) agar SPSA berhenti lebih cepat saat energi sudah stabil.
2.  **Memoization**: Simpan hasil Hamiltonian jika data pasar tidak berubah signifikan (jarang terjadi di backtest, tapi berguna untuk testing).

---

## 4. Contoh Perubahan Struktur Kode (Strategi PDF)

Untuk mencapai kecepatan PDF, struktur loop di `run_vqe_adaptive.py` sebaiknya diubah dari:
```python
# SEKARANG (Lambat)
for depth in range(1, max_depth + 1):
    # run_spsa panggil QNode berkali-kali dalam loop Python
    params, energy = run_spsa(cost_fn, ...) 
```

Menjadi (Mengikuti Logika PDF):
```python
# SARAN (Cepat - Numba-style)
@njit
def optimized_spsa(H_matrix, n_iterations, ...):
    theta = np.random.rand(28) # Fixed size
    for k in range(n_iterations):
        # Hitung gradien dengan matrix-vector multiplication langsung
        # Tidak ada overhead objek Python
        ...
    return theta
```

---

## Kesimpulan
Penyebab utama kelambatan adalah penggunaan framework **PennyLane** untuk simulasi skala kecil yang dijalankan berulang kali dalam loop backtest. Mengadopsi pendekatan **Numba + NumPy** seperti pada PDF akan meningkatkan kecepatan hingga **10x - 100x lipat** untuk kasus $N=2$ hingga $N=8$.
