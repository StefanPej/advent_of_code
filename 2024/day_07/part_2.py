from aoc_utils import *

test = read_input(2024, 7, filename='test')
inp_ = read_input(2024, 7)

inp = test
inp = inp_

inp = [[int(i.split(":")[0]), list(map(int, i.split(":")[1].split()))] for i in inp]

#smart
def is_poss(target, running_total, nums):
    if running_total == target and not nums:
        return True
    if not nums or running_total > target:
        return False
    nums_copy = nums.copy()
    next_num = nums_copy.pop(0)

    running_total_plus = running_total + next_num
    running_total_mult = running_total * next_num
    running_total_concat = int(str(running_total) + str(next_num))
    return is_poss(target, running_total_plus, nums_copy) or is_poss(target, running_total_mult, nums_copy) or is_poss(target, running_total_concat, nums_copy)

ans = 0
for line in inp:
    target, nums = line
    nums_copy = nums.copy()
    running_total = nums_copy.pop(0)
    if is_poss(target, running_total, nums_copy):
        ans += target
print(ans)

# smarter
ans = 0
for line in inp:
    target, nums = line
    possibilities = [nums.pop(0)]
    while True:
        if target in possibilities and not nums:
            ans += target
            break
        if not nums:
            break
        num = nums.pop(0)
        for i in range(len(possibilities)):
            possibilities.append(possibilities[i] * num)
            possibilities.append(int(str(possibilities[i]) + str(num)))
            possibilities[i] = possibilities[i] + num
print(ans)