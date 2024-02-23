def sor(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            print(a, end=" ")
        else:
            print(b, end=" ")
    print()

def sakktabla(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            sor(n, "c", "i")
        else: 
            sor(n, "i", "c")


def main():
    n = int(input("Sorok száma: "))
    sakktabla(n, 1, 2)
        
main()