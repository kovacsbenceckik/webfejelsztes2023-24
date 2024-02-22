n = int(input())
szinek = []

for i in range(n):
    szinek.append(input())
min = 0
for i in range(n):
    if len(szinek[i]) < len(szinek[min]):
        min = i
print(szinek[min])