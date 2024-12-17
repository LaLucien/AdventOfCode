import numpy as np

DAY = 17
FILE = "test.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        content = file.read()

    content = content.split("\n")

    program = np.array([int(num) for num in content[-1].split(": ")[-1].split(",")], dtype=int)
    RegA = int(content[0].replace("\n", "").split(": ")[-1])
    RegB = int(content[1].replace("\n", "").split(": ")[-1])
    RegC = int(content[2].replace("\n", "").split(": ")[-1])

    return program, np.array([RegA, RegB, RegC], dtype=int)



def combo(literal, Regs):
    if literal in range(0,4):
        return literal
    if literal == 4:
        return Regs[0]
    if literal == 5:
        return Regs[1]
    if literal == 6:
        return Regs[2]
    raise Exception()


def adv(Regs, literal, index = 0):
    Regs[0] = Regs[index] // (2 ** combo(literal, Regs))
    return

def bxl(Regs, literal):
    Regs[1] ^ literal
    return

def bst(Regs, literal):
    # do chammer potentiel bitwise and shenanegans mache
    Regs[1] = combo(literal, Regs) % 8
    return





def solve1(program, Regs):
    i = 0
    output = ""
    while i < len(program)-1:
        print(i)
        opcode = program[i]
        literal = program[i+1]
        
        if opcode == 0:
            adv(Regs, literal)
            i+=2
            continue
        if opcode == 1:
            bxl(Regs, literal)
            i+=2
            continue
        if opcode == 2:
            bst(Regs, literal)
            i+=2
            continue
        if opcode == 3:
            if not Regs[0]:
                i+=2
                continue
            # if i == len(program)-2:
            #     break
            i = literal    
            continue
        if opcode == 4:
            Regs[1] ^= Regs[2] 
            i+=2
            continue
        if opcode == 5:
            output += str(combo(literal, Regs)%8) + ","
            i+=2
            continue
        if opcode == 6:
            adv(Regs, literal, 1)
            i+=2
            continue
        if opcode == 7:
            adv(Regs, literal, 2)
            i+=2
            continue

    return output[:len(output)-1]



def solve2(input):


    return 




if __name__ == "__main__":
    program, Regs = getInput()
    print(solve1(program, Regs))
    print(solve2(input))
