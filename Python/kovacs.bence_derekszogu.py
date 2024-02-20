from random import *
from math import *

def generalas(oldalak):
    befogo1 = randrange(1, 101)
    befogo2 = randrange(1, 101)
    atfogo = sqrt(befogo1**2 + befogo2**2)
    atfogo = round(atfogo, 2)
    oldalak.extend([befogo1, befogo2, atfogo])
    print(oldalak)

def haromszog(a, b):
    return (a*b)/2

def kor(r):
    return r**2*pi

def arany(t1, t2):
    ertek = t1/t2*100
    return round(ertek, 2)
    
def main():
    x = []
    generalas(x)
    ht = haromszog(x[0], x[1])
    kt = kor(x[2] / 2)
    print(f"Arány: {arany(ht, kt)}%")
main()
