def befajl(nevek, magassagok):
    cigany = open("wow.txt", "r", encoding="UTF-8")
    sor = cigany.readline().split(" ")
    while sor != [""]:
        nevek.append(sor[0])
        magassagok.append(int(sor[1].strip()))
        sor = cigany.readline().split(" ")
    cigany.close()

def rendezes(nevek, magassagok):
    n = len(magassagok)
    for i in range(n):
        for j in range(i + 1, n):
            if magassagok[i] > magassagok[j]:
                x = nevek[i]
                y = magassagok[i]
                magassagok[i] = magassagok[j]
                nevek[i] = nevek[j]
                nevek[j] = x
                magassagok[j] = y

def kifajl(nevek, magassagok):
    fw = open("eredmeny.txt", "w", encoding="UTF-8")
    i = 0
    while i < len(nevek):
        fw.write(f"{nevek[i]} {magassagok[i]}")
        i += 1

def main():
    nevek = []
    magassagok = []
    befajl(nevek, magassagok)
    rendezes(nevek, magassagok)
    kifajl(nevek, magassagok)
    # print(nevek)
    # print(magassagok)
main()