from random import randint

def szelesseg():
    r = randint(50, 70)
    while r % 2 != 0:
        r = randint(50, 70)
    return r

def szinek_valasztasa():
    r = randint(0, 255)
    list = []
    for i in range(5):
        list.append(r)
        r = randint(0, 255)
    return list

def befajl(tag, darab, zarotag):
    fr = open("tartalom.txt", "r", encoding="UTF-8")
    sor = fr.readline().split(";")
    while sor != [""]:
        tag.append(sor[0])
        zarotag.append(int(sor[1]))
        darab.append(int(sor[2].strip()))
        sor = fr.readline().split(";")
  

def tagekirasa(tag, darab, zarotag):
    hanykep = 0
    for i in range(len(tag)):
        aktualistag = tag[i]
        if aktualistag == "img":
            hanykep += 1*darab[i]
        if zarotag[i] > 0:
            print(f"<{aktualistag}></{aktualistag}>")
        elif zarotag[i] < 1:
            print(f"<{aktualistag}>")
    return hanykep

def nincszarotag(tag, darab, zarotag):
    zarohianyos = 0
    for i in range(len(tag)):
        if zarotag[i] == 0:
            zarohianyos += 1*darab[i]
    return zarohianyos
  
def hosszutag(tag):
    maxi = 0
    for i in range(len(tag)):
        if len(tag[i]) > len(tag[maxi]):
            maxi = i
    return tag[maxi]

def bennevan(szo, elem):
    n = len(szo)
    astagek = 0
    i = 0
    while i < n and not(szo[i] == elem):
        i += 1

    if i < n:
        astagek += 1
    return astagek

def main():
    print("1.feladat")
    szazalek = szelesseg()
    print(f"width: {szazalek}%;")
    print()
    print("2. feladat")
    list = szinek_valasztasa()
    mini = 0    
    for i in range(len(list)):
        if list[i] < list[mini]:
            mini = i
    print(f"A választott kék szín: rgb(0, 0, {list[mini]})")
    print()
    print("3. feladat\na) Tagek nevei:")
    tag = []
    darab = []
    zarotag = []
    befajl(tag, darab, zarotag)
    hanykep = tagekirasa(tag, darab, zarotag)
    print("b) Képek száma:", hanykep)
    zaronelkuli = nincszarotag(tag, darab, zarotag)
    print(f"c) {zaronelkuli} olyan tag van, aminek nincs záró tag-je.")
    leghosszabbnevu = hosszutag(tag)
    print(f"d) A leghosszabb nevű tag: {leghosszabbnevu}")
    for i in range(len(tag)):
        abetusek = bennevan(tag[i], "a")
    a = "a"
    print(f"e) {abetusek} fajta különböző tag nevében van {a} betű!")
main()