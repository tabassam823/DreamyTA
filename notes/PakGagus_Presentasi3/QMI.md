# Quantum Mutual Information (QMI) & Ekstraksi Parameter Interaksi
## 1. Apa itu Quantum Mutual Information (QMI)?

Dalam teori informasi kuantum, **QMI** adalah ukuran korelasi total (baik korelasi klasik maupun korelasi kuantum/entanglement) antara dua subsistem dalam sebuah sistem kuantum yang lebih besar.

Jika kita memiliki dua buah spin (atau qubit) $i$ dan $j$, QMI di antara keduanya didefinisikan menggunakan **[[Kritik]] ($S$)**:

$$I(i:j) = S(
ho_i) + S(
ho_j) - S(
ho_{ij})$$

Di mana:
- $ho_i, ho_j$: Matriks densitas terreduksi (reduced density matrix) dari spin $i$ dan $j$.
- $ho_{ij}$: Matriks densitas gabungan dari kedua spin tersebut.
- $S(ho) = -	\text{Tr}(ho \ln{ho})$: Entropi Von Neumann.

## 2. Mengapa QMI Digunakan untuk Mencari $J_{ij}$?

Dalam masalah **Inverse Ising Problem** atau **Hamiltonian Learning**, tujuannya adalah membalikkan proses fisika: kita memiliki data (hasil pengukuran spin) dan ingin mencari Hamiltonian ($h_i$ dan $J_{ij}$) yang menghasilkan data tersebut.

**Parameter Interaksi ($J_{ij}$)** mencerminkan seberapa kuat dua spin saling memengaruhi. Hubungan antara QMI dan $J_{ij}$ didasarkan pada prinsip-prinsip berikut:

### A. Deteksi Konektivitas
QMI memberikan nilai yang mencerminkan "kedekatan" informasi antara dua titik. Jika $I(i:j)$ bernilai besar, maka terdapat interaksi yang kuat ($J_{ij}$ besar) atau jalur korelasi yang signifikan di antara mereka.

### B. Prinsip Maksimum Entropi (Max-Ent)
Dalam statistik, kita dapat menunjukkan bahwa parameter interaksi $J_{ij}$ berkaitan dengan korelasi dua titik ($C_{ij} = \langle s_i s_j 
angle - \langle s_i 
angle \langle s_j 
angle$). Karena QMI adalah ukuran korelasi yang lebih umum (mencakup aspek non-linear dan kuantum), QMI sering digunakan sebagai "proksi" atau alat bantu untuk menentukan besarnya kopling dalam sistem yang sangat terjerat (*entangled*).

## 3. Prosedur Ekstraksi (Secara Umum)

Secara detail, langkah-langkah untuk mendapatkan $J_{ij}$ menggunakan QMI adalah:

1.  **Persiapan State**: Siapkan sistem kuantum (misalnya melalui simulasi atau eksperimen) pada keadaan tertentu (misalnya *ground state* atau *thermal state*).
2.  **Tomografi / Pengukuran**: Lakukan pengukuran untuk mendapatkan matriks densitas $
ho_{ij}$ untuk setiap pasangan spin.
3.  **Hitung QMI**: Hitung nilai $I(i:j)$ untuk seluruh pasangan dalam sistem.
4.  **Pemetaan ke Hamiltonian**: 
    - Gunakan algoritma optimasi untuk mencari set $\{J_{ij}\}$ yang meminimalkan perbedaan antara korelasi yang diprediksi model dengan nilai QMI yang diobservasi.
    - Dalam beberapa pendekatan numerik, $J_{ij}$ dianggap berbanding lurus dengan fungsi dari $I(i:j)$ pada jarak pendek.

## 4. Keunggulan Menggunakan QMI

1.  **Menangkap Korelasi Kuantum**: Berbeda dengan *Mutual Information* klasik, QMI mampu menangkap efek *entanglement* yang tidak terdeteksi oleh korelasi statistik biasa.
2.  **Robust terhadap Noise**: QMI cenderung lebih stabil dalam mendeteksi struktur jaringan interaksi pada sistem kuantum yang memiliki gangguan (noise).
3.  **Aplikasi pada Machine Learning**: Dalam *Quantum Neural Networks*, QMI sering digunakan sebagai fungsi biaya (*loss function*) untuk memastikan informasi mengalir dengan benar melalui parameter interaksi yang dipelajari.

## 5. Kesimpulan

QMI adalah alat diagnostik yang sangat kuat dalam fisika kuantum. Dengan menganalisis bagaimana informasi "dibagi" di antara spin, kita dapat merekonstruksi struktur Hamiltonian dan menentukan besarnya parameter interaksi **$J_{ij}$** secara akurat, bahkan dalam sistem yang sangat kompleks.
