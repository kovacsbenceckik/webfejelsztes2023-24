n = int(input())
nappaliak = []
estiek = []

for i in range(n):
    sor = input().split()
    nappali = int(sor[0])
    esti = int(sor[1])
    nappaliak.append(nappali)
    estiek.append(esti)
print(nappaliak, estiek)