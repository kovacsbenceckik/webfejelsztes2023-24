from random import randint

def osztalyozas():
    fw = open("naplo.txt", "w", encoding="UTF-8")
    for i in range(16):
        r = randint(1, 5)
        fw.write(r)
    fw.close()

def main():
    osztalyozas()
    
main()