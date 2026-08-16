@echo off
REM Batch script untuk menjalankan Aplikasi Manajemen Inventaris di Windows
REM Double-click file ini untuk menjalankan aplikasi

echo ============================================================
echo APLIKASI MANAJEMEN INVENTARIS
echo Proyek Akhir - Teknik Informatika
echo ============================================================
echo.

REM Cek apakah Python terinstal
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu dari https://www.python.org
    echo.
    pause
    exit /b 1
)

echo [INFO] Python terdeteksi
echo [INFO] Memulai aplikasi...
echo.

REM Jalankan aplikasi
python main.py

REM Jika aplikasi ditutup
echo.
echo [INFO] Aplikasi telah ditutup
pause
