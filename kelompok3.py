class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

    def display_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, gerbong, jumlah_kursi, jenis_layanan_kereta, rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.gerbong = gerbong
        self.jumlah_kursi = jumlah_kursi
        self.jenis_layanan_kereta = jenis_layanan_kereta
        self.rute = rute

    def tambah_rute(self, tambah_rute):
        self.rute.append(tambah_rute)

    def kurangi_rute(self, hapus_rute):
        if hapus_rute in self.rute:
            self.rute.remove(hapus_rute)


class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil
        self._Mobil__kondisi_mesin = False  # Name mangling

    def start_engine(self):
        if not self._Mobil__kondisi_mesin:
            self._Mobil__kondisi_mesin = True
            print(f"{self.nama} mesin mobil menyala")
        else:
            print(f"{self.nama} mesin mobil sudah menyala")

    def stop_engine(self):
        if self._Mobil__kondisi_mesin:
            self._Mobil__kondisi_mesin = False
            print(f"{self.nama} mesin mobil mati")
        else:
            print(f"{self.nama} mesin mobil sudah mati")

    def maju(self):
        if self._Mobil__kondisi_mesin:
            print(f"{self.nama} mobil maju")
        else:
            print(f"{self.nama} hidupkan mobil terlebih dahulu")

    def mundur(self):
        if self._Mobil__kondisi_mesin:
            print(f"{self.nama} mobil mundur")
        else:
            print(f"{self.nama} hidupkan mobil terlebih dahulu")

    def belok(self):
        if self._Mobil__kondisi_mesin:
            print(f"{self.nama} mobil belok")
        else:
            print(f"{self.nama} hidupkan mobil terlebih dahulu")

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.front_wing = front_wing
        self.rear_wing = rear_wing

    def race(self):
        print(f"{self.nama} Mobil dalam mode balap")


class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.sunroof_type = sunroof_type
        self.shock_breaker = shock_breaker

    def sunroof_terbuka(self):
        print(f"{self.nama} Sunroof Terbuka")

    def sunroof_tertutup(self):
        print(f"{self.nama} Sunroof Tertutup")

# print class KendaraanDarat
kendar = KendaraanDarat(2023, "vario mber", "Hitam banget", 120, "Pertalite", 2, 3)
print("====class KendaraanDarat====")
kendar.display_attributes()
print()

# print class Kereta
kereta = Kereta(2023, "kereta Malam", "Biru", 150, "Listrik", 20, 100, 10, 100, "Ekonomi Miskin", ["Jogja", "Solo"])
kereta.tambah_rute("Rumah danis")
print("====class Kereta====")
kereta.display_attributes()
print()

# print class Mobil
mobil = Mobil(2022, "Rubicon", "Hitam", 180, "Bensin", 4, 5, "Jeep")
print("====class Mobil====")
mobil.display_attributes()
mobil.start_engine()
mobil.maju()
print()

# print class MobilBalap
mobil_balap = MobilBalap(2022, "Ferrari", "Merah", 300, "Bensin", 4, 2, "Sport", "High", "Low")
print("====class Mobilbalap====")
mobil_balap.display_attributes()
mobil_balap.race()
print()

# print class MobilCrossroad
mobil_crossroad = MobilCrossroad(2022, "Hummer", "Hijau", 120, "Bensin", 4, 4, "Armored SUV", "Panoramic", "Offroad")
print("====class MobilCrossroad====")
mobil_crossroad.display_attributes()
mobil_crossroad.sunroof_terbuka()