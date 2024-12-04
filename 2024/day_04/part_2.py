from aoc_utils import *

test = read_input(2024, 4, filename='test')
inp_ = read_input(2024, 4)

inp = inp_

inp = [[char for char in line] for line in inp]
line_len = len(inp[0])
col_len = len(inp)

ans = 0
for row in range(len(inp)):
    for col, char in enumerate(inp[row]):
        if char != 'A' or row == 0 or row == len(inp) - 1 or col == 0 or col == len(inp) - 1:
            continue
        
        top_left = inp[row-1][col-1]
        top_right = inp[row-1][col+1]
        bot_left = inp[row+1][col-1]
        bot_right = inp[row+1][col+1]

        if top_right+top_left == 'MM' and bot_left+bot_right == 'SS':
            ans += 1
        if top_right+top_left == 'SS' and bot_left+bot_right == 'MM':
            ans += 1
        if top_left+top_right == 'SM' and bot_left+bot_right == 'SM':
            ans += 1
        if top_left+top_right == 'MS' and bot_left+bot_right == 'MS':
            ans += 1

print(ans)