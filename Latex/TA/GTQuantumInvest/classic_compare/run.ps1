# Pastikan berada di direktori script
Set-Location $PSScriptRoot

Write-Host "Memulai Batch Classic Markowitz Comparison (N=2 ke N=12)..." -ForegroundColor Cyan

# Deteksi Python
$PythonPath = "python"
if (Test-Path "..\venv\Scripts\python.exe") {
    $PythonPath = (Resolve-Path "..\venv\Scripts\python.exe").Path
    Write-Host "Menggunakan Virtual Environment: $PythonPath" -ForegroundColor Green
}

# Jalankan main.py untuk semua N
& $PythonPath main.py

Write-Host ""
Write-Host "SELURUH PROSES CLASSIC COMPARISON SELESAI." -ForegroundColor Cyan
