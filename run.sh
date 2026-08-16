#!/bin/bash
# Shell script untuk menjalankan Aplikasi Manajemen Inventaris di Linux/Mac
# Jalankan dengan: ./run.sh

echo "============================================================"
echo "APLIKASI MANAJEMEN INVENTARIS"
echo "Proyek Akhir - Teknik Informatika"
echo "============================================================"
echo ""

# Cek apakah Python terinstal
if ! command -v python3 &> /dev/null
then
    echo "[ERROR] Python3 tidak ditemukan!"
    echo "Silakan install Python3 terlebih dahulu"
    echo "Ubuntu/Debian: sudo apt-get install python3 python3-tk"
    exit 1
fi

echo "[INFO] Python3 terdeteksi"
echo "[INFO] Memulai aplikasi..."
echo ""

# Jalankan aplikasi
python3 main.py

# Jika aplikasi ditutup
echo ""
echo "[INFO] Aplikasi telah ditutup"
