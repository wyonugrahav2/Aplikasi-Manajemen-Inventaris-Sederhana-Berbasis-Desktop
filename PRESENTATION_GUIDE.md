# Panduan Presentasi Proyek Akhir

## 📊 Outline Presentasi (15-20 Menit)

### Slide 1: Title Slide (1 menit)
```
APLIKASI MANAJEMEN INVENTARIS
SEDERHANA BERBASIS DESKTOP

Nama: [Nama Mahasiswa]
NIM: [NIM]
Dosen Pembimbing: [Nama Dosen]
Teknik Informatika - 2024
```

---

### Slide 2: Latar Belakang (2 menit)

**Masalah:**
- Pencatatan manual tidak efisien
- Rentan kesalahan
- Sulit tracking data

**Solusi:**
- Aplikasi desktop terkomputerisasi
- Database SQLite
- GUI user-friendly

**Tujuan:**
- Memudahkan manajemen inventaris
- Meningkatkan efisiensi
- Mengurangi kesalahan

---

### Slide 3: Fitur Utama (2 menit)

**1. Sistem Autentikasi**
- Login dengan password hashing
- Registrasi user baru
- Validasi keamanan

**2. Manajemen Inventaris (CRUD)**
- Create: Tambah item
- Read: Lihat semua item
- Update: Ubah data
- Delete: Hapus item

**3. Validasi Data**
- Input validation
- Error handling
- Data integrity

---

### Slide 4: Teknologi yang Digunakan (1 menit)

```
┌─────────────────────────────────┐
│  Python 3.x                     │
│  - Bahasa pemrograman utama     │
└─────────────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼───┐    ┌───▼────┐
│Tkinter│    │ SQLite │
│  GUI  │    │Database│
└───────┘    └────────┘
```

**Alasan Pemilihan:**
- Python: Mudah dipelajari, powerful
- Tkinter: Built-in, cross-platform
- SQLite: Lightweight, embedded

---

### Slide 5: Arsitektur Sistem (2 menit)

```
┌─────────────────────────────────┐
│    PRESENTATION LAYER           │
│    (Login UI, Inventory UI)     │
└─────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│    BUSINESS LOGIC LAYER         │
│    (Controllers, Validators)    │
└─────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│    DATA ACCESS LAYER            │
│    (Database Manager)           │
└─────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│    DATABASE LAYER               │
│    (SQLite Database)            │
└─────────────────────────────────┘
```

**Pattern:** MVC (Model-View-Controller)

---

### Slide 6: Database Design (2 menit)

**Tabel 1: users**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
```

**Tabel 2: inventaris**
```sql
CREATE TABLE inventaris (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    jumlah INTEGER NOT NULL CHECK(jumlah >= 0),
    harga REAL NOT NULL CHECK(harga >= 0)
);
```

**Normalisasi:** 3NF (Third Normal Form)

---

### Slide 7: Keamanan Sistem (2 menit)

**1. Password Hashing (SHA-256)**
```
Plaintext → SHA-256 → Hash (64 char hex)
"Admin123" → "8c6976e5b5410415..."
```

**2. Input Validation**
- Username: 5-20 karakter, alphanumeric
- Password: Min 8 karakter, kompleksitas
- Data: Type checking, range validation

**3. SQL Injection Prevention**
- Prepared statements
- Parameter binding

---

### Slide 8: DEMO APLIKASI (5 menit)

**Demo Flow:**

1. **Registrasi**
   - Username: admin
   - Password: Admin123
   - Show validation

2. **Login**
   - Login dengan kredensial
   - Show success

3. **Tambah Item**
   - Nama: Laptop Dell
   - Jumlah: 5
   - Harga: 15000000
   - Show di tabel

4. **Update Item**
   - Select item
   - Ubah jumlah: 10
   - Show update

5. **Delete Item**
   - Select item
   - Konfirmasi delete
   - Show deletion

6. **Statistik**
   - Show total item
   - Show total nilai

---

### Slide 9: Testing Results (2 menit)

**Unit Testing**
```
✓ Security module: 3/3 passed
✓ Validators module: 3/3 passed
✓ Database module: 2/2 passed
```

**Integration Testing**
```
✓ Login flow: Passed
✓ CRUD operations: Passed
✓ Data validation: Passed
```

**User Acceptance Testing**
```
✓ All scenarios: 8/8 passed
```

**Total: 18/18 tests passed (100%)**

---

### Slide 10: Build & Deployment (1 menit)

**Executable (.exe)**
- PyInstaller untuk convert Python → EXE
- Single file atau folder mode
- Tidak perlu Python terinstall

**Installer**
- Inno Setup untuk Windows installer
- Professional installation wizard
- Start Menu integration
- Uninstaller included

**Distribusi**
- Portable version (USB-ready)
- Installer version (recommended)

---

### Slide 11: Kesimpulan (1 menit)

**Pencapaian:**
✅ Aplikasi berfungsi dengan baik
✅ Semua fitur terimplementasi
✅ Testing 100% passed
✅ Dokumentasi lengkap
✅ Build & deployment ready

**Manfaat:**
- Memudahkan manajemen inventaris
- Meningkatkan efisiensi
- Mengurangi kesalahan
- Portable dan mudah digunakan

---

### Slide 12: Pengembangan Lanjutan (1 menit)

**Fitur yang Bisa Ditambahkan:**
- Export/Import data (CSV, Excel)
- Search dan filter advanced
- Kategori item
- Laporan grafis
- Multi-user dengan role
- Backup/restore otomatis
- Dark mode
- Mobile version

---

### Slide 13: Q&A (Sisa waktu)

**Pertanyaan yang Mungkin Ditanya:**

1. **Mengapa pilih Python?**
   - Mudah dipelajari
   - Library lengkap
   - Cross-platform

2. **Mengapa SQLite?**
   - Lightweight
   - Embedded (no server)
   - Portable

3. **Bagaimana keamanan password?**
   - SHA-256 hashing
   - No plaintext storage
   - Validation rules

4. **Apakah bisa multi-user?**
   - Ya, multiple users bisa registrasi
   - Shared database
   - Bisa dikembangkan dengan role management

5. **Bagaimana cara distribusi?**
   - Build EXE dengan PyInstaller
   - Buat installer dengan Inno Setup
   - Distribusi via download atau USB

---

## 🎯 Tips Presentasi

### Persiapan

**1 Minggu Sebelum:**
- [ ] Buat slides
- [ ] Prepare demo
- [ ] Test aplikasi
- [ ] Backup data

**1 Hari Sebelum:**
- [ ] Review slides
- [ ] Practice demo
- [ ] Prepare laptop
- [ ] Backup ke USB

**Hari H:**
- [ ] Datang lebih awal
- [ ] Test proyektor
- [ ] Test aplikasi
- [ ] Siapkan mental

---

### Saat Presentasi

**Do's:**
✅ Bicara jelas dan percaya diri
✅ Eye contact dengan audience
✅ Explain dengan bahasa sederhana
✅ Show enthusiasm
✅ Prepare untuk Q&A

**Don'ts:**
❌ Membaca slides
❌ Terlalu cepat
❌ Terlalu teknis
❌ Tidak prepare demo
❌ Panik saat error

---

### Demo Tips

**Persiapan Demo:**
1. Fresh database (clean state)
2. Prepare test data
3. Practice flow
4. Backup plan jika error

**Demo Flow:**
```
1. Show login screen
2. Register new user
3. Login
4. Show empty inventory
5. Add items (2-3 items)
6. Show in table
7. Update one item
8. Delete one item
9. Show statistics
10. Logout
```

**Jika Demo Error:**
- Tetap tenang
- Explain apa yang seharusnya terjadi
- Show screenshots backup
- Continue dengan slides

---

## 📝 Script Presentasi

### Opening (1 menit)

```
"Selamat pagi/siang Bapak/Ibu dosen dan teman-teman.

Saya [Nama], NIM [NIM], akan mempresentasikan Proyek Akhir saya
dengan judul 'Aplikasi Manajemen Inventaris Sederhana Berbasis Desktop'.

Proyek ini dibimbing oleh [Nama Dosen Pembimbing].

Mari kita mulai."
```

---

### Latar Belakang (2 menit)

```
"Latar belakang proyek ini adalah masalah yang sering dihadapi
oleh usaha kecil dan menengah dalam mengelola inventaris.

Pencatatan manual menggunakan buku atau spreadsheet seringkali
tidak efisien dan rentan terhadap kesalahan.

Oleh karena itu, saya mengembangkan aplikasi desktop yang dapat
membantu mengelola data inventaris secara terkomputerisasi.

Aplikasi ini dibangun menggunakan Python, Tkinter untuk GUI,
dan SQLite untuk database."
```

---

### Fitur (2 menit)

```
"Aplikasi ini memiliki tiga fitur utama:

Pertama, Sistem Autentikasi. User harus login terlebih dahulu
dengan username dan password. Password di-hash menggunakan SHA-256
untuk keamanan.

Kedua, Manajemen Inventaris dengan operasi CRUD lengkap.
User dapat menambah, melihat, mengubah, dan menghapus data item.

Ketiga, Validasi Data. Semua input divalidasi untuk memastikan
integritas data. Misalnya, jumlah harus integer positif,
harga harus numeric positif."
```

---

### Arsitektur (2 menit)

```
"Dari segi arsitektur, aplikasi ini menggunakan pattern MVC
atau Model-View-Controller.

Layer pertama adalah Presentation Layer, yang menangani GUI
dan interaksi user.

Layer kedua adalah Business Logic Layer, yang berisi validasi
dan business rules.

Layer ketiga adalah Data Access Layer, yang mengelola koneksi
dan operasi database.

Dan layer terakhir adalah Database Layer, yaitu SQLite database
untuk menyimpan data.

Dengan arsitektur ini, kode menjadi modular, maintainable,
dan mudah di-test."
```

---

### Demo (5 menit)

```
"Sekarang saya akan demo aplikasi ini.

[Jalankan aplikasi]

Pertama, saya akan registrasi user baru.
Username: admin, Password: Admin123.

[Klik Register]

Registrasi berhasil. Sekarang saya login dengan kredensial yang sama.

[Klik Login]

Login berhasil. Sekarang kita masuk ke halaman inventaris.

Saya akan tambah item baru. Nama: Laptop Dell, Jumlah: 5,
Harga: 15000000.

[Klik Tambah]

Item berhasil ditambahkan dan muncul di tabel.
Perhatikan statistik di bawah juga terupdate.

Sekarang saya akan update item ini. Saya klik item di tabel,
data otomatis muncul di form. Saya ubah jumlah menjadi 10.

[Klik Update]

Item berhasil diupdate. Statistik juga terupdate.

Terakhir, saya akan hapus item ini.

[Klik Delete, Konfirmasi]

Item berhasil dihapus.

Demikian demo aplikasi ini."
```

---

### Testing (2 menit)

```
"Untuk testing, saya melakukan tiga jenis testing:

Unit Testing untuk test setiap modul secara independen.
Hasilnya 8 dari 8 test passed.

Integration Testing untuk test interaksi antar modul.
Hasilnya 5 dari 5 test passed.

Dan User Acceptance Testing untuk test dari perspektif user.
Hasilnya 8 dari 8 scenario passed.

Total 18 dari 18 test cases passed, atau 100% success rate."
```

---

### Kesimpulan (1 menit)

```
"Sebagai kesimpulan, aplikasi ini telah berhasil dikembangkan
dengan semua fitur yang direncanakan.

Aplikasi ini dapat membantu mengelola inventaris secara efisien,
mengurangi kesalahan, dan meningkatkan produktivitas.

Untuk pengembangan lanjutan, aplikasi ini bisa ditambahkan
fitur export/import data, search advanced, dan laporan grafis.

Demikian presentasi saya. Terima kasih atas perhatiannya.
Saya siap menjawab pertanyaan."
```

---

## 🎤 Q&A Preparation

### Pertanyaan Teknis

**Q: Mengapa pilih Python dan bukan bahasa lain?**
```
A: Python dipilih karena beberapa alasan:
1. Mudah dipelajari dan readable
2. Library lengkap (Tkinter built-in)
3. Cross-platform
4. Cocok untuk rapid development
5. Sesuai dengan kurikulum Teknik Informatika
```

**Q: Bagaimana cara kerja password hashing?**
```
A: Password hashing menggunakan SHA-256, yaitu cryptographic
hash function yang mengubah password menjadi string 64 karakter
hexadecimal. Prosesnya one-way, artinya tidak bisa di-reverse.
Saat login, password yang diinput di-hash dan dibandingkan
dengan hash yang tersimpan di database.
```

**Q: Bagaimana mencegah SQL Injection?**
```
A: Aplikasi ini menggunakan prepared statements atau parameterized
queries. Jadi query dan data dipisah. SQLite driver akan
otomatis escape special characters, sehingga SQL injection
tidak mungkin terjadi.
```

**Q: Apakah aplikasi ini bisa untuk multi-user concurrent?**
```
A: Untuk versi saat ini, aplikasi support multiple users
(bisa registrasi banyak user), tapi tidak concurrent access
karena SQLite file-based. Untuk concurrent access, perlu
upgrade ke client-server database seperti PostgreSQL atau MySQL.
```

---

### Pertanyaan Fungsional

**Q: Apakah data bisa di-export?**
```
A: Untuk versi saat ini belum ada fitur export. Tapi ini
masuk dalam rencana pengembangan lanjutan. Bisa ditambahkan
export ke CSV atau Excel menggunakan library pandas.
```

**Q: Bagaimana cara backup data?**
```
A: Karena menggunakan SQLite, backup sangat mudah. Cukup
copy file database/inventaris.db ke lokasi lain. Untuk restore,
tinggal replace file tersebut.
```

**Q: Apakah bisa digunakan di Mac atau Linux?**
```
A: Ya, aplikasi ini cross-platform. Bisa berjalan di Windows,
Linux, dan Mac selama Python dan Tkinter terinstall. Untuk
distribusi, bisa build executable untuk masing-masing platform.
```

---

### Pertanyaan Akademik

**Q: Apa kontribusi proyek ini terhadap ilmu pengetahuan?**
```
A: Proyek ini mengintegrasikan beberapa konsep fundamental
Teknik Informatika:
1. Rekayasa Perangkat Lunak (SDLC, MVC)
2. Keamanan Informasi (Hashing, Validation)
3. Basis Data (Relational DB, Normalization)
4. Pemrograman (OOP, Modular Design)

Proyek ini juga bisa menjadi referensi pembelajaran untuk
mahasiswa lain dalam mengembangkan aplikasi desktop.
```

**Q: Apa tantangan terbesar dalam pengembangan?**
```
A: Tantangan terbesar adalah:
1. Merancang arsitektur yang modular dan maintainable
2. Implementasi keamanan yang proper (password hashing)
3. Validasi input di multiple layers
4. Build executable yang portable
5. Dokumentasi yang lengkap dan jelas
```

---

## 📊 Backup Materials

### Screenshots

Siapkan screenshots untuk backup jika demo error:
1. Login screen
2. Registration success
3. Inventory window
4. Add item success
5. Update item
6. Delete confirmation
7. Statistics display
8. Error validation

---

### Video Demo

Rekam video demo sebagai backup:
- Duration: 3-5 menit
- Show all features
- Clear narration
- Good quality

---

## ✅ Checklist Presentasi

### 1 Minggu Sebelum
- [ ] Buat slides lengkap
- [ ] Prepare demo scenario
- [ ] Test aplikasi thoroughly
- [ ] Buat backup materials
- [ ] Practice presentasi

### 1 Hari Sebelum
- [ ] Review slides
- [ ] Practice demo 3x
- [ ] Prepare laptop
- [ ] Backup ke USB
- [ ] Print handout (optional)

### Hari H - Sebelum Presentasi
- [ ] Datang 30 menit lebih awal
- [ ] Test proyektor
- [ ] Test aplikasi
- [ ] Prepare mental
- [ ] Review Q&A

### Hari H - Saat Presentasi
- [ ] Bicara jelas dan percaya diri
- [ ] Eye contact
- [ ] Manage waktu
- [ ] Handle Q&A dengan baik
- [ ] Thank audience

---

## 🎉 GOOD LUCK!

**Remember:**
- Anda sudah prepare dengan baik
- Aplikasi Anda berkualitas
- Dokumentasi lengkap
- Testing 100% passed

**You got this! 💪**

---

© 2024 - Proyek Akhir Teknik Informatika
