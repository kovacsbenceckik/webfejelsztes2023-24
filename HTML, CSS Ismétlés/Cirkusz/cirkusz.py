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

def main():
    print("1. feladat\n")
    nev = input("Mi a neve? ")
    igeny = int(input("Mennyit szeretne keresni? "))
    valasz = ajanlat(igeny)
    print(f"Kedves {nev}! A végső ajánlatunk: {valasz} Ft.\n")
    print("2. feladat")
    idok = idok_megadasa()
    arak = arak_megadasa()
    print("Árlista:\n")
    for i in range(len(idok)):
        print(f"{idok[i]} {arak[i]}")

main()