from aoc_utils import *

inp = read_input(2023, 23)
#inp = read_input(2023, 23, filename='test')

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
    row, col = location
    if grid[row][col] == '>':
        next_loc = add_tuples(location, RIGHT)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                return [next_loc]
            else:
                return []
        else:
            return []
    if grid[row][col] == '^':
        next_loc = add_tuples(location, UP)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                return [next_loc]
            else:
                return []
        else:
            return []
    if grid[row][col] == '<':
        next_loc = add_tuples(location, LEFT)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                return [next_loc]
            else:
                return []
        else:
            return []
    if grid[row][col] == 'v':
        next_loc = add_tuples(location, DOWN)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                return [next_loc]
            else:
                return []
        else:
            return []

    for dir in dirs:
        next_loc = add_tuples(location, dir)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                ret.append(next_loc)
    return ret


start_loc = (0,1)
seen = set()
seen.add(start_loc)


ans = 0
best_path = set()
steps = [(start_loc, seen, 0)]
while steps:
    location, seen, steps_taken = steps.pop()

    if location == (140,139):
        if len(seen) - 1 > ans:
            best_path = seen
        ans = max(ans, len(seen) - 1)
        
        continue

    next_steps = take_step(location, DIRS, seen, inp)
    for step in next_steps:
        new_seen = seen.copy()
        new_seen.add(step)
        steps.append((step, new_seen, steps_taken+1))

print(ans)

def print_path(path, input):
    out = ""
    for i, line in enumerate(input):
        l = ""
        for j, char in enumerate(line):
            if (i,j) in path:
                l += 'X'
            else:
                l += char
        l += '\n'
        out += l
    return out
#print(print_path(best_path, inp))
