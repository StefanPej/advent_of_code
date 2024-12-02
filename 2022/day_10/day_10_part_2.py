from aoc_utils import *


test = read_input(2022, 10, filename='test')
inp = read_input(2022, 10)
out = ["." for _ in range(240)]
counter = 0

X = 1
ans = 0
num = 0
waiting = False
instruction_counter = 0
while counter < 240:
    if counter%40 in [X-1, X, X+1]:
        out[counter] = "#"


    if waiting:
        X += num
        waiting = False
        counter += 1
        continue

    if not waiting:
        instruction = inp[instruction_counter % len(inp)]
        instruction_counter += 1

        if instruction != 'noop' :
            num = int(instruction.split()[1])
            waiting = True
    counter += 1

min_ind = 0
max_ind = 40

while max_ind <= 240:
    print(out[min_ind:max_ind])
    min_ind += 40
    max_ind += 40