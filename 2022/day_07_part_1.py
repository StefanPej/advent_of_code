from utils2022 import read_input
from collections import defaultdict

input = read_input('07')

dirs = {'root':{}}

def parse_instructions(input, line_no):
    line = input[line_no]
    if line.startswith('$'):
        if 'cd' in line:
            if '/' in line:
                return 'root'
            elif '..' in line:
                return 'up'
            else:
                return line.split()[2]
        if 'ls' in line:
            contents = []
            while True:
                line_no += 1
                line = input[line_no]
                if line.startswith('$'):
                    break
                contents.append(line)
            return contents
    return None

current_dir = 'root'
depth_tracker = ['root']
for i in range(len(input)):
    instruction = parse_instructions(input, i)
    print(i+1, instruction)
    if not instruction:
        continue
    if instruction == 'root':
        current_dir = 'root'
        depth_tracker = ['root']
        dir = dirs['root']
    elif instruction == 'up':
        current_dir = depth_tracker[-1]
        depth_tracker.pop()
        if not depth_tracker:
            depth_tracker = ['root']
        dir = dirs
        for level in depth_tracker:
            dir = dir.get(level)
        print(dir)
    elif type(instruction) == str:
        if not current_dir == 'root':
            depth_tracker.append(current_dir)
        current_dir = instruction
        dir = dir.get(current_dir)
        print(dir)
    elif type(instruction) == list:
        for item in instruction:
            if item.startswith('d'):
                dir[item.split()[1]] = {}
            else:
                dir[item.split()[1]] = int(item.split()[0])
print(dirs)


