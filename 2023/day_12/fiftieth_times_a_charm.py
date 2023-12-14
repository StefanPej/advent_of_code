from aoc_utils import *
from functools import cache

inp = read_input(2023, 12)

with open("./2023/day_12/test.txt", "r") as o:
    inp = o.readlines()

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
    springs.append(([*spring], broken))

def check_valid(spring, groups):
    spring = ''.join(char for char in spring)
    spring = spring.replace('?', '.')
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    if len(grouped_broken) != len(groups):
        return 0
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return 0
    #print(spring)
    return 1

def check_if_possible(spring, groups, left_to_place):
    spring = ''.join(char for char in spring)
    amt_q = spring.count('?')
    amt_hash = spring.count('#')
    spring = spring.replace('?', '.')
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    if amt_q < left_to_place-amt_hash:
        return 0
    if len(grouped_broken) > len(groups):
        #print('asdasd')
        return 0
    if max(groups) < len(max(grouped_broken, key=len)):
        return 0
    return 1

def check_if_borked(spring, groups, index):
    spring = spring[:index+1]
    spring = ''.join(char for char in spring)
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    
    if len(grouped_broken) > len(groups):
        return 0
    
    for i, broke in enumerate(grouped_broken):
        if len(broke) > groups[i]:
            return 0
        
    return 1
    

def solve(spring, groups, index, left_to_place):

    
    if left_to_place == 0 or '?' not in spring:
        cache_[(tuple(spring[index:]), left_to_place)] = check_valid(spring, groups)
        return check_valid(spring, groups)
    
    if not check_if_borked(spring, groups, index):
        cache_[(tuple(spring[index:]), left_to_place)] = 0
        return 0
    
    if (tuple(spring[index:]), left_to_place) in cache_:
        return cache_[(tuple(spring[index:]), left_to_place)]

    for i in range(index, len(spring)):
        if spring[i] == '?':
            spring[i] = '#'
            left = spring.copy()
            spring[i] = '.'
            right = spring.copy()
            return solve(left, groups, i, left_to_place-1) + solve(right, groups, i, left_to_place)
        
    cache_[(tuple(spring[index:]), left_to_place)] = check_valid(spring, groups)
    return cache_[(tuple(spring[index:]), left_to_place)]

cache_ = {}
    
# test = springs[5]
# print(test)
# print(solve(test[0], test[1], 0))
# #print(solve(test[0], test[1], 1))
    
total = 0
for spring in springs[5:]:
    total += solve(spring[0], spring[1], 0, sum(spring[1]))
print(total)