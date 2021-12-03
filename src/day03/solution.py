def part1(data):
    datalength = len([c for c in data[0]])

    zeros = [0] * datalength
    ones = [0] * datalength

    for i in range(datalength):
        for line in data:
            match int(line[i]):
                case 0: zeros[i] += 1
                case 1: ones[i] += 1

    gamma = [0] * datalength
    epsilon = [0] * datalength

    for i in range(datalength):
        if zeros[i] < ones[i]:
            gamma[i] = 1
        else:
            epsilon[i] = 1

    gamma_total = "".join(map(str, gamma))
    epsilon_total = "".join(map(str, epsilon))

    return int(gamma_total, 2) * int(epsilon_total, 2)


def part2(data):
    datalength = len([c for c in data[0]])

    oxygen = [x for x in data]
    for i in range(datalength):
        zeros = [0] * datalength
        ones = [0] * datalength

        for j in range(datalength):
            for line in oxygen:
                match int(line[j]):
                    case 0: zeros[j] += 1
                    case 1: ones[j] += 1

        if len(oxygen) == 1:
            break
        if zeros[i] <= ones[i]:
            oxygen = [x for x in oxygen if int(x[i]) == 1]
        else:
            oxygen = [x for x in oxygen if int(x[i]) == 0]

    co2 = [x for x in data]
    for i in range(datalength):
        zeros = [0] * datalength
        ones = [0] * datalength

        for j in range(datalength):
            for line in co2:
                match int(line[j]):
                    case 0: zeros[j] += 1
                    case 1: ones[j] += 1

        if len(co2) == 1:
            break
        if ones[i] >= zeros[i]:
            co2 = [x for x in co2 if int(x[i]) == 0]
        else:
            co2 = [x for x in co2 if int(x[i]) == 1]

    oxygen_total = "".join(map(str, oxygen))
    co2_total = "".join(map(str, co2))

    print(int(oxygen_total, 2))
    print(int(co2_total, 2))

    return int(oxygen_total, 2) * int(co2_total, 2)
    pass


data = open("src/day03/day03.txt", "r").readlines()
data = [line[:-1] for line in data]

# data = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010",
# ]

print(part1(data))
print(part2(data))
