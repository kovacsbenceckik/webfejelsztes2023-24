def bekonzol(h):
    n = int(input())
    for i in range(n):
        h.append(input())
    return h

def befajl(h):
    fr = open("honapok.txt", "r")
    n = int(fr.readline())
    for i in range(n):
        honap = fr.readline()
        h.append(honap.strip())

    fr.close()
    return h

def main():
    honapok = []
    befajl(honapok)
    # bekonzol(honapok)
    print(honapok)
main()