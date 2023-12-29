from aoc_utils import *

inp = read_input(2022, 8)
#inp = read_input(2022, 8, filename='test')

def check_visibility(loc, grid):
    row, col = loc
    grid_copy = grid.copy()
    tree_height = int(grid_copy[row][col])
    visible_from = []
    if row in [0, len(grid_copy)-1] or col in [0, len(grid_copy[0])-1]:
        return True
    
    visible = True
    for other in grid_copy[row][:col]:
        if int(other) >= tree_height:
            visible = False
    if visible:
        visible_from.append('left')
    
    visible = True
    for other in grid_copy[row][col+1:]:
        if int(other) >= tree_height:
            visible = False
    if visible:
        visible_from.append('right')

    grid_copy = transpose(grid_copy)

    visible = True
    for other in grid_copy[col][:row]:
        if int(other) >= tree_height:
            visible = False
    if visible:
        visible_from.append('top')
    visible = True
    for other in grid_copy[col][row+1:]:
        if int(other) >= tree_height:
            visible = False
    if visible:
        visible_from.append('bottom')

    return True if visible_from else False


count = 0

for i in range(len(inp)):
    for j in range(len(inp[0])):
        count += check_visibility((i,j), inp)
print(count)