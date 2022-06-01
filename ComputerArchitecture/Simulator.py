import numpy as np
from Assembler import binToHexa


def simulator():
    RAM = [0] * 10000
    ROM = []
    PC = 0
    ACC = 0
    opcode = None
    rest = 0
    value_code = []

    ROM = np.loadtxt('instructions.txt', dtype=str)
    binary_instructions = hextoBin(ROM)

    print("   ------------- ROM -------------")
    for i in range(len(ROM)):
        print("  ", i, ":", "0x", ROM[i], "-->", binary_instructions[i])

    last_opcode = ""
    step_count = 1
    while PC < len(ROM):

        print("\n")
        print("Step", step_count, ":")
        step_count += 1
        print("PC : ", PC)
        opcode = (binary_instructions[PC][0:4])
        rest = (binary_instructions[PC][4:])
        rest = test_negate(rest)

        if opcode == "0000":
            if ACC == 0:
                PC = PC + rest
            else:
                PC += 1

        elif opcode == "0001":
            if ACC < 0:
                PC = PC + rest
            else:
                PC += 1
        elif opcode == "0010":
            ACC = rest
            PC += 1
        elif opcode == "0011":
            ACC = RAM[rest]
            PC += 1
        elif opcode == "0100":
            RAM[rest] = ACC
            print(ACC)
            PC += 1
        elif opcode == "0101":
            ACC = ACC + RAM[rest]
            PC += 1
        elif opcode == "0110":
            ACC = ACC - RAM[rest]
            PC += 1
        elif opcode == "0111":
            ACC = ACC * RAM[rest]
            PC += 1
        elif opcode == "1000":
            try:
                ACC = ACC / RAM[rest]
                PC += 1
            except ZeroDivisionError:
                print("ACC CAN NOT DIVIDED BY ZERO")
                print("EXIT THE PROGRAM")
                exit(0)
        elif opcode == "1001":
            ACC = 0 - ACC
            PC += 1
        elif opcode == "1010":
            ACC = ACC << rest
            PC += 1
        elif opcode == "1011":
            ACC = ACC >> rest
            PC += 1
        elif opcode == "1100":
            ACC = ACC ^ RAM[rest]
            PC += 1
        elif opcode == "1101":
            ACC = ~ACC
            PC += 1
        elif opcode == "1110":
            ACC = ACC & RAM[rest]
            PC += 1
        elif opcode == "1111":
            ACC = ACC | RAM[rest]
            PC += 1

        last_opcode = opcode
        print("ACC :", ACC)
        print("RAM :", RAM)


def test_negate(rest):
    if binaryToDecimal(int(rest)) > 2048:
        hex_val = "F" + hex(binaryToDecimal(int(rest)))[2:].upper()
        rest = "{0:08b}".format(int(hex_val, 16))
        rest = signed2s_complement(rest)

        if binaryToDecimal(int(rest)) == 0:
            rest = 0
        else:
            rest = rest.lstrip("0")
        rest = binaryToDecimal(int(rest))

        return 0-rest
    else:
        if binaryToDecimal(int(rest)) == 0:
            rest = 0
        else:
            rest = rest.lstrip("0")
        rest = binaryToDecimal(int(rest))
        return rest


def signed2s_complement(x):
    x = x.replace("0", "x").replace("1", "0").replace("x", "1")
    integer_sum = int(x, 2) + int("000000000001", 2)
    binary_sum = bin(integer_sum)
    return binary_sum[2:]


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
