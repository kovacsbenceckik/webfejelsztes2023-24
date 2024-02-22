def beolvasas(szinek):
    n = int(input())
    for i in range(n):
        szinek.append(input())
    return n

def legrovidebb(szinek):
    min = 0
    for i in range(1, len(szinek)):
        if len(szinek[i]) < len(szinek[min]):
            min = i
    return szinek[min]

def kiiras(szin):
    print("A legrövidebb nevű szín:", szin)

szinek = []
beolvasas(szinek)
legrovidebb_szin = legrovidebb(szinek)
kiiras(legrovidebb_szin)