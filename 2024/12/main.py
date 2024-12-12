import numpy as np

DAY = 12
FILE = "test.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        lines = file.readlines()

    input = []
    for line in lines:
        input.append(np.array([c for c in line.strip()], dtype=str))

    return np.pad(np.array(input), constant_values=".", pad_width=1)



def solve1(input):
    # initialize dict
    plantData = {}
    for symbol in np.unique(input):
        if symbol == ".":
            continue
        plantData[symbol] = np.array([0,0], dtype=int)

    xLength = input.shape[1] - 1
    for i in range(1, input.shape[0]-1):
        for j in range(1, xLength):
            currentPlant = input[i,j]
            plantData[currentPlant][0] += 1

            newBorderLength = 0
            if currentPlant != input[i - 1,j]:
                newBorderLength += 1
            if currentPlant != input[i + 1,j]:
                newBorderLength += 1
            if currentPlant != input[i,j - 1]:
                newBorderLength += 1
            if currentPlant != input[i,j + 1]:
                newBorderLength += 1

            plantData[currentPlant][1] += newBorderLength

    totalPrice = 0   
    for key in plantData.keys():
        totalPrice += plantData[key][0] * plantData[key][1]

    return totalPrice



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
