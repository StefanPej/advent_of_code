from aoc_utils import *

inp = read_input(2023, 13)

with open('2023/day_13/test.txt') as o:
    inp = o.readlines()
inp = [line.strip() for line in inp]

maps = []
new_map = []
for line in inp:
    if line == '':
        maps.append(new_map)
        new_map = []
        continue
    new_map.append(line)
maps.append(new_map)
    
def confirm_reflection(map, reflection_point):
    start = reflection_point
    end = reflection_point + 1
    while start >= 0 and end < len(map):
        #print(map[start], 'VS', map[end])
        if map[start] != map[end]:
            return False
        start -= 1
        end += 1
    return True
    
def solve_map(map):
    reflection_point = 0
    for i in range(1,len(map)):
        if map[i] == map[i-1]:
            temp_ref = i-1
            if confirm_reflection(map, temp_ref):
                reflection_point = temp_ref + 1
                break
        
    return reflection_point

def identify_cosmic_bit_flip(map):
    for i in range(1, len(map)):
        ind_m1 = [*map[i-1]]
        ind = [*map[i]]
        if sum([char1!=char2 for char1, char2 in zip(ind_m1, ind)]) == 1:
            print(ind_m1, ind)
            

identify_cosmic_bit_flip(maps[0])

# total = 0
# for map in maps:
#     total += solve_map(transpose(map))
#     total += 100*solve_map(map)
    
# print(total)