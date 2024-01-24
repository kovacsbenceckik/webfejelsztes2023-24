n = int(input())

bevetel = []

for i in range(n):
    be = int(input())
    bevetel.append(be)

eddigi = 0
asdf = 0
for i in range(n):
    if bevetel[i] > eddigi:
        asdf += 1
        eddigi = bevetel[i]
print(asdf)
