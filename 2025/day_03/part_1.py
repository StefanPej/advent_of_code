from aoc_utils import *

t = """987654321111111
811111111111119
234234234234278
818181911112111"""
t = t.split("\n")

inp = read_input(2025, 3)

count = 0
for line in inp:
    l, r = len(line)-2, len(line)-1,
    
    l_ind = l
    while l > 0:
        new_l = l - 1
        if line[new_l] >= line[l_ind]:
            l_ind = new_l

        l = new_l

    r_ind = r
    while r > l_ind + 1:
        new_r = r - 1
        if line[new_r] >= line[r_ind]:
            r_ind = new_r

        r = new_r

    val = int(line[l_ind] + line[r_ind])
    count += val

print(count)