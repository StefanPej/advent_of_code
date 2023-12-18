from aoc_utils import *
import shapely

inp = read_input(2023, 18)

def convert(hex):
    return int(hex, 16)

dirs = {0:'R',
        1:'D',
        2:'L',
        3:'U'}

instructions = []
for line in inp:
    hex_num = line.split('#')[1]
    hex_num = hex_num.strip()
    hex_num = hex_num.replace(')', '')
    instructions.append((dirs[int(hex_num[-1])], convert(hex_num[:len(hex_num)-1])))

def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

coords = []
current_coord = (0,0)
for dir, num in instructions:
    num = num
    if dir == 'L':
        current_coord = add_tuples(current_coord, (0, -num))
    if dir == 'R':
        current_coord = add_tuples(current_coord, (0, num))
    if dir == 'U':
        current_coord = add_tuples(current_coord, (-num, 0))
    if dir == 'D':
        current_coord = add_tuples(current_coord, (num, 0))
    coords.append(current_coord)
    
shape = shapely.Polygon(coords)
# GEOMETRY
print(int(((shape.length+2)/2) + shape.area))
