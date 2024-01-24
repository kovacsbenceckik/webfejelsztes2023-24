n = int(input())
idok = []
for i in range(n):
    idok.append(int(input()))

lassuak = []

for i in range(n):
    if idok[i] > 120:
        lassuak.append(i)

if lassuak != []:
    mini = lassuak[0]
    for i in range(len(lassuak)):
        j = lassuak[i]
        if idok[j] < idok[mini]:
            mini = j
    print(mini+1, idok[mini])
else:
    print(-1)
