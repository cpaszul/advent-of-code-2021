import re

DEFAULT_INPUT = 'day13.txt'

def day_13(loc: str = DEFAULT_INPUT) -> tuple[int, dict[tuple[int, int], bool]]:
    grid = {}
    folds = []
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'(\d+),(\d+)', line):
                x, y = map(int, (m.group(1), m.group(2)))
                grid[(x, y)] = True
            elif m := re.match(r'fold along (\w)=(\d+)', line):
                folds.append((m.group(1), int(m.group(2))))
    grid = fold(grid, *folds[0])
    part_1_result = len(grid)
    for f in folds[1:]:
        grid = fold(grid, *f)
    return part_1_result, grid

def fold(grid: dict[tuple[int, int], bool], fold_dir: str, fold_line: int) -> None:
    new_points = []
    for key in grid:
        if fold_dir == 'x' and key[0] > fold_line:
            move_amount = key[0] - fold_line
            new_points.append((fold_line - move_amount, key[1]))
            grid[key] = False
        if fold_dir == 'y' and key[1] > fold_line:
            move_amount = key[1] - fold_line
            new_points.append((key[0], fold_line - move_amount))
            grid[key] = False
    for point in new_points:
        grid[point] = True
    grid = {k:v for k, v in grid.items() if v}
    return grid

def draw(grid: dict[tuple[int, int], bool]) -> None:
    max_x = max(grid, key=lambda p:p[0])[0]
    max_y = max(grid, key=lambda p:p[1])[1]
    rows = []
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            if (x, y) in grid:
                row += '#'
            else:
                row += '.'
        rows.append(row)
    print('\n'.join(rows))
        
if __name__ == '__main__':
    part_1, part_2 = day_13()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:')
    draw(part_2)
