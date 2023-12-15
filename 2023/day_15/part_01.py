from aoc_utils import *

inp = read_input(2023, 15)

inp = [line.strip() for line in inp]
inp = [item for item in inp[0].split(',')]

def get_hash(string):
    
    ret = 0
    for char in string:
        ret += ord(char)
        ret *= 17
        ret = ret%256
        
    return ret

print(apply_function_get_total(get_hash, inp, 'add'))