def befajl(nevek, korok):
    fr = open("nevek.txt", "r", encoding="UTF-8")
    sor = fr.readline().split(" ")
    
    while sor != [""]:
        nevek.append(sor[0])
        korok.append(int(sor[1].strip()))
        sor = fr.readline().split(" ")
    fr.close()

# def rendez(nevek, korok):







# def kifajl(nevek, korok):






def main():
    nevek, korok = [], []
    befajl(nevek, korok)
    # rendez(nevek, korok)
    # kifajl(nevek, korok)

main()