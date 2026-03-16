Untuk menurunkan ekspansi orde ke-1 hingga ke-3 dari divergensi Kullback--Leibler ($D_{KL}$) terhadap parameter kopling $J_{ij}$, kita dapat meninjau sistem Ising pada rezim interaksi lemah.

Secara konseptual, $D_{KL}$ atau _Mutual Information_ mengukur seberapa jauh distribusi probabilitas gabungan $P(s_i, s_j)$ menyimpang dari distribusi produk independen $P(s_i)P(s_j)$ akibat adanya parameter interaksi $J_{ij}$.

### Penurunan Ekspansi Taylor

Jika kita mengasumsikan energi interaksi kecil, kita dapat melakukan ekspansi Taylor pada fungsi $D_{KL}(J_{ij})$ di sekitar $J_{ij} = 0$:

$$I(i:j) \approx I(0) + \frac{\partial I}{\partial J_{ij}} \bigg|_{J_{ij}=0} J_{ij} + \frac{1}{2!} \frac{\partial^2 I}{\partial J_{ij}^2} \bigg|_{J_{ij}=0} J_{ij}^2 + \frac{1}{3!} \frac{\partial^3 I}{\partial J_{ij}^3} \bigg|_{J_{ij}=0} J_{ij}^3$$

Berikut adalah karakteristik dari masing-masing orde:

- **Orde Ke-0 ($I(0)$):** Bernilai **0**. Ketika tidak ada interaksi ($J_{ij}=0$), variabel bersifat independen, sehingga tidak ada informasi yang dibagikan.
    
- **Orde Ke-1 (Linear):** Bernilai **0**. Dalam sistem setimbang (stasioner), turunan pertama terhadap parameter interaksi pada titik nol biasanya hilang karena sifat simetri atau kondisi ekstremum dari fungsi energi bebas.
    
- **Orde Ke-2 (Kuadratik):** Memberikan kontribusi dominan:
    
    $$\frac{J_{ij}^2}{2}$$
    
    Suku inilah yang digunakan dalam naskah Anda untuk menunjukkan bahwa $I(i:j) \propto J_{ij}^2$.
    
- **Orde Ke-3 (Kubik):** Pada banyak model Ising simetris, suku orde ganjil akan bernilai **0** karena sifat paritas dari distribusi probabilitas. Namun, jika terdapat medan eksternal ($h_i$) yang sangat kuat atau asimetri yang signifikan, suku ini mungkin muncul sebagai koreksi kecil, namun biasanya diabaikan dalam pendekatan interaksi lemah ($weak-interaction$) karena nilainya yang jauh lebih kecil ($\ll J_{ij}^2$).
    

### Ringkasan Bentuk Ekspansi

Maka, bentuk ekspansi hingga orde ke-3 dapat diringkas sebagai berikut:

$$I(i:j) \approx 0 + 0 + \frac{J_{ij}^2}{2} + 0 + \mathcal{O}(J_{ij}^4)$$

Inilah alasan mengapa secara matematis Anda dapat langsung mengambil aproksimasi $|J_{ij}| [cite_start]\propto \sqrt{I(i:j)}$. Pengambilan akar kuadrat ini secara efektif "membalikkan" ekspansi orde kedua tersebut untuk mendapatkan kembali magnitudo kekuatan interaksinya.

Apakah Anda ingin saya membantu menuliskan pembuktian matematis yang lebih formal untuk menunjukkan mengapa orde ke-1 dan ke-3 bernilai nol dalam konteks mekanika statistik?