#from aocd import lines

def part1(data):
    horizontal = 0
    depth = 0

    for tuple in data:
        tuple = tuple.split(" ")
        command, number = tuple
        
        match str(command):
            case "forward":
                horizontal = horizontal + int(number)
            case "down":
                depth = depth + int(number)
            case "up":
                depth = depth - int(number)

    return horizontal * depth

def part2(data):
    horizontal = 0
    depth = 0
    aim = 0

    for tuple in data:
        tuple = tuple.split(" ")
        command, number = tuple
        n = int(number)
        
        match str(command):
            case "forward":
                horizontal = horizontal + n
                depth = depth + (aim * n)
            case "down":
                aim = aim + n
            case "up":
                aim = aim - n

    return horizontal * depth

data = open("src/day02/day02.txt","r").readlines()

# data = [
#     "forward 5",
#     "down 5",
#     "forward 8",
#     "up 3",
#     "down 8",
#     "forward 2",
# ]

print(len(data))
print(part1(data))
print(part2(data))
