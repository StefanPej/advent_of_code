from aoc_utils import *
from math import ceil
from scipy.ndimage import rotate

inp = read_input(2023, 21)

inp = [list(line) for line in inp]

with open('2023/day_21/full_grid_odd.txt') as o:
    full_odd = o.readlines()

dots_odd = 0
for line in full_odd:
    for char in line:
        if char == 'X':
            dots_odd += 1

with open('2023/day_21/full_grid_even.txt') as o:
    full_even = o.readlines()

dots_even = 0
for line in full_even:
    for char in line:
        if char == 'X':
            dots_even += 1

#print(dots_odd, dots_even)
odds = 1
evens = 1
for i in range(1,202300):
    evens += i
# reflect it
evens *= 2
# add middle row, minus one since double counting mid
evens += 202298
#print("evens: ", evens)

# pascal shit
for i in range(1,202299):
    odds += i
# reflect it
odds *= 2
# add middle row, minus one since double counting mid
odds += 202298-1
#print("odds: ", odds)


total = odds * dots_odd
total += evens * dots_even

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

def get_endings(start_pos, steps):
    possibilities = [(start_pos, steps)]
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
    
    return len(end_locs)

top = get_endings((130,65), 130)
bot = get_endings((0,65), 130)
right = get_endings((65,0), 130)
left = get_endings((65,130), 130)

total += top + bot + right + left

num_bigs = 202299 
num_lils = 202299 + 1

tr_lil = get_endings((130,0), 64)
tl_lil = get_endings((130,130), 64)
br_lil = get_endings((0,0), 64)
bl_lil = get_endings((0,130), 64)

total += num_lils*(tr_lil + tl_lil + br_lil + bl_lil)

tr_big = get_endings((130, 0), 195)
tl_big = get_endings((130, 130), 195)
br_big = get_endings((0, 0), 195)
bl_big = get_endings((0, 130), 195)

total += num_bigs*(tr_big + tl_big + br_big + bl_big)

print(total)
