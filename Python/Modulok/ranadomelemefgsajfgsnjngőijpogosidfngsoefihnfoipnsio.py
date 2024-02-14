from random import *

x = ["kebab", "processzor", "gyros", "Mjölnir", "Vivaldi", "RTX 3060 12GB GDDR6", "Elvonó"]

n = len(x)
db = 0
for i in range(20):
    r = randint(1, n-1)
    db += 1
    print(db, x[r-1])