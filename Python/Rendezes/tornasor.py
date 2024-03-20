def rendez(nevek):
    n = len(nevek)
    for i in range(n):
        j = minindex(nevek[i], i)
        csere(nevek[i], i, j)






def main():
    nevek = ["Robi", "Laci", "Anna",  "Dani", "Ricsi", "Marci"]
    magassagok = [175, 142, 150, 158, 172, 175]
    n = len(nevek)

    # F1 - Adjuk meg a névsort!
    # Feltehető, hogy nincs ékezet a nevekben!
    nevsor = rendez(nevek)
    print("1. Névsor:", nevsor)




    # F2 - Adjuk meg a tornasort (nevek)!
    # (Magasság szerinti növekvő sorrend.)
    print("2. Tornasor:")
    print("   Nevek:", nevek)
    print("   Magasságok:", magassagok)




    # F3 - Egyetlen rendezési függvényt használjunk!

    # F4 - Azonos magasságok esetén a névsor alapján rendezzünk!
    
    # F5 - Adjuk meg, hogy ki áll a tornasor közepén (medián)!
    print("5. A tornasor közepe: ", end="")


main()