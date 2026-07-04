Pertanyaan ini sangat penting, karena istilah **"fungsi potensial global"** sering terdengar abstrak padahal konsepnya cukup intuitif.

### Intuisi dasar

Dalam *game theory*, setiap pemain memiliki **fungsi utilitas** masing-masing.

Misalkan terdapat tiga investor (agen):

* Agen 1 memilih membeli atau tidak membeli saham A.
* Agen 2 memilih membeli atau tidak membeli saham B.
* Agen 3 memilih membeli atau tidak membeli saham C.

Masing-masing mempunyai utilitas

[
u_1,;u_2,;u_3
]

yang bergantung pada keputusan semua agen.

Masalahnya adalah:

> Bagaimana mengetahui apakah seluruh sistem menjadi "lebih baik" ketika satu agen mengubah strateginya?

Karena ada banyak fungsi utilitas, sulit melakukan analisis langsung.

Di sinilah diperkenalkan **fungsi potensial global**

[
\Phi(\mathbf{x}).
]

Alih-alih mengamati semua utilitas satu per satu, kita cukup mengamati satu fungsi saja.

---

## Mengapa disebut "global"?

Karena

* utilitas hanya milik **satu agen**, sedangkan
* fungsi potensial menggambarkan **keadaan seluruh sistem permainan**.

Misalnya

[
\Phi(x_1,x_2,x_3)
]

memberikan satu angka yang merepresentasikan "kualitas" konfigurasi strategi seluruh pemain.

Sebagai analogi:

* **Utilitas** = kepuasan masing-masing orang.
* **Potensial global** = skor keseluruhan permainan.

---

## Mengapa bisa mewakili seluruh utilitas?

Inilah syarat utama Exact Potential Game.

Untuk setiap perubahan strategi agen ke-(i),

[
\Delta u_i
==========

\Delta\Phi.
]

Artinya

jika agen memperoleh keuntungan sebesar

[
+0.25,
]

maka fungsi potensial juga naik sebesar

[
+0.25.
]

Sebaliknya jika utilitas turun

[
-0.4,
]

potensial juga turun

[
-0.4.
]

Jadi fungsi potensial **tidak harus sama dengan jumlah utilitas**, tetapi perubahan nilainya selalu sama dengan perubahan utilitas pemain yang sedang bergerak.

Ini jauh lebih penting daripada nilai absolutnya.

---

## Contoh sederhana

Misalkan terdapat dua aset.

Keadaan awal

| Strategi | Potensial |
| -------- | --------: |
| (0,0)    |         5 |
| (1,0)    |         8 |
| (1,1)    |         7 |

Bayangkan agen pertama mengubah strategi

[
(0,0)
\rightarrow
(1,0).
]

Misalkan utilitas agen pertama naik

[
2
\rightarrow
5.
]

Maka

[
\Delta u_1=3.
]

Karena ini Exact Potential Game,

[
\Delta\Phi
==========

# 8-5

3.

]

Sekarang agen kedua mencoba masuk

[
(1,0)
\rightarrow
(1,1).
]

Misalkan utilitasnya turun sebesar 1.

Maka

[
\Delta u_2=-1.
]

Potensial juga berubah

[
7-8=-1.
]

Jadi setiap agen cukup melihat apakah langkahnya menaikkan potensial atau tidak.

---

## Pada kasus portofolio

Fungsi potensialnya adalah

[
\Phi(\mathbf{x})
================

\sum_i
\mu_i\frac{x_i}{K}
------------------

\frac{\gamma}{2}
\sum_{i,j}
\sigma_{ij}
\frac{x_i}{K}
\frac{x_j}{K}.
]

Perhatikan bentuknya.

Suku pertama

[
\sum_i
\mu_i\frac{x_i}{K}
]

adalah **total expected return** portofolio.

Sedangkan suku kedua

[
\frac{\gamma}{2}
\sum_{i,j}
\sigma_{ij}
\frac{x_i}{K}
\frac{x_j}{K}
]

adalah **penalti risiko** akibat kovarians antar aset.

Jadi sebenarnya

[
\Phi
====

## \text{return}

\text{risk penalty}.
]

Artinya semakin besar (\Phi),

* return semakin tinggi,
* risiko relatif semakin kecil,
* sehingga konfigurasi portofolio semakin baik menurut kriteria Markowitz.

---

## Mengapa disebut "potensial"?

Istilah ini berasal dari fisika.

Pada mekanika klasik, terdapat energi potensial

[
V(x).
]

Sebuah bola selalu bergerak menuju energi potensial yang lebih rendah.

Demikian pula dalam EPG, pemain selalu bergerak menuju keadaan dengan **potensial yang lebih tinggi** (atau ekuivalen dengan **energi Hamiltonian yang lebih rendah**, karena (H=-\Phi)).

Itulah sebabnya pada slide berikutnya dilakukan transformasi

[
H=-\Phi.
]

Dengan demikian,

* **maksimisasi utilitas** dalam teori permainan menjadi
* **minimisasi energi** dalam fisika statistik.

Inilah jembatan matematis yang memungkinkan masalah optimasi portofolio diselesaikan menggunakan **Model Ising**, **QUBO**, dan akhirnya **VQE**.

### Saran kecil untuk slide

Kalimat pertama pada slide berbunyi:

> *Model permainan yang memetakan seluruh utilitas pemain menjadi satu fungsi potensial global ((\Phi)).*

Agar lebih presisi secara teori permainan, saya menyarankan menggantinya menjadi:

> **Model permainan yang memiliki suatu fungsi potensial global (\Phi), sehingga setiap perubahan utilitas individu akibat perubahan strategi sepenuhnya tercermin oleh perubahan nilai (\Phi). Dengan demikian, dinamika seluruh permainan dapat dianalisis melalui satu fungsi skalar.**

Kalimat ini lebih sesuai dengan definisi formal *Exact Potential Game*, karena (\Phi) bukan "gabungan" atau "jumlah" utilitas pemain, melainkan fungsi yang **mereplikasi perubahan marginal** setiap utilitas individu. Ini juga menjelaskan mengapa (\Phi) dapat dijadikan dasar pencarian *Nash Equilibrium*.

