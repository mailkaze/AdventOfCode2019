import os
from secret import path as path

os.chdir(path)
with open('input.txt', 'r') as f:
    intcode = list(map(int, f.readline().strip().split(',')))

# el programa empieza pidiendo el ID del ordenador, este es 1.
ID = 1
# los outputs 0. Si es otra cosa algo funciona mal.
# el último output será el diagnostico del TEST, éste no tiene por qué ser 0.

def opcode_parameter_mode_extractor(instruction):
    opcode = 0
    parameter_mode =[0,0,0,0,0,0,0,0,0,0]
    if instruction < 100:
        opcode = instruction
    else:
        opcode = str(instruction)[-2:]
        # TODO asignar los parameter modes

    return opcode, parameter_mode

def intcode1():
    #sumar
    pass

def intcode2():
    #multiplicar
    pass

def intcode3():
    #guardar un input
    pass

def intcode4():
    #output
    pass

opcode = 0
i = 0
while opcode != 99:
    #extraer el opcode y los parameter modes.
    opcode, parameter_mode = opcode_parameter_mode_extractor(intcode[i])
    print(opcode)
    i += 4
    