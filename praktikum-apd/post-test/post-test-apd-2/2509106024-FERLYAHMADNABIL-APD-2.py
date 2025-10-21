
data = [21, 2.1, "emyu", True]

print("=== Data Sebelum Diubah ===")
print(data[0], "->", type(data[0]))
print(data[1], "->", type(data[1]))
print(data[2], "->", type(data[2]))
print(data[3], "->", type(data[3]))

total_awal = data[0] + data[1]
print("Total nilai int + float:", total_awal)

data[0] = str(data[0])      
data[1] = int(data[1])      
data[2] = bool(data[2])     
data[3] = float(data[3])    

print("\n=== Data Setelah Diubah ===")
print(data[0], "->", type(data[0]))
print(data[1], "->", type(data[1]))
print(data[2], "->", type(data[2]))
print(data[3], "->", type(data[3]))

total_setelah = data[1] + data[3]
print("Total nilai int + float:", total_setelah)