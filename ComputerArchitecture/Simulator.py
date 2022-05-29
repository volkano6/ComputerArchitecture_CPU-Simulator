import numpy as np


def simulator():
    RAM = [0] * 20
    ROM = []
    PC = 0
    ACC = 0
    opcode = None
    rest = 0

    ROM = np.loadtxt('instructions.txt', dtype=str)
    binary_instructions = hextoBin(ROM)
    print("   ------------- ROM -------------")
    for i in range(len(ROM)):
        print("  ", i, ":", "0x", ROM[i], "-->", binary_instructions[i])

    for step in range(len(ROM)):
        print("\n")
        print("Step", step + 1, ":")

        opcode = (binary_instructions[step][0:4])
        rest = (binary_instructions[step][4:])

        if binaryToDecimal(int(rest)) == 0:
            rest = 0
        else:
            rest = rest.lstrip("0")
        rest = binaryToDecimal(int(rest))

        if opcode == "0000":
            if ACC == 0:
                PC = PC + rest
        elif opcode == "0001":
            if ACC < 0:
                PC = PC + rest
        elif opcode == "0010":
            ACC = rest
        elif opcode == "0011":
            ACC = RAM[rest]
        elif opcode == "0100":
            RAM[rest] = ACC
        elif opcode == "0101":
            ACC = ACC + RAM[rest]
        elif opcode == "0110":
            ACC = ACC - RAM[rest]
        elif opcode == "0111":
            ACC = ACC * RAM[rest]
        elif opcode == "1000":
            ACC = ACC / RAM[rest]
        elif opcode == "1001":
            ACC = 0 - ACC
        elif opcode == "1010":
            ACC = ACC << rest
        elif opcode == "1011":
            ACC = ACC >> rest
        elif opcode == "1100":
            ACC = ACC ^ RAM[rest]
        elif opcode == "1101":
            ACC = ~ACC
        elif opcode == "1110":
            ACC = ACC & RAM[rest]
        elif opcode == "1111":
            ACC = ACC | RAM[rest]

        print("ACC :", ACC)
        print("PC : ", PC, "-->   0 x", ROM[step])
        print(RAM)
        PC += 1



def hextoBin(hexArr):
    binArr = []

    index = 0
    for i in hexArr:
        my_hexdata = i

        scale = 16  ## equals to hexadecimal

        num_of_bits = 16

        binData = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        binArr.append(binData)
    # print(binArr)
    return binArr


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
        # if decimal == 0:
        #     print("decimal : ", 0)
    return decimal


if __name__ == '__main__':
    simulator()
