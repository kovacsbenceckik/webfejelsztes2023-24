a = int(input("a: "))

paros = 0

for i in range(0, 40):
    if a % 2 == 0:
        paros += 1
    print(a, end=" ")
    a *= 3
    a = a % 7

szazalek = paros / 0.4
print(f"\nA tagok {szazalek} %-a páros.")