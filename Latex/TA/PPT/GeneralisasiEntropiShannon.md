Ya, **penurunan yang Anda tuliskan memang menggunakan prinsip diagonalisasi matriks melalui dekomposisi spektral**. Bahkan, inilah cara yang paling umum dan paling rigor dalam buku-buku mekanika kuantum. Namun ada satu hal konseptual yang perlu diluruskan.

**Sebenarnya Anda tidak sedang "menurunkan" Entropi Shannon menjadi Entropi Von Neumann.**

Yang dilakukan adalah **menggeneralisasi** Entropi Shannon ke ruang Hilbert menggunakan operator densitas.

Alur logikanya adalah

[
\text{probabilitas klasik}
\longrightarrow
\text{operator densitas}
\longrightarrow
\text{fungsi operator } \log(\rho)
\longrightarrow
\text{trace}
]

baru kemudian diperlihatkan bahwa jika keadaan tersebut ternyata hanyalah distribusi probabilitas klasik, maka rumus itu kembali menjadi Entropi Shannon.

---

# Mengapa perlu dekomposisi spektral?

Misalkan kita langsung menulis

[
S(\rho)=-\operatorname{Tr}(\rho\log\rho).
]

Masalahnya adalah

> **Apa arti (\log(\rho))?**

Logaritma matriks tidak dihitung dengan mengambil log setiap elemen matriks.

Sebagai contoh,

[
\rho=
\begin{pmatrix}
0.6&0.3\
0.3&0.4
\end{pmatrix}
]

maka

[
\log(\rho)
\neq
\begin{pmatrix}
\log0.6&\log0.3\
\log0.3&\log0.4
\end{pmatrix}.
]

Yang benar adalah mendefinisikan fungsi matriks melalui **Teorema Spektral**.

Karena (\rho) Hermitian,

[
\rho=U\Lambda U^\dagger,
]

dengan

[
\Lambda=
\begin{pmatrix}
\lambda_1&&\
&\lambda_2&\
&&\ddots
\end{pmatrix}.
]

Kemudian fungsi apa pun didefinisikan sebagai

[
f(\rho)=Uf(\Lambda)U^\dagger,
]

sehingga

[
\log(\rho)
==========

U
\begin{pmatrix}
\log\lambda_1&&\
&\log\lambda_2&\
&&\ddots
\end{pmatrix}
U^\dagger.
]

Inilah alasan matematis mengapa dekomposisi spektral diperlukan.

---

# Mengapa hasil akhirnya menjadi seperti Shannon?

Perhatikan

[
\rho
====

U\Lambda U^\dagger.
]

Maka

[
\log\rho
========

U(\log\Lambda)U^\dagger.
]

Akibatnya

[
\rho\log\rho
============

U\Lambda U^\dagger
U(\log\Lambda)U^\dagger
=======================

U(\Lambda\log\Lambda)U^\dagger.
]

Sekarang gunakan sifat invariansi trace terhadap transformasi kesamaan

[
\operatorname{Tr}(UAU^\dagger)
==============================

\operatorname{Tr}(A),
]

sehingga

[
\operatorname{Tr}(\rho\log\rho)
===============================

\operatorname{Tr}(\Lambda\log\Lambda).
]

Karena matriks diagonal,

[
\Lambda\log\Lambda=
\begin{pmatrix}
\lambda_1\log\lambda_1&&\
&\lambda_2\log\lambda_2&\
&&\ddots
\end{pmatrix},
]

maka

[
\operatorname{Tr}(\rho\log\rho)
===============================

\sum_i
\lambda_i\log\lambda_i.
]

Sehingga

[
S(\rho)
=======

-\sum_i
\lambda_i\log\lambda_i.
]

Inilah persamaan yang identik dengan Entropi Shannon, hanya saja probabilitas (p_i) digantikan oleh nilai eigen operator densitas.

---

# Jadi apakah langkah-langkahmu sudah benar?

Secara umum, **ya**, tetapi ada satu bagian yang sebaiknya diperbaiki.

Pada Langkah 2 Anda menulis

[
\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|.
]

Lalu pada Langkah 3

[
\rho=\sum_j\lambda_j|e_j\rangle\langle e_j|.
]

Urutan ini berpotensi membuat pembaca mengira

[
p_i=\lambda_i.
]

Padahal **tidak selalu demikian**.

Keadaan campuran

[
\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|
]

adalah **sekadar salah satu cara menulis** operator densitas. Basis (|\psi_i\rangle) bahkan tidak harus ortogonal.

Sedangkan

[
\rho=\sum_j\lambda_j|e_j\rangle\langle e_j|
]

adalah **dekomposisi spektral**, yaitu representasi khusus pada basis eigen, sehingga (|e_j\rangle) pasti ortonormal dan (\lambda_j) adalah nilai eigen.

Keduanya hanya identik jika (|\psi_i\rangle) memang merupakan basis eigen dari (\rho).

---

# Untuk presentasi atau skripsi, saya menyarankan alur berikut

Alur yang lebih kuat secara matematis adalah:

1. Ingatkan definisi Entropi Shannon
   [
   H=-\sum_i p_i\log p_i.
   ]

2. Motivasi bahwa pada mekanika kuantum probabilitas digantikan oleh operator densitas.

3. Definisikan Entropi Von Neumann
   [
   S(\rho)=-\operatorname{Tr}(\rho\log\rho).
   ]

4. Karena (\rho) Hermitian, gunakan Teorema Spektral
   [
   \rho=U\Lambda U^\dagger.
   ]

5. Definisikan
   [
   \log\rho
   ========

   U(\log\Lambda)U^\dagger.
   ]

6. Gunakan invariansi trace untuk memperoleh
   [
   S(\rho)
   =======

   -\sum_i\lambda_i\log\lambda_i.
   ]

7. Tunjukkan bahwa bila (\rho) sudah diagonal dengan elemen diagonal (p_i),
   [
   \rho=\operatorname{diag}(p_1,p_2,\ldots),
   ]
   maka
   [
   \lambda_i=p_i
   ]
   sehingga
   [
   S(\rho)
   =======

   # -\sum_i p_i\log p_i

   H.
   ]

Urutan ini lebih akurat secara matematis karena menekankan bahwa **Entropi Von Neumann adalah generalisasi Entropi Shannon**, dan dekomposisi spektral digunakan untuk menunjukkan bahwa rumus tersebut mereduksi ke bentuk Shannon ketika operator densitas merepresentasikan distribusi probabilitas klasik. Ini juga menghindari kesan yang keliru bahwa Entropi Shannon "diturunkan" menjadi Entropi Von Neumann.

