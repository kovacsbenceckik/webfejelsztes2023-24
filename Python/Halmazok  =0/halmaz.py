def eleme(elem, y):
    i = 0
    while i < len(y) and not(y[i] == elem):
        i += 1
    return i < len(y)

def egyediek(x):
    eredmeny = []
    for i in range(len(x)):
        if not eleme(x[i], eredmeny):
            eredmeny.append(x[i])
    return eredmeny
    
def main():
    lista = [3, 5, 3, 3, 2, 5, 2, 3]
    halmaz = egyediek(lista)
    print(halmaz)
    
main()