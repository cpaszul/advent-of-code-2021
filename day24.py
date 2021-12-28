DEFAULT_INPUT = 'day24.txt'

# inspired by https://www.reddit.com/r/adventofcode/comments/rom5l5/2021_day_24pen_paper_monad_deparsed/
def day_24(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    block = []
    blocks = []
    for line in lines:
        if line == "inp w":
            if block:
                blocks.append(block)
            block = [line]
        else:
            block.append(line)
    blocks.append(block)
    stack = []
    formulae = []
    for i, block in enumerate(blocks):
        if block[4] == "div z 1":
            y_const = int(block[15].split(' ')[2])
            stack.append((i, y_const))
        else:
            x_const = int(block[5].split(' ')[2])
            prev, y_const = stack.pop()
            formulae.append((prev, x_const + y_const, i))
    large = [0] * 14
    small = [0] * 14
    for formula in formulae:
        left, mod, right = formula
        if mod >= 0:
            large[right] = 9
            large[left] = 9 - mod
            small[left] = 1
            small[right] = 1 + mod
        else:
            large[left] = 9
            large[right] = 9 + mod
            small[right] = 1
            small[left] = 1 - mod
    return int(''.join(map(str, large))), int(''.join(map(str, small)))
        
if __name__ == '__main__':
    part_1, part_2 = day_24()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
