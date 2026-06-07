#!/bin/bash

# Pindah ke direktori PPT jika skrip dijalankan dari root
cd "$(dirname "$0")"

echo "===================================================="
echo "🚀 Memulai Kompilasi Presentasi LaTeX (Beamer)"
echo "===================================================="

# Nama file utama tanpa ekstensi
FILENAME="main"

# Membersihkan file sementara lama
echo "🧹 Membersihkan file residu lama..."
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.pdf

# Kompilasi Tahap 1: Generate file aux dan toc
echo "📥 Kompilasi Tahap 1..."
pdflatex -interaction=nonstopmode $FILENAME.tex > /dev/null

# Kompilasi Tahap 2: Finalisasi (untuk daftar isi dan referensi silang)
echo "📥 Kompilasi Tahap 2..."
pdflatex -interaction=nonstopmode $FILENAME.tex > /dev/null

if [ $? -eq 0 ]; then
    echo "===================================================="
    echo "✅ Berhasil! File presentasi siap: $FILENAME.pdf"
    echo "===================================================="
else
    echo "===================================================="
    echo "❌ Terjadi kesalahan saat kompilasi."
    echo "🔍 Silakan periksa file main.log untuk detailnya."
    echo "===================================================="
fi
