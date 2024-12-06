from aoc_utils import *

test = read_input(2024, 6, filename='test')
inp_ = read_input(2024, 6)

inp = test
inp = inp_

inp = [list(i) for i in inp]

dirs = {'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r':(0, 1)}

cur_dir = 'u'
for row, line in enumerate(inp):
    for col, char in enumerate(line):
        if char == "^":
            guard_pos = (row, col)

visited = set()
visited.add(guard_pos)

while True:

    dir_row, dir_col = dirs[cur_dir]
    cur_row, cur_col = guard_pos
    new_row, new_col = cur_row + dir_row, cur_col + dir_col
    if new_row < 0 or new_row >= len(inp) or new_col < 0 or new_row >= len(inp[0]):
        break
    if inp[new_row][new_col] == "#":
        if cur_dir == 'u':
            cur_dir = 'r'
        elif cur_dir == 'r':
            cur_dir = 'd'
        elif cur_dir == 'd':
            cur_dir = 'l'
        elif cur_dir == 'l':
            cur_dir = 'u'
        continue

    guard_pos = (new_row, new_col)
    visited.add(guard_pos)

print(len(visited))