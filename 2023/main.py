def get_line(line):
    for char in line:
        if char.isdigit():
            first_num = str(char)
            break
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            last_num = str(line[i])
            break
    return int(first_num+last_num)

with open("inputs.txt", "r") as o:
    inputs = o.readlines()

count = 0
for line in inputs:
    count += get_line(line)

print(count)