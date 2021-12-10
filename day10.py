from collections import deque

DEFAULT_INPUT = 'day10.txt'

def day_10(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = list(line.rstrip() for line in f.readlines())
    error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    total_error_score = 0
    total_completion_scores = []
    for line in lines:
        corrupted, result = complete_line(line)
        if corrupted:
            total_error_score += error_scores[result]
        else:
            score = 0
            for char in result:
                score *= 5
                score += completion_scores[char]
            total_completion_scores.append(score)
    total_completion_scores.sort()
    return total_error_score, total_completion_scores[len(total_completion_scores)//2]

def complete_line(line: str) -> tuple[bool, str]:
    opening_chars = '([{<'
    pairs = {'<': '>', '{': '}', '(': ')', '[': ']'}
    d = deque()
    for char in line:
        if char in opening_chars:
            d.append(char)
        else:
            opening = d.pop()
            if pairs[opening] == char:
                continue
            else:
                return (True, char)
    to_complete = ''
    while d:
        to_complete += pairs[d.pop()]
    return (False, to_complete)
    

if __name__ == '__main__':
    part_1, part_2 = day_10()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
