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

def ujversenyzo():
    


def main():
    nevek, pontok = [], []
    maxpont = befajl(nevek, pontok)
    ujversenyzo()
main()