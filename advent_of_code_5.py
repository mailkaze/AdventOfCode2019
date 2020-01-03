import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    whire1 = f.readline().strip().split(',')
    whire2 = f.readline().strip().split(',')

def create_coordinates(whire):
    whire_coordinates = []
    x, y = 0, 0
    for vector in whire:
        direction = vector[0]
        distance = int(vector[1:])
        if direction is 'U':
            for _ in range(distance):
                y += 1
                whire_coordinates.append((x, y))
        elif direction is 'D':
            for _ in range(distance):
                y -= 1
                whire_coordinates.append((x, y))
        elif direction is 'L':
            for _ in range(distance):
                x -= 1
                whire_coordinates.append((x, y))
        elif direction is 'R':
            for _ in range(distance):
                x += 1
                whire_coordinates.append((x, y))
    return whire_coordinates

def find_intersections(wc1, wc2):
    intersections = list(set(wc1).intersection(wc2)) 
    return intersections

def find_lower_intersection(inter):
    #sumar las coordinadas como si ambas fueran números positivos
    sums = []
    for coor in inter:
        sums.append(abs(coor[0]) + abs(coor[1]))
    return min(sums)

whire1_coordinates = create_coordinates(whire1)
whire2_coordinates = create_coordinates(whire2)
intersections = find_intersections(whire1_coordinates, whire2_coordinates)

print(find_lower_intersection(intersections))