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

    return program, RegA, RegB, RegC

def solve1(program, RegA, RegB, RegC):
    
    return 



def solve2(input):


    return 




if __name__ == "__main__":
    program, RegA, RegB, RegC = getInput()
    print(solve1(program, RegA, RegB, RegC))
    print(solve2(input))
