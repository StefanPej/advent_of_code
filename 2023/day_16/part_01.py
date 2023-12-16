from aoc_utils import *
import os
from termcolor import colored
inp = read_input(2023, 16)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

#print(colored('gello', 'red'))

class Beam:
    def __init__(self, direction, location):
        self.direction = direction
        self.location = location
        self.travelled = set()
    def travel(self):
        self.location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        if not (0 <= self.location[0] < len(inp)) or not (0 <= self.location[1] < len(inp[0])):
            self.location = 0

def print_grid(grid, energised):
    out_str = ''
    for i , line in enumerate(grid):
        for j, char in enumerate(line):
            if (i, j) in energised:
                out_str += colored(char, 'red')
            else:
                out_str += char
        out_str += '\n'

    print(out_str)

    
beams = [Beam(RIGHT, (0,-1))]
energised = set()

while len(beams) > 0:
    for i, beam in enumerate(beams):
        beam.travel()
        travel_append = (beam.location, beam.direction)
        if beam.location == 0 or travel_append in energised:
            beams.pop(i)
            continue
        energised.add(travel_append)
        
        tile = inp[beam.location[0]][beam.location[1]]
        if beam.direction == RIGHT and tile == '\\':
            beam.direction = DOWN
        elif beam.direction == LEFT and tile == '\\':
            beam.direction = UP
        elif beam.direction == DOWN and tile == '\\':
            beam.direction = RIGHT
        elif beam.direction == UP and tile == '\\':
            beam.direction = LEFT
        elif beam.direction == RIGHT and tile == '/':
            beam.direction = UP
        elif beam.direction == LEFT and tile == '/':
            beam.direction = DOWN
        elif beam.direction == DOWN and tile == '/':
            beam.direction = LEFT
        elif beam.direction == UP and tile == '/':
            beam.direction = RIGHT
        elif beam.direction in [RIGHT, LEFT] and tile == '|':
            beams.pop(i)
            beams.append(Beam(UP, beam.location))
            beams.append(Beam(DOWN, beam.location))
        elif beam.direction in [UP, DOWN] and tile == '-':
            beams.pop(i)
            beams.append(Beam(LEFT, beam.location))
            beams.append(Beam(RIGHT, beam.location))

        
        os.system('cls')
        print_grid(inp, set(item[0] for item in energised))
        #input()
            


energised_unique = set(item[0] for item in energised)
print(len(energised_unique))

