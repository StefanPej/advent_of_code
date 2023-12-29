from aoc_utils import *

inp = read_input(2022, 9)
inp = read_input(2022, 9, filename='test')

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

grid = [['.' for _ in range(30)] for _ in range(30)]
           
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

def make_move(positions, dir):

    new_positions = []
    head_pos = positions[0]
    new_head = add_tuples(head_pos, dir)
    new_positions.append(new_head)

    for pos in positions[1:]:
        if pos in [add_tuples(new_positions[-1], d) for d in ALL_DIRS] or pos == new_positions[-1]:
            new_positions.append(pos)
        
        else:
            pos_row, pos_col = pos
            head_row, head_col = new_positions[-1]
            if pos_row != head_row and pos_col != head_col:
                if head_row - pos_row == 2:
                    new_positions.append(add_tuples(new_positions[-1], UP))
                if head_row - pos_row == -2:
                    new_positions.append(add_tuples(new_positions[-1], DOWN))
                if head_col - pos_col == 2:
                    new_positions.append(add_tuples(new_positions[-1], LEFT))
                if head_row - pos_row == -2:
                    new_positions.append(add_tuples(new_positions[-1], RIGHT))
            elif pos_row == head_row:
                if head_col > pos_col:
                    new_positions.append((pos_row, pos_col + 1))
                else:
                    new_positions.append((pos_row, pos_col - 1))
            elif pos_col == head_col:
                if head_row > head_row:
                    new_positions.append((pos_row + 1, pos_col))
                else:
                    new_positions.append((pos_row - 1, pos_col))


    #print(len(new_positions))
    return new_positions

def print_grid(grid, positions, seen):
    out = ""
    for i, line in enumerate(grid):
        l = ""
        for j, char in enumerate(line):
            coord = (i,j)
            if coord in positions:
                l += str(positions.index(coord))
            elif coord in seen:
                l += '#'
            else:
                l += '.'
        out += l + '\n'
    print(out)

positions = [(29, 1) for _ in range(10)]
SEEN = set()
SEEN.add(positions[-1])

for line in inp:
    dir, amt = line.split()
    dir = dir_map[dir]
    amt = int(amt)
    for _ in range(amt):
        print_grid(grid, positions, SEEN)
        input()
        positions = make_move(positions, dir)
        print(positions[-1])
        SEEN.add(positions[-1])

print(len(SEEN))