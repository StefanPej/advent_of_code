from aoc_utils import *



COORDS = {0:'x', 1:'y', 2:'z'}
FALLIN_DIR = (0,0,-1)
UP = (0,0,1)


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

def hoo_yah(num, first_iter, test=False, bricks_d={}): 
    
    if first_iter:
        inp = read_input(2023, 22)
        if test:
            with open('2023/day_22/test.txt') as o:
                inp = o.readlines()
                inp = [line.strip() for line in inp]

        bricks = []
        
        for i, line in enumerate(inp, start=1):
            start, end = line.split('~')
            start, end = start.split(','), end.split(',')
            bricks.append(Brick(start, end, i))


    else:
        bricks = []
        for val in bricks_d.values():
            bricks.append(Brick(val.start, val.end, val.name))

    if num:
        bricks.pop(num-1)

    GRID = {}
    for brick in bricks:
        brick.write_to_grid(GRID)

    bricks = sorted(bricks)
    for brick in bricks:
        brick.fall(GRID)
    
    bricks_dict = {brick.name:brick for brick in bricks}

    return bricks_dict

nums_inp = len(read_input(2023, 22))+1
OG = hoo_yah(0, True, False)
total = 0
for i in range(1, nums_inp):
    new = hoo_yah(i, False, False, OG)
    for k, v in new.items():
        if OG[k].coords != v.coords:
            total += 1

print(total)

