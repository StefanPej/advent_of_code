from aoc_utils import *

inp = read_input(2023, 23)
inp = read_input(2023, 23, filename='test')

inp = [list(line) for line in inp]


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

def take_step(location, dirs, seen, grid):
    ret = []

    for dir in dirs:
        next_loc = add_tuples(location, dir)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                #print(grid[next_loc[0]][next_loc[1]])
                ret.append(next_loc)
    return ret



start_loc = (0,1)
for i, char in enumerate(inp[-1]):
    if char == '.':
        end_loc = (len(inp)-1, i)
print(end_loc)
seen = set()
seen.add(start_loc)

#print(take_step(start_loc, DIRS, seen, inp))

ans = 0
best_path = set()
steps = [(0, start_loc, seen)]

already_seen = {}
while steps:
    steps_taken, location, seen = steps.pop()

    if location == end_loc:
        if steps_taken > ans:
            best_path = seen
        ans = max(ans, steps_taken)
        
        continue

    next_steps = take_step(location, DIRS, seen, inp)
    for step in next_steps:
        new_seen = seen.copy()
        new_seen.add(step)
        steps.append((steps_taken+1, step, new_seen))

    #print(steps)
    #input()
print(best_path)
print(ans)

# def print_path(path, input):
#     out = ""
#     for i, line in enumerate(input):
#         l = ""
#         for j, char in enumerate(line):
#             if (i,j) in path:
#                 l += 'O'
#             else:
#                 l += char
#         l += '\n'
#         out += l
#     return out
# print(print_path(best_path, inp))
