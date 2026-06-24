1Ya dan tidak. Ada hubungan yang sangat dalam, tetapi arah logikanya biasanya kebalik dari yang banyak orang bayangkan.

---

## Jalur 1: Dari operator uniter umum menuju eksponensial Pauli

Anda telah memperoleh bentuk umum

[  
U=  
e^{i\alpha}  
\begin{pmatrix}  
e^{i\beta}\cos\theta &  
e^{i\gamma}\sin\theta  
\  
-e^{-i\gamma}\sin\theta &  
e^{-i\beta}\cos\theta  
\end{pmatrix}.  
]

Bentuk ini adalah parameterisasi grup (U(2)) atau (SU(2)).

Dari teori grup Lie, diketahui bahwa setiap elemen (SU(2)) dapat ditulis sebagai eksponensial suatu kombinasi linear matriks Pauli:

# [  
U

e^{-i\frac{\theta}{2}  
(n_x X+n_y Y+n_z Z)}.  
]

atau lebih ringkas

# [  
U

e^{-i\frac{\theta}{2}  
(\hat n\cdot \vec{\sigma})},  
]

dengan

# [  
\vec{\sigma}

(X,Y,Z).  
]

Jadi bentuk eksponensial Pauli sebenarnya **ekuivalen** dengan bentuk matriks umum (SU(2)).

---

## Jalur 2: Dari eksponensial Pauli menuju matriks umum

Ini justru yang lebih sering dilakukan di buku komputasi kuantum.

Definisikan

# [  
\hat n

(n_x,n_y,n_z)  
]

sebagai vektor satuan.

Kemudian

# [  
U

e^{-i\frac{\theta}{2}  
(\hat n\cdot \vec{\sigma})}.  
]

Karena

[  
(\hat n\cdot \vec{\sigma})^2=I,  
]

maka deret Taylor dapat disederhanakan menjadi

# [  
U

I\cos\frac{\theta}{2}  
-i(\hat n\cdot\vec{\sigma})  
\sin\frac{\theta}{2}.  
]

Sekarang tuliskan

# [  
\hat n

(\sin\eta\cos\phi,,  
\sin\eta\sin\phi,,  
\cos\eta).  
]

Maka setelah substitusi Pauli (X,Y,Z), diperoleh

[  
U=  
\begin{pmatrix}  
\cos\frac{\theta}{2}  
-i\cos\eta,\sin\frac{\theta}{2}  
&  
-e^{i\phi}\sin\eta,\sin\frac{\theta}{2}  
\  
e^{-i\phi}\sin\eta,\sin\frac{\theta}{2}  
&  
\cos\frac{\theta}{2}  
+i\cos\eta,\sin\frac{\theta}{2}  
\end{pmatrix}.  
]

Ini ternyata identik dengan parameterisasi umum (SU(2)).

---

## Mengapa ada faktor (1/2)?

Ini pertanyaan yang sering muncul.

Rotasi ruang tiga dimensi biasa ditulis

[  
R(\theta)=e^{-i\theta J},  
]

dengan (J) generator rotasi.

Untuk spin-(\frac12),

[  
J_i=\frac{\sigma_i}{2}.  
]

Karena generator rotasi adalah

[  
\frac{\sigma_i}{2},  
]

maka operator rotasinya menjadi

# [  
R_i(\theta)

e^{-i\theta \sigma_i/2}.  
]

Jadi faktor (1/2) muncul karena qubit merepresentasikan sistem spin-(\frac12).

---

## Untuk skripsi Anda

Menurut saya urutan yang paling elegan adalah:

1. Turunkan bentuk umum (SU(2)).
    
2. Tunjukkan bahwa (X,Y,Z) adalah kasus khusus.
    
3. Kemudian tulis:
    

> Selain dapat direpresentasikan sebagai kasus khusus dari operator (SU(2)), matriks Pauli juga berperan sebagai generator rotasi pada ruang keadaan qubit. Berdasarkan teori grup Lie, setiap operator uniter satu-qubit dapat dituliskan sebagai eksponensial dari kombinasi linear matriks Pauli,

[  
U=  
e^{-i\frac{\theta}{2}  
(\hat n\cdot\vec{\sigma})}.  
]

4. Dari persamaan ini baru diturunkan
    

[  
R_x(\theta),  
\quad  
R_y(\theta),  
\quad  
R_z(\theta).  
]

Dengan demikian pembaca melihat rantai logika yang utuh:

[  
SU(2)  
;\Longrightarrow;  
X,Y,Z  
;\Longrightarrow;  
\hat n\cdot\vec{\sigma}  
;\Longrightarrow;  
e^{-i\theta(\hat n\cdot\vec{\sigma})/2}  
;\Longrightarrow;  
R_x,R_y,R_z.  
]

Ini adalah alur matematis yang paling rapi untuk menjembatani gerbang Pauli ke gerbang rotasi dalam bab teori VQE.