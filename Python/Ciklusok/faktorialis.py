#olvass be egy n pozitív egész számot
#beolvasás
n = int(input("szám: "))
#feldolgozás
fakt = 1
for i in range(1, n+1):
    fakt *= i 

#kiírás
print(n, "faktoriális:", fakt)