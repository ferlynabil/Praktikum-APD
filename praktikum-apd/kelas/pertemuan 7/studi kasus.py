
while True:
    try:
        nama = input("Masukkan nama: ").strip()
        if not nama:  
            raise ValueError("Nama tidak boleh kosong atau hanya berisi spasi!")
        break
    except ValueError as e:
        print("Error:", e)

while True:
    try:
        password = input("Masukkan password: ")
        if len(password) < 8 and not any(char.isdigit() for char in password):
            raise ValueError("Password terlalu pendek (<8 karakter) dan tidak mengandung angka!")
        elif len(password) < 8:
            raise ValueError("Password harus minimal 8 karakter!")
        elif not any(char.isdigit() for char in password):
            raise ValueError("Password harus mengandung minimal satu angka!")
        break
    except ValueError as e:
        print("Error:", e)

barang = {
    "A01": "Buku",
    "A02": "Pulpen",
    "A03": "Pensil"
}

try:
    kode = input("Masukkan kode barang: ").strip().upper()
    print("Nama barang:", barang[kode])
except KeyError:
    print("Kode barang tidak ditemukan")
