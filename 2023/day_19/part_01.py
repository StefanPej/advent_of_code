from aoc_utils import *

inp = read_input(2023, 19)

# with open('2023/day_19/test.txt') as o:
#     inp = o.readlines()

doing_workflows = True

workflows_l = []
parts = []

for line in inp:
    if line == "":
        doing_workflows = False
        continue
    if doing_workflows:
        workflows_l.append(line)
    else:
        parts.append(line)

workflows = {}

for flow in workflows_l:
    flow_name, instructions = flow.split('{')
    instructions = instructions.rstrip('}')
    inst_list = instructions.split(',')
    workflows[flow_name] = inst_list

def run_instruction(part, inst):
    if not ':' in inst:
        return inst
    instruction, loc = inst.split(':')
    val = instruction[0]
    operation = instruction[1]
    comparitor = instruction[2:]

    part_val = int(part[val])

    if operation == '<':
        if part_val < int(comparitor):
            return loc
    if operation == '>':
        if part_val > int(comparitor):
            return loc

    return False

parts = [part.replace('=',':') for part in parts]

clean_parts = []
for part in parts:
    part = part.replace('{', '').replace('}', '')
    part_l = part.split(',')
    new_dict = {}
    for l in part_l:
        name, num = l.split(':')
        new_dict[name] = num
    clean_parts.append(new_dict)

total = 0
for part in clean_parts:
    inst = 'in'
    while inst not in 'RA':
        instructions = workflows[inst]
        for ins in instructions:
            inst = run_instruction(part, ins)
            if inst:
                break
    if inst == 'A':
        total += int(part['x']) + int(part['m']) + int(part['a']) + int(part['s']) 

print(total)


    