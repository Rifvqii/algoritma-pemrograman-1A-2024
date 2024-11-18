
basket = {"adimas", "rifki", "rendi", "hilya", "naisa"}
renang = {"adimas", "jefri", "rio", "kiki", "naisa"}

print("daftar siswa di Klub Basket:", basket)
print("daftar siswa di Klub Renang:", renang)

# INTERSECTION
kedua_klub = basket & renang
print("siswa yang mengikuti kedua klub:", kedua_klub)
# SYMETRIC DIFFRENCE
satu_klub = basket ^ renang
print("siswa yang hanya mengikuti satu klub saja:", satu_klub)
# UNION
semua_siswa = basket | renang
print("semua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa)

print(f"jumlah semua {len(semua_siswa)}")

