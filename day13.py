import re

DEFAULT_INPUT = 'day13.txt'

def day_13(loc: str = DEFAULT_INPUT) -> tuple[int, set[tuple[int, int]]]:
    points = set()
    folds = []
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'(\d+),(\d+)', line):
                x, y = map(int, (m.group(1), m.group(2)))
                points.add((x, y))
            elif m := re.match(r'fold along (\w)=(\d+)', line):
                folds.append((m.group(1), int(m.group(2))))
    points = fold(points, *folds[0])
    part_1_result = len(points)
    for f in folds[1:]:
        points = fold(points, *f)
    return part_1_result, points

# move_amount = x - fold_line;new_x = fold_line - move_amount ->
# new_x = fold_line - (x - fold_line) -> new_x = 2 * fold_line - x
def fold(points: set[tuple[int, int]], fold_dir: str, fold_line: int) -> set[tuple[int, int]]:
    new_points = set()
    for point in points:
        x, y = point
        if fold_dir == 'x' and x > fold_line:
            new_points.add((2 * fold_line - x, y))
        elif fold_dir == 'y' and y > fold_line:
            new_points.add((x, 2 * fold_line - y))
        else:
            new_points.add(point)
    return new_points

def draw(points: set[tuple[int, int]]) -> None:
    max_x = max(points, key=lambda p:p[0])[0]
    max_y = max(points, key=lambda p:p[1])[1]
    rows = []
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            if (x, y) in points:
                row += '#'
            else:
                row += ' '
        rows.append(row)
    print('\n'.join(rows))
        
if __name__ == '__main__':
    part_1, part_2 = day_13()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:')
    draw(part_2)
