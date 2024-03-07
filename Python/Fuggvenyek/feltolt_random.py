from random import randint
'''
A feltolt függvény paraméterként
kapjon egy számot, visszatérési értéke
pedig egy lista, amelyben pontosan
annyi egész szám van,
amennyi a paraméter értéke volt!
Pl.: feltolt(12) értéke egy 12 elemű lista.

Az egész számokat véletlenszerűen sorsold
a [-50, 50] intervallumból!

Legyen a függvénynek egy pozitivak nevű
opcionális paramétere is, amelynek
igaz értéket adva az eredeti helyett
az [1, 100] intervallumból választunk számokat!

Ha nem adjunk meg a választható
pozitivak paraméter értékét, akkor
alapértelmezetten hamis legyen!
'''
def feltolt(a, pozitivak = False):
    lista = []
    for i in range(a):
        if pozitivak == True:    
            r = randint(1, 100)
        else:
            r = randint(-50, 50)
        lista.append(r)
    return lista

# Tesztelés
def main():
    print(feltolt(12))
    print(feltolt(7, pozitivak=True))

main()