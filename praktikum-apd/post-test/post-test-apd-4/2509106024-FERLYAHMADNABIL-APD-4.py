import os

username_benar = "nabil"
password_benar = "024"

kesempatan = 0
login = False

while kesempatan < 5:
    os.system('cls' )
    print("=== LOGIN PROGRAM JENIS DAN LUAS SEGITIGA ===")
    user = input("Masukkan Username : ")
    pw = input("Masukkan 3 digit NIM terakhir : ")

    if user.lower() == username_benar and pw == password_benar:
        print("\nLogin berhasil! Selamat datang,", user)
        login = True
        input("Tekan Enter untuk lanjut...")
        os.system('cls' )
        break
    else:
        kesempatan += 1
        print("\nUsername atau Password salah!")
        print("Sisa percobaan:", 5 - kesempatan)
        input("Tekan Enter untuk coba lagi...")

if not login:
    print("\nTerlalu banyak percobaan login. Program berhenti.")
    exit()


while True:
    print("=== MENU PROGRAM ===")
    print("1. Tentukan Jenis Segitiga & Hitung Luas")
    print("2. Keluar Program")
    pilih = input("Pilih menu (1/2): ")

    if pilih == "1":
        os.system('cls')
        print("=== MENENTUKAN JENIS SEGITIGA ===")

        a = int(input("Masukkan sisi A: "))
        b = int(input("Masukkan sisi B: "))
        c = int(input("Masukkan sisi C: "))


        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                print("\nJenis segitiga: Segitiga Sama Sisi")
            elif a == b or a == c or b == c:
                print("\nJenis segitiga: Segitiga Sama Kaki")
            else:
                print("\nJenis segitiga: Segitiga Sembarang")

          
            print("\n--- Hitung Luas Segitiga ---")
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga adalah:", luas)
        else:
            print("\nBukan segitiga! (Tidak memenuhi aturan segitiga)")

        input("\nTekan Enter untuk kembali ke menu...")
        os.system('cls' )

    elif pilih == "2":
        os.system('cls' )
        print("Terima kasih sudah menggunakan program ini #GGMU 2-0")
        break

    else:
        print("\nPilihan tidak tersedia!")
        input("Tekan Enter untuk coba lagi...")
        clear()