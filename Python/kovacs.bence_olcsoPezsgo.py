tipusok = [
"BB Spumante", "Kölyök alma",
"Törley Muscateller", "Szovjetszkoje Igrisztoje",
"Hungaria Grande", "Törley alkoholmentes",
"BB alkoholmentes", "Kölyök szamóca"
]

alkoholos = [
True, False,
True, True,
True, False,
False, False
]

arak = [1249, 899, 1699, 1140, 2989, 1699, 1469, 899]

ar = 0
db = 0

for i in range(len(alkoholos)):
    if alkoholos[i] == False:
        db += 1
        ar += arak[i]
    i += 1
atlag = ar / db
# print(f"ár:{ar}, darab:{db}, átlag:{atlag}")

i = 0
x = len(arak)
while i < x and not(arak[i] < atlag and alkoholos[i] == True):
    i += 1
if i < x:
    print(f"Alkoholmentesek átlagánál olcsóbb alkoholos: {tipusok[i]}")
else:
    print("Minden alkoholos drágább a mentesek átlagos áránál!")