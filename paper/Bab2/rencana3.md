# Rencana Revisi Bab 2: Langkah 3 (Protokol Permainan Kuantum)

**Tujuan:** Merestrukturisasi dan memperkaya pembahasan mengenai protokol permainan kuantum agar mengikuti alur konstruktif yang pedagogis, memisahkan definisi alat (matriks densitas) dari metode aplikasinya (Protokol EWL & Marinatto-Weber).

**Referensi:**
*   `Introduction_to_Quantum_Game_Theory.pdf` (Section 6, 7, 8)
*   `Bab2/Bab2.md` (Sub-bab 2.1.3 saat ini)
*   `Bab2/Saran_Pengeditan_Bab_2.md` (Poin 3 dan 4)

### Langkah Kerja:

1.  **Refactoring Sub-bab 2.1.3 (Formalisme Matriks Densitas):**
    *   **Fokus:** Ubah sub-bab ini agar *hanya* membahas definisi matematis Matriks Densitas ($\rho$) dan sifat-sifatnya (seperti *trace*, *mixed state* vs *pure state*).
    *   **Tindakan:** Hapus bagian spesifik tentang protokol Marinatto-Weber dari sub-bab ini (simpan untuk dipindahkan ke 2.1.4). Sisakan definisi $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ dan sifat dasarnya.

2.  **Pembuatan Sub-bab Baru: 2.1.4 Protokol Kuantisasi Permainan:**
    *   **Fokus:** Membahas langkah-langkah umum mengkuantisasi permainan klasik dan dua protokol utama (EWL dan MW).
    *   **Struktur Konten:**
        *   **Pengantar:** Jelaskan secara umum komponen permainan kuantum (Sistem, State Awal, Strategi Uniter, Pengukuran/Payoff).
        *   **Skema Eisert-Wilkens-Lewenstein (EWL):**
            *   Jelaskan penggunaan operator *entanglement* $J$ dan *un-entanglement* $J^\dagger$.
            *   Persamaan state awal: $|\psi_{in}\rangle = J |00\rangle$.
            *   Persamaan state akhir: $|\psi_f\rangle = J^\dagger (U_A \otimes U_B) J |00\rangle$.
        *   **Skema Marinatto-Weber (MW):**
            *   Pindahkan materi MW dari 2.1.3 ke sini.
            *   Jelaskan relevansinya untuk *Mixed Strategy*.
            *   Persamaan evolusi: $\rho_f = U \rho_{in} U^\dagger$.
            *   Payoff: $ = \text{Tr}(P \rho_f)$.

3.  **Penyesuaian Penomoran:**
    *   Sub-bab "Teori Permainan Bayesian..." yang saat ini bernomor **2.1.4** (hasil revisi langkah 1) akan digeser menjadi **2.1.5**.

### Output yang Diharapkan:
Struktur Bab 2.1 akan menjadi:
*   2.1.1 Ruang Hilbert... (Sudah Revisi)
*   2.1.2 Teori Permainan Klasik (Sudah Revisi)
*   2.1.3 Formalisme Matriks Densitas (Hanya definisi alat)
*   2.1.4 Protokol Kuantisasi Permainan (Berisi EWL & MW)
*   2.1.5 Teori Permainan Bayesian...
