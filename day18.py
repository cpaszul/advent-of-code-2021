from math import floor, ceil
from itertools import permutations
import re

DEFAULT_INPUT = 'day18.txt'

class Snail:
    def __init__(self, line: str) -> None:
        self.snail = list(int(char) if char.isdigit() else char for char in line)
        self.reduce()

    def __str__(self) -> str:
        return ''.join(str(ele) if isinstance(ele, int) else ele for ele in self.snail)

    def reduce(self) -> None:
        if i := self.has_four_depth():
            self.explode(i)
            self.reduce()
        to_split = []
        for index, ele in enumerate(self.snail):
            if isinstance(ele, int) and ele > 9:
                to_split.append(index)
        if to_split:
            self.split(to_split[0])
            self.reduce()

    def explode(self, i: int) -> None:
        num_1 = self.snail[i + 1]
        num_2 = self.snail[i + 3]
        left_num = i
        while True:
            if left_num == 0:
                break
            if isinstance(self.snail[left_num], int):
                self.snail[left_num] += num_1
                break
            left_num -= 1
        right_num = i + 4
        while True:
            if right_num == len(self.snail):
                break
            if isinstance(self.snail[right_num], int):
                self.snail[right_num] += num_2
                break
            right_num += 1
        self.snail = self.snail[:i] + [0] + self.snail[i + 5:]

    def has_four_depth(self) -> int:
        depth = -1
        for index, ele in enumerate(self.snail):
            if ele == '[':
                depth += 1
                if depth == 4:
                    return index
            if ele == ']':
                depth -= 1
        return 0

    def split(self, i: int) -> None:
        num = self.snail[i]/2
        self.snail = self.snail[:i] + ['['] + [floor(num)] + [','] + [ceil(num)] + [']'] + self.snail[i + 1:]

    def __add__(self, other):
        if isinstance(other, Snail):
            return Snail('[' + str(self) + ',' + str(other) + ']')
        else:
            return NotImplemented

    def magnitude(self) -> int:
        mag = str(self)
        while s := re.search(r'\[\d+,\d+\]', mag):
            i = s.start()
            j = s.end()
            left, right = map(int, mag[i + 1:j - 1].split(','))
            mag = mag[:i] + str(3 * left + 2 * right) + mag[j:]
        return int(mag)

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        nums = list(Snail(line.rstrip()) for line in f.readlines())
    total = nums[0]
    for num in nums[1:]:
        total += num
    return total.magnitude()

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        nums = list(Snail(line.rstrip()) for line in f.readlines())
    mags = []
    for num_a, num_b in permutations(nums, 2):
        num_sum = num_a + num_b
        mags.append(num_sum.magnitude())
    return max(mags)
    
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
