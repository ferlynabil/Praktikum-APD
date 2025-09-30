# membuat list dengan berbagai tipe data
data = [21, 2.1, "emyu", True]

print("=== Data Sebelum Diubah ===")
print(data[0], "->", type(data[0]))
print(data[1], "->", type(data[1]))
print(data[2], "->", type(data[2]))
print(data[3], "->", type(data[3]))

# hitung total nilai int + float (manual)
total_awal = data[0] + data[1]
print("Total nilai int + float:", total_awal)

# ============================
# Ubah tipe data
data[0] = str(data[0])      # int -> str
data[1] = int(data[1])      # float -> int
data[2] = bool(data[2])     # str -> bool
data[3] = float(data[3])    # bool -> float

print("\n=== Data Setelah Diubah ===")
print(data[0], "->", type(data[0]))
print(data[1], "->", type(data[1]))
print(data[2], "->", type(data[2]))
print(data[3], "->", type(data[3]))

# hitung total lagi (manual, cuma ambil int + float)
total_setelah = data[1] + data[3]
print("Total nilai int + float:", total_setelah)