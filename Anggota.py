class Anggota:
    def __init__(self, nama_anggota_perpustakaan, nomor_anggota_perpustakaan, alamat):  
        self.__nama_anggota = nama_anggota_perpustakaan
        self.__nomor_anggota = nomor_anggota_perpustakaan
        self.__alamat = alamat
        self.__daftar_pinjaman = []
        
    def get_nama_anggota(self):
        return self.__nama_anggota
    
    def get_nomor_anggota(self):
        return self.__nomor_anggota
    
    def menampilkan_informasi_anggota(self):
        print(f"Nama Anggota: {self.__nama_anggota}\nNomor Anggota: {self.__nomor_anggota}\nAlamat: {self.__alamat}")
        
    def pinjam_buku(self, buku):
        if buku.get_status_buku() == "tersedia":
            self.__daftar_pinjaman.append(buku)
            buku.set_status_buku("dipinjam")
            print(f"Buku '{buku.get_judul_buku()}' berhasil dipinjam.")
        else:
            print(f"Mohon maaf, Buku '{buku.get_judul_buku()}' tidak tersedia.")
    
    def kembalikan_buku(self, buku):
        if buku in self.__daftar_pinjaman:
            self.__daftar_pinjaman.remove(buku)
            buku.set_status_buku("tersedia")
            print(f"Buku '{buku.get_judul_buku()}' berhasil dikembalikan.")
        else:
            print(f"Buku '{buku.get_judul_buku()}' tidak ada dalam daftar pinjaman.")


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []
        
    def menambahkan_buku(self, buku):
        self.__daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul_buku()}' berhasil ditambahkan.")
        
    def menambahkan_anggota_baru(self, nama_anggota, nomor_anggota, alamat):
        anggota_baru = Anggota(nama_anggota, nomor_anggota, alamat)
        self.__daftar_anggota.append(anggota_baru)
        print(f"Anggota '{anggota_baru.get_nama_anggota()}' berhasil ditambahkan.")
            
    def pinjam_buku(self, nomor_anggota, ISBN):
        anggota = next((anggota for anggota in self.__daftar_anggota if anggota.get_nomor_anggota() == nomor_anggota), None)
        buku = next((buku for buku in self.__daftar_buku if buku.get_ISBN() == ISBN), None)
        
        if anggota and buku:
            anggota.pinjam_buku(buku)
        else:
            print("Buku atau anggota tidak valid!")
    
    def kembalikan_buku(self, nomor_anggota, ISBN):
        anggota = next((anggota for anggota in self.__daftar_anggota if anggota.get_nomor_anggota() == nomor_anggota), None)
        buku = next((buku for buku in self.__daftar_buku if buku.get_ISBN() == ISBN), None)
        
        if anggota and buku:
            anggota.kembalikan_buku(buku)
        else:
            print("Buku atau anggota tidak valid!")

    def menampilkan_daftar_buku(self):
        print("Daftar Buku Tersedia di Perpustakaan Ilmu:")
        for buku in self.__daftar_buku:
            if buku.get_status_buku() == "tersedia":
                buku.menampilkan_informasi_buku()
                print("\n" + "-" * 30 + "\n")
    
    def menampilkan_informasi_anggota(self):
        for anggota in self.__daftar_anggota:
            anggota.menampilkan_informasi_anggota()
            print("\n" + "-" * 30 + "\n")
