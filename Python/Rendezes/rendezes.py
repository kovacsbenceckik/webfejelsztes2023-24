from random import randint
from time import time

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

def feltolt_nagyjabol_rendezett(n):
    eredmeny = []
    eredmeny.append(randint(1, 9))

    for i in range(n):
        elozo = eredmeny[i]
        r = randint(1, 10)
        if r <= 8:
            eredmeny.append(elozo + 1)
        else:
            eredmeny.append(elozo - 1)
    return eredmeny

def teszt(n):
    x = feltolt_nagyjabol_rendezett(n)
    print("Lista feltöltve!")

    y = x.copy()
    kezdet = time()
    minkiv(y)
    veg = time()
    print("Minkiv kész:", veg - kezdet)

    z = x.copy()
    kezdet = time()
    buborek(z)
    veg = time()
    print("Buborekos kész:", veg - kezdet)

def main():
    teszt(1000)

main()