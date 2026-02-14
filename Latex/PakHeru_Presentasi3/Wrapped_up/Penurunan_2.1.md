### 1. Formulasi Ekspektasi Diskret

Secara statistik, nilai ekspektasi dari variabel acak $R_k$ yang bergantung pada suatu kejadian (event) $A$ didefinisikan sebagai:

$$\mathbb{E}[R|A] = \sum r \cdot P(R=r|A)$$

Dalam kasus Anda:

- **Event $A$** adalah sistem berada pada State $\ket{ij}$.
    
- **$R_k$** adalah nilai return aset ke-$k$.
    

Maka, nilai $u_{ij}^k$ adalah rata-rata dari semua nilai $R_k$ yang muncul hanya pada hari-hari di mana State tercatat sebagai $\ket{ij}$.

---

### 2. Penurunan dari Data Historis

Misalkan kita memiliki total $N$ hari pengamatan.

1. Identifikasi himpunan waktu $T_{ij}$, yaitu kumpulan hari di mana State adalah $\ket{ij}$:
    
    $$T_{ij} = \{t \in \{1, \dots, N\} \mid \text{State}_t = \ket{ij}\}$$
    
2. Jumlah hari tersebut adalah $n_{ij}$ (seperti pada persamaan 1.8 di gambar sebelumnya).
    
3. Maka, estimasi _a posteriori_ untuk ekspektasi return tersebut adalah **rata-rata aritmetika** dari $R_k$ pada hari-hari tersebut:
    
    $$u_{ij}^k = \frac{1}{n_{ij}} \sum_{t \in T_{ij}} R_k(t)$$
    

---

### 3. Hubungan dengan Probabilitas

Jika kita melihatnya dari sudut pandang probabilitas bersama (_joint probability_), berdasarkan hukum Bayes:

$$P(R_k | \ket{ij}) = \frac{P(R_k \cap \ket{ij})}{P(\ket{ij})}$$

Sehingga $u_{ij}^k$ merepresentasikan nilai pusat (mean) dari distribusi return $R_k$ yang telah "difilter" oleh keadaan kuantum $\ket{ij}$.