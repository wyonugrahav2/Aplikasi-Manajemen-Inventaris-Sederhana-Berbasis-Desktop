# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller Spec File untuk Aplikasi Manajemen Inventaris
File ini digunakan untuk konfigurasi advanced PyInstaller

Cara menggunakan:
    pyinstaller inventaris_app.spec

Author: Proyek Akhir - Teknik Informatika
"""

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('database', 'database'),  # Include database folder
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'sqlite3',
        'hashlib',
        're',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='InventarisApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compress dengan UPX (optional)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window (GUI only)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Bisa ditambahkan: icon='icon.ico'
)
