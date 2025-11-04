from colorama import Fore, Style, init
from login import login_user, clear_screen
from hps import tampilkan_pemain, total_harga_pemain
from data import pemain

init(autoreset=True, convert=True, strip=False)

user_login, role = login_user()

while True:
    clear_screen()
    print(Fore.RED + "=== MANCHESTER UNITED MANAGEMENT SYSTEM (MUNYUK)===")
    print(Fore.GREEN + f"Login sebagai: {user_login} ({role})")
    print("---------------------------------------------")
    print("[1] Lihat Data Pemain")
    if role == "admin":
        print("[2] Tambah Pemain Baru")
        print("[3] Update Data Pemain")
        print("[4] Hapus Pemain")
        print("[5] Lihat Total Harga Semua Pemain")
    print("[6] Logout")
    print("---------------------------------------------")

    menu = input(Fore.BLUE + "Pilih menu: " + Style.RESET_ALL)

    if menu == "1":
        tampilkan_pemain(pemain)
        input("\nTekan Enter untuk kembali...")

    elif menu == "2" and role == "admin":
        clear_screen()
        print(Fore.YELLOW + "=== TAMBAH PEMAIN BARU ===")
        nama = input("Nama pemain: ")
        negara = input("Asal negara: ")
        klub = input("Klub sebelumnya: ")
        rating = int(input("Rating (0-100): "))
        harga = int(input("Harga (€): "))
        id_baru = max(pemain.keys()) + 1
        pemain[id_baru] = {"nama": nama, "negara": negara, "klub": klub, "rating": rating, "harga": harga}
        input(Fore.GREEN + " Pemain berhasil ditambahkan!")

    elif menu == "3" and role == "admin":
        tampilkan_pemain(pemain)
        nomor = int(input("Masukkan nomor pemain: "))
        if nomor in pemain:
            data = pemain[nomor]
            print("\nKosongkan jika tidak ingin mengubah field.")
            nama_baru = input(f"Nama [{data['nama']}]: ") or data["nama"]
            negara_baru = input(f"Negara [{data['negara']}]: ") or data["negara"]
            klub_baru = input(f"Klub [{data['klub']}]: ") or data["klub"]
            rating_baru = input(f"Rating [{data['rating']}]: ") or data["rating"]
            harga_baru = input(f"Harga [{data['harga']}]: ") or data["harga"]
            pemain[nomor] = {
                "nama": nama_baru, "negara": negara_baru, "klub": klub_baru,
                "rating": int(rating_baru), "harga": int(harga_baru)
            }
            input(Fore.GREEN + " Data pemain diperbarui!")

    elif menu == "4" and role == "admin":
        tampilkan_pemain(pemain)
        nomor = int(input("Masukkan nomor pemain yang ingin dihapus: "))
        if nomor in pemain:
            del pemain[nomor]
            input(Fore.GREEN + " Pemain berhasil dihapus!")

    elif menu == "5" and role == "admin":
        clear_screen()
        total = total_harga_pemain(pemain)
        print(Fore.MAGENTA + f" Total harga semua pemain: €{total:,}")
        input("\nTekan Enter untuk kembali...")

    elif menu == "6":
        clear_screen()
        print(Fore.YELLOW + "Logout berhasil. Terima kasih telah menggunakan sistem MUNYUK!")
        break

    else:
        input(Fore.RED + " Menu tidak valid atau akses ditolak!")
