gyumolcsok = ["alma", "banán", "körte", "szilva", "barack"]
ertekek = [6.8, 5.42, 7.5, 3.14, 6.7]

max = 0

for i in range(1, len(ertekek)):
    if ertekek[i] > ertekek[max]:
        max = i

print(f"Az ország kedvenc gyümölcse: {gyumolcsok[max]}")