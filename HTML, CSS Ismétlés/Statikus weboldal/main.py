from random import randint

def szelesseg():
    r = randint(50, 70)
    while r % 2 != 0:
        r = randint(50, 70)
    return r

def szinek_valasztasa():
    r = randint(0, 255)
    list = []
    for i in range(5):
        list.append(r)
        r = randint(0, 255)

    mini = 0    
    for i in range=(len(list)):
        if list[i] > list[mini]:
            mini = i
    return list

def main():
    print("1.feladat")
    szazalek = szelesseg()
    print(f"width: {szazalek}%;")
    print("2. feladat")
    print(f"A választott kék szín: ")

main()