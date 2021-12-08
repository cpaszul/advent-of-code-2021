DEFAULT_INPUT = 'day8.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    outputs = []
    with open(loc) as f:
        for line in f.readlines():
            outputs.append(list(map(len, line.rstrip().split('| ')[1].split(' '))))
    simple_digits = 0
    for output in outputs:
        simple_digits += len(list(digit for digit in output if digit in (2, 4, 3, 7)))
    return simple_digits

def part_2(loc: str = DEFAULT_INPUT) -> int:
    lines = []
    with open(loc) as f:
        for line in f.readlines():
            left, right = line.rstrip().split(' | ')
            left = list(map(frozenset, left.split(' ')))
            right = list(map(frozenset, right.split(' ')))
            lines.append((left, right))
    return sum(line_num(*line) for line in lines)

def line_num(left: list[frozenset[str]], right: list[frozenset[str]]) -> int:
    solutions = solve_display(left)
    num_str = ''
    for s in right:
        num_str += solutions[s]
    return int(num_str)

''' Notes:
length 2 -> 1
length 3 -> 7
length 4 -> 4
length 5 -> 2, 3, 5
length 6 -> 0, 6, 9
length 7 -> 8

UNSOLVED: 2, 3, 5 | 0, 6, 9
3 contains both segments of 1, 2 and 5 do not
6 contains 1 segment of 1, 0 and 9 contain both
UNSOLVED: 2, 5 | 0, 9
5 is entirely contained within 6, 2 is not
9 contains all of 3, 0 does not
'''

def solve_display(displays: list[frozenset[str]]) -> dict[frozenset[str], str]:
    solutions = {}
    len_5 = []
    len_6 = []
    for display in displays:
        if len(display) == 2:
            solutions['1'] = display
        elif len(display) == 3:
            solutions['7'] = display
        elif len(display) == 4:
            solutions['4'] = display
        elif len(display) == 5:
            len_5.append(display)
        elif len(display) == 6:
            len_6.append(display)
        else:
            solutions['8'] = display
    while '3' not in solutions:
        potential_3 = len_5.pop(0)
        if len(potential_3 & solutions['1']) == 2:
            solutions['3'] = potential_3
        else:
            len_5.append(potential_3)
    while '6' not in solutions:
        potential_6 = len_6.pop(0)
        if len(potential_6 & solutions['1']) == 1:
            solutions['6'] = potential_6
        else:
            len_6.append(potential_6)
    potential_5 = len_5[0]
    if len(potential_5 & solutions['6']) == 5:
        solutions['5'] = potential_5
        solutions['2'] = len_5[1]
    else:
        solutions['2'] = potential_5
        solutions['5'] = len_5[1]
    potential_9 = len_6[0]
    if len(potential_9 & solutions['3']) == 5:
        solutions['9'] = potential_9
        solutions['0'] = len_6[1]
    else:
        solutions['0'] = potential_9
        solutions['9'] = len_6[1]
    return {value: key for key, value in solutions.items()}
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
