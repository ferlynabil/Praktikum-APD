import os
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True, convert=True, strip=False)

def total_harga_pemain(pemain):
    return sum(data["harga"] for data in pemain.values())

def tampilkan_pemain(pemain):
    clear_screen()
    print(Fore.RED + "=== DAFTAR PEMAIN MANCHESTER UNITED ===" + Style.RESET_ALL)
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Negara", "Klub", "Rating", "Harga (€)"]
    for i, data in pemain.items():
        tabel.add_row([
            i,
            data["nama"],
            data["negara"],
            data["klub"],
            data["rating"],
            f"€{data['harga']:,}"
        ])
    print(Fore.CYAN + str(tabel) + Style.RESET_ALL)

def tampilkan_user(users):
    print(Fore.YELLOW + "\n=== DAFTAR USER TERDAFTAR ===" + Style.RESET_ALL)
    tabel = PrettyTable()
    tabel.field_names = ["Username", "Role"]
    for username, data in users.items():
        tabel.add_row([username, data["role"]])
    print(Fore.CYAN + str(tabel) + Style.RESET_ALL)

def clear_screen():
    os.system("cls" )
