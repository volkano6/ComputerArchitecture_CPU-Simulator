# ComputerArchitecture_CPU-Simulator

<head>
</head>

<body>
  <h1> CPU Simulator</h1>
  <br>

  <h3> 2.1.Description of Project </h3>
  <p>
    The project involves the implementation of a translator which takes the assembly code and converts it to a machine code (expressed in HEX). This software is also known as the assembler and is quite crucial to the execution of the program. The main objective in the design of the assembler is a fast program that will translate the assembly code to a binary file with various types of instructions contained in it, ready for execution.
  </p>
  <br>
  <p>
  The set of executable operations is specified in the form of instructions. Table 1 lists the instructions that the processor intends to support this project. The left-most column shows the opcode of the instruction. Menomics are listed in the following column and the explanation of that menomic is given in the column next to that. The right-most column shows the operation the corresponding instruction executes.
  </p>
  <img src="" alt="">

  <h3>2.2.Description of Solution</h3>
  <p>The solution of the project has two major parts. In the first part, we programmed an assembler code, and in the second part, we programmed a simulator 
    that executes the output that we get from our assembler code. Python is used as a programming language for this project.
    </p>
  <h4>2.2.1. Assembler code</h4>
  <p>+ According to ISA, we have if statements to obtain binary responses of instructions. If statements are arranged according to menomics and return their binary values. The rest value, which comes after the menomics, is decimal and it is converted into binary form. Once we are done with this phase, we convert all bits into hexadecimal. Hexadecimal instructions are saved into a text file named instructions.
  </p>
  <h4>2.2.2. Simulator code</h4>
  <p>Firstly, our simulator code reads the instructions from the instructions.txt file. Secondly, hex instructions are converted to a binary format that the computer can understand. After these operations, we have 16 bits of binary code. Simulator code splits these 16 bits as 4-12. The first 4 bits represent opcodes, and the rest of the 12 bits give either the immediate value or the absolute address in the memory. Opcodes provide to understand what operation will be performed. In simulator code, there are if statements that are prepared for the opcodes. In the if statements, there are operations over ACC PC RAM, which are prepared according to the opcodes in the ISA table. Finally, we see the results in the console and our simulation is completed.</p>
</body>

</html>
