DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    boards = []
    numbers = None
    with open(loc) as f:
        numbers = list(map(int, f.readline().split(',')))
        f.readline()
        board = []
        for line in f.readlines():
            if line == '\n':
                boards.append(board)
                board = []
            else:
                nums = [int(num) for num in line.split(' ') if num]
                board.append([(num, False) for num in nums])
        boards.append(board)
    winning_values = []
    for called_number in numbers:
        remaining_boards = []
        for board in boards:
            mark(board, called_number)
            if winning_board(board):
                winning_values.append(called_number * sum_unmarked(board))
            else:
                remaining_boards.append(board)
        boards = remaining_boards
    return winning_values[0], winning_values[-1]

def mark(board: list[list[tuple[int, bool]]], num: int) -> None:
    for row in board:
        for i, cell in enumerate(row):
            if cell[0] == num:
                row[i] = (num, True)

def winning_board(board: list[list[tuple[int, bool]]]) -> bool:
    for row in board:
        if all(cell[1] for cell in row):
            return True
    for y in range(5):
        if all(board[x][y][1] for x in range(5)):
            return True
    return False

def sum_unmarked(board: list[list[tuple[int, bool]]]) -> int:
    total = 0
    for row in board:
        for cell in row:
            if not cell[1]:
                total += cell[0]
    return total

if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
