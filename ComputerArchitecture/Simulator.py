import numpy as np
import Assembler
import math


def simulator():

    RAM = []
    ROM = []
    PC = 0
    ACC = 0

    ROM = np.loadtxt('instructions.txt', dtype=str)
    binary_instructions = hextoBin(ROM)

    print("HEX ARRAY: " , ROM)
    print("BINARY ARRAY: " , binary_instructions)

def hextoBin(hexArr):
    binArr = []

    index = 0
    for i in hexArr:
        my_hexdata = i

        scale = 16  ## equals to hexadecimal

        num_of_bits = 16

        binData = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        binArr.append(binData)
    #print(binArr)
    return binArr




def BRZ(x, ACC, RAM, PC):
    if ACC == 0:
        PC += x

def BRN(x, ACC, RAM, PC):
    if ACC < 0:
        PC += x

def LDI(x, ACC, RAM, PC):
    ACC == x

def LDM(x, ACC, RAM, PC):
    ACC == RAM[x]

def STR(x, ACC, RAM, PC):
    RAM[x] == ACC

def ADD(x, ACC, RAM, PC):
    ACC == ACC + RAM[x]

def SUB(x, ACC, RAM, PC):
    ACC == ACC - RAM[x]

def MUL(x, ACC, RAM, PC):
    ACC == ACC * RAM[x]

def DIV(x, ACC, RAM, PC):
    ACC == ACC / RAM[x]

def NEG(x, ACC, RAM, PC):
    ACC == -ACC

def LSL(x, ACC, RAM, PC):
    ACC == ACC << x

def LSR(x, ACC, RAM, PC):
    ACC == ACC >> x

def XOR(x, ACC, RAM, PC):
    ACC == ACC ^ RAM[x]

def NOT(x, ACC, RAM, PC):
    ACC != ACC

def AND(x, ACC, RAM, PC):
    ACC == ACC and RAM[x]

def OR(x, ACC, RAM, PC):
    ACC == ACC or RAM[x]


def getOpCode(opcode, x, ACC, RAM, PC):

  if opcode == "0000":
      BRZ(x, ACC, RAM, PC)
  elif opcode == "0001":
      BRN(x, ACC, RAM, PC)
  elif opcode == "0010":
      LDI(x, ACC, RAM, PC)
  elif opcode == "0011":
      LDM(x, ACC, RAM, PC)
  elif opcode == "0100":
      STR(x, ACC, RAM, PC)
  elif opcode == "0101":
      ADD(x, ACC, RAM, PC)
  elif opcode == "0110":
      SUB(x, ACC, RAM, PC)
  elif opcode == "0111":
      MUL(x, ACC, RAM, PC)
  elif opcode == "1000":
      DIV(x, ACC, RAM, PC)
  elif opcode == "1001":
      NEG(x, ACC, RAM, PC)
  elif opcode == "1010":
      LSL(x, ACC, RAM, PC)
  elif opcode == "1011":
      LSR(x, ACC, RAM, PC)
  elif opcode == "1100":
      XOR(x, ACC, RAM, PC)
  elif opcode == "1101":
      NOT(x, ACC, RAM, PC)
  elif opcode == "1110":
      AND(x, ACC, RAM, PC)
  elif opcode == "1111":
      OR(x, ACC, RAM, PC)


if __name__ == '__main__':
    simulator()