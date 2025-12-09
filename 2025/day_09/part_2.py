from aoc_utils import *
from shapely import Polygon

inp = read_input(2025, 9)
test = read_input(2025, 9, filename='test')

points=[]
for line in inp:
    points.append(tuple(map(int, line.split(","))))
big = Polygon(points)

rec = 0
for i in range(len(points)-1):
    xi, yi = points[i]
    for j in range(i+1, len(points)):
        xj, yj = points[j]
        corners = [(xi, yi), (xi, yj), (xj, yj), (xj, yi)]
        little = Polygon(corners)
        if big.contains(little):
            x_diff = abs(xi-xj) + 1
            y_diff = abs(yi-yj) + 1
            rec = max(x_diff*y_diff, rec)

print(rec)