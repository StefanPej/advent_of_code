from aoc_utils import *

inp = read_input(2023, 24)
#inp = read_input(2023, 24, filename='test')

class Stone:
    def __init__(self, info):
        self.info = info
        self.int_info = self.parse_info(self.info)
        self.x, self.y, self.z, self.vx, self.vy, self.vz = self.int_info
        self.a, self.b, self.c = self.get_standard_form(self.int_info)

    def parse_info(self, info):
        int_info = tuple(map(int, info.replace('@', ',').split(',')))
        return int_info
    
    def get_standard_form(self, int_info):
        x, y, z, vx, vy, vz = int_info
        return vy, -vx, ((vy * x) - (vx * y))

    def __repr__(self):
        return f"Stone with coords: {self.x}, {self.y}, {self.z}. Velocity: {self.vx}, {self.vy}, {self.vz}. Standard form: {self.a}x + {self.b}y = {self.c}"

def check_collision(stone1, stone2):
    s1a, s1b, s1c = stone1.a, stone1.b, stone1.c
    s2a, s2b, s2c = stone2.a, stone2.b, stone2.c

    s1x, s1y, s1vx, s1vy = stone1.x, stone1.y, stone1.vx, stone1.vy
    s2x, s2y, s2vx, s2vy = stone2.x, stone2.y, stone2.vx, stone2.vy

    if s1a*s2b == s2a*s1b:
        return float('inf'), float('inf')
    
    x_col = (s2c*s1b - s1c*s2b)/(s2a*s1b - s2b*s1a)
    y_col = -(s2c*s1a - s1c*s2a)/(s2a*s1b - s2b*s1a)

    if not ((x_col - s1x)*s1vx > 0 and (y_col - s1y)*s1vy > 0) or not ((x_col - s2x)*s2vx > 0 and (y_col - s2y)*s2vy > 0):
        return float('inf'), float('inf')

    return x_col, y_col
    


stones = [Stone(line) for line in inp]

upper_b = 400000000000000
lower_b = 200000000000000

count = 0
for i, stone1 in enumerate(stones[:-1]):
    for stone2 in stones[i:]:
        x_col, y_col = check_collision(stone1, stone2)
        if lower_b <= x_col <= upper_b and lower_b <= y_col <= upper_b:
            count += 1
print(count)