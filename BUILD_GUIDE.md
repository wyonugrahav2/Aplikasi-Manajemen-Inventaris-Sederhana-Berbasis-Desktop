# Panduan Lengkap: Build EXE dan Installer

## Daftar Isi
1. [Persiapan](#persiapan)
2. [Membuat File EXE](#membuat-file-exe)
3. [Membuat Installer](#membuat-installer)
4. [Troubleshooting](#troubleshooting)

---

## PERSIAPAN

### 1. Install PyInstaller

PyInstaller adalah tool untuk convert Python script menjadi executable.

```cmd
pip install pyinstaller
```

**Verifikasi instalasi:**
```cmd
pyinstaller --version
```

### 2. Install Inno Setup (untuk Installer)

Download dan install Inno Setup:
- Website: https://jrsoftware.org/isinfo.php
- Download: Inno Setup 6.x (versi terbaru)
- Install dengan default settings

---

## MEMBUAT FILE EXE

### Metode 1: Menggunakan Build Script (Recommended)

Kami sudah menyediakan script otomatis untuk build.

**Langkah:**

1. **Buka Command Prompt di folder proyek**
   ```cmd
   cd C:\path\to\project
   ```

2. **Jalankan build script**
   ```cmd
   python build_exe.py
   ```

3. **Pilih mode build:**
   - **Option 1:** Single File (portable, lambat startup)
   - **Option 2:** Folder Mode (cepat startup, butuh folder)
   - **Option 3:** Both (buat keduanya)

4. **Tunggu proses build selesai**
   - Proses memakan waktu 1-5 menit
   - File hasil ada di folder `dist/`

**Output:**
```
dist/
├── InventarisApp.exe          # Single file (jika pilih option 1)
└── InventarisApp/             # Folder mode (jika pilih option 2)
    ├── InventarisApp.exe
    ├── _internal/
    └── database/
```

---

### Metode 2: Manual dengan PyInstaller

#### A. Single File Executable

```cmd
pyinstaller --name=InventarisApp --onefile --windowed --add-data="database;database" --hidden-import=tkinter --hidden-import=sqlite3 main.py
```

**Penjelasan parameter:**
- `--name=InventarisApp`: Nama file executable
- `--onefile`: Buat single file (portable)
- `--windowed`: No console window (GUI only)
- `--add-data="database;database"`: Include folder database
- `--hidden-import=tkinter`: Pastikan tkinter included
- `--hidden-import=sqlite3`: Pastikan sqlite3 included
- `main.py`: Entry point aplikasi

**Kelebihan:**
- ✓ Single file, portable
- ✓ Mudah didistribusikan

**Kekurangan:**
- ✗ Startup lebih lambat (extract ke temp folder)
- ✗ File size lebih besar

---

#### B. Folder Mode Executable

```cmd
pyinstaller --name=InventarisApp --onedir --windowed --add-data="database;database" --hidden-import=tkinter --hidden-import=sqlite3 main.py
```

**Penjelasan parameter:**
- `--onedir`: Buat folder dengan dependencies

**Kelebihan:**
- ✓ Startup lebih cepat
- ✓ Mudah di-debug

**Kekurangan:**
- ✗ Butuh folder lengkap (tidak portable)

---

### Metode 3: Menggunakan Spec File

Spec file memberikan kontrol lebih detail.

**Langkah:**

1. **Gunakan spec file yang sudah disediakan**
   ```cmd
   pyinstaller inventaris_app.spec
   ```

2. **Atau generate spec file baru**
   ```cmd
   pyi-makespec --name=InventarisApp --onefile --windowed main.py
   ```

3. **Edit spec file sesuai kebutuhan**
   - Tambahkan data files
   - Tambahkan hidden imports
   - Set icon

4. **Build dengan spec file**
   ```cmd
   pyinstaller inventaris_app.spec
   ```

---

## MEMBUAT INSTALLER

Setelah membuat EXE, kita buat installer profesional dengan Inno Setup.

### Langkah 1: Build EXE (Folder Mode)

**PENTING:** Untuk installer, gunakan **Folder Mode**, bukan Single File.

```cmd
python build_exe.py
# Pilih option 2 (Folder Mode)
```

Pastikan folder `dist/InventarisApp/` ada dan berisi:
```
dist/InventarisApp/
├── InventarisApp.exe
├── _internal/
│   ├── Python DLLs
│   └── Dependencies
└── database/
```

---

### Langkah 2: Konfigurasi Inno Setup Script

File `setup_installer.iss` sudah disediakan. Edit jika perlu:

```iss
#define MyAppName "Aplikasi Manajemen Inventaris"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Nama Anda"
```

**Penting:** Ganti `AppId` dengan GUID unik:
1. Buka https://www.guidgenerator.com/
2. Generate GUID baru
3. Replace di line:
   ```iss
   AppId={{GUID-ANDA-DI-SINI}}
   ```

---

### Langkah 3: Compile Installer

#### Cara 1: Menggunakan Inno Setup GUI

1. **Buka Inno Setup Compiler**
2. **File → Open** → Pilih `setup_installer.iss`
3. **Build → Compile**
4. **Tunggu proses selesai**

Output: `installer_output/InventarisApp_Setup_v1.0.0.exe`

---

#### Cara 2: Command Line

```cmd
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup_installer.iss
```

---

### Langkah 4: Test Installer

1. **Jalankan installer**
   ```
   installer_output/InventarisApp_Setup_v1.0.0.exe
   ```

2. **Ikuti wizard instalasi**
   - Pilih lokasi instalasi
   - Pilih create desktop icon (optional)
   - Install

3. **Test aplikasi**
   - Jalankan dari Start Menu
   - Atau dari Desktop shortcut
   - Verifikasi semua fitur berjalan

4. **Test uninstaller**
   - Control Panel → Programs → Uninstall
   - Atau dari Start Menu → Uninstall

---

## STRUKTUR FILE HASIL BUILD

### Setelah Build EXE

```
project_root/
├── build/                     # Temporary build files (bisa dihapus)
├── dist/
│   ├── InventarisApp.exe     # Single file (jika onefile)
│   └── InventarisApp/        # Folder mode (jika onedir)
│       ├── InventarisApp.exe
│       ├── _internal/
│       └── database/
└── InventarisApp.spec        # PyInstaller spec file
```

### Setelah Build Installer

```
project_root/
├── dist/
│   └── InventarisApp/        # Source untuk installer
└── installer_output/
    └── InventarisApp_Setup_v1.0.0.exe  # Installer final
```

---

## DISTRIBUSI

### File yang Didistribusikan

#### Option 1: Portable (Single File)
```
InventarisApp.exe              # ~15-25 MB
README.md                      # Dokumentasi
USER_GUIDE.md                  # Panduan pengguna
```

**Cara pakai:**
- Double-click `InventarisApp.exe`
- Tidak perlu instalasi

---

#### Option 2: Installer (Recommended)
```
InventarisApp_Setup_v1.0.0.exe  # ~20-30 MB
```

**Cara pakai:**
- Jalankan installer
- Ikuti wizard
- Aplikasi terinstall di Program Files
- Shortcut otomatis dibuat

---

## TROUBLESHOOTING

### Error: "PyInstaller not found"

**Solusi:**
```cmd
pip install pyinstaller
```

---

### Error: "Failed to execute script"

**Penyebab:** Missing dependencies atau hidden imports

**Solusi:**
1. Tambahkan hidden imports di spec file:
   ```python
   hiddenimports=['module_name']
   ```

2. Atau di command line:
   ```cmd
   --hidden-import=module_name
   ```

---

### Error: "tkinter not found"

**Solusi:**
```cmd
pyinstaller --hidden-import=tkinter --hidden-import=tkinter.ttk main.py
```

---

### Error: Database tidak ditemukan

**Penyebab:** Folder database tidak di-include

**Solusi:**
```cmd
pyinstaller --add-data="database;database" main.py
```

---

### EXE terlalu besar

**Solusi:**

1. **Gunakan UPX compression**
   ```cmd
   pyinstaller --upx-dir=C:\path\to\upx main.py
   ```

2. **Exclude modules yang tidak perlu**
   ```cmd
   pyinstaller --exclude-module=matplotlib main.py
   ```

3. **Gunakan folder mode** (lebih kecil dari onefile)

---

### Startup lambat (Single File)

**Penyebab:** Single file extract ke temp folder setiap startup

**Solusi:**
- Gunakan **Folder Mode** (`--onedir`)
- Atau buat installer

---

### Antivirus mendeteksi sebagai virus

**Penyebab:** False positive (umum untuk PyInstaller)

**Solusi:**

1. **Add exception di antivirus**
2. **Code signing certificate** (untuk distribusi profesional)
3. **Upload ke VirusTotal** untuk verifikasi

---

### Installer tidak bisa compile

**Error:** "Cannot find file"

**Solusi:**
1. Pastikan path di `setup_installer.iss` benar
2. Pastikan folder `dist/InventarisApp/` ada
3. Build EXE dulu sebelum compile installer

---

## TIPS DAN BEST PRACTICES

### 1. Testing

✅ **Selalu test di komputer lain** (tanpa Python terinstall)
✅ **Test di Windows versi berbeda** (Win 10, Win 11)
✅ **Test installer dan uninstaller**

### 2. Versioning

✅ **Update version number** di:
- `setup_installer.iss`
- `CHANGELOG.md`
- `README.md`

### 3. Documentation

✅ **Include dokumentasi** dalam installer:
- README.md
- USER_GUIDE.md
- LICENSE

### 4. Icon

✅ **Tambahkan icon** untuk profesionalitas:
```cmd
pyinstaller --icon=icon.ico main.py
```

Buat icon:
- Size: 256x256 pixels
- Format: .ico
- Tools: GIMP, Photoshop, atau online converter

### 5. Digital Signature

Untuk distribusi profesional, pertimbangkan **code signing certificate**:
- Menghilangkan warning "Unknown Publisher"
- Meningkatkan trust user
- Mengurangi false positive antivirus

---

## CHECKLIST BUILD

### Pre-Build
- [ ] Semua fitur sudah di-test
- [ ] Tidak ada error di console
- [ ] Database berfungsi dengan baik
- [ ] Dokumentasi sudah lengkap

### Build EXE
- [ ] PyInstaller terinstall
- [ ] Build script dijalankan
- [ ] EXE berhasil dibuat
- [ ] Test EXE di komputer lain

### Build Installer
- [ ] Inno Setup terinstall
- [ ] Spec file sudah dikonfigurasi
- [ ] GUID sudah diganti
- [ ] Installer berhasil di-compile
- [ ] Test instalasi
- [ ] Test uninstalasi

### Post-Build
- [ ] File size reasonable (<50 MB)
- [ ] Startup time acceptable (<5 detik)
- [ ] Semua fitur berfungsi
- [ ] Dokumentasi included
- [ ] Version number correct

---

## RESOURCES

### Tools
- **PyInstaller:** https://pyinstaller.org/
- **Inno Setup:** https://jrsoftware.org/isinfo.php
- **UPX:** https://upx.github.io/
- **GUID Generator:** https://www.guidgenerator.com/

### Documentation
- **PyInstaller Manual:** https://pyinstaller.org/en/stable/
- **Inno Setup Help:** https://jrsoftware.org/ishelp/

### Icon Resources
- **Icons8:** https://icons8.com/
- **Flaticon:** https://www.flaticon.com/
- **ICO Converter:** https://convertio.co/png-ico/

---

## KESIMPULAN

Dengan mengikuti panduan ini, Anda dapat:
✅ Membuat file executable (.exe) dari aplikasi Python
✅ Membuat installer profesional untuk Windows
✅ Mendistribusikan aplikasi ke user tanpa Python

**Rekomendasi untuk Proyek Akhir:**
- Gunakan **Installer** (lebih profesional)
- Include **dokumentasi lengkap**
- Test di **multiple computers**

---

**Selamat! Aplikasi Anda siap didistribusikan! 🚀**

© 2024 - Proyek Akhir Teknik Informatika
