import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    whire1 = f.readline().strip().split(',')
    whire2 = f.readline().strip().split(',')


#whire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#whire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

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

def count_steps(wc1, wc2, inter):
    steps = []
    for step1, coor1 in enumerate(wc1, start=1):
        if coor1 in inter:
            for step2, coor2 in enumerate(wc2, start=1):
                if coor2 == coor1:
                    steps.append(step1+step2)
    return min(steps)

whire1_coordinates = create_coordinates(whire1)
whire2_coordinates = create_coordinates(whire2)
intersections = find_intersections(whire1_coordinates, whire2_coordinates)
steps = count_steps(whire1_coordinates, whire2_coordinates, intersections)

#print(whire1_coordinates, '\n', whire2_coordinates)
#print(intersections)
#print(find_lower_intersection(intersections))
print('STEPS: ', steps)