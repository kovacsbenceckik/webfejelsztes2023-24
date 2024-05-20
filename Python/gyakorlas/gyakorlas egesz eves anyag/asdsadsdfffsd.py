from random import randint

def betusor(betu1, betu2, betu3):
    betuk = ""
    for i in range(30):
        r = randint(1, 3)
        if r == 1:
            betuk += betu1
        elif r == 2:
            betuk += betu2
        elif r == 3:
            betuk += betu3
    print(betuk)
            


def main():
    betu1 = "x"
    betu2 = "5"
    betu3 = "?"
    betusor(betu1, betu2, betu3)
main()
    