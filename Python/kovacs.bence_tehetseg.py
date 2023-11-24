n = int(input("n: "))
oszto = 3
a = 0
szam = 0
for i in range(1,n+1):
     if i % 7 == 0:
           szam += i
print(f"1-től {n}-ig a 7-tel oszthatók összege: ", szam)
while szam % oszto == 0:
    a += 1
    oszto *= 3
print("Ennyiszer osztható 3-mal: ", a)