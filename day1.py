DEFAULT_INPUT = 'day1.txt'

def day_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        depths = [int(line) for line in f.readlines()]
    sums = [a + b + c for a, b, c in zip(depths, depths[1:], depths[2:])]
    return sum(1 for a, b in zip(depths, depths[1:]) if a < b), \
           sum(1 for a, b in zip(sums, sums[1:]) if a < b)

if __name__ == '__main__':
    part_1, part_2 = day_1()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
