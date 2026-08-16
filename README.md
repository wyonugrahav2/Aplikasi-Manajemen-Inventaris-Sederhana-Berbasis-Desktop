# Aplikasi Manajemen Inventaris Sederhana Berbasis Desktop

## Identitas Proyek

**Judul:** Aplikasi Manajemen Inventaris Sederhana Berbasis Desktop  
**Platform:** Desktop Application  
**Target OS:** Windows & Linux  
**Bahasa Pemrograman:** Python 3.x  
**GUI Framework:** Tkinter  
**Database:** SQLite (embedded, file-based)

---

## Deskripsi Proyek

Aplikasi ini merupakan sistem manajemen inventaris sederhana yang dibangun sebagai Proyek Akhir mata kuliah Teknik Informatika. Aplikasi ini mengimplementasikan konsep-konsep fundamental dalam pengembangan perangkat lunak, termasuk:

- **Arsitektur MVC** (Model-View-Controller)
- **Keamanan Sistem** (Password Hashing, Input Validation)
- **Database Management** (SQLite, CRUD Operations)
- **GUI Development** (Tkinter, Event-Driven Programming)
- **Software Engineering** (Modular Design, SDLC)

---

## Fitur Utama

### 1. Sistem Autentikasi (Login System)
- **Registrasi User** dengan validasi username dan password
- **Login** dengan verifikasi kredensial
- **Password Hashing** menggunakan SHA-256
- **Validasi Input:**
  - Username: 5-20 karakter, alphanumeric
  - Password: minimal 8 karakter, mengandung huruf besar, kecil, dan angka

### 2. Manajemen Inventaris (CRUD)
- **Create:** Menambah item baru ke inventaris
- **Read:** Menampilkan semua item dalam bentuk tabel
- **Update:** Mengubah data item yang sudah ada
- **Delete:** Menghapus item dari inventaris

### 3. Validasi Data
- Validasi nama item (tidak boleh kosong, minimal 3 karakter)
- Validasi jumlah (harus integer, tidak boleh negatif)
- Validasi harga (harus numeric, tidak boleh negatif)

### 4. Statistik Inventaris
- Total jumlah item
- Total nilai inventaris (jumlah × harga)

---

## Struktur Folder

```
project_root/
│
├── main.py                     # Entry point aplikasi
│
├── database/
│   ├── db.py                   # Database manager & initialization
│   └── inventaris.db           # SQLite database file (auto-generated)
│
├── auth/
│   ├── login.py                # Login UI & logic
│   └── security.py             # Password hashing & validation
│
├── inventory/
│   ├── inventory_ui.py         # Inventory GUI
│   └── inventory_controller.py # CRUD business logic
│
├── utils/
│   ├── validators.py           # Input validation functions
│   └── helpers.py              # Helper utility functions
│
└── README.md                   # Dokumentasi proyek
```

---

## Arsitektur Sistem

### Model-View-Controller (MVC)

```
┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                      │
│         (login.py, inventory_ui.py)                     │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 BUSINESS LOGIC LAYER                     │
│    (security.py, inventory_controller.py, validators)   │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  DATA ACCESS LAYER                       │
│                     (db.py)                             │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   DATABASE LAYER                         │
│                  (inventaris.db)                        │
└─────────────────────────────────────────────────────────┘
```

---

## Database Schema

### Tabel: users
| Kolom         | Tipe    | Constraint                    |
|---------------|---------|-------------------------------|
| id            | INTEGER | PRIMARY KEY AUTOINCREMENT     |
| username      | TEXT    | UNIQUE NOT NULL               |
| password_hash | TEXT    | NOT NULL                      |

### Tabel: inventaris
| Kolom  | Tipe    | Constraint                           |
|--------|---------|--------------------------------------|
| id     | INTEGER | PRIMARY KEY AUTOINCREMENT            |
| nama   | TEXT    | NOT NULL                             |
| jumlah | INTEGER | NOT NULL, CHECK(jumlah >= 0)         |
| harga  | REAL    | NOT NULL, CHECK(harga >= 0)          |

---

## Instalasi dan Penggunaan

### Opsi 1: Menggunakan Installer (Recommended untuk End User)

**Download installer:**
- Download `InventarisApp_Setup_v1.0.0.exe` dari [Releases](releases)
- Jalankan installer
- Ikuti wizard instalasi
- Launch dari Start Menu

**Keuntungan:**
- ✓ Tidak perlu Python
- ✓ Instalasi otomatis
- ✓ Start Menu integration
- ✓ Uninstaller included

---

### Opsi 2: Portable Version

**Download portable:**
- Download `InventarisApp.exe` dari [Releases](releases)
- Double-click untuk menjalankan
- Tidak perlu instalasi

**Keuntungan:**
- ✓ Tidak perlu Python
- ✓ Portable (bisa di USB)
- ✓ Tidak modify system

---

### Opsi 3: Menjalankan dari Source Code (untuk Developer)

#### Prasyarat
- Python 3.x terinstal di sistem
- Tkinter (biasanya sudah termasuk dalam instalasi Python)
- SQLite3 (built-in Python)

#### Langkah Instalasi

1. **Clone atau download proyek ini**
   ```bash
   git clone <repository-url>
   cd project_root
   ```

2. **Pastikan struktur folder sesuai**
   ```
   Verifikasi bahwa semua folder (database, auth, inventory, utils) ada
   ```

3. **Jalankan aplikasi**
   ```bash
   python main.py
   ```
   
   Atau gunakan launcher:
   - Windows: Double-click `run.bat`
   - Linux: `./run.sh`

### Cara Penggunaan

1. **Registrasi User Baru**
   - Jalankan aplikasi
   - Masukkan username dan password sesuai ketentuan
   - Klik tombol "Register"
   - Login dengan kredensial yang baru dibuat

2. **Login**
   - Masukkan username dan password
   - Klik tombol "Login"
   - Jika berhasil, akan masuk ke halaman inventaris

3. **Menambah Item**
   - Isi form: Nama Item, Jumlah, Harga
   - Klik tombol "Tambah"
   - Item akan muncul di tabel

4. **Mengupdate Item**
   - Klik item di tabel untuk memilih
   - Form akan terisi otomatis
   - Ubah data yang diinginkan
   - Klik tombol "Update"

5. **Menghapus Item**
   - Klik item di tabel untuk memilih
   - Klik tombol "Hapus"
   - Konfirmasi penghapusan

6. **Clear Form**
   - Klik tombol "Clear" untuk membersihkan form

---

## Konsep Teknis

### 1. Password Hashing (SHA-256)

Password tidak disimpan dalam bentuk plaintext. Aplikasi menggunakan SHA-256 untuk hashing:

```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
```

**Karakteristik SHA-256:**
- One-way function (tidak dapat di-reverse)
- Deterministic (input sama → output sama)
- Avalanche effect (perubahan kecil → hash sangat berbeda)
- 256-bit (64 karakter hexadecimal)

### 2. Input Validation

Validasi dilakukan di multiple layers:
- **Client-side:** Validasi format dan tipe data
- **Business Logic:** Validasi business rules
- **Database:** Constraints (NOT NULL, CHECK, UNIQUE)

### 3. Prepared Statements

Menggunakan parameterized queries untuk mencegah SQL Injection:

```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

### 4. Event-Driven Programming

Tkinter menggunakan event-driven architecture:

```python
button = tk.Button(root, text="Login", command=handle_login)
```

---

## Testing

### Test Case 1: Registrasi User

| Input                          | Expected Output           |
|--------------------------------|---------------------------|
| Username: "admin", Password: "Admin123" | Registrasi berhasil |
| Username: "adm", Password: "Admin123"   | Error: Username minimal 5 karakter |
| Username: "admin", Password: "admin"    | Error: Password harus mengandung huruf besar dan angka |

### Test Case 2: Login

| Input                          | Expected Output           |
|--------------------------------|---------------------------|
| Username: "admin", Password: "Admin123" | Login berhasil |
| Username: "admin", Password: "wrong"    | Error: Password salah |
| Username: "notexist", Password: "Admin123" | Error: Username tidak ditemukan |

### Test Case 3: CRUD Inventaris

| Operasi | Input                                    | Expected Output           |
|---------|------------------------------------------|---------------------------|
| Create  | Nama: "Laptop", Jumlah: 10, Harga: 5000000 | Item berhasil ditambahkan |
| Create  | Nama: "", Jumlah: 10, Harga: 5000000     | Error: Nama tidak boleh kosong |
| Create  | Nama: "Laptop", Jumlah: -5, Harga: 5000000 | Error: Jumlah tidak boleh negatif |
| Update  | ID: 1, Nama: "Laptop HP", Jumlah: 15, Harga: 6000000 | Item berhasil diupdate |
| Delete  | ID: 1                                    | Item berhasil dihapus |

---

## Build dan Deployment

### Membuat File Executable (.exe)

Untuk membuat file executable yang dapat dijalankan tanpa Python:

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Build EXE**
   ```bash
   python build_exe.py
   ```
   
   Atau manual:
   ```bash
   pyinstaller --name=InventarisApp --onefile --windowed --add-data="database;database" main.py
   ```

3. **Output:** `dist/InventarisApp.exe`

**Dokumentasi lengkap:** Lihat [BUILD_GUIDE.md](BUILD_GUIDE.md)

---

### Membuat Installer

Untuk membuat installer profesional:

1. **Install Inno Setup**
   - Download: https://jrsoftware.org/isinfo.php

2. **Build Installer**
   ```bash
   build_installer.bat
   ```
   
   Atau manual:
   ```bash
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup_installer.iss
   ```

3. **Output:** `installer_output/InventarisApp_Setup_v1.0.0.exe`

**Dokumentasi lengkap:** Lihat [DEPLOYMENT.md](DEPLOYMENT.md)

---

## Troubleshooting

### Error: "No module named 'tkinter'"
**Solusi:**
- **Windows:** Reinstall Python dengan opsi "tcl/tk and IDLE" dicentang
- **Linux:** Install tkinter
  ```bash
  sudo apt-get install python3-tk
  ```

### Error: "Database is locked"
**Solusi:**
- Tutup semua instance aplikasi yang sedang berjalan
- Hapus file `inventaris.db` dan jalankan ulang aplikasi

### Error: "Permission denied" saat membuat database
**Solusi:**
- Pastikan folder `database/` memiliki permission write
- Jalankan aplikasi dengan permission yang sesuai

### Error saat Build EXE
**Solusi:**
- Pastikan PyInstaller terinstall: `pip install pyinstaller`
- Lihat [BUILD_GUIDE.md](BUILD_GUIDE.md) untuk troubleshooting lengkap

---

## Pengembangan Lebih Lanjut

Beberapa fitur yang dapat ditambahkan:

1. **Export/Import Data** (CSV, Excel)
2. **Pencarian dan Filter** item
3. **Kategori Item** (pengelompokan barang)
4. **Laporan** (grafik, statistik)
5. **Multi-user dengan Role** (admin, user)
6. **Backup Database** otomatis
7. **Logging Activity** user

---

## Referensi

1. **Python Documentation:** https://docs.python.org/3/
2. **Tkinter Documentation:** https://docs.python.org/3/library/tkinter.html
3. **SQLite Documentation:** https://www.sqlite.org/docs.html
4. **SHA-256 Hashing:** https://en.wikipedia.org/wiki/SHA-2
5. **MVC Pattern:** https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller

---

## Lisensi

Proyek ini dibuat untuk keperluan akademik (Proyek Akhir) dan dapat digunakan sebagai referensi pembelajaran.

---

## Kontak

Untuk pertanyaan atau saran, silakan hubungi:
- **Email:** [email-anda]
- **GitHub:** [github-username]

---

**© 2024 - Proyek Akhir Teknik Informatika**
