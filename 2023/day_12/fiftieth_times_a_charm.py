from aoc_utils import *

inp = read_input(2023, 12)

# with open("./2023/day_12/test.txt", "r") as o:
#     inp = o.readlines()

springs = []
for line in inp:
    spring, broken = line.split()
    broken = broken.split(',')
    broken = [int(broke) for broke in broken]
    springs.append(([*spring], broken))

def check_valid(spring, groups):
    spring = ''.join(char for char in spring)
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    if len(grouped_broken) != len(groups):
        return 0
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return 0
    #print(spring)
    return 1

def solve(spring, groups, index):
    #print(spring)
    spring_str = "".join(char for char in spring)
    if spring_str in cache:
        return cache[spring_str]
    
    if index >= len(spring):
        cache[spring_str] = check_valid(spring_str, groups)
        return cache[spring_str]

    for i in range(index, len(spring)):
        if spring[i] == '?':
            spring[i] = '#'
            left = spring.copy()
            spring[i] = '.'
            right = spring.copy()
            return solve(left, groups, i) + solve(right, groups, i)

    cache[spring_str] = check_valid(spring_str, groups)
    return cache[spring_str]

cache = {}
    
# test = springs[5]
# print(test)
# print(solve(test[0], test[1], 0))
# #print(solve(test[0], test[1], 1))
    
total = 0
for spring in springs:
    total += solve(spring[0], spring[1], 0)
print(total)