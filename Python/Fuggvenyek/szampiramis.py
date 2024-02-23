def main():
    n = int(input("Sorok száma: "))
    for i in range(1, n+1):
        sor(i)    


def sor(n):
    for i in range(1, n+1):
        print(i, end=" ")
    print()

main()