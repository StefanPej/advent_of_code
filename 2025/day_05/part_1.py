from aoc_utils import *

test = read_input(2025, 5, filename='test')
inp = read_input(2025, 5)

ranges = []
ing = []

filling_ranges = True
for line in inp:
    if line == "":
        filling_ranges = False
        continue

    if filling_ranges:
        ranges.append(line)

    else:
        ing.append(line)

count = 0
for i in ing:
    fresh = False
    for ran in ranges:
        lower, upper = map(int, ran.split("-"))
        if int(i) in range(lower, upper+1):
            fresh = True

    count += fresh


print(count)