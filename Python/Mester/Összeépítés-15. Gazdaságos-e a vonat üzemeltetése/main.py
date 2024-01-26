n = int(input())
helyezes = []
perc = []
masodperc = []

for i in range(n):
    sor = input().split()
    hely = int(sor[0])
    minut = int(sor[1])
    sec = int(sor[2])
    helyezes.append(hely)
    perc.append(minut)
    masodperc.append(sec)