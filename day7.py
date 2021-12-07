from functools import cache

DEFAULT_INPUT = 'day7.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        positions = list(map(int, f.readline().split(',')))
    min_num = min(positions)
    max_num = max(positions)
    costs = []
    for pos in range(min_num, max_num + 1):
        costs.append(sum(abs(p - pos) for p in positions))
    costs.sort()
    return costs[0]

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        positions = list(map(int, f.readline().split(',')))
    min_num = min(positions)
    max_num = max(positions)
    costs = []
    for pos in range(min_num, max_num + 1):
        costs.append(alignment_cost(positions, pos))
    costs.sort()
    return costs[0]

def alignment_cost(nums: list[int], position: int) -> int:
    return sum(fuel_cost(abs(n - position)) for n in nums)

@cache
def fuel_cost(steps: int) -> int:
    total = 0
    i = 1
    while i <= steps:
        total += i
        i += 1
    return total

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
