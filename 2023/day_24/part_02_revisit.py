from aoc_utils import *
import sympy

inp = read_input(2023, 24)
#inp = read_input(2023, 24, filename='test')

def parse_info(line):
    return tuple(map(int, line.replace('@', ',').split(',')))

stones = [parse_info(line) for line in inp]

sx_, sy_, sz_, vx_, vy_, vz_ = sympy.symbols("sx_ sy_ sz_ vx_ vy_ vz_")

ans = sympy.solve([(vy - vy_)*(vz - vz_)*(sx_ - sx) - (vx - vx_)*(vz - vz_)*(sy_ - sy)  for sx, sy, sz, vx, vy, vz in stones[:20]])
ans2 = sympy.solve([(vy - vy_)*(vz - vz_)*(sx_ - sx) - (vx - vx_)*(vy - vy_)*(sz_ - sz)  for sx, sy, sz, vx, vy, vz in stones[:20]])

for poss1 in ans:
    for poss2 in ans2:
        if not all([poss1.get(sx_), poss2.get(sx_), poss1.get(vx_), poss2.get(vx_)]):
            continue
        if poss1[sx_] == poss2[sx_] and poss1[vx_] == poss2[vx_]:
            print(poss1[sx_]+poss1[sy_]+poss2[sz_])