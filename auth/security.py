"""
Security Module
Modul ini bertanggung jawab untuk:
1. Password hashing menggunakan SHA-256
2. Validasi username dan password
3. Verifikasi kredensial login

Author: Proyek Akhir - Teknik Informatika
"""

import hashlib
import re


def hash_password(password):
    """
    Melakukan hashing password menggunakan SHA-256.
    SHA-256 adalah cryptographic hash function yang menghasilkan
    256-bit (32-byte) hash value.
    
    Args:
        password (str): Password dalam bentuk plaintext
        
    Returns:
        str: Password yang sudah di-hash dalam format hexadecimal
        
    Example:
        >>> hash_password("Admin123")
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def validate_username(username):
    """
    Validasi username berdasarkan kriteria:
    - Panjang 5-20 karakter
    - Hanya alphanumeric (huruf dan angka)
    - Case-sensitive
    
    Args:
        username (str): Username yang akan divalidasi
        
    Returns:
        tuple: (bool, str) - (status validasi, pesan error/sukses)
    """
    if not username:
        return False, "Username tidak boleh kosong"
    
    if len(username) < 5:
        return False, "Username minimal 5 karakter"
    
    if len(username) > 20:
        return False, "Username maksimal 20 karakter"
    
    if not username.isalnum():
        return False, "Username hanya boleh huruf dan angka"
    
    return True, "Username valid"


def validate_password(password):
    """
    Validasi password berdasarkan kriteria keamanan:
    - Minimal 8 karakter
    - Mengandung minimal 1 huruf besar (A-Z)
    - Mengandung minimal 1 huruf kecil (a-z)
    - Mengandung minimal 1 angka (0-9)
    - Case-sensitive
    
    Args:
        password (str): Password yang akan divalidasi
        
    Returns:
        tuple: (bool, str) - (status validasi, pesan error/sukses)
    """
    if not password:
        return False, "Password tidak boleh kosong"
    
    if len(password) < 8:
        return False, "Password minimal 8 karakter"
    
    # Cek huruf besar menggunakan regex
    if not re.search(r'[A-Z]', password):
        return False, "Password harus mengandung minimal 1 huruf besar"
    
    # Cek huruf kecil menggunakan regex
    if not re.search(r'[a-z]', password):
        return False, "Password harus mengandung minimal 1 huruf kecil"
    
    # Cek angka menggunakan regex
    if not re.search(r'\d', password):
        return False, "Password harus mengandung minimal 1 angka"
    
    return True, "Password valid"


def verify_password(input_password, stored_hash):
    """
    Verifikasi password dengan membandingkan hash.
    
    Args:
        input_password (str): Password yang diinput user
        stored_hash (str): Hash password yang tersimpan di database
        
    Returns:
        bool: True jika password cocok, False jika tidak
    """
    input_hash = hash_password(input_password)
    return input_hash == stored_hash
