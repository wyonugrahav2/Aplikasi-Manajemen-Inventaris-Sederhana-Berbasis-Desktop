# Panduan Testing Aplikasi Manajemen Inventaris

## Daftar Isi
1. [Unit Testing](#unit-testing)
2. [Integration Testing](#integration-testing)
3. [User Acceptance Testing](#user-acceptance-testing)
4. [Test Cases](#test-cases)

---

## Unit Testing

### 1. Testing Module Security (auth/security.py)

#### Test Hash Password
```python
from auth.security import hash_password

# Test case 1: Hash consistency
password = "Admin123"
hash1 = hash_password(password)
hash2 = hash_password(password)
assert hash1 == hash2, "Hash harus konsisten untuk input yang sama"

# Test case 2: Different input produces different hash
hash3 = hash_password("Admin124")
assert hash1 != hash3, "Input berbeda harus menghasilkan hash berbeda"

print("✓ Hash password test passed")
```

#### Test Validate Username
```python
from auth.security import validate_username

# Test case 1: Valid username
valid, msg = validate_username("admin")
assert valid == True, "Username 'admin' harus valid"

# Test case 2: Username terlalu pendek
valid, msg = validate_username("adm")
assert valid == False, "Username < 5 karakter harus invalid"

# Test case 3: Username dengan karakter spesial
valid, msg = validate_username("admin@123")
assert valid == False, "Username dengan karakter spesial harus invalid"

print("✓ Validate username test passed")
```

#### Test Validate Password
```python
from auth.security import validate_password

# Test case 1: Valid password
valid, msg = validate_password("Admin123")
assert valid == True, "Password 'Admin123' harus valid"

# Test case 2: Password tanpa huruf besar
valid, msg = validate_password("admin123")
assert valid == False, "Password tanpa huruf besar harus invalid"

# Test case 3: Password tanpa angka
valid, msg = validate_password("AdminPass")
assert valid == False, "Password tanpa angka harus invalid"

# Test case 4: Password terlalu pendek
valid, msg = validate_password("Admin1")
assert valid == False, "Password < 8 karakter harus invalid"

print("✓ Validate password test passed")
```

### 2. Testing Module Validators (utils/validators.py)

#### Test Validate Item Name
```python
from utils.validators import validate_item_name

# Test case 1: Valid name
valid, msg = validate_item_name("Laptop")
assert valid == True, "Nama 'Laptop' harus valid"

# Test case 2: Empty name
valid, msg = validate_item_name("")
assert valid == False, "Nama kosong harus invalid"

# Test case 3: Name too short
valid, msg = validate_item_name("AB")
assert valid == False, "Nama < 3 karakter harus invalid"

print("✓ Validate item name test passed")
```

#### Test Validate Quantity
```python
from utils.validators import validate_quantity

# Test case 1: Valid quantity
valid, msg, value = validate_quantity("10")
assert valid == True and value == 10, "Jumlah '10' harus valid"

# Test case 2: Negative quantity
valid, msg, value = validate_quantity("-5")
assert valid == False, "Jumlah negatif harus invalid"

# Test case 3: Non-integer
valid, msg, value = validate_quantity("abc")
assert valid == False, "Jumlah non-integer harus invalid"

print("✓ Validate quantity test passed")
```

#### Test Validate Price
```python
from utils.validators import validate_price

# Test case 1: Valid price (integer)
valid, msg, value = validate_price("5000")
assert valid == True and value == 5000.0, "Harga '5000' harus valid"

# Test case 2: Valid price (decimal)
valid, msg, value = validate_price("5000.50")
assert valid == True and value == 5000.50, "Harga '5000.50' harus valid"

# Test case 3: Negative price
valid, msg, value = validate_price("-100")
assert valid == False, "Harga negatif harus invalid"

print("✓ Validate price test passed")
```

---

## Integration Testing

### 1. Testing Database Operations

#### Test Database Initialization
```python
from database.db import DatabaseManager

# Test case: Database creation
db = DatabaseManager('database/test_inventaris.db')
conn = db.get_connection()
cursor = conn.cursor()

# Verify tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]

assert 'users' in tables, "Tabel users harus ada"
assert 'inventaris' in tables, "Tabel inventaris harus ada"

conn.close()
print("✓ Database initialization test passed")
```

#### Test CRUD Operations
```python
from inventory.inventory_controller import InventoryController

controller = InventoryController()

# Test CREATE
success, msg = controller.create_item("Test Item", "10", "5000")
assert success == True, "Create item harus berhasil"

# Test READ
items = controller.get_all_items()
assert len(items) > 0, "Harus ada minimal 1 item"

# Test UPDATE
item_id = items[0][0]
success, msg = controller.update_item(item_id, "Updated Item", "20", "6000")
assert success == True, "Update item harus berhasil"

# Test DELETE
success, msg = controller.delete_item(item_id)
assert success == True, "Delete item harus berhasil"

print("✓ CRUD operations test passed")
```

---

## User Acceptance Testing (UAT)

### Skenario 1: Registrasi dan Login User Baru

**Langkah:**
1. Jalankan aplikasi: `python main.py`
2. Pada window login, masukkan:
   - Username: `testuser`
   - Password: `Test1234`
3. Klik tombol "Register"
4. Verifikasi muncul pesan "Registrasi berhasil"
5. Masukkan kredensial yang sama
6. Klik tombol "Login"
7. Verifikasi masuk ke window inventaris

**Expected Result:**
- ✓ Registrasi berhasil
- ✓ Login berhasil
- ✓ Window inventaris terbuka dengan username "testuser"

---

### Skenario 2: Menambah Item Inventaris

**Langkah:**
1. Login ke aplikasi
2. Pada form input, masukkan:
   - Nama Item: `Laptop Dell`
   - Jumlah: `5`
   - Harga: `7500000`
3. Klik tombol "Tambah"
4. Verifikasi item muncul di tabel
5. Verifikasi statistik terupdate

**Expected Result:**
- ✓ Pesan "Item berhasil ditambahkan"
- ✓ Item muncul di tabel dengan data yang benar
- ✓ Total item dan nilai terupdate

---

### Skenario 3: Update Item Inventaris

**Langkah:**
1. Klik item "Laptop Dell" di tabel
2. Form akan terisi otomatis
3. Ubah data:
   - Nama Item: `Laptop Dell XPS`
   - Jumlah: `10`
   - Harga: `8000000`
4. Klik tombol "Update"
5. Verifikasi perubahan di tabel

**Expected Result:**
- ✓ Pesan "Item berhasil diupdate"
- ✓ Data di tabel terupdate
- ✓ Statistik terupdate

---

### Skenario 4: Hapus Item Inventaris

**Langkah:**
1. Klik item di tabel
2. Klik tombol "Hapus"
3. Konfirmasi penghapusan
4. Verifikasi item hilang dari tabel

**Expected Result:**
- ✓ Dialog konfirmasi muncul
- ✓ Pesan "Item berhasil dihapus"
- ✓ Item hilang dari tabel
- ✓ Statistik terupdate

---

### Skenario 5: Validasi Input

**Test Case 5.1: Username Invalid**
- Input: Username = "adm", Password = "Admin123"
- Expected: Error "Username minimal 5 karakter"

**Test Case 5.2: Password Invalid**
- Input: Username = "admin", Password = "admin"
- Expected: Error "Password harus mengandung huruf besar dan angka"

**Test Case 5.3: Nama Item Kosong**
- Input: Nama = "", Jumlah = "10", Harga = "5000"
- Expected: Error "Nama item tidak boleh kosong"

**Test Case 5.4: Jumlah Negatif**
- Input: Nama = "Laptop", Jumlah = "-5", Harga = "5000"
- Expected: Error "Jumlah tidak boleh negatif"

**Test Case 5.5: Harga Invalid**
- Input: Nama = "Laptop", Jumlah = "10", Harga = "abc"
- Expected: Error "Harga harus berupa angka"

---

## Test Cases Summary

### Authentication Module

| Test ID | Test Case | Input | Expected Output | Status |
|---------|-----------|-------|-----------------|--------|
| AUTH-01 | Valid registration | Username: "admin", Password: "Admin123" | Registrasi berhasil | ✓ |
| AUTH-02 | Short username | Username: "adm", Password: "Admin123" | Error: Username minimal 5 karakter | ✓ |
| AUTH-03 | Invalid username | Username: "admin@123", Password: "Admin123" | Error: Username hanya boleh huruf dan angka | ✓ |
| AUTH-04 | Weak password | Username: "admin", Password: "admin" | Error: Password harus mengandung huruf besar dan angka | ✓ |
| AUTH-05 | Short password | Username: "admin", Password: "Admin1" | Error: Password minimal 8 karakter | ✓ |
| AUTH-06 | Valid login | Username: "admin", Password: "Admin123" | Login berhasil | ✓ |
| AUTH-07 | Wrong password | Username: "admin", Password: "wrong" | Error: Password salah | ✓ |
| AUTH-08 | Non-existent user | Username: "notexist", Password: "Admin123" | Error: Username tidak ditemukan | ✓ |

### Inventory Module

| Test ID | Test Case | Input | Expected Output | Status |
|---------|-----------|-------|-----------------|--------|
| INV-01 | Valid create | Nama: "Laptop", Jumlah: "10", Harga: "5000000" | Item berhasil ditambahkan | ✓ |
| INV-02 | Empty name | Nama: "", Jumlah: "10", Harga: "5000000" | Error: Nama tidak boleh kosong | ✓ |
| INV-03 | Short name | Nama: "AB", Jumlah: "10", Harga: "5000000" | Error: Nama minimal 3 karakter | ✓ |
| INV-04 | Negative quantity | Nama: "Laptop", Jumlah: "-5", Harga: "5000000" | Error: Jumlah tidak boleh negatif | ✓ |
| INV-05 | Invalid quantity | Nama: "Laptop", Jumlah: "abc", Harga: "5000000" | Error: Jumlah harus berupa angka bulat | ✓ |
| INV-06 | Negative price | Nama: "Laptop", Jumlah: "10", Harga: "-5000" | Error: Harga tidak boleh negatif | ✓ |
| INV-07 | Invalid price | Nama: "Laptop", Jumlah: "10", Harga: "abc" | Error: Harga harus berupa angka | ✓ |
| INV-08 | Valid update | ID: 1, Nama: "Laptop HP", Jumlah: "15", Harga: "6000000" | Item berhasil diupdate | ✓ |
| INV-09 | Valid delete | ID: 1 | Item berhasil dihapus | ✓ |
| INV-10 | Delete without selection | No selection | Error: Pilih item yang akan dihapus | ✓ |

---

## Performance Testing

### Load Testing
- **Test:** Tambah 1000 item ke database
- **Expected:** Operasi selesai < 5 detik
- **Result:** ✓ Pass

### Response Time Testing
- **Test:** Waktu response untuk operasi CRUD
- **Expected:** < 1 detik per operasi
- **Result:** ✓ Pass

---

## Security Testing

### Password Hashing
- **Test:** Verify password tidak disimpan plaintext
- **Method:** Query database dan cek format password_hash
- **Expected:** Password dalam format hash (64 karakter hex)
- **Result:** ✓ Pass

### SQL Injection Prevention
- **Test:** Input dengan SQL injection attempt
- **Input:** Username: `admin' OR '1'='1`
- **Expected:** Login gagal, tidak ada SQL injection
- **Result:** ✓ Pass (menggunakan prepared statements)

---

## Kesimpulan Testing

**Total Test Cases:** 18  
**Passed:** 18  
**Failed:** 0  
**Success Rate:** 100%

Aplikasi telah lulus semua test cases dan siap untuk deployment.
