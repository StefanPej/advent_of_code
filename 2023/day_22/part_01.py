from aoc_utils import *

inp = read_input(2023, 22)

# with open('2023/day_22/test.txt') as o:
#     inp = o.readlines()
#     inp = [line.strip() for line in inp]

COORDS = {0:'x', 1:'y', 2:'z'}
FALLIN_DIR = (0,0,-1)
UP = (0,0,1)
GRID = {}

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1], tuple1[2] + tuple2[2])

class Brick:
    def __init__(self, start, end, name):
        self.name = name
        self.start = list(map(int, start))
        self.end = list(map(int, end))
        self.coords = []
        self.length = abs(int(start[0])+int(start[1])+int(start[2])-int(end[0])-int(end[1])-int(end[2]))+1

        if self.start == self.end:
            self.coords.append(tuple(self.start))
        
        else:
            for i in range(3):
                if self.start[i] != self.end[i]:
                    dir_change = i

            for i in range(self.end[dir_change] - self.start[dir_change] + 1):
                if dir_change == 0:
                    self.coords.append((self.start[0] + i, self.start[1], self.start[2]))
                if dir_change == 1:
                    self.coords.append((self.start[0], self.start[1] + i, self.start[2]))
                if dir_change == 2:
                    self.coords.append((self.start[0], self.start[1], self.start[2] + i))

    def write_to_grid(self, grid):
        for coord in self.coords:
            #print(coord)
            grid[coord] = self.name

    def fall(self, grid):
        falling = True
        while falling:
            new_coords = [add_tuples(self_coord, FALLIN_DIR) for self_coord in self.coords]
            possible = True
            for coord in new_coords:
                #print(coord)
                exist_coord = grid.get(coord)
                if exist_coord:
                    if exist_coord!= self.name:
                        falling = False
                        possible = False
                if coord[2] < 1:
                    falling = False
                    possible = False
            if possible:
                for coord in self.coords:
                    del grid[coord]
                #print(self.name, new_coords)
                self.coords = new_coords
                self.write_to_grid(grid)


    def __repr__(self):
        return f"COORDS: {self.coords}, LENGTH: {self.length}"
    
    def __lt__(self, other):
        self_min_z = min(coord[2] for coord in self.coords)
        other_min_z = min(coord[2] for coord in other.coords)

        return self_min_z < other_min_z
    

bricks = []
bricks_dict = {}
for i, line in enumerate(inp, start=1):
    start, end = line.split('~')
    start, end = start.split(','), end.split(',')
    bricks.append(Brick(start, end, i))
    bricks_dict[i] = Brick(start, end, i)

#bricks = sorted(bricks)

print(bricks[0])

for brick in bricks:
    brick.write_to_grid(GRID)

#print(GRID)
its = 0
while True:
    its += 1
    changed = False
    #bricks = sorted(bricks)
    brick_pos = {brick.name:brick.coords for brick in bricks}
    for brick in bricks:
        brick.fall(GRID)
    for brick in bricks:
        if brick_pos[brick.name] != brick.coords:
            changed = True
    if not changed:
        break
print(its)
#print(order_dict(GRID))
len_count = {i:0 for i in range(1, len(inp)+1)}
for val in GRID.values():
    len_count[val] += 1

for brick in bricks:
    assert len_count[brick.name] == brick.length

for brick in bricks:
    for coord in brick.coords:
        assert coord in GRID

dependants = {i:set() for i in range(1, len(inp)+1)}
aboves = {i:set() for i in range(1, len(inp)+1)}
poss = set()
for brick in bricks:
    depends_on = set()
    above = set()
    for coord in brick.coords:
        below_coord = add_tuples(coord, FALLIN_DIR)
        above_coord = add_tuples(coord, UP)
        if GRID.get(below_coord):
            if GRID.get(below_coord) != brick.name:
                depends_on.add(GRID.get(below_coord))
                dependants[brick.name].add(GRID.get(below_coord))
        if GRID.get(above_coord):
            if GRID.get(above_coord) != brick.name:
                above.add(GRID.get(above_coord))
                aboves[brick.name].add(GRID.get(above_coord))
    if len(depends_on) > 1:
        print('adding', brick.name, depends_on)
        poss = poss.union(depends_on)
    # if len(depends_on) == 1:
    #     poss.discard(list(depends_on)[0])
    # #print(above)
    if len(above) == 0:
        poss.add(brick.name)


for k, v in dependants.items():
    if len(v) == 1:
        poss.discard(list(v)[0])

print(len(poss))
#print(dependants)
#print(aboves)
# deps = set()
# for vals in dependants.values():
#     if len(vals) > 1:
#         deps = deps.union(vals)

# for k, val in aboves.items():
#     if len(val) == 0:
#         deps.add(k)

# print(len(deps))
# OG = GRID.copy()
# can_remove = 0
# #bricks = sorted(bricks)
# for i in range(1, len(bricks)+1):
#     GRID = OG.copy()
#     to_del = []
#     for k, v in GRID.items():
#         if v == i:
#             to_del.append(k)
#     print(to_del)
#     for del_ in to_del:
#         del GRID[del_]
#     for j, brick in enumerate(bricks, start=1):
#         if i == j:
#             continue
#         print(i, j)
#         print(brick.coords)
#         # if i == 5 and j > 935:
#         #     print(GRID)
#         brick.fall(GRID)
#     if GRID == OG:
#         can_remove +=1
#     print(can_remove)
# print(can_remove)