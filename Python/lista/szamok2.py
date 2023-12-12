'''
3. Írasd ki minden elem kétszeresét!
'''
# Kimenet:
# F3: 10 6 14 8 24 -18 62 14
lista = [5, 3, 7, 4, 12, -9, 31, 7]
n = len(lista) # 8
print(lista)

print("F3:", end=" ")
for i in range(n):
    print(2*lista[i], end=" ")
print()

'''
4. Írasd ki minden második elemet!
'''
# Kimenet:
# F4: 3 4 -9 7
# print("F4:", end=" ")
# for i in range(1, n, 2):
#     print(lista[i], end=" ")

# MO2 (Gábor)
print("F4:", end=" ")
for i in range(n):
    if i % 2 == 1:
        print(lista[i], end=" ")
print()

'''
5. Írasd ki a 3-mal osztható elemeket!
'''
# Kimenet:
# F5: 3 12 -9
print("F5:", end=" ")
for i in range(n):
    aktualis = lista[i]
    if aktualis % 3 == 0:
        print(aktualis, end=" ")
print()

'''
6. Írasd ki az elemeket
fordított sorrendben!
'''
# Kimenet:
# F6: 7 31 -9 12 4 7 3 5
# print("F6:", end=" ")
# for i in range(n-1, -1, -1):
#     print(lista[i], end=" ")
# print()

# MO2
print("F6:", end=" ")
for i in range(n, 0, -1):
    print(lista[i-1], end=" ")
print()

# MO3 (Máriusz)
# print("F6:", end=" ")
# for i in range(n):
#     print(lista[n-i-1], end=" ")
# print()

# MO4 (python)
# print("F6:", end=" ")
# for i in range(n):
#     print(lista[-i-1], end=" ")
# print()

'''
7. Írd ki az elemeket, de
mindegyiket növeld meg az
indexének értékével!
'''
# lista = [5, 3, 7, 4, 12, -9, 31, 7]
# Kimenet:
# F7: 5 4 9 7 16 -4 37 14
print("F7:", end=" ")
for i in range(n):
    print(lista[i]+i, end=" ")
print()