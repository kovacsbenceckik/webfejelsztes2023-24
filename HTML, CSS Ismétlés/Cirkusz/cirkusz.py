from random import randint

def ajanlat(igeny):
    if igeny >= 400000:
        valasz = round(igeny * 0.6)
        return valasz
    else:
        valasz = round(igeny * 0.8)
        return valasz

def idok_megadasa():
    idok = []
    ido = 12
    for i in range(11):
        idok.append(f"{ido}:00")
        ido += 1
    return idok

def arak_megadasa():
    arak = []
    ar = 8000
    for i in range(11):
        arak.append(ar)
        ar -= 350
    r = randint(0, len(arak)-1)
    arak[r] * 0.5
    return arak

def kiir():
    idok = idok_megadasa()
    arak = arak_megadasa()
    print("Árlista:")
    for i in range(len(idok)):
        print(f"{idok[i]} {arak[i]}")

def befajl(letszam, idopontok, varosok):
    fr = open("eloadasok.txt", "r", encoding="UTF-8")
    sor = fr.readline().split("---")
    while sor != [""]:
        letszam.append(int(sor[0]))
        idopontok.append(sor[1])
        varosok.append(sor[2].strip())
        sor = fr.readline().split("---")
    fr.close()

def nyolcoraskezdes(idopontok, varosok):
    nyolcasok = []
    for i in range(len(varosok)):
        if idopontok[i] == "20:00":
            nyolcasok.append(varosok[i])
    return nyolcasok

def legkevesebb(letszam, varosok):
    mini = 0
    for i in range(1, len(letszam)):
        if letszam[i] < letszam[mini]:
            mini = i
    telitettseg = round((letszam[mini] / 400) * 100, 2)
    print(f"c) Legkevesebb néző városa: {varosok[mini]}. Telítettség: {telitettseg}%")

def milliomosoke(letszam):
    osszeg = 0
    n = len(letszam)
    for i in range(n):
        osszeg += letszam[i] * 4300
    print(f"d) A cirkusz bevétele: {osszeg/1000000} millió Ft.")

def delelott(idopontok):
    osszesites = 0
    for i in range(len(idopontok)):
        akt = idopontok[i].split(":")
        if int(akt[0]) < 12:
            osszesites += 1
    return osszesites

def main():
    print("1. feladat \n")
    nev = input("Mi a neve? ")
    igeny = int(input("Mennyit szeretne keresni? "))
    valasz = ajanlat(igeny)
    print(f"Kedves {nev}! A végső ajánlatunk: {valasz} Ft.\n")
    print()
    print("2. feladat")
    kiir()
    print()
    print("3. feladat")
    letszam, idopontok, varosok = [], [], []
    befajl(letszam, idopontok, varosok)
    nyolcasok = nyolcoraskezdes(idopontok, varosok)
    print(f"b) 20:00-kor kezdődő előadások helye: {nyolcasok}")
    legkevesebb(letszam, varosok)
    milliomosoke(letszam)
    hanydarab = delelott(idopontok)
    print(f"e) {hanydarab} előadás kezdőtött délelőtt.")
    
main()