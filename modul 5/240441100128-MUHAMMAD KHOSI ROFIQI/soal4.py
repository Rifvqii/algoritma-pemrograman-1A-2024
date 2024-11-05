def palindrom(kalimat):
    dibalik = ""
    for i in kalimat:
        dibalik = i + dibalik
        print(i)
    if dibalik == kalimat:
        print ("benar")
    else:
        print ("salah")
    # return dibalik
kalimat = input("kalimat : ")
print(palindrom(kalimat))


