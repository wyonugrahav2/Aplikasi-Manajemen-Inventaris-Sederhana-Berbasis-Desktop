# LAPORAN PROYEK AKHIR
## APLIKASI MANAJEMEN INVENTARIS SEDERHANA BERBASIS DESKTOP

---

### IDENTITAS MAHASISWA
- **Nama:** [Nama Mahasiswa]
- **NIM:** [Nomor Induk Mahasiswa]
- **Program Studi:** Teknik Informatika
- **Mata Kuliah:** Proyek Akhir / Pemrograman Desktop
- **Dosen Pembimbing:** [Nama Dosen]
- **Tahun Akademik:** 2024

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang

Manajemen inventaris merupakan aspek penting dalam operasional bisnis, terutama untuk usaha kecil dan menengah. Pencatatan manual menggunakan buku atau spreadsheet seringkali tidak efisien dan rentan terhadap kesalahan. Oleh karena itu, diperlukan sistem terkomputerisasi yang dapat membantu pengelolaan data inventaris secara lebih efektif dan efisien.

Proyek ini bertujuan untuk mengembangkan aplikasi desktop sederhana yang dapat membantu pengguna dalam mengelola data inventaris barang. Aplikasi ini dibangun menggunakan bahasa pemrograman Python dengan framework GUI Tkinter dan database SQLite, yang merupakan teknologi yang sesuai untuk aplikasi desktop skala kecil hingga menengah.

### 1.2 Rumusan Masalah

1. Bagaimana merancang sistem manajemen inventaris yang user-friendly?
2. Bagaimana mengimplementasikan sistem autentikasi yang aman?
3. Bagaimana mengimplementasikan operasi CRUD (Create, Read, Update, Delete) untuk data inventaris?
4. Bagaimana memastikan validasi data input untuk menjaga integritas database?

### 1.3 Tujuan Proyek

1. Mengembangkan aplikasi desktop untuk manajemen inventaris
2. Mengimplementasikan sistem autentikasi dengan password hashing
3. Mengimplementasikan operasi CRUD untuk data inventaris
4. Menerapkan validasi input data untuk menjaga integritas sistem
5. Menghasilkan aplikasi yang dapat berjalan di Windows dan Linux

### 1.4 Manfaat Proyek

**Manfaat Teoritis:**
- Menerapkan konsep rekayasa perangkat lunak (SDLC, MVC)
- Memahami implementasi keamanan sistem (password hashing)
- Menerapkan konsep database relasional
- Memahami event-driven programming

**Manfaat Praktis:**
- Membantu pengguna mengelola inventaris secara terkomputerisasi
- Mengurangi kesalahan pencatatan manual
- Mempercepat proses pencarian dan pelaporan data
- Dapat digunakan sebagai basis pengembangan sistem yang lebih kompleks

### 1.5 Batasan Masalah

1. Aplikasi bersifat single-user (tidak multi-user concurrent)
2. Database menggunakan SQLite (file-based, bukan client-server)
3. Tidak ada fitur export/import data
4. Tidak ada fitur backup otomatis
5. Tidak ada fitur laporan grafis
6. Fokus pada operasi CRUD dasar

---

## BAB II: LANDASAN TEORI

### 2.1 Rekayasa Perangkat Lunak

#### 2.1.1 Software Development Life Cycle (SDLC)

SDLC adalah proses sistematis untuk mengembangkan perangkat lunak berkualitas tinggi. Proyek ini menggunakan model SDLC dengan fase:

1. **Analysis (Analisis):** Identifikasi kebutuhan sistem
2. **Design (Perancangan):** Perancangan arsitektur dan database
3. **Implementation (Implementasi):** Coding dan development
4. **Testing (Pengujian):** Unit testing dan UAT

#### 2.1.2 Model-View-Controller (MVC)

MVC adalah design pattern yang memisahkan aplikasi menjadi tiga komponen:

- **Model:** Mengelola data dan business logic (database, controller)
- **View:** Menampilkan data ke user (GUI)
- **Controller:** Menghubungkan Model dan View (event handlers)

**Keuntungan MVC:**
- Separation of concerns
- Maintainability tinggi
- Reusability kode
- Testability lebih mudah

### 2.2 Keamanan Sistem

#### 2.2.1 CIA Triad

Prinsip dasar keamanan informasi:

1. **Confidentiality (Kerahasiaan):** Password di-hash, tidak plaintext
2. **Integrity (Integritas):** Validasi input, database constraints
3. **Availability (Ketersediaan):** Sistem dapat diakses setelah autentikasi

#### 2.2.2 Password Hashing

Password hashing adalah proses mengubah password plaintext menjadi hash menggunakan fungsi kriptografi satu arah (one-way function).

**SHA-256 (Secure Hash Algorithm 256-bit):**
- Menghasilkan hash 256-bit (64 karakter hexadecimal)
- Deterministic: input sama → output sama
- One-way: tidak dapat di-reverse
- Avalanche effect: perubahan kecil input → hash sangat berbeda

**Formula:**
```
H = SHA256(password)
```

Dimana:
- H = Hash digest (output)
- password = Input plaintext

**Contoh:**
```
Input:  "Admin123"
Output: "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
```

### 2.3 Database

#### 2.3.1 Relational Database

Database relasional menyimpan data dalam bentuk tabel dengan relasi antar tabel. Karakteristik:

- Data terstruktur dalam rows dan columns
- Menggunakan SQL (Structured Query Language)
- Mendukung ACID properties

#### 2.3.2 SQLite

SQLite adalah embedded relational database dengan karakteristik:

- **Serverless:** Tidak memerlukan database server
- **Self-contained:** Single file database
- **Zero-configuration:** Tidak perlu setup
- **Cross-platform:** Portabel antar OS
- **ACID compliant:** Atomicity, Consistency, Isolation, Durability

#### 2.3.3 Normalisasi Database

Proyek ini menggunakan **Third Normal Form (3NF)**:

**1NF (First Normal Form):**
- Setiap kolom berisi atomic values
- Tidak ada repeating groups

**2NF (Second Normal Form):**
- Memenuhi 1NF
- Tidak ada partial dependency

**3NF (Third Normal Form):**
- Memenuhi 2NF
- Tidak ada transitive dependency

#### 2.3.4 CRUD Operations

CRUD adalah operasi dasar database:

1. **Create:** INSERT - menambah data baru
2. **Read:** SELECT - membaca/menampilkan data
3. **Update:** UPDATE - mengubah data existing
4. **Delete:** DELETE - menghapus data

### 2.4 GUI Development

#### 2.4.1 Tkinter

Tkinter adalah standard GUI library untuk Python dengan karakteristik:

- Built-in Python (tidak perlu install terpisah)
- Cross-platform (Windows, Linux, Mac)
- Event-driven programming
- Widget-based architecture

#### 2.4.2 Event-Driven Programming

Paradigma pemrograman dimana flow program ditentukan oleh events (user actions):

```
User Action → Event → Event Handler → Business Logic → Update UI
```

**Contoh:**
- User click button → Button click event → handle_login() → Verify credentials → Show result

---

## BAB III: ANALISIS DAN PERANCANGAN SISTEM

### 3.1 Analisis Kebutuhan

#### 3.1.1 Kebutuhan Fungsional

1. **Sistem Autentikasi**
   - FR-01: Sistem harus dapat melakukan registrasi user baru
   - FR-02: Sistem harus dapat melakukan login user
   - FR-03: Sistem harus memvalidasi username dan password

2. **Manajemen Inventaris**
   - FR-04: Sistem harus dapat menambah item baru (Create)
   - FR-05: Sistem harus dapat menampilkan semua item (Read)
   - FR-06: Sistem harus dapat mengubah data item (Update)
   - FR-07: Sistem harus dapat menghapus item (Delete)

3. **Validasi Data**
   - FR-08: Sistem harus memvalidasi input username (5-20 karakter, alphanumeric)
   - FR-09: Sistem harus memvalidasi input password (min 8 karakter, kompleksitas)
   - FR-10: Sistem harus memvalidasi input data inventaris

4. **Statistik**
   - FR-11: Sistem harus menampilkan total jumlah item
   - FR-12: Sistem harus menampilkan total nilai inventaris

#### 3.1.2 Kebutuhan Non-Fungsional

1. **Usability:** Interface user-friendly dan intuitif
2. **Security:** Password hashing, input validation
3. **Performance:** Response time < 1 detik
4. **Portability:** Dapat berjalan di Windows dan Linux
5. **Reliability:** Data tersimpan persistent di database

### 3.2 Perancangan Sistem

#### 3.2.1 Arsitektur Sistem

```
┌─────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER                      │
│         (login.py, inventory_ui.py)                     │
│         - Menampilkan GUI                               │
│         - Menangani user interaction                    │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 BUSINESS LOGIC LAYER                     │
│    (security.py, inventory_controller.py, validators)   │
│         - Validasi input                                │
│         - Business rules                                │
│         - Password hashing                              │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  DATA ACCESS LAYER                       │
│                     (db.py)                             │
│         - Database connection                           │
│         - Query execution                               │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   DATABASE LAYER                         │
│                  (inventaris.db)                        │
│         - Data persistence                              │
│         - SQLite database                               │
└─────────────────────────────────────────────────────────┘
```

#### 3.2.2 Entity Relationship Diagram (ERD)

```
┌─────────────────────┐
│       USERS         │
├─────────────────────┤
│ PK  id              │
│     username        │
│     password_hash   │
└─────────────────────┘

┌─────────────────────┐
│    INVENTARIS       │
├─────────────────────┤
│ PK  id              │
│     nama            │
│     jumlah          │
│     harga           │
└─────────────────────┘
```

**Keterangan:**
- PK = Primary Key
- Tidak ada relasi antar tabel (independent entities)

#### 3.2.3 Database Schema

**Tabel: users**
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
```

**Tabel: inventaris**
```sql
CREATE TABLE inventaris (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    jumlah INTEGER NOT NULL CHECK(jumlah >= 0),
    harga REAL NOT NULL CHECK(harga >= 0)
);
```

#### 3.2.4 Use Case Diagram

```
                    ┌─────────────┐
                    │    User     │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐      ┌──────────┐      ┌──────────┐
   │Register │      │  Login   │      │  Logout  │
   └─────────┘      └──────────┘      └──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐      ┌──────────┐      ┌──────────┐
   │  Create │      │   Read   │      │  Update  │
   │  Item   │      │  Items   │      │   Item   │
   └─────────┘      └──────────┘      └──────────┘
                           │
                           ▼
                    ┌──────────┐
                    │  Delete  │
                    │   Item   │
                    └──────────┘
```

#### 3.2.5 Sequence Diagram - Login Process

```
User          Login UI       Security       Database
 │                │              │              │
 │─── Input ────→│              │              │
 │                │              │              │
 │                │─ Validate ─→│              │
 │                │              │              │
 │                │              │─── Query ──→│
 │                │              │              │
 │                │              │←── Hash ────│
 │                │              │              │
 │                │← Compare ───│              │
 │                │              │              │
 │← Success/Fail ─│              │              │
```

#### 3.2.6 Flowchart - CRUD Operations

**Create Item:**
```
[Start] → [Input Data] → [Validate] → {Valid?}
                                         │
                                    Yes  │  No
                                         │
                                    [Insert DB] → [Show Success]
                                         │
                                    [Refresh Display] → [End]
                                         │
                                    [Show Error] → [End]
```

---

## BAB IV: IMPLEMENTASI

### 4.1 Lingkungan Pengembangan

- **OS:** Windows 11 / Linux Ubuntu 22.04
- **Python Version:** 3.11.x
- **IDE:** Visual Studio Code / PyCharm
- **Database:** SQLite 3
- **GUI Framework:** Tkinter (built-in)
- **Version Control:** Git

### 4.2 Struktur Proyek

```
project_root/
│
├── main.py                     # Entry point
├── database/
│   ├── __init__.py
│   ├── db.py                   # Database manager
│   └── inventaris.db           # SQLite database
├── auth/
│   ├── __init__.py
│   ├── login.py                # Login UI
│   └── security.py             # Security functions
├── inventory/
│   ├── __init__.py
│   ├── inventory_ui.py         # Inventory GUI
│   └── inventory_controller.py # CRUD logic
├── utils/
│   ├── __init__.py
│   ├── validators.py           # Input validators
│   └── helpers.py              # Helper functions
└── README.md
```

### 4.3 Implementasi Modul

#### 4.3.1 Database Manager (database/db.py)

Modul ini mengimplementasikan:
- Singleton pattern untuk koneksi database
- Inisialisasi database dan tabel
- Fungsi helper untuk query dan update

**Fungsi Utama:**
- `__init__()`: Inisialisasi database
- `get_connection()`: Mendapatkan koneksi database
- `execute_query()`: Eksekusi SELECT query
- `execute_update()`: Eksekusi INSERT/UPDATE/DELETE

#### 4.3.2 Security Module (auth/security.py)

Modul ini mengimplementasikan:
- Password hashing menggunakan SHA-256
- Validasi username dan password
- Verifikasi kredensial login

**Fungsi Utama:**
- `hash_password(password)`: Hash password dengan SHA-256
- `validate_username(username)`: Validasi format username
- `validate_password(password)`: Validasi kompleksitas password
- `verify_password(input, stored_hash)`: Verifikasi password

#### 4.3.3 Validators Module (utils/validators.py)

Modul ini mengimplementasikan:
- Validasi nama item
- Validasi jumlah (integer, non-negative)
- Validasi harga (numeric, non-negative)

**Fungsi Utama:**
- `validate_item_name(nama)`: Validasi nama item
- `validate_quantity(jumlah_str)`: Validasi jumlah
- `validate_price(harga_str)`: Validasi harga
- `validate_item_data()`: Validasi lengkap data item

#### 4.3.4 Inventory Controller (inventory/inventory_controller.py)

Modul ini mengimplementasikan business logic CRUD:

**Fungsi Utama:**
- `get_all_items()`: Mengambil semua item
- `get_item_by_id(id)`: Mengambil item berdasarkan ID
- `create_item()`: Menambah item baru
- `update_item()`: Mengubah data item
- `delete_item()`: Menghapus item
- `get_total_items()`: Menghitung total item
- `get_total_value()`: Menghitung total nilai

#### 4.3.5 GUI Modules

**Login UI (auth/login.py):**
- Form input username dan password
- Button register dan login
- Event handlers untuk autentikasi

**Inventory UI (inventory/inventory_ui.py):**
- Form input data item
- Treeview untuk menampilkan data
- Buttons untuk CRUD operations
- Statistik display

### 4.4 Algoritma Kunci

#### 4.4.1 Password Hashing Algorithm

```python
import hashlib

def hash_password(password):
    # Encode password ke bytes
    password_bytes = password.encode('utf-8')
    
    # Hash menggunakan SHA-256
    hash_object = hashlib.sha256(password_bytes)
    
    # Convert ke hexadecimal string
    hash_hex = hash_object.hexdigest()
    
    return hash_hex
```

**Kompleksitas:** O(1) - constant time

#### 4.4.2 CRUD Operations Algorithm

**Create:**
```
1. Validate input data
2. IF valid THEN
3.   INSERT INTO database
4.   RETURN success
5. ELSE
6.   RETURN error message
```

**Read:**
```
1. SELECT * FROM inventaris
2. RETURN results
```

**Update:**
```
1. Validate input data
2. Check if item exists
3. IF valid AND exists THEN
4.   UPDATE database
5.   RETURN success
6. ELSE
7.   RETURN error message
```

**Delete:**
```
1. Check if item exists
2. IF exists THEN
3.   Confirm deletion
4.   DELETE FROM database
5.   RETURN success
6. ELSE
7.   RETURN error message
```

---

## BAB V: PENGUJIAN

### 5.1 Unit Testing

Pengujian dilakukan pada setiap modul secara independen:

**Security Module:**
- ✓ Hash password consistency
- ✓ Username validation
- ✓ Password validation

**Validators Module:**
- ✓ Item name validation
- ✓ Quantity validation
- ✓ Price validation

**Database Module:**
- ✓ Database initialization
- ✓ Connection management
- ✓ Query execution

### 5.2 Integration Testing

Pengujian interaksi antar modul:

- ✓ Login flow (UI → Security → Database)
- ✓ CRUD operations (UI → Controller → Database)
- ✓ Data validation (UI → Validators → Controller)

### 5.3 User Acceptance Testing (UAT)

| Test Case | Status | Keterangan |
|-----------|--------|------------|
| Registrasi user baru | ✓ Pass | Berhasil dengan validasi |
| Login dengan kredensial valid | ✓ Pass | Berhasil masuk sistem |
| Login dengan kredensial invalid | ✓ Pass | Error message sesuai |
| Tambah item valid | ✓ Pass | Item tersimpan di database |
| Tambah item invalid | ✓ Pass | Error message sesuai |
| Update item | ✓ Pass | Data terupdate |
| Delete item | ✓ Pass | Item terhapus |
| Statistik display | ✓ Pass | Nilai akurat |

**Total Test Cases:** 18  
**Passed:** 18  
**Failed:** 0  
**Success Rate:** 100%

---

## BAB VI: PENUTUP

### 6.1 Kesimpulan

1. Aplikasi manajemen inventaris berbasis desktop berhasil dikembangkan menggunakan Python, Tkinter, dan SQLite
2. Sistem autentikasi dengan password hashing SHA-256 berhasil diimplementasikan
3. Operasi CRUD untuk data inventaris berfungsi dengan baik
4. Validasi input data berhasil menjaga integritas database
5. Aplikasi dapat berjalan di Windows dan Linux
6. Semua test cases (18 cases) berhasil lulus dengan success rate 100%

### 6.2 Saran Pengembangan

1. **Fitur Tambahan:**
   - Export/import data (CSV, Excel)
   - Pencarian dan filter advanced
   - Kategori item
   - Laporan grafis
   - Multi-user dengan role management

2. **Keamanan:**
   - Implementasi bcrypt untuk password hashing
   - Session management
   - Audit logging

3. **Performance:**
   - Pagination untuk data besar
   - Caching mechanism
   - Database indexing

4. **UI/UX:**
   - Modern theme (ttk.Style)
   - Dark mode
   - Responsive design
   - Keyboard shortcuts

---

## DAFTAR PUSTAKA

1. Python Software Foundation. (2024). *Python Documentation*. https://docs.python.org/3/
2. Python Software Foundation. (2024). *Tkinter Documentation*. https://docs.python.org/3/library/tkinter.html
3. SQLite Consortium. (2024). *SQLite Documentation*. https://www.sqlite.org/docs.html
4. NIST. (2015). *Secure Hash Standard (SHS)*. FIPS PUB 180-4.
5. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
6. Sommerville, I. (2015). *Software Engineering* (10th ed.). Pearson.
7. Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). *Database System Concepts* (7th ed.). McGraw-Hill.

---

## LAMPIRAN

### Lampiran A: Source Code
Lihat folder proyek untuk source code lengkap.

### Lampiran B: Screenshot Aplikasi
[Tambahkan screenshot aplikasi di sini]

### Lampiran C: User Manual
Lihat file USER_GUIDE.md

### Lampiran D: Testing Documentation
Lihat file TESTING.md

---

**© 2024 - Proyek Akhir Teknik Informatika**
