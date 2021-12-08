import re
from enum import Enum


class Digits(Enum):
    ZERO = 6
    ONE = 2
    TWO = 5
    THREE = 5
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 3
    EIGHT = 7
    NINE = 6


# count amount of 1, 4, 7, and 8
def part1(data):
    counter = 0

    for group in data:
        # first_half = group[:10]
        second_half = group[10:]

        for digit in second_half:
            match len(digit):
                case Digits.ONE._value_:
                    counter += 1
                case Digits.FOUR._value_:
                    counter += 1
                case Digits.SEVEN._value_:
                    counter += 1
                case Digits.EIGHT._value_:
                    counter += 1

    return counter


def part2(data):
    pass


data = open("src/day08/input.txt", "r").readlines()
# data = open("src/day08/example.txt", "r").readlines()
# data = open("src/day08/example2.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [re.sub(r" \| ", r" ", line) for line in data]
data = [line.split(" ") for line in data]

print(part1(data))
print(part2(data))
