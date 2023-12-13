from aoc_utils import *

inp = read_input(2023, 13)

# with open('2023/day_13/test.txt') as o:
#     inp = o.readlines()
# inp = [line.strip() for line in inp]

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

def reflect_char(line, index):
    split = [*line]
    if split[index] == '.':
        split[index] = '#'
    else:
        split[index] = '.'
    return ''.join(char for char in split)

maps_og_soln = {i:'' for i in range(len(maps))}

total = 0
for i, map in enumerate(maps):
    if solve_map(transpose(map)):
        maps_og_soln[i] = ('vert', solve_map(transpose(map)))
    if solve_map(map):
        maps_og_soln[i] = ('hori', solve_map(map))
        
print(maps_og_soln)

def try_map(map):
    total = 0
    total += solve_map(transpose(map))
    total += 100*solve_map(map)
    return total


def solve_maps(map, ind):
    eh = []
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            temp = map.copy()
            #print(temp)
            temp[i] = reflect_char(temp[i], j)
            #print(temp)
            if solve_map(transpose(temp)):
                eh.append(('vert', solve_map(transpose(temp))))
                if maps_og_soln[ind] != ('vert', solve_map(transpose(temp))):
                    #print(('vert', solve_map(transpose(temp))))
                    #print('found dupe')
                    print('adding: ', solve_map(transpose(temp)))
                    return solve_map(transpose(temp))
            if solve_map(temp):
                eh.append(('hori', solve_map(temp)))
                if maps_og_soln[ind] != ('hori', solve_map(temp)):
                    print('adding: ', 100*solve_map(temp))
                    return 100*solve_map(temp)
    #print(eh)
    # og_soln = maps_og_soln[ind]
    # #print(og_soln)
    # if og_soln[0] == 'hori':
    #     #print('1234')
    #     print('adding: ', 100*og_soln[1])
    #     return 100*og_soln[1]
    # print('adding: ', og_soln[1])
    return try_map(map)
    
    
total = 0
for ind, map in enumerate(maps):
    print(ind)
    total += solve_maps(map, ind)
    


    
print(total)