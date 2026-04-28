# Metodologi Penelitian: Implementasi qPCA pada Model Heath-Jarrow-Morton (HJM)

Dokumen ini merinci urutan metodologi yang digunakan dalam paper *"Toward pricing financial derivatives with an IBM quantum computer"* (Phys. Rev. Research 3, 013167), mulai dari akuisisi data hingga ekstraksi hasil pada platform komputasi kuantum.

## 1. Persiapan Data dan Penyandian (Classical Setup)
Tahap awal melibatkan pengolahan data historis pasar keuangan untuk membangun fondasi stokastik model.
- **Konstruksi Matriks Kovarians:** Menghitung matriks korelasi silang $\sigma$ dari perubahan *forward rates*.
- **Normalisasi Density Matrix:** Mengubah matriks menjadi $\rho$ dengan syarat $\text{tr}[\rho] = 1$ agar dapat dipetakan ke sirkuit kuantum.
- **Unitary Encoding:** Menyandi matriks $\rho$ ke dalam operator evolusi waktu $U = e^{2\pi i \rho}$.

## 2. Tahap I: Estimasi Eigenvector Iteratif
Karena vektor eigen tidak diketahui secara *a priori*, digunakan protokol iteratif untuk mengisolasinya.
- **Inisialisasi:** Memulai dengan *random state* $|b_0\rangle$.
- **Protokol Iteratif:** Menerapkan evolusi uniter dan proyeksi pada estimasi biner $n$-bit untuk eigenvalue tertinggi.
- **Konvergensi:** Hasil pengukuran diumpankan kembali (*feedback*) sebagai input iterasi berikutnya hingga vektor eigen $|u_{max}\rangle$ stabil.

## 3. Estimasi Fase dan Refinement (Quantum Execution)
Setelah vektor eigen kasar didapatkan, dilakukan penyempurnaan akurasi.
- **Rotasi Basis:** Melakukan pengukuran pada basis $x, y, \text{dan } r$ untuk menentukan fase kompleks relatif antar qubit.
- **Tahap II (Refinement):** Menggunakan vektor eigen yang telah dikonvergensi sebagai input untuk algoritma *Quantum Phase Estimation* (QPE) dengan presisi bit yang lebih tinggi guna mendapatkan eigenvalue $\lambda_{max}$ yang akurat.

## 4. Mitigasi Galat dan Hasil Akhir
Langkah terakhir untuk menjamin integritas data pada sistem NISQ (*Noisy Intermediate-Scale Quantum*).
- **Error Mitigation:** Menggunakan *Richardson's extrapolation* dan teknik mitigasi galat pembacaan (*readout error mitigation*).
- **Outcome Akhir:** Ekstraksi komponen utama (eigenvalue dan eigenvector) yang akan digunakan sebagai input profil volatilitas dalam simulasi model HJM untuk penetapan harga derivatif.

## 5. Diagram Alir Metodologi

```mermaid
graph TD
    Start([Mulai]) --> A[Data Historis Forward Rates]
    A --> B[Konstruksi Matriks Kovarians sigma]
    B --> C[Normalisasi Density Matrix rho, tr=1]
    C --> D[Penyandian rho ke Operator Uniter U]
    D --> E[Inisialisasi Register & State b0]
    
    subgraph T1 [Tahap I: Estimasi Eigenvector Iteratif]
        E --> F[Evolusi Uniter & QFT]
        F --> G[Proyeksi pada Estimasi Biner y_n]
        G --> H{Stabil/Konvergen?}
        H -->|Belum: Feedback State| F
        H -->|Ya| I[Isolasi Vektor Eigen u_max]
    end
    
    subgraph T2 [Tahap II: Refinement Eigenvalue]
        I --> J[Rotasi Basis x, y, r & Fase Relatif]
        J --> K[Refinement Eigenvalue QPE]
        K --> L[Mitigasi Galat & Richardson Extrapolation]
    end
    
    L --> M[Hasil Akhir: Komponen Utama HJM]
    M --> End([Selesai])
    
    style T1 fill:#f9f,stroke:#333,stroke-width:2px
    style T2 fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Start fill:#ddd,stroke:#333,stroke-width:2px
    style End fill:#ddd,stroke:#333,stroke-width:2px
```
