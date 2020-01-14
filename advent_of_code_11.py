import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    orbits = []
    line = f.readline().strip()
    while line:
        orbit = str(line).split(")")
        orbits.append(orbit)
        line = f.readline().strip()

direct = len(orbits)
indirect = 0

def count_indirects(orbits, orbit):
    a = orbit[0]
    b = orbit[1]
    count = 0
    while a != 'COM':
        for search in orbits:
            if search[1] == a:
                count += 1
                a = search[0]
    return count

for orbit in orbits:
    indirect += count_indirects(orbits, orbit)

    
print (direct + indirect)
