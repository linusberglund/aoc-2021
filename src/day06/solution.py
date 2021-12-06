DAYS = 256
SPAWN_DAYS = 8
RECOVERY_DAYS = 6


def part1(data, days):
    sea = [x for x in data]
    for _ in range(days):
        for index, fish in enumerate(sea):
            match fish:
                case 0:
                    sea[index] = RECOVERY_DAYS
                    sea.append(SPAWN_DAYS + 1)
                case _:
                    sea[index] -= 1
    return len(sea)


def part2_memo(fish, days, memo):
    if (fish, days) in memo:
        return memo[(fish, days)]

    if fish >= days:
        memo[(fish, days)] = 1
        return 1

    next_day = days - fish - 1

    child = part2_memo(SPAWN_DAYS, next_day, memo)
    current = part2_memo(RECOVERY_DAYS, next_day, memo)

    memo[(SPAWN_DAYS, next_day)] = child
    memo[(RECOVERY_DAYS, next_day)] = current

    memo[(fish, days)] = child + current

    return memo[(fish, days)]


def part2(data, days):
    # {fish_lifetime, days_left}: total_fishes_from_this_fish
    memo = {}
    result = []

    for fish in data:
        result.append(part2_memo(fish, days, memo))

    return sum(result)


data = open("src/day06/input.txt", "r").readlines()
# data = open("src/day06/example.txt", "r").readlines()

data = [line.strip("\n") for line in data]
data = [line.split(",") for line in data][0]
data = [int(n) for n in data]

print(part1(data, 80))
print(part2(data, DAYS))
