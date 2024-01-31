n = int(input("n: "))

osszeg = 0

for i in range(1, n+1):
    i = i**2
    if i % 2 == 0:
        i *= -1
    osszeg += i
print("Négyzetösszeg:", osszeg)