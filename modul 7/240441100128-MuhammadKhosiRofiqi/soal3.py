
kelas = []  
max_siswa = 3 

def tambah_siswa(nama, asal_sekolah):
    for k in kelas:
        if len(k) < max_siswa:
            k.append({'nama': nama, 'asal_sekolah': asal_sekolah})
            print(f"Siswa {nama} berhasil ditambahkan ke kelas")
            return
    kelas.append([{'nama': nama, 'asal_sekolah': asal_sekolah}])
    print(f"siswa {nama} berhasil ditambahkan ke kelas")

def tampilkan_semua_kelas():
    if len(kelas) == 0:
        print("belum ada siswa")
    else:
        for i in range(len(kelas)):
            print(f"Kelas {i+1}:") 
            for siswa in kelas[i]:
                print(f"{siswa['nama']} ({siswa['asal_sekolah']})")

def update_siswa(nama_lama, nama_baru, asal_sekolah_baru):
    for k in kelas:
        for siswa in k:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"siswa {nama_lama} berhasil diupdate")
                return

def hapus_siswa(nama):
    for k in kelas:
        for i in range(len(k)):
            if k[i]['nama'] == nama:
                k.pop(i)
                print(f"Siswa {nama} telah dihapus")
                return

def menu():
    while True:
        print("== Menu Bimbingan ==")
        print("a. Tambah Siswa")
        print("b. Tampilkan Semua Kelas")
        print("c. Update Data Siswa")
        print("d. Hapus Siswa")
        print("e. Keluar")
        
        pilihan = input("Pilih menu (a/b/c/d/e): ")

        if pilihan == "a":
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            tambah_siswa(nama, asal_sekolah)
            print(f"Siswa {nama} berhasil ditambahkan")
        
        elif pilihan == "b":
            tampilkan_semua_kelas()

        elif pilihan == "c":
            nama_lama = input("masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("masukkan nama baru: ")
            asal_sekolah_baru = input("masukkan asal sekolah baru: ")
            update_siswa(nama_lama, nama_baru, asal_sekolah_baru)
        
        elif pilihan == "d":
            nama = input("masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
        
        elif pilihan == "e":
            print("terima kasih!!!!!")
            break
        
        else:
            print("pilihan tidak valid")

menu()