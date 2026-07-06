# Daftar file main yang akan dijalankan
$MainFiles = @("main_N2.py", "main_N4.py")

# Deteksi Python path
$PythonPath = "python"
if (Test-Path ".\venv\Scripts\python.exe") {
    $PythonPath = (Resolve-Path ".\venv\Scripts\python.exe").Path
    Write-Host "Menggunakan Virtual Environment: $PythonPath" -ForegroundColor Green
}

# Konfigurasi Mode (Warm-Start GT vs NoGT)
$Modes = @(
    @{Value = "True"; Suffix = "GT"},
    @{Value = "False"; Suffix = "NoGT"}
)

foreach ($Mode in $Modes) {
    $SuffixMode = $Mode.Suffix
    $ValMode = $Mode.Value
    
    Write-Host "`n====================================================" -ForegroundColor Cyan
    Write-Host "RUNNING MODE: $SuffixMode (Warm-Start = $ValMode)" -ForegroundColor Cyan
    Write-Host "====================================================`n" -ForegroundColor Cyan

    # 0. Update config.py secara dinamis
    Write-Host "Mengatur use_warm_start ke $ValMode di config.py..." -ForegroundColor Gray
    (Get-Content config.py) -replace "'use_warm_start': .*", "'use_warm_start': $ValMode," | Set-Content config.py

    Write-Host "Memulai Parallel Simulation untuk N=2 sampai N=12..." -ForegroundColor Cyan

    $Jobs = @()
    foreach ($Script in $MainFiles) {
        if (Test-Path $Script) {
            Write-Host "Memulai background process: $Script" -ForegroundColor Gray
            # Pastikan path absolut untuk script agar job tidak bingung folder kerja
            $ScriptAbsPath = (Resolve-Path $Script).Path
            
            # Menggunakan Start-Job dengan ArgumentList yang lebih aman
            $Jobs += Start-Job -ScriptBlock { 
                param($py, $s) 
                Set-Location $using:PWD
                & $py $s 
            } -ArgumentList $PythonPath, $ScriptAbsPath
        }
    }

    Write-Host "Menunggu semua simulasi mode $SuffixMode selesai..." -ForegroundColor Yellow
    $WaitCount = 0
    while ($Jobs | Where-Object { $_.State -eq 'Running' }) {
        Start-Sleep -Seconds 10
        $WaitCount += 10
        $RunningCount = ($Jobs | Where-Object { $_.State -eq 'Running' }).Count
        Write-Host "[$WaitCount detik] Masih berjalan: $RunningCount proses..." -ForegroundColor Gray
        
        # Ambil output secara berkala agar tidak menumpuk di memori
        foreach ($Job in $Jobs) {
            Receive-Job -Job $Job | Out-String | Write-Host -ForegroundColor Gray
        }
    }

    # Cek hasil akhir job
    foreach ($Job in $Jobs) {
        if ($Job.State -eq "Failed") {
            Write-Host "Job $($Job.Name) GAGAL total!" -ForegroundColor Red
        }
        # Ambil sisa output/error
        Receive-Job -Job $Job -ErrorAction SilentlyContinue | Out-String | Write-Host
    }

    Write-Host "----------------------------------------------------"
    Write-Host "Simulasi mode $SuffixMode selesai. Mengorganisir hasil..." -ForegroundColor Cyan

    # Folder Induk: Hasil_GT atau Hasil_NoGT
    $MasterFolderName = "Hasil_$SuffixMode"
    if (Test-Path $MasterFolderName) {
        Write-Host "Menghapus folder lama $MasterFolderName..." -ForegroundColor Gray
        Remove-Item -Path $MasterFolderName -Recurse -Force
    }
    New-Item -Path $MasterFolderName -ItemType Directory | Out-Null

    foreach ($Script in $MainFiles) {
        if ($Script -match "main_N(\d+)\.py") {
            $N = $Matches[1]
        } else {
            continue
        }

        # Nama folder sub-hasil: Hasil_N*_GT atau Hasil_N*_NoGT
        $SubFolderName = "Hasil_N${N}_$SuffixMode"
        $SuffixVal = "_N$N"
        $AnalisisDir = "Analisis_Window_N$N"

        # 1. Buat sub-folder hasil jika belum ada
        if (-not (Test-Path $SubFolderName)) {
            New-Item -Path $SubFolderName -ItemType Directory | Out-Null
        }

        # 2. Pindahkan semua file yang memiliki suffix _NX (termasuk intermediate, utama, dan ekuitas)
        Get-Item "*$SuffixVal*" -Exclude "*.py" -ErrorAction SilentlyContinue | Move-Item -Destination "$SubFolderName/" -Force -ErrorAction SilentlyContinue

        # 3. Pindahkan folder analisis jendela ke dalam SubFolderName
        if (Test-Path $AnalisisDir) {
            if (Test-Path "$SubFolderName/$AnalisisDir") {
                Remove-Item -Path "$SubFolderName/$AnalisisDir" -Recurse -Force
            }
            Move-Item -Path $AnalisisDir -Destination "$SubFolderName/" -Force
        }

        # 4. Masukkan SubFolderName ke dalam MasterFolderName
        Move-Item -Path $SubFolderName -Destination "$MasterFolderName/" -Force

        Write-Host "Selesai merapikan $SubFolderName ke dalam $MasterFolderName." -ForegroundColor Green
    }

    # Bersihkan Job untuk batch berikutnya
    Remove-Job -Job $Jobs
}

Write-Host "`nSELURUH PROSES SIMULASI (GT & NoGT) TELAH SELESAI." -ForegroundColor Cyan
