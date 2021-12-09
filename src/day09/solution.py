from pprint import pprint


def part1(data):
    heatmap = [[int(location) for location in line] for line in data]
    risk_levels = [[False for location in line] for line in data]

    for line_index, line in enumerate(heatmap):
        for location_index, location in enumerate(heatmap[line_index]):
            current = heatmap[line_index][location_index]

            left, right, up, down = 9, 9, 9, 9
            if location_index - 1 >= 0:
                left = heatmap[line_index][location_index - 1]
            if location_index < len(line) - 1:
                right = heatmap[line_index][location_index + 1]
            if line_index - 1 >= 0:
                up = heatmap[line_index - 1][location_index]
            if line_index < len(data) - 1:
                down = heatmap[line_index + 1][location_index]

            if current < left and current < right and current < up and current < down:
                risk_levels[line_index][location_index] = True

    risk = []
    for line_index, line in enumerate(heatmap):
        for location_index, location in enumerate(heatmap[line_index]):
            if risk_levels[line_index][location_index]:
                risk.append(1 + heatmap[line_index][location_index])

    return sum(risk)


def part2(data):
    pass


data = open("src/day09/input.txt", "r").readlines()
# data = open("src/day09/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
