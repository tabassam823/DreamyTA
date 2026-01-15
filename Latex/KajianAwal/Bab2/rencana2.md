# Rencana Lanjutan untuk Revisi Bab 2: Langkah 2

## Gaya Paragraf: Deduktif vs. Induktif dengan Studi Kasus

**Tujuan:** Mengubah gaya paragraf pengantar di sub-bab 2.1.1 `Bab2/Bab2.md` dari deduktif-deskriptif menjadi induktif-eksploratif, dengan menggunakan studi kasus sebagai pancingan untuk memperkenalkan konsep.

### Langkah-langkah:
1.  **Identifikasi Paragraf Target:** Temukan paragraf pengantar di sub-bab `2.1.1 Ruang Hilbert, Superposisi, dan Sistem Qubit vs Qutrit` pada file `Bab2/Bab2.md`.
    *   **Saat ini:** "Sebagai pengantar induktif untuk memahami kebutuhan akan sistem kuantum berdimensi tinggi, kita dapat meninjau kasus **prediksi pasar saham secara *real-time*** (Bakshi & Srinivasan, 2025). Dalam memodelkan dinamika pasar yang kompleks (seperti data indeks NIFTY 50), penggunaan sistem biner klasik atau bahkan sistem kuantum dua-level (**qubit**) sering kali menghadapi keterbatasan dalam merepresentasikan data kontinu tanpa kehilangan informasi signifikan akibat *discretization error*. Struktur data pasar yang kaya memerlukan kapasitas representasi yang lebih padat daripada yang dapat ditawarkan oleh qubit tunggal."

2.  **Susun Ulang Alur Narasi (Induktif):**
    *   Mulai dengan memperkenalkan **masalah konkret** (prediksi pasar saham real-time/NIFTY 50) dan tantangannya (data kontinu, *discretization error*).
    *   **Tekankan keterbatasan** sistem klasik/qubit dalam mengatasi masalah ini.
    *   **Ciptakan kebutuhan** akan representasi informasi yang lebih besar/padat.
    *   **Perkenalkan qutrit** sebagai solusi untuk mengatasi keterbatasan tersebut, menyoroti "keunggulan kuantum" yang ditawarkannya.
    *   **Baru kemudian** masuk ke definisi formal dan matematis qutrit dan ruang Hilbert.

3.  **Implementasi (Menggunakan `replace` tool):**
    *   Buat `old_string` yang mencakup paragraf pengantar lama di `Bab2/Bab2.md`.
    *   Buat `new_string` yang berisi paragraf yang telah disusun ulang dengan gaya induktif, dimulai dari masalah dan diakhiri dengan memperkenalkan solusi qutrit sebelum definisi formal.
    *   Perbarui file `Bab2/Bab2.md` menggunakan `replace` tool.
