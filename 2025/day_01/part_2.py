from aoc_utils import *

inp = read_input(2025, 1)

dial = 50
count = 0
for line in inp:
    dir = line[0]
    num = int(line[1:])

    mult = -1 if dir == 'L' else 1

    for _ in range(num):
        dial = dial + mult*1
        dial = dial % 100
        if dial == 0:
            count += 1
    
print(count)