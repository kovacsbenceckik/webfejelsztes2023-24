#F1
n = int(input())
nevek = []
magyar = []
matek = []
tori = []

for i in range(n):
    sor = input().split()
    nev = sor[0]
    magy = int(sor[1])
    mat = int(sor[2])
    tort = int(sor[3])
    nevek.append(nev)
    magyar.append(magy)
    matek.append(mat)
    tori.append(tort)
#F2

ossz = 0
for i in range(n):
    ossz += tori[i]    
print("2. feladat:", round(ossz/n, 3))

#F3
osszeg = 0
for i in range(n):
    if matek[i] == 1:
        osszeg += 1

print("3. feladat:", osszeg)
#F4 - Maximum kivalasztas
maxi = 0
maxe = (magyar[0] + matek[0] + tori[0])
for i in range(1, n):
    atlag = (magyar[i] + matek[i] + tori[i]) / 3
    if atlag > maxe:
        maxi = i
        maxe = atlag
print("4. feladat:", nevek[maxi])

#F5
i = 0
while i < n and not(magyar[i] < matek[i]):
    i += 1
if i < n:
    print("5. feladat:", nevek[i])
else:
    print("5. feladat: Nincs.")

# F6
anev = 0
anevpoz = [] 
for i in range(n):     
    hossz = len(nevek[i]) -1
    if nevek[i][hossz] == "a":         
        anev += 1         
        anevpoz.append(i)
print("6. feladat:", anev, end=" ")
sza = len(anevpoz)-1 
for i in range(len(anevpoz)-1):
    print(nevek[anevpoz[i]], end=" ")
print(nevek[anevpoz[sza]])

# F7
i = 0
while i < n and not(magyar[i] == matek[i] and magyar[i] == tori[i] and matek[i] == tori[i]):
    i += 1
if i < n:
    print("7. feladat: Vanik.")
else:
    print("7. feladat: Nincs.")
    
# F8

print("8. feladat:")


# F9

print("9. feladat:")


# F10

print("10. feladat:")

