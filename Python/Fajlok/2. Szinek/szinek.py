def befajl(sz):
    fr = open("szinek.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        sz.append(sor)
        sor = fr.readline().strip()
    fr.close()
    return sz

def koncsik_egy_cigany_dani_is_szilard_csak_siman_cigo():
    szinek = []
    befajl(szinek)
    print(szinek)

koncsik_egy_cigany_dani_is_szilard_csak_siman_cigo()