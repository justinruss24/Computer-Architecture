"""CPU functionality."""

import sys


LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # ram that holds 256 bytes
        self.ram = [0] * 256
        # 8 registers (list of 0)
        self.reg = [0] * 8
        # internal pc register is 0
        self.pc = 0
        # set up the branch table
        self.running = True
        self.branchtable = {}
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[PUSH] = self.handlePUSH
        self.branchtable[POP] = self.handlePOP
        self.branchtable[CALL] = self.handle_CALL
        self.branchtable[RET] = self.handle_RET
        self.stack_pointer = 0xf4
        self.reg[7] = self.stack_pointer

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def handle_HLT(self, *args):
        self.running = False
    
    def handle_LDI(self, op_a, op_b):
        self.reg[op_a] = op_b

    def handle_PRN(self, op_a, op_b):
        print(self.reg[op_a])
    
    def handle_MUL(self, op_a, op_b):
        print(op_a, op_b)
        self.alu('MUL', op_a, op_b)

    def handlePUSH(self, a, b = None):
        # decrement stack pointer
        self.stack_pointer -= 1
        # self.stack_pointer &= 0xff  # keep in range of 00-FF
        # get register number and value stored at specified reg number
        reg_num = self.ram[self.pc + 1]
        val = self.reg[reg_num]

        # store value in ram
        self.ram[self.stack_pointer] = val

    
    def handlePOP(self, a, b = None):
        # get value from RAM
        address = self.stack_pointer
        val = self.ram[address]

        # store at given register
        reg_num = self.ram[self.pc + 1]
        self.reg[reg_num] = val

        # increment stack pointer and program counter
        self.stack_pointer += 1
        self.stack_pointer &= 0xff  # keep in range of 00-FF
    
    def handle_CALL(self, op_a, op_b):
        addr = self.reg[op_a]
        rtn_addr = self.pc + 2
        self.reg[7] -= 1
        sp = self.reg[7]
        self.ram[sp] = rtn_addr
        self.pc = addr
    
    def handle_RET(self, *args):
        rtn_addr = self.ram[self.reg[7]]
        self.reg[7] += 1
        self.pc = rtn_addr

    def ram_read(self, MAR):  # MAR = Memory address register
        # uses an address to read and returns the value stored at that address
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):  # MDR = Memory data register
        self.ram[MAR] = MDR

    def load(self, filename):
        """Load a program into memory."""

        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    line = line.split('#')
                    temp = line[0].strip()
                    if temp:
                        value = int(temp, 2)
                        self.ram[address] = value
                        address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {filename} not found")

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == 'MUL':
            # print(self.reg[reg_b])
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        while self.running:
            ir = self.ram_read(self.pc)

            op_a = self.ram_read(self.pc + 1)
            op_b = self.ram_read(self.pc + 2)

            add_to_pc = (ir >> 6) + 1

            self.branchtable[ir](op_a, op_b)

            self.pc += add_to_pc

