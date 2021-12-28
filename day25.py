DEFAULT_INPUT = 'day25.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                grid[(x, y)] = cell
    max_x = max(grid, key=lambda t:t[0])[0]
    max_y = max(grid, key=lambda t:t[1])[1]
    def down(point: tuple[int, int]) -> tuple[int, int]:
        x, y = point
        y += 1
        y %= max_y + 1
        return x, y
    def right(point: tuple[int, int]) -> tuple[int, int]:
        x, y = point
        x += 1
        x %= max_x + 1
        return x, y
    i = 1
    while True:
        to_move_right = []
        to_move_down = []
        no_right_move = False
        no_down_move = False
        for key, value in grid.items():
            if value == '>' and grid[right(key)] == '.':
                to_move_right.append(key)
        if not to_move_right:
            no_right_move = True
        for key in to_move_right:
            grid[key] = '.'
            grid[right(key)] = '>'
        for key, value in grid.items():
            if value == 'v' and grid[down(key)] == '.':
                to_move_down.append(key)
        if not to_move_down:
            no_down_move = True
        if no_right_move and no_down_move:
            return i
        for key in to_move_down:
            grid[key] = '.'
            grid[down(key)] = 'v'
        i += 1
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
