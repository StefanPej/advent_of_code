with open("./2023/day_10/input.txt", "r") as o:
    input = o.readlines()

class Pipe:
    def __init__(self, coords, letter):
        self.letter = letter
        self.coords = coords
        self.connect_to = []
        return
    def add_connector(self, coord):
        if coord[0] < 1 or coord[0] > 140 or coord[1] < 1 or coord[1] > 140:
            return
        self.connect_to.append(coord)
    def next_step(self, enter_direction):
        if self.letter == '|':
            if enter_direction == 't':
                return (self.coords[0]+1, self.coords[1]), 't'
            if enter_direction == 'b':
                return (self.coords[0]-1, self.coords[1]), 'b'
        if self.letter == '-':
            if enter_direction == 'l':
                return (self.coords[0], self.coords[1]+1), 'l'
            if enter_direction == 'r':
                return (self.coords[0], self.coords[1]-1), 'r'
        if self.letter == 'L':
            if enter_direction == 't':
                return (self.coords[0], self.coords[1]+1), 'l'
            if enter_direction == 'r':
                return (self.coords[0]-1, self.coords[1]), 'b'
        if self.letter == 'J':
            if enter_direction == 't':
                return (self.coords[0], self.coords[1]-1), 'r'
            if enter_direction == 'l':
                return (self.coords[0]-1, self.coords[1]), 'b'
        if self.letter == '7':
            if enter_direction == 'l':
                return (self.coords[0]+1, self.coords[1]), 't'
            if enter_direction == 'b':
                return (self.coords[0], self.coords[1]-1), 'r'
        if self.letter == 'F':
            if enter_direction == 'r':
                return (self.coords[0]+1, self.coords[1]), 't'
            if enter_direction == 'b':
                return (self.coords[0], self.coords[1]+1), 'l'
        if self.letter == 'S':
            if enter_direction == 'l':
                return (self.coords[0]-1, self.coords[1]), 'b'
            if enter_direction == 't':
                return (self.coords[0], self.coords[1]-1), 'r'

    def __repr__(self):
        return f'LETTER: {self.letter}, COORD: {self.coords}, CONNECTED: {self.connect_to}'

pipes = {} 
for i, line in enumerate(input, start=1):
    for j, pipe in enumerate(line, start=1):
        if pipe != '.':
            pipe_obj = Pipe((i, j), pipe)
            if pipe == '|':
                pipe_obj.add_connector((i-1, j))
                pipe_obj.add_connector((i+1, j))
            elif pipe == '-':
                pipe_obj.add_connector((i, j-1))
                pipe_obj.add_connector((i, j+1))
            elif pipe == 'L':
                pipe_obj.add_connector((i-1, j))
                pipe_obj.add_connector((i, j+1))
            elif pipe == 'J':
                pipe_obj.add_connector((i-1, j))
                pipe_obj.add_connector((i, j-1))
            elif pipe == '7':
                pipe_obj.add_connector((i, j-1))
                pipe_obj.add_connector((i+1, j))
            elif pipe == 'F':
                pipe_obj.add_connector((i, j+1))
                pipe_obj.add_connector((i+1, j))
            elif pipe == 'S':
                pipe_obj = Pipe((i, j), 'J')
                pipe_obj.add_connector((i, j-1))
                pipe_obj.add_connector((i-1, j))
                s_pipe = pipe_obj
            pipes[str((i,j))] = pipe_obj

loop = []
current_pipe = s_pipe
enter_dir = 't'
while True:
    loop.append(current_pipe)
    next_step, enter_dir = current_pipe.next_step(enter_dir)
    current_pipe = pipes[str(next_step)]
    if current_pipe.coords == s_pipe.coords:
        break


print(len(loop)/2)


# Re save the grid without all the junk in prep for p2
def output_grid(loop):
    grid = []
    for _ in range(len(input)):
        temp = []
        for _ in range(len(input[0])):
            temp.append('I')
        grid.append(temp)

    for pipe in loop:
        grid[pipe.coords[0]][pipe.coords[1]] = pipe.letter

    out = ''
    for line in grid:
        temp = ''
        for letter in line:
            temp += letter
        temp += '\n'
        out += temp


    with open("./2023/day_10/grid.txt", "w+") as o:
        o.write(out)
    return grid

output_grid(loop)

