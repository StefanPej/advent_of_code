from aoc_utils import *

test = read_input(2024, 4, filename='test')
inp_ = read_input(2024, 4)

inp = inp_

inp = [[char for char in line] for line in inp]
line_len = len(inp[0])
col_len = len(inp)
def search_right(line, index):
    if index + 3 >= line_len:
        return 0
    if line[index:index+4] == ['X', 'M', 'A', 'S']:
        return 1
    return 0

def search_left(line, index):
    if index - 3 < 0:
        return 0
    if line[index-3:index+1] == ['S', 'A', 'M', 'X']:
        return 1
    return 0

def search_down(row_ind, index):
    if row_ind + 3 >= col_len:
        return 0
    if inp[row_ind + 1][index] + inp[row_ind + 2][index] + inp[row_ind + 3][index] == "MAS":
        return 1
    return 0

def search_up(row_ind, index):
    if row_ind - 3 < 0:
        return 0
    if inp[row_ind - 1][index] + inp[row_ind - 2][index] + inp[row_ind - 3][index] == "MAS":
        return 1
    return 0

def search_diag_down_right(row_ind, index):
    if row_ind + 3 >= col_len or index + 3 >= line_len:
        return 0
    if inp[row_ind + 1][index+1] + inp[row_ind + 2][index+2] + inp[row_ind + 3][index+3] == "MAS":
        return 1
    return 0

def search_diag_down_left(row_ind, index):
    if row_ind + 3 >= col_len or index - 3 < 0:
        return 0
    if inp[row_ind + 1][index-1] + inp[row_ind + 2][index-2] + inp[row_ind + 3][index-3] == "MAS":
        return 1
    return 0

def search_diag_up_left(row_ind, index):
    if row_ind - 3 < 0 or index - 3 < 0:
        return 0
    if inp[row_ind - 1][index-1] + inp[row_ind - 2][index-2] + inp[row_ind - 3][index-3] == "MAS":
        return 1
    return 0

def search_diag_up_right(row_ind, index):
    if row_ind - 3 < 0 or index + 3 >= line_len:
        return 0
    if inp[row_ind - 1][index+1] + inp[row_ind - 2][index+2] + inp[row_ind - 3][index+3] == "MAS":
        return 1
    return 0

ans = 0
for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == "X":
            ans += search_right(line, j)
            ans += search_left(line, j)
            ans += search_down(i, j)
            ans += search_up(i, j)
            ans += search_diag_down_right(i, j)
            ans += search_diag_up_left(i,j)
            ans += search_diag_down_left(i, j)
            ans += search_diag_up_right(i,j)
print(ans)

