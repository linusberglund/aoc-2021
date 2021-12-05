import re
from pprint import pprint
import time
import os


def show_diagram(diagram):
    os.system("cls" if os.name == "nt" else "printf '\033c'")
    for x in diagram:
        print(*x, sep="")
    time.sleep(0.01)
    pass


def plot(x, y, diagram):
    if diagram[x][y] == ".":
        diagram[x][y] = 1
    elif int(diagram[x][y]):
        diagram[x][y] += 1
    # show_diagram(diagram)
    return diagram


def draw_row(row, start, length, diagram):
    for i in range(start, start + length):
        diagram = plot(row, i, diagram)

    return diagram


def draw_col(col, start, length, diagram):
    for line_index, line in enumerate(diagram):
        if line_index < start:
            continue
        if line_index > start + length - 1:
            continue

        diagram = plot(line_index, col, diagram)

    return diagram


def draw_diagonal(x1, y1, x2, y2, diagram):
    # print(x1, y1, x2, y2, sep="", end="\n")

    if x2 > x1 and y2 > y1:
        # print("Down Right e.g. 0,0 -> 9,9")
        point_range = zip(range(x1, x2 + 1), range(y1, y2 + 1))
        for y, x in point_range:
            # for x in range(x1, x2 + 1):
            #     for y in range(y1, y2 + 1):
            #         if x == y:
            diagram = plot(x, y, diagram)
            pass

    # 5,5 -> 8,2
    elif x2 > x1 and y1 > y2:
        # print("Down Left e.g. 0,9 -> 9,0")
        point_range = zip(range(x1, x2 + 1), range(y1, y2 - 1, -1))
        for y, x in point_range:
            # for x in range(x1, x2 + 1):
            #     for y in range(y1, y2 - 1, -1):
            #         if (x + y) == abs(x2 - x1):
            diagram = plot(x, y, diagram)
            pass

    elif x1 > x2 and y1 > y2:
        # print("Up Left e.g. 9,9 -> 0,0")
        point_range = zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1))
        for y, x in point_range:
            # for x in range(x1, x2 - 1, -1):
            #     for y in range(y1, y2 - 1, -1):
            #         if x + ~y + 1 == 0:
            diagram = plot(x, y, diagram)
            pass

    elif x1 > x2 and y2 > y1:
        # print("Up Right e.g. 9,0 -> 0,9")
        point_range = zip(range(x1, x2 - 1, -1), range(y1, y2 + 1))
        for y, x in point_range:
            # for x in range(x1, x2 - 1, -1):
            #     for y in range(y1, y2 + 1):
            #         if (x + y) == abs(x1 - x2):
            diagram = plot(x, y, diagram)
            pass

    # for x in diagram:
    #     print(*x, sep="")

    return diagram


def part1(data):
    size = max(max(x) for x in data) + 1
    diagram = [["." for i in range(size)] for i in range(size)]

    for line in data:
        x1, y1, x2, y2 = line

        # unreadable, should be a 3.10 match statement
        if x1 == x2 and y1 < y2:
            diagram = draw_col(x1, y1, y2 - y1 + 1, diagram)
            pass
        elif x1 == x2 and y2 < y1:
            diagram = draw_col(x1, y2, y1 - y2 + 1, diagram)
            pass
        elif y1 == y2 and x1 < x2:
            diagram = draw_row(y1, x1, x2 - x1 + 1, diagram)
            pass
        elif y1 == y2 and x2 < x1:
            diagram = draw_row(y1, x2, x1 - x2 + 1, diagram)
            pass

    # for x in diagram:
    #     print(*x, sep="")

    danger = [[x for x in line if x != "." and int(x) > 1] for line in diagram if line]
    danger = [x for sublist in danger for x in sublist if x]

    return len(danger)


def part2(data):
    size = max(max(x) for x in data) + 1
    diagram = [["." for i in range(size)] for i in range(size)]

    for line in data:
        x1, y1, x2, y2 = line

        # unreadable, should be a 3.10 match statement
        if x1 == x2 and y1 < y2:
            diagram = draw_col(x1, y1, y2 - y1 + 1, diagram)
            pass
        elif x1 == x2 and y2 < y1:
            diagram = draw_col(x1, y2, y1 - y2 + 1, diagram)
            pass
        elif y1 == y2 and x1 < x2:
            diagram = draw_row(y1, x1, x2 - x1 + 1, diagram)
            pass
        elif y1 == y2 and x2 < x1:
            diagram = draw_row(y1, x2, x1 - x2 + 1, diagram)
            pass
        else:
            diagram = draw_diagonal(x1, y1, x2, y2, diagram)

    # for x in diagram:
    #     print(*x, sep="")

    danger = [[x for x in line if x != "." and int(x) > 1] for line in diagram if line]
    danger = [x for sublist in danger for x in sublist if x]

    return len(danger)


data = open("src/day05/input.txt", "r").readlines()
# data = open("src/day05/example.txt", "r").readlines()
# data = open("src/day05/test1.txt", "r").readlines()
# data = open("src/day05/test2.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [re.sub(r" -> ", r",", line) for line in data]
data = [line.split(",") for line in data]
data = [[int(n) for n in line] for line in data]

print(part1(data))
print(part2(data))
