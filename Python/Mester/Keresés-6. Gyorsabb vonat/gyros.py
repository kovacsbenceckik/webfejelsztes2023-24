n = int(input())

violinvonat = []

for i in range(n):
    y = int(input())
    violinvonat.append(y)    


i = 1
while i < n and not(violinvonat[i] < violinvonat[i-1]):
    i += 1
if i < n:
    print(i+1)