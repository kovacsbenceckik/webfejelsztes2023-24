n = int(input("n: "))

fakt =1
for i in range(n, 0, -2):
    fakt *= i

print("n!! =", fakt)