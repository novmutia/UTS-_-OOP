class BukuNovel(Buku):
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku, buku_nv):
        super().__init__(judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku)
        self.__buku_nv = buku_nv
        
    def get_kode_buku_nv(self):
        return self.__buku_nv
        
    def menampilkan_informasi_buku(self):
        super().menampilkan_informasi_buku()
        print(f"Buku Novel: {self.__buku_nv}")
