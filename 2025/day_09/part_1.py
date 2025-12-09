from aoc_utils import *

inp = read_input(2025, 9)
test = read_input(2025, 9, filename='test')

rec = 0
for i in range(len(inp)-1):
    xi, yi = map(int, inp[i].split(","))
    for j in range(i+1, len(inp)):
        xj, yj = map(int, inp[j].split(","))
        x_diff = abs(xi-xj) + 1
        y_diff = abs(yi-yj) + 1
        rec = max(x_diff*y_diff, rec)
print(rec)