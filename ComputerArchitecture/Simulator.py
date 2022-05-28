import Assembler

def simulaor():

    RAM = []
    ROM = []
    instructions = []
    ACC = 0

    instructions = []

    instruction_file = open("instructions.txt", "r+")

    line = instruction_file.readline()
    line.replace(" ", "")
    print(line)



if __name__ == '__main__':
    simulaor()