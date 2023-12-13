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
        if map[start] != map[end]:
            return False
        start -= 1
        end += 1
    return True


def solve_map(map):
    # There can be more than one reflection point now, store all of them
    reflection_points = []
    for i in range(1,len(map)):
        if map[i] == map[i-1]:
            temp_ref = i-1
            if confirm_reflection(map, temp_ref):
                reflection_points.append(temp_ref + 1)
    return reflection_points


def reflect_char(line, index):
    split = [*line]
    split[index] = '#' if split[index] == '.' else '#'
    return ''.join(char for char in split)


def solve_maps(map, ind):
    # Try changing everything one-by one
    for i in range(len(map)):
        for j in range(len(map[i])):
            # Flip the char
            temp = map.copy()
            temp[i] = reflect_char(temp[i], j)

            # Get all vertical/horizontal solns. Return the one that aint in the OG
            if solve_map(transpose(temp)):
                for soln in solve_map(transpose(temp)):
                    if soln not in maps_og_soln[ind]['vert']:
                        return soln
            if solve_map(temp):
                for soln in solve_map(temp):
                    if soln not in maps_og_soln[ind]['hori']:
                        return 100*soln
                
# Get all OG solns from P1
maps_og_soln = {i:{'vert':[], 'hori':[]} for i in range(len(maps))}
for i, map in enumerate(maps):
    if solve_map(transpose(map)):
        maps_og_soln[i]['vert'] = solve_map(transpose(map))
    if solve_map(map):
        maps_og_soln[i]['hori'] = solve_map(map)
        

total = 0
for ind, map in enumerate(maps):
    total += solve_maps(map, ind)
print(total)