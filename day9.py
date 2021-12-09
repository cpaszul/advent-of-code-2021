from collections import deque

DEFAULT_INPUT = 'day9.txt'

def day_9(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        grid = [list(map(int, list(line.rstrip()))) for line in f.readlines()]
    max_x = len(grid[0])
    max_y = len(grid)
    low_points = [(x, y) for y in range(max_y) for x in range(max_x) if is_low_point(x, y, grid)]
    basins = []
    for lp in low_points:
        basins.append(basin_size(lp, grid))
    basins.sort(reverse=True)
    return sum(1 + grid[lp[1]][lp[0]] for lp in low_points), basins[0] * basins[1] * basins[2]

def is_low_point(x: int, y: int, grid: list[list[int]]) -> bool:
    point = grid[y][x]
    adj = adjacent_points(x, y, grid)
    for i, j in adj:
        if point >= grid[j][i]:
            return False
    return True

def adjacent_points(x: int, y: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    max_x = len(grid[0])
    max_y = len(grid)
    potential = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    return [(i, j) for i, j in potential if 0 <= i < max_x and 0 <= j < max_y]

def basin_size(point: tuple[int, int], grid: list[list[int]]) -> int:
    basin = set([point])
    d = deque([point])
    while d:
        x, y = d.popleft()
        adj = adjacent_points(x, y, grid)
        for i, j in adj:
            if (i, j) not in basin and grid[j][i] != 9:
                d.append((i, j))
                basin.add((i, j))
    return len(basin)
        
if __name__ == '__main__':
    part_1, part_2 = day_9()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
