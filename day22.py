from collections import defaultdict
import re

DEFAULT_INPUT = 'day22.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    pattern = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    steps = []
    region = defaultdict(bool)
    with open(loc) as f:
        for line in f.readlines():
            m = pattern.match(line)
            steps.append((m.group(1) == 'on',
                          int(m.group(2)), int(m.group(3)),
                          int(m.group(4)), int(m.group(5)),
                          int(m.group(6)), int(m.group(7))))
    for step in steps:
        val, x_min, x_max, y_min, y_max, z_min, z_max = step
        for x in range(max(-50, x_min), min(50, x_max) + 1):
            for y in range(max(-50, y_min), min(50, y_max) + 1):
                for z in range(max(-50, z_min), min(50, z_max) + 1):
                    region[(x, y, z)] = val
    return sum(region.values())
             
def part_2(loc: str = DEFAULT_INPUT):
    with open(loc) as f:
       pass
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
