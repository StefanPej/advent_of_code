from aoc_utils import *

inp = read_input(2025, 4)
test = read_input(2025, 4, filename="test")


def scan_around(row, col, grid):

    row = int(row)
    col = int(col)

    max_rows = len(grid)-1
    max_cols = len(grid[0])-1

    around = [(row + nr, col + nc) for nr in range(-1,2,1) for nc in range(-1,2,1)]

    count = 0
    for nr, nc in around:
        if (nr == row and nc == col) or (nc < 0) or (nc > max_cols) or (nr < 0) or (nr > max_rows):
            continue
        if grid[nr][nc] == "@":
            count +=1

    return count < 4

grid_to_use = inp
count = 0
removed = []

while True:

    for rr, rc in removed:
        new_row = grid_to_use[rr][:rc] + "." + grid_to_use[rr][rc + 1:]
        grid_to_use[rr] = new_row
    removed = []

    for row_num, row in enumerate(grid_to_use):
        for col_num, char in enumerate(row):
            if char != "@":
                continue
            has_removed = scan_around(row_num, col_num, grid_to_use)
            if has_removed:
                count += 1
                removed.append((row_num, col_num))
    
    if not removed:
        break

print(count)
