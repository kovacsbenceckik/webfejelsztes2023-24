p = int(input("p: "))

db = 0
for i in range(1, p+1):
    if p % i == 0:
        db += 1

# print("Osztók száma:", db)
if db == 2:
    print("Prím!!!")
else:
    print("nem prím")