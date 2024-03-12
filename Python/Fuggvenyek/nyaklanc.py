# 1 feltételt kellett amúgy belerakni még amit néztünk
# ami visszafele is megnézi
import random

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


def general():
    gyongyInt = random.randint(1, 3)
    gyongy = ''
    if gyongyInt == 1:
        gyongy = 'P'
    elif gyongyInt == 2:
        gyongy = 'K'
    else:
        gyongy = 'S'
    return gyongy


def nyaklanc(n):
    lanc = ""
    for i in range(n):
        gyongy = general()
        while i > 0 and (lanc[i - 1] == 'P' and gyongy == 'K' or lanc[i - 1] == 'K' and gyongy == 'P' or i == n - 1 and \
                lanc[0] == 'K' and gyongy == 'P' or i == n - 1 and lanc[0] == 'P' and gyongy == 'K'):
            gyongy = general()
        lanc += gyongy

    return lanc


def main():
    print(nyaklanc(2))
    print(nyaklanc(3))
    print(nyaklanc(7))
    print(nyaklanc(15))


main()