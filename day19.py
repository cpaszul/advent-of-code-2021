from itertools import combinations
from collections import deque
import re

DEFAULT_INPUT = 'day19.txt'
ROTATIONS = [('+x', '+y', '+z'), ('-y', '+x', '+z'), ('-x', '-y', '+z'), ('+y', '-x', '+z'),
             ('-z', '+y', '+x'), ('-y', '-z', '+x'), ('+z', '-y', '+x'), ('+y', '+z', '+x'),
             ('-z', '-x', '+y'), ('-x', '+z', '+y'), ('+z', '+x', '+y'), ('+x', '-z', '+y'),
             ('+x', '-y', '-z'), ('-y', '-x', '-z'), ('-x', '+y', '-z'), ('+y', '+x', '-z'),
             ('-z', '-y', '-x'), ('-y', '+z', '-x'), ('+z', '+y', '-x'), ('+y', '-z', '-x'),
             ('+x', '+z', '-y'), ('+z', '-x', '-y'), ('-x', '-z', '-y'), ('-z', '+x', '-y')]

class Scanner:
    def __init__(self, number: int, beacons: list[tuple[int, int, int]], rot: tuple[int, int, int]):
        self.number = number
        self.beacons = []
        for x, y, z in beacons:
            if rot[0][1] == 'x':
                bx = x
            elif rot[0][1] == 'y':
                bx = y
            else:
                bx = z
            if rot[0][0] == '-':
                bx *= -1
            if rot[1][1] == 'x':
                by = x
            elif rot[1][1] == 'y':
                by = y
            else:
                by = z
            if rot[1][0] == '-':
                by *= -1
            if rot[2][1] == 'x':
                bz = x
            elif rot[2][1] == 'y':
                bz = y
            else:
                bz = z
            if rot[2][0] == '-':
                bz *= -1
            self.beacons.append((bx, by, bz))       
        if number == 0:
            self.position = (0, 0, 0)
            self.generate_real_beacons()
        else:
            self.position = None
        self.generate_distances()

    def __repr__(self):
        if self.position is None:
            return f'Scanner #{self.number} at unknown position'
        return f'Scanner #{self.number} at position {self.position}'

    def generate_distances(self):
        self.distances = {}
        for point_a, point_b in combinations(self.beacons, 2):
            points = [point_a, point_b]
            points.sort(key=lambda p:p[2])
            points.sort(key=lambda p:p[1])
            points.sort(key=lambda p:p[0])
            point_a, point_b = points
            distance = (point_b[0] - point_a[0],
                        point_b[1] - point_a[1],
                        point_b[2] - point_a[2])
            if distance in self.distances:
                print(self.distances[distance], point_a, point_b)
            self.distances[distance] = (point_a, point_b)

    def determine_position(self, other_scanner, shared_point: tuple[tuple[int, int, int], tuple[int, int, int]]):
        other_position = other_scanner.position
        other_point = shared_point[0]
        point = shared_point[1]
        x = other_position[0] + other_point[0] - point[0]
        y = other_position[1] + other_point[1] - point[1]
        z = other_position[2] + other_point[2] - point[2]
        self.position = (x, y, z)
        self.generate_real_beacons()

    def generate_real_beacons(self):
        self.real_beacons = set()
        for x, y, z in self.beacons:
            real_x = x + self.position[0]
            real_y = y + self.position[1]
            real_z = z + self.position[2]
            self.real_beacons.add((real_x, real_y, real_z))
        

def day_19(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    known = []
    known_nums = [0]
    unknown = deque()
    with open(loc) as f:
        num = None
        beacons = []
        for line in f.readlines():
            if m := re.match(r'--- scanner (\d+) ---', line):
                num = int(m.group(1))
            elif m := re.match(r'(-?\d+),(-?\d+),(-?\d+)', line):
                x, y, z = map(int, m.groups())
                beacons.append((x, y, z))
            else:
                if num == 0:
                    known.append(Scanner(0, beacons, ('+x', '+y', '+z')))
                else:
                    for rot in ROTATIONS:
                        unknown.append(Scanner(num, beacons, rot))
                beacons = []
        if beacons:
            for rot in ROTATIONS:
                unknown.append(Scanner(num, beacons, rot))
    while unknown:
        scanner_b = unknown.popleft()
        if scanner_b.number in known_nums:
            continue
        solved = False
        for scanner_a in known:
            if len(shared := common_points(scanner_a, scanner_b)) >= 12:
                solved = True
                scanner_b.determine_position(scanner_a, shared.pop())
                break
        if solved:
            known.append(scanner_b)
            known_nums.append(scanner_b.number)
            continue
        unknown.append(scanner_b)
    all_beacons = set()
    for scanner in known:
        all_beacons |= scanner.real_beacons
    scanner_distances = []
    for scanner_a, scanner_b in combinations(known, 2):
        scanner_distances.append(scanner_distance(scanner_a, scanner_b))
    return len(all_beacons), max(scanner_distances)

def common_points(scanner_a, scanner_b) -> set[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    shared = set()
    for distance in scanner_a.distances:
        if distance in scanner_b.distances:
            point_a = (scanner_a.distances[distance][0], scanner_b.distances[distance][0])
            point_b = (scanner_a.distances[distance][1], scanner_b.distances[distance][1])
            shared.add(point_a)
            shared.add(point_b)
    return shared

def scanner_distance(scanner_a, scanner_b):
    p_a = scanner_a.position
    p_b = scanner_b.position
    return abs(p_a[0] - p_b[0]) + (p_a[1] - p_b[1]) + (p_a[2] - p_b[2])
        
if __name__ == '__main__':
    part_1, part_2 = day_19()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
