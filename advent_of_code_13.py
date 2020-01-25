import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    intcode = list(map(int, f.readline().strip().split(',')))

max_output = 0
def opcode_parameter_mode_extractor(instruction):
    opcode = 0
    parameter_modes =[0,0,0,0,0,0,0,0,0,0]
    if instruction < 100:
        opcode = instruction
    else:
        opcode = int(str(instruction)[-2:])
        param = list(str(instruction)[:-2])
        param.reverse()
        for i in range(len(param)):
            parameter_modes[i] = int(param[i])
    return opcode, parameter_modes


def solve_intcode(intcopy, phase, input_signal):
    opcode = 0
    i = 0
    input_value = phase
    while opcode != 99:
        # extraer el opcode y los parameter modes:
        opcode, parameter_modes = opcode_parameter_mode_extractor(intcopy[i])
        # dar valor a los parámetros y ejecutar la operación correspondiente al opcode:
        if opcode == 1:
            # sumar:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            intcopy[intcopy[i+3]] = para1 + para2
            i += 4
        elif opcode == 2:
            # multiplicar:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            intcopy[intcopy[i+3]] = para1 * para2
            i += 4
        elif opcode == 3:
            # guardar un input:
            intcopy[intcopy[i+1]] = input_value
            #la primera vez que pide un input es el phase configuration y la segunda es el input signal.
            input_value = input_signal
            i += 2
        elif opcode == 4:
            # devolver un output:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]] 
            #print(para1)
            i += 2
            return para1
        elif opcode == 5:
            # saltar si es True:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            if para1 != 0:
                i = para2 
            else:
                i += 3
        elif opcode == 6:
            # saltar si es False:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            if para1 == 0:
                i = para2 
            else:
                i += 3
        elif opcode == 7:
            # menor que:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            intcopy[intcopy[i+3]] = 1 if para1 < para2 else 0
            i += 4
        elif opcode == 8:
            # igual a:
            para1 = intcopy[i+1] if parameter_modes[0] == 1 else intcopy[intcopy[i+1]]
            para2 = intcopy[i+2] if parameter_modes[1] == 1 else intcopy[intcopy[i+2]]
            intcopy[intcopy[i+3]] = 1 if para1 == para2 else 0
            i += 4

def permutation(lst):
    # NOT MINE:
    # Si la lista está vacía:
    if len(lst) == 0: 
        return [] 
    # Si la lista solo tiene un elemento:
    if len(lst) == 1: 
        return [lst] 

    l = [] 
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
       # Extract lst[i] or m from the list.  remLst is remaining list 
       remLst = lst[:i] + lst[i+1:] 
       # Generating all permutations where m is first element 
       for p in permutation(remLst): 
           l.append([m] + p)

    return l


convinations = permutation([0,1,2,3,4])
# Una vuelta por cada conjunto de permutación
for convination in convinations:
    #aqui llama 5 veces a la función y el output de cada una es el input de la siguiente:
    input_signal = 0
    for phase in convination:
        intcode_copy = intcode.copy()
        input_signal = solve_intcode(intcode_copy, phase, input_signal)
    if input_signal > max_output:
        max_output = input_signal

print(max_output)