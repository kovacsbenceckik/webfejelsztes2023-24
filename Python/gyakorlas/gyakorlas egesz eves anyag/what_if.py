cimek = [
    "Nebula beállna a Nova hadtestbe?",
    "Peter Quill rátámadna a Föld legnagyobb szuperhőseire?",
    "Happy Hogan megmentené a Karácsonyt?",
    "Vasember összetűzésbe keveredne a Nagymesterrel?",
    "Carter Kapitány megküzdene a Hydra-Ölővel?",
    "Kahhori felforgatná a világot?",
    "Hela rátalálna a Tíz Gyűrűre?",
    "a Bosszúállók 1602-ben élnének?",
    "Doctor Strange beavatkozna?"
]

percek = [29, 29, 27, 32, 30, 32, 28, 29, 31]

ertekelesek = [7, 9, 7, 8, 7.5, 8, 9.5, 7, 5]

# F1

anyad = []
n = len(cimek)

for i in range(n):
    if ertekelesek[i] > 7:
        anyad.append(cimek[i])
print(anyad)

# F2

maxi = 0

for i in range(n):
    if percek[i] > percek[maxi]:
        maxi = i
print()
print(cimek[maxi])

# F3

elso = percek[0]
utolso = percek[-1]
db = 0
for i in range(n):
    if percek[i] < elso and percek[i] < utolso:
        db += 1
print()
print(db)
# F4
perc = 0
for i in range(n):
    perc += percek[i]
ora = int(perc / 60)
perccc = int(perc % 60)
print(f"{ora} óra {perccc} perc")