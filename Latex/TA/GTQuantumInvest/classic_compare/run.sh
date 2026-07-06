#!/bin/bash

# Pastikan berada di direktori script
cd "$(dirname "$0")"

echo "Memulai Batch Classic Markowitz Comparison (N=2 ke N=12)..."

# Deteksi Python
PYTHON_CMD="python3"
if [ -f "../venv/Scripts/python" ]; then
    PYTHON_CMD="../venv/Scripts/python"
elif [ -f "../venv/bin/python" ]; then
    PYTHON_CMD="../venv/bin/python"
fi

# Jalankan main.py untuk semua N
$PYTHON_CMD main.py

echo ""
echo "SELURUH PROSES CLASSIC COMPARISON SELESAI."
