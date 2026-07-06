Menurut saya ini adalah cara terbaik untuk memahami **mengapa barren plateau muncul**, karena kita akan melihatnya berkembang dari ansatz yang sama seperti milikmu, bukan langsung menerima hasil teorema McClean. Saya akan membangun penjelasannya secara bertahap, dari depth = 1 hingga muncul konsep 2-design.

---

# Langkah 1. Ansatz yang sama dengan punyamu

Mari kita sederhanakan notasi. Misalkan hanya ada **2 qubit** dengan satu layer:

[
U(\boldsymbol{\theta})
======================

U_{\text{ent}}
U_{\text{rot}},
]

dengan

[
U_{\text{rot}}
==============

(R_z(\phi_1)R_y(\theta_1))
\otimes
(R_z(\phi_2)R_y(\theta_2)),
]

dan

[
U_{\text{ent}}
==============

\mathrm{CNOT}*{2\rightarrow1}
\mathrm{CNOT}*{1\rightarrow2}.
]

State awal

[
|\psi_0\rangle
==============

|00\rangle.
]

State akhir

[
|\psi(\theta)\rangle
====================

U(\theta)|00\rangle.
]

Misalkan cost function yang sederhana

[
C(\theta)
=========

\langle Z_1\rangle.
]

---

# Langkah 2. Depth = 0

Belum ada gerbang.

State

[
|00\rangle.
]

Maka

[
\langle Z_1\rangle
==================

1.

]

Gradien

[
\frac{\partial C}{\partial\theta}=0.
]

Belum menarik.

---

# Langkah 3. Tambahkan satu gerbang (R_y)

Supaya mudah dipahami, abaikan dulu semua gerbang lain.

Misalkan hanya

[
R_y(\theta)
]

pada qubit pertama.

Keadaan menjadi

[
|\psi\rangle
============

\cos\frac\theta2|00\rangle
+
\sin\frac\theta2|10\rangle.
]

Sekarang hitung

[
\langle Z_1\rangle.
]

Karena

[
Z|0\rangle=|0\rangle,
]

[
Z|1\rangle=-|1\rangle,
]

maka

[
C(\theta)
=========

## \cos^2\frac\theta2

\sin^2\frac\theta2.
]

Gunakan identitas

[
\cos^2x-\sin^2x=\cos2x.
]

Didapat

[
\boxed{
C(\theta)=\cos\theta.
}
]

Gradien

[
\boxed{
\frac{\partial C}{\partial\theta}
=================================

-\sin\theta.
}
]

---

## Apa artinya?

Landscape optimasinya

```text
 ^
 |\
 | \
 |  \
 |   \
 |    \
 |     \
 +---------->

```

Gradien besar.

Optimizer mudah bergerak.

Belum ada barren plateau.

---

# Langkah 4. Tambahkan rotasi pada qubit kedua

Sekarang

[
R_y(\theta_1)
\otimes
R_y(\theta_2).
]

State menjadi

[
\begin{aligned}
|\psi\rangle
=&
c_1c_2|00\rangle
+
c_1s_2|01\rangle\
&
+s_1c_2|10\rangle
+
s_1s_2|11\rangle,
\end{aligned}
]

dengan

[
c_i=\cos\frac{\theta_i}{2},
]

[
s_i=\sin\frac{\theta_i}{2}.
]

Masih separable.

Masih mudah.

Gradien masih cukup besar.

---

# Langkah 5. Tambahkan CNOT pertama

Sekarang amplitudo berubah menjadi

[
\begin{aligned}
|\psi\rangle
=&
c_1c_2|00\rangle
+
c_1s_2|01\rangle\
&
+s_1c_2|11\rangle
+
s_1s_2|10\rangle.
\end{aligned}
]

Sekarang amplitudo mulai saling bercampur.

Parameter

[
\theta_1
]

dan

[
\theta_2
]

tidak bisa dipisahkan lagi.

Misalnya koefisien

[
|11\rangle
==========

s_1c_2.
]

Ia bergantung pada dua parameter sekaligus.

---

# Langkah 6. Tambahkan satu layer lagi

Sekarang

```text
Ry
↓

Rz
↓

CNOT

↓

Ry

↓

Rz

↓

CNOT
```

Perhatikan apa yang terjadi.

Layer pertama menghasilkan

empat amplitudo.

Layer kedua memutar kembali semua amplitudo itu.

Akibatnya

koefisien baru menjadi

[
a_{00}'
=======

f(\theta_1,\theta_2,\theta_3,\theta_4,\ldots)
]

yang berisi

puluhan suku sinus dan cosinus.

Misalnya bentuknya menjadi

[
\begin{aligned}
a_{00}
======

&
c_1c_2c_3
---------

c_1s_2s_3
\
&
+s_1c_2e^{i\phi}
+\cdots
\end{aligned}
]

Mulai sangat rumit.

---

# Langkah 7. Mengapa gradien mengecil?

Sekarang lihat satu amplitudo.

Misalnya

[
a
=

## 0.31

0.27
+
0.14
----

0.16
+
0.21
----

0.23.
]

Banyak suku saling membatalkan.

Sekarang gradien

[
\frac{\partial a}{\partial\theta}
]

juga merupakan penjumlahan

positif

dan

negatif.

Sebagian besar saling menghilangkan.

Inilah awal munculnya barren plateau.

---

# Langkah 8. Hubungan dengan Central Limit Theorem

Misalkan terdapat

100

kontribusi acak

[
x_i.
]

Jumlahnya

[
S
=

\sum_i x_i.
]

Menurut Central Limit Theorem,

[
S
]

akan mendekati distribusi Gaussian.

Rata-ratanya

nol.

Variansnya

kecil dibanding jumlah komponennya.

Gradien pada ansatz dalam mengalami fenomena yang serupa: banyak kontribusi sinus dan cosinus dari parameter yang berbeda saling menambah dan mengurangi sehingga estimasi gradien terkonsentrasi di sekitar nol.

---

# Langkah 9. Sekarang bayangkan 20 qubit

Bukan lagi

4

basis.

Tetapi

[
2^{20}
======

1,048,576
]

basis.

Artinya

lebih dari satu juta amplitudo.

Setiap layer mencampur semuanya.

Koefisien akhirnya menjadi

[
a_i
===

\sum
(\text{jutaan suku sinus-cosinus}).
]

Masing-masing suku

positif

atau

negatif.

Sebagian besar saling menghilangkan.

Gradien akhirnya

sangat kecil.

---

# Langkah 10. Di sinilah muncul 2-design

Sekarang bayangkan kita tidak tahu lagi

amplitudo mana berasal dari mana.

Setelah

cukup banyak layer,

semua amplitudo

terlihat acak.

Secara statistik

[
a_{00},
a_{01},
a_{10},
a_{11},
\dots
]

berperilaku seperti

bilangan acak kompleks.

Distribusi amplitudonya hampir sama dengan distribusi Haar.

Karena distribusi amplitudonya sudah sama,

maka

* rata-rata energi,
* variansi energi,
* rata-rata gradien,
* variansi gradien,

juga sama.

Itulah arti

> ansatz mendekati **unitary 2-design**.

Bukan berarti sirkuit menjadi benar-benar acak, tetapi untuk semua besaran yang hanya bergantung pada **momen kedua** (misalnya (|a_i|^2), korelasi dua titik, atau variansi gradien), statistiknya sudah tidak dapat dibedakan dari sirkuit yang dipilih secara acak menurut distribusi Haar.

---

# Visualisasi seluruh proses

```text
Depth = 1

|00>
 ↓
Ry
 ↓
State masih sederhana

Gradien besar
──────────────────────────────

Depth = 2

Ry
 ↓
CNOT
 ↓
Ry
 ↓
CNOT

Parameter mulai bercampur

Gradien mulai mengecil
──────────────────────────────

Depth = 5

Semua amplitudo bercampur

Banyak interferensi

Gradien kecil
──────────────────────────────

Depth = 20

Distribusi amplitudo hampir acak

≈ Haar

≈ 2-design

Variansi gradien ≈ 0

Barren Plateau
```

---

## Mengapa ansatz-mu masih dapat bekerja?

Di sinilah desain ansatz modern menjadi penting. Walaupun secara teori **deep hardware-efficient ansatz** dapat mendekati 2-design, dalam praktik VQE sering kali kondisi itu **tidak benar-benar tercapai**, karena:

1. **Depth dibatasi** oleh decoherence perangkat kuantum dan biaya komputasi.
2. **Hamiltonian yang dioptimasi bersifat lokal**, sehingga gradien parameter tertentu masih dipengaruhi terutama oleh lingkungan lokalnya, bukan oleh seluruh ruang Hilbert.
3. **Parameter tidak diinisialisasi secara acak penuh**, tetapi menggunakan strategi seperti warm start atau identity initialization.
4. Optimizer seperti **SPSA** atau pendekatan layer-wise membantu menjaga parameter tetap berada di wilayah landscape yang masih memiliki gradien informatif.

Itulah sebabnya ansatz seperti yang kamu gunakan (rotasi lokal → CNOT → rotasi lokal → CNOT, diulang beberapa layer) masih efektif untuk masalah berukuran kecil hingga menengah. Tantangannya mulai muncul ketika jumlah qubit dan depth bertambah sehingga sirkuit semakin menyerupai unitary acak dan efek 2-design mulai mendominasi.

