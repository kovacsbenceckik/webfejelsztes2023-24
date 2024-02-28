def parosE(n):
    return n % 2 == 0


def parosakSzama(x):
    db = 0
    for i in range(len(x)):
        if parosE(x[i]):
            db += 1
    return db

def main():
    x = [5, 3, 2, 8, 1]
    db = parosakSzama(x)
    print("Párosak száma:", db)

main()