with open("./2023/day_08/input.txt", "r") as o:
    input = o.readlines()

instructions = [char for char in input[0].strip()]

inst_map = {'L': 'left', 'R': 'right'}

nodes_raw = input[2:]
nodes = {}
for line in nodes_raw:
    line = line.strip()
    node = line.split()[0]
    left, right = line.split()[2].replace('(', '').replace(',',''), line.split()[3].replace(')', '').replace(',','')
    nodes[node] = {'left': left, 'right':right}

current_pos = 'AAA'
count = 0
inst_count = 0
while True:
    inst = instructions[inst_count]
    current_pos = nodes[current_pos][inst_map[inst]]
    count += 1
    inst_count += 1
    if current_pos == 'ZZZ':
        break
    inst_count = inst_count % len(instructions)

print(count)

