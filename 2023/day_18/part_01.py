from aoc_utils import *

inp = read_input(2023, 18)

# with open('2023/day_18/test.txt') as o:
#     inp = o.readlines()

grid = [['*' for _ in range(1000)] for _ in range(1000)]

start = (500,500)

def dig(coord, grid):
    row, col = coord
    grid[row][col] = '#'
    return grid

current_loc = start
for inst in inp:
    direction, amt, _ = inst.split()
    amt = int(amt)
    for i in range(1,amt+1):
        if direction == 'L':
            current_loc = (current_loc[0], current_loc[1]-1)
        elif direction == 'R':
            current_loc = (current_loc[0], current_loc[1]+1)
        elif direction == 'U':
            current_loc = (current_loc[0]-1, current_loc[1])
        elif direction == 'D':
            current_loc = (current_loc[0]+1, current_loc[1])
        grid = dig(current_loc, grid)

in_hole = False
total = 0
border = set()
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == '#':
            total+=1
            border.add((i,j))
      

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
           
start_fill = [(501,505)]
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRS = [UP, DOWN, LEFT, RIGHT]

trapped = set(start_fill)
filling = True
while filling:
    len_trap = len(trapped)
    to_add = set()
    for trap in trapped:
        
        for dir in DIRS:
            x, y = add_tuples(trap, dir)
            if grid[x][y] == '*':
                to_add.add((x,y))
    trapped = trapped.union(to_add)
    if len_trap == len(trapped):
        filling = False
    
print(total + len(trapped))