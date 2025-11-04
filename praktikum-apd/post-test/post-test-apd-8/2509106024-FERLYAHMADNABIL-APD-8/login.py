from colorama import Fore, Style, init
from prettytable import PrettyTable
from hps import clear_screen
from data import users
from datetime import datetime

init(autoreset=True, convert=True, strip=False)

def login_user():
    while True:
        clear_screen()
        tabel = PrettyTable()
        tabel.field_names = [Fore.YELLOW + "Menu " + Style.RESET_ALL, Fore.YELLOW + "Keterangan" + Style.RESET_ALL]
        tabel.add_row(["1", "Login"])
        tabel.add_row(["2", "Registrasi"])
        tabel.add_row(["3", "Keluar"])

        print(Fore.RED + "=== SISTEM LOGIN MANCHESTER UNITED ===" + Style.RESET_ALL)
        print(tabel)
        pilih = input(Fore.CYAN + "Pilih menu: " + Style.RESET_ALL)

        if pilih == "1":
            clear_screen()
            print(Fore.YELLOW + "=== LOGIN ===" + Style.RESET_ALL)
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if username in users and users[username]["password"] == password:
                waktu = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                clear_screen()
                tabel_login = PrettyTable()
                tabel_login.field_names = ["Status", "Tanggal & Waktu Login"]
                tabel_login.add_row([" Login Berhasil", waktu])
                print(Fore.GREEN + str(tabel_login))
                role = users[username]["role"]
                input("\nTekan Enter untuk melanjutkan ke sistem...")
                return username, role
            else:
                input(Fore.RED + " Username atau password salah! Tekan Enter untuk ulang...")

        elif pilih == "2":
            clear_screen()
            print(Fore.YELLOW + "=== REGISTER USER BARU ===" + Style.RESET_ALL)
            new_user = input("Buat username: ").strip()
            if new_user in users:
                input(Fore.RED + " Username sudah digunakan! Tekan Enter...")
                continue

            new_pass = input("Buat password: ").strip()
            if not new_pass:
                input(Fore.RED + " Password tidak boleh kosong! Tekan Enter...")
                continue

            role = "user"
            users[new_user] = {"password": new_pass, "role": role}

            clear_screen()
            tabel_reg = PrettyTable()
            tabel_reg.field_names = ["Status", "Username", "Role"]
            tabel_reg.add_row([" Registrasi Berhasil", new_user, role])
            print(Fore.GREEN + str(tabel_reg))
            input("\nTekan Enter untuk kembali ke menu login...")

        elif pilih == "3":
            clear_screen()
            tabel_keluar = PrettyTable()
            tabel_keluar.field_names = ["Status", "Pesan"]
            tabel_keluar.add_row([" Keluar", "Terima kasih telah menggunakan sistem MUNYUK!"])
            print(Fore.YELLOW + str(tabel_keluar))
            exit()

        else:
            input(Fore.RED + " Pilihan tidak valid! Tekan Enter untuk ulang...")
