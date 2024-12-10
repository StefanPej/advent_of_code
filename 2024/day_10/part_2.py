from aoc_utils import *
from collections import deque

test = read_input(2024, 10, filename='test')
inp_ = read_input(2024, 10)

inp = test
inp = inp_

inp = [list(map(int, list(line))) for line in inp]

def do_dfs(row, col, inp):
    ans = 0
    DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    Q = deque()
    Q.append((0, row, col))

    while Q:
        n, r, c = Q.popleft()

        if n == 9:
            ans += 1

        for rc, cc in DIRS:
            nr, nc = r + rc, c + cc
            
            if not ((0 <= nr < len(inp)) and (0 <= nc < len(inp[0]))):
                continue

            if inp[nr][nc] == n + 1:
                Q.append((n+1, nr, nc))

    return ans

ans = 0
for r, l in enumerate(inp):
    for c, ch in enumerate(l):
        if ch == 0:
            ans += do_dfs(r, c, inp)

print(ans)