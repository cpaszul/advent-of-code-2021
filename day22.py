from collections import defaultdict, namedtuple
import re

DEFAULT_INPUT = 'day22.txt'

Cube = namedtuple('Cube', ['x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max'])        

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
             
def part_2(loc: str = DEFAULT_INPUT) -> int:
    pattern = re.compile(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
    instructs = []
    cubes = []
    with open(loc) as f:
        for line in f.readlines():
            m = pattern.match(line)
            instruct = (m.group(1) == 'on', Cube(int(m.group(2)), int(m.group(3)), int(m.group(4)),
                                                 int(m.group(5)), int(m.group(6)), int(m.group(7))))
            instructs.append(instruct)
    for instruct in instructs:
        new_cubes = []
        for cube in cubes:
            split_cubes = remove_cube(cube, instruct[1])
            new_cubes.extend(split_cubes)
        if instruct[0]:
            new_cubes.append(instruct[1])
        cubes = new_cubes
    return sum(volume(cube) for cube in cubes)

def remove_cube(cube: Cube, remove: Cube) -> list[Cube]:
    if not intersect(cube, remove):
        return [cube]
    new_cubes = []
    x_min, x_max, y_min, y_max, z_min, z_max = cube
    if x_min < remove.x_min:
        new_cubes.append(Cube(x_min, remove.x_min - 1,
                              y_min, y_max,
                              z_min, z_max))
        x_min = remove.x_min
    if x_max > remove.x_max:
        new_cubes.append(Cube(remove.x_max + 1, x_max,
                              y_min, y_max,
                              z_min, z_max))
        x_max = remove.x_max
    if y_min < remove.y_min:
        new_cubes.append(Cube(x_min, x_max,
                              y_min, remove.y_min - 1,
                              z_min, z_max))
        y_min = remove.y_min
    if y_max > remove.y_max:
        new_cubes.append(Cube(x_min, x_max,
                              remove.y_max + 1, y_max,
                              z_min, z_max))
        y_max = remove.y_max
    if z_min < remove.z_min:
        new_cubes.append(Cube(x_min, x_max,
                              y_min, y_max,
                              z_min, remove.z_min - 1))
    if z_max > remove.z_max:
        new_cubes.append(Cube(x_min, x_max,
                              y_min, y_max,
                              remove.z_max + 1, z_max))
    return new_cubes

def intersect(cube_a: Cube, cube_b: Cube) -> bool:
    return cube_b.x_min <= cube_a.x_max and cube_a.x_min <= cube_b.x_max and \
           cube_b.y_min <= cube_a.y_max and cube_a.y_min <= cube_b.y_max and \
           cube_b.z_min <= cube_a.z_max and cube_a.z_min <= cube_b.z_max

def volume(cube: Cube) -> int:
    return (cube.x_max + 1 - cube.x_min) * (cube.y_max + 1 - cube.y_min) * (cube.z_max + 1 - cube.z_min)
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
