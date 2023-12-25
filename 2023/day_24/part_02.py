from aoc_utils import *
from shapely.geometry import LineString
from math import ceil

inp = read_input(2023, 24)
# with open('2023/day_24/test.txt') as o:
#     inp = o.readlines()
# inp = [line.strip() for line in inp]


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

def find_max_xyz(stones, time):
    max_xyz = (0,0,0)
    max_stone = "123"
    for i, stone in enumerate(stones):
        s0_x, s0_y, s0_z = stone[0]
        s0_xv, s0_yv, s0_zv = stone[1]
        
        new_xyz = (s0_x + s0_xv*time, s0_y + s0_yv*time, s0_z + s0_zv*time)
        if all(m<n for m,n in zip(max_xyz,new_xyz)):
            max_xyz = new_xyz
            max_stone = i
            
    return max_stone

def fine_max_z(stones, time):
    max_xyz = 0
    max_stone = "123"
    for i, stone in enumerate(stones):
        s0_x, s0_y, s0_z = stone[0]
        s0_xv, s0_yv, s0_zv = stone[1]
        
        new_xyz = s0_z + s0_zv*time
        if max_xyz < new_xyz:
            max_xyz = new_xyz
            max_stone = i
            
    return max_stone

def find_min_xyz(stones, time):
    min_xyz = (float('inf'),float('inf'),float('inf'))
    min_stone = "123"
    for i, stone in enumerate(stones, start=1):
        s0_x, s0_y, s0_z = stone[0]
        s0_xv, s0_yv, s0_zv = stone[1]
        
        new_xyz = (s0_x + s0_xv*time, s0_y + s0_yv*time, s0_z + s0_zv*time)
        if all(m>n for m,n in zip(min_xyz,new_xyz)):
            min_xyz = new_xyz
            min_stone = i
            
    return min_stone

def find_next_xyz(stones, cap_stone, time):
    max_xyz = (0,0,0)
    if cap_stone == float('inf'):
        cap = (float('inf'), float('inf'), float('inf'))
    else:
        cap = stones[cap_stone][0]
    max_stone = "WRONG"
    for i, stone in enumerate(stones, start=1):
        if i == cap_stone:
            #print(cap_stone, i)
            continue
        s0_x, s0_y, s0_z = stone[0]
        s0_xv, s0_yv, s0_zv = stone[1]
        
        new_xyz = (s0_x + s0_xv*time, s0_y + s0_yv*time, s0_z + s0_zv*time)
        if all(m<n for m,n in zip(max_xyz,new_xyz)) and all(m>n for m,n in zip(cap,new_xyz)) :
            max_xyz = new_xyz
            max_stone = i
            
    return max_stone

def find_next_z(stones, cap_stone, time):
    max_xyz = 0
    if cap_stone == float('inf'):
        cap = float('inf')
    else:
        cap = stones[cap_stone][0][2] + stones[cap_stone][1][2]*time
    max_stone = "ERROR"
    for i, stone in enumerate(stones):
        if i == cap_stone:
            continue
        s0_x, s0_y, s0_z = stone[0]
        s0_xv, s0_yv, s0_zv = stone[1]
        
        new_xyz = s0_z + s0_zv*time
        if max_xyz < new_xyz and cap > new_xyz:
            max_xyz = new_xyz
            max_stone = i
            
    return max_stone



hail_paths = []
for stone in hail:
    s1_x, s1_y, s1_z = stone[0]
    s1_xv, s1_yv, s1_zv = stone[1]
    stone1_line = LineString([(s1_x, s1_y, s1_z), (s1_x + (time*s1_xv), s1_y + (time*s1_yv), s1_z + (time*s1_zv))])
    hail_paths.append(stone1_line)

#print(hail[123])
stone_order = []
curr_max = float('inf')


times = 1
last_loop = []
for i in range(times):
    max_z = []
    curr_cap = float("inf")
    for _ in range(len(inp)):
        # new_max = find_max_xyz(hail, 10)
        # stone_order.append(new_max)
        # curr_max = new_max
        #print(len(max_z))
        new_max = find_next_z(hail, curr_cap, i)
        #print(new_max)
        #print(len(max_z))
        max_z.append(new_max)
        curr_cap = new_max
        #print(curr_max)
        #input()


        # other_stone = hail[max_stone-1]

        # other_stonex, other_stoney, other_stonez = other_stone[0]
        # other_stonexv, other_stoneyv, other_stonezv = other_stone[1]

        # other_stones.append((other_stonex + other_stonexv*i, other_stoney + other_stoneyv*i, other_stonez + other_stonezv*i))
    

    if i != 0:
        if last_loop != max_z:
            print('NO MATCH')
            
    last_loop = max_z    
    
highest = max_z[0]
lowest = max_z[-1]

def generate_points(stone, time):
    stone = hail[stone]
    ret = []
    s1_x, s1_y, s1_z = stone[0]
    s1_xv, s1_yv, s1_zv = stone[1]
    for i in range(time):
        ret.append((s1_x + s1_xv*i, s1_y + s1_yv*i, s1_z + s1_zv*i))
    return ret


points_to_try = 10000
max_points = generate_points(highest, points_to_try)
min_points = generate_points(lowest, points_to_try)

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

lines_to_try = set()
for i in range(len(max_points)-300):
    for j in range(i, len(min_points)):
        lines_to_try.add(make_line(max_points[i], min_points[j]))
        
for i in range(len(min_points)-300):
    for j in range(i, len(max_points)):
        lines_to_try.add(make_line(min_points[i], max_points[j]))
print(f"MADE {len(lines_to_try)} LINES TO TEST")

def check_collision(line, paths):
    for path in paths:
        if not line.intersects(path):
            return False
    return True

for line in lines_to_try:
    if check_collision(line, hail_paths):
        print(line)
        break

exit(0)

# PLAN
# FIND WHICH STONE IS ALWAYS NEXT, AND SO ON UNTIL WE FIND ORDER OF STONES
# FIND WHICH START AND END TIME PRODUCES THE LINE

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