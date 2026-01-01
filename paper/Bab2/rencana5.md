# Rencana Revisi Bab 2: Langkah 5 (Integrasi Fisika Statistik & Komputasi)

**Tujuan:** Mengintegrasikan sub-bab Fisika Statistik dan Komputasi agar memiliki alur yang koheren dengan narasi Teori Permainan dan Ekonomi, sesuai saran pada `Saran_Pengeditan_Bab_2.md` poin 5.

**Referensi:**
*   `Bab2/Saran_Pengeditan_Bab_2.md` (Poin 5)
*   `Bab2/Bab2.md` (Sub-bab 2.2 dan 2.3 saat ini)

### Langkah Kerja:

1.  **Refactoring Sub-bab 2.2 (Fisika Statistik dan Sistem Kompleks):**
    *   **Judul Baru:** Ubah judul menjadi yang lebih integratif, misal: **"Fisika Statistik dalam Pemodelan Pasar dan Optimasi"**.
    *   **2.2.1 Model Ising:**
        *   Pertegas narasi bahwa Model Ising bukan hanya model feromagnetisme, tapi **analogi langsung** untuk interaksi agen ekonomi (spin up/down = beli/jual).
        *   Hubungkan *Ground State* Hamiltonian Ising secara eksplisit dengan **Nash Equilibrium** atau solusi optimal dalam *Game Theory* (sudah dimulai di langkah sebelumnya, tapi perlu diperhalus alurnya).
    *   **2.2.2 Proses Stokastik (GBM) & 2.2.3 Fraktal:**
        *   Bingkai GBM dan Fraktal bukan sekadar model harga aset, tapi sebagai **deskripsi lingkungan (environment)** atau *noise* di mana permainan ekonomi berlangsung.
        *   Ini menjadi landasan mengapa kita butuh *Mixed Strategy* (probabilitas) dan *Matriks Densitas* (ketidakpastian).

2.  **Refactoring Sub-bab 2.3 (Metode Komputasi dan Numerik):**
    *   **Judul Baru:** Ubah judul menjadi **"Metode Solusi Komputasi untuk Ekuilibrium Ekonomi"**.
    *   **2.3.1 Monte Carlo & 2.3.4 QAOA:**
        *   Gabungkan atau hubungkan narasi: Monte Carlo adalah cara klasik mencari ekuilibrium/solusi, sedangkan QAOA adalah cara kuantum mencari *Ground State* (solusi optimal) dari Hamiltonian Ising yang merepresentasikan masalah ekonomi tersebut.
    *   **2.3.2 BSDE & 2.3.3 Curse of Dimensionality:**
        *   Jelaskan bahwa ini adalah teknik untuk menyelesaikan masalah *pricing* yang kompleks (dimensi tinggi) yang muncul dari model pasar yang telah didefinisikan sebelumnya (LMM).

3.  **Restrukturisasi Alur (Flow):**
    *   Pastikan transisi antar sub-bab terasa natural:
        *   Masalah Ekonomi (Game Theory) -> Dimodelkan dengan Fisika (Ising/Hamiltonian) -> Di dalam lingkungan yang tidak pasti (Stokastik/Fraktal) -> Diselesaikan dengan Metode Komputasi (Monte Carlo/QAOA/BSDE).

4.  **Implementasi Teknis:**
    *   Gunakan `replace` untuk mengubah judul dan narasi penghubung pada `Bab2/Bab2.md`.
