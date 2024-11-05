def angka (r):

    if r == 0:
        return 0
    elif r == 1:
        return 1
    else:
        return angka(r-1)+angka(r-2)
print(angka(7))