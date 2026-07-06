#!/bin/bash

# DreamyTA QPCA execution script
# Skrip ini menjalankan simulasi QPCA dan menyimpan hasilnya dalam bentuk gambar .png

echo "--------------------------------------------------"
echo "Memulai simulasi QPCA (Quantum Principal Component Analysis)"
echo "--------------------------------------------------"

# 1. Menjalankan QPCA_eigenstate.py
echo "[1/3] Menjalankan QPCA_eigenstate.py..."
python3 QPCA_eigenstate.py
echo "Selesai. Hasil disimpan di qpca_eigenstate_result.png"
echo ""

# 2. Menjalankan QPCA_4x4eigenstate.py
echo "[2/3] Menjalankan QPCA_4x4eigenstate.py..."
python3 QPCA_4x4eigenstate.py
echo "Selesai. Hasil disimpan di qpca_4x4_result.png"
echo ""

# 3. Menjalankan QPCA_QPhE.py
echo "[3/3] Menjalankan QPCA_QPhE.py..."
python3 QPCA_QPhE.py
echo "Selesai. Hasil disimpan di qpca_qphe_result.png"
echo ""

echo "--------------------------------------------------"
echo "Semua simulasi berhasil dijalankan!"
echo "Silakan periksa folder ini untuk file gambar (.png) hasil plot."
echo "--------------------------------------------------"
