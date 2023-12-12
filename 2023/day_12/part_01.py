from aoc_utils import *
from itertools import combinations

inp = read_input(2023, 12)

springs = []
for line in inp:
    spring, broken = line.split()
    broken = broken.split(',')
    broken = [int(broke) for broke in broken]
    springs.append((spring, broken))

def check_valid(spring, groups):
    spring = ''.join(char for char in spring)
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return False
    return True


def solve(spring):
    springs = spring[0]
    groups = spring[1]

    already_broken = springs.count('#')
    need_to_place = sum(groups) - already_broken

    q_marks = []
    for i, char in enumerate(springs):
        if char == '?':
            q_marks.append(i)

    all_possibilities = [combo for combo in combinations(q_marks, need_to_place)]

    count = 0
    for poss in all_possibilities:
        temp = [*springs]
        for ind in poss:
            temp[ind] = '#'

        for i, char in enumerate(temp):
            if char == '?':
                temp[i] = '.'
        #print(temp)
        if check_valid(temp, groups):
            count += 1
    
    return count
            
print(solve(springs[32]))
#print(apply_function_get_total(solve, springs, 'add'))