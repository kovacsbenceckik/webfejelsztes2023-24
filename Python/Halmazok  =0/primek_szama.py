def primE(n):
    if n == 1:
        return False
    i = 2
    while i < n and not (n % i == 0):
        i += 1
    # if i < n:
    #     return False
    # else:
    #     return True
    return not(i < n) and n != 1

def primekSzama(x):
    db = 0
    for i in range(len(x)):
        if primE(x[i]):
            db += 1
    return db

def main():
    x = [5, 3, 2, 8, 1]
    db = primekSzama(x)
    print("Prímek száma:", db)

main()