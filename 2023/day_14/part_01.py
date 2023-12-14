from aoc_utils import *

inp = read_input(2023, 14)

def cha_cha_slide(row):
    row = list(row)
    for i in range(len(row)):
        if row[i] == 'O':
            current_pos = i
            next_pos = i-1
            while current_pos > 0 and next_pos > -1:
                if row[next_pos] in ['0', '#']:
                    break
                row[current_pos], row[next_pos] = row[next_pos], row[current_pos]
                current_pos -= 1
                next_pos -= 1
    return row

north_rocks = []
for row in transpose(inp):
    north_rocks.append(cha_cha_slide(row))   
north_rocks = transpose(north_rocks)

total = 0
for i, row in enumerate(north_rocks):
    for char in row:
        if char == 'O':
            total += len(north_rocks) - i
            
print(total)