from random import randint
'''
Sára nyakláncot készít piros, sárga és kék
színű gyöngyökből.

Egyetlen fontos szabály van:
piros gyöngyöt nem követhet kék!

Készíts függvényt nyaklanc(n) néven,
amely visszatérési értéke egy n hosszú
szöveg, amely P, S és K karakterekből áll
a fenti szabálynak megfelelően!

Pl.:
nyaklanc(2) lehetséges értékei:
"PP", "PS",
"SS", "SK", "SP"
"KK", "KYS"

Vigyázat: nem csak "PK", de "KP" sem jó,
mert a nyaklánc két végét össze kell kötni!
'''
def nyaklanc(n):
    sorrend = []
    for i in range(n):
        r = randint(1, 3)
        if r == 1:
            sorrend.append("P")
        elif r == 2:
            sorrend.append("K")
        else:
            sorrend.append("S")
    
    return sorrend

# Tesztelés
def main():
    print(nyaklanc(2))
    print(nyaklanc(3))
    print(nyaklanc(7))
    print(nyaklanc(15))

main()