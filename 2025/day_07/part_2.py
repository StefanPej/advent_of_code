from aoc_utils import *
from functools import cache

inp = read_input(2025, 7)
test = read_input(2025, 7, filename='test')

inp = [[char for char in line] for line in inp]

beam = (0, inp[0].index('S'))

@cache
def solve(beam):
    if beam[1] < 0 or beam[1] > len(inp[0])-1:
        return 0
    while beam[0] < len(inp):
        if inp[beam[0]][beam[1]] in ".S":
            beam = (beam[0] + 1, beam[1])
        elif inp[beam[0]][beam[1]] == "^":
            return solve((beam[0], beam[1] - 1)) + solve((beam[0], beam[1] + 1))
    return 1

print(solve(beam))