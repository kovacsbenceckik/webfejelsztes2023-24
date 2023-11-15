p = int(input("p: "))

db = 0
i = 1
while i <= p and db <= 2:
 if p % i == 0:
     db += 1
     i += 1

# print("Osztók száma:", db)
if db == 2:
    print("Prím!!!")
else:
    print("nem prím")