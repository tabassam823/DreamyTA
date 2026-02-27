#!/bin/bash

# Menghapus file sisa kompilasi sebelumnya
# rm *.aux *.bbl *.blg *.log *.out

echo "--- Memulai Kompilasi Tahap 1 (XeLaTeX) ---"
xelatex -interaction=nonstopmode main.tex         

echo "--- Memproses Sitasi (BibTeX) ---"
bibtex main        

echo "--- Memulai Kompilasi Tahap 2 (XeLaTeX) ---"
xelatex -interaction=nonstopmode main.tex         

echo "--- Memulai Kompilasi Tahap 3 (Final XeLaTeX) ---"
xelatex -interaction=nonstopmode main.tex         

echo "--- Selesai! File PDF siap diperiksa. ---"
