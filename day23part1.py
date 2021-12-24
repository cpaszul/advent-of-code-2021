from collections import defaultdict, deque
import heapq

DEFAULT_INPUT = 'day23.txt'

Point = tuple[int, int]
State = tuple[frozenset[Point], frozenset[Point], frozenset[Point], frozenset[Point], frozenset[Point]]
HALLWAYS = set([(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)])
INVALID = set([(3, 1), (5, 1), (7, 1), (9, 1)])
A_FINAL = set([(3, 2), (3, 3)])
B_FINAL = set([(5, 2), (5, 3)])
C_FINAL = set([(7, 2), (7, 3)])
D_FINAL = set([(9, 2), (9, 3)])
ALL_POINTS = HALLWAYS | INVALID | A_FINAL | B_FINAL | C_FINAL | D_FINAL

def part_1(loc: str = DEFAULT_INPUT) -> int:
    init_open_points = set()
    init_a_s = set()
    init_b_s = set()
    init_c_s = set()
    init_d_s = set()
    energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            for x, cell in enumerate(row.rstrip()):
                if cell == '.':
                    init_open_points.add((x, y))
                if cell == 'A':
                    init_a_s.add((x, y))
                if cell == 'B':
                    init_b_s.add((x, y))
                if cell == 'C':
                    init_c_s.add((x, y))
                if cell == 'D':
                    init_d_s.add((x, y))
    starting_state = (frozenset(init_open_points), frozenset(init_a_s),
                      frozenset(init_b_s), frozenset(init_c_s), frozenset(init_d_s))
    seen = set()
    dists = distances()
    h = [(0, starting_state)]
    while h:
        energy_cost, state = heapq.heappop(h)
        open_spaces, a_s, b_s, c_s, d_s = state
        if winning_state(state):
            return energy_cost
        if state in seen:
            continue
        seen.add(state)
        can_move = set()
        for a in a_s:
            if a != (3, 3) and a_s != A_FINAL:
                can_move.add((a, 'A'))
        for b in b_s:
            if b != (5, 3) and b_s != B_FINAL:
                can_move.add((b, 'B'))
        for c in c_s:
            if c != (7, 3) and c_s != C_FINAL:
                can_move.add((c, 'C'))
        for d in d_s:
            if d != (9, 3) and d_s != D_FINAL:
                can_move.add((d, 'D'))
        for point, amphi_type in can_move:
            destinations = get_valid_moves(state, point, amphi_type)
            for end_point in destinations:
                new_cost = energy_cost + dists[point][end_point] * energy[amphi_type]
                new_o_s = set(open_spaces)
                new_a_s = set(a_s)
                new_b_s = set(b_s)
                new_c_s = set(c_s)
                new_d_s = set(d_s)
                new_o_s.add(point)
                new_o_s.remove(end_point)
                if amphi_type == 'A':
                    new_a_s.add(end_point)
                    new_a_s.remove(point)
                if amphi_type == 'B':
                    new_b_s.add(end_point)
                    new_b_s.remove(point)
                if amphi_type == 'C':
                    new_c_s.add(end_point)
                    new_c_s.remove(point)
                if amphi_type == 'D':
                    new_d_s.add(end_point)
                    new_d_s.remove(point)
                new_state = (frozenset(new_o_s), frozenset(new_a_s), frozenset(new_b_s),
                             frozenset(new_c_s), frozenset(new_d_s))
                if new_state not in seen:
                    heapq.heappush(h, (new_cost, new_state))

def get_valid_moves(state: State, point: Point, amphi_type: str) -> list[Point]:
    o_s, a_s, b_s, c_s, d_s = state
    open_spaces = set(o_s)
    open_spaces -= INVALID
    if amphi_type == 'A':
        open_spaces -= B_FINAL
        open_spaces -= C_FINAL
        open_spaces -= D_FINAL
        if any(space in b_s or space in c_s or space in d_s for space in A_FINAL):
            open_spaces -= A_FINAL
    if amphi_type == 'B':
        open_spaces -= A_FINAL
        open_spaces -= C_FINAL
        open_spaces -= D_FINAL
        if any(space in a_s or space in c_s or space in d_s for space in B_FINAL):
            open_spaces -= B_FINAL
    if amphi_type == 'C':
        open_spaces -= A_FINAL
        open_spaces -= B_FINAL
        open_spaces -= D_FINAL
        if any(space in a_s or space in b_s or space in d_s for space in C_FINAL):
            open_spaces -= C_FINAL
    if amphi_type == 'D':
        open_spaces -= A_FINAL
        open_spaces -= B_FINAL
        open_spaces -= C_FINAL
        if any(space in a_s or space in b_s or space in c_s for space in D_FINAL):
            open_spaces -= D_FINAL
    if point in HALLWAYS:
        open_spaces -= HALLWAYS
    return [end_point for end_point in open_spaces if path_exists(state, point, end_point)]

def path_exists(state: State, start: Point, end: Point) -> bool:
    d = deque([start])
    seen = set([start])
    while d:
        current = d.popleft()
        for adj in adjacent(current):
            if adj == end:
                return True
            if adj in state[0] and adj not in seen:
                seen.add(adj)
                d.append(adj)
    return False

def distances() -> defaultdict[Point, dict[Point, int]]:
    dists = defaultdict(dict)
    for point in ALL_POINTS:
        d = deque([(point, 0)])
        seen = set([point])
        while d:
            current, dist = d.popleft()
            for adj in adjacent(current):
                if adj in ALL_POINTS and adj not in seen:
                    seen.add(adj)
                    dists[point][adj] = dist + 1
                    d.append((adj, dist + 1))
    return dists
    
def winning_state(state: State) -> bool:
    _, a_s, b_s, c_s, d_s = state
    return a_s == A_FINAL and b_s == B_FINAL and c_s == C_FINAL and d_s == D_FINAL

def adjacent(point: Point) -> list[Point]:
    x, y = point
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
