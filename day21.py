from collections import namedtuple, Counter

DEFAULT_INPUT = 'day21.txt'

State = namedtuple('State', ['p1_pos', 'p1_score', 'p2_pos', 'p2_score'])

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
            dice = (dice - 1) % 100 + 1
            i += 1
        if player_one_turn:
            new_space = (player_one[0] + move)
            new_space = (new_space - 1) % 10 + 1
            player_one[1] += new_space
            player_one[0] = new_space
        else:
            new_space = (player_two[0] + move)
            new_space = (new_space - 1) % 10 + 1
            player_two[1] += new_space
            player_two[0] = new_space
        player_one_turn = not player_one_turn
        if player_one[1] >= 1000:
            return player_two[1] * i
        if player_two[1] >= 1000:
            return player_one[1] * i


def part_2(loc: str = DEFAULT_INPUT) -> int:
    dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    with open(loc) as f:
        p1_pos = int(f.readline().split(' ')[-1])
        p2_pos = int(f.readline().split(' ')[-1])
    initial_state = State(p1_pos, 0, p2_pos, 0)
    count = Counter({initial_state: 1})
    player_one_turn = True
    player_one_victories = 0
    player_two_victories = 0
    while count:
        new_count = Counter()
        for state in count:
            state_amount = count[state]
            if player_one_turn:
                for dice_result, result_times in dice.items():
                    new_space = state.p1_pos + dice_result
                    new_space = (new_space - 1) % 10 + 1
                    new_score = state.p1_score + new_space
                    if new_score >= 21:
                        player_one_victories += state_amount * result_times
                        continue
                    new_state = State(new_space, new_score, state.p2_pos, state.p2_score)
                    new_count[new_state] += state_amount * result_times
            else:
                for dice_result, result_times in dice.items():
                    new_space = state.p2_pos + dice_result
                    new_space = (new_space - 1) % 10 + 1
                    new_score = state.p2_score + new_space
                    if new_score >= 21:
                        player_two_victories += state_amount * result_times
                        continue
                    new_state = State(state.p1_pos, state.p1_score, new_space, new_score)
                    new_count[new_state] += state_amount * result_times
        player_one_turn = not player_one_turn
        count = new_count
    return max(player_one_victories, player_two_victories)
            
            
        
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
