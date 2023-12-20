lista = [5, 2, 6, 7, -11, 35, 2, 13, 10]
print(f"x = {lista}")

osszeg = 0
db = 0
for i in range(len(lista)):
    if lista[i] % 2 != 0:
        osszeg += lista[i]
        db += 1
        
osszeg /= db
print(f"A páratlanok átlaga: {osszeg}")