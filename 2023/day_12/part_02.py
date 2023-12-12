from aoc_utils import *
from itertools import combinations

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

    spring_broken = [group for group in springs.split('.') if group != '']
    biggest_group = max(spring_broken, key=len)
    if len(biggest_group) == max(groups):
       spring_broken[spring_broken.index(biggest_group)] = '#'*max(groups)

    springs = "".join(char for char in spring_broken)

    spring_broken = [*springs]
    for i, char in enumerate(spring_broken):
        if char == '.':
            continue
        if char == '?':
            break
        if char == '#':
            hash_count = 1
            ind = i
            while hash_count < groups[0]:
                ind += 1
                spring_broken[ind] = '#'
                hash_count += 1
            spring_broken[ind+1] = '.'
            groups.pop(0)
            break
    
    springs = "".join(char for char in spring_broken)

    spring_broken = [*springs]
    for i, char in enumerate(reversed(spring_broken)):
        if char == '.':
            continue
        if char == '?':
            break
        if char == '#':
            hash_count = 1
            ind = len(spring_broken) -1 -i
            while hash_count < groups[-1]:
                ind -= 1
                spring_broken[ind] = '#'
                hash_count += 1
            spring_broken[ind+1] = '.'
            groups.pop(-1)
            break
    
    springs = "".join(char for char in spring_broken)
    print(springs, groups)

    already_broken = springs.count('#')
    need_to_place = sum(groups) - already_broken

    q_marks = []
    for i, char in enumerate(springs):
        if char == '?':
            q_marks.append(i)


    print(len(q_marks), need_to_place)
    # count = 0
    # for poss in combinations(q_marks, need_to_place):
    #     count += 1
    #     temp = [*springs]
    #     for ind in poss:
    #         temp[ind] = '#'

    #     for i, char in enumerate(temp):
    #         if char == '?':
    #             temp[i] = '.'
    #     #print(temp)
    #     if check_valid(temp, groups):
    #         count += 1
    
    return #count

print(solve(springs[77]))
# if __name__ == '__main__':   
#     from multiprocessing import Pool

#     pool = Pool(5)

#     results = []
#     for result in pool.map(solve, springs):
#         results.append(result)
#         if len(results) % 10 == 0:
#             print(len(results))

#    print(sum(results))
    #print(apply_function_get_total(solve, springs, 'add'))

#[print(spring) for spring in springs]