from aoc_utils import *

inp = read_input(2022, 8)
#inp = read_input(2022, 8, filename='test')

def check_visibility(loc, grid):
    row, col = loc
    grid_copy = grid.copy()
    tree_height = int(grid_copy[row][col])
    if row in [0, len(grid_copy)-1] or col in [0, len(grid_copy[0])-1]:
        return 0
    
    left = 0
    for other in grid_copy[row][col-1::-1]:
        left += 1
        if int(other) >= tree_height:
            break

    right = 0
    for other in grid_copy[row][col+1:]:
        right += 1
        if int(other) >= tree_height:
            break

    grid_copy = transpose(grid_copy)

    top = 0
    for other in grid_copy[col][row-1::-1]:
        top += 1
        if int(other) >= tree_height:
            break

    bot = 0
    for other in grid_copy[col][row+1:]:
        bot += 1
        if int(other) >= tree_height:
            break
    
    return left*right*top*bot

best = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        best = max(best, check_visibility((i,j), inp))

print(best)