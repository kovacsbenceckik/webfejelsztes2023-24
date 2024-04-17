def befajl(nevek, korok, fr):
    sor = fr.readline().split(" ")
    while sor != [""]:
        nevek.append(sor[0])
        korok.append(int(sor[1].strip()))
        sor = fr.readline().split(" ")


def minindex(korok, k):
    index = k
    for i in range(k+1, len(korok)):
        if korok[i] < korok[index]:
            index = i
    return index

def rendez(nevek, korok):
    n = len(nevek)
    for i in range(n):
        j = minindex(korok, i)
        korok[i], korok[j] = korok[j], korok[i]
        nevek[i], nevek[j] = nevek[j], nevek[i]

        
def kifajl(nevek, korok, fw):
    for i in range(len(korok)):
        fw.write(f"{nevek[i]} {korok[i]}\n")


def main():
    nevek, korok = [], []
    f = open("nevek.txt", "a+", encoding="UTF-8")
    
# Megnyitási módok:
# r+ --> nem hozza létre a fájlt, ha nem létezik
# w+ --> törli a fájl tartalmát
# a+ --> az író-olvasó fej (kezdetben) a fájl végén van

    f.seek(0) # az elejere rakjuk a segget az a+ -nak
    befajl(nevek, korok, f)
    rendez(nevek, korok)
    f.truncate(0) # torli a teljes tartalmat
    kifajl(nevek, korok, f)
    f.close()
main()
