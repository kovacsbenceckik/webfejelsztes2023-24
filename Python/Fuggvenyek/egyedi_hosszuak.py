'''
Készíts függvényt egyedi_hosszuak(x) néven, amely
megadja az x lista azon elemeit,
amelyek előtt nincs velük azonos hosszú elem!

Paraméterek:
x: szövegeket tartalmazó lista

Visszatérési érték:
Egy lista a megfelelő (egyedi) elemekkel!
'''
def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)


def egyedi_hosszuak(szavak):
    egyediek = []
    hosszak = []
    for i in range(len(szavak)):
        if not(bennevan(len(szavak[i]), hosszak)):
            egyediek.append(szavak[i])
            hosszak.append(len(szavak[i]))
    return egyediek

def main():
    print(egyedi_hosszuak(["alma", "banan", "korte", "barack"]) == ["alma", "banan", "barack"])
    print(egyedi_hosszuak(["piros", "feher", "zold", "barna", "lila"]) == ["piros", "zold"])
    print(egyedi_hosszuak(["abc", "aab", "abba", "baba"]) == ["abc", "abba"])

main()