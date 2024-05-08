from random import randint
import os

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

def ujversenyzo(nevek, pontok, maxpont):
    fw = open("be.txt", "a", encoding="UTF-8")
    nevek.append("Aloe Vera")
    r = randint(0, maxpont)
    pontok.append(r)
    fw.write(f"Aloe Vera: {pontok[-1]}\n")
    fw.close()

def futtatas():
    fw = open("naplo.txt", "a+", encoding="UTF-8")
    fw.seek(0)
    sor = fw.readline()
    db = 0
    while sor != "":
        db += 1
        sor = fw.readline()
    fw.write(f"A program {db + 1}. alkalommal futott sikeresen!\n")
    fw.close()

def rendez(nevek, pontok):
    for i in range(len(nevek)):
        for j in range(i + 1, len(nevek)):
            if pontok[i] < pontok[j]:
                n = nevek[i]
                p = pontok[i]
                nevek[i] = nevek[j]
                pontok[i] = pontok[j]
                nevek[j] = n
                pontok[j] = p
    return nevek, pontok
            
def kiiras(nevek, pontok):
    fw = open("eredmeny.txt", "w", encoding="UTF-8")
    fw.write(f"Eredmenyek: \n")
    for i in range(len(nevek)):
        fw.write(f"{nevek[i]} - {pontok[i]} \n")
    fw.close()

def main():
    nevek, pontok = [], []
    os.chdir(r"D:\Github\webfejelsztes2023-24\Python\Fajlok\Verseny")
    maxpont = befajl(nevek, pontok)
    ujversenyzo(nevek, pontok, maxpont)
    futtatas()
    print(rendez(nevek, pontok))
    kiiras(nevek, pontok)
main()
