# Panduan Pengguna - Aplikasi Manajemen Inventaris

## Daftar Isi
1. [Pengenalan](#pengenalan)
2. [Instalasi](#instalasi)
3. [Memulai Aplikasi](#memulai-aplikasi)
4. [Fitur-Fitur](#fitur-fitur)
5. [Tips dan Trik](#tips-dan-trik)
6. [Troubleshooting](#troubleshooting)

---

## Pengenalan

Aplikasi Manajemen Inventaris adalah sistem desktop sederhana untuk mengelola data barang/produk. Aplikasi ini cocok untuk:
- Toko kecil dan menengah
- Gudang penyimpanan
- Manajemen aset kantor
- Pembelajaran sistem inventaris

**Fitur Utama:**
- ✓ Sistem login yang aman
- ✓ Tambah, ubah, hapus data barang
- ✓ Tampilan data dalam bentuk tabel
- ✓ Statistik inventaris real-time
- ✓ Database lokal (tidak perlu internet)

---

## Instalasi

### Prasyarat
- **Python 3.x** terinstal di komputer
- **Tkinter** (biasanya sudah termasuk dalam Python)
- **SQLite3** (built-in Python)

### Langkah Instalasi

#### Windows

1. **Download Python**
   - Kunjungi: https://www.python.org/downloads/
   - Download Python 3.x (versi terbaru)
   - Jalankan installer
   - ✓ Centang "Add Python to PATH"
   - ✓ Centang "tcl/tk and IDLE"
   - Klik "Install Now"

2. **Verifikasi Instalasi**
   ```cmd
   python --version
   ```
   Output: `Python 3.x.x`

3. **Download Aplikasi**
   - Extract file ZIP ke folder pilihan Anda
   - Contoh: `C:\Users\YourName\Documents\InventarisApp`

#### Linux (Ubuntu/Debian)

1. **Install Python dan Tkinter**
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk
   ```

2. **Verifikasi Instalasi**
   ```bash
   python3 --version
   ```

3. **Download Aplikasi**
   - Extract file ke folder pilihan
   - Contoh: `~/Documents/InventarisApp`

---

## Memulai Aplikasi

### Windows

1. Buka **Command Prompt** atau **PowerShell**
2. Navigate ke folder aplikasi:
   ```cmd
   cd C:\path\to\InventarisApp
   ```
3. Jalankan aplikasi:
   ```cmd
   python main.py
   ```

### Linux

1. Buka **Terminal**
2. Navigate ke folder aplikasi:
   ```bash
   cd ~/path/to/InventarisApp
   ```
3. Jalankan aplikasi:
   ```bash
   python3 main.py
   ```

### Shortcut (Opsional)

**Windows:**
- Buat file `run.bat`:
  ```batch
  @echo off
  python main.py
  pause
  ```
- Double-click `run.bat` untuk menjalankan

**Linux:**
- Buat file `run.sh`:
  ```bash
  #!/bin/bash
  python3 main.py
  ```
- Beri permission: `chmod +x run.sh`
- Jalankan: `./run.sh`

---

## Fitur-Fitur

### 1. Registrasi User Baru

**Langkah:**
1. Jalankan aplikasi
2. Window login akan muncul
3. Masukkan **Username** (5-20 karakter, hanya huruf dan angka)
4. Masukkan **Password** (minimal 8 karakter, harus ada huruf besar, kecil, dan angka)
5. Klik tombol **"Register"**
6. Jika berhasil, akan muncul pesan "Registrasi berhasil"

**Contoh:**
- Username: `admin`
- Password: `Admin123`

**Ketentuan Password:**
- ✓ Minimal 8 karakter
- ✓ Mengandung huruf BESAR (A-Z)
- ✓ Mengandung huruf kecil (a-z)
- ✓ Mengandung angka (0-9)

**Contoh Password Valid:**
- `Admin123` ✓
- `Password1` ✓
- `Inventaris2024` ✓

**Contoh Password Invalid:**
- `admin123` ✗ (tidak ada huruf besar)
- `ADMIN123` ✗ (tidak ada huruf kecil)
- `AdminPass` ✗ (tidak ada angka)
- `Admin1` ✗ (kurang dari 8 karakter)

---

### 2. Login

**Langkah:**
1. Masukkan **Username** yang sudah terdaftar
2. Masukkan **Password**
3. Klik tombol **"Login"**
4. Jika berhasil, window inventaris akan terbuka

**Tips:**
- Username dan password bersifat **case-sensitive**
- Pastikan Caps Lock tidak aktif
- Jika lupa password, tidak ada fitur reset (untuk keamanan)

---

### 3. Menambah Item Baru

**Langkah:**
1. Setelah login, Anda akan melihat form input
2. Isi data item:
   - **Nama Item**: Nama produk/barang (minimal 3 karakter)
   - **Jumlah**: Jumlah stok (harus angka bulat, tidak boleh negatif)
   - **Harga**: Harga per unit dalam Rupiah (harus angka, tidak boleh negatif)
3. Klik tombol **"Tambah"**
4. Item akan muncul di tabel

**Contoh:**
- Nama Item: `Laptop Dell XPS 13`
- Jumlah: `5`
- Harga: `15000000`

**Validasi:**
- ✓ Nama tidak boleh kosong
- ✓ Jumlah harus integer positif
- ✓ Harga harus numeric positif

---

### 4. Mengubah/Update Item

**Langkah:**
1. **Klik** item di tabel yang ingin diubah
2. Data item akan otomatis muncul di form input
3. Ubah data yang diinginkan
4. Klik tombol **"Update"**
5. Konfirmasi perubahan

**Tips:**
- Pastikan item sudah dipilih (highlight di tabel)
- Semua field harus diisi
- Validasi sama seperti saat menambah item

---

### 5. Menghapus Item

**Langkah:**
1. **Klik** item di tabel yang ingin dihapus
2. Klik tombol **"Hapus"**
3. Dialog konfirmasi akan muncul
4. Klik **"Yes"** untuk konfirmasi
5. Item akan dihapus dari database

**Peringatan:**
- ⚠️ Penghapusan bersifat **permanen**
- ⚠️ Data yang sudah dihapus **tidak dapat dikembalikan**
- ⚠️ Pastikan item yang dipilih sudah benar

---

### 6. Clear Form

**Fungsi:**
- Membersihkan semua field input
- Menghapus selection item di tabel
- Berguna untuk memulai input baru

**Cara:**
- Klik tombol **"Clear"**

---

### 7. Statistik Inventaris

**Informasi yang Ditampilkan:**
- **Total Item**: Jumlah total semua barang di inventaris
- **Total Nilai**: Nilai total inventaris (Jumlah × Harga)

**Lokasi:**
- Di bagian bawah window, background biru muda

**Update:**
- Statistik otomatis terupdate setiap kali ada perubahan data

---

## Tips dan Trik

### 1. Keyboard Shortcuts

- **Enter** di field Username/Password → Login
- **Tab** → Pindah antar field
- **Esc** → Close dialog

### 2. Format Input

**Harga:**
- Bisa input tanpa titik: `5000000`
- Bisa input dengan titik: `5000000.50`
- Tampilan otomatis diformat: `Rp 5.000.000`

**Jumlah:**
- Hanya angka bulat: `10`, `100`, `1000`
- Tidak boleh desimal: `10.5` ✗

### 3. Backup Data

**Manual Backup:**
1. Tutup aplikasi
2. Copy file `database/inventaris.db`
3. Simpan di lokasi aman

**Restore:**
1. Tutup aplikasi
2. Replace file `database/inventaris.db` dengan backup
3. Jalankan aplikasi kembali

### 4. Multi-User

**Cara:**
- Setiap user harus registrasi dengan username berbeda
- Satu database digunakan bersama
- Semua user dapat melihat dan mengubah data yang sama

---

## Troubleshooting

### Problem 1: "No module named 'tkinter'"

**Solusi Windows:**
1. Uninstall Python
2. Download installer Python terbaru
3. Saat install, centang "tcl/tk and IDLE"
4. Install ulang

**Solusi Linux:**
```bash
sudo apt-get install python3-tk
```

---

### Problem 2: "Database is locked"

**Penyebab:**
- Aplikasi masih berjalan di background
- File database sedang diakses program lain

**Solusi:**
1. Tutup semua instance aplikasi
2. Restart komputer (jika perlu)
3. Jalankan aplikasi kembali

---

### Problem 3: "Permission denied"

**Penyebab:**
- Folder tidak memiliki write permission

**Solusi Windows:**
1. Klik kanan folder aplikasi
2. Properties → Security
3. Edit → Allow "Full control"

**Solusi Linux:**
```bash
chmod -R 755 /path/to/InventarisApp
```

---

### Problem 4: Window Tidak Muncul

**Solusi:**
1. Cek apakah ada error di terminal/command prompt
2. Pastikan Python dan Tkinter terinstal
3. Coba jalankan dengan verbose:
   ```bash
   python -v main.py
   ```

---

### Problem 5: Data Hilang

**Penyebab:**
- File database terhapus atau corrupt

**Solusi:**
1. Restore dari backup (jika ada)
2. Jika tidak ada backup, database akan dibuat baru (kosong)
3. Input ulang data

**Pencegahan:**
- Backup database secara berkala
- Jangan hapus file `inventaris.db`

---

### Problem 6: Lupa Password

**Solusi:**
⚠️ Tidak ada fitur reset password untuk keamanan

**Opsi:**
1. Registrasi user baru dengan username berbeda
2. Atau, hapus database dan mulai dari awal:
   ```bash
   # Backup dulu jika perlu
   rm database/inventaris.db
   # Jalankan aplikasi, database baru akan dibuat
   ```

---

## FAQ (Frequently Asked Questions)

**Q: Apakah aplikasi ini memerlukan internet?**  
A: Tidak. Aplikasi ini sepenuhnya offline dan menggunakan database lokal.

**Q: Berapa maksimal item yang bisa disimpan?**  
A: SQLite dapat menyimpan jutaan record. Praktisnya, tergantung kapasitas storage komputer.

**Q: Apakah bisa digunakan di Mac?**  
A: Ya, dengan Python dan Tkinter terinstal. Langkah sama seperti Linux.

**Q: Apakah data aman?**  
A: Password di-hash dengan SHA-256. Data tersimpan lokal di komputer Anda.

**Q: Bisa export ke Excel?**  
A: Fitur ini belum tersedia di versi saat ini. Bisa dikembangkan lebih lanjut.

**Q: Bisa print laporan?**  
A: Fitur ini belum tersedia di versi saat ini. Bisa dikembangkan lebih lanjut.

---

## Kontak Support

Jika mengalami masalah yang tidak tercantum di panduan ini:

- **Email:** [email-support]
- **GitHub Issues:** [repository-url]/issues
- **Dokumentasi:** Baca README.md dan TESTING.md

---

**Selamat menggunakan Aplikasi Manajemen Inventaris!**

© 2024 - Proyek Akhir Teknik Informatika
