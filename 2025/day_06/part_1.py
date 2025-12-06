from aoc_utils import *

inp = read_input(2025, 6)
test = read_input(2025, 6, filename='test')

inp = [line.split() for line in inp]

num_problems = len(inp[0])

count = 0
for i in range(num_problems):
    if inp[-1][i] == "+":
        ans = 0
        for line in inp[:-1]:
            ans += int(line[i])
    else:
        ans = 1
        for line in inp[:-1]:
            ans *= int(line[i])
    count += ans

print(count)