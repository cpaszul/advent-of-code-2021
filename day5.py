from collections import Counter
import re

DEFAULT_INPUT = 'day5.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    vents = Counter()
    with open(loc) as f:
        for line in f.readlines():
            x0, y0, x1, y1 = map(int, re.findall(r'\d+', line))
            if x0 == x1:
                min_y = min(y0, y1)
                max_y = max(y0, y1)
                for y in range(min_y, max_y + 1):
                    vents[(x0, y)] += 1
            elif y0 == y1:
                min_x = min(x0, x1)
                max_x = max(x0, x1)
                for x in range(min_x, max_x + 1):
                    vents[(x, y0)] += 1
    return sum(1 for value in vents.values() if value > 1)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    vents = Counter()
    with open(loc) as f:
        for line in f.readlines():
            x0, y0, x1, y1 = map(int, re.findall(r'\d+', line))
            if x0 == x1:
                min_y = min(y0, y1)
                max_y = max(y0, y1)
                for y in range(min_y, max_y + 1):
                    vents[(x0, y)] += 1
            elif y0 == y1:
                min_x = min(x0, x1)
                max_x = max(x0, x1)
                for x in range(min_x, max_x + 1):
                    vents[(x, y0)] += 1
            else:
                x = x0
                y = y0
                if x0 < x1:
                    if y0 < y1: #x increases, y increases
                        while x <= x1 and y <= y1:
                            vents[(x, y)] += 1
                            x += 1
                            y += 1
                    else: #x increases, y decreases
                        while x <= x1 and y >= y1:
                            vents[(x, y)] += 1
                            x += 1
                            y -= 1
                else:
                    if y0 < y1: #x decreases, y increases
                        while x >= x1 and y <= y1:
                            vents[(x, y)] += 1
                            x -= 1
                            y += 1
                    else: #x decreases, y decreases
                        while x >= x1 and y >= y1:
                            vents[(x, y)] += 1
                            x -= 1
                            y -= 1
    return sum(1 for value in vents.values() if value > 1)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
