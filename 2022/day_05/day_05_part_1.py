def read_input(day):
    with open(f'2022/input_{day}.txt') as o:
        out = o.readlines()
    return out
input = read_input('05')

stacks = {str(i):[] for i in range(1,10)}

crates = input[:8]
for i in range(len(crates)-1, -1, -1):
    count = 0
    for j in range(1, len(crates[i]), 4):
        count += 1
        if crates[i][j] == ' ':
            continue
        stacks[str(count)].append(crates[i][j])

def parse_line(line):
    split_line = line.split()
    return {'move': int(split_line[1]), 'from':split_line[3], 'to':split_line[5]}

for line in input[10:]:
    inst = parse_line(line)
    for _ in range(inst['move']):
        stacks[inst['to']].append(stacks[inst['from']].pop())

print(''.join(v[-1] for v in stacks.values()))
