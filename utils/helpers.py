"""
Helpers Module
Modul ini berisi fungsi-fungsi utility umum yang digunakan
di berbagai bagian aplikasi.

Author: Proyek Akhir - Teknik Informatika
"""


def format_currency(amount):
    """
    Format angka menjadi format mata uang Rupiah.
    
    Args:
        amount (float): Jumlah uang
        
    Returns:
        str: String terformat (contoh: "Rp 1.000.000")
    """
    return f"Rp {amount:,.0f}".replace(',', '.')


def format_number(number):
    """
    Format angka dengan pemisah ribuan.
    
    Args:
        number (int): Angka yang akan diformat
        
    Returns:
        str: String terformat (contoh: "1.000")
    """
    return f"{number:,}".replace(',', '.')


def clear_entries(*entries):
    """
    Membersihkan isi dari multiple Entry widgets.
    
    Args:
        *entries: Variable number of Entry widgets
    """
    for entry in entries:
        entry.delete(0, 'end')


def confirm_action(title, message):
    """
    Menampilkan dialog konfirmasi.
    
    Args:
        title (str): Judul dialog
        message (str): Pesan konfirmasi
        
    Returns:
        bool: True jika user mengkonfirmasi, False jika tidak
    """
    from tkinter import messagebox
    return messagebox.askyesno(title, message)
