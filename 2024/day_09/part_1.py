from aoc_utils import *

test = read_input(2024, 9, filename='test')
inp_ = read_input(2024, 9)

inp = test
inp = inp_

inp = inp[0]

il = []

file = True
id = 0
for i in range(len(inp)):
    num = int(inp[i])
    for _ in range(num):
        if file:
            il.append(id)
        else:
            il.append(".")
    if file:
        id += 1
    file = not file

l = 0
r = len(il)-1
while l < r:
    if il[l] == "." and il[r] != ".":
        il[l], il[r] = il[r], il[l]
        l += 1
        r -= 1
    elif il[l] != ".":
        l += 1
    elif il[r] == ".":
        r -= 1

ans = 0
for i, num in enumerate(il):
    if isinstance(num, int):
        ans += num * i

print(ans)
        