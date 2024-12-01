from aoc_utils import *

inp = read_input(2024, 1)
left = []
right = []

for i in inp:
    left_n, right_n = i.split()
    left.append(int(left_n))
    right.append(int(right_n))

left.sort()
right.sort()

total = 0
for ln, rn in zip(left, right):
    diff = abs(ln-rn)
    total += diff

print(total)