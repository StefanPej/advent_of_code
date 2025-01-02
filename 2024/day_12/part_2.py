from aoc_utils import *
from collections import deque

test = read_input(2024, 12, filename='test2')
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

def find_topleft(grid):
    for r, l in enumerate(grid):
        for c, ch in enumerate(l):
            if ch == 'X':
                return (r-1,c)
            
def write_grid(grid):
    with open('./2024/day_12/help.txt', 'w+') as f:
        for line in grid:
            f.write("".join(line))
            f.write("\n")

def trace_outside(grid):
    ans = 0
    dirs = {'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)}

    tl = find_topleft(grid)
    seen = set()
    tr = dirs['R']
    r, c = tl
    first = True
    while True:

        if not first:
            if (r,c) == tl:
                break
            seen.add((r, c))
        first = False
        grid[r][c] = '*'

        if tr == dirs['R']:
            if not grid[r + dirs['D'][0]][c + dirs['D'][1]] == 'X':
                tr = dirs['D']
                r, c = r + tr[0], c + tr[1]
                ans += 1
            elif grid[r + tr[0]][c + tr[1]] == 'X':
                tr = dirs['U']
                ans += 1
            elif not grid[r + tr[0]][c + tr[1]] == 'X':
                r, c = r + tr[0], c + tr[1]
        elif tr == dirs['D']:
            if not grid[r + dirs['L'][0]][c + dirs['L'][1]] == 'X':
                tr = dirs['L']
                r, c = r + tr[0], c + tr[1]
                ans += 1
            elif grid[r + tr[0]][c + tr[1]] == 'X':
                tr = dirs['R']
                ans += 1
            elif not grid[r + tr[0]][c + tr[1]] == 'X':
                r, c = r + tr[0], c + tr[1]
        elif tr == dirs['L']:
            if not grid[r + dirs['U'][0]][c + dirs['U'][1]] == 'X':
                tr = dirs['U']
                r, c = r + tr[0], c + tr[1]
                ans += 1
            elif grid[r + tr[0]][c + tr[1]] == 'X':
                tr = dirs['D']
                ans += 1
            elif not grid[r + tr[0]][c + tr[1]] == 'X':
                r, c = r + tr[0], c + tr[1]
        elif tr == dirs['U']:
            if not grid[r + dirs['R'][0]][c + dirs['R'][1]] == 'X':
                tr = dirs['R']
                r, c = r + tr[0], c + tr[1]
                ans += 1
            elif grid[r + tr[0]][c + tr[1]] == 'X':
                tr = dirs['L']
                ans += 1
            elif not grid[r + tr[0]][c + tr[1]] == 'X':
                r, c = r + tr[0], c + tr[1]
    return ans

edges = {}
for k, v in regs.items():
    grid = [["." for _ in range(len(inp[0]) + 2)] for _ in range(len(inp) + 2)]

    for r, c, _ in v:
        grid[r+1][c+1] = 'X'

    outside_edges = trace_outside(grid)
    edges[k] = {'outside': outside_edges, 'inside': 0}

def flood_fill(grid):
    seen = set()
    start = (0,0)
    Q = deque()
    Q.append(start)
    while Q:
        cr, cc = Q.popleft()
        if (cr, cc) in seen:
            continue
        grid[cr][cc] = '+'
        for (dr, dc) in [(-1,0), (1,0), (0,-1), (0,1)]:
            if 0 <= cr + dr < len(grid) and 0 <= cc + dc < len(grid[0]):
                if grid[cr+dr][cc+dc] == '.':
                    Q.append((cr+dr, cc+dc))
        seen.add((cr,cc))
    return grid

for k, v in regs.items():
    grid = [["." for _ in range(len(inp[0]) + 2)] for _ in range(len(inp) + 2)]

    for r, c, _ in v:
        grid[r+1][c+1] = 'X'

    grid = flood_fill(grid)

    for k1, v1 in regs.items():
        if k1 == k:
            continue
        r, c, _ = v1[0]
        if grid[r+1][c+1] == '.':
            edges[k]['inside'] += edges[k1]['outside']

ans = 0
for k, v in regs.items():
    a = len(v)
    e = sum(edges[k].values())
    ans += a*e

print(ans)