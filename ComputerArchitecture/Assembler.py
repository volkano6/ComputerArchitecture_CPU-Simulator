
def main():

    instructions = []

    assembly_file = "assembly.txt"

    assembly_restored_file = restore_file(assembly_file)

    file = open(assembly_restored_file, "r+")

    lines = file.readlines()

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

    if decimal < 0:
        hexadecimal = str(to_hex(decimal, 12))

    if len(hexadecimal) == 0:
        hexadecimal += "000"
    if len(hexadecimal) == 1:
        hexadecimal = "00" + hexadecimal
    if len(hexadecimal) == 2:
        hexadecimal = "0" + hexadecimal

    return hexadecimal

def restore_file(assembly_file):
    with open(assembly_file) as fp:
        contents = fp.readlines()

    # initialize two counter to check mismatch between "(" and ")"
    open_bracket_counter = 0
    close_bracket_counter = 0

    # whenever an element deleted from the list length of the list will be decreased
    decreasing_counter = 0

    for number in range(len(contents)):
        # checking if the line contains "#" or not
        if "#" in contents[number - decreasing_counter]:

            # delete the line if startswith "#"
            if contents[number - decreasing_counter].startswith("#"):
                contents.remove(contents[number - decreasing_counter])
                decreasing_counter += 1

            # delete the character after the "#"
            else:
                newline = ""
                for character in contents[number - decreasing_counter]:
                    if character == "(":
                        open_bracket_counter += 1
                        newline += character
                    elif character == ")":
                        close_bracket_counter += 1
                        newline += character
                    elif character == "#" and open_bracket_counter == close_bracket_counter:
                        break
                    else:
                        newline += character
                contents.remove(contents[number - decreasing_counter])
                contents.insert(number - decreasing_counter, newline)

    contents = [x.strip(' ') for x in contents]
    contents = [x.replace("\n", "") for x in contents]
    space_counter = 0
    for i in range(len(contents)):
        if contents[i] == "":
            space_counter += 1
    for i in range(space_counter):
        contents.remove("")

    # writing into a new file
    with open("assembly_out.txt", "w+") as fp:
        for i in range(len(contents)):
            fp.writelines(contents[i])
            fp.writelines("\n")
    return "assembly_out.txt"

def to_hex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits)).lstrip('0x')

def _to_int(val, nbits):
    i = int(val, 16)
    if i >= 2 ** (nbits - 1):
        i -= 2 ** nbits
    return i

def hex2complement(number):
    hexadecimal_result = format(number, "03X")
    return hexadecimal_result.zfill(4)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


