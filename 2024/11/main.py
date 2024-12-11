# import numpy as np
# from numba import njit, prange

DAY = 11
FILE = "input.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        line = file.readline()
    nums = [int(num) for  num in line.split(" ")]
    return nums


def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            stoneStr = str(stone)
            newStones.append(int(stoneStr[0:len(stoneStr)//2]))
            second =  stoneStr[len(stoneStr)//2:]
            second = second.lstrip("0")
            if second == "":
                second = "0"
            newStones.append(int(second))
            continue
        newStones.append(stone * 2024)
    return newStones
            


def solve1(stones):
    for i in range(25):
        print(f"blink {i}")
        newStones =  blink(stones)
        stones = newStones
    return len(stones)


# same as part one too slow
def solve2(input):
    
    return 
 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
