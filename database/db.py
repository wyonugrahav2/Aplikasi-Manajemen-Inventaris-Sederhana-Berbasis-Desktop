"""
Database Manager Module
Modul ini bertanggung jawab untuk:
1. Inisialisasi database SQLite
2. Pembuatan tabel users dan inventaris
3. Menyediakan koneksi database untuk modul lain

Author: Proyek Akhir - Teknik Informatika
"""

import sqlite3
import os


class DatabaseManager:
    """
    Class untuk mengelola koneksi dan operasi database SQLite.
    Mengimplementasikan Singleton pattern untuk memastikan hanya ada satu koneksi.
    """
    
    def __init__(self, db_path='database/inventaris.db'):
        """
        Inisialisasi DatabaseManager.
        
        Args:
            db_path (str): Path ke file database SQLite
        """
        self.db_path = db_path
        self._ensure_database_directory()
        self._initialize_database()
    
    def _ensure_database_directory(self):
        """
        Memastikan direktori database ada.
        Jika tidak ada, akan dibuat secara otomatis.
        """
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
    
    def _initialize_database(self):
        """
        Inisialisasi database dan membuat tabel jika belum ada.
        Menggunakan IF NOT EXISTS untuk mencegah error jika tabel sudah ada.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabel users untuk sistem autentikasi
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        
        # Tabel inventaris untuk data barang
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventaris (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                jumlah INTEGER NOT NULL CHECK(jumlah >= 0),
                harga REAL NOT NULL CHECK(harga >= 0)
            )
        ''')
        
        conn.commit()
        conn.close()
        print("[INFO] Database berhasil diinisialisasi")
    
    def get_connection(self):
        """
        Membuat dan mengembalikan koneksi baru ke database.
        
        Returns:
            sqlite3.Connection: Objek koneksi database
        """
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query, params=None):
        """
        Eksekusi query SELECT dan mengembalikan hasil.
        
        Args:
            query (str): SQL query untuk dieksekusi
            params (tuple): Parameter untuk prepared statement
            
        Returns:
            list: Hasil query dalam bentuk list of tuples
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        results = cursor.fetchall()
        conn.close()
        return results
    
    def execute_update(self, query, params=None):
        """
        Eksekusi query INSERT, UPDATE, atau DELETE.
        
        Args:
            query (str): SQL query untuk dieksekusi
            params (tuple): Parameter untuk prepared statement
            
        Returns:
            int: Jumlah baris yang terpengaruh
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            conn.commit()
            affected_rows = cursor.rowcount
            return affected_rows
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


# Instance global untuk digunakan di seluruh aplikasi
db_manager = DatabaseManager()
