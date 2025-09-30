import math

# Input panjang sisi segitiga
sisi_a = int(input("Masukkan panjang sisi A: "))
sisi_b = int(input("Masukkan panjang sisi B: "))
sisi_c = int(input("Masukkan panjang sisi C: "))

if (sisi_a + sisi_b > sisi_c) and (sisi_a + sisi_c > sisi_b) and (sisi_b + sisi_c > sisi_a):
    # Menentukan jenis segitiga
    if sisi_a == sisi_b == sisi_c:
        jenis = "Segitiga Sama Sisi"
    elif sisi_a == sisi_b or sisi_a == sisi_c or sisi_b == sisi_c:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"
    print("Jenis segitiga:", jenis)

    # Menghitung luas segitiga 
    s = (sisi_a + sisi_b + sisi_c) / 2
    luas = math.sqrt(s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c))
    print("Luas segitiga:", luas)

else:
    print("Bukan segitiga")
