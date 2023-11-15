#Bemenet: a, k (egész számok)
#Kimenet: a-nak a k-adik hatványa
a = float(input("szam: "))
k = int(input("hatvany: "))

hatvany = 1
i = 1
#  for i in range(k):
while i <= k:
    hatvany *= a
    print(hatvany)
    i += 1

print("Hatvány: ", hatvany)