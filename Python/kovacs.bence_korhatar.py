eletkor1 = int(input("1. vendég: "))
eletkor2 = int(input("2. vendég: "))

if eletkor1 >= 18 and eletkor2 >= 18:
    print("Máris hozom amit kértek!")
elif eletkor1 < 18 and eletkor2 >= 18:
    osszegzes = eletkor2
elif eletkor1 >= 18 and eletkor2 < 18:
    osszegzes = eletkor1
else:
    print("Sajnos egyiküket sem szolgálhatom ki!")

if osszegzes == eletkor1 or osszegzes == eletkor2:
    print(f"Csak a {osszegzes} éves vendéget szolgálhatom ki !")

    