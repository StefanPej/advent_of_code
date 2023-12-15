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


def get_instuctions(seq):
    if '-' in seq:
        return seq.split("-")[0], '-'
    elif '=' in seq:
        return seq.split('=')
    raise RuntimeError('you fucking IDIOT')


boxes = {i:[] for i in range(256)}
for seq in inp:
    label, inst = get_instuctions(seq)
    box = get_hash(label)
    box_conts = boxes[box]
    lens = False
    if label in [cont[0] for cont in box_conts]:
        lens = [cont for cont in box_conts if cont[0] == label][0]
        lens_index = box_conts.index(lens)
    if inst.isdigit():
        if lens:         
            box_conts.pop(lens_index)
            box_conts.insert(lens_index, (label, inst))
        else:    
            box_conts.append((label, inst))
    elif inst == '-':
        if lens:
            box_conts.pop(lens_index)

total = 0
for k, v in boxes.items():
    box_num = k+1
    sub_tot = 0
    for i, lens in enumerate(v, start=1):
        sub_tot += i*int(lens[1])*box_num
    total += sub_tot

print(total)