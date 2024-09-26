
import random
import os
import time

#print ("\n" * 50)
os.system("cls")

n = int(input("Informe um número inteiro positivo: "))

while n > 0:
    #os.system("cls")
    dezena = int(random.random() * 60)
    print(f"Dezena {n} ___ {dezena}")
    time.sleep(1)
    n -= 1



