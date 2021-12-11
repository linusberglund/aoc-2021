from colorama import Fore


def print_state(data):
    for line in data:
        for octopus in line:
            match octopus:
                case 0:
                    print(Fore.CYAN, end="")
                    print(octopus, end="")
                    print(Fore.RESET, end="")
                case 1:
                    print(Fore.MAGENTA, end="")
                    print(octopus, end="")
                    print(Fore.RESET, end="")
                case 9:
                    print(Fore.RED, end="")
                    print(octopus, end="")
                    print(Fore.RESET, end="")
                case _:
                    print(octopus, end="")
                    print(Fore.RESET, end="")
        print()
    pass


def is_inside_grid(data, x, y):
    if y not in range(0, len(data)):
        return False

    if x not in range(0, len(data[0])):
        return False

    return True


def find_neighbors(data, x, y):
    neighbors = set()
    for i in range(x - 1, x + 1 + 1):
        for j in range(y - 1, y + 1 + 1):
            # don't add self
            # if i == x and j == y:
            #     continue
            if is_inside_grid(data, i, j):
                neighbors.add((i, j))

    return neighbors


def find_flashers(data):
    flashers = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] > 9:
                flashers.add((i, j))
    return flashers


def step(data):
    # print_state(data)
    # print("-----")

    # First, the energy level of each octopus increases by 1.
    data = [[octopus + 1 for octopus in line] for line in data]

    # Then, any octopus with an energy level greater than 9 flashes (at most once per step).
    flashes = 0
    already_flashing = set()
    about_to_flash = set()
    about_to_flash = about_to_flash.union(find_flashers(data))

    while len(about_to_flash) > 0:
        new_flashers = find_flashers(data)
        about_to_flash = new_flashers
        about_to_flash = about_to_flash.difference(already_flashing)
        for (x, y) in about_to_flash:
            if (x, y) in already_flashing:
                continue

            already_flashing.add((x, y))
            neighbors = find_neighbors(data, x, y)
            flashable_neighbors = neighbors.difference(already_flashing)
            for (i, j) in flashable_neighbors:
                data[i][j] += 1

    # Finally, any octopus that flashed during this step has its energy level set to 0.
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] > 9:
                data[i][j] = 0
                flashes += 1

    return data, flashes


def part1(data):
    print_state(data)
    print("-----")

    flashes = []
    for _ in range(100):
        data, step_flash = step(data)
        flashes.append(step_flash)

    print_state(data)
    print("-----")
    return sum(flashes)


def part2(data):
    current_step = 0

    while sum(map(sum, data)) != 0:
        data, step_flash = step(data)
        current_step += 1
        pass

    return current_step


data = open("src/day11/input.txt", "r").readlines()
# data = open("src/day11/example.txt", "r").readlines()
# data = open("src/day11/test1.txt", "r").readlines()
# data = open("src/day11/test2.txt", "r").readlines()
# data = open("src/day11/test3.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [[int(n) for n in line] for line in data]

print(part1(data))
print(part2(data))
