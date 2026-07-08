# Fase_LatarBelakang
slide ke:
1. file diawali dengan foto-foto orang yang terlibat pada penelitian yaitu markowitz, lenz ising onsager, montegna, kahneman tversky, von neumann morgenstern, shannon
2. dimasukkan slide analisis fundamental, teknikal
3. analisis kuantitatif yang sudah ada
4. markowitz dan contoh pembagiannnya
5. tujuan 
6. batasan masalah
# Fase_Metode
slide ke:
1. 
# Fase_Hasil
slide ke:
1. tampilkan simulasi konvergensinya
2. tunjukin gambar konvergensi terutama untuk entropi tinggi (tidak optimal) dan entropi rendah (optimal)
3. tampilkan pergerakan harga
4. tampilkan gambar performa masingmasing strategi untuk N=2 dan N=4
5. tabel metrik
6. kesimpulan
7. saran
### Penurunan Fungsi Utilitas Pemain

Fungsi objektif Markowitz dapat dituliskan sebagai

$$
U(\mathbf{x})
=
\frac{1}{K}\sum_{i=1}^{N}\mu_i x_i
-
\frac{\gamma}{2K^2}
\sum_{i=1}^{N}\sum_{j=1}^{N}\sigma_{ij}x_i x_j.
$$

Komponen keuntungan setiap pemain didefinisikan sebagai kontribusi return aset yang dipilih, sedangkan komponen risiko diperoleh dari perubahan (*marginal contribution*) fungsi risiko global terhadap keputusan pemain ke-$i$. Oleh karena itu, utilitas pemain didefinisikan sebagai

$$
u_i(\mathbf{x})
=
\frac{\mu_i}{K}x_i
-
\frac{\gamma}{2K^2}
x_i
\left(
\sigma_{ii}
+
2\sum_{j\neq i}\sigma_{ij}x_j
\right).
$$

Bentuk tersebut dapat diturunkan dari ekspansi bentuk kuadratik

$$
\mathbf{x}^T\Sigma\mathbf{x}
=
\sum_{i=1}^{N}\sigma_{ii}x_i^2
+
2\sum_{i<j}\sigma_{ij}x_ix_j.
$$

Karena variabel keputusan bersifat biner,

$$
x_i\in\{0,1\},
\qquad
x_i^2=x_i,
$$

maka persamaan di atas menjadi

$$
\mathbf{x}^T\Sigma\mathbf{x}
=
\sum_{i=1}^{N}\sigma_{ii}x_i
+
2\sum_{i<j}\sigma_{ij}x_ix_j.
$$

Suku pertama merepresentasikan risiko individual (varians) dari aset ke-$i$, sedangkan suku kedua merepresentasikan risiko interaksi akibat kovarians antar pasangan aset. Faktor 2 muncul karena matriks kovarians bersifat simetris ($\sigma_{ij}=\sigma_{ji}$), sehingga setiap pasangan aset dihitung dua kali pada bentuk kuadratik.

Ketika pemain ke-$i$ mengubah strateginya, perubahan fungsi risiko global yang dirasakan pemain tersebut adalah

$$
\sigma_{ii}
+
2\sum_{j\neq i}\sigma_{ij}x_j,
$$

sehingga utilitas pemain dapat dituliskan kembali sebagai

$$
u_i(\mathbf{x})
=
\frac{\mu_i}{K}x_i
-
\frac{\gamma}{2K^2}
x_i
\left(
\sigma_{ii}
+
2\sum_{j\neq i}\sigma_{ij}x_j
\right).
$$

Perumusan utilitas ini memastikan bahwa setiap perubahan utilitas lokal pemain identik dengan perubahan fungsi potensial global, sehingga memenuhi syarat sebagai *Exact Potential Game* (EPG),

$$
u_i(x_i',x_{-i})-u_i(x_i,x_{-i})
=
\Phi(x_i',x_{-i})-\Phi(x_i,x_{-i}).
$$