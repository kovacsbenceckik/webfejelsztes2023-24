from random import randint

def befajl(hely, eso):
    fr = open("csapadek.txt", "r", encoding="UTF-8")
    sor = fr.readline()
    hanyadiksor = 0
    while sor != "":
        hanyadiksor += 1
        if hanyadiksor % 2 == 0:
            eso.append(int(sor.strip()))
        else:
            hely.append(sor.strip())
        sor = fr.readline()

def joslat(szam):
    r = randint(-3, 3)
    szam += r
    return szam

def kiir(eso, hely):
    fw = open("holnap.txt", "w", encoding="UTF-8")
    for i in range(len(eso)):    
        aktualis = joslat(eso[i])
        fw.writelines(f"{hely[i]} -> {aktualis}\n")
    fw.close()

def keres(hely, eso, randomvaros):
    i = 0
    while i < len(hely) and not (hely[i] == randomvaros):
        i += 1
    if i < len(hely):
        return eso[i]
    else:
        return -1

def f3(hely, eso):
    cegled = keres(hely, eso, "Cegléd")
    csemo = keres(hely, eso, "Csemő")
    if cegled == -1 or csemo == -1:
        print("3. Nem található Cegléd vagy Csemő!")
    elif csemo > cegled:
        print("3. Csemőben több esett!")
    elif cegled > csemo:
        print("3. Cegléden több esett!")
    else:
        print("3. Ugyanannyi esett Cegléden és Csemőben!")

def main():
    hely, eso = [], []
    befajl(hely, eso)
    kiir(eso, hely)
    f3(hely, eso)
main()