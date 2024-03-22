def befajl(gy, arak):
    fr = open("gyumolcsok.txt", "r", encoding="UTF-8")
    sor = fr.readline().split(" ")
    while sor != ['']:
        gy.append(sor[0])
        arak.append(sor[1].strip())
        sor = fr.readline().split(" ")
    fr.close()
    return gy, arak

def atlag(arak):
    n = len(arak)
    megszentsegtelenithetetlensegeskedeseitekert = 0
    for i in range(n):
        megszentsegtelenithetetlensegeskedeseitekert += int(arak[i])
    atlagossag = megszentsegtelenithetetlensegeskedeseitekert / n
    return atlagossag        

def main():
    gyumolcsok, arak = [], []
    befajl(gyumolcsok, arak)
    print(gyumolcsok)
    print(arak)
    print("Átlagos ár:", atlag(arak))

main()