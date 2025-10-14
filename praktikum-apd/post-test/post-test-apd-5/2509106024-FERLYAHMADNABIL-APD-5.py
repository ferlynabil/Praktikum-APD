import os

akun = [["admin", "024", "admin"], ["user", "420", "user"]]
pemain = [
    ["Bruno Fernandes", "Portugal", "Sporting Lisbon", 90, 80000000],
    ["Casemiro", "Brazil", "Real Madrid", 88, 70000000],
    ["Benjamin Sesko", "Slovenia", "Salzburg", 92, 85000000],
    ["Kobbie Mainoo", "Inggris", "Akademi MU", 81, 2500000],
    ["Senne Lammes", "Belgia", "Royal Antwerp", 94, 18000000],
]

login = False
role = ""

while not login:
    os.system('cls')
    print("=== MANAJEMEN TIM MANCHESTER UNITED / MUNYUK ===")
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = input("Username: ")
        pw = input("Password: ")

        i = 0
        while i < len(akun):
            if akun[i][0] == user and akun[i][1] == pw:
                login = True
                role = akun[i][2]
                break
            i = i + 1

        if login == False:
            input("Username / Password salah! Tekan Enter untuk lanjut...")

    elif pilih == "2":
        os.system('cls')
        print("=== REGISTER AKUN BARU ===")
        user_baru = input("Masukkan username baru: ")
        pw_baru = input("Masukkan password: ")
        akun.append([user_baru, pw_baru, "user"])
        input("Registrasi berhasil! Silakan login kembali...")

    elif pilih == "3":
        os.system('cls')
        print("Terima kasih telah menggunakan sistem manajemen MU (Munyuk)!")
        exit()

    else:
        input("Pilihan tidak valid! Tekan Enter...")

while True:
    os.system('cls')
    print("=== MANCHESTER UNITED MANAGEMENT SYSTEM ===")
    print("Login sebagai:", role)
    print("---------------------------------------------")
    print("[1] Lihat Data Pemain")
    if role == "admin":
        print("[2] Tambah Pemain Baru")
        print("[3] Update Harga Pemain")
        print("[4] Hapus Pemain")
    print("[5] Logout")
    print("---------------------------------------------")
    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls')
        print("=== DAFTAR PEMAIN MANCHESTER UNITED ===")
        print("No | Nama                | Negara        | Klub Sebelumnya     | Rating | Harga (€)")
        print("-------------------------------------------------------------------------------")
        i = 0
        while i < len(pemain):
            print(i+1, "|", pemain[i][0], "|", pemain[i][1], "|", pemain[i][2], "|", pemain[i][3], "|", pemain[i][4])
            i = i + 1
        input("\nTekan Enter untuk kembali...")

    elif menu == "2" and role == "admin":
        os.system('cls')
        print("=== TAMBAH PEMAIN BARU ===")
        nama = input("Nama pemain: ")
        negara = input("Asal negara: ")
        klub = input("Klub sebelumnya: ")
        rating = input("Rating performa (0-100): ")
        harga = input("Harga pasar (€): ")

        cek_angka = True
        for huruf in rating:
            if huruf not in "0123456789":
                cek_angka = False
        for huruf in harga:
            if huruf not in "0123456789":
                cek_angka = False

        if cek_angka == True:
            pemain.append([nama, negara, klub, int(rating), int(harga)])
            input("Pemain baru berhasil ditambahkan!")
        else:
            input("Input rating atau harga harus angka!")

    elif menu == "3" and role == "admin":
        os.system('cls')
        print("=== UPDATE HARGA PEMAIN ===")
        index = input("Masukkan nomor pemain: ")

        angka_benar = True
        for huruf in index:
            if huruf not in "0123456789":
                angka_benar = False

        if angka_benar == True:
            index = int(index) - 1
            if index >= 0 and index < len(pemain):
                print("Nama pemain:", pemain[index][0])
                harga_baru = input("Masukkan harga baru (€): ")

                angka_baru = True
                for huruf in harga_baru:
                    if huruf not in "0123456789":
                        angka_baru = False

                if angka_baru == True:
                    pemain[index][4] = int(harga_baru)
                    input("Harga pemain berhasil diperbarui!")
                else:
                    input("Harga harus berupa angka!")
            else:
                input("Nomor pemain tidak ditemukan!")
        else:
            input("Masukkan angka yang benar!")

    elif menu == "4" and role == "admin":
        os.system('cls')
        print("=== HAPUS PEMAIN ===")
        index = input("Masukkan nomor pemain yang akan dihapus: ")

        angka_valid = True
        for huruf in index:
            if huruf not in "0123456789":
                angka_valid = False

        if angka_valid == True:
            index = int(index) - 1
            if index >= 0 and index < len(pemain):
                print("Menghapus pemain:", pemain[index][0])
                yakin = input("Yakin (y/n)? ")
                if yakin == "y" or yakin == "Y":
                    del pemain[index]
                    input("Pemain berhasil dihapus!")
                else:
                    input("Penghapusan dibatalkan.")
            else:
                input("Nomor pemain tidak valid!")
        else:
            input("Masukkan angka yang benar!")

    elif menu == "5":
        break

    else:
        input("Menu tidak valid atau akses ditolak!")
