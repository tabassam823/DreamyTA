#!/bin/bash

# Daftar file main yang akan dijalankan
MAIN_FILES=("main_N2.py" "main_N4.py" "main_N6.py" "main_N8.py" "main_N10.py" "main_N12.py")

# Deteksi Python path
PYTHON_CMD="python3"
if [ -f "./venv/Scripts/python" ]; then
    PYTHON_CMD="./venv/Scripts/python"
elif [ -f "./venv/bin/python" ]; then
    PYTHON_CMD="./venv/bin/python"
fi
echo "Menggunakan Python: $PYTHON_CMD"

# Konfigurasi Mode (Warm-Start GT vs NoGT)
MODES=("True" "False")
SUFFIXES=("GT" "NoGT")

for i in "${!MODES[@]}"; do
    VAL_MODE="${MODES[$i]}"
    SUFFIX_MODE="${SUFFIXES[$i]}"
    
    echo ""
    echo "===================================================="
    echo "RUNNING MODE: $SUFFIX_MODE (Warm-Start = $VAL_MODE)"
    echo "===================================================="
    echo ""

    # 0. Update config.py secara dinamis
    echo "Mengatur use_warm_start ke $VAL_MODE di config.py..."
    sed -i "s/'use_warm_start': .*/'use_warm_start': $VAL_MODE,/" config.py

    echo "Memulai Parallel Simulation untuk N=2 sampai N=12..."

    for SCRIPT in "${MAIN_FILES[@]}"; do
        if [ ! -f "$SCRIPT" ]; then
            echo "Peringatan: $SCRIPT tidak ditemukan, melewati..."
            continue
        fi
        echo "Memulai background process: $SCRIPT"
        $PYTHON_CMD "$SCRIPT" &
    done

    echo "Menunggu semua simulasi mode $SUFFIX_MODE selesai..."
    wait

    echo "----------------------------------------------------"
    echo "Simulasi mode $SUFFIX_MODE selesai. Mengorganisir hasil..."

    # Folder Induk: Hasil_GT atau Hasil_NoGT
    MASTER_FOLDER_NAME="Hasil_$SUFFIX_MODE"
    if [ -d "$MASTER_FOLDER_NAME" ]; then
        rm -rf "$MASTER_FOLDER_NAME"
    fi
    mkdir -p "$MASTER_FOLDER_NAME"

    for SCRIPT in "${MAIN_FILES[@]}"; do
        if [[ $SCRIPT =~ main_N([0-9]+)\.py ]]; then
            N="${BASH_REMATCH[1]}"
        else
            continue
        fi

        # Nama folder sub-hasil: Hasil_N*_GT atau Hasil_N*_NoGT
        SUB_FOLDER_NAME="Hasil_N${N}_$SUFFIX_MODE"
        SUFFIX_VAL="_N$N"
        ANALISIS_DIR="Analisis_Window_N$N"

        mkdir -p "$SUB_FOLDER_NAME"

        # Pindahkan semua file yang memiliki suffix _NX (termasuk ekuitas)
        for f in *"$SUFFIX_VAL"*; do
            if [ -f "$f" ] && [[ "$f" != *.py ]]; then
                mv "$f" "$SUB_FOLDER_NAME/" 2>/dev/null
            fi
        done

        if [ -d "$ANALISIS_DIR" ]; then
            rm -rf "$SUB_FOLDER_NAME/$ANALISIS_DIR"
            mv "$ANALISIS_DIR" "$SUB_FOLDER_NAME/"
        fi

        mv "$SUB_FOLDER_NAME" "$MASTER_FOLDER_NAME/"
        echo "Selesai merapikan $SUB_FOLDER_NAME."
    done
done

echo ""
echo "SELURUH PROSES SIMULASI (GT & NoGT) TELAH SELESAI."
