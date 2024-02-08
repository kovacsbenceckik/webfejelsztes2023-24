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
maxe = (magyar[0] + matek[0] + tori[0]) / 3
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
nevet = []
for i in range(n):
    hossz = len(nevek[i])
    if nevek[i][hossz-1] == "a":
        nevet.append(nevek[i])
print("6. feladat:",len(nevet), end=" ")
for i in range(len(nevet)):
    print(nevet[i], end=" ")
print()
# F7
i = 0
while i < n and not(magyar[i] == matek[i] and magyar[i] == tori[i] and matek[i] == tori[i]):
    i += 1
if i < n:
    print("7. feladat: Vanik.")
else:
    print("7. feladat: Nincs.")
    
# F8
i = 0
while i < n and magyar[i] != 5:
    i += 1
if i < n:
    for j in range(i+1, n):
        if magyar[j] == 5 and matek[j] <= matek[i]:
            i = j
    print("8. feladat:", nevek[i])
else:
    print("8. feladat:", -1)
# F9
bukottdiak = 0
for i in range(n):
    if magyar[i] == 1 or matek[i] == 1 or tori[i] == 1:
        bukottdiak += 1

print(f"9. feladat: {round((bukottdiak/n)*100, 2)}%")
# F10
print("10. feladat:")
for i in range(n):
    if i == 0:
        if matek[i] < matek[i+1]:
            print(i+1, end=" ")
    elif i == n-1:
        if matek[i] < matek[i-1]:
            print(i+1, end=" ")
    else:
        if matek[i] < matek[i+1] or matek[i] < matek[i-1]:
            print(i+1, end=" ")

