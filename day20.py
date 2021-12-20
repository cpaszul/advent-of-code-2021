from collections import defaultdict

DEFAULT_INPUT = 'day20.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    image = defaultdict(bool)
    with open(loc) as f:
        rule = f.readline().rstrip()
        f.readline()
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                image[(x, y)] = cell == '#'
    image = enhance(image, rule, True)
    image = enhance(image, rule, False)
    return sum(image.values())

def enhance(image: dict[tuple[int, int], bool], rule: str, default: bool) -> dict[tuple[int, int], bool]:
    min_x = min(image.keys(), key=lambda t:t[0])[0]
    min_y = min(image.keys(), key=lambda t:t[1])[1]
    max_x = max(image.keys(), key=lambda t:t[0])[0]
    max_y = max(image.keys(), key=lambda t:t[1])[1]
    sequence = ((-1, -1), (0, -1), (1, -1),
                (-1,  0), (0,  0), (1,  0),
                (-1,  1), (0,  1), (1,  1))
    new_image = defaultdict(lambda: default)
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            bin_num = ''
            for dx, dy in sequence:
                bin_num += '1' if image[(x + dx, y + dy)] else '0'
            index = int(bin_num, 2)
            new_image[(x, y)] = rule[index] == '#'
    return new_image

def part_2(loc: str = DEFAULT_INPUT) -> int:
    image = defaultdict(bool)
    with open(loc) as f:
        rule = f.readline().rstrip()
        f.readline()
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                image[(x, y)] = cell == '#'
    for _ in range(25):
        image = enhance(image, rule, True)
        image = enhance(image, rule, False)
    return sum(image.values())
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
