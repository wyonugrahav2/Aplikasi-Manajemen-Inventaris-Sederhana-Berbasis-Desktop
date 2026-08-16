"""
Validators Module
Modul ini bertanggung jawab untuk:
1. Validasi input data inventaris
2. Validasi tipe data (integer, float)
3. Validasi business rules

Author: Proyek Akhir - Teknik Informatika
"""


def validate_item_name(nama):
    """
    Validasi nama item inventaris.
    
    Args:
        nama (str): Nama item
        
    Returns:
        tuple: (bool, str) - (status validasi, pesan error/sukses)
    """
    if not nama or not nama.strip():
        return False, "Nama item tidak boleh kosong"
    
    if len(nama.strip()) < 3:
        return False, "Nama item minimal 3 karakter"
    
    if len(nama.strip()) > 100:
        return False, "Nama item maksimal 100 karakter"
    
    return True, "Nama valid"


def validate_quantity(jumlah_str):
    """
    Validasi jumlah item (harus integer positif).
    
    Args:
        jumlah_str (str): Jumlah dalam bentuk string
        
    Returns:
        tuple: (bool, str, int) - (status validasi, pesan, nilai integer)
    """
    if not jumlah_str or not jumlah_str.strip():
        return False, "Jumlah tidak boleh kosong", None
    
    try:
        jumlah = int(jumlah_str)
    except ValueError:
        return False, "Jumlah harus berupa angka bulat", None
    
    if jumlah < 0:
        return False, "Jumlah tidak boleh negatif", None
    
    return True, "Jumlah valid", jumlah


def validate_price(harga_str):
    """
    Validasi harga item (harus numeric positif).
    
    Args:
        harga_str (str): Harga dalam bentuk string
        
    Returns:
        tuple: (bool, str, float) - (status validasi, pesan, nilai float)
    """
    if not harga_str or not harga_str.strip():
        return False, "Harga tidak boleh kosong", None
    
    try:
        harga = float(harga_str)
    except ValueError:
        return False, "Harga harus berupa angka", None
    
    if harga < 0:
        return False, "Harga tidak boleh negatif", None
    
    return True, "Harga valid", harga


def validate_item_data(nama, jumlah_str, harga_str):
    """
    Validasi lengkap data item inventaris.
    
    Args:
        nama (str): Nama item
        jumlah_str (str): Jumlah dalam bentuk string
        harga_str (str): Harga dalam bentuk string
        
    Returns:
        tuple: (bool, str, dict) - (status, pesan, data valid)
    """
    # Validasi nama
    valid_nama, msg_nama = validate_item_name(nama)
    if not valid_nama:
        return False, msg_nama, None
    
    # Validasi jumlah
    valid_jumlah, msg_jumlah, jumlah = validate_quantity(jumlah_str)
    if not valid_jumlah:
        return False, msg_jumlah, None
    
    # Validasi harga
    valid_harga, msg_harga, harga = validate_price(harga_str)
    if not valid_harga:
        return False, msg_harga, None
    
    # Return data yang sudah divalidasi
    data = {
        'nama': nama.strip(),
        'jumlah': jumlah,
        'harga': harga
    }
    
    return True, "Data valid", data
