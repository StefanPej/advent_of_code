from aoc_utils import *

test = read_input(2025, 5, filename='test')
inp = read_input(2025, 5)

ranges = []
for line in inp:
    if line == "":
        break
    lower, upper = map(int, line.split("-"))
    ranges.append((lower, upper))

no_overlaps = [ranges[0]]

for low_ran_og, high_ran_og in ranges[1:]:
    new_ranges = [(low_ran_og, high_ran_og)]
    while new_ranges:
        low_ran, high_ran = new_ranges.pop()
        has_changed = False
        for low_other, high_other in no_overlaps:    
            if low_ran >= low_other and high_ran <= high_other: # new range completely enclosed
                has_changed = True
                break
            elif low_ran < low_other and high_ran > high_other: # new range completely overlaps
                new_low = (low_ran, low_other-1)
                new_high = (high_other + 1, high_ran)
                new_ranges.append(new_low)
                new_ranges.append(new_high)
                has_changed = True
                break
            elif low_ran < low_other and high_ran >= low_other: # lower bound is outside but upper inside
                new_low = (low_ran, low_other-1)
                new_ranges.append(new_low)
                has_changed = True
                break
            elif low_ran <= high_other and high_ran > high_other: # high bound is outside but lower insider
                new_high = (high_other + 1, high_ran)
                new_ranges.append(new_high)
                has_changed = True
                break
        if not has_changed:
            no_overlaps.append((low_ran, high_ran))

count = 0
for small, big in no_overlaps:
    diff = big - small + 1
    count += diff

print(count)