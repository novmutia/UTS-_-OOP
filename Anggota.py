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
            
