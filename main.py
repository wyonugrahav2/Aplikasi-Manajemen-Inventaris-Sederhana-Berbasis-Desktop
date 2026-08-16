"""
Main Entry Point
Aplikasi Manajemen Inventaris Sederhana Berbasis Desktop

Deskripsi:
Aplikasi ini adalah sistem manajemen inventaris sederhana yang dibangun
menggunakan Python, Tkinter, dan SQLite. Aplikasi ini mengimplementasikan
sistem autentikasi dan operasi CRUD untuk manajemen data inventaris.

Fitur Utama:
1. Sistem Login dengan password hashing (SHA-256)
2. CRUD Inventaris (Create, Read, Update, Delete)
3. Validasi input data
4. Database SQLite lokal
5. GUI berbasis Tkinter

Author: Proyek Akhir - Teknik Informatika
Platform: Windows & Linux
Python Version: 3.x
"""

import tkinter as tk
from auth.login import LoginWindow
from inventory.inventory_ui import InventoryWindow


def main():
    """
    Fungsi utama aplikasi.
    Menginisialisasi window login dan menangani flow aplikasi.
    """
    
    def on_login_success(username):
        """
        Callback function yang dipanggil setelah login berhasil.
        Membuka window inventaris.
        
        Args:
            username (str): Username user yang berhasil login
        """
        # Buat window baru untuk inventaris
        inventory_root = tk.Tk()
        InventoryWindow(inventory_root, username)
        inventory_root.mainloop()
    
    # Inisialisasi window login
    login_root = tk.Tk()
    LoginWindow(login_root, on_login_success)
    login_root.mainloop()


if __name__ == "__main__":
    print("=" * 60)
    print("SISTEM MANAJEMEN INVENTARIS")
    print("Proyek Akhir - Teknik Informatika")
    print("=" * 60)
    print("\n[INFO] Aplikasi dimulai...")
    print("[INFO] Silakan login untuk melanjutkan\n")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Aplikasi dihentikan oleh user")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {str(e)}")
    finally:
        print("\n[INFO] Terima kasih telah menggunakan aplikasi ini")
        print("=" * 60)
