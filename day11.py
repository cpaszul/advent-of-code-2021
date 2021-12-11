DEFAULT_INPUT = 'day11.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, value in enumerate(line.rstrip()):
                grid[(x, y)] = int(value)
    total_flashes = 0
    for _ in range(100):
        total_flashes += step(grid)
    return total_flashes

def adjacent(x: int, y: int) -> list[tuple[int, int]]:
    return [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]

def step(grid: dict[tuple[int, int], int]) -> int:
    for key in grid:
        grid[key] += 1
    flashed = set()
    while True:
        to_flash = [key for key, value in grid.items() if key not in flashed and value > 9]
        if not to_flash:
            for key in flashed:
                grid[key] = 0
            return len(flashed)
        for key in to_flash:
            flashed.add(key)
            adj_cells = [adj for adj in adjacent(*key) if adj in grid]
            for adj in adj_cells:
                grid[adj] += 1

def draw(grid: dict[tuple[int, int], int]) -> None:
    rows = []
    for y in range(10):
        row = ''
        for x in range(10):
            row += str(grid[(x, y)])
        rows.append(row)
    print('\n'.join(rows))

def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, value in enumerate(line.rstrip()):
                grid[(x, y)] = int(value)
    i = 0
    while True:
        flashes = step(grid)
        i += 1
        if flashes == 100:
            return i
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
