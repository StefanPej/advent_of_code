from aoc_utils import *

inp = read_input(2023, 13)

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

total = 0
for map in maps:
    total += solve_map(transpose(map))
    total += 100*solve_map(map)
    
print(total)