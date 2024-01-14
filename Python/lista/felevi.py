targyak = [
    "Fizika", "Matek",
    "Testnevelés", "Irodalom",
    "Antalné Debreczi Imola", "Történelem",
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

#------------------------------------------------------------------
n = len(jegyek)

# F1: Igaz-e, hogy minden tárgyból átment? (nem igaz)
i = 0
while i < n and not(jegyek[i] == 1):
    i += 1
if i < n:
    print("Van amiből megbukott")
else:
    print("Mindenben sikeres volt a tanulmányozás")

# F2: Melyik a leghosszabb nevű tantárgy? (Digitális kultúra)
maxi = 0
for i in range(1, n):
    if len(targyak[i]) > len(targyak[maxi]):
        maxi = i
print(targyak[maxi])

# F3: Van-e olyan tantárgy, amiből ugyanolyan jegyet szerzett, mint irodalomból?
# Feltehető, hogy van "Irodalom" nevű tantárgy!
# Van: (Történelem)
i = 0
while i < n and not(targyak[i] == 'Irodalom'):
    i += 1
irodalomjegy = jegyek[i]
j = 0
while j < n and not(jegyek[j] == irodalomjegy and targyak[j] != "Irodalom"):
    j += 1
if j < n:
    print("Van olyan tantárgy, amelyből ugyanolyan jegyet kapott:", targyak[j])
else:   
    print("Nincs olyan tantárgy")

# F4: Van-e olyan szakmai tárgy, amiből 3-as jegynél rosszabbat kapott?
# Ha igen, akkor add meg az utolsó ilyen tárgy nevét! (Webprog)
i = n - 1
while i >= 0 and not(szakmai[i] == True and jegyek[i] < 3):
    i -= 1
if i >= 0:
    print("Az utolsó szakmai tárgy, amelyből 3-asnál rosszabbat kapott:", targyak[i])
else:
    print("nem vót ijen")

# F5: Van-e két egymást követő tantárgy, ami ugyanazzal a betűvel kezdődik?
# Ha igen, add meg a nevüket! (most nincs, de próbáld ki olyan listával is, amikor van)
i = 0
while i < n-1 and not(targyak[i][0] == targyak[i+1][0]):
    i += 1
if i < n-1:
    print("VAn:", targyak[i], targyak[i+1])
else:
    print("büdös cigány")