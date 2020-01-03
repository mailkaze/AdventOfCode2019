import os

os.chdir('C:\\Users\\Restaurante\\Downloads\\DEV\\ejercicios')
arr = []
with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        arr.append(line)
        line = f.readline().strip()

def calcular(mass, fuel):
    ans = (int(mass) // 3) - 2
    if ans <= 0:
        return fuel
    fuel += ans
    return calcular(ans, fuel)

#answer = sum(list(map(calcular, arr)))
total_fuel = 0
for mass in arr:
    fuel = 0
    fuel = calcular(mass, fuel)
    total_fuel += fuel

print(total_fuel)