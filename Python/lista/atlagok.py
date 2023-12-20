lista = [5, 3, 7, 4, 12, -9, 31, 7]
n = len(lista)

'''
8. Írasd ki a szomszédos elemek átlagait!
'''
# Kimenet:
# F8: 4.0 5.0 5.5 8.0 1.5 11.0 19.0
print("F8:", end=" ")
for i in range(n-1):
    atlag = (lista[i] + lista[i+1]) / 2
    print(atlag, end=" ")
print()

# print("F8:", end=" ")
# for i in range(1, n):
#     atlag = (lista[i] + lista[i-1]) / 2
#     print(atlag, end=" ")
# print()

# print("F_G:", end=" ")
# for i in range(n-2):
#     atlag = (lista[i] + lista[i+2]) / 2
#     print(atlag, end=" ")
# print()

'''
9. Írasd ki az elemek összegét!
'''
# lista = [5, 3, 7, 4, 12, -9, 31, 7]
# Kimenet:
# F9: 60
s = 0
for i in range(n):
    s += lista[i]
print("F9:", s)
