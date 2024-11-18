
wadah = []

def tambah_barang():
    nama_barang = input("Nama Barang: ")
    id_barang = input("ID Barang: ")
    prioritas = input("tingkat Prioritas (darurat/biasa/non-darurat): ")
    while prioritas not in ['darurat', 'biasa', 'non-darurat']:
        print("tidak valid")
        prioritas = input("Tingkat Prioritas (darurat/biasa/non-darurat): ")

    barang = (id_barang, nama_barang, prioritas)
    wadah.append(barang)
    

    

    print("Barang berhasil ditambahkan!")

def tampilbarang():
    if not (wadah):
        print("Belum ada barang yang ditambahkan.")
    else:
        print("daftar Barang yang Dikirim:")
        for barang in wadah:
            print("darurat:")
            if barang[2] == 'darurat':
                print(f"ID : {barang[0]}, Nama Barang: {barang[1]}")
        for barang in wadah:
            print("Biasa:")
            if barang[2] == 'biasa':
                print(f"ID: {barang[0]}, Nama Barang: {barang[1]}")
        for barang in wadah:
            print("Non-Darurat:")
            if barang[2] == 'non-darurat':
                print(f"ID: {barang[0]}, Nama Barang: {barang[1]}")

def m():
    while True:
        tambah_barang()
        tampilbarang()
        
        lagi = input("apakah Anda ingin menambahkan barang lain? (ya/tidak): ")
        if lagi != "ya":
            print("terima kasih!!!!!!!")
            break

m()