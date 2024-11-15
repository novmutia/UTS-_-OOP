class BukuPengetahuanUmum(Buku):
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku, buku_pu):
        super().__init__(judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku)
        self.__buku_pu = buku_pu
        
    def get_kode_buku_pu(self):
        return self.__buku_pu
        
    def menampilkan_informasi_buku(self):
        super().menampilkan_informasi_buku()
        print(f"Kode Buku Pengetahuan Umum: {self.__buku_pu}")