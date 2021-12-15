import heapq

DEFAULT_INPUT = 'day15.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = []
    with open(loc) as f:
        for line in f.readlines():
            grid.append(list(map(int, list(line.rstrip()))))
    initial_state = (0, (0, 0))
    h = [initial_state]
    visited = set()
    while h:
        risk, point = heapq.heappop(h)
        if point == (99, 99):
            return risk
        if point in visited:
            continue
        visited.add(point)
        all_adj = adjacent(*point, 100)
        for adj in all_adj:
            i, j = adj
            new_state = (risk + grid[j][i], adj)
            heapq.heappush(h, new_state)

def adjacent(x: int, y: int, max_size: int) -> list[tuple[int, int]]:
    potential = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(i, j) for i, j in potential if 0 <= i < max_size and 0 <= j < max_size]

def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = []
    with open(loc) as f:
        for line in f.readlines():
            grid.append(list(map(int, list(line.rstrip()))))
    initial_state = (0, (0, 0))
    h = [initial_state]
    visited = set()
    while h:
        risk, point = heapq.heappop(h)
        if point == (499, 499):
            return risk
        if point in visited:
            continue
        visited.add(point)
        all_adj = adjacent(*point, 500)
        for adj in all_adj:
            i, j = adj
            new_state = (risk + get_risk(grid, i, j), adj)
            heapq.heappush(h, new_state)

def get_risk(grid: list[list[int]], x: int, y: int) -> int:
    x_base = x % 100
    x_mod = x // 100
    y_base = y % 100
    y_mod = y // 100
    val = grid[y_base][x_base] + x_mod + y_mod
    while val > 9:
        val -= 9
    return val
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
