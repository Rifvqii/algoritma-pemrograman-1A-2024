

data = []
def tambahkaryawan(nip, nama, alamat, departemen, jabatan):
    karyawan = (nip, nama, alamat, departemen, jabatan)
    data.append(karyawan)
    print("Data karyawan berhasil ditambahkan.")

def semuakaryawan():
    for i in range(5):
        print("karyawan ke :",i+1)
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
        tambahkaryawan(nip, nama, alamat, departemen, jabatan)

def tampilkaryawan():
    if not data:
        print("Belum ada data karyawan.")
    else:
        print("Daftar Karyawan:")
        for karyawan in data:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan(cari, dalam):
    hasil_cari = []

    if cari == "nip":
        no = 0
    elif cari == "nama":
        no = 1
    elif cari == "alamat":
        no = 2
    elif cari == "departemen":
        no = 3
    elif cari == "jabatan":
        no = 4
    else :
        print ("data tidak valid")

    for karyawan in data:
        if karyawan[no] == dalam:
            hasil_cari.append(karyawan)

    return hasil_cari

def m():
    while True:
        print("=== Menu ===")
        print("a. tambah Data Karyawan")
        print("b. tambah 5 Karyawan Sekaligus")
        print("c. tampilkan Semua Karyawan")
        print("d. cari Karyawan Berdasarkan Atribut")
        print("e. keluar")
        
        pilihan = input("Pilih menu (a/b/c/d/e): ")
        if pilihan == "a":
            nip = input("NIP: ")
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            departemen = input("Departemen: ")
            jabatan = input("Jabatan: ")
            tambahkaryawan(nip, nama, alamat, departemen, jabatan)
        
        elif pilihan == "b":
            semuakaryawan()
        
        elif pilihan == "c":
            tampilkaryawan()
        
        elif pilihan == "d":
            print("Pencarian Data Karyawan")
            print("atribut pencarian: nip, nama, alamat, departemen, jabatan")
            cari = input("masukkan atribut yang dicari: ")
            dalam = input("masukkan data krywn untuk pencarian: ")
            
            hasil = cari_karyawan(cari, dalam)
            if hasil:
                print("Hasil Pencarian:")
                for karyawan in hasil:
                    print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
            else:
                print("data tidak valis")
        
        elif pilihan == "e":
            print("makasi")
            break

m()


