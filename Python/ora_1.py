# n = int(input("n: "))

# print("Osztók: ", end="")

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=" ")

# n = int(input("n: "))

# i = 2

# while i < n and n % i != 0 and n != 1:
#     i += 1
# if i < n or n == 1:
#     print("Nem prím!")
# else:
#     print("Prím!")

ora = 8
perc = 0

while ora < 18:
    print(f"{f'0{ora}' if ora < 10 else str(ora)}:{f'0{perc}' if perc < 10 else str(perc)}")
    perc += 25
    if perc >= 60:
        ora += 1
        perc -= 60
print("18:00")