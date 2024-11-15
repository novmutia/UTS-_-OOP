
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
        
        print("Daftar Buku yang Dipinjam:")
        if anggota._Anggota__daftar_pinjaman: 
            for buku in anggota._Anggota__daftar_pinjaman:
                print(f"- {buku.get_judul_buku()} (ISBN: {buku.get_ISBN()})")
        else:
            print("- Tidak ada buku yang dipinjam.")
        
        print("\n" + "-" * 30 + "\n")