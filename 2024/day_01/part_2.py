from aoc_utils import *

inp = read_input(2024, 1)
left = []
right = []

for i in inp:
    left_n, right_n = i.split()
    left.append(int(left_n))
    right.append(int(right_n))

r_counter = {}

for num in right:
    if not num in r_counter:
        r_counter[num] = 1
    else:
        r_counter[num] += 1

total = 0

for num in left:
    r_amount = r_counter.get(num, 0)
    total += r_amount * num

print(total)