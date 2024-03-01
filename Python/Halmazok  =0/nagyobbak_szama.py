'''
Készíts függvényt nagyobbak_szama(szamok, k) néven!

Paraméterek:
- szamok: egészeket tartalmazó lista
- k: küszöbérték, amelynél nagyobbak számát szeretnénk tudni

Visszatérési érték:
Hány darab k-nál nagyobb szám van a listában?
Ha k értékét nem adjuk meg, akkor a pozitív számok számával tér vissza.
'''
# Megszamolas tetel
def nagyobbak_szama(szamok, k=0):
    db = 0
    for i in range(len(szamok)):
        if szamok[i] > k:
            db += 1
    return db


def main():
    print(nagyobbak_szama([4, -1, 0, 7, 5], 4) == 2)
    print(nagyobbak_szama([4, -1, 0, 7, 5]) == 3)

main()