from collections import namedtuple
import re

DEFAULT_INPUT = 'day17.txt'

Rect = namedtuple('Rect', ['x0', 'x1', 'y0', 'y1'])

def day_17(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        m = re.findall(r'-?\d+', f.readline())
        rect = Rect(*map(int, m))
    max_y = -1
    valid_velocities = 0
    for dy in range(rect.y0, 250):
        for dx in range(1, rect.x1 + 1):
            y = highest_y(dx, dy, rect)
            if y is not None:
                max_y = max(max_y, y)
                valid_velocities += 1
    return max_y, valid_velocities
    
def point_within_rect(x: int, y: int, rect: tuple[int, int, int, int]) -> bool:
    return rect.x0 <= x <= rect.x1 and rect.y0 <= y <= rect.y1

def highest_y(dx: int, dy: int, rect: tuple[int, int, int, int]) -> int:
    x, y = 0, 0
    max_y = -1
    while True:
        x += dx
        y += dy
        max_y = max(max_y, y)
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        if point_within_rect(x, y, rect):
            return max_y
        if y < rect.y0:
            return None

        
if __name__ == '__main__':
    part_1, part_2 = day_17()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
