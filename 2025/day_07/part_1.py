from aoc_utils import *

inp = read_input(2025, 7)
test = read_input(2025, 7, filename='test')

inp = [[char for char in line] for line in inp]

beams = [inp[0].index('S')]
splits = 0
for line in inp[1:]:
    new_beams = []
    while beams:
        beam = beams.pop()
        if line[beam] == ".":
            new_beams.append(beam)
            line[beam] = "|"
        if line[beam] == "^":
            splits += 1
            if beam - 1 >= 0:
                new_beams.append(beam - 1)
                line[beam - 1] = "|"
            if beam + 1 <= len(line) - 1:
                new_beams.append(beam + 1)
                line[beam + 1] = "|"
    beams = new_beams

print(splits)
