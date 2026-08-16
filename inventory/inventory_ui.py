"""
Inventory UI Module
Modul ini bertanggung jawab untuk:
1. Menampilkan GUI manajemen inventaris
2. Menangani interaksi user dengan sistem inventaris
3. Menampilkan data dalam bentuk tabel

Author: Proyek Akhir - Teknik Informatika
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Menambahkan parent directory ke path untuk import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inventory.inventory_controller import InventoryController
from utils.helpers import format_currency, clear_entries, confirm_action


class InventoryWindow:
    """
    Class untuk mengelola window inventaris dan operasi CRUD.
    """
    
    def __init__(self, root, username):
        """
        Inisialisasi InventoryWindow.
        
        Args:
            root: Tkinter root window
            username (str): Username user yang login
        """
        self.root = root
        self.username = username
        self.controller = InventoryController()
        self.selected_item_id = None
        
        self.root.title(f"Manajemen Inventaris - {username}")
        self.root.geometry("900x600")
        
        # Center window
        self._center_window()
        
        self._create_widgets()
        self._load_data()
    
    def _center_window(self):
        """
        Menempatkan window di tengah layar.
        """
        self.root.update_idletasks()
        width = 900
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def _create_widgets(self):
        """
        Membuat dan menempatkan widget GUI.
        """
        # Header frame
        header_frame = tk.Frame(self.root, bg='#2196F3', height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="SISTEM MANAJEMEN INVENTARIS",
            font=('Arial', 16, 'bold'),
            bg='#2196F3',
            fg='white'
        )
        title_label.pack(side='left', padx=20, pady=15)
        
        user_label = tk.Label(
            header_frame,
            text=f"User: {self.username}",
            font=('Arial', 10),
            bg='#2196F3',
            fg='white'
        )
        user_label.pack(side='right', padx=20)
        
        # Main container
        main_container = tk.Frame(self.root, padx=20, pady=20)
        main_container.pack(fill='both', expand=True)
        
        # Input frame
        input_frame = tk.LabelFrame(main_container, text="Input Data Item", padx=10, pady=10)
        input_frame.pack(fill='x', pady=(0, 10))
        
        # Nama
        tk.Label(input_frame, text="Nama Item:", width=12, anchor='w').grid(row=0, column=0, padx=5, pady=5)
        self.entry_nama = tk.Entry(input_frame, width=40)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=5)
        
        # Jumlah
        tk.Label(input_frame, text="Jumlah:", width=12, anchor='w').grid(row=1, column=0, padx=5, pady=5)
        self.entry_jumlah = tk.Entry(input_frame, width=20)
        self.entry_jumlah.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        # Harga
        tk.Label(input_frame, text="Harga (Rp):", width=12, anchor='w').grid(row=2, column=0, padx=5, pady=5)
        self.entry_harga = tk.Entry(input_frame, width=20)
        self.entry_harga.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        # Button frame
        button_frame = tk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Buttons
        tk.Button(
            button_frame, text="Tambah", width=12, command=self._create_item,
            bg='#4CAF50', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame, text="Update", width=12, command=self._update_item,
            bg='#FF9800', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame, text="Hapus", width=12, command=self._delete_item,
            bg='#F44336', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame, text="Clear", width=12, command=self._clear_form,
            bg='#9E9E9E', fg='white', font=('Arial', 9, 'bold')
        ).pack(side='left', padx=5)
        
        # Table frame
        table_frame = tk.LabelFrame(main_container, text="Data Inventaris", padx=10, pady=10)
        table_frame.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=('ID', 'Nama', 'Jumlah', 'Harga', 'Total'),
            show='headings',
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=self.tree.yview)
        
        # Define columns
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nama', text='Nama Item')
        self.tree.heading('Jumlah', text='Jumlah')
        self.tree.heading('Harga', text='Harga')
        self.tree.heading('Total', text='Total Nilai')
        
        self.tree.column('ID', width=50, anchor='center')
        self.tree.column('Nama', width=300, anchor='w')
        self.tree.column('Jumlah', width=100, anchor='center')
        self.tree.column('Harga', width=150, anchor='e')
        self.tree.column('Total', width=150, anchor='e')
        
        self.tree.pack(fill='both', expand=True)
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self._on_item_select)
        
        # Statistics frame
        stats_frame = tk.Frame(main_container, bg='#E3F2FD', padx=10, pady=10)
        stats_frame.pack(fill='x', pady=(10, 0))
        
        self.label_stats = tk.Label(
            stats_frame,
            text="Total Item: 0 | Total Nilai: Rp 0",
            font=('Arial', 10, 'bold'),
            bg='#E3F2FD'
        )
        self.label_stats.pack()
    
    def _load_data(self):
        """
        Memuat data dari database dan menampilkan di treeview.
        """
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load data from database
        items = self.controller.get_all_items()
        
        for item in items:
            item_id, nama, jumlah, harga = item
            total = jumlah * harga
            
            self.tree.insert('', 'end', values=(
                item_id,
                nama,
                jumlah,
                format_currency(harga),
                format_currency(total)
            ))
        
        # Update statistics
        self._update_statistics()
    
    def _update_statistics(self):
        """
        Mengupdate statistik total item dan nilai.
        """
        total_items = self.controller.get_total_items()
        total_value = self.controller.get_total_value()
        
        self.label_stats.config(
            text=f"Total Item: {total_items} | Total Nilai: {format_currency(total_value)}"
        )
    
    def _on_item_select(self, event):
        """
        Event handler ketika item di treeview dipilih.
        """
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            self.selected_item_id = values[0]
            
            # Populate form
            self.entry_nama.delete(0, tk.END)
            self.entry_nama.insert(0, values[1])
            
            self.entry_jumlah.delete(0, tk.END)
            self.entry_jumlah.insert(0, values[2])
            
            # Remove currency formatting from harga
            harga_str = str(values[3]).replace('Rp ', '').replace('.', '')
            self.entry_harga.delete(0, tk.END)
            self.entry_harga.insert(0, harga_str)
    
    def _create_item(self):
        """
        Menambah item baru ke inventaris.
        """
        nama = self.entry_nama.get()
        jumlah = self.entry_jumlah.get()
        harga = self.entry_harga.get()
        
        success, message = self.controller.create_item(nama, jumlah, harga)
        
        if success:
            messagebox.showinfo("Sukses", message)
            self._clear_form()
            self._load_data()
        else:
            messagebox.showerror("Error", message)
    
    def _update_item(self):
        """
        Mengupdate item yang sudah ada.
        """
        if not self.selected_item_id:
            messagebox.showwarning("Peringatan", "Pilih item yang akan diupdate")
            return
        
        nama = self.entry_nama.get()
        jumlah = self.entry_jumlah.get()
        harga = self.entry_harga.get()
        
        success, message = self.controller.update_item(
            self.selected_item_id, nama, jumlah, harga
        )
        
        if success:
            messagebox.showinfo("Sukses", message)
            self._clear_form()
            self._load_data()
        else:
            messagebox.showerror("Error", message)
    
    def _delete_item(self):
        """
        Menghapus item dari inventaris.
        """
        if not self.selected_item_id:
            messagebox.showwarning("Peringatan", "Pilih item yang akan dihapus")
            return
        
        if not confirm_action("Konfirmasi", "Apakah Anda yakin ingin menghapus item ini?"):
            return
        
        success, message = self.controller.delete_item(self.selected_item_id)
        
        if success:
            messagebox.showinfo("Sukses", message)
            self._clear_form()
            self._load_data()
        else:
            messagebox.showerror("Error", message)
    
    def _clear_form(self):
        """
        Membersihkan form input.
        """
        clear_entries(self.entry_nama, self.entry_jumlah, self.entry_harga)
        self.selected_item_id = None
