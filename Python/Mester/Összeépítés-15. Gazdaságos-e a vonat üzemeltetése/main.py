# Be
n = int(input()) # 6
masodiksor = input().split()
ar = int(masodiksor[0])
koltseg = int(masodiksor[1]) # 1000
leszallok, felszallok = [], []
for i in range(n):
    sor = input().split()
    le = int(sor[0])
    leszallok.append(le)
    fel = int(sor[1])
    felszallok.append(fel)
# print(felszallok)

# Feld
bevetelek = []
letszam = 0
for i in range(n-1):
    letszam = letszam + felszallok[i] - leszallok[i]
    bevetel = letszam * ar
    bevetelek.append(bevetel)
# print(bevetelek)

osszbevetel = 0
for i in range(len(bevetelek)):
    osszbevetel += bevetelek[i]
# print(osszbevetel)

osszkoltseg = (n-1) * koltseg

# Ki
if osszkoltseg < osszbevetel:
    print(1)
else:
    print(0)