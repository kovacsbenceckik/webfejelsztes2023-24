n = int(input("n: "))

osszeg = 0

for i in range(1, n+1):
    aktualis = i*(i+1)
    osszeg += aktualis

    print(f"{i}*{i+1}", end=" ")

    if i != n:
        print("+", end=" ")
    else:
        print("=", end=" ")
    
print(osszeg)