from aocd import data

def part1(lines):


    # lines = open("src/day01/day01.txt","r").readlines()
    # lines = open("src/day01/2000testcase.txt","r").readlines()

    last = int(lines[0])
    current = int(lines[0])
    increases = 0

    for i in range(1,len(lines)):
        last = lines[i-1]
        current = lines[i]
        if int(current) > int(last):
            increases = increases + 1

    # print(lines[len(lines)-1])
    print(increases)

def part2(lines):
    last_window = []
    current_window = []
    increases = 0

    for i in range(3,len(lines)):
        last_window_A = lines[i-3]
        last_window_B = lines[i-2]
        current_window_A= lines[i-2]
        last_window_C  = lines[i-1]
        current_window_B = lines[i-1]
        current_window_C = lines[i]

        last = int(last_window_A) + int(last_window_B) + int(last_window_C)
        current = int(current_window_A) + int(current_window_B) + int(current_window_C)

        # print(last, current)

        if int(current) > int(last):
            increases = increases + 1
    
    print(increases)

example = [
    "199",
    "200",
    "208",
    "210",
    "200",
    "207",
    "240",
    "269",
    "260",
    "263",
]

part1(data.splitlines())
part2(data.splitlines())
