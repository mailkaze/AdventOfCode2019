import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    intcode = list(map(int, f.readline().strip().split(',')))

# el programa empieza pidiendo el ID del ordenador, este es 5.
ID = 5
# el último output será el diagnostico del TEST.

def opcode_parameter_mode_extractor(instruction):
    opcode = 0
    parameter_modes =[0,0,0,0,0,0,0,0,0,0]
    if instruction < 100:
        opcode = instruction
    else:
        opcode = int(str(instruction)[-2:])
        # TODO asignar los parameter modes
        param = list(str(instruction)[:-2])
        param.reverse()
        for i in range(len(param)):
            parameter_modes[i] = int(param[i])
    return opcode, parameter_modes

opcode = 0
i = 0
while opcode != 99:
    # extraer el opcode y los parameter modes:
    opcode, parameter_modes = opcode_parameter_mode_extractor(intcode[i])
    # dar valor a los parámetros y ejecutar la operación correspondiente al opcode:
    if opcode == 1:
        # sumar:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        intcode[intcode[i+3]] = para1 + para2
        i += 4
    elif opcode == 2:
        # multiplicar:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        intcode[intcode[i+3]] = para1 * para2
        i += 4
    elif opcode == 3:
        # guardar un input:
        intcode[intcode[i+1]] = ID
        i += 2
    elif opcode == 4:
        # devolver un output:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]] 
        print(para1)
        i += 2
    elif opcode == 5:
        # saltar si es True:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        if para1 != 0:
            i = para2 
        else:
            i += 3
    elif opcode == 6:
        # saltar si es False:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        if para1 == 0:
            i = para2 
        else:
            i += 3
    elif opcode == 7:
        # menor que:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        intcode[intcode[i+3]] = 1 if para1 < para2 else 0
        i += 4
    elif opcode == 8:
        # igual a:
        para1 = intcode[i+1] if parameter_modes[0] == 1 else intcode[intcode[i+1]]
        para2 = intcode[i+2] if parameter_modes[1] == 1 else intcode[intcode[i+2]]
        intcode[intcode[i+3]] = 1 if para1 == para2 else 0
        i += 4
    