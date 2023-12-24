from aoc_utils import *
from shapely.geometry import LineString
from sympy import Plane, Point3D
from math import ceil

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

time = 10000000000000000

# def hits_ground(stone):
#     _, _, z = stone[0]
#     _, _, v = stone[1]

#     if v > 0:
#         return float('inf')


#     return ceil(z // abs(v))

# ground_hits = []
# for i, stone in enumerate(hail, start=1):
#     ground_hits.append((i, hits_ground(stone)))

# print(order_list(ground_hits, 1)[0])



hail_paths = []
for stone in hail:
    s1_x, s1_y, s1_z = stone[0]
    s1_xv, s1_yv, s1_zv = stone[1]
    stone1_line = LineString([(s1_x, s1_y, s1_z), (s1_x + (time*s1_xv), s1_y + (time*s1_yv), s1_z + (time*s1_zv))])
    hail_paths.append(stone1_line)

stone_0_coords = []
stone_1_coords = []


time2 = 6000
for i in range(time2):
    s0_x, s0_y, s0_z = hail[0][0]
    s0_xv, s0_yv, s0_zv = hail[0][1]
    s1_x, s1_y, s1_z = hail[1][0]
    s1_xv, s1_yv, s1_zv = hail[1][1]

    stone_0_coords.append((s0_x + s0_xv*i, s0_y + s0_yv*i, s0_z + s0_zv*i))
    stone_1_coords.append((s1_x + s1_xv*i, s1_y + s1_yv*i, s1_z + s1_zv*i))

#print(stone_0_coords)

def make_line(coord1, coord2):
    vx = coord1[0] - coord2[0]
    vy = coord1[1] - coord2[1]
    vz = coord1[2] - coord2[2]

    ls_x = coord1[0] + vx*time
    ls_y = coord1[1] + vy*time
    ls_z = coord1[2] + vz*time

    le_x = coord1[0] - vx*time
    le_y = coord1[1] - vy*time
    le_z = coord1[2] - vz*time

    return LineString([(ls_x, ls_y, ls_z), (le_x, le_y, le_z)])

all_lines = []
for i in range(len(stone_0_coords)):
    coord1 = stone_0_coords[i]
    for coord2 in stone_1_coords[i+1:-1]:
        all_lines.append(make_line(coord1, coord2))

for i in range(len(stone_1_coords)):
    coord1 = stone_1_coords[i]
    for coord2 in stone_0_coords[i+1:-1]:
        all_lines.append(make_line(coord1, coord2))

print(f'Added all lines, total amount: {len(all_lines)}')

def check_collision(line, paths):
    for path in paths:
        if not line.intersects(path):
            return False
    return True

for line in all_lines:
    if check_collision(line, hail_paths):
        print(line)
        break


# def construct_plane(stone1, stone2):
#     s1_x, s1_y, s1_z = stone1[0]
#     s1_xv, s1_yv, s1_zv = stone1[1]
#     s2_x, s2_y, s2_z = stone2[0]

#     plane = Plane(Point3D(s1_x, s1_y, s1_z), Point3D(s1_x + s1_xv, s1_y + s1_yv, s1_z + s1_zv), Point3D(s2_x, s2_y, s2_z))

#     return plane

# print(construct_plane(hail[0], hail[1]).equation())

#print(lines)