# Template TA ITS v.1.0

## Deskripsi

Template ini dibuat khusus dalam format LaTeX untuk mempermudah mahasiswa/i 
dalam penyusunan laporan tugas akhir (TA) di lingkungan [Institut Teknologi
Sepuluh Nopember (ITS)](https://www.its.ac.id/), 
khususnya di [Departemen Fisika](https://www.its.ac.id/fisika/).

> Template ini **bukanlah template resmi** dari ITS, namun dibuat sedemikian rupa
sehingga sesuai dengan pedoman penyusunan laporan TA yang dibuat oleh
Departemen Fisika, ITS.

Template ini dapat digunakan dengan bebas (dan bertanggung jawab) dan dapat 
disesuaikan untuk berbagai keperluan.

Template ini dapat dijalankan dengan menggunakan *compiler* LuaLaTeX untuk 
menghasilkan *file* TA dalam format `*.pdf`. Untuk mempermudah penggunaan
template ini, kami sangat menyarankan *user* untuk menggunakan "Overleaf.com"

## Cara Penggunaan

*User* dapat mengunduh seluruh *file* template TA ini dengan menekan tombol
`code` yang berwarna hijau, kemudian pilih “Download ZIP”. *File* tersebut
kemudian bisa dijalankan baik melalui “Overleaf.com” maupun TeX *editor*
yang biasa digunakan.

Penjelasan lebih lengkap mengenai cara penggunaan template ini dapat dilihat
melalui video berikut ini: [https://youtu.be/ucTR7dgIFiA](https://youtu.be/ucTR7dgIFiA)

## Struktur File

```bash
.
├── halaman-depan             
│   ├── 00-BGcover.jpg
│   ├── 00-Logo-ITS.png
│   ├── abstract.tex
│   ├── abstrak.tex
│   ├── cover.tex
│   ├── daftarGambar.tex
│   ├── daftarIsi.tex
│   ├── daftarTabel.tex
│   ├── kataPengantar.tex
│   └── pengesahan.tex
├── konten
│   ├── bab01.tex
│   ├── bab02.tex
│   ├── bab03.tex
│   ├── bab04.tex
│   └── bab05.tex
├── halaman-belakang
│   ├── biografi.tex
│   └── lampiran
│       └── lampiranA.tex
├── gambar
│   ├── contoh.png
│   ├── flowchart.png
│   └── foto.png
├── pustaka.bib
├── format-pustaka.bst
├── informasi.tex              
├── kodeUnit.tex
├── pengaturan.tex
├── main.tex
└── README.md
```

Template untuk TA ini terdiri dari beberapa bagian, di mana *file* `main.tex`
merupakan bagian utama yang berguna untuk menyatakan dan mengatur kerangka
serta *input* yang digunakan dalam laporan TA. 

Dengan menggunakan template ini, *user* tidak lagi direpotkan untuk mengatur
format dokumen TA, seperti tampilan *cover*, tampilan lembar pengesahan,
jenis huruf, ukuran huruf, jarak spasi, batas tepi halaman (*margin*), daftar
isi, daftar tabel, daftar gambar, daftar pustaka, dan lainnya. 

Sebagai contoh, dengan melengkapi informasi nama, nomor induk, nama dosen pembimbing,
NIP dosen pembimbing, dan seterusnya pada `informasi.tex`, halaman Cover dan
Lembar Pengesahan yang dihasilkan setelah proses kompilasi akan sudah sesuai
dengan format yang ditentukan.

Dengan demikian, *user* dapat lebih fokus kepada penyusunan bagian isi dan
substansi, BAB 1 hingga BAB 5, dari TA yang hendak dilaporkan.

**[`halaman-depan`](./halaman-depan)** berisi *file* `*.tex` dan gambar yang
akan dimuat di bagian depan laporan TA, tepatnya sebelum BAB Pendahuluan.
Abstrak TA ditulis pada *file* `abstrak.tex` (Bahasa Indonesia) dan `abstract.tex`
(Bahasa Inggris).

**[`konten`](./konten)** berisi *file* `*.tex` yang menjadi isi dari laporan TA.

**[`halaman-belakang`](./halaman-belakang)** berisi *file* `biografi.tex` untuk
memuat biografi singkat penulis dan **[`lampiran`](./lampiran)** untuk memuat
lampiran-lampiran.

Kode ringkas untuk simbol, satuan, dan singkatan yang digunakan dalam laporan TA
dapat dideklarasikan pada `kodeUnit.tex`.

## Kontributor

1. Sasfan Arman Wella, BRIN (sasfan.a.wella@gmail.com) 
2. Nadya Amalia, BRIN (amalianadd@gmail.com) 
3. Fitrotul Millah, ITS (fitrotulmillah2000@gmail.com) 
4. Nathasya Veronica, ITS (nathasyaveronica363@gmail.com)

> *Catatan*:
> Silahkan hubungi kami bila ada pertanyaan seputar penggunaan template ini.
Kami pun sangat terbuka bila ada saran/kritik yang bisa menyempurnakan template ini.
