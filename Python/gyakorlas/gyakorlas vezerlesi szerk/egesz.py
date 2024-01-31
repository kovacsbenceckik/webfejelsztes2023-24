a = int(input("a: "))

aktualis = a
paros = 0

for i in range(40):
    if aktualis % 2 == 0:
        paros += 1
    aktualis = (aktualis * 3) % 7 
    print(aktualis, end=" ")

paros /= 40
paros *= 100
print(f"\nblablabla", round(paros, 2))