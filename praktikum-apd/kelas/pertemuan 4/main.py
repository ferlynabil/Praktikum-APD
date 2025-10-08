
# for i in range(10):
#     print (i + 1)

#(0,1,2,3,4,5,6,7,8,9)
# for i in range(1,11,2):
#     print (i)

# nama = ( "nabil", "diftya", "anugrah")
# for i in nama:
#       print(i)


# for i in range (5):
#     print ("rafli")

# #while loop
# jawab = "ya"
# hitung = 0

# while (jawab == "ya"):
#     hitung += 1
#     jawab = input("ulangi lagi : ?")

# print ("total jawab ya {hitung}")

# cuaca = "hujan"

# while (cuaca == "hujan" or cuaca == "Hujan"):
#     print ("jangan keluar rumah ")
#     cuaca = input("cuaca saat ini : ")

# print ("pergi keluar rumah")


# angka = 10

# while (angka > 1):
#     print (angka)
#     angka -= 2

# for i in range (1,9):
#     for j in range (1,9):
#         print (f"{i} x {j} = {i*j}")
#     print ()

# break
# angka = (2, 5, 8, 12, 15, 7, 20)

# print ("mencari angka yang lebih dari 10,,,,")

# for i in angka:
#     print (f"memeriksa angka {i}")
#     if (i > 10):
#         print (f" {i} lebih dari 10 adalah {i}")
#         break

# print ("Program selesai")
    

# for i in range(1, 11):
#     if i % 2 != 0:
#         continue
#     print(f"Angka genap ditemukan: {i}")

# print("program selesai")

# kuadrat = [i**2 for i in range(1, 6)]
# print (kuadrat)

# angka_genap = [x for x in range(1, 11) if x % 2 == 0]
# print (angka_genap)

# for x in range (1, 11):
#     if x % 2 == 0:
#         print (x)

# angka_ganjil = [x for x in range(1, 11) if x % 2 == 1]
# print (angka_ganjil)

# for i in range (1,6):
#     print (" " * (6-i)+"*"*(2*i-1))

for i in range (1,6):
    print (" " * (i)+"*"*(2*(6-i)-1))