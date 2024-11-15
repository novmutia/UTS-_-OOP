def menu(perpustakaan):
    print("----------------------------------------------------------------------")
    print("-----------------SELAMAT DATANG DI PERPUSTAKAAN ILMU------------------")
    print("----------------------------------------------------------------------")
    print("\n")
        
    while True:
        print("Menu Perpustakaan Ilmu:")
        print("1. Informasi Buku Perpustakaan Ilmu")
        print("2. Menambahkan Buku")
        print("3. Menambahkan Anggota")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Daftar Buku Tersedia")
        print("7. Informasi Anggota Perpustakaan Ilmu")
        print("8. Keluar")
        
        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            perpustakaan.menampilkan_daftar_buku()
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "2":
            print("Masukkan informasi buku:")
            print("Pilih jenis buku:")
            print("1. Buku Pengetahuan Umum")
            print("2. Buku Novel")
            jenis_buku = input("Pilih (1/2): ")
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            tahun = input("Masukkan tahun terbit: ")
            ISBN = input("Masukkan ISBN: ")
            if jenis_buku == "1":
                kode_buku_pu = input("Masukkan Kode buku Pengetahuan Umum: ")
                buku = BukuPengetahuanUmum(judul, pengarang, tahun, ISBN, "tersedia", kode_buku_pu)
            elif jenis_buku == "2":
                kode_buku_nv = input("Masukkan Kode buku Novel: ")
                buku = BukuNovel(judul, pengarang, tahun, ISBN, "tersedia", kode_buku_nv)
                
            perpustakaan.menambahkan_buku(buku)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "3":
            nama = input("Masukkan nama anggota: ")
            nomor = input("Masukkan nomor anggota: ")
            alamat = input("Masukkan alamat anggota: ")
            perpustakaan.menambahkan_anggota_baru(nama, nomor, alamat)
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "4":
            nomor_anggota = input("Masukkan nomor anggota: ")
            ISBN = input("Masukkan ISBN buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(nomor_anggota, ISBN)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "5":
            nomor_anggota = input("Masukkan nomor anggota: ")
            ISBN = input("Masukkan ISBN buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(nomor_anggota, ISBN)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "6":
            perpustakaan.menampilkan_daftar_buku()
            print("\n" + "-" * 30 + "\n")
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "7":
            perpustakaan.menampilkan_informasi_anggota()
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "8":
            print("--Terima kasih telah berkunjung di perpustakaan ilmu--")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

if __name__ == "__main__":
    perpustakaan = Perpustakaan()            
    menu(perpustakaan)

            
