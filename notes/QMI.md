	# Quantum Mutual Information (QMI) & Ekstraksi Parameter Interaksi
## 1. Apa itu Quantum Mutual Information (QMI)?

Dalam teori informasi kuantum, **QMI** adalah ukuran korelasi total (baik korelasi klasik maupun korelasi kuantum/entanglement) antara dua subsistem dalam sebuah sistem kuantum yang lebih besar.

Jika kita memiliki dua buah spin (atau qubit) $i$ dan $j$, QMI di antara keduanya didefinisikan menggunakan **[[Von Neumann Entropy]] ($S$)**:

$$I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij})$$

Di mana:
- $\rho_i, \rho_j$: Matriks densitas terreduksi (reduced density matrix) dari spin $i$ dan $j$.
- $\rho_{ij}$: Matriks densitas gabungan dari kedua spin tersebut.
- $S(\rho) = -	\text{Tr}(\rho \ln{\rho})$: Entropi Von Neumann.

## 2. Mengapa QMI Digunakan untuk Mencari $J_{ij}$?

Dalam masalah **Inverse Ising Problem** atau **Hamiltonian Learning**, tujuannya adalah membalikkan proses fisika: kita memiliki data (hasil pengukuran spin) dan ingin mencari Hamiltonian ($h_i$ dan $J_{ij}$) yang menghasilkan data tersebut.

**Parameter Interaksi ($J_{ij}$)** mencerminkan seberapa kuat dua spin saling memengaruhi. Hubungan antara QMI dan $J_{ij}$ didasarkan pada prinsip-prinsip berikut:

### A. Deteksi Konektivitas
QMI memberikan nilai yang mencerminkan "kedekatan" informasi antara dua titik. Jika $I(i:j)$ bernilai besar, maka terdapat interaksi yang kuat ($J_{ij}$ besar) atau jalur korelasi yang signifikan di antara mereka.

### B. Prinsip Maksimum Entropi (Max-Ent)
Dalam statistik, kita dapat menunjukkan bahwa parameter interaksi $J_{ij}$ berkaitan dengan korelasi dua titik ($C_{ij} = \langle s_i s_j \rangle - \langle s_i \rangle \langle s_j \rangle$). Karena QMI adalah ukuran korelasi yang lebih umum (mencakup aspek non-linear dan kuantum), QMI sering digunakan sebagai "proksi" atau alat bantu untuk menentukan besarnya kopling dalam sistem yang sangat terjerat (*entangled*).

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

## 5. Contoh Perhitungan Matriks Densitas

Untuk memahami bagaimana QMI dihitung secara praktis, bayangkan kita memiliki sebuah *pure state* (keadaan murni) $|\psi\rangle$ untuk sistem dua qubit:

$$|\psi\rangle = \alpha_{00} |00\rangle + \alpha_{01} |01\rangle + \alpha_{10} |10\rangle + \alpha_{11} |11\rangle$$

Di mana $\sum_{ij} |\alpha_{ij}|^2 = 1$. Langkah-langkah untuk mendapatkan matriks densitasnya adalah:

### A. Matriks Densitas Gabungan $\rho_{ij}$
Matriks ini diperoleh dari *outer product* $|\psi\rangle\langle\psi|$:

$$\rho_{ij} = \begin{pmatrix} 
|\alpha_{00}|^2 & \alpha_{00}\alpha_{01}^* & \alpha_{00}\alpha_{10}^* & \alpha_{00}\alpha_{11}^* \\ 
\alpha_{01}\alpha_{00}^* & |\alpha_{01}|^2 & \alpha_{01}\alpha_{10}^* & \alpha_{01}\alpha_{11}^* \\ 
\alpha_{10}\alpha_{00}^* & \alpha_{10}\alpha_{01}^* & |\alpha_{10}|^2 & \alpha_{10}\alpha_{11}^* \\ 
\alpha_{11}\alpha_{00}^* & \alpha_{11}\alpha_{01}^* & \alpha_{11}\alpha_{10}^* & |\alpha_{11}|^2 
\end{pmatrix}$$

### B. Matriks Densitas Terreduksi $\rho_i$ (Partial Trace terhadap qubit $j$)
Kita menjumlahkan elemen-elemen yang berkaitan dengan qubit kedua ($j$):

$$\rho_i = \text{Tr}_j(\rho_{ij}) = \begin{pmatrix} 
|\alpha_{00}|^2 + |\alpha_{01}|^2 & \alpha_{00}\alpha_{10}^* + \alpha_{01}\alpha_{11}^* \\ 
\alpha_{10}\alpha_{00}^* + \alpha_{11}\alpha_{01}^* & |\alpha_{10}|^2 + |\alpha_{11}|^2 
\end{pmatrix}$$

### C. Matriks Densitas Terreduksi $\rho_j$ (Partial Trace terhadap qubit $i$)
Kita menjumlahkan elemen-elemen yang berkaitan dengan qubit pertama ($i$):

$$\rho_j = \text{Tr}_i(\rho_{ij}) = \begin{pmatrix} 
|\alpha_{00}|^2 + |\alpha_{10}|^2 & \alpha_{00}\alpha_{01}^* + \alpha_{10}\alpha_{11}^* \\ 
\alpha_{01}\alpha_{00}^* + \alpha_{11}\alpha_{10}^* & |\alpha_{01}|^2 + |\alpha_{11}|^2 
\end{pmatrix}$$

> **Mengapa notasi Trace-nya tampak terbalik?**
> Secara konseptual, $\rho_i$ adalah "apa yang tersisa" dari sistem setelah kita mengabaikan informasi pada qubit $j$. Notasi $\text{Tr}_j$ berarti kita melakukan operasi penjumlahan (rata-rata) terhadap semua kemungkinan status pada qubit $j$. Jadi, untuk mendapatkan matriks milik $i$, kita harus "membuang" (trace-out) si $j$. Begitu pula sebaliknya.

Setelah mendapatkan $\rho_{ij}$, $\rho_i$, dan $\rho_j$, kita dapat menghitung masing-masing entropi Von Neumann untuk mendapatkan nilai $I(i:j)$. Perlu dicatat bahwa untuk *pure state*, $S(\rho_{ij}) = 0$, sehingga $I(i:j) = S(\rho_i) + S(\rho_j)$.

### D. Kasus Mixed State (Keadaan Campuran)
Jika sistem berada dalam *mixed state* (misalnya karena gangguan termal atau noise), $\rho_{ij}$ tidak dapat dinyatakan sebagai satu vektor tunggal $|\psi\rangle$, melainkan sebagai kombinasi statistik:
$$\rho_{ij} = \sum_k p_k |\psi_k\rangle\langle\psi_k|$$

> **Apa makna $p_k$ dan bagaimana syarat Hermitian/Trace terpenuhi?**
> $p_k$ adalah probabilitas klasik bahwa sistem berada pada state $|\psi_k\rangle$. Karena ini adalah probabilitas, maka $\sum p_k = 1$ dan $p_k \ge 0$.
> 1. **Hermitian**: Karena setiap komponen $|\psi_k\rangle\langle\psi_k|$ adalah hasil kali luar (*outer product*) yang bersifat Hermitian, dan $p_k$ bernilai real, maka jumlahannya pasti Hermitian.
> 2. **Trace = 1**: $\text{Tr}(\rho_{ij}) = \sum p_k \text{Tr}(|\psi_k\rangle\langle\psi_k|)$. Karena setiap $|\psi_k\rangle$ ternormalisasi, maka $\text{Tr}(|\psi_k\rangle\langle\psi_k|) = 1$. Karena $\sum p_k = 1$, maka total trace matriks tersebut adalah 1.
Misalkan kita memiliki $\rho_{ij}$ dalam bentuk matriks umum (yang memenuhi syarat Hermitian dan trace = 1):
$$\rho_{ij} = \begin{pmatrix} 
\rho_{aa} & \rho_{ab} & \rho_{ac} & \rho_{ad} \\ 
\rho_{ba} & \rho_{bb} & \rho_{bc} & \rho_{bd} \\ 
\rho_{ca} & \rho_{cb} & \rho_{cc} & \rho_{cd} \\ 
\rho_{da} & \rho_{db} & \rho_{dc} & \rho_{dd} 
\end{pmatrix}$$

Langkah *partial trace* secara indeks dapat dijabarkan sebagai berikut (mengasumsikan basis $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ berkorespondensi dengan indeks $a, b, c, d$):

1.  **Mencari $\rho_i$ (Trace terhadap Qubit $j$):**
    Kita menjumlahkan elemen yang memiliki status qubit $i$ yang sama, tetapi status qubit $j$ yang berbeda:
    - $(\rho_i)_{00} = \langle 00|\rho_{ij}|00\rangle + \langle 01|\rho_{ij}|01\rangle = \rho_{aa} + \rho_{bb}$
    - $(\rho_i)_{01} = \langle 00|\rho_{ij}|10\rangle + \langle 01|\rho_{ij}|11\rangle = \rho_{ac} + \rho_{bd}$
    - $(\rho_i)_{10} = \langle 10|\rho_{ij}|00\rangle + \langle 11|\rho_{ij}|01\rangle = \rho_{ca} + \rho_{db}$
    - $(\rho_i)_{11} = \langle 10|\rho_{ij}|10\rangle + \langle 11|\rho_{ij}|11\rangle = \rho_{cc} + \rho_{dd}$

    Sehingga: $\rho_i = \begin{pmatrix} \rho_{aa} + \rho_{bb} & \rho_{ac} + \rho_{bd} \\ \rho_{ca} + \rho_{db} & \rho_{cc} + \rho_{dd} \end{pmatrix}$

2.  **Mencari $\rho_j$ (Trace terhadap Qubit $i$):**
    Kita menjumlahkan elemen yang memiliki status qubit $j$ yang sama, tetapi status qubit $i$ yang berbeda:
    - $(\rho_j)_{00} = \langle 00|\rho_{ij}|00\rangle + \langle 10|\rho_{ij}|10\rangle = \rho_{aa} + \rho_{cc}$
    - $(\rho_j)_{01} = \langle 00|\rho_{ij}|01\rangle + \langle 10|\rho_{ij}|11\rangle = \rho_{ab} + \rho_{cd}$
    - $(\rho_j)_{10} = \langle 01|\rho_{ij}|00\rangle + \langle 11|\rho_{ij}|10\rangle = \rho_{ba} + \rho_{dc}$
    - $(\rho_j)_{11} = \langle 01|\rho_{ij}|01\rangle + \langle 11|\rho_{ij}|11\rangle = \rho_{bb} + \rho_{dd}$

    Sehingga: $\rho_j = \begin{pmatrix} \rho_{aa} + \rho_{cc} & \rho_{ab} + \rho_{cd} \\ \rho_{ba} + \rho_{dc} & \rho_{bb} + \rho_{dd} \end{pmatrix}$

**Perbedaan Utama dalam QMI:**
Pada *mixed state*, entropi sistem gabungan **$S(\rho_{ij}) > 0$**. Hal ini mencerminkan adanya ketidakpastian klasik selain korelasi kuantum. Dalam perhitungan QMI:
$$I(i:j) = S(\rho_i) + S(\rho_j) - S(\rho_{ij})$$
Keberadaan $S(\rho_{ij})$ yang bernilai positif ini akan "mengurangi" nilai korelasi total dibandingkan jika sistem tersebut murni, karena sebagian dari entropi subsistem berasal dari keacakan internal sistem itu sendiri, bukan dari interaksi antar subsistem.

## 6. Kesimpulan

QMI adalah alat diagnostik yang sangat kuat dalam fisika kuantum. Dengan menganalisis bagaimana informasi "dibagi" di antara spin, kita dapat merekonstruksi struktur Hamiltonian dan menentukan besarnya parameter interaksi **$J_{ij}$** secara akurat, bahkan dalam sistem yang sangat kompleks.
