#7
#1+3+5+7 = 16

n = int(input("pozitiv egesz szam: "))

osszeg = 0
# for i in range(n+1):
#     if i % 2 == 1:
#         osszeg += i
x = 1
while x <= n:
    osszeg += x
    x += 2

print(osszeg)