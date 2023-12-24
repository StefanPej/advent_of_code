from aoc_utils import *
from shapely.geometry import LineString

inp = read_input(2023, 24)
#inp = read_input(2023, 24, filename='test')

def parse_inp(line):
    coords_raw, velo_raw = line.split('@')
    coords = coords_raw.split()
    coords = tuple([int(coord.rstrip(',')) for coord in coords])

    velo = velo_raw.split()
    velo = tuple([int(vel.rstrip(',')) for vel in velo])

    return (coords, velo) 


hail = [parse_inp(line) for line in inp]


test_start = 200000000000000
test_end = 400000000000000
time = 10000000000000000000000
count = 0

for i, stone1 in enumerate(hail[:-1]):
    s1_x, s1_y, _ = stone1[0]
    s1_xv, s1_yv, _ = stone1[1]
    stone1_line = LineString([(s1_x, s1_y), (s1_x + (time*s1_xv), s1_y + (time*s1_yv))])

    for stone2 in hail[i+1:]:
        s2_x, s2_y, _ = stone2[0]
        s2_xv, s2_yv, _ = stone2[1]
        stone2_line = LineString([(s2_x, s2_y), (s2_x + (time*s2_xv), s2_y + (time*s2_yv))])

        intersect = stone1_line.intersection(stone2_line)
        if intersect:
            x_int = intersect.xy[0][0]
            y_int = intersect.xy[1][0]
            if test_start <= x_int <= test_end and test_start <= y_int <= test_end:
                count += 1

print(count)