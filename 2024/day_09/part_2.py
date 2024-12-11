from aoc_utils import *

test = read_input(2024, 9, filename='test')
inp_ = read_input(2024, 9)

inp = test
inp = inp_

inp = inp[0]

fl = []
sl = []

f = True
fn = 0
i = 0

for char in inp:
    n = int(char)
    if f:
        fl.append([fn, i, n])
        fn += 1
    else:
        sl.append([i, n])
    f = not f
    i += n

fln = []
for f in fl[::-1]:
    fn, fs, fle = f
    for i, s in enumerate(sl):
        ss, sle = s

        if fs < ss:
            break

        if fle <= sle:
            fs = ss
            ss += fle
            sle -= fle
            sl[i] = [ss, sle]
            break
    fln.append([fn, fs, fle])

ans = 0
for f in fln:
    fn, fs, fle = f
    for i in range(fle):
        ans += fn * (fs + i)

print(ans)