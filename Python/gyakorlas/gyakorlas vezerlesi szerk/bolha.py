n = int(input("Bolha: "))

aktualis = n

while aktualis != 0:
    print(aktualis, end=" -> ")
    aktualis *= -1
    maradek = aktualis % 10
    if maradek == 0:
        maradek = 10
    if aktualis > 0:
        aktualis -= maradek
    else:
        aktualis += maradek

print(aktualis, end="")