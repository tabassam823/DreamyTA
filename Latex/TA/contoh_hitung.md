Kita lakukan **contoh lengkap langkah demi langkah** menggunakan **mixed state** dari data yang kamu berikan. Ini sangat mirip dengan prosedur yang biasa dipakai dalam **quantum information untuk data klasik**.

Data observasi:

|AAPL|TSLA|Frekuensi|
|---|---|---|
|Up|Up|35|
|Up|Down|15|
|Down|Up|20|
|Down|Down|30|

Total observasi:

$$  
N = 35+15+20+30 = 100  
$$

---

# 1. Ubah Frekuensi Menjadi Probabilitas

$$  
p_{uu} = 35/100 = 0.35  
$$

$$  
p_{ud} = 15/100 = 0.15  
$$

$$  
p_{du} = 20/100 = 0.20  
$$

$$  
p_{dd} = 30/100 = 0.30  
$$

Distribusi joint:

||TSLA Up|TSLA Down|
|---|---|---|
|AAPL Up|0.35|0.15|
|AAPL Down|0.20|0.30|

---

# 2. Bentuk Density Matrix (Mixed State)

Untuk **mixed state klasik**, density matrix berbentuk **diagonal**:

Basis:

$$  
|00\rangle, |01\rangle, |10\rangle, |11\rangle  
$$

dengan interpretasi:

|basis|arti|
|---|---|
|(|00\rangle)|
|(|01\rangle)|
|(|10\rangle)|
|(|11\rangle)|

Density matrix:

$$  
\rho_{AB} =  
\begin{pmatrix}  
0.35 & 0 & 0 & 0 \\  
0 & 0.15 & 0 & 0 \\  
0 & 0 & 0.20 & 0 \\  
0 & 0 & 0 & 0.30  
\end{pmatrix}  
$$

Ini disebut **classical mixed state** karena tidak ada koherensi (off-diagonal = 0).

---

# 3. Reduced Density Matrix

## Sistem A (AAPL)

Marginal probability:

$$  
p_A(up) = 0.35 + 0.15 = 0.50  
$$

$$  
p_A(down) = 0.20 + 0.30 = 0.50  
$$

Maka

$$  
\rho_A =  
\begin{pmatrix}  
0.50 & 0 \  
0 & 0.50  
\end{pmatrix}  
$$

---

## Sistem B (TSLA)

$$  
p_B(up) = 0.35 + 0.20 = 0.55  
$$

$$  
p_B(down) = 0.15 + 0.30 = 0.45  
$$

$$  
\rho_B =  
\begin{pmatrix}  
0.55 & 0 \  
0 & 0.45  
\end{pmatrix}  
$$

---

# 4. Von Neumann Entropy

Rumus:

$$  
S(\rho) = -\sum_i \lambda_i \log_2 \lambda_i  
$$

di mana (\lambda_i) adalah eigenvalue.

Karena matriks diagonal, eigenvalue = probabilitas.

---

# 5. Entropy Sistem A

Eigenvalue:

$$  
0.5,0.5  
$$

$$  
S(\rho_A)  
= -0.5\log_2(0.5)-0.5\log_2(0.5)  
$$

$$  
S(\rho_A)=1 \text{ bit}  
$$

---

# 6. Entropy Sistem B

Eigenvalue:

$$  
0.55,0.45  
$$

# $$  
S(\rho_B)

-0.55\log_2(0.55)  
-0.45\log_2(0.45)  
$$

Perhitungan:

$$  
\log_2(0.55)\approx -0.862  
$$

$$  
\log_2(0.45)\approx -1.152  
$$

Sehingga

$$  
S(\rho_B)  
=0.474+0.518  
$$

$$  
S(\rho_B)\approx0.9925 \text{ bit}  
$$

---

# 7. Entropy Sistem Gabungan

Eigenvalue:

$$  
0.35,0.15,0.20,0.30  
$$

# $$  
S(\rho_{AB})

-\sum p_i \log_2 p_i  
$$

Hitung satu per satu

$$  
-0.35\log_2(0.35) = 0.530  
$$

$$  
-0.15\log_2(0.15) = 0.411  
$$

$$  
-0.20\log_2(0.20) = 0.464  
$$

$$  
-0.30\log_2(0.30) = 0.521  
$$

Jumlah:

$$  
S(\rho_{AB}) \approx 1.926 \text{ bit}  
$$

---

# 8. Quantum Mutual Information

Rumus:

$$  
I(A:B)=S(\rho_A)+S(\rho_B)-S(\rho_{AB})  
$$

Masukkan nilai:

$$  
I(A:B)=1 + 0.9925 - 1.926  
$$

$$  
I(A:B)\approx 0.0665  
$$

---

# 9. Interpretasi Hasil

$$  
I(A:B)\approx0.067 \text{ bit}  
$$

Artinya:

- korelasi antara **AAPL dan TSLA kecil**
    
- hampir independen
    
- hanya sekitar **0.067 bit informasi bersama**
    

Jika dua saham sangat berkorelasi, nilainya bisa mendekati **1 bit**.

---

# 10. Insight Penting (Untuk Penelitianmu)

Karena kita memakai **mixed state diagonal**, maka berlaku:

$$  
S(\rho)=H(p)  
$$

sehingga

$$  
I_{quantum}=I_{classical}  
$$

Artinya:

**quantum mutual information = classical mutual information**

pada sistem ini.

---

# 11. Perbedaan Jika Kamu Pakai Pure State

Jika kamu melakukan metode yang kamu jelaskan sebelumnya:

$$  
|\psi\rangle =  
\sqrt{0.35}|00\rangle  
+\sqrt{0.15}|01\rangle  
+\sqrt{0.20}|10\rangle  
+\sqrt{0.30}|11\rangle  
$$

maka

$$  
\rho = |\psi\rangle\langle\psi|  
$$

akan muncul **koherensi kuantum** (off-diagonal terms), dan hasil:

- (S(\rho_{AB}) = 0)
    
- QMI menjadi jauh lebih besar
    

Ini sering dipakai dalam **quantum embedding of classical data**.

---

✅ Jika kamu mau, kita bisa lanjut ke tahap yang **sangat menarik untuk risetmu**, yaitu:

1️⃣ menghitung **quantum mutual information untuk pure state embedding** dari data yang sama

2️⃣ melihat **perbedaan besar antara mixed state vs pure state**

3️⃣ ini bisa menjadi **argumen ilmiah kuat di paper kamu** tentang _quantum representation of market correlations_.