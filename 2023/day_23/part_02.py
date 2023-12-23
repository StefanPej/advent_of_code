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

    for dir in dirs:
        next_loc = add_tuples(location, dir)
        if not check_oob(next_loc, grid):
            if not next_loc in seen and not grid[next_loc[0]][next_loc[1]] == '#':
                ret.append(next_loc)
    return ret

branches = set()
for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == '#':
            continue
        if len(take_step((i,j), DIRS, set(), inp)) > 2:
            branches.add((i,j))

start_loc = (0,1)
for i, char in enumerate(inp[-1]):
    if char == '.':
        end_loc = (len(inp)-1, i)

branches.add(start_loc)
branches.add(end_loc)
branch_dists = {branch:{} for branch in branches}
for branch in branches:
    start = branch
    branch_seen = set()
    branch_seen.add(start)
    steps = [(1, start, branch_seen)]

    while steps:
        steps_taken, location, seen = steps.pop()
        next_steps = take_step(location, DIRS, seen, inp)
        for step in next_steps:
            if step in branches:
                branch_dists[branch][step] = steps_taken
                break
            new_seen = seen.copy()
            new_seen.add(step)
            steps.append((steps_taken+1, step, new_seen))


current_loc = start_loc
seen = set()
seen.add(current_loc)
paths = [(current_loc, seen, 0)]
ans = 0
while paths:
    loc, seen, dist = paths.pop()

    if loc == end_loc:
        ans = max(ans, dist)

    for dest in branch_dists[loc]:
        if dest not in seen:
            seen_copy = seen.copy()
            seen_copy.add(dest)
            paths.append((dest, seen_copy, dist + branch_dists[loc][dest]))

print(ans)
