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

def brutus(range_tuple):
    min_, max_ = range_tuple


    total = 0
    for i in range(min_,max_):
        for j in range(min_,max_):
            for k in range(min_,max_):
                for l in range(min_,max_):
                    part = {'x':i, 'm':j, 'a':k, 's':l}
                    inst = 'in'
                    while inst not in 'RA':
                        instructions = workflows[inst]
                        for ins in instructions:
                            inst = run_instruction(part, ins)
                            if inst:
                                break
                    if inst == 'A':
                        total += 1
                        #print(total)
    return total

# def brutus2(range_tuple):
#     min_, max_ = range_tuple


#     total = 0
#     for i in range(0,2):
#         for j in range(0,2):
#             for k in range(0,2):
#                 for l in range(0,4001):
#                     part = {'x':i, 'm':j, 'a':k, 's':l}
#                     inst = 'in'
#                     while inst not in 'RA':
#                         instructions = workflows[inst]
#                         for ins in instructions:
#                             inst = run_instruction(part, ins)
#                             if inst:
#                                 break
#                     if inst == 'A':
#                         total += 1
#     return total

from multiprocessing import Pool
if __name__ == '__main__':
    NUM_PROCS = 5
    pool = Pool(NUM_PROCS)
    ranges = [(1,800), (800, 1600), (1600,2400), (2400,3200), (3200,4001)]
    rets = []
    for res in pool.map(brutus, ranges):
        rets.append(res)
    print(rets)
    print(sum(rets))


    