# Bab 4.1
- [x] analisis numerik tambahkan expected returns dan matriks kovarians
- [x] menyebutkan lampiran C pada @../Lampiran/Lampiran-C.tex
- [x] tambahkan proses matematika numerik dalam menghitung expected return sesuai dengan data teratas pada tabel E.1 di lampiran E dengan n=126 karena satu semester
- [x] tambahkan juga proses matematika numerik dalam menghitung kovarians dan varians lalu baru dimasukkan ke matriks kovarians untuk sampel data N=2 saja
- [x] menambahkan proses matematis dari risk aversion endogen $\gamma$ menggunakan fungsi aktivasi sigmoid dengan \mu dan \sigma yang keduanya menggunakan log return 
1. masih kurang simple return dan log return
2. kurang perhitungan expected return (berapa jumlah dan rata-ratanya)
3. kurang rumus dan perhitungan varians dan kovarians
4. kurang contoh kasus untuk 4 aset (bagaimana bentuk matriks kovarians nya)
# Bab 4.2
- [x] tidak perlu ada sub-subbab (langsung dijadikan satu saja)
- [x] menunjukkan persamaan model markowitz dulu dengan menyebut indeks persamaan yang ada di bab 2 (masih salah pemanggilan indeks)
- [x] memberikan penurunan rumus lengkap hingga masuk ke fungsi potensial (tambahkan juga bahwa kita menggunakan aturan setengah dari opsi aset yang tersedia sehingga bobot sama dengan $\sum\omega_i = \sum\frac{x_i}{k} = 1$ sesuai dengan model mean-variance) 
- [x] menyebutkan lampiran A sebagai penjelasan lebih lengkap
- [x] menjabarkan contoh numerik dalam mencari nash eq untuk kasus 2 aset saja (gunakan data yang diberikan pada subbab sebelumnya)
1. kurang matirks payoff
2. kurang pencarian nash eq untuk kasus 4 aset dan matriks payoff nya

# Bab 4.3
- [x] tidak perlu ada sub-subbab (langsung dijadikan satu saja)
- [x] gunakan penurunan rumus lengkap pada [[5_QUBO.md]] (masih kurang lenkap karena harus ada runut penjabaran matematisnya)
- [x] bagaimana bentuk lengkap dari persamaan hamiltonian untuk N=2 dan N=4 (ditunjukkan semua tanpa menggunakan \sum dan indeks i atau j langsung jadi angka numerik dalam bentuk simbolik)
- [x] tunjukkan bentuk hamiltonian dari sampel data yang terdapat pada subbab sebelumnya
1. kurang contoh numerik untuk N=4
# Bab 4.4
- [x] disebutkan gambar rangkaian kuantum yang ada pada gambar F.1 dan I.1 lalu baru masuk ke persaman 4.5 (sebaiknya ditampilkan langsung saja tidak perlu di lampiran tapi menggunakan gambar depth=1 [[2021-05-05_circuit.png]])
- [x] dijabarkan bentuk matematis dari |\langle \psi(\theta) | H | \psi(\theta) \rangle sebagaimana penurunan rumus pada [[6_Gradient_Descent.md]]
- [x] tidak perlu disebutkan warm-start terlebih dahulu (biarkan menjadi "arsitektur ansatz dalam VQE")
- [x] definisikan $U_{rot}^{(L)}(\theta)$ sebagai sebagai gerbang awal (langkah pertama di setiap iterasi) sampai ke bentuk matriksnya  
- [x] jabarkan bentuk matriksnya untuk contoh N=2 dengan depth=1 (berarti 2 layer) (matriks lengkap termasuk matriks rotasi dan entanglement)
1. harusnya ada tensor product nya
2. kurang contoh jumlah aset N=4(?)
3. contoho numeriknya kurang konkrit
# Bab 4.5
- [x] sebaiknya letakkan penjelasan learning ke dalam bab 4.6
- [x] isi bab 4.5 dengan rumus gradien yang dilengkapi dan pembuktian bahwa parameter shift rule merupakan gradien juga yang mana digunakan sebagai gradient descent untuk moda optimasi dasar (yang kemudian diupgrade menjadi SPSA agar lebih efisien)
- [x] ambil persaamaan $U_{rot}^{(L)}(\theta)$ lalu lakukan langkah pertama p ada setiap iterasi yaitu mencari gradien pada gerbang R_z terlebih dahulu (sesuai dengan sirkuit kuantum) hingga mendapatkan gradiennya yaitu $i/2\langle\psi(\theta)|[\sigma_zH|]\psi(\theta)\rangle$  lalu dihubungkan dengan pergeseran positif dan negatif untuk selanjutnya dikurnagi dan mendapatkan $i\langle\psi(\theta)|[\sigma_zH|]\psi(\theta)\rangle$ sehingga saat disubstitusi akan menjadi parameter shift rule
- [x] gunakan penurunan rumus pada [[6_Gradient_Descent.md]] secara lengkap
- [x] tambahkan juga contoh numerik optimasi ini dalam mengupdate parameter theta pada gradient descent 
1. contoh numeriknya kurang konkrit (harus manual)

# Bab 4.6
- [x] sebut persamaan parameter shift rule di subbab sebelumnya lalu aplikasikan ke fungsi optimasi spsa pada umumnya.
- [x] jelaskan juga tentang distribusi bernoulli dan jelaskan alasannya
- [x] jelaskan juga secara numerik mengapa optimasi spsa akan lebih cepat daripada gradient descent
- [x] gunakan file [[7_SPSA.md]] sebagai referensi penurunan rumus (mulai dari ekspansi deret taylor lalu digunakan untuk estimasi \hat{g})
- [x] tambahkan juga contoh numerik optimasi ini dalam mengupdate parameter theta
- [x] tambahkan hasil energi paling optimal yang didapat seperti pada subbab 4.10 yang memberikan energi untuk setiap status
1. penurunan rumusnya kurang konkrit (harus manual)

# Bab 4.7
- [x] aku ingin bab ini jelas: yaitu mendeteksi perubahan distribusi probabilitas yang ada pada lampiran D dan G (saat probabilitasnya sama, maka entropinya akan tinggi. tapi saat probabilitas tinggi satu, maka entropinya akan rendah)
- [x] berikan contoh numerik untuk entropi tinggi dengan menyebut gambar D.18 (dengan Game theory untuk entropi rendah dan tanpa game theory untuk entropi tinggi)
- [x] tambahkan proses matematis perhitungan entropi von neumann untuk iterasi terakhi dengan sampel data yang telah diproses pada subbab sebelumnya
1. kurang contoh numerik untuk aset N=4

# Bab 4.8
- [x] ganti judulnya agar menjadi umum seperti "analisis stabilitas penggunaan EPG sebagai warm-start" (tidak hanya entropi saja)
- [x] tambahkan jua analisa konvergensi spsa dan depth ke berapa yang paling optimal sesuai data yang ada di `/home/asus/Documents/DreamyTA/Latex/TA/GTQuantumInvest/Hasil_N*_**GT/laporan_backtest_N2.txt` (aku ingin menunjukkan bahwa dengan warm-start, depth yang terpilih banyak di angka kecil yang menandakan bahwa daya komputasinya bisa lebih sedikit)
- [x] sebaiknya tidak perlu ada persamaan 4.9 karena kita tidak membahas entropi perturbasi
1. jangan ada penyebutan file .txt
2. apa mungkin gak perlu ya soalnya udah masuk ke 4.11
# Bab 4.9
- [x] aku ingin tujuannya jelas: semakin banyak depth artinya semakin tinggi ekspresibilitas namun sangat rentan terkena barren plateau
- [x] ditunjukkan secara matematis dengan contoh N=2 mengapa bisa meningkatkan ekspresibilitas namun rentan barren plateau
- [x] ditunjukkan secara matematis dengan contoh N=4 mengapa bisa meningkatkan ekspresibilitas namun rentan barren plateau lebih tinggi
- [x] tambahkan proses perhitungan numerik dari sampel data yang diproses pada subbab sebelumnya. berikan juga perbedaan varians gradien tinggi (berarti tidak barren plateau) dan varians gradien sangat rendah (berarti mungkin saja terjebak di barren plateau)
1. masih butuh contoh numerik yang menggunakan matriks atau apapun yang merepresentasikan ekspresibilitas

# Bab 4.10
- [x] aku ingin tujuannya jelas: menunjukkan bahwa brute force hanya sekedar validator yang dapat bekerja optimal di N kecil namun tidak akan optimal di N besar (seperti 100 ke atas).
- [x] sebaiknya tidak perlu ada "probabilitas kuantum" hanya fokus ke algoritma brute force saja yang dilengkapi dengan contoh numerik sampel data dari subbab sebelumnya (butuh proses matematis menggunakan data yang diproses sebelumnya)
1. contoh numeriknya kurang konkrit

# Bab 4.11
- [x] lengkapi bab nya dengan tabel berisi data yang ada di `/home/asus/Documents/DreamyTA/Latex/TA/GTQuantumInvest/Hasil_N*_**GT/laporan_backtest_N2.txt` (tambahkan juga baris unttuk VQE (tanpa GT))
- [x] berikan penjelasan bahwa VQE akan lebih bagus secara performa saat ditambahkan warm-start menggunakan algoritma EPG
- [x] tambahkan juga tabel tersebut untuk N=4
- [x] baris equal weight dan ihsg nilainya sama. tabelnya harus diperbaiki supaya lebih rapi dan efisien
1. tabelnya kok masih jelek ya
# Bab 4.12
- [x] dijelaskan bagaimana algoritma rebalancingnya alih-alih menjelaskan persamaan 4.13
- [x] (Selesai)
- [x] masukkan saja gambar F.3, F.4, F.5 untuk N=2 dan I.3, I.4, I.5 untuk N=4 (sehingga gambar tersebut di lampiran bisa dihilangkan)
