n = int(input())

tea = []
ar = []
for i in range(n):
    tea.append(input())
    ar.append(int(input()))
    
eladas = 0
for i in range(n):
    if tea[i] == tea[0]:
        eladas += ar[i]
print(eladas)