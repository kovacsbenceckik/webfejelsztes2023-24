from random import randint

def csere(x, i, j):
    seged = x[i]
    x[i] = x[j]
    x[j] = seged

def minindex(x, k):
    index = k
    for i in range(k+1, len(x)):
        if x[i] < x[index]:
            index = i
    return index

def maxindex(x, k):
    index = k
    for i in range(k+1, len(x)):
        if x[i] > x[index]:
            index = i
    return index

def rendezes(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

def feltolt(n):
    x = []
    for i in range(n):
        r = randint(1, 600)
        x.append(r)
    return x
def main():
    x = feltolt(100)
    print("Eredeti:", x)
    rendezes(x)
    print("Rendezett:", x)
main() 