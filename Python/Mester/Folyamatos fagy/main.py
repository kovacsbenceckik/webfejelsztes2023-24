sor = input().split()
n = int(sor[0])
k = int(sor[1])
minimum = []
maximum = []

for i in range(n):
    sor = input().split()
    minimum.append(int(sor[0]))
    maximum.append(int(sor[1]))

i = 0
while i < n-1 and not(maximum[i] < 0 and maximum[i+1] < 0):
    i += 1
if i < n:
    print(i)