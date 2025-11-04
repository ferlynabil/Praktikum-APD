from prettytable import PrettyTable
import random

def tampilkan_pemain(data_pemain):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Negara", "Klub Sebelumnya", "Rating", "Harga (€)"]
    for i, data in data_pemain.items():
        tabel.add_row([i, data['nama'], data['negara'], data['klub'], data['rating'], data['harga']])
    print(tabel)

def tambah_pemain(pemain):
    print("=== TAMBAH PEMAIN BARU ===")
    nama = input("Nama pemain: ")
    negara = input("Asal negara: ")
    klub = input("Klub sebelumnya: ")

    try:
        rating_input = input("Rating (kosongkan untuk acak): ")
        rating = int(rating_input) if rating_input else random.randint(70, 99)
        harga_input = input("Harga (€) (kosongkan untuk acak): ")
        harga = int(harga_input) if harga_input else random.randint(1_000_000, 100_000_000)

        id_baru = max(pemain.keys()) + 1 if pemain else 1
        pemain[id_baru] = {
            "nama": nama, "negara": negara, "klub": klub,
            "rating": rating, "harga": harga
        }
        input("Pemain baru berhasil ditambahkan!")
    except ValueError:
        input("Rating dan harga harus berupa angka!")

from colorama import Fore, Style
from prettytable import PrettyTable
from hps import clear_screen

def hapus_pemain(pemain):
    clear_screen()
    print(Fore.YELLOW + "=== HAPUS DATA PEMAIN ===" + Style.RESET_ALL)
    try:
        nomor = int(input("Masukkan nomor pemain yang ingin dihapus: "))
        if nomor in pemain:
            data = pemain[nomor]
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama", "Negara", "Klub", "Rating", "Harga (€)"]
            tabel.add_row([nomor, data['nama'], data['negara'], data['klub'], data['rating'], f"{data['harga']:,}"])
            print(Fore.CYAN + str(tabel) + Style.RESET_ALL)

            yakin = input(Fore.RED + "Yakin ingin menghapus pemain ini? (y/n): " + Style.RESET_ALL).lower()
            if yakin == "y":
                del pemain[nomor]
                input(Fore.GREEN + " Pemain berhasil dihapus! Tekan Enter untuk kembali..." + Style.RESET_ALL)
            else:
                input(Fore.YELLOW + " Penghapusan dibatalkan. Tekan Enter untuk kembali..." + Style.RESET_ALL)
        else:
            input(Fore.RED + " Nomor pemain tidak ditemukan! Tekan Enter untuk kembali..." + Style.RESET_ALL)
    except ValueError:
        input(Fore.RED + "⚠️  Masukkan angka yang benar! Tekan Enter untuk kembali..." + Style.RESET_ALL)


def update_pemain(pemain):
    print("=== UPDATE DATA PEMAIN ===")
    try:
        nomor = int(input("Masukkan nomor pemain yang ingin diupdate: "))
        if nomor in pemain:
            data = pemain[nomor]
            print(f"\nData pemain saat ini: {data}")
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
    except ValueError:
        input("Masukkan angka yang benar!")
