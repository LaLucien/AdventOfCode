import numpy as np

DAY = 10
FILE = "input.txt"

def getInput():

    lines = []

    with open(f"2024/{DAY}/{FILE}", "r") as file:
        content = file.readlines()
        for line in content:
            num = []
            for c in line.replace("\n",""):
                num.append(int(c))
            lines.append(np.array(num))
    lines = np.array(lines)
    linesPadded = np.pad(lines, 1, constant_values=-1)
    return linesPadded


def leads_to_nine(input, i, j, previousHight):
    if input[i,j] == 9:
        return 1
    if input[i,j] <= previousHight or input[i,j] - previousHight >= 2:
        return 0
    return leads_to_nine(input, i + 1, j, input[i,j]) + leads_to_nine(input, i - 1, j, input[i,j]) + leads_to_nine(input, i, j + 1, input[i,j]) + leads_to_nine(input, i, j - 1, input[i,j])



def count_trails(input, i, j, previousHight, ninepos):
    if input[i,j] <= previousHight or input[i,j] > previousHight + 1:
        return 

    if input[i,j] == 9:
        ninepos.append([i,j])
        return 
    
    count_trails(input, i - 1, j, input[i,j], ninepos)
    count_trails(input, i + 1, j, input[i,j], ninepos) 
    count_trails(input, i, j - 1, input[i,j], ninepos)
    count_trails(input, i, j + 1, input[i,j], ninepos)
    return  
    

def solve1(input):
    trailheadscore = 0
    distinctScore = 0
    xLength = input.shape[1]
    for i in range(1, input.shape[0]-1):
        for j in range(1, xLength - 1):
            if(not input[i,j]):
                ninepos = []
                count_trails(input, i,j,-1, ninepos)
                trailheadscore += np.unique(ninepos, axis=0).shape[0]
                distinctScore += len(ninepos)
                
    return trailheadscore, distinctScore



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    # sol1 = 
    print(solve1(input))
    # print(solve2(input)) #in sol1
