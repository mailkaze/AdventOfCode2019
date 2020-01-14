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

def orbits_chain(origin, orbits):
    chain = []
    for orbit in orbits:
        if orbit[1] == origin:
            a = orbit[0]
            chain.append(a)
    while a != 'COM':
        for search in orbits:
            if search[1] == a:
                chain.append(a)
                a = search[0]
    return chain

def count_transfers(origin, orbits, common_orbit):
    transfers = 0

    for orbit in orbits:
        if orbit[1] == origin:
            a = orbit[0]
            transfers += 1
    while a != common_orbit:
        for search in orbits:
            if search[1] == a:
                transfers += 1
                a = search[0]
    return transfers

my_orbit = ''
santas_orbit = ''
for orbit in orbits:
    if orbit[1] == 'YOU':
        my_orbit = orbit[0]
    elif orbit[1] == 'SAN':
        santas_orbit = orbit[0]

my_chain = orbits_chain(my_orbit, orbits)
santas_chain = orbits_chain(santas_orbit, orbits)

for i in my_chain:
    if i in santas_chain:
        common_orbit = i
        break

my_transfers = count_transfers(my_orbit, orbits, common_orbit)
santas_transfers = count_transfers(santas_orbit, orbits, common_orbit)
print(my_transfers + santas_transfers)
