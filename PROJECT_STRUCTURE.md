# Struktur Proyek - Aplikasi Manajemen Inventaris

## 📁 Struktur Folder Lengkap

```
project_root/
│
├── 📄 main.py                          # Entry point aplikasi
├── 📄 README.md                        # Overview proyek
├── 📄 requirements.txt                 # Dependencies
├── 📄 .gitignore                       # Git ignore rules
│
├── 🚀 run.bat                          # Windows launcher
├── 🚀 run.sh                           # Linux/Mac launcher
│
├── 📚 USER_GUIDE.md                    # Panduan pengguna lengkap
├── 📚 TESTING.md                       # Dokumentasi testing
├── 📚 LAPORAN_PROYEK_AKHIR.md         # Laporan akademik
├── 📚 QUICK_START.md                   # Quick start guide
├── 📚 CONTOH_DATA.md                   # Contoh data testing
├── 📚 CHANGELOG.md                     # Version history
├── 📚 CONTRIBUTING.md                  # Contribution guidelines
├── 📚 LICENSE                          # License file
├── 📚 PROJECT_STRUCTURE.md             # File ini
│
├── 📂 database/                        # Database layer
│   ├── 📄 __init__.py                 # Package initializer
│   ├── 📄 db.py                       # Database manager
│   └── 💾 inventaris.db               # SQLite database (auto-generated)
│
├── 📂 auth/                            # Authentication layer
│   ├── 📄 __init__.py                 # Package initializer
│   ├── 📄 login.py                    # Login UI & logic
│   └── 📄 security.py                 # Password hashing & validation
│
├── 📂 inventory/                       # Inventory management layer
│   ├── 📄 __init__.py                 # Package initializer
│   ├── 📄 inventory_ui.py             # Inventory GUI
│   └── 📄 inventory_controller.py     # CRUD business logic
│
└── 📂 utils/                           # Utility functions
    ├── 📄 __init__.py                 # Package initializer
    ├── 📄 validators.py               # Input validation
    └── 📄 helpers.py                  # Helper functions
```

---

## 📋 Deskripsi File

### Root Files

#### main.py
**Fungsi:** Entry point aplikasi  
**Tanggung Jawab:**
- Inisialisasi aplikasi
- Menampilkan login window
- Menangani flow aplikasi
- Error handling global

**Key Functions:**
- `main()`: Fungsi utama
- `on_login_success()`: Callback setelah login berhasil

---

#### README.md
**Fungsi:** Dokumentasi overview proyek  
**Isi:**
- Deskripsi proyek
- Fitur utama
- Instalasi
- Penggunaan
- Arsitektur sistem
- Database schema
- Testing
- Troubleshooting

---

#### requirements.txt
**Fungsi:** Daftar dependencies  
**Isi:**
- Python version requirement
- Library dependencies (built-in only)
- Installation notes

---

#### .gitignore
**Fungsi:** Git ignore rules  
**Isi:**
- Python cache files
- Database files
- IDE files
- OS files

---

### Launcher Scripts

#### run.bat (Windows)
**Fungsi:** Launcher untuk Windows  
**Fitur:**
- Check Python installation
- Run aplikasi
- Error handling
- Pause setelah selesai

---

#### run.sh (Linux/Mac)
**Fungsi:** Launcher untuk Linux/Mac  
**Fitur:**
- Check Python3 installation
- Run aplikasi
- Error handling

---

### Documentation Files

#### USER_GUIDE.md
**Fungsi:** Panduan lengkap pengguna  
**Isi:**
- Instalasi detail
- Cara penggunaan
- Tips dan trik
- Troubleshooting
- FAQ

---

#### TESTING.md
**Fungsi:** Dokumentasi testing  
**Isi:**
- Unit testing
- Integration testing
- User acceptance testing
- Test cases
- Performance testing
- Security testing

---

#### LAPORAN_PROYEK_AKHIR.md
**Fungsi:** Laporan akademik lengkap  
**Isi:**
- Pendahuluan
- Landasan teori
- Analisis dan perancangan
- Implementasi
- Pengujian
- Penutup
- Daftar pustaka

---

#### QUICK_START.md
**Fungsi:** Quick start guide  
**Isi:**
- Instalasi cepat
- Penggunaan cepat
- Ketentuan penting
- Troubleshooting cepat

---

#### CONTOH_DATA.md
**Fungsi:** Contoh data untuk testing  
**Isi:**
- Data user testing
- Data inventaris testing
- Test cases
- Skenario testing
- Checklist testing

---

#### CHANGELOG.md
**Fungsi:** Version history  
**Isi:**
- Release notes
- Features per version
- Bug fixes
- Planned features

---

#### CONTRIBUTING.md
**Fungsi:** Contribution guidelines  
**Isi:**
- Cara berkontribusi
- Code style guide
- Commit conventions
- Pull request process

---

#### LICENSE
**Fungsi:** License file  
**Isi:**
- MIT License
- Academic use notice
- Disclaimer

---

### Database Layer (database/)

#### db.py
**Fungsi:** Database manager  
**Tanggung Jawab:**
- Inisialisasi database
- Membuat tabel
- Menyediakan koneksi
- Execute query
- Execute update

**Key Classes:**
- `DatabaseManager`: Main database manager class

**Key Functions:**
- `__init__()`: Initialize database
- `get_connection()`: Get database connection
- `execute_query()`: Execute SELECT query
- `execute_update()`: Execute INSERT/UPDATE/DELETE

---

#### inventaris.db
**Fungsi:** SQLite database file  
**Tabel:**
- `users`: User authentication data
- `inventaris`: Inventory data

**Auto-generated:** Ya, dibuat otomatis saat aplikasi pertama kali dijalankan

---

### Authentication Layer (auth/)

#### login.py
**Fungsi:** Login UI dan logic  
**Tanggung Jawab:**
- Menampilkan login window
- Handle registrasi
- Handle login
- Validasi input
- Interaksi dengan database

**Key Classes:**
- `LoginWindow`: Login window class

**Key Functions:**
- `__init__()`: Initialize login window
- `_create_widgets()`: Create GUI widgets
- `_handle_login()`: Handle login process
- `_handle_register()`: Handle registration process

---

#### security.py
**Fungsi:** Security functions  
**Tanggung Jawab:**
- Password hashing (SHA-256)
- Username validation
- Password validation
- Password verification

**Key Functions:**
- `hash_password()`: Hash password dengan SHA-256
- `validate_username()`: Validasi format username
- `validate_password()`: Validasi kompleksitas password
- `verify_password()`: Verifikasi password

---

### Inventory Layer (inventory/)

#### inventory_ui.py
**Fungsi:** Inventory GUI  
**Tanggung Jawab:**
- Menampilkan inventory window
- Form input data
- Treeview untuk display data
- Handle user interaction
- Update statistik

**Key Classes:**
- `InventoryWindow`: Inventory window class

**Key Functions:**
- `__init__()`: Initialize inventory window
- `_create_widgets()`: Create GUI widgets
- `_load_data()`: Load data from database
- `_create_item()`: Handle create operation
- `_update_item()`: Handle update operation
- `_delete_item()`: Handle delete operation
- `_update_statistics()`: Update statistics display

---

#### inventory_controller.py
**Fungsi:** CRUD business logic  
**Tanggung Jawab:**
- Business logic CRUD
- Interaksi dengan database
- Validasi data
- Error handling

**Key Classes:**
- `InventoryController`: Controller class

**Key Functions:**
- `get_all_items()`: Get all items
- `get_item_by_id()`: Get item by ID
- `create_item()`: Create new item
- `update_item()`: Update existing item
- `delete_item()`: Delete item
- `get_total_items()`: Get total item count
- `get_total_value()`: Get total inventory value

---

### Utils Layer (utils/)

#### validators.py
**Fungsi:** Input validation  
**Tanggung Jawab:**
- Validasi nama item
- Validasi jumlah
- Validasi harga
- Validasi lengkap data item

**Key Functions:**
- `validate_item_name()`: Validate item name
- `validate_quantity()`: Validate quantity
- `validate_price()`: Validate price
- `validate_item_data()`: Validate complete item data

---

#### helpers.py
**Fungsi:** Helper functions  
**Tanggung Jawab:**
- Format currency
- Format number
- Clear entries
- Confirm action

**Key Functions:**
- `format_currency()`: Format number to Rupiah
- `format_number()`: Format number with separator
- `clear_entries()`: Clear multiple entry widgets
- `confirm_action()`: Show confirmation dialog

---

## 🔄 Flow Diagram

### Application Flow

```
[Start]
   │
   ▼
[main.py]
   │
   ▼
[LoginWindow] ──────────────┐
   │                        │
   │ (Register)             │ (Login)
   │                        │
   ▼                        ▼
[security.py]          [security.py]
   │                        │
   │ (Hash Password)        │ (Verify Password)
   │                        │
   ▼                        ▼
[db.py]                [db.py]
   │                        │
   │ (Insert User)          │ (Query User)
   │                        │
   ▼                        ▼
[Success]              [Success]
   │                        │
   └────────────┬───────────┘
                │
                ▼
        [InventoryWindow]
                │
    ┌───────────┼───────────┐
    │           │           │
    ▼           ▼           ▼
[Create]    [Update]    [Delete]
    │           │           │
    ▼           ▼           ▼
[validators.py]
    │           │           │
    ▼           ▼           ▼
[inventory_controller.py]
    │           │           │
    ▼           ▼           ▼
[db.py]
    │           │           │
    ▼           ▼           ▼
[Database]
    │           │           │
    ▼           ▼           ▼
[Refresh Display]
```

---

## 🏗️ Arsitektur Layer

### Layer 1: Presentation (UI)
```
┌─────────────────────────────────────┐
│     login.py                        │
│     inventory_ui.py                 │
│                                     │
│  - Menampilkan GUI                  │
│  - Handle user interaction          │
│  - Display data                     │
└─────────────────────────────────────┘
```

### Layer 2: Business Logic
```
┌─────────────────────────────────────┐
│     security.py                     │
│     inventory_controller.py         │
│     validators.py                   │
│                                     │
│  - Validasi input                   │
│  - Business rules                   │
│  - Password hashing                 │
│  - CRUD logic                       │
└─────────────────────────────────────┘
```

### Layer 3: Data Access
```
┌─────────────────────────────────────┐
│     db.py                           │
│                                     │
│  - Database connection              │
│  - Query execution                  │
│  - Transaction management           │
└─────────────────────────────────────┘
```

### Layer 4: Database
```
┌─────────────────────────────────────┐
│     inventaris.db                   │
│                                     │
│  - Data persistence                 │
│  - SQLite database                  │
└─────────────────────────────────────┘
```

---

## 📊 Dependencies Graph

```
main.py
  │
  ├─→ auth/login.py
  │     ├─→ auth/security.py
  │     │     └─→ hashlib (built-in)
  │     │     └─→ re (built-in)
  │     └─→ database/db.py
  │           └─→ sqlite3 (built-in)
  │
  └─→ inventory/inventory_ui.py
        ├─→ inventory/inventory_controller.py
        │     ├─→ database/db.py
        │     └─→ utils/validators.py
        └─→ utils/helpers.py
              └─→ tkinter.messagebox
```

---

## 🎯 Module Responsibilities

| Module | Responsibility | Dependencies |
|--------|---------------|--------------|
| main.py | Application entry point | auth.login, inventory.inventory_ui |
| database/db.py | Database management | sqlite3 |
| auth/security.py | Security & validation | hashlib, re |
| auth/login.py | Login UI & logic | auth.security, database.db, tkinter |
| inventory/inventory_controller.py | CRUD business logic | database.db, utils.validators |
| inventory/inventory_ui.py | Inventory GUI | inventory.inventory_controller, utils.helpers, tkinter |
| utils/validators.py | Input validation | - |
| utils/helpers.py | Helper functions | tkinter.messagebox |

---

## 📈 Code Statistics

```
Total Files: 9 Python files
Total Lines: ~1500 lines
Total Functions: ~40 functions
Total Classes: 4 classes

Breakdown:
- Database Layer: ~150 lines
- Auth Layer: ~350 lines
- Inventory Layer: ~600 lines
- Utils Layer: ~200 lines
- Main: ~50 lines
- Documentation: ~5000 lines
```

---

## 🔐 Security Layers

```
User Input
    │
    ▼
[Client-side Validation]
    │ (validators.py)
    ▼
[Business Logic Validation]
    │ (security.py, inventory_controller.py)
    ▼
[Database Constraints]
    │ (NOT NULL, CHECK, UNIQUE)
    ▼
[Prepared Statements]
    │ (SQL Injection Prevention)
    ▼
Database
```

---

**Struktur proyek ini mengikuti best practices untuk:**
- ✅ Separation of Concerns
- ✅ Modular Design
- ✅ Maintainability
- ✅ Scalability
- ✅ Testability

© 2024 - Proyek Akhir Teknik Informatika
