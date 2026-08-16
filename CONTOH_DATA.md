# Contoh Data untuk Testing

## Data User untuk Testing

### User 1 (Admin)
```
Username: admin
Password: Admin123
```

### User 2 (Manager)
```
Username: manager
Password: Manager123
```

### User 3 (Staff)
```
Username: staff01
Password: Staff123
```

---

## Data Inventaris untuk Testing

### Kategori: Elektronik

#### Item 1: Laptop
```
Nama Item: Laptop Dell XPS 13
Jumlah: 5
Harga: 15000000
Total Nilai: Rp 75.000.000
```

#### Item 2: Mouse
```
Nama Item: Mouse Logitech MX Master 3
Jumlah: 20
Harga: 1500000
Total Nilai: Rp 30.000.000
```

#### Item 3: Keyboard
```
Nama Item: Keyboard Mechanical Keychron K2
Jumlah: 15
Harga: 1200000
Total Nilai: Rp 18.000.000
```

#### Item 4: Monitor
```
Nama Item: Monitor LG UltraWide 34 inch
Jumlah: 8
Harga: 6500000
Total Nilai: Rp 52.000.000
```

#### Item 5: Printer
```
Nama Item: Printer HP LaserJet Pro
Jumlah: 3
Harga: 3500000
Total Nilai: Rp 10.500.000
```

---

### Kategori: Furniture

#### Item 6: Meja Kantor
```
Nama Item: Meja Kantor Standing Desk
Jumlah: 10
Harga: 2500000
Total Nilai: Rp 25.000.000
```

#### Item 7: Kursi
```
Nama Item: Kursi Ergonomis Herman Miller
Jumlah: 12
Harga: 8000000
Total Nilai: Rp 96.000.000
```

---

### Kategori: Alat Tulis

#### Item 8: Pulpen
```
Nama Item: Pulpen Pilot G2
Jumlah: 100
Harga: 5000
Total Nilai: Rp 500.000
```

#### Item 9: Buku Tulis
```
Nama Item: Buku Tulis A4 100 Lembar
Jumlah: 50
Harga: 15000
Total Nilai: Rp 750.000
```

#### Item 10: Spidol
```
Nama Item: Spidol Whiteboard Snowman
Jumlah: 30
Harga: 8000
Total Nilai: Rp 240.000
```

---

## Summary Total

```
Total Item: 10 jenis
Total Quantity: 253 unit
Total Nilai: Rp 307.990.000
```

---

## Test Cases dengan Data di Atas

### Test Case 1: Input Data Valid
**Input:** Laptop Dell XPS 13, 5, 15000000  
**Expected:** Item berhasil ditambahkan

### Test Case 2: Input Nama Kosong
**Input:** "", 5, 15000000  
**Expected:** Error "Nama item tidak boleh kosong"

### Test Case 3: Input Jumlah Negatif
**Input:** Laptop, -5, 15000000  
**Expected:** Error "Jumlah tidak boleh negatif"

### Test Case 4: Input Harga Invalid
**Input:** Laptop, 5, abc  
**Expected:** Error "Harga harus berupa angka"

### Test Case 5: Update Data
**Input:** ID=1, Laptop HP, 10, 16000000  
**Expected:** Item berhasil diupdate

### Test Case 6: Delete Data
**Input:** ID=1  
**Expected:** Item berhasil dihapus

---

## Skenario Testing Lengkap

### Skenario 1: Setup Awal
1. Registrasi user "admin" dengan password "Admin123"
2. Login dengan kredensial tersebut
3. Verifikasi masuk ke halaman inventaris

### Skenario 2: Input Data Massal
1. Input semua 10 item di atas satu per satu
2. Verifikasi setiap item muncul di tabel
3. Verifikasi statistik terupdate

### Skenario 3: Operasi CRUD
1. Pilih item "Laptop Dell XPS 13"
2. Update jumlah menjadi 10
3. Verifikasi perubahan
4. Hapus item
5. Verifikasi item hilang

### Skenario 4: Validasi Input
1. Coba input dengan nama kosong → Error
2. Coba input dengan jumlah negatif → Error
3. Coba input dengan harga invalid → Error
4. Verifikasi semua error message sesuai

### Skenario 5: Multi-User
1. Logout dari user "admin"
2. Registrasi user "manager"
3. Login dengan user "manager"
4. Verifikasi dapat melihat data yang sama
5. Tambah item baru
6. Logout dan login kembali dengan "admin"
7. Verifikasi item dari "manager" terlihat

---

## Data untuk Performance Testing

### Test Load 100 Items
Gunakan script Python untuk generate data:

```python
# generate_test_data.py
from inventory.inventory_controller import InventoryController

controller = InventoryController()

for i in range(1, 101):
    nama = f"Test Item {i}"
    jumlah = str(i * 10)
    harga = str(i * 100000)
    controller.create_item(nama, jumlah, harga)

print("100 items created successfully")
```

**Expected:**
- Operasi selesai < 5 detik
- Semua item tersimpan di database
- Tabel menampilkan semua item
- Statistik akurat

---

## Data untuk Boundary Testing

### Boundary Values

#### Nama Item
```
Min valid: "ABC" (3 karakter)
Max valid: "A" * 100 (100 karakter)
Invalid: "AB" (2 karakter)
Invalid: "A" * 101 (101 karakter)
```

#### Jumlah
```
Min valid: 0
Max valid: 999999999
Invalid: -1
Invalid: "abc"
```

#### Harga
```
Min valid: 0
Max valid: 999999999.99
Invalid: -0.01
Invalid: "xyz"
```

---

## Checklist Testing

- [ ] Registrasi user baru
- [ ] Login dengan kredensial valid
- [ ] Login dengan kredensial invalid
- [ ] Tambah item valid
- [ ] Tambah item dengan nama kosong
- [ ] Tambah item dengan jumlah negatif
- [ ] Tambah item dengan harga invalid
- [ ] Update item
- [ ] Delete item
- [ ] Clear form
- [ ] Statistik display
- [ ] Multi-user access
- [ ] Logout dan login kembali
- [ ] Data persistence (restart aplikasi)

---

**Gunakan data di atas untuk testing manual aplikasi!**
