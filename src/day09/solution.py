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


def find_low_points(heightmap):
    risk = []

    for line_index, line in enumerate(heightmap):
        for location_index in range(len(heightmap[line_index])):

            current = heightmap[line_index][location_index]
            left, right, up, down = 9, 9, 9, 9

            if location_index - 1 >= 0:
                left = heightmap[line_index][location_index - 1]
            if location_index < len(line) - 1:
                right = heightmap[line_index][location_index + 1]
            if line_index - 1 >= 0:
                up = heightmap[line_index - 1][location_index]
            if line_index < len(data) - 1:
                down = heightmap[line_index + 1][location_index]

            if current < left and current < right and current < up and current < down:
                risk.append((line_index, location_index))

    return risk


def traverse_basin(heightmap, searched: set, point: tuple, basins):

    if point in searched:
        return

    searched.add(point)

    (x, y) = point

    left, up, down, right = (9, 9, 9, 9)

    if y - 1 >= 0:
        left = heightmap[x][y - 1]
    if x - 1 >= 0:
        up = heightmap[x - 1][y]
    if x < len(heightmap) - 1:
        down = heightmap[x + 1][y]
    if y < len(heightmap[0]) - 1:
        right = heightmap[x][y + 1]

    if sum([left, up, down, right]) >= 9 * 4:
        return

    if left < 9:
        traverse_basin(heightmap, searched, (x, y - 1), basins)
    if up < 9:
        traverse_basin(heightmap, searched, (x - 1, y), basins)
    if down < 9:
        traverse_basin(heightmap, searched, (x + 1, y), basins)
    if right < 9:
        traverse_basin(heightmap, searched, (x, y + 1), basins)

    basins[x][y] = True
    return basins


def part2(data):
    heightmap = [[int(location) for location in line] for line in data]
    low_points = find_low_points(heightmap)

    basin_sizes = []

    for point in low_points:
        searched = set()
        basins = [[False for location in line] for line in data]
        basins = traverse_basin(heightmap, searched, point, basins)
        basin_sizes.append((sum(map(sum, basins))))

    basin_sizes.sort(reverse=True)
    basin_sizes = basin_sizes[:3]

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


data = open("src/day09/input.txt", "r").readlines()
# data = open("src/day09/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
