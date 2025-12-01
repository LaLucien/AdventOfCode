import os

DAY = 1
FILE = "puzzle.txt"
# FILE = "test.txt"


def getInput():

    with open(f"2025/{DAY}/{FILE}", "r") as file:

        return file.readlines()


def solve1(input):
    dial_pos = 50
    zero_transits = 0
    for line in input:
        move = int(line[1:])
        match line[0]:
            case "R":

                dial_pos += move

            case "L":

                dial_pos -= move
        dial_pos %= 100
        if dial_pos == 0:
            zero_transits += 1

    return zero_transits


def solve2(input):

    dial_pos = 50
    zero_transits = 0
    for line in input:
        move = int(line[1:])
        if abs(move) >= 100:
            zero_transits += abs(move) // 100
            move = 100 - move // 100

            # if move < 0:
            # move = 100 - move // 100
            # else:
            # move %= 100
            continue
        match line[0]:
            case "R":

                dial_pos += move
                if dial_pos > 99:
                    zero_transits += 1
                    dial_pos = dial_pos % 100
                # if dial_pos == 0:
                #     zero_transits += 1

            case "L":
                not_from_zero = dial_pos != 0
                dial_pos -= move
                if dial_pos < 0:
                    zero_transits += 1 if not_from_zero else 0
                    dial_pos = 100 + dial_pos
                # dial_pos %= 100
                if dial_pos == 0:
                    zero_transits += 1
        # print(dial_pos, " ", zero_transits)

    return zero_transits


if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
