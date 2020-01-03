import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    array = f.read().strip().split(',')

array = list(map(int, array))

def calcular(arr, j, k):
    i = 0
    while True:
        arr[1] = j
        arr[2] = k
        code = arr[i]
        pos1 = arr[i+1]
        pos2 = arr[i+2]
        pos3 = arr[i+3]
        if code == 1:
            arr[pos3] = arr[pos1] + arr[pos2]
        elif code == 2:
            arr[pos3] = arr[pos1] * arr[pos2]
        elif code == 99:
            break
        i += 4
    return arr

fin = False
for j in range(100):
    for k in range(100):
        temp_arr = array[:]
        temp_arr = calcular(temp_arr, j, k)
        if temp_arr[0] == 19690720:
            fin = True
            break
    if fin:
        break
ans = 100 * temp_arr[1] + temp_arr[2]
print(ans)