# irasd ki minden elem ketszereset

lista = [5, 3, 7, 4, 12, -9, 31, 7]

n = len(lista)
# print("F3: ", end="")
# for i in range(n):
#     print(2*lista[i], end=" ")


'''
írasd ki a 3-mal osztható elemeket!-
'''

# kimenet: F5: 2 12 -9
print("F5: ", end="")
for i in range(n):
    if lista[i] % 3 == 0:
        print(lista[i], end=" ")