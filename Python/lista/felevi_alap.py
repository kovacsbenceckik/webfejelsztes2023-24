# Tantárgyak listája
targyak = [
    "Fizika", "Matek",
    "Testnevelés", "Irodalom",
    "Angol", "Történelem",
    "Progalap", "IKT",
    "Digitális kultúra", "ITA",
    "Webprog", "Adatbázis"
]

# Szakmai tantárgy-e?
szakmai = [
    False, False,
    False, False,
    False, False,
    True, True,
    False, True,
    True, True,
]

# Félév végi jegyek
jegyek = [3, 1, 2, 4, 5, 4, 2, 5, 5, 4, 1, 4]
n = len(jegyek)
#------------------------------------------------------------------


# F1
# Összegzés (sorozatszámítás) tétel
osszeg = 0
for i in range(n):
    osszeg += jegyek[i]
atlag = osszeg / n
print(f"1. Átlag: {round(atlag, 2)}")

# F2
# Megszámolás
db = 0
for i in range(n):
    if jegyek[i] > 1:
        db += 1
arany = db / n * 100
print(f"2. Teljesített tárgyak aránya: {round(arany, 2)}%")

# F3
# Megszámolás
db = 0
for i in range(n):
    if jegyek[i] == 1 and szakmai[i]:
        db += 1
print(f"3. Bukott szakmai tárgyak száma: {db}")
# F4
legnagyobbsorszam = 0
for i in range(1, n):
    if jegyek[i] > jegyek[legnagyobbsorszam]:
        legnagyobbsorszam = i
kedvenc = targyak[legnagyobbsorszam]
print(f"4. Kedvenc tantárgy: {kedvenc}")

# F5
db = 0
for i in range(n):
 if jegyek[i] > atlag:
     db += 1
print(f"5. Átlagfeletti tárgyak száma: {db}")
    
# F6


# F7


# F8
mini = 0
targy = targyak[0] # "Fizika"
mine = len(targy) # 6
for i in range(1, n):
    akutalisTargy = targyak[i]
    
# F9


# F10


# F11


# F12
