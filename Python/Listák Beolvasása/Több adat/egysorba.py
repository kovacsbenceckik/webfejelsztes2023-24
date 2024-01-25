n = int(input())
nevek = []
darabszam = []

for i in range(n):
    sor = input().split()
    nevek.append(sor[0])
    darabszam.append(int(sor[1]))

print("gyümölcsök:", nevek)
print("mennyiségek:", darabszam)