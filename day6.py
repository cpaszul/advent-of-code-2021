from collections import Counter

DEFAULT_INPUT = 'day6.txt'

def day_6(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        fish = Counter(map(int, f.readline().split(',')))
    for i in range(256):
        new_fish = Counter()
        for turn, fish_num in fish.items():
            if turn == 0:
                new_fish[6] += fish_num
                new_fish[8] += fish_num
            else:
                new_fish[turn - 1] += fish_num
        fish = new_fish
        if i == 79:
            part_1_result = sum(fish.values())
    return part_1_result, sum(fish.values())

if __name__ == '__main__':
    part_1, part_2 = day_6()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
