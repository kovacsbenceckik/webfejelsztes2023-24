sor = input().split()
n = int(sor[0])
k = int(sor[1])
minimum = []
maximum = []

for i in range(n):
    sor = input().split()
    minimum.append(int(sor[0]))
    maximum.append(int(sor[1]))
db = 0

for i in range(n):
    if maximum[i] < 0:
        db += 1

utsonap = -1
streak = 0

i = 0

while streak != k and i < n:
    i += 1
    if maximum[i] < 0:
        streak += 1
        if streak == k:
            utsonap = i + 1
    else:
        streak = 0

print(db, utsonap)