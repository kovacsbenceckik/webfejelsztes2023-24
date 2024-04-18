from random import randint

def befajl(nevek, pontok):
    fr = open("be.txt", "r", encoding="UTF-8")
    maxpont = int(fr.readline())
    sor = fr.readline().split(": ")
    while sor != [""]:
        nevek.append(sor[0])
        pontok.append(int(sor[1].strip()))
        sor = fr.readline().split(": ")
    fr.close()
    return maxpont
        
def futtatas():
    fw = open("naplo.txt", "a+", encoding="UTF-8")
    fw.seek(0)
    db = 0
    sor = fw.readline()
    while sor != "":
        db += 1
        sor = fw.readline()
    fw.write(f"A program {db+1} alkalommal futott le sikeresen!\n")
    fw.close()
    
def bennevan(str, list):
    i = 0
    while i < len(list) and not(list[i] == str):
        i += 1
    if i < len(list):
        return True
    else:
        return False

def ujjatekos(nevek, pontok, maxpont):
    fw = open("be.txt", "a", encoding="UTF-8")
    if bennevan("Aloe Vera", nevek):
        pass
    else:
        nevek.append("Aloe Vera")
        r = randint(0, maxpont)
        pontok.append(r)
        fw.write(f"Aloe Vera: {r}\n")
    fw.close()

def rendez(nevek, pontok):
    n = len(pontok)
    for i in range(n):
        for j in range(i + 1, n):
            if pontok[i] < pontok[j]:
                x = pontok[i]
                y = nevek[i]
                nevek[i] = nevek[j]
                pontok[i] = pontok[j]
                nevek[j] = y
                pontok[j] = x

def kiir(nevek, pontok):
    fw = open("eredmeny.txt", "w", encoding="UTF-8")
    for i in range(len(nevek)):
        fw.write(f"{nevek[i]}: {pontok[i]}\n")
    fw.close()

def main():
    nevek, pontok = [], []
    maxpont = befajl(nevek, pontok)
    futtatas()
    ujjatekos(nevek, pontok, maxpont)
    rendez(nevek, pontok)
    kiir(nevek, pontok)
    print(nevek)
    print(pontok)

main()