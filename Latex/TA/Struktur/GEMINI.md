# Instruksi Pemetaan Struktur (Daster)

File ini mengatur prosedur konversi dan pemetaan konten dari file LaTeX di `/Contents/Daster/` ke dalam format analisis Markdown di folder `/Struktur/`.

## 1. Format File Output

### A. Header Utama
Gunakan `# [Nomor Subbab] [Judul Subbab]`.

### B. Analisis Paragraf
Setiap paragraf diidentifikasi berdasarkan tujuan spesifiknya yang ditulis dalam kurung.
**Format Header Paragraf:** `### Paragraf [n] ([Tujuan Paragraf])`

Setiap unit kalimat disusun untuk mendukung tujuan tersebut:
1. **[Ringkasan Isi Kalimat]**: Inti informasi atau narasi.
2. **> [Tujuan Kalimat]**: Penjelasan mengapa kalimat tersebut ada (sebagai latar belakang, pendukung, jembatan, atau kesimpulan).

**Pola Penulisan:**
- Kalimat dapat bersifat sekuensial (lanjutan dari sebelumnya).
- Tidak harus setiap kalimat berdiri sendiri sebagai jawaban mandiri.

### C. Tabel Q&A
Tabel digunakan untuk merangkum poin-poin paling krusial dalam paragraf tersebut.
**Aturan Tabel:**
- **Tidak semua kalimat wajib masuk ke tabel.**
- Hanya pilih kalimat yang mengandung informasi kunci atau data teknis yang perlu diverifikasi.
- Fokus pada ekstraksi jawaban yang presisi dari teks.

### D. Saran Gambar (Opsional)
Jika sebuah paragraf menjelaskan konsep yang sangat terbantu dengan visualisasi (misalnya: grafik, diagram sirkuit, atau geometri), tambahkan baris saran gambar.
**Format:** `` `Gambar: [Deskripsi Singkat Gambar]` ``
**Penempatan:** Letakkan tepat di bawah poin kalimat yang paling relevan dengan visualisasi tersebut, sebelum tabel Q&A.

## 2. Prinsip Penulisan Baru
- **Target Oriented**: Seluruh kalimat dalam satu blok paragraf harus bekerja sama untuk mencapai target yang tertulis di dalam kurung sebelah nama paragraf.
- **Fleksibilitas Narasi**: Kalimat boleh berfungsi hanya sebagai pendukung atau transisi logis agar alur "kisah" Dasar Teori mengalir dengan baik.
- **Ringkas & Tepat**: Fokus pada ekstraksi logika, bukan penyalinan kata per kata dari LaTeX.
- **Bahasa**: Santai namun tetap akurat secara teknis.

## 3. Alur Kerja
1. Baca file LaTeX asal.
2. Tentukan "Kisah/Tujuan" dari setiap paragraf dan tuliskan dalam kurung di header.
3. Pecah paragraf menjadi unit-unit kalimat yang saling mendukung.
4. Identifikasi poin kunci untuk dimasukkan ke tabel Q&A.
