from random import randint

# Eljárás:
# Megcseréli az "x" lista
# "i"-edik és "j"-edik elemét!
def csere(x, i, j):
    # seged = x[i]
    # x[i] = x[j]
    # x[j] = seged
    x[i], x[j] = x[j], x[i]

# Függvény:
# Az "x" listában a "k"-adik elemtől
# kezdve melyik a legkisebb indexű?
def minindex(x, k):
    index = k
    for i in range(k+1, len(x)):
        if x[i] < x[index]:
            index = i
    return index

# Minimumkiválasztásos rendezés
# 1. Megkeressük az i-edik legkisebb elemet
# 2. Megcseréljük az aktuálissal
def minkiv(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

# Buborékos rendezés
def buborek(x):
    n = len(x)
    for i in range(n):
        vanCsere = False
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                csere(x, j, j+1)
                vanCsere = True
        if not vanCsere:
            return

# Függvény:
# Megad egy "n" elemű listát
# 1 és 9 közötti random
# számokkal feltöltve!
def feltolt(n):
    eredmeny = []
    for i in range(n):
        r = randint(1, 9)
        eredmeny.append(r)
    return eredmeny

def main():
    x = [5, 2, 7, 1, 2, 3]
    print("Eredeti:", x)
    buborek(x)
    print("Rendezett:", x)

    x = feltolt(100)
    print("Random lista:", x)
    buborek(x)
    print("Rendezett random:", x)

main()