# Panduan Deployment dan Distribusi

## Daftar Isi
1. [Persiapan Deployment](#persiapan-deployment)
2. [Build Process](#build-process)
3. [Testing](#testing)
4. [Distribusi](#distribusi)
5. [Maintenance](#maintenance)

---

## PERSIAPAN DEPLOYMENT

### 1. Pre-Deployment Checklist

#### Code Quality
- [ ] Semua fitur sudah di-test dan berfungsi
- [ ] Tidak ada error atau warning di console
- [ ] Code sudah di-review dan clean
- [ ] Dokumentasi sudah lengkap dan up-to-date

#### Version Control
- [ ] Version number sudah diupdate di semua file
- [ ] CHANGELOG.md sudah diupdate
- [ ] Git commit dan tag version
  ```bash
  git add .
  git commit -m "Release v1.0.0"
  git tag v1.0.0
  ```

#### Documentation
- [ ] README.md lengkap
- [ ] USER_GUIDE.md lengkap
- [ ] BUILD_GUIDE.md lengkap
- [ ] LICENSE file ada

#### Testing
- [ ] Unit tests passed
- [ ] Integration tests passed
- [ ] UAT completed
- [ ] Test di multiple Windows versions

---

## BUILD PROCESS

### Metode 1: Build Otomatis (Recommended)

#### Windows

**Build EXE + Installer:**
```cmd
build_installer.bat
```

Script ini akan:
1. ✓ Check dependencies
2. ✓ Build EXE dengan PyInstaller
3. ✓ Compile installer dengan Inno Setup
4. ✓ Output installer siap distribusi

**Output:**
```
installer_output/InventarisApp_Setup_v1.0.0.exe
```

---

### Metode 2: Build Manual

#### Step 1: Install Dependencies

```cmd
pip install pyinstaller
```

Download Inno Setup:
- https://jrsoftware.org/isinfo.php

---

#### Step 2: Build EXE

**Option A: Single File (Portable)**
```cmd
pyinstaller --name=InventarisApp --onefile --windowed --add-data="database;database" --hidden-import=tkinter --hidden-import=sqlite3 main.py
```

**Option B: Folder Mode (untuk Installer)**
```cmd
pyinstaller --name=InventarisApp --onedir --windowed --add-data="database;database" --hidden-import=tkinter --hidden-import=sqlite3 main.py
```

**Output:**
```
dist/
├── InventarisApp.exe          # Single file
└── InventarisApp/             # Folder mode
    ├── InventarisApp.exe
    └── _internal/
```

---

#### Step 3: Build Installer

1. **Edit setup_installer.iss**
   - Update version number
   - Generate dan ganti GUID baru
   - Update publisher info

2. **Compile dengan Inno Setup**
   ```cmd
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup_installer.iss
   ```

3. **Output:**
   ```
   installer_output/InventarisApp_Setup_v1.0.0.exe
   ```

---

## TESTING

### 1. Test EXE

#### Test di Development Machine

```cmd
cd dist
InventarisApp.exe
```

**Checklist:**
- [ ] Aplikasi berjalan tanpa error
- [ ] Login berfungsi
- [ ] CRUD operations berfungsi
- [ ] Database tersimpan dengan benar
- [ ] Statistik terupdate
- [ ] Tidak ada console window muncul

---

#### Test di Clean Machine

**Setup test environment:**
1. Virtual Machine atau komputer lain
2. Windows 10/11 fresh install
3. **TIDAK ADA Python terinstall**

**Test procedure:**
1. Copy `InventarisApp.exe` ke test machine
2. Double-click untuk run
3. Test semua fitur
4. Verifikasi database dibuat
5. Restart aplikasi, verifikasi data persist

**Expected result:**
- ✓ Aplikasi berjalan tanpa Python
- ✓ Semua fitur berfungsi
- ✓ Data tersimpan persistent

---

### 2. Test Installer

#### Installation Test

1. **Jalankan installer**
   ```
   InventarisApp_Setup_v1.0.0.exe
   ```

2. **Wizard steps:**
   - [ ] Welcome screen muncul
   - [ ] License agreement ditampilkan
   - [ ] Pilih lokasi instalasi
   - [ ] Pilih Start Menu folder
   - [ ] Pilih create desktop icon
   - [ ] Installation progress
   - [ ] Completion screen

3. **Verify installation:**
   - [ ] Files terinstall di Program Files
   - [ ] Start Menu shortcut dibuat
   - [ ] Desktop icon dibuat (jika dipilih)
   - [ ] Uninstaller terdaftar di Control Panel

---

#### Application Test

1. **Launch dari Start Menu**
   - [ ] Aplikasi berjalan
   - [ ] Semua fitur berfungsi

2. **Launch dari Desktop**
   - [ ] Shortcut berfungsi
   - [ ] Aplikasi berjalan

3. **Data persistence**
   - [ ] Buat data test
   - [ ] Close aplikasi
   - [ ] Buka lagi
   - [ ] Data masih ada

---

#### Uninstallation Test

1. **Uninstall via Control Panel**
   ```
   Control Panel → Programs → Uninstall a program
   ```

2. **Verify uninstallation:**
   - [ ] Files dihapus dari Program Files
   - [ ] Start Menu shortcut dihapus
   - [ ] Desktop icon dihapus
   - [ ] Registry entries dihapus
   - [ ] Uninstaller hilang dari Control Panel

---

### 3. Compatibility Test

Test di berbagai environment:

| OS | Version | Status |
|----|---------|--------|
| Windows 10 | 21H2 | ✓ |
| Windows 10 | 22H2 | ✓ |
| Windows 11 | 21H2 | ✓ |
| Windows 11 | 22H2 | ✓ |

---

### 4. Security Test

#### Antivirus Scan

Upload ke VirusTotal:
- https://www.virustotal.com/

**Expected:**
- 0-2 false positives (normal untuk PyInstaller)

**Jika banyak detection:**
1. Review code untuk suspicious patterns
2. Exclude unnecessary modules
3. Consider code signing

---

#### Windows SmartScreen

**Test:**
1. Download installer dari internet
2. Run installer
3. Check SmartScreen warning

**Expected:**
- "Unknown publisher" warning (normal tanpa code signing)

**Solution:**
- Click "More info" → "Run anyway"
- Atau: Get code signing certificate

---

## DISTRIBUSI

### 1. File yang Didistribusikan

#### Option A: Portable Version

**Package:**
```
InventarisApp_Portable_v1.0.0.zip
├── InventarisApp.exe
├── README.md
├── USER_GUIDE.md
└── LICENSE
```

**Cara pakai:**
1. Extract ZIP
2. Double-click `InventarisApp.exe`
3. Tidak perlu instalasi

**Kelebihan:**
- ✓ Portable, bisa di USB
- ✓ Tidak perlu admin rights
- ✓ Tidak modify system

**Kekurangan:**
- ✗ Startup lebih lambat
- ✗ Tidak ada Start Menu entry

---

#### Option B: Installer Version (Recommended)

**Package:**
```
InventarisApp_Setup_v1.0.0.exe
```

**Cara pakai:**
1. Run installer
2. Follow wizard
3. Launch dari Start Menu

**Kelebihan:**
- ✓ Professional installation
- ✓ Start Menu integration
- ✓ Uninstaller included
- ✓ Faster startup

**Kekurangan:**
- ✗ Butuh admin rights (optional)
- ✗ Modify system

---

### 2. Distribution Channels

#### Direct Download

**Setup:**
1. Upload ke file hosting:
   - Google Drive
   - Dropbox
   - OneDrive
   - GitHub Releases

2. Create download page:
   - Version info
   - System requirements
   - Installation instructions
   - Screenshots

**Example GitHub Release:**
```markdown
## Release v1.0.0

### Downloads
- [Installer (Recommended)](link-to-installer.exe) - 25 MB
- [Portable Version](link-to-portable.zip) - 20 MB

### System Requirements
- Windows 10/11 (64-bit)
- 50 MB free disk space
- No Python required

### Installation
1. Download installer
2. Run as administrator
3. Follow wizard

### What's New
- Initial release
- Login system
- CRUD operations
- Database management
```

---

#### GitHub Releases

**Steps:**
1. Create release on GitHub
2. Upload installer
3. Write release notes
4. Tag version

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

#### Website/Blog

**Create landing page:**
- Product description
- Features list
- Screenshots
- Download button
- Documentation links
- Support contact

---

### 3. Documentation Distribution

**Include with installer:**
- README.md
- USER_GUIDE.md
- LICENSE

**Online documentation:**
- GitHub Wiki
- GitHub Pages
- ReadTheDocs

---

## MAINTENANCE

### 1. Version Updates

**Semantic Versioning:**
```
MAJOR.MINOR.PATCH
1.0.0
```

- **MAJOR:** Breaking changes
- **MINOR:** New features (backward compatible)
- **PATCH:** Bug fixes

**Example:**
- `1.0.0` → Initial release
- `1.0.1` → Bug fix
- `1.1.0` → New feature
- `2.0.0` → Breaking change

---

### 2. Update Process

**Steps:**
1. Fix bugs atau add features
2. Update version number
3. Update CHANGELOG.md
4. Test thoroughly
5. Build new installer
6. Create GitHub release
7. Notify users

---

### 3. Bug Tracking

**Use GitHub Issues:**
- Bug reports
- Feature requests
- Questions

**Issue template:**
```markdown
## Bug Description
[Describe the bug]

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: Windows 10
- Version: 1.0.0
- Error message: [if any]

## Screenshots
[If applicable]
```

---

### 4. User Support

**Support channels:**
- GitHub Issues
- Email support
- Documentation
- FAQ

**Response time:**
- Critical bugs: 24 hours
- Normal bugs: 1 week
- Feature requests: 1 month

---

## ADVANCED TOPICS

### 1. Code Signing

**Why:**
- Remove "Unknown Publisher" warning
- Increase user trust
- Reduce antivirus false positives

**How:**
1. Get code signing certificate
   - DigiCert
   - Sectigo
   - GlobalSign

2. Sign executable:
   ```cmd
   signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com InventarisApp.exe
   ```

**Cost:**
- ~$100-300/year

---

### 2. Auto-Update

**Implementation:**
1. Check for updates on startup
2. Download new version
3. Install update
4. Restart application

**Libraries:**
- PyUpdater
- Esky

---

### 3. Analytics

**Track:**
- Installation count
- Active users
- Feature usage
- Crash reports

**Tools:**
- Google Analytics
- Sentry (crash reporting)
- Custom analytics

---

### 4. Localization

**Support multiple languages:**
- Indonesian (default)
- English
- Others

**Implementation:**
- Use gettext
- Separate language files
- Language selector in settings

---

## CHECKLIST DEPLOYMENT

### Pre-Deployment
- [ ] Code tested and working
- [ ] Version number updated
- [ ] CHANGELOG updated
- [ ] Documentation complete
- [ ] Git committed and tagged

### Build
- [ ] PyInstaller installed
- [ ] Inno Setup installed
- [ ] EXE built successfully
- [ ] Installer compiled successfully

### Testing
- [ ] EXE tested on dev machine
- [ ] EXE tested on clean machine
- [ ] Installer tested
- [ ] Uninstaller tested
- [ ] Compatibility tested
- [ ] Antivirus scan passed

### Distribution
- [ ] Files uploaded
- [ ] Release notes written
- [ ] Download links working
- [ ] Documentation accessible

### Post-Deployment
- [ ] Monitor for issues
- [ ] Respond to user feedback
- [ ] Plan next version

---

## RESOURCES

### Tools
- **PyInstaller:** https://pyinstaller.org/
- **Inno Setup:** https://jrsoftware.org/isinfo.php
- **VirusTotal:** https://www.virustotal.com/
- **Code Signing:** https://www.digicert.com/

### Documentation
- **PyInstaller Manual:** https://pyinstaller.org/en/stable/
- **Inno Setup Help:** https://jrsoftware.org/ishelp/
- **Semantic Versioning:** https://semver.org/

---

## KESIMPULAN

Dengan mengikuti panduan ini, Anda dapat:
✅ Build executable dan installer profesional
✅ Test secara menyeluruh
✅ Distribute ke users
✅ Maintain dan update aplikasi

**Aplikasi Anda siap untuk production deployment! 🚀**

© 2024 - Proyek Akhir Teknik Informatika
