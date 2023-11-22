n = int(input("n: "))

osszeg = 0

for i in range(1, n+1):
    aktualis = i**2
    if i %2 ==0:
        osszeg -= aktualis
    else:
        osszeg += aktualis

print(osszeg)