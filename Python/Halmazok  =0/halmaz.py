def eleme(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

def egyediek(lista):
    eredmeny = []
    for i in range(len(lista)):
        if not eleme(lista[i], eredmeny):
            eredmeny.append(lista[i])
    return eredmeny
    
def main():
    lista = [3, 5, 3, 3, 2, 5, 2, 3]
    halmaz = egyediek(lista)
    print(halmaz)
    
main()