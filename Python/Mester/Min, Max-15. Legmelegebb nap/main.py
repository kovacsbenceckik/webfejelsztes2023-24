# Be
n = int(input())
homersekletek = []
for i in range(n):
    y = int(input())
    homersekletek.append(y)

# Feld - TUTUTUTU MAX VERSTAPPEN

maxi = 0
for i in range(1, n):
    if homersekletek[i] > homersekletek[maxi]:
        maxi = i
print(maxi+1)