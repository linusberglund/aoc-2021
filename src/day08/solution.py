import re
from enum import Enum
from pprint import pprint


class Digits(Enum):
    ONE = 2
    FOUR = 4
    SEVEN = 3
    EIGHT = 7
    TWO_THREE_FIVE = 5
    ZERO_SIX_NINE = 6


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


"""
2 = ONE
3 = SEVEN
4 = FOUR

5 = TWO
5 = THREE
5 = FIVE

6 = ZERO
6 = SIX
6 = NINE

7 = EIGHT

class SegmentSets(Enum):
    ZERO = {"a", "b", "c", "d", "e", "g"}
    ONE = {"c", "f"}
    TWO = {"a", "c", "d", "e", "g"}
    THREE = {"a", "c", "d", "f", "g"}
    FOUR = {"b", "c", "d", "f"}
    FIVE = {"a", "b", "d", "f", "g"}
    SIX = {"a", "b", "d", "e", "f", "g"}
    SEVEN = {"a" "c", "f"}
    EIGHT = {"a", "b", "c", "d", "e", "f", "g"}
    NINE = {"a", "b", "c", "d", "f", "g"}
"""


def part2(data):

    result = []

    for line in data:
        first_half = line[:10]
        second_half = line[10:]

        # number: {set of line-specific segments}
        segment_mapping = {}

        for segment_group in first_half:
            segments = set(segment_group)
            match len(segments):
                case Digits.ONE.value:
                    segment_mapping[1] = segments
                case Digits.FOUR.value:
                    segment_mapping[4] = segments
                case Digits.SEVEN.value:
                    segment_mapping[7] = segments
                case Digits.EIGHT.value:
                    segment_mapping[8] = segments

        for segment_group in first_half:
            segments = set(segment_group)
            match len(segments):
                case Digits.TWO_THREE_FIVE.value:
                    if segments.issuperset(segment_mapping[1]):
                        segment_mapping[3] = segments
                    elif len(segments.difference(segment_mapping[4])) == 3:
                        segment_mapping[2] = segments
                    elif len(segments.difference(segment_mapping[4])) == 2:
                        segment_mapping[5] = segments
                case Digits.ZERO_SIX_NINE.value:
                    if segments.issuperset(segment_mapping[4]):
                        segment_mapping[9] = segments
                        segments.difference
                    elif segments.issuperset(segment_mapping[1]):
                        segment_mapping[0] = segments
                    elif not segments.issuperset(segment_mapping[1]):
                        segment_mapping[6] = segments

        output = []
        for segment_group in second_half:
            for i in range(10):
                if segment_mapping[i] == set(segment_group):
                    output.append(str(i))

        output_final = ""
        for x in output:
            output_final += x

        result.append(int(output_final))
    return sum(result)


data = open("src/day08/input.txt", "r").readlines()
# data = open("src/day08/example2.txt", "r").readlines()
# data = open("src/day08/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [re.sub(r" \| ", r" ", line) for line in data]
data = [line.split(" ") for line in data]

print(part1(data))
print(part2(data))
