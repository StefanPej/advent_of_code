from aoc_utils import *

test = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

inp_ = read_input(2025, 2)[0]

def parse_inp(text):
    return [(int(bracket.split('-')[0]),int(bracket.split('-')[1])) for bracket in text.split(',')]

test = parse_inp(test)
inp_ = parse_inp(inp_)

def is_nonsense(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        sl = str_num[:i]
        times_needed = len(str_num)/i
        if times_needed != int(times_needed):
            continue
        
        if sl*int(times_needed) == str_num:
            return True

count = 0
for start, end in inp_:
    for i in range(start, end + 1):
        if is_nonsense(i):
            count += i
            

print(count)