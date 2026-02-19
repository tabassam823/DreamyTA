# Catatan Evaluasi Presentasi Analisis Numerik

Berdasarkan hasil presentasi yang ada pada [[presentasi_analisis_numerik.pdf]] dan sumber kode [[, berikut adalah poin-poin evaluasi yang perlu diperbaiki pada slide:

1. **Slide 6 (Statistik Data)**:
   - Tambahkan penjelasan rumus untuk setiap kolom tabel, terutama kolom **"% Naik"** yang masih bersifat ambigu.
   - Berikan keterangan tambahan terkait urgensi atau alasan mengapa tabel statistik tersebut perlu ditampilkan dalam konteks optimasi ini.

2. **Slide 7 (Risk Aversion & Utilitas Markowitz)**:
   - Mengingat audiens adalah mahasiswa Fisika dan Matematika, tambahkan penurunan rumus **Lagrangian Multiplier** untuk *risk aversion endogen*.
   - Tambahkan penurunan rumus fungsi utilitas Markowitz yang diturunkan dari fungsi biaya (*cost function*) Markowitz.

3. **Slide 8 (Matriks Payoff)**:
   - Sediakan satu contoh perhitungan konkret pada salah satu sel di tabel matriks payoff agar audiens dapat memahami proses transformasi nilai return ke dalam matriks.

4. **Slide 9 (Parameter Hamiltonian)**:
   - Tambahkan penjelasan mengenai bagaimana matriks densitas dihitung berdasarkan nilai-nilai yang telah ditampilkan pada slide sebelumnya.

5. **Slide 10 (Interpretasi Hasil Numerik)**:
   - Berikan penjelasan logis mengenai fenomena di mana **bias bernilai negatif namun korelasi bernilai positif**.
   - Perjelas interpretasi terkait penentuan sifat model game agar tidak ambigu (hubungkan dengan tabel hubungan aset di slide sebelumnya) dan jelaskan signifikansi fisik/ekonomi dari bias negatif tersebut.

6. **Slide 11 (Analisis Entropi & QMI)**:
   - Sertakan contoh perhitungan manual/langkah demi langkah untuk nilai **S (Entropy)** dan **QMI** agar audiens memahami alur matematis di baliknya.

7. **Slide 14-15 (Hasil & Implementasi)**:
   - Analisis ulang hasil yang kurang optimal; pertimbangkan untuk menghilangkan parameter **shots** jika memang mengganggu akurasi atau tidak diperlukan.
   - Pada grafik distribusi state terhadap probabilitas, fokuskan hanya pada pilihan aset "2 dari 4". Hilangkan opsi pemilihan aset yang tidak sesuai (pilihan 1, 3, atau 4) dari grafik untuk memperjelas hasil.

8. **Struktur Akhir**:
   - Hapus bagian **Kesimpulan dan Diskusi** karena tidak diperlukan.
