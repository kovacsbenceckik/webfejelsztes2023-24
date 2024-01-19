n = int(input())
k  =int(input())
menetidok = []
for i in range(n):
    ido = int(input())
    menetidok.append(ido)

# Feldolgozas - kivalogatas tetel
megoldasok = []
for i in range(n):
    if menetidok[i] < k:
        megoldasok.append(i+1)

# Kiiras
print(len(megoldasok), end=" ")
for i in range(len(megoldasok)):
    print(megoldasok[i], end=" ")
