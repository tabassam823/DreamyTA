# Fase_LatarBelakang
slide ke:
1. jelasin inflasi (gambar nixon) --> jelasin investasi (gambar investasi) --> jelasin diversifikasi
2. jelasin model markowitz (ditunjukkan persamaannya dan pareto optimumnya) --> yang diformulasikan ke model ising menjadi persamaan hamiltonian ising (Tunjukkan Persamaan Umum Dari Hamilton & Ising)
3. jelasin proses memasukkan hamiltonian ising ke dalam komputer kuantum untuk mendapatkan konfigurasi keputusan aset
4. jelasin masalah dari efisiensi komputer kuantum untuk masuk ke warm start strategy salah satu kandidat yang bisa digunakan adalah konsep nash equilibrium dari game theory
5. cara untuk melhat performa adalah dilakukan backtesting dan membandingkan model yang digunakan (GT-VQE) dengan pencarian optimasi portofolio strategi lain (SLSQP, only Nash eq, only VQE)
6. tujuan
7. batasan masalah

# Fase_Metode
slide ke:
1. tunjukin diagram alirnya dulu sebagai pembuka
2. proses pre-processing data
3. masukin data ke markowitz
4. ubah markowitz jadi EPG dan cara mencari nash eq
5. ubah EPG jadi ising
6. bentuk sirkuit efficientSU(2), bnetu gerbang matriks untuk 1 depth saja
7. optimasi SPSA
8. evaluasi distribuis probabiltas menggunakan entropi
9. tunjukin algoritma backtesting
10. tunjukin proses perhitungan matriks yang terdiri dari sharpe ratio, pembanding SLSQP, konsep MDD, return, dan equal weight

# Fase_Hasil
slide ke:
1. tampilkan simulasi konvergensinya
2. tunjukin gambar konvergensi terutama untuk entropi tinggi (tidak optimal) dan entropi rendah (optimal)
3. tampilkan pergerakan harga
4. tampilkan gambar performa masingmasing strategi untuk N=2 dan N=4
5. tabel metrik
6. kesimpulan
7. saran