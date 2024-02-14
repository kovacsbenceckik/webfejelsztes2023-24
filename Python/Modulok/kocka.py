from random import *

n = int(input("Dobások száma: "))
gy = [0, 0, 0, 0, 0, 0]
for i in range(n):
    r = randint(1, 6)
    gy[r-1] += 1
print(gy)