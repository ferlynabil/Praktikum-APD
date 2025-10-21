import os

akun = {
    "admin": {"password": "024", "role": "admin"},
    "user": {"password": "420", "role": "user"}
}

pemain = {
    1: {"nama": "Bruno Fernandes", "negara": "Portugal", "klub": "Sporting Lisbon", "rating": 90, "harga": 80000000},
    2: {"nama": "Casemiro", "negara": "Brazil", "klub": "Real Madrid", "rating": 88, "harga": 70000000},
    3: {"nama": "Benjamin Sesko", "negara": "Slovenia", "klub": "Salzburg", "rating": 92, "harga": 85000000},
    4: {"nama": "Kobbie Mainoo", "negara": "Inggris", "klub": "Akademi MU", "rating": 81, "harga": 2500000},
    5: {"nama": "Senne Lammes", "negara": "Belgia", "klub": "Royal Antwerp", "rating": 94, "harga": 18000000},
}

login = False
role = ""
user_login = ""

while not login:
    os.system('cls')
    print("=== MANAJEMEN TIM MANCHESTER UNITED (MUNYUK) ===")
    print("[1] Login")
    print("[2] Register")
    print("[3] Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        os.system('cls')
        print("=== LOGIN ===")
        user = input("Username: ")
        pw = input("Password: ")

        if user in akun and akun[user]["password"] == pw:
            login = True
            role = akun[user]["role"]
            user_login = user
        else:
            input("Username atau password salah! Tekan Enter untuk lanjut...")

    elif pilih == "2":
        os.system('cls')
        print("=== REGISTER AKUN BARU ===")
        user_baru = input("Masukkan username baru: ")
        if user_baru in akun:
            input("Username sudah terdaftar! Tekan Enter untuk kembali...")
        else:
            pw_baru = input("Masukkan password: ")
            akun[user_baru] = {"password": pw_baru, "role": "user"}
            input("Registrasi berhasil! Silakan login kembali...")

    elif pilih == "3":
        os.system('cls')
        print("Terima kasih telah menggunakan sistem manajemen MU (Munyuk)!")
        exit()

    else:
        input("Pilihan tidak valid! Tekan Enter untuk lanjut...")

while True:
    os.system('cls')
    print("=== MANCHESTER UNITED MANAGEMENT SYSTEM ===")
    print(f"Login sebagai: {user_login} ({role})")
    print("---------------------------------------------")
    print("[1] Lihat Data Pemain")
    if role == "admin":
        print("[2] Tambah Pemain Baru")
        print("[3] Update Data Pemain")
        print("[4] Hapus Pemain")
    print("[5] Logout")
    print("---------------------------------------------")
    menu = input("Pilih menu: ")

    if menu == "1":
        os.system('cls')
        print("=== DAFTAR PEMAIN MANCHESTER UNITED ===")
        print("No | Nama                | Negara        | Klub Sebelumnya     | Rating | Harga (€)")
        print("-------------------------------------------------------------------------------")
        for i, data in pemain.items():
            print(f"{i:<2} | {data['nama']:<18} | {data['negara']:<12} | {data['klub']:<18} | {data['rating']:<6} | {data['harga']}")
        input("\nTekan Enter untuk kembali...")

    elif menu == "2" and role == "admin":
        os.system('cls')
        print("=== TAMBAH PEMAIN BARU ===")
        nama = input("Nama pemain: ")
        negara = input("Asal negara: ")
        klub = input("Klub sebelumnya: ")
        rating = input("Rating performa (0-100): ")
        harga = input("Harga pasar (€): ")

        if rating.isdigit() and harga.isdigit():
            id_baru = max(pemain.keys()) + 1 if pemain else 1
            pemain[id_baru] = {
                "nama": nama,
                "negara": negara,
                "klub": klub,
                "rating": int(rating),
                "harga": int(harga)
            }
            input("Pemain baru berhasil ditambahkan!")
        else:
            input("Input rating atau harga harus berupa angka!")

    elif menu == "3" and role == "admin":
        os.system('cls')
        print("=== UPDATE DATA PEMAIN ===")
        nomor = input("Masukkan nomor pemain yang ingin diupdate: ")

        if nomor.isdigit():
            nomor = int(nomor)
            if nomor in pemain:
                data = pemain[nomor]
                print(f"\nData pemain saat ini:")
                print(f"Nama       : {data['nama']}")
                print(f"Negara     : {data['negara']}")
                print(f"Klub       : {data['klub']}")
                print(f"Rating     : {data['rating']}")
                print(f"Harga (€)  : {data['harga']}")
                print("--------------------------------------")
                print("Kosongkan input jika tidak ingin mengubah field tersebut.\n")

                nama_baru = input(f"Nama baru [{data['nama']}]: ") or data['nama']
                negara_baru = input(f"Negara baru [{data['negara']}]: ") or data['negara']
                klub_baru = input(f"Klub baru [{data['klub']}]: ") or data['klub']
                rating_baru = input(f"Rating baru [{data['rating']}]: ") or str(data['rating'])
                harga_baru = input(f"Harga baru (€) [{data['harga']}]: ") or str(data['harga'])

                if rating_baru.isdigit() and harga_baru.isdigit():
                    pemain[nomor] = {
                        "nama": nama_baru,
                        "negara": negara_baru,
                        "klub": klub_baru,
                        "rating": int(rating_baru),
                        "harga": int(harga_baru)
                    }
                    input("Data pemain berhasil diperbarui!")
                else:
                    input("Rating dan harga harus berupa angka!")
            else:
                input("Nomor pemain tidak ditemukan!")
        else:
            input("Masukkan angka yang benar!")

    elif menu == "4" and role == "admin":
        os.system('cls')
        print("=== HAPUS PEMAIN ===")
        nomor = input("Masukkan nomor pemain yang akan dihapus: ")

        if nomor.isdigit():
            nomor = int(nomor)
            if nomor in pemain:
                print("Menghapus pemain:", pemain[nomor]["nama"])
                yakin = input("Yakin (y/n)? ")
                if yakin.lower() == "y":
                    del pemain[nomor]
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
