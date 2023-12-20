ar = 1670
egesz = int(input("Add meg az összeget: "))

visszajaro = egesz - ar

if egesz > ar:
    print(f"Sikeres vásárlás! Visszajáró: {visszajaro}Ft.")
elif egesz < ar:
    print(f"Sikertelen vásárlás! Hiányzik: {-(visszajaro)}Ft.")
else:
    print("Sikeres vásárlás! Nincs visszajáró!")