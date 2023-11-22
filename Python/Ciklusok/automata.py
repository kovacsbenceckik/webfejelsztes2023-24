ar = 1670
egesz = int(input("Add meg az összeget: "))

visszajaro = egesz - ar
hiany = ar - egesz

if egesz == ar:
    print ("Sikeres vásárlás! Nincs visszajáró.")
elif egesz > ar:
    print (f"Sikeres vásárlás! Visszajáró: {visszajaro}Ft.")
else:
    print(f"Sikertelen vásárlás! Hiányzik {hiany}Ft.") 