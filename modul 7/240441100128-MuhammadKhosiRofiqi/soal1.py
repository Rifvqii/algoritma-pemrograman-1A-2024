alat_peminjaman = {
    "alat_tekanandarah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat_tensi": 0,
    "inheler": 0
}

alat_peminjaman["alat_tekanandarah"] += 2
alat_peminjaman["termometer"] += 3
alat_peminjaman["stetoskop"] += 4
alat_peminjaman["alat_tekanandarah"] -= 1
alat_peminjaman["termometer"] -= 2
alat_peminjaman["stetoskop"] -= 3
alat_peminjaman["inheler"] += 2

print("Jadi alat yang dipinjam Heni saat ini adalah:")
for alat in alat_peminjaman:
    jumlah = alat_peminjaman[alat]
    if jumlah > 0:
        print(f"{alat}: {jumlah}")