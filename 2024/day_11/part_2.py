from aoc_utils import *
from collections import defaultdict

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

c = defaultdict(int)

for num in inp:
    c[num] += 1


for _ in range(75):
    c_new = defaultdict(int)
    for num, n in c.items():
        r = process(num)
        for rs in r:
            c_new[rs] += n
    
    c = c_new

print(sum(c.values()))