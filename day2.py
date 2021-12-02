DEFAULT_INPUT = 'day2.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        moves = [((spl := line.split())[0], int(spl[1])) for line in f.readlines()]
    x, y = 0, 0
    for move_dir, move_amount in moves:
        if move_dir == 'forward':
            x += move_amount
        elif move_dir == 'up':
            y -= move_amount
        else:
            y += move_amount
    return x * y

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        moves = [((spl := line.split())[0], int(spl[1])) for line in f.readlines()]
    x, y, aim = 0, 0, 0
    for move_dir, move_amount in moves:
        if move_dir == 'forward':
            x += move_amount
            y += aim * move_amount
        elif move_dir == 'up':
            aim -= move_amount
        else:
            aim += move_amount
    return x * y

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
