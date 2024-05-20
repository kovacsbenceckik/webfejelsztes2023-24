# F1
n = int(input())
nevek, perc, gyakorisag = [], [], []
for i in range(n):
    sor = input().split()
    nevek.append(sor[0])
    perc.append(int(sor[1]))
    gyakorisag.append(int(sor[2]))
    
# F2
tiznelrovidebb = []
for i in range(n):
    if perc[i] < 10:
        tiznelrovidebb.append(nevek[i])
print(len(tiznelrovidebb), end=" ")
for i in range(len(tiznelrovidebb)):
    print(tiznelrovidebb[i], end=" ")

print()
# F3
i = 0
while i < n and perc[i] * gyakorisag[i] < 120:
    i += 1
if i < n:
    print(nevek[i])
else:
    print(-1)

# F4
maxi = 0
for i in range(n):
    if perc[i] < 60 and perc[i] > perc[maxi]:
        maxi = i

print(nevek[maxi])        


# F5
