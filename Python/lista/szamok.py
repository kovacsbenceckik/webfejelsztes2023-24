# Adott egy egész számokból álló lista:
lista = [5, 3, 7, 4, 12, -9, 31, 7]
hossz = len(lista)

'''
1. Írasd ki a lista elemeit 
egymás mellé szóközzel elválasztva!
'''
# Kimenet:
# F1: 5 3 7 4 12 -9 31 7
print("F1:", end=" ")
# MO1 (Zalán)
# i = 0
# while i < hossz:
#     print(lista[i], end=" ")
#     i += 1

# MO2 (Gábor)
for i in range(hossz):
    print(lista[i], end=" ")
print()

# MO3 (t_fnorbi)
# for elem in lista:
#     print(elem, end=" ")

# MO4 (python)
# print(*lista)



'''
2. Írasd ki az elemeket pontosvesszővel
és szóközzel elválasztva! Az utolsó
elem után ne legyen már pontosvessző!
'''
# Kimenet:
# F2: 5; 3; 7; 4; 12; -9; 31; 7

# MO1
# print("F2:", end=" ")
# for i in range(hossz):
#     if i == hossz-1:
#         print(lista[i])
#     else:
#         print(lista[i], end="; ")

# MO2
print("F2:", end=" ")
for i in range(hossz-1):
    print(lista[i], end="; ")
print(lista[hossz-1])
