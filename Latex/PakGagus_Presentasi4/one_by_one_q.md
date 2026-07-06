# Pertanyaan yang harus bisa dijawab pada file [[one_by_one]] untuk mengisi missing link yang ada
## 1. Bagaimana risk endogen didapatkan?
## 2. Atas dasar apa rumus pencarian bias diperoleh dari marginal ekspektasi
## 3. Bagaimana penurunan rumus QMI sehingga didapat rumus $I(F:L)$
### a. Bagaimana konsep dan penurunan rumus dari fungsi trace (dari mana asalnya)
### b. Bagaimana bisa densitas matriks menjadi parameter utama dalam QMI
### c. Mengapa $\rho_{LF}$ mendekati nol dan bagaimana perhitungan matriksnya?
## 4. Pemetaan Ising Hamiltonian
### a. Bagaimana parameter bias ($h_i$) dan interaksi ($J_{ij}$) disusun menjadi operator `SparsePauliOp` atau matriks Hamiltonian $H = \sum h_i Z_i + \sum J_{ij} Z_i Z_j$?
### b. Bagaimana kaitan antara state $|0\rangle$ (Up) / $|1\rangle$ (Down) dengan eigenvalue dari operator Pauli-Z (+1 dan -1)?
## 5. Logika Interaksi (QMI)
### a. Quantum Mutual Information ($I$) selalu bernilai positif ($\ge 0$). Dalam model Ising, tanda $J$ menentukan sifat feromagnetik atau antiferomagnetik. Apakah penggunaan QMI secara langsung sebagai $J$ berarti kita mengasumsi hubungan antar saham selalu "searah" dalam minimalisasi energi?
## 6. Algoritma VQE dan Ansatz
### a. Mengapa `EfficientSU2` dipilih sebagai ansatz untuk masalah ini dibandingkan ansatz lain seperti `RealAmplitudes`?
### b. Bagaimana penentuan jumlah *reps* (layer) pada sirkuit kuantum mempengaruhi konvergensi hasil?
## 7. Interpretasi Hasil Akhir
### a. Bagaimana cara menginterpretasikan *ground state* (misal bitstring '0101') yang dihasilkan VQE menjadi keputusan pemilihan saham atau strategi portofolio yang konkret?
