from aoc_utils import *

inp = read_input(2023, 16)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Beam:
    def __init__(self, direction, location):
        self.direction = direction
        self.location = location
        self.travelled = set()
    def travel(self):
        self.location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        if self.location[0] >= len(inp) or self.location[0] < 0 or self.location[1] < 0 or self.location[1] >= len(inp[0]):
            self.location = 0
        return self.location
    
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


energised_unique = set(item[0] for item in energised)
print(len(energised_unique))
