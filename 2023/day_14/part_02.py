from aoc_utils import *

inp = read_input(2023, 14)

def cha_cha_slide(row, reverse_row=False):
    row = list(reversed(row)) if reverse_row else list(row)
    
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

    return list(reversed(row)) if reverse_row else row

def run_cycle(inp):
    instructions = [(True, False), (False, False), (True, True), (False, True)]

    for transpose_grid, reverse_row in instructions:
        inp = transpose(inp) if transpose_grid else inp
        rocks = []
        for row in inp:
            rocks.append(cha_cha_slide(row, reverse_row))
        rocks = transpose(rocks) if transpose_grid else rocks
        inp = rocks
        
    return inp
        
    
rocks = inp
for _ in range(1000): # WHAT A DIVINE COINCIDENCE LMAO
    rocks = run_cycle(rocks)
    
total = 0
for i, row in enumerate(rocks):
    for char in row:
        if char == 'O':
            total += len(rocks) - i
            
print(total)