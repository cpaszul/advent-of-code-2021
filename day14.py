from collections import Counter
import re

DEFAULT_INPUT = 'day14.txt'

def day_14(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    rules = {}
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'(\w\w) -> (\w)', line):
                rules[m.group(1)] = m.group(2)
            elif m := re.match(r'(\w+)', line):
                polymer = m.group(1)
    start = polymer[0]
    end = polymer[-1]
    polymer_pairs = Counter()
    for a, b in zip(polymer, polymer[1:]):
        polymer_pairs[a + b] += 1
    for i in range(40):
        new_pairs = Counter()
        for pair in polymer_pairs:
            a, b = pair
            insert = rules[pair]
            new_pairs[a + insert] += polymer_pairs[pair]
            new_pairs[insert + b] += polymer_pairs[pair]
        polymer_pairs = new_pairs
        if i == 9:
            elem_count = get_count(polymer_pairs, start, end)
            part_1_result = max(elem_count.values()) - min(elem_count.values())
    elem_count = get_count(polymer_pairs, start, end)
    return part_1_result, max(elem_count.values()) - min(elem_count.values())

def get_count(pairs: dict[str, int], start: str, end: str) -> dict[str, int]:
    elem_count = Counter()
    for pair in pairs:
        a, b = pair
        elem_count[a] += pairs[pair]
        elem_count[b] += pairs[pair]
    elem_count[start] += 1
    elem_count[end] += 1
    for elem in elem_count:
        elem_count[elem] //= 2
    return elem_count
        
        
if __name__ == '__main__':
    part_1, part_2 = day_14()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)

