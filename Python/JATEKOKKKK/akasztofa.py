from random import randrange
from os import system
# vbhblkjfdoihNiggeröuebihbfNiggerdvolyhz blfdih ypifubpfhb hounéyofNiggerdnlyihbf éjn ouíoubvéi b.

def kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print(s[i], end=" ")
    print()

def sorsolas():
    szavak = [
    "halozat","python", "vampirevape.co.uk",
    "ertelmes","szamitogep",
    "snus", "poco", "fnlckik"]
    r = randrange(len(szavak))
    neo = szavak[r]
    # for ziglus
    return neo
def kezdeti_allapot(n):
    eredmeny = []
    for i in range(n):
        eredmeny.append("_")
    return eredmeny

def csere(betu, aktualis, megoldas):
    for i in range(len(megoldas)):
        if megoldas[i] == betu:
            aktualis[i] = betu

def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(elem == lista[i]):
        i += 1
    return i < len(lista)

def fordulo(aktualis, megoldas, hibaszam):
    betu = input("\n Betű:")
    if not(bennevan(betu, megoldas)):
        hibaszam += 1
    print(megoldas)
    csere(betu, aktualis, megoldas)
    system("cls")
    kirajzol(aktualis)
    return hibaszam

def eredmenyhirdetes(hibaszam):
    if hibaszam <= 2:
        print("Nyertél :)")
    else:
        print("Vesztettél :(")
    

def jatek(megoldas):
    aktualis = kezdeti_allapot(len(megoldas))
    kirajzol(aktualis)
    hibaszam = 0
    while bennevan("_", aktualis) and hibaszam <= 2:
        hibaszam = fordulo(aktualis, megoldas, hibaszam)
    eredmenyhirdetes(hibaszam)

def mian():
    system("cls")
    megoldas = sorsolas()
    print(megoldas)
    jatek(megoldas)

mian()