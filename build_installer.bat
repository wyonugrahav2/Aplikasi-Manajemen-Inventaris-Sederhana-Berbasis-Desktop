@echo off
REM Batch script untuk build installer secara otomatis
REM Script ini akan:
REM 1. Build EXE dengan PyInstaller
REM 2. Compile installer dengan Inno Setup

echo ============================================================
echo BUILD INSTALLER - APLIKASI MANAJEMEN INVENTARIS
echo ============================================================
echo.

REM Cek Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    pause
    exit /b 1
)

REM Cek PyInstaller
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PyInstaller belum terinstall!
    echo.
    echo Install dengan: pip install pyinstaller
    pause
    exit /b 1
)

echo [INFO] Step 1: Building EXE dengan PyInstaller...
echo.

REM Build EXE (folder mode untuk installer)
python build_exe.py

if errorlevel 1 (
    echo [ERROR] Build EXE gagal!
    pause
    exit /b 1
)

echo.
echo [INFO] Step 2: Checking Inno Setup...
echo.

REM Cek Inno Setup
set INNO_PATH="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if not exist %INNO_PATH% (
    echo [ERROR] Inno Setup tidak ditemukan!
    echo.
    echo Download dan install dari: https://jrsoftware.org/isinfo.php
    pause
    exit /b 1
)

echo [INFO] Step 3: Compiling installer dengan Inno Setup...
echo.

REM Compile installer
%INNO_PATH% setup_installer.iss

if errorlevel 1 (
    echo [ERROR] Compile installer gagal!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo BUILD SELESAI!
echo ============================================================
echo.
echo Installer ada di: installer_output\InventarisApp_Setup_v1.0.0.exe
echo.
pause
