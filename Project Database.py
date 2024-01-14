import mysql.connector

class Barang:
    def __init__(self, id_barang, nama_barang, Harga_barang, stok):
        self.id_barang = id_barang
        self.nama = nama_barang
        self.harga = Harga_barang
        self.jumlah_stok = stok

    def display_info(self):
        print("+="*20)
        print(f"ID Barang: {self.id_barang}")
        print(f"nama: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Jumlah Stok: {self.jumlah_stok}")
        print("+="*20)

class Penjualan:
    def __init__(self, id_transaksi,id_barang,nama_barang, jumlah_barang, total_harga):
        self.id_transaksi = id_transaksi
        self.id_barang = id_barang
        self.nama = nama_barang
        self.jumlah_barang = jumlah_barang
        self.total_harga = total_harga

    def display_info(self):
        print(f"ID Transaksi    : {self.id_transaksi}")
        print(f"id_barang       : {self.id_barang}")
        print(f"nama barang     : {self.nama}")
        print(f"jumlah barang   : {self.jumlah_barang}")
        print(f"total harga     : {self.total_harga}")
        print("")


class Toko:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="5220411253"
        )
        self.cursor = self.connection.cursor()

        self.daftar_barang = []
        self.daftar_penjualan = []

        # Mengambil data Barang dan Penjualan dari database saat inisialisasi
        self.ambil_data_barang_dari_database()
        query = "SELECT * from penjualan"
        self.cursor.execute(query)

        for penjualan in self.cursor.fetchall():
            self.daftar_penjualan.append(Penjualan(penjualan[0], penjualan[1], penjualan[2],penjualan[3], penjualan[4]))

    def tambah_barang(self, barang):
        # ...
        try:
            # Menambahkan data ke database
            query = "INSERT INTO barang (id_barang, nama, harga, jumlah_stok) VALUES (%s, %s, %s, %s)"
            values = (barang.id_barang, barang.nama, barang.harga, barang.jumlah_stok)
            self.cursor.execute(query, values)
            self.connection.commit()

            self.ambil_data_barang_dari_database()
            print(f"Barang {barang.nama} berhasil ditambahkan ke Toko.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def ambil_data_barang_dari_database(self):
        try:
            # Mengambil data barang dari database
            query = "SELECT * FROM barang"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for row in result:
                barang = Barang(*row)
                self.daftar_barang.append(barang)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    #update data Barang
    def update_stok_barang(self, id_barang, jumlah):
        for barang in self.daftar_barang:
            if barang.id_barang == id_barang:
                barang.jumlah_stok += jumlah
                # Menyimpan perubahan stok ke database
                self.simpan_perubahan_stok_ke_database(id_barang, barang.jumlah_stok)
                print(f"Stok barang {barang.nama} berhasil diperbarui.")
                return
        print("barang tidak ditemukan.")
    
    def simpan_perubahan_stok_ke_database(self, id_barang, stok_baru):
        try:
            # Mengupdate stok barang di database
            query = "UPDATE barang SET jumlah_stok = %s WHERE id_barang = %s"
            values = (stok_baru, id_barang)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def jual_barang(self, id_barang, nama, jumlah):
        for barang in self.daftar_barang:
            if barang.id_barang == id_barang and barang.jumlah_stok > 0:
                if jumlah <= barang.jumlah_stok:
                    barang.jumlah_stok -= jumlah
                    total_harga = int(barang.harga)*jumlah# Hitung total harga berdasarkan harga per barang dan jumlah
                    id_transaksi = len(self.daftar_penjualan) + 1
                    penjualan = Penjualan(id_transaksi, id_barang, nama, jumlah, total_harga)
                    self.daftar_penjualan.append(penjualan)

                    # Menyimpan informasi Penjualan ke database
                    self.simpan_penjualan_ke_database(penjualan)

                    # Menyimpan perubahan stok Barang ke database
                    self.simpan_perubahan_stok_ke_database(id_barang, barang.jumlah_stok)

                    print(f"Barang {barang.nama} berhasil dibeli. Total Harga: {total_harga}")
                    return
                else:
                    print("Jumlah barang yang diminta melebihi stok yang tersedia.")
                    return
        print("="*20, "Barang tidak tersedia atau stok habis.", "="*20)
    


    def simpan_penjualan_ke_database(self, penjualan):
        try:
            # Menambahkan data Penjualan ke database
            query = "INSERT INTO penjualan (id_transaksi, id_barang, nama, jumlah_barang, total_harga) VALUES (%s, %s, %s, %s, %s)"
            values = (penjualan.id_transaksi, penjualan.id_barang, penjualan.nama, penjualan.jumlah_barang, penjualan.total_harga)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def simpan_perubahan_stok_ke_database(self, id_barang, stok_baru):
        try:
            # Mengupdate stok Barang di database
            query = "UPDATE barang SET jumlah_stok = %s WHERE id_barang = %s"
            values = (stok_baru, id_barang)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    def hapus_penjualan_dari_database(self, id_transaksi):
        try:
            # Menghapus data Penjualan dari database
            query = "DELETE FROM penjualan WHERE id_transaksi = %s"
            values = (id_transaksi,)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def tampilkan_menu():
    print("==== Menu Toko ====")
    print("1. Tambah Barang")
    print("2. penjualan Barang")
    print("3. Tampilkan Informasi Barang")
    print("4. Tampilkan Informasi Penjualan")
    print("5. Update stok Barang")
    print("0. Keluar")

# Contoh penggunaan program dengan perulangan
Toko = Toko()

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (0-6): ")

    if pilihan == "0":
        print("Terima kasih, keluar dari program.")
        break
    elif pilihan == "1":
        id_barang = int(input("Masukkan ID Barang   : "))
        nama = input("Masukkan nama Barang  : ")
        harga = input("Masukkan harga  : ")
        jumlah_stok = int(input("Masukkan Jumlah Stok   : "))
        barang = Barang(id_barang, nama, harga, jumlah_stok)
        Toko.tambah_barang(barang) 
    elif pilihan == "2":
        id_barang = int(input("Masukkan ID Barang yang akan dijual    : "))
        nama = input("Masukkan Nama barang  : ")
        jumlah = int(input("Masukkan jumlah barang  : "))  # Perbaikan: Ubah input menjadi integer
        Toko.jual_barang(id_barang, nama, jumlah)
    elif pilihan == "3":
        for barang in Toko.daftar_barang:
            barang.display_info()
    elif pilihan == "4":
        for penjualan in Toko.daftar_penjualan:
            penjualan.display_info()
    elif pilihan == "5":
        id_barang = int(input("Masukkan ID Barang yang akan diupdate    : "))
        jumlah = int(input("tambahkan Stok Barang   : "))
        Toko.update_stok_barang(id_barang,jumlah)
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")