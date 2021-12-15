from colorama import Fore


def print_cave(cave, path=None):
    max_x = len(cave)
    max_y = len(cave[0])
    for x in range(max_x):
        for y in range(max_y):
            if path and (x, y) in path:
                print(Fore.MAGENTA, cave[x][y], Fore.RESET, sep="", end="")
            else:
                print(cave[x][y], sep="", end="")
        print()


def is_inside_grid(data, x, y):
    if x not in range(0, len(data)):
        return False

    if y not in range(0, len(data[0])):
        return False

    return True


def find_neighbors(data, node):
    x, y = node
    neighbors = set()

    left = (x, y - 1)
    up = (x - 1, y)
    down = (x + 1, y)
    right = (x, y + 1)

    for (x, y) in {left, up, down, right}:
        if is_inside_grid(data, x, y):
            neighbors.add((x, y))

    return neighbors


# X DOWNWARDS, Y RIGHTWARDS
def dijkstra(cave: list(list())):
    unvisited = {(x, y) for x in range(len(cave)) for y in range(len(cave[0]))}
    dist = dict()
    prev = dict()

    graph_sum = sum(sum(cave, []))

    for x, y in unvisited:
        dist[(x, y)] = graph_sum

    dist[(0, 0)] = 0

    while unvisited:

        # if not len(unisited) % 100:
        #     print(len(vunvisited))

        dist_unvisited = {k: v for k, v in dist.items() if k in unvisited}
        node = min(dist_unvisited, key=dist_unvisited.get)
        unvisited.remove(node)

        for neighbor in find_neighbors(cave, node).intersection(unvisited):
            x, y = neighbor
            alt = dist[node] + cave[x][y]

            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = node

    # path = list()
    # node = (len(cave) - 1, len(cave[0]) - 1)
    # path.append(node)
    # while True:
    #     node = prev[node]
    #     path.append(node)
    #     if node == (0, 0):
    #         break
    # print_cave(cave, path)

    return dist


def part1(data):
    cave = data.copy()
    result = dijkstra(cave)
    return result[(len(cave) - 1, len(cave[0]) - 1)]


################################################################################


def create_full_map(cave):
    new_cave = []

    # width
    for line in cave:
        new_line = []
        for i in range(5):
            current_line = [x + i for x in line]
            current_line = [((x - 1) % 9) + 1 for x in current_line]
            new_line.extend(current_line)
        new_cave.append(new_line)

    # length
    new_cave_2 = []
    for i in range(5):
        for line in new_cave:
            current_line = [x + i for x in line]
            current_line = [((x - 1) % 9) + 1 for x in current_line]
            new_cave_2.append(current_line)

    return new_cave_2


def part2(data):
    cave = data.copy()
    cave = create_full_map(cave)
    print("Will take hours :)")
    result = dijkstra(cave)
    return result[(len(cave) - 1, len(cave[0]) - 1)]


data = open("src/day15/input.txt", "r").readlines()
# data = open("src/day15/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [[int(n) for n in line] for line in data]

print(part1(data))
print(part2(data))
