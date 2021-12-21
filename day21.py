DEFAULT_INPUT = 'day21.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        player_one = [int(f.readline().split(' ')[-1]), 0]
        player_two = [int(f.readline().split(' ')[-1]), 0]
    player_one_turn = True
    dice = 1
    i = 0
    while True:
        move = 0
        for _ in range(3):
            move += dice
            dice += 1
            if dice == 101:
                dice = 1
            i += 1
        if player_one_turn:
            new_space = (player_one[0] + move)
            while new_space > 10:
                new_space -= 10
            player_one[1] += new_space
            player_one[0] = new_space
        else:
            new_space = (player_two[0] + move)
            while new_space > 10:
                new_space -= 10
            player_two[1] += new_space
            player_two[0] = new_space
        player_one_turn = not player_one_turn
        if player_one[1] >= 1000:
            return player_two[1] * i
        if player_two[1] >= 1000:
            return player_one[1] * i
            

def part_2(loc: str = DEFAULT_INPUT):
    with open(loc) as f:
        pass
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
