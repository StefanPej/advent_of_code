from aoc_utils import *
from collections import deque

test = read_input(2024, 12, filename='test')
inp_ = read_input(2024, 12)

inp = test
inp = inp_

inp = [list(line) for line in inp]

SEEN = set()
regs = {}

for r, l in enumerate(inp):
    for c, ch in enumerate(l):
        if (r,c) in SEEN:
            continue
        Q = deque()
        Q.append(((r,c), (r,c)))
        SEEN.add((r,c))
        regs[(r,c)] = []
        while Q:
            reg, coords = Q.popleft()
            sides = 4
            cr, cc = coords

            for (dr, dc) in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= cr + dr < len(inp) and 0 <= cc + dc < len(inp[0]):
                    if inp[cr+dr][cc+dc] == ch:
                        sides -= 1
                        if (cr+dr, cc+dc) not in SEEN:
                            Q.append((reg, (cr+dr, cc+dc)))
                        SEEN.add((cr+dr, cc+dc))
            regs[reg].append((cr,cc,sides))

ans = 0      
for k, v in regs.items():
    a = len(v)
    p = sum([va[2] for va in v])
    ans += a*p
print(ans)