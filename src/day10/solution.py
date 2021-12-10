def line_checker_part1(line):
    matches = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    first = "([{<"
    second = ")]}>"

    stack = []
    for char in line:
        stack.append(char)

        if len(stack) >= 2:
            opening = stack[-2]
            closing = stack[-1]

            if opening in first and closing in first:
                continue

            match (opening, closing):
                case "(", ")":
                    # print("! () !")
                    stack.pop()
                    stack.pop()
                    pass
                case "[", "]":
                    # print("! [] !")
                    stack.pop()
                    stack.pop()
                    pass
                case "{", "}":
                    # print("! {} !")
                    stack.pop()
                    stack.pop()
                    pass
                case "<", ">":
                    # print("! <> !")
                    stack.pop()
                    stack.pop()
                    pass
                case _, _:
                    if closing in first:
                        # print("INCOMPLETE")
                        return 0
                    if matches[opening] != closing:
                        # print("CORRUPTED")
                        return score[closing]

    # print("INCOMPLETE")
    return 0


# corrupted, not incomplete
def part1(data):

    result = []
    for line in data:
        error_score = line_checker_part1(line)
        result.append(error_score)

    return sum(result)


def line_checker_part2(line):
    matches = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    first = "([{<"
    second = ")]}>"

    stack = []
    for char in line:
        stack.append(char)

        if len(stack) >= 2:
            opening = stack[-2]
            closing = stack[-1]

            if opening in first and closing in first:
                continue

            match (opening, closing):
                case "(", ")":
                    # print("! () !")
                    stack.pop()
                    stack.pop()
                    pass
                case "[", "]":
                    # print("! [] !")
                    stack.pop()
                    stack.pop()
                    pass
                case "{", "}":
                    # print("! {} !")
                    stack.pop()
                    stack.pop()
                    pass
                case "<", ">":
                    # print("! <> !")
                    stack.pop()
                    stack.pop()
                    pass
                case _, _:
                    if matches[opening] != closing:
                        # print("CORRUPTED")
                        return 0

    result = 0
    stack.reverse()
    for fix in stack:
        result = (result * 5) + score[matches[fix]]
    return result


# incomplete, not corrupted
def part2(data):
    result = []
    for line in data:
        score = line_checker_part2(line)
        if score != 0:
            result.append(score)

    result.sort()
    # always odd
    result = result[int((len(result) / 2) - 0.5)]

    return result


data = open("src/day10/input.txt", "r").readlines()
# data = open("src/day10/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
