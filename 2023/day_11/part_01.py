with open("./2023/day_11/input.txt", "r") as o:
    input = o.readlines()
    
from itertools import combinations

input = [line.strip() for line in input]
print(len(input))

def add_stars(input):
    to_add = []
    line_len = len(input[0])
    for i, line in enumerate(input):
        #print(set(line))
        if set(line) == {'.'}:
            to_add.append(i)
    for add in reversed(to_add):
        input.insert(add, '.'*line_len)
        
    galaxies = []
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i,j))
    gals = [gal[1] for gal in galaxies]
    
    cols_add = []
    for i in range(line_len):
        if i not in gals:
            cols_add.append(i)
    
    new_in = []
    for i in range(len(input)):
        new_ln = ''
        for j in range(line_len):
            if j not in cols_add:
                new_ln += input[i][j]
            else:
                new_ln += '..'
        new_in.append(new_ln)
    return new_in


input = add_stars(input)   
galaxies = []
for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == '#':
            galaxies.append((i,j))
            
print(len(galaxies))

pairs = []
for pair in combinations(galaxies, 2):
    pairs.append(pair)
print(len(pairs))
    
def get_dist(one, two):

    x_diff = abs(one[0]-two[0])
    y_diff = abs(one[1]-two[1])
    return x_diff + y_diff

count = 0
for pair in pairs:

    count += get_dist(pair[0], pair[1])
print(count)
