import os
import math
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    arr = []
    line = f.readline().strip()
    while line:
        arr.append(line)
        line = f.readline().strip()

def calcular(mass):
    try:
        return (int(mass) // 3) - 2
    except:
        pass
    

suma = sum(list(map(calcular, arr)))
print(suma)
