class Pasien:
    def __init__(self, nama, tanggal_masuk, kondisi_kesehatan):
        self.__nama = nama
        self.__tanggal_masuk = tanggal_masuk
        self.__kondisi_kesehatan = kondisi_kesehatan

    def get_nama(self):
        return self.__nama

    def get_tanggal_masuk(self):
        return self.__tanggal_masuk

    def get_kondisi_kesehatan(self):
        return self.__kondisi_kesehatan

    def display_info(self):
        print(f"Nama Pasien: {self.__nama}")
        print(f"Tanggal Masuk: {self.__tanggal_masuk}")
        print(f"Kondisi Kesehatan: {self.__kondisi_kesehatan}")


class Dokter(Pasien):
    def __init__(self, nama, tanggal_masuk, spesialisasi, jumlah_pasien_tertangani):
        super().__init__(nama, tanggal_masuk, "Sehat")
        self.__spesialisasi = spesialisasi
        self.__jumlah_pasien_tertangani = jumlah_pasien_tertangani

    def get_spesialisasi(self):
        return self.__spesialisasi

    def get_jumlah_pasien_tertangani(self):
        return self.__jumlah_pasien_tertangani

    def display_info(self):
        super().display_info()
        print(f"Spesialisasi: {self.__spesialisasi}")
        print(f"Jumlah Pasien Tertangani: {self.__jumlah_pasien_tertangani}")


class Perawat(Pasien):
    def __init__(self, nama, tanggal_masuk, spesialisasi, jumlah_pasien_tertangani):
        super().__init__(nama, tanggal_masuk, "Sehat")
        self.__spesialisasi = spesialisasi
        self.__jumlah_pasien_tertangani = jumlah_pasien_tertangani

    def get_spesialisasi(self):
        return self.__spesialisasi

    def get_jumlah_pasien_tertangani(self):
        return self.__jumlah_pasien_tertangani

    def display_info(self):
        super().display_info()
        print(f"Spesialisasi Perawat: {self.__spesialisasi}")
        print(f"Jumlah Pasien Tertangani: {self.__jumlah_pasien_tertangani}")


class AlatMedis(Dokter):
    def __init__(self, nama, tanggal_masuk, jenis, produsen):
        super().__init__(nama, tanggal_masuk, "Berfungsi", 0) 
        self.__jenis = jenis
        self.__produsen = produsen

    def get_jenis(self):
        return self.__jenis

    def get_produsen(self):
        return self.__produsen

    def display_info(self):
        super().display_info()
        print(f"Jenis Alat Medis: {self.__jenis}")
        print(f"Produsen: {self.__produsen}")


def main():
    while True:
        print("\n=== Informasi Kesehatan di Rumah Sakit ===")
        print("1. Informasi Pasien")
        print("2. Informasi Dokter")
        print("3. Informasi Perawat")
        print("4. Informasi Alat Medis")
        print("5. Keluar")

        pilihan = input("Masukkan nomor pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan nama Pasien: ")
            tanggal_masuk = int(input("Masukkan tahun masuk: "))
            kondisi_kesehatan = input("Masukkan kondisi kesehatan Pasien: ")

            pasien = Pasien(nama, tanggal_masuk, kondisi_kesehatan)
            pasien.display_info()

        elif pilihan == "2":
            nama = input("Masukkan nama Dokter: ")
            tanggal_masuk = int(input("Masukkan tahun masuk: "))
            spesialisasi = input("Masukkan spesialisasi Dokter: ")
            jumlah_pasien_tertangani = int(input("Masukkan jumlah pasien yang telah ditangani: "))

            dokter = Dokter(nama, tanggal_masuk, spesialisasi, jumlah_pasien_tertangani)
            dokter.display_info()

        elif pilihan == "3":
            nama = input("Masukkan nama Perawat: ")
            tanggal_masuk = int(input("Masukkan tahun masuk Perawat Tersebut: "))
            spesialisasi = input("Masukkan spesialisasi Perawat: ")
            jumlah_pasien_tertangani = int(input("Masukkan jumlah pasien yang sudah ditangani: "))

            perawat = Perawat(nama, tanggal_masuk, spesialisasi, jumlah_pasien_tertangani)
            perawat.display_info()

        elif pilihan == "4":
            nama = input("Masukkan nama Alat Medis: ")
            tanggal_masuk = int(input("Masukkan tahun masuk: "))
            jenis = input("Masukkan jenis Alat Medis yang dibutuhkan: ")
            produsen = input("Masukkan produsen Alat Medis yang Menginginkan: ")

            alat_medis = AlatMedis(nama, tanggal_masuk, jenis, produsen)
            alat_medis.display_info()

        elif pilihan == "5":
            print("Terima kasih! Keluar dari aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")


if __name__ == "__main__":
    main()
