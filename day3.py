from collections import Counter
from typing import Callable

DEFAULT_INPUT = 'day3.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    ones_counts = Counter()
    numbers = 0
    with open(loc) as f:
        for line in f.readlines():
            numbers += 1
            for i, c in enumerate(line.rstrip()):
                if c == '1':
                    ones_counts[i] += 1
    gamma = ''
    epsilon = ''
    for digit in range(len(ones_counts)):
        if ones_counts[digit] < numbers / 2:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        numbers = [line.rstrip() for line in f.readlines()]
    return filter_numbers(numbers.copy(), lambda x, y: x > y, '1') * \
           filter_numbers(numbers.copy(), lambda x, y: x < y, '0')

def filter_numbers(numbers: list[str], op: Callable[[int, int], bool], equal_val: str) -> int:
    size = len(numbers[0])
    for i in range(size):
        ones_count = sum(1 for number in numbers if number[i] == '1')
        if ones_count == len(numbers) / 2:
            filter_value = equal_val
        elif op(ones_count, len(numbers) / 2):
            filter_value = '1'
        else:
            filter_value = '0'
        numbers = [number for number in numbers if number[i] == filter_value]
        if len(numbers) == 1:
            return int(numbers[0], 2)

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
