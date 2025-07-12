import numpy as np

DAY = 7
FILE = "puzzle.txt"


def getInput():

    solutions = []
    equations = []
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        lines = file.readlines()

    for line in lines:
        solutions.append(int(line.split(":")[0]))
        numbers = []
        for snum in line.strip().split(": ")[1].split(" "):
            numbers.append(int(snum))
        equations.append(np.array(numbers))

    return (np.array(solutions), equations)


def check_solution(expected, running_total, numbers, current_index):
    if expected == running_total:
        return True
    if current_index + 1 >= len(numbers):
        return False
    return check_solution(
        expected, running_total + numbers[current_index + 1], numbers, current_index + 1
    ) or check_solution(
        expected, running_total * numbers[current_index + 1], numbers, current_index + 1
    )


def solve1(input):
    solutions = input[0]
    equations = input[1]
    # operators = np.array(["+", "*"])
    solution = 0
    for expected, numbers in zip(solutions, equations):
        if check_solution(expected, 0 + numbers[0], numbers, 0) or check_solution(
            expected, 1 * numbers[0], numbers, 0
        ):
            solution += expected

    return solution


def solve2(input):

    return


if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
