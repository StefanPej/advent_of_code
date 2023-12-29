from aoc_utils import *

inp = read_input(2022, 9)
#inp = read_input(2022, 9, filename='test')

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
           
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
TL = (-1, -1)
BL = (1, -1)
TR = (-1, 1)
BR = (1, 1)

DIRS = [UP, DOWN, LEFT, RIGHT]
ALL_DIRS = DIRS + [TL, BL, TR, BR]

dir_map = {'R':RIGHT, 'U':UP, 'L':LEFT, 'D':DOWN}

def make_move(head_pos, tail_pos, dir):


    new_head = add_tuples(head_pos, dir)

    if tail_pos in [add_tuples(new_head, d) for d in ALL_DIRS] or tail_pos == new_head:
        return new_head, tail_pos
    
    opposite_dir = (dir[0]*-1, dir[1]*-1)
    new_tail = add_tuples(new_head, opposite_dir)

    return new_head, new_tail

head = tail = (0, 0)
SEEN = set()
SEEN.add(tail)

for line in inp:
    dir, amt = line.split()
    dir = dir_map[dir]
    amt = int(amt)
    for _ in range(amt):
        head, tail = make_move(head, tail, dir)
        SEEN.add(tail)

print(len(SEEN))