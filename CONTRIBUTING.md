# Contributing Guidelines

Terima kasih atas minat Anda untuk berkontribusi pada proyek ini!

## 🎓 Konteks Akademik

Proyek ini adalah Proyek Akhir untuk mata kuliah Teknik Informatika. Kontribusi sangat diterima untuk:
- Perbaikan bug
- Peningkatan dokumentasi
- Penambahan fitur
- Optimasi kode

## 🚀 Cara Berkontribusi

### 1. Fork Repository

```bash
# Fork repository ini ke akun GitHub Anda
# Clone fork Anda
git clone https://github.com/your-username/inventory-management-app.git
cd inventory-management-app
```

### 2. Buat Branch Baru

```bash
# Buat branch untuk fitur/perbaikan Anda
git checkout -b feature/nama-fitur
# atau
git checkout -b fix/nama-bug
```

### 3. Lakukan Perubahan

- Ikuti style guide yang ada
- Tambahkan dokumentasi untuk kode baru
- Update README jika perlu
- Pastikan kode berjalan tanpa error

### 4. Testing

```bash
# Test perubahan Anda
python main.py

# Pastikan semua fungsi berjalan dengan baik
```

### 5. Commit Changes

```bash
git add .
git commit -m "feat: menambahkan fitur export CSV"
# atau
git commit -m "fix: memperbaiki bug validasi harga"
```

**Commit Message Convention:**
- `feat:` untuk fitur baru
- `fix:` untuk perbaikan bug
- `docs:` untuk perubahan dokumentasi
- `style:` untuk formatting
- `refactor:` untuk refactoring kode
- `test:` untuk testing
- `chore:` untuk maintenance

### 6. Push ke GitHub

```bash
git push origin feature/nama-fitur
```

### 7. Buat Pull Request

- Buka repository Anda di GitHub
- Klik "New Pull Request"
- Jelaskan perubahan yang Anda buat
- Submit pull request

## 📋 Checklist Pull Request

Sebelum submit PR, pastikan:

- [ ] Kode berjalan tanpa error
- [ ] Dokumentasi sudah diupdate
- [ ] Commit message jelas dan deskriptif
- [ ] Tidak ada conflict dengan branch main
- [ ] Testing sudah dilakukan
- [ ] Code style konsisten

## 🎨 Code Style Guide

### Python Style

Ikuti PEP 8 Python Style Guide:

```python
# Good
def calculate_total_value(quantity, price):
    """
    Menghitung total nilai item.
    
    Args:
        quantity (int): Jumlah item
        price (float): Harga per item
        
    Returns:
        float: Total nilai
    """
    return quantity * price

# Bad
def calc(q,p):
    return q*p
```

### Naming Conventions

- **Variables:** `snake_case`
- **Functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_CASE`

```python
# Good
user_name = "admin"
def validate_input():
    pass
class DatabaseManager:
    pass
MAX_ITEMS = 1000

# Bad
UserName = "admin"
def ValidateInput():
    pass
class database_manager:
    pass
maxItems = 1000
```

### Documentation

Setiap fungsi harus memiliki docstring:

```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        type: Description
        
    Raises:
        ExceptionType: Description
    """
    pass
```

## 🐛 Melaporkan Bug

Jika menemukan bug, buat issue dengan informasi:

1. **Deskripsi bug:** Jelaskan apa yang terjadi
2. **Langkah reproduksi:** Bagaimana bug terjadi
3. **Expected behavior:** Apa yang seharusnya terjadi
4. **Screenshots:** Jika memungkinkan
5. **Environment:**
   - OS: Windows/Linux/Mac
   - Python version: 3.x
   - Error message: Copy paste error

**Template Issue:**

```markdown
## Bug Description
[Jelaskan bug secara singkat]

## Steps to Reproduce
1. Buka aplikasi
2. Klik tombol X
3. Error muncul

## Expected Behavior
[Apa yang seharusnya terjadi]

## Actual Behavior
[Apa yang sebenarnya terjadi]

## Screenshots
[Jika ada]

## Environment
- OS: Windows 11
- Python: 3.11.0
- Error: [Copy paste error message]
```

## 💡 Mengusulkan Fitur

Untuk mengusulkan fitur baru, buat issue dengan:

1. **Deskripsi fitur:** Apa fitur yang diusulkan
2. **Motivasi:** Mengapa fitur ini diperlukan
3. **Use case:** Bagaimana fitur akan digunakan
4. **Alternatif:** Apakah ada alternatif lain

**Template Feature Request:**

```markdown
## Feature Description
[Jelaskan fitur yang diusulkan]

## Motivation
[Mengapa fitur ini diperlukan]

## Use Case
[Bagaimana fitur akan digunakan]

## Alternatives
[Apakah ada alternatif lain]
```

## 🔍 Review Process

Setelah submit PR:

1. Maintainer akan review kode Anda
2. Mungkin ada request untuk perubahan
3. Setelah approved, PR akan di-merge
4. Kontribusi Anda akan masuk ke changelog

## 📚 Area Kontribusi

Beberapa area yang membutuhkan kontribusi:

### High Priority
- [ ] Export/Import data (CSV, Excel)
- [ ] Search dan filter advanced
- [ ] Backup/restore database
- [ ] Unit tests

### Medium Priority
- [ ] Dark mode theme
- [ ] Keyboard shortcuts
- [ ] Print laporan
- [ ] Grafik statistik

### Low Priority
- [ ] Multi-language support
- [ ] Custom themes
- [ ] Plugin system
- [ ] API integration

## 🤝 Code of Conduct

- Bersikap profesional dan hormat
- Terima kritik konstruktif
- Fokus pada improvement
- Bantu sesama contributor

## 📞 Kontak

Jika ada pertanyaan:
- **Email:** [wyonugrahav2@gmail.com]
- **GitHub Issues:** [repository-url]/issues
- **Discussion:** [repository-url]/discussions

## 🙏 Terima Kasih

Terima kasih telah berkontribusi pada proyek ini! Setiap kontribusi, sekecil apapun, sangat berarti.

---

**Happy Coding! 🚀**

© 2024 - Proyek Akhir Teknik Informatika
