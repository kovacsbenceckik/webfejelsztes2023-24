# Válogassuk ki a közös elemeket
def bennevan(szam, x):
    i = 0
    while i < len(x) and not x[i] == szam:
        i += 1
    return i < len(x)
def metszet(a, b):
    eredmeny = []
    for i in range(len(a)):
        if bennevan(a[i], b):
            eredmeny.append(a[i])
    return eredmeny

def unio(a, b):
    un = []
    for i in range(len(a)):
        un.append(a[i])
    for i in range(len(b)):
        if not bennevan(b[i], a):
            un.append(b[i])
    return un

def kulonbseg(a, b):
    kulonb = []
    for i in range(len(a)):
        if not(bennevan(a[i], b)):
            if not(bennevan(a[i], kulonb)):
                kulonb.append(a[i])
    for i in range(len(b)):
        if not(bennevan(b[i], a)):
            if not(bennevan(b[i], kulonb)):
                kulonb.append(b[i])
    return kulonb

def szimm_diff(a, b):
    eredmeny = []
    un = unio(a, b)
    metsz = metszet(a, b)
    
    for i in range(len(un)):
        if not bennevan(un[i], metsz):
            eredmeny.append(un[i])
    return eredmeny

def main():
    a = [2, 7, 1, 5, 3]
    b = [1, 6, 8, 7]
    m = metszet(a, b)
    u = unio(a, b)
    k = kulonbseg(a, b)
    print("Metszet:", m)
    print("Unió:", u)
    print("Külonbség:", k)
    szim = szimm_diff(a, b)
    print("Szimmetrikus differencia:", szim)

main()