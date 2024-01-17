x = [5, 1, 2, -6, 7, 7, 16, 2, 2, 32, -3, 5, 6]
n = len(x)

# F1 - Másolás tétel
# Másold át az elemeket egy másik listába!
y = []
for i in range(n):
    y.append(x[i])
print("1. Másolt lista:", y)

# F2
# Másold át az elemek négyzeteit egy másik listába!
negyzetek = []
for i in range(n):
    negyzetek.append(x[i]*x[i])
print("Négyzetes lista:", negyzetek)

# F3
# Válogasd ki a 10 alatti elemeket egy másik listába!
i = 0
tizalatti = []
for i in range(n):
    if x[i] < 10:
        tizalatti.append(x[i])
print("Tíz alattiak:", tizalatti)

# F4
# Válogasd ki a negatív elemek indexeit egy másik listába!
negativ = []
for i in range(n):
    if x[i] < 0:
        negativ.append(i)
print("Negatív számok indexei:", negativ)

ertekek = []
m = len(negativ)
for i in range(m):
    index = negativ[i]
    ertekek.append(x[index])
print("Negatív számok:", ertekek)
# F5
# Válogasd szét a páros és a páratlan elemeket!
paros = []
paratlan = []
for i in range(n):
    if x[i] % 2 == 0:
        paros.append(x[i])
    else:
        paratlan.append(x[i])
print("Páros számok:", paros)
print("Páratlan számok:", paratlan)