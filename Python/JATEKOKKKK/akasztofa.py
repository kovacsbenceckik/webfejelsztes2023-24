from random import randrange
from os import system
# vbhblkjfdhodfzboihéfnbőaöuebihbfdvolyhz blfdih ypifubőyoubypfhb hounéyofdnlyihbf éjn ouíőáouőáoubvéi b.

def vonalak_kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print("_", end=" ")
    print()

def sorsolas():
    szavak = [
    "halozat","python", "vampirevape.co.uk",
    "ertelmes","szamitogep",
    "snus", "poco", "fnlckik"]
    r = randrange(len(szavak))
    neo = szavak[r]
    # for ziglus
    return neo

def mian():
    system("cls")
    megoldas = sorsolas()
    vonalak_kirajzol(megoldas)
    print(megoldas)

mian()