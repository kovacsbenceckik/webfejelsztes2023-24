from time import time, sleep
# print("ido:", time())
# print("random ", int(time() * 100) % 100)

for i in range(40):
    ido = time()
    r = int(ido * 10000) % 10
    print(r, end=" ")
    sleep(0.001)
