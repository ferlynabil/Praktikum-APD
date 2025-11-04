# num = int("42") 
# name = str(123)
# data = list("abc") 
# data = dict(a=1, b=2) 
# print(type(num))

# angka = 20

# buah = frozenset (["apel", "jeruk", "mangga"])
# print(list(buah))

# angka = (1,2,3,4,5)
# angka = 3.2456
# print(round(angka,2))

# print(pow(2,3,11))

# buah = ["apel", "pisang " , "mangga"]
# for i, item in enumerate(buah):
#     print(i, item)

angka = [1,2,3,4,5,6,]
genap = filter(lambda x: x % 2 == 0, angka)
print(genap)