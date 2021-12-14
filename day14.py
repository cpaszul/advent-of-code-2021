from collections import Counter
import re

DEFAULT_INPUT = 'day14.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    rules = {}
    with open(loc) as f:
        for line in f.readlines():
            if m := re.match(r'(\w\w) -> (\w)', line):
                rules[m.group(1)] = m.group(2)
            elif m := re.match(r'(\w+)', line):
                polymer = m.group(1)
    for _ in range(10):
        polymer = pair_insert(polymer, rules)
    c = Counter(polymer)
    return max(c.values()) - min(c.values())
    
def pair_insert(polymer: str, rules: dict[str, str]) -> str:
    new_polymer = []
    for i in range(1, len(polymer)):
        char_b = polymer[i]
        char_a = polymer[i - 1]
        if not new_polymer or new_polymer[-1] != (char_a, i - 1):
            new_polymer.append((char_a, i - 1))
        if char_a + char_b in rules:
            new_polymer.append((rules[char_a + char_b], -1))
        new_polymer.append((char_b, i))
    return ''.join(t[0] for t in new_polymer)      

def part_2(loc: str = DEFAULT_INPUT) -> int:
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
    for _ in range(40):
        new_pairs = Counter()
        for pair in polymer_pairs:
            a, b = pair
            insert = rules[pair]
            new_pairs[a + insert] += polymer_pairs[pair]
            new_pairs[insert + b] += polymer_pairs[pair]
        polymer_pairs = new_pairs
    c = get_count(polymer_pairs, start, end)
    return max(c.values()) - min(c.values())

'''
NNCB -> NN: 1, NC: 1, CB: 1 -> N: 3;2, C: 2;1, B: 1;1
NCNBCHB -> NC: 1, CN: 1, NB: 1, BC: 1, CH: 1, HB: 1 -> N: 3;2, C: 4;2, B: 3;2

initial thought: add 1 to the ends, take half
'''
def get_count(pairs: dict[str, int], start: str, end: str) -> dict[str, int]:
    c = Counter()
    for pair in pairs:
        a, b = pair
        c[a] += pairs[pair]
        c[b] += pairs[pair]
    c[start] += 1
    c[end] += 1
    for key in c:
        c[key] //= 2
    return c
        
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())

