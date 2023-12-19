from aoc_utils import *

inp = read_input(2023, 19)

# with open('2023/day_19/test.txt') as o:
#     inp = o.readlines()
# inp = [line.strip() for line in inp]

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

def run_instruction(part, instruction):
    if not ':' in instruction:
        return [(instruction, part)]
    
    comparison, dest = instruction.split(':')

    letter_to_check = comparison[0]
    operator = comparison[1]
    number_to_check = int(comparison[2:])

    part_min, part_max = part[letter_to_check]

    if part_min <= number_to_check <= part_max:
        if operator == '>':
            new_range = (number_to_check+1, part_max)
            continue_range = (part_min, number_to_check)
        else:
            new_range = (part_min, number_to_check-1)
            continue_range = (number_to_check, part_max)
        new_dict = part.copy()
        continue_dict = part.copy()
        new_dict[letter_to_check] = new_range
        continue_dict[letter_to_check] = continue_range

        return [(dest, new_dict), (False, continue_dict)]
    
    return [(False, part)]


def run_workflow(part, flow):
    ret = []
    for inst in flow:
        output = run_instruction(part, inst)
        if len(output) == 2:
            ret.append(output[0])
            part = output[1][1]
            out = output
        else:
            part = output[0][1]
            out = output
    if len(out) == 1:
        ret.append(out[0])
    return ret

all_parts = {'x':(1,4000), 'm':(1,4000), 'a':(1,4000), 's':(1,4000)}

accepted = []
parts = [('in', all_parts)]
while parts:
    part = parts.pop(0)
    flow, part_dic = part
    out = run_workflow(part_dic, workflows[flow])
    for x in out:
        if x[0] == 'A':
            accepted.append(x)
        elif x[0] != 'R':
            parts.append(x)

total = 0
for accept in accepted:
    acc_dict = accept[1]
    sub_val = 1
    for v in acc_dict.values():
        sub_val *= v[1] - v[0] +1
    total += sub_val

print(total)