from aoc_utils import *
from functools import cache

inp = read_input(2023, 12)

# with open("./2023/day_12/test.txt", "r") as o:
#     inp = o.readlines()

springs = []
for line in inp:
    spring, broken = line.split()
    temp_sp = []
    temp_br = []
    for _ in range(5):
        temp_sp.append(spring)
        temp_br.append(broken)
    spring = "?".join(sp for sp in temp_sp)
    broken = ','.join(br for br in temp_br)
    broken = broken.split(',')
    broken = [int(broke) for broke in broken]
    springs.append((spring, tuple(broken)))

@cache
def solve(spring, groups):
    
    #groups_done = check_groups_places(spring, groups, index)
    #key = (tuple(spring[index:]), left_to_place, groups_done)
    

    # if not check_if_borked(spring, groups, index):
    #     #cache_[key] = 0
    #     return 0

    if not groups:
        if '#' in spring:
            return 0
        return 1
        
    if not spring:
        if len(groups) > 0:
            return 0
        return 1
    
    if not '#' in spring and not '?' in spring:
        if len(groups) == 0:
            return 1
        return 0

    current_char = spring[0]
    rest_of_spring = spring[1:]

    while current_char not in '#?':
        current_char = rest_of_spring[0]
        rest_of_spring = rest_of_spring[1:]

    if current_char == '?':
        return solve('#'+rest_of_spring, groups) + solve('.'+rest_of_spring, groups)
    
    if current_char == '#':
        if len(current_char+rest_of_spring) >= groups[0] and '.' not in (current_char+rest_of_spring)[:groups[0]]:
            if len(current_char+rest_of_spring) > groups[0]:
                if (current_char+rest_of_spring)[groups[0]] == '#':
                    return 0
            return solve(rest_of_spring[groups[0]:], groups[1:])
        return 0
    
print(apply_function_get_total(solve, springs, 'sum'))