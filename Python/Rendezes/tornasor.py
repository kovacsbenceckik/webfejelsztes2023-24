# A "k"-adik elemtől kezdve
# melyik a minimális elem "x"-ben?
def minindex(x, k):
    index = k
    for i in range(k+1, len(x)):
        if x[i] < x[index]:
            index = i
    return index

# Ezt most nem használjuk!
def rendez_eredeti(nevek):
    n = len(nevek)
    for i in range(n):
        j = minindex(nevek, i)
        nevek[i], nevek[j] = nevek[j], nevek[i]

# Rendezi az x listát az y szerint!
# rendez(x, y)
def rendez(x, y):
    n = len(x)
    for i in range(n):
        j = minindex(y, i)
        x[i], x[j] = x[j], x[i]
        y[i], y[j] = y[j], y[i]

def main():
    nevek = ["Robi", "Laci", "Anna",  "Dani", "Ricsi", "Marci"]
    magassagok = [175, 142, 150, 158, 172, 175]
    n = len(nevek)

    # F1 - Adjuk meg a névsort!
    # Feltehető, hogy nincs ékezet a nevekben!
    nevsor = nevek.copy()
    rendez(nevsor, nevsor.copy())
    print("1. Névsor:", nevsor)

    # F2 - Adjuk meg a tornasort (nevek)!
    # (Magasság szerinti növekvő sorrend.)
    rendez(nevek, magassagok)
    print("2. Tornasor:")
    print("   Nevek:", nevek)
    print("   Magasságok:", magassagok)

    # F3 - Egyetlen rendezési függvényt használjunk!

    # F4 - Azonos magasságok esetén a névsor alapján rendezzünk!
    
    # F5 - Adjuk meg, hogy ki áll a tornasor közepén (medián)!
    print("5. A tornasor közepe: ", end="")


main()