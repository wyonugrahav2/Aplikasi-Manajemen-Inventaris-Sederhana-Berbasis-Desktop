"""
Login UI Module
Modul ini bertanggung jawab untuk:
1. Menampilkan GUI login
2. Menangani proses autentikasi user
3. Validasi input login

Author: Proyek Akhir - Teknik Informatika
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Menambahkan parent directory ke path untuk import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auth.security import validate_username, validate_password, verify_password
from database.db import db_manager


class LoginWindow:
    """
    Class untuk mengelola window login dan proses autentikasi.
    """
    
    def __init__(self, root, on_login_success):
        """
        Inisialisasi LoginWindow.
        
        Args:
            root: Tkinter root window
            on_login_success: Callback function yang dipanggil saat login berhasil
        """
        self.root = root
        self.on_login_success = on_login_success
        self.root.title("Login - Sistem Manajemen Inventaris")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Center window
        self._center_window()
        
        self._create_widgets()
    
    def _center_window(self):
        """
        Menempatkan window di tengah layar.
        """
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def _create_widgets(self):
        """
        Membuat dan menempatkan widget GUI.
        """
        # Frame utama
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="SISTEM MANAJEMEN INVENTARIS",
            font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=(0, 20))
        
        # Username
        username_frame = tk.Frame(main_frame)
        username_frame.pack(fill='x', pady=5)
        
        tk.Label(username_frame, text="Username:", width=12, anchor='w').pack(side='left')
        self.entry_username = tk.Entry(username_frame, width=25)
        self.entry_username.pack(side='left', padx=5)
        
        # Password
        password_frame = tk.Frame(main_frame)
        password_frame.pack(fill='x', pady=5)
        
        tk.Label(password_frame, text="Password:", width=12, anchor='w').pack(side='left')
        self.entry_password = tk.Entry(password_frame, width=25, show='*')
        self.entry_password.pack(side='left', padx=5)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Login button
        btn_login = tk.Button(
            button_frame,
            text="Login",
            width=12,
            command=self._handle_login,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 10, 'bold')
        )
        btn_login.pack(side='left', padx=5)
        
        # Register button
        btn_register = tk.Button(
            button_frame,
            text="Register",
            width=12,
            command=self._handle_register,
            bg='#2196F3',
            fg='white',
            font=('Arial', 10, 'bold')
        )
        btn_register.pack(side='left', padx=5)
        
        # Info label
        info_label = tk.Label(
            main_frame,
            text="Ketentuan Password:\n• Minimal 8 karakter\n• Mengandung huruf besar, kecil, dan angka",
            font=('Arial', 8),
            fg='gray',
            justify='left'
        )
        info_label.pack(pady=(10, 0))
        
        # Bind Enter key
        self.entry_username.bind('<Return>', lambda e: self._handle_login())
        self.entry_password.bind('<Return>', lambda e: self._handle_login())
    
    def _handle_login(self):
        """
        Menangani proses login.
        """
        username = self.entry_username.get().strip()
        password = self.entry_password.get()
        
        # Validasi input kosong
        if not username or not password:
            messagebox.showerror("Error", "Username dan password harus diisi")
            return
        
        # Validasi format username
        valid_user, msg_user = validate_username(username)
        if not valid_user:
            messagebox.showerror("Error", msg_user)
            return
        
        # Query database untuk mendapatkan password hash
        query = "SELECT password_hash FROM users WHERE username = ?"
        results = db_manager.execute_query(query, (username,))
        
        if not results:
            messagebox.showerror("Error", "Username tidak ditemukan")
            return
        
        stored_hash = results[0][0]
        
        # Verifikasi password
        if verify_password(password, stored_hash):
            messagebox.showinfo("Sukses", f"Login berhasil!\nSelamat datang, {username}")
            self.root.destroy()
            self.on_login_success(username)
        else:
            messagebox.showerror("Error", "Password salah")
    
    def _handle_register(self):
        """
        Menangani proses registrasi user baru.
        """
        username = self.entry_username.get().strip()
        password = self.entry_password.get()
        
        # Validasi username
        valid_user, msg_user = validate_username(username)
        if not valid_user:
            messagebox.showerror("Error", msg_user)
            return
        
        # Validasi password
        valid_pass, msg_pass = validate_password(password)
        if not valid_pass:
            messagebox.showerror("Error", msg_pass)
            return
        
        # Cek apakah username sudah ada
        query = "SELECT id FROM users WHERE username = ?"
        results = db_manager.execute_query(query, (username,))
        
        if results:
            messagebox.showerror("Error", "Username sudah terdaftar")
            return
        
        # Hash password dan simpan ke database
        from auth.security import hash_password
        password_hash = hash_password(password)
        
        insert_query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        try:
            db_manager.execute_update(insert_query, (username, password_hash))
            messagebox.showinfo("Sukses", "Registrasi berhasil!\nSilakan login")
            self.entry_password.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Registrasi gagal: {str(e)}")
