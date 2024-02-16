# Jelölés
# def osszeg(lista: list[int]) -> int :
def osszeg(lista):
    n = len(lista)
    s = 0
    for i in range(n):
        s += lista[i]
    return s

def osszeg2(*lista):
    n = len(lista)
    s = 0
    for i in range(n):
        s += lista[i]
    return s

print(osszeg([5, 2, -7, 12, 2])) # 14
print(osszeg([5, -2, 8])) # 11
print(osszeg([])) # 0
print(osszeg([13, 88])) # 101
print(osszeg([7])) # 7

print(osszeg2(3, -1, 11, -10))
# print(osszeg(5)) # 5
# print(osszeg(5, 7)) # 12♪