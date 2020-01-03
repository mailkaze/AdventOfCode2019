import os
from secret import path as path

os.chdir(path)
arr = []
with open('input.txt', 'r') as f:
    arr = f.read().strip().split(',')

arr = list(map(int, arr))
arr[1] = 12
arr[2] = 2

code = 0
i = 0
while True:
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

print(arr[0])