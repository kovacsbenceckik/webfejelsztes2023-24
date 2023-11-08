suly = float(input("Hány kg a csomag? "))
tav = float(input("Hány km-re kell vinni a csomagot? "))

if suly < 5 and tav < 500:
    dij = 20
elif suly < 5 and tav >= 500:
    dij = 35
elif suly >= 5 and tav < 500:
    dij = 30
else:
    dij = 50

print(f"A csomagszállítás díja $", dij)