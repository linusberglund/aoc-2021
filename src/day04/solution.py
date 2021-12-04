def read_winning_numbers(data):
    return [int(n) for n in data[0].split(",") if n.isdigit()]


def read_bingo_boards(data):
    board_lines = []

    for index, line in enumerate(data):
        if index == 0:
            continue
        if not line.strip():
            continue

        board_lines.append([int(n) for n in line.split() if n.isdigit()])

    boards = []
    for i in range(0, len(board_lines), 5):
        boards.append(board_lines[i : i + 5])

    return boards


def find_number_in_board(number, board):
    try:
        x = [x for x in board if number in x][0]
        return (board.index(x), x.index(number))
    except:
        return False


def find_number_in_all_boards(number, boards):

    board_line_number = []

    for board_index, b in enumerate(boards):
        result = find_number_in_board(number, b)
        if result:
            board_line_number.append((board_index, result[0], result[1]))

    return board_line_number


def check_board_win(board_marked):
    for line_index, line in enumerate(board_marked):
        if sum(line) == 5:
            return (line_index, None)

    column = [False for i in range(5)]

    for line in board_marked:
        for column_index, boolean in enumerate(line):
            column[column_index] = column[column_index] + boolean

    for col_index, col in enumerate(column):
        if col == 5:
            return (None, col_index)

    return False


def calc_unmarked(board, board_marked):
    sum = 0

    for line in range(5):
        for col in range(5):
            if board_marked[line][col] == False:
                sum += board[line][col]

    return sum


def part1(data):
    numbers = read_winning_numbers(data)
    boards = read_bingo_boards(data)

    # for board_index, board in enumerate(boards_marked):
    #     for line_index, line in enumerate(board):
    #         for entry_index, entry in enumerate(line):
    #             boards_marked[board_index][line_index][entry_index] = False

    boards_marked = [
        [[False for i in range(5)] for i in range(5)] for i in range(len(boards))
    ]

    for number in numbers:
        to_be_marked = find_number_in_all_boards(number, boards)

        for entry in to_be_marked:
            boards_marked[entry[0]][entry[1]][entry[2]] = True

        for index, board in enumerate(boards):
            board_marked = boards_marked[index]
            check = check_board_win(board_marked)
            if check:
                return calc_unmarked(board, board_marked) * number


def part2(data):
    numbers = read_winning_numbers(data)
    boards = read_bingo_boards(data)

    boards_marked = [
        [[False for i in range(5)] for i in range(5)] for i in range(len(boards))
    ]

    board_final_scores = []
    boards_to_skip = set()

    for number in numbers:
        to_be_marked = find_number_in_all_boards(number, boards)

        for entry in to_be_marked:
            boards_marked[entry[0]][entry[1]][entry[2]] = True

        for index, board in enumerate(boards):
            if index in boards_to_skip:
                continue
            board_marked = boards_marked[index]
            check = check_board_win(board_marked)
            if check:
                boards_to_skip.add(index)
                board_final_scores.append(calc_unmarked(board, board_marked) * number)

    return board_final_scores[-1]


data = open("src/day04/day04.txt", "r").readlines()
# data = open("src/day04/example.txt", "r").readlines()
# data = open("src/day04/test1.txt", "r").readlines()
# data = open("src/day04/test2.txt", "r").readlines()

data = [line.strip("\n") for line in data]

print(part1(data))
print(part2(data))
