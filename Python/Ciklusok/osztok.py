#szam --> irjuk ki a pozitiv egesz osztoit

#minta:
#n: 24
# 1 2 3 4 6 8 12 24

#beolvasas
n = int(input("n: "))

#feldolgzas+kiiras
print("A szám osztói: ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
