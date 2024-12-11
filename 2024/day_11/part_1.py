from aoc_utils import *
from collections import deque

test = read_input(2024, 11, filename='test')
inp_ = read_input(2024, 11)

inp = test
inp = inp_

inp = inp[0].split()

def process(s):
    if s == '0':
        return ['1']
    elif len(s) % 2 == 0:
        l, r = s[:len(s)//2], s[len(s)//2:]
        if len(r) > 1:
            if r == '0'*len(r):
                r = '0'
            else:
                r = r.lstrip('0')
        return [l, r]
    else:
        return [str(int(s)*2024)]

Q = deque(inp)
for _ in range(25):
    new = deque()
    while Q:
        s = Q.popleft()
        r = process(s)
        for rs in r:
            new.append(rs)
    Q = new

print(len(Q))