
def main():

    instructions = []

    assembly_file = open("assembly.txt", "r+")
    lines = assembly_file.readlines()

    for line in lines:

        line = line.strip()

        line_info = line.split(" ")
        line_hex_code = binToHexa(getOpCode(line_info[0])) + decimalToHexadecimal(int(line_info[1]))
        instructions.append(line_hex_code)

    output_file = open("instructions.txt", "w+")
    for i in range(len(instructions)):
        output_file.write(instructions[i] + " ")

def getOpCode(menomic):
    menomic = menomic.upper()
    return_value = ""
    if menomic == "BRZ":
        return_value = "0000"
    elif menomic == "BRN":
        return_value = "0001"
    elif menomic == "LDI":
        return_value = "0010"
    elif menomic == "LDM":
        return_value = "0011"
    elif menomic == "STR":
        return_value = "0100"
    elif menomic == "ADD":
        return_value = "0101"
    elif menomic == "SUB":
        return_value = "0110"
    elif menomic == "MUL":
        return_value = "0111"
    elif menomic == "DIV":
        return_value = "1000"
    elif menomic == "NEG":
        return_value = "1001"
    elif menomic == "LSL":
        return_value = "1010"
    elif menomic == "LSR":
        return_value = "1011"
    elif menomic == "XOR":
        return_value = "1100"
    elif menomic == "NOT":
        return_value = "1101"
    elif menomic == "AND":
        return_value = "1110"
    elif menomic == "ORR":
        return_value = "1111"
    else:
        return_value = ""
    return return_value


# Python code to convert binary number
# into hexadecimal number

# function to convert
# binary to hexadecimal

def binToHexa(n):
    bnum = int(n)
    h = 0
    m = 1
    chk = 1
    i = 0
    hnum = []
    while bnum != 0:
        rem = bnum % 10
        h = h + (rem * m)
        if chk % 4 == 0:
            if h < 10:
                hnum.insert(i, chr(h + 48))
            else:
                hnum.insert(i, chr(h + 55))
            m = 1
            h = 0
            chk = 1
            i = i + 1
        else:
            m = m * 2
            chk = chk + 1
        bnum = int(bnum / 10)

    if chk != 1:
        hnum.insert(i, chr(h + 48))
    if chk == 1:
        i = i - 1
    result = ""
    while i >= 0:
        i = i - 1
        result += hnum[i]
    if str(result) == "":
        result = "0"
    return result


def decimalToHexadecimal(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    if len(hexadecimal) == 0:
        hexadecimal += "000"
    if len(hexadecimal) == 1:
        hexadecimal = "00" + hexadecimal
    if len(hexadecimal) == 2:
        hexadecimal = "0" + hexadecimal

    return hexadecimal


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


