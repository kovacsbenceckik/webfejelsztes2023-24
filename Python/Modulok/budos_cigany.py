#ermet 100x feldobjkuk aztan I vagy F-et kene kapni de ugyse
from random import *
ik = 0
fk = 0
for i in range(100):
    r = randint(1,2)
    if r == 1:
        print("I", end=" ")
        ik += 1
    else:
        print("F", end=" ")
        fk += 1
print()
print(f"I-k száma: {ik}")
print(f"F-k száma: {fk}")
