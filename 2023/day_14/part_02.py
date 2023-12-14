from aoc_utils import *

inp = read_input(2023, 14)

def cha_cha_slide(row, reverse=False):
    row = list(row)
    if not reverse:
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
    else:
        for i in range(len(row)-1, -1, -1):
            if row[i] == 'O':
                current_pos = i
                next_pos = i+1
                while current_pos <len(row)-1 and next_pos < len(row):
                    if row[next_pos] in ['0', '#']:
                        break
                    row[current_pos], row[next_pos] = row[next_pos], row[current_pos]
                    current_pos += 1
                    next_pos += 1
        
    return row

def run_cycle(inp):
    north_rocks = []
    for row in transpose(inp):
        north_rocks.append(cha_cha_slide(row))
    north_rocks = transpose(north_rocks)
    
    west_rocks = []
    for row in north_rocks:
        west_rocks.append(cha_cha_slide(row))
        
    south_rocks = []
    for row in transpose(west_rocks):
        south_rocks.append(cha_cha_slide(row, True))
    south_rocks = transpose(south_rocks)
        
    east_rocks = []
    for row in south_rocks:
        east_rocks.append(cha_cha_slide(row, True))
        
    return east_rocks
        
    
rocks = inp
for _ in range(1000): # WHAT A DIVINE COINCIDENCE LMAO
    rocks = run_cycle(rocks)
    
total = 0
for i, row in enumerate(rocks):
    for char in row:
        if char == 'O':
            total += len(rocks) - i
            
print(total)