from collections import defaultdict, deque
from string import ascii_uppercase

DEFAULT_INPUT = 'day12.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    graph = defaultdict(list)
    big_caves = set()
    with open(loc) as f:
        for line in f.readlines():
            a, b = line.rstrip().split('-')
            graph[a].append(b)
            graph[b].append(a)
            if all(char in ascii_uppercase for char in a):
                big_caves.add(a)
            if all(char in ascii_uppercase for char in b):
                big_caves.add(b)
    d = deque([['start']])
    paths = 0
    while d:
        path = d.popleft()
        if path[-1] == 'end':
            paths += 1
            continue
        adjacent_nodes = graph[path[-1]]
        for adj in adjacent_nodes:
            if adj in big_caves or adj not in path:
                d.append(path + [adj])
    return paths

def part_2(loc: str = DEFAULT_INPUT) -> int:
    graph = defaultdict(list)
    big_caves = set()
    small_caves = set()
    with open(loc) as f:
        for line in f.readlines():
            a, b = line.rstrip().split('-')
            graph[a].append(b)
            graph[b].append(a)
            if all(char in ascii_uppercase for char in a):
                big_caves.add(a)
            elif a not in ('start', 'end'):
                small_caves.add(a)
            if all(char in ascii_uppercase for char in b):
                big_caves.add(b)
            elif b not in ('start', 'end'):
                small_caves.add(b)
    d = deque([(['start'], False)])
    paths = 0
    while d:
        path, twice_visited = d.popleft()
        if path[-1] == 'end':
            paths += 1
            continue
        adjacent_nodes = graph[path[-1]]
        for adj in adjacent_nodes:
            if adj in big_caves or adj not in path:
                d.append((path + [adj], twice_visited))
            if adj in small_caves and adj in path and not twice_visited:
                d.append((path + [adj], True))
    return paths
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
