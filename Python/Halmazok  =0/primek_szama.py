def primE(n):
    i = 2
    while i < n and not (n % i == 0):
        i += 1
    # if i < n:
    #     return False
    # else:
    #     return True
    return not(i < n)

# def primekSzama(x):


def main():
    x = [5, 3, 2, 8, 1]
    db = primekSzama(x)
    print("Párosak száma:", db)

main()