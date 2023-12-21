from aoc_utils import *

inp = read_input(2023, 21)

# with open('2023/day_21/test.txt') as o:
#     inp = o.readlines()

inp = [list(line) for line in inp]

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == 'S':
            start_pos = (i, j)
            inp[i][j] = '.'

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
           
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRS = [UP, DOWN, LEFT, RIGHT]

def check_oob(location, inp):
    if not (0 <= location[0] < len(inp)) or not (0 <= location[1] < len(inp[0])):
        return True
    return False

def take_step(loc, steps_left):
    ret = []
    for dir in DIRS:
        new_row, new_col = add_tuples(dir, loc)
        if not check_oob((new_row, new_col), inp):
            if inp[new_row][new_col] != '#':
                ret.append(((new_row, new_col), steps_left-1))
    return ret

possibilities = [(start_pos, 65)]
seen = set()
end_locs = set()
while possibilities:
    pos, steps_left = possibilities.pop(0)
    
    if (pos, steps_left) in seen:
        continue
    seen.add((pos, steps_left))
    if steps_left == 0:
        end_locs.add(pos)
        continue
    possibilities += take_step(pos, steps_left)

        
print(len(end_locs))

out = []
for i in range(len(inp)):
    sub = ""
    for j in range(len(inp[0])):
        if (i,j) in end_locs:
            sub+='X'
        else:
            sub += str(inp[i][j])
    out.append(sub)

with open('2023/day_21/end_locs.txt', 'w') as o:
    for line in out:
        o.write(line + '\n')
