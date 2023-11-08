#Beolvasás
x = float(input("x értéke "))
y = float(input("y értéke "))

# feldolgozás
if x > 0 and y > 0:
    sn = 1
elif x > 0 and y < 0:
    sn = 4
elif x < 0 and y < 0:
    sn = 3
else:
    sn =2

#kiírás
print(f"A megadott pont a(z) {sn}. siknegyedben van!")