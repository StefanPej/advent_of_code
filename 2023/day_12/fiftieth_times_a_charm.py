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
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    if len(grouped_broken) != len(groups):
        return 0
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return 0
    #print(spring)
    return 1

@cache
def solve(spring, groups):
    #print(spring)
    spring_str = "".join(char for char in spring)
    spring = list(spring)

    for i in range(len(spring)):
        if spring[i] == '?':
            spring[i] = '#'
            left = spring.copy()
            spring[i] = '.'
            right = spring.copy()
            return solve(tuple(left), groups) + solve(tuple(right), groups)

    return check_valid(spring_str, groups)

cache = {}
    
# test = springs[5]
# print(test)
# print(solve(test[0], test[1], 0))
# #print(solve(test[0], test[1], 1))
    
total = 0
for spring in springs[5:6]:
    total += solve(tuple(spring[0]), tuple(spring[1]))
print(total)