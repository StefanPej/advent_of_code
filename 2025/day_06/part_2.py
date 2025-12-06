from aoc_utils import *
import math

inp = read_input(2025, 6, strip=False)
test = read_input(2025, 6, filename='test', strip=False)

num_lens = []
count = 0
for i, char in enumerate(inp[-1][1:]):
    if i == len(inp[-1]) - 2:
        num_lens.append(count + 2)
    elif char == " ":
        count += 1
    else:
        num_lens.append(count)
        count = 0

inp_ = []
for line in inp:
    slice_start = 0
    temp_line = []
    slice_num = 0
    while slice_start <= len(inp[0].strip()):
        if slice_num >= len(num_lens):
            slice_num -= 1
        temp_line.append(line[slice_start:slice_start+num_lens[slice_num]])
        slice_start += num_lens[slice_num]+1
        slice_num += 1
    inp_.append(temp_line)

def make_numbers(nums):
    new_nums = ["" for _ in range(len(nums[0]))]
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            new_nums[i] += nums[j][i]
    return [int(num) for num in new_nums]

num_problems = len(inp_[0])
count = 0
for i in range(num_problems):
    nums = [line[i] for line in inp_[:-1]]
    new_nums = make_numbers(nums)

    if inp_[-1][i].strip() == "+":
        count += sum(new_nums)
    else:
        count += math.prod(new_nums)

print(count)