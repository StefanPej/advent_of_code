from aoc_utils import *

test = read_input(2022, 10, filename='test')
inp = read_input(2022, 10)

counter = 1
X = 1
ans = 0
num = 0
waiting = False
instruction_counter = 0

while counter < 221:
    if counter in [20, 60, 100, 140, 180, 220]:
        ans += X * counter

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

print(ans)
    


