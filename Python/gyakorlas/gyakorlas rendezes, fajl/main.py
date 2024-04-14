def befajl(nevek, magassagok):
    fr = open("adatok.txt", "r", encoding="UTF-8")
    sor = fr.readline().split(" ")
    while sor != [""]:
        nevek.append(sor[0])
        magassagok.append(int(sor[1].strip()))
        sor = fr.readline().split(" ")
    fr.close()
    return nevek, magassagok

def minindex(magassagok, k):
    index = k
    for i in range(k+1, len(magassagok)):
        if magassagok[i] < magassagok[index]:
            index = i
    return index

def rendez(nevek, magassagok):
    n = len(nevek)
    for i in range(n):
        j = minindex(magassagok, i)
        magassagok[i], magassagok[j] = magassagok[j], magassagok[i]
        nevek[i], nevek[j] = nevek[j], nevek[i]

def main():
    nevek, magassagok = [], []
    befajl(nevek, magassagok)
    rendez(nevek, magassagok)
    print(nevek, magassagok)
main()