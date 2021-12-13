from pprint import pprint as pp


def read_chart(data):
    dots = [x for x in data if "," in x]
    dots = [x.split(",") for x in dots]
    dots = [[int(x) for x in line] for line in dots]

    folds = [x for x in data if "fold" in x]
    folds = [x.split(" ") for x in folds]
    folds = [[x for x in l if "=" in x] for l in folds]
    folds = [x for items in folds for x in items]
    folds = [x.split("=") for x in folds]

    return (dots, folds)


def find_dots_size(dots):
    max_x = 0
    max_y = 0

    for x, y in dots:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return max_x + 1, max_y + 1


def draw_chart(chart):
    for x in chart:
        print(*x, sep="")
    pass


def create_chart(dots):
    max_x, max_y = find_dots_size(dots)

    chart = [["." for x in range(max_x)] for y in range(max_y)]

    for y, x in dots:
        chart[x][y] = "#"

    return chart


# horizontal = up, vertical = left
def fold(chart, along_x, fold_line):
    if along_x:
        for line_index, line in enumerate(chart):
            if line_index is fold_line:
                for char_index, char in enumerate(line):
                    chart[line_index][char_index] = "-"
                pass
            for char_index, char in enumerate(line):
                if char == "#":
                    chart[-line_index - 1][char_index] = "#"
        new_chart = chart[:fold_line]
    else:
        for line_index, line in enumerate(chart):
            if line_index is fold_line:
                for char_index, char in enumerate(line):
                    chart[line_index][char_index] = "-"
                pass
            for char_index, char in enumerate(line):
                if char == "#":
                    chart[line_index][-char_index - 1] = "#"
        new_chart = []
        for line in chart:
            new_chart.append(line[:fold_line])

    return new_chart


def count_dots(chart):
    counter = 0
    for line_index, line in enumerate(chart):
        for char_index, char in enumerate(line):
            if char == "#":
                counter += 1
    return counter


def part1(data):
    dots, folds = read_chart(data)
    chart = create_chart(dots)
    for (dir, pos) in folds[:1]:
        match dir:
            case "y":
                chart = fold(chart, True, int(pos))
            case "x":
                chart = fold(chart, False, int(pos))

    return count_dots(chart)


def part2(data):
    dots, folds = read_chart(data)
    chart = create_chart(dots)
    for (dir, pos) in folds:
        match dir:
            case "y":
                chart = fold(chart, True, int(pos))
            case "x":
                chart = fold(chart, False, int(pos))

    draw_chart(chart)
    return count_dots(chart)


data = open("src/day13/input.txt", "r").readlines()
# data = open("src/day13/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
