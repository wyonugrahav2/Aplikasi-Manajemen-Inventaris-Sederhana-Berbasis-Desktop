"""
Inventory Controller Module
Modul ini bertanggung jawab untuk:
1. Business logic CRUD inventaris
2. Interaksi dengan database untuk operasi inventaris
3. Validasi data sebelum operasi database

Author: Proyek Akhir - Teknik Informatika
"""

import sys
import os

# Menambahkan parent directory ke path untuk import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db import db_manager
from utils.validators import validate_item_data


class InventoryController:
    """
    Controller untuk mengelola operasi CRUD inventaris.
    Mengimplementasikan business logic layer.
    """
    
    def __init__(self):
        """
        Inisialisasi InventoryController.
        """
        self.db = db_manager
    
    def get_all_items(self):
        """
        Mengambil semua item dari database.
        
        Returns:
            list: List of tuples berisi data item (id, nama, jumlah, harga)
        """
        query = "SELECT id, nama, jumlah, harga FROM inventaris ORDER BY id"
        return self.db.execute_query(query)
    
    def get_item_by_id(self, item_id):
        """
        Mengambil item berdasarkan ID.
        
        Args:
            item_id (int): ID item
            
        Returns:
            tuple: Data item (id, nama, jumlah, harga) atau None
        """
        query = "SELECT id, nama, jumlah, harga FROM inventaris WHERE id = ?"
        results = self.db.execute_query(query, (item_id,))
        return results[0] if results else None
    
    def create_item(self, nama, jumlah_str, harga_str):
        """
        Membuat item baru di inventaris.
        
        Args:
            nama (str): Nama item
            jumlah_str (str): Jumlah dalam bentuk string
            harga_str (str): Harga dalam bentuk string
            
        Returns:
            tuple: (bool, str) - (status sukses, pesan)
        """
        # Validasi data
        valid, message, data = validate_item_data(nama, jumlah_str, harga_str)
        if not valid:
            return False, message
        
        # Insert ke database
        query = "INSERT INTO inventaris (nama, jumlah, harga) VALUES (?, ?, ?)"
        try:
            self.db.execute_update(query, (data['nama'], data['jumlah'], data['harga']))
            return True, "Item berhasil ditambahkan"
        except Exception as e:
            return False, f"Gagal menambahkan item: {str(e)}"
    
    def update_item(self, item_id, nama, jumlah_str, harga_str):
        """
        Mengupdate item yang sudah ada.
        
        Args:
            item_id (int): ID item yang akan diupdate
            nama (str): Nama item baru
            jumlah_str (str): Jumlah baru dalam bentuk string
            harga_str (str): Harga baru dalam bentuk string
            
        Returns:
            tuple: (bool, str) - (status sukses, pesan)
        """
        # Validasi data
        valid, message, data = validate_item_data(nama, jumlah_str, harga_str)
        if not valid:
            return False, message
        
        # Cek apakah item ada
        if not self.get_item_by_id(item_id):
            return False, "Item tidak ditemukan"
        
        # Update database
        query = "UPDATE inventaris SET nama = ?, jumlah = ?, harga = ? WHERE id = ?"
        try:
            affected = self.db.execute_update(
                query, 
                (data['nama'], data['jumlah'], data['harga'], item_id)
            )
            if affected > 0:
                return True, "Item berhasil diupdate"
            else:
                return False, "Tidak ada perubahan data"
        except Exception as e:
            return False, f"Gagal mengupdate item: {str(e)}"
    
    def delete_item(self, item_id):
        """
        Menghapus item dari inventaris.
        
        Args:
            item_id (int): ID item yang akan dihapus
            
        Returns:
            tuple: (bool, str) - (status sukses, pesan)
        """
        # Cek apakah item ada
        if not self.get_item_by_id(item_id):
            return False, "Item tidak ditemukan"
        
        # Delete dari database
        query = "DELETE FROM inventaris WHERE id = ?"
        try:
            affected = self.db.execute_update(query, (item_id,))
            if affected > 0:
                return True, "Item berhasil dihapus"
            else:
                return False, "Gagal menghapus item"
        except Exception as e:
            return False, f"Gagal menghapus item: {str(e)}"
    
    def search_items(self, keyword):
        """
        Mencari item berdasarkan nama.
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            list: List of tuples berisi data item yang cocok
        """
        query = "SELECT id, nama, jumlah, harga FROM inventaris WHERE nama LIKE ? ORDER BY id"
        return self.db.execute_query(query, (f"%{keyword}%",))
    
    def get_total_items(self):
        """
        Menghitung total jumlah item di inventaris.
        
        Returns:
            int: Total jumlah item
        """
        query = "SELECT SUM(jumlah) FROM inventaris"
        result = self.db.execute_query(query)
        return result[0][0] if result[0][0] else 0
    
    def get_total_value(self):
        """
        Menghitung total nilai inventaris (jumlah * harga).
        
        Returns:
            float: Total nilai inventaris
        """
        query = "SELECT SUM(jumlah * harga) FROM inventaris"
        result = self.db.execute_query(query)
        return result[0][0] if result[0][0] else 0.0
