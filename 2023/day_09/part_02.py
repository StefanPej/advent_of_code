with open("./2023/day_09/input.txt", "r") as o:
    input = o.readlines()

input = [line.strip() for line in input]
clean_ins = []
for line in input:
    clean_ins.append([int(num) for num in line.split()])

def get_line_maps(line):
    out = [line]
    current = line
    solving = True
    while solving:
        temp = []
        for i in range(1, len(current)):
            temp.append(current[i]-current[i-1])
        out.append(temp)
        current = temp
        if not any(temp):
            solving = False
    
    return out

def get_next_val(mapping):
    cur_val = 0
    for l in reversed(mapping):
        cur_val = l[0] - cur_val 
    return cur_val

count = 0
for line in clean_ins:
    map = get_line_maps(line)
    val = get_next_val(map)
    count += val

print(count)