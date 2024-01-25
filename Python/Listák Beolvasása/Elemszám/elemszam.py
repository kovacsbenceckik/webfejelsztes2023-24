n = int(input("n: "))
szamok = []
for i in range(n):
    bemenet = int(input("Nemzeti Adó- és Vámhivatal kér Öntől számadót:"))
    szamok.append(bemenet)
print(szamok)

#Összeg
s = 0
for i in range(n):
    s += szamok[i]
print("Számok összege:", s)

#negyzetek
negyzetek = []
for i in range(n):
    negyzetek.append(szamok[i]*szamok[i])
print("Számok négyzetei:", negyzetek)