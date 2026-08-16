"""
Build Script untuk Membuat Executable
Menggunakan PyInstaller untuk convert Python ke EXE

Author: Proyek Akhir - Teknik Informatika
"""

import os
import sys
import shutil
import subprocess

def check_pyinstaller():
    """
    Cek apakah PyInstaller sudah terinstall.
    """
    try:
        import PyInstaller
        print("✓ PyInstaller sudah terinstall")
        return True
    except ImportError:
        print("✗ PyInstaller belum terinstall")
        print("\nInstalasi PyInstaller:")
        print("  pip install pyinstaller")
        return False

def clean_build_folders():
    """
    Membersihkan folder build dan dist dari build sebelumnya.
    """
    folders = ['build', 'dist', '__pycache__']
    for folder in folders:
        if os.path.exists(folder):
            print(f"Menghapus folder {folder}...")
            shutil.rmtree(folder)
    
    # Hapus file .spec jika ada
    spec_files = [f for f in os.listdir('.') if f.endswith('.spec')]
    for spec_file in spec_files:
        print(f"Menghapus {spec_file}...")
        os.remove(spec_file)
    
    print("✓ Cleanup selesai\n")

def build_exe():
    """
    Build executable menggunakan PyInstaller.
    """
    print("=" * 60)
    print("BUILDING EXECUTABLE")
    print("=" * 60)
    print()
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--name=InventarisApp',           # Nama executable
        '--onefile',                       # Single file executable
        '--windowed',                      # No console window (GUI only)
        '--icon=NONE',                     # Icon (bisa ditambahkan nanti)
        '--add-data=database;database',    # Include database folder
        '--hidden-import=tkinter',         # Ensure tkinter included
        '--hidden-import=sqlite3',         # Ensure sqlite3 included
        '--clean',                         # Clean cache
        'main.py'                          # Entry point
    ]
    
    print("Menjalankan PyInstaller...")
    print(f"Command: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("\n✓ Build berhasil!")
        print(f"\nFile executable ada di: dist/InventarisApp.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build gagal!")
        print(f"Error: {e.stderr}")
        return False

def build_onedir():
    """
    Build executable dalam folder (lebih cepat startup).
    """
    print("=" * 60)
    print("BUILDING EXECUTABLE (FOLDER MODE)")
    print("=" * 60)
    print()
    
    cmd = [
        'pyinstaller',
        '--name=InventarisApp',
        '--onedir',                        # Folder mode (bukan single file)
        '--windowed',
        '--icon=NONE',
        '--add-data=database;database',
        '--hidden-import=tkinter',
        '--hidden-import=sqlite3',
        '--clean',
        'main.py'
    ]
    
    print("Menjalankan PyInstaller (folder mode)...")
    print(f"Command: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        print("\n✓ Build berhasil!")
        print(f"\nFolder executable ada di: dist/InventarisApp/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Build gagal!")
        print(f"Error: {e.stderr}")
        return False

def main():
    """
    Main function untuk build process.
    """
    print("\n" + "=" * 60)
    print("BUILD SCRIPT - APLIKASI MANAJEMEN INVENTARIS")
    print("=" * 60)
    print()
    
    # Check PyInstaller
    if not check_pyinstaller():
        print("\nInstal PyInstaller terlebih dahulu:")
        print("  pip install pyinstaller")
        sys.exit(1)
    
    print("\nPilih mode build:")
    print("1. Single File (InventarisApp.exe) - Lambat startup, portable")
    print("2. Folder Mode (InventarisApp/) - Cepat startup, butuh folder")
    print("3. Both (Single File + Folder)")
    print("4. Clean only (hapus build folders)")
    
    choice = input("\nPilihan (1/2/3/4): ").strip()
    
    if choice == '4':
        clean_build_folders()
        print("✓ Cleanup selesai")
        return
    
    # Clean sebelum build
    clean_build_folders()
    
    if choice == '1':
        build_exe()
    elif choice == '2':
        build_onedir()
    elif choice == '3':
        print("\n--- Building Single File ---")
        build_exe()
        print("\n--- Building Folder Mode ---")
        build_onedir()
    else:
        print("Pilihan tidak valid")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("BUILD SELESAI")
    print("=" * 60)
    print("\nCek folder 'dist/' untuk hasil build")

if __name__ == "__main__":
    main()
