def beFajl(cimek, ertekelesek):
    fr = open("filmek.csv", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        adatok = sor.split(";")
        cimek.append(adatok[0])
        ertekelesek.append(float(adatok[1]))
        sor = fr.readline().strip()
    fr.close()

# Megadja a legjobb értékelésű film címét.
def legjobb(cimek, ertekelesek):
    maxi = 0
    for i in range(1, len(ertekelesek)):
        if ertekelesek[i] > ertekelesek[maxi]:
            maxi = i
    return cimek[maxi]

def main():
    cimek, ertekelesek = [], []
    beFajl(cimek, ertekelesek)
    legjobbfilm = legjobb(cimek, ertekelesek)
    print("A legjobb értékelésű film:", legjobbfilm)
    
main()