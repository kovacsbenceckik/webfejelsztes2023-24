n = int(input("Bolha: "))
print(f"{n} -> ", end="")
while n != 0:
    n *= -1
    maradek = n % 10
    if maradek == 0:
        maradek = 10
    if n < 0:
         n += maradek
    else:  
        n -= maradek

    if n != 0:
        print(f"{n} -> ", end="")
print('0')