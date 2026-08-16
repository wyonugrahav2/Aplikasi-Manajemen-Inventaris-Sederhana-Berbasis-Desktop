# Quick Start Guide - Aplikasi Manajemen Inventaris

## 🚀 Mulai Cepat (5 Menit)

### Windows

1. **Install Python** (jika belum ada)
   - Download: https://www.python.org/downloads/
   - ✓ Centang "Add Python to PATH"
   - ✓ Centang "tcl/tk and IDLE"

2. **Jalankan Aplikasi**
   - Double-click file `run.bat`
   - ATAU buka Command Prompt:
     ```cmd
     python main.py
     ```

### Linux

1. **Install Python dan Tkinter**
   ```bash
   sudo apt update
   sudo apt install python3 python3-tk
   ```

2. **Jalankan Aplikasi**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
   ATAU:
   ```bash
   python3 main.py
   ```

---

## 📝 Penggunaan Cepat

### 1. Registrasi (Pertama Kali)

```
Username: admin
Password: Admin123
```

Klik **"Register"**

### 2. Login

Gunakan kredensial yang sama, klik **"Login"**

### 3. Tambah Item

```
Nama Item: Laptop Dell
Jumlah: 5
Harga: 7500000
```

Klik **"Tambah"**

### 4. Update Item

1. Klik item di tabel
2. Ubah data di form
3. Klik **"Update"**

### 5. Hapus Item

1. Klik item di tabel
2. Klik **"Hapus"**
3. Konfirmasi

---

## ⚠️ Ketentuan Penting

### Username
- ✓ 5-20 karakter
- ✓ Hanya huruf dan angka
- ✗ Tidak boleh ada spasi atau simbol

### Password
- ✓ Minimal 8 karakter
- ✓ Harus ada huruf BESAR
- ✓ Harus ada huruf kecil
- ✓ Harus ada angka

**Contoh Valid:**
- `Admin123` ✓
- `Password1` ✓
- `Inventaris2024` ✓

**Contoh Invalid:**
- `admin123` ✗ (tidak ada huruf besar)
- `Admin` ✗ (kurang dari 8 karakter)
- `AdminPass` ✗ (tidak ada angka)

---

## 📚 Dokumentasi Lengkap

- **README.md** - Overview proyek
- **USER_GUIDE.md** - Panduan lengkap pengguna
- **TESTING.md** - Dokumentasi testing
- **LAPORAN_PROYEK_AKHIR.md** - Laporan akademik

---

## 🆘 Troubleshooting Cepat

### Error: "No module named 'tkinter'"
**Solusi:** Reinstall Python dengan opsi tcl/tk dicentang

### Error: "Database is locked"
**Solusi:** Tutup semua instance aplikasi

### Window tidak muncul
**Solusi:** Cek apakah Python dan Tkinter terinstal dengan benar

---

## 📞 Bantuan

Jika masih ada masalah, baca dokumentasi lengkap di:
- USER_GUIDE.md (Panduan detail)
- TESTING.md (Test cases)

---

**Selamat menggunakan! 🎉**
