def iras(nev):
    fw = open("nevek.txt", "a", encoding="UTF-8")
    fw.write(f"{nev}\n")
    
    fw.close()

def main():
    nev = input("Név:")
    iras(nev)


main()