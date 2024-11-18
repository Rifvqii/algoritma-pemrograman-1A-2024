
daftarpinjam = []

def creatpeminjaman():
    print("=== Tambah Peminjaman Buku ===")
    id_pinjam = input("Masukkan ID Peminjaman: ")
    nama = input("Masukkan Nama Peminjam: ")
    judul = input("Masukkan Judul Buku: ")
    tanggal = input("Masukkan Tanggal Peminjaman: ")
    
    peminjaman = (id_pinjam, nama, judul, tanggal)
    daftarpinjam.append(peminjaman)
    print("Peminjaman berhasil ditambahkan!")

def tampilkan_peminjaman():
    print("=== Daftar Peminjaman Buku ===")
    if not daftarpinjam:
        print("Belum ada data peminjaman.")
        return

    for pinjam in daftarpinjam :
        print(f"ID Peminjaman: {pinjam[0]}")
        print(f"nama Peminjam: {pinjam[1]}")
        print(f"nudul Buku: {pinjam[2]}")
        print(f"tanggal Peminjaman: {pinjam[3]}")
  
def updatepeminjaman():
    print("=== Update Data Peminjaman ===")
    if not daftarpinjam:
        print("Belum ada data peminjaman")
        return
    
    id_pinjam = input("Masukkan ID Peminjaman yang akan diupdate: ")
    indeks = -1
    for i in range(len(daftarpinjam)):
        if daftarpinjam[i][0] == id_pinjam:
            indeks = i
            break
    if indeks == -1:
        print("ID Peminjaman tidak ditemukan!")
        return
    
    #data baru
    print("masukkan data baru:")
    nama = input("masukkan Nama Peminjam: ")
    judul = input("asukkan judul Buku: ")
    tanggal = input("asukkan tanggal peminjaman: ")
    
    peminjaman_baru = (id_pinjam, nama, judul, tanggal)
    daftarpinjam[indeks] = peminjaman_baru
    print("Data peminjaman berhasil diupdate!")

def hapus_peminjaman(daftarpinjam):
    print("=== HAPUS DATA PINJAM ===")
    if not daftarpinjam:
        print("belum ada data peminjaman")
        return
    
    id_pinjam = input("masukkan ID Peminjaman yang akan dihapus: ")


                
    while True :
        for i in range(len(daftarpinjam)):
            if daftarpinjam[i][0] == id_pinjam:
                del daftarpinjam[i]
                print("data peminjaman berhasil dihapus!")
                return
    

def menu():
    print("=== MENU ===")
    print("a. Tambah Peminjaman")
    print("b. Lihat Daftar Peminjaman") 
    print("c. Update Peminjaman")
    print("d. Hapus Peminjaman")
    print("e. Keluar")
    
    pilihan = input("Masukkan pilihan (a/b/c/d/e): ")
    return pilihan

while True:
    pilihan = menu()
    
    if pilihan == "a":
        creatpeminjaman()
    elif pilihan == "b":
        tampilkan_peminjaman()
    elif pilihan == "c":
        updatepeminjaman()
    elif pilihan == "d":
        hapus_peminjaman(daftarpinjam)
    elif pilihan == "e":
        print("terima kasih !")
        break
    else:
        print("tidak valid!")
