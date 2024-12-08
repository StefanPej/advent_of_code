from aoc_utils import *

test = read_input(2024, 8, filename='test')
inp_ = read_input(2024, 8)

inp = test
inp = inp_

ants = [["." for _ in range(len(inp[0]))] for _ in range(len(inp))]
ans = 0
for row, line in enumerate(inp):
    for col, char in enumerate(line):
        if char != ".":
            if ants[row][col] != '#':
                ans += 1
                ants[row][col] = '#'

            for inner_row, inner_line in enumerate(inp):
                for inner_col, inner_char in enumerate(inner_line):
                    if inner_char == char and ((row != inner_row) and (col != inner_col)):
                        col_dif = col - inner_col
                        row_dif = row - inner_row

                        anti_row, anti_col = row + row_dif, col + col_dif

                        while 0 <= anti_row < len(inp) and 0 <= anti_col < len(inp[0]):
                            if ants[anti_row][anti_col] != '#':
                                ans += 1
                                ants[anti_row][anti_col] = '#'
                            anti_row, anti_col = anti_row + row_dif, anti_col + col_dif

print(ans)

                    
