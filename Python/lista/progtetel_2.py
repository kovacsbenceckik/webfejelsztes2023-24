x = [5, 1, 6, -3, 12, 8, 10, 29, 16, 6, 2, 11]
n = len(x)

# F0
# x[i] != 6
i = 0
while i < n and not(x[i] == 6):
    i += 1
if i < n:
    print("0. Első 6-os sorszáma:", i+1)
else:
    print("0. Nincs a listában 6-os.")

# F1
# Add meg az első páros számot! Ha nincs a listában páros szám, akkor az „1. Nincs páros szám!” kerüljön a konzolra!
# 1. Első páros szám: 6
# x[i] % 2 != 0
# x[i] % 2 == 1
i = 0
while i < n and not(x[i] % 2 == 0):
    i += 1
if i < n:
    print("1. Első páros szám:", x[i])

# F2
# Van-e a listában 10 és 20 közötti szám (a határokat is beleértve)? Ha igen, add meg a sorszámát!
# 2. Első 10 és 20 közötti sorszáma: 5
# nem(A és B) => nem(A) vagy nem(B)
# x[i] < 10 or x[i] > 20
i = 0
while i < n and not(x[i] >= 10 and x[i] <= 20):
    i += 1
if i < n:
    print("2. Első 10 és 20 közötti sorszáma:", i+1)

# F3
# 3. Található-e 3-mal osztható páratlan szám? Amennyiben igen, add meg az elsőt!
# 3. Első 3-mal osztható páratlan: -3
i = 0
while i < n and not(x[i] % 3 == 0 and x[i] % 2 == 1):
    i += 1
if i < n:
    print("3. Első 3-mal osztható páratlan:", x[i])

# F4
# 4. Osztható-e valamelyik szám 4-gyel? Ha igen, add meg az utolsót!
# 4. Utolsó 4-gyel oszható: 16
i = n-1
while i >= 0 and not(x[i] % 4 == 0):
    i -= 1
if i >= 0:
    print("4. Utolsó 4-gyel oszható:", x[i])

# F5
# 5. Igaz-e, hogy a lista első eleme a legkisebb?
# Pl.: 5. Nem az első a legkisebb!
# Eldöntés: Van-e kisebb elem az elsőnél?
i = 0
while i < n and not(x[i] < x[0]):
    i += 1
if i < n:
    print("5. Nem az első a legkisebb!")
else:
    print("5. Az első a legkisebb!")

# F6
i = 0
ossz = 0
for i in range(n):
    ossz += x[i]
atlag = ossz / n
while i < n and not(x[i] >= atlag):
    i += 1
if i < n:
    print("6. Első legalább átlagos elem: ", x[i])

# F7
# 7. Monoton növekedő-e a lista?
# Pl.: 7. Nem monoton növekvő!
i = 0
while i < n-1 and not(x[i] < x[i-1]):
    i += 1
if i < n:
    print("7. Nem monoton növekvő!")
else:
    print("7. Monoton növekvő!")


# F8
# 8. Egyforma előjelű-e az összes eleme a listának?
#Eldöntés: van e ket egymas melletti kulonbozo elojel?

i = 0
while i < n and not(x[i] > 0 and x[i+1] < 0 or x[i] < 0 and x[i+1] > 0):
    i += 1
if i < n :
    print("8. Nem egyforma előjelűek!")
else:
    print("8. Egyforma előjelűek!")

# F9 


# F10


# F11


# F12