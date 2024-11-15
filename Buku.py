class Buku:
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku):
        self.__judul_buku = judul_buku
        self.__pengarang_buku = pengarang_buku
        self.__tahun_terbit = tahun_terbit
        self.__ISBN = ISBN
        self.__Status_buku = Status_buku
        
    def menampilkan_informasi_buku(self):
        print(f"Judul Buku: {self.__judul_buku}\nPengarang Buku: {self.__pengarang_buku}\nTahun Terbit: {self.__tahun_terbit}\nISBN: {self.__ISBN}\nStatus Buku: {self.__Status_buku}")
        
    def get_judul_buku(self):
        return self.__judul_buku
    
    def get_ISBN(self):
        return self.__ISBN
    
    def get_status_buku(self):
        return self.__Status_buku
    
    def set_status_buku(self, status_buku):
        self.__Status_buku = status_buku
