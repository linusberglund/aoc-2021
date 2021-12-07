import statistics
from pprint import pprint


def part1(data):
    med = int(statistics.median(data))
    cost = []
    for crab in data:
        cost.append(abs(crab - med))

    return sum(cost)


def part2(data):

    # (crab_pos, destination): total_cost
    cost = {}

    highest_pos = max(data)

    for crab in data:
        for i in range(highest_pos + 1):
            if (crab, i) not in cost:
                cost[(crab, i)] = 0

            if crab == 16 and i == 5:
                pass
            if crab == 1 and i == 5:
                pass

            n = abs(crab - i)
            cost[(crab, i)] = int(n * (n + 1) / 2)

            # >:(
            # cost[(crab, i)] = cost[(crab, i)] + int(n*(n+1)/2)

    # combined_pos: total_cost
    total_cost = {}

    for i in range(highest_pos + 1):
        for crab in data:
            if i not in total_cost:
                total_cost[i] = 0

            total_cost[i] += cost[(crab, i)]

    return min(total_cost.values())


data = open("src/day07/input.txt", "r").readlines()
# data = open("src/day07/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [line.split(",") for line in data][0]
data = [int(n) for n in data]

print(part1(data))
print(part2(data))
