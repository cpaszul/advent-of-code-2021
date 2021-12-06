from collections import deque

DEFAULT_INPUT = 'day6.txt'

def day_6(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        fish = deque([0] * 9)
        for n in map(int, f.readline().split(',')):
            fish[n] += 1
    for i in range(256):
        fish[7] += fish[0]
        fish.rotate(-1)
        if i == 79:
            part_1_result = sum(fish)
    return part_1_result, sum(fish)

if __name__ == '__main__':
    part_1, part_2 = day_6()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
