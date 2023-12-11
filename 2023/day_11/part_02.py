with open("./2023/day_11/input.txt", "r") as o:
    input = o.readlines()
    
from itertools import combinations

input = [line.strip() for line in input]
#print(len(input))

def add_stars(input):        
    galaxies = []
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i,j))
    gals = [gal[1] for gal in galaxies]
    
    cols_add = []
    for i in range(len(input[0])):
        if i not in gals:
            cols_add.append(i)
            
    gals = [gal[0] for gal in galaxies]
    line_add = []
    for i in range(len(input)):
        if i not in gals:
            line_add.append(i)
    
    return cols_add, line_add, galaxies


cols_added, vert_added, galaxies = add_stars(input)  

pairs = []
for pair in combinations(galaxies, 2):
    pairs.append(pair)
    
#print(len(pairs))
def get_dist(one, two, cols_add, line_add):

    x_diff = abs(one[0]-two[0])
    y_diff = abs(one[1]-two[1])
    x_min = min(one[0],two[0])
    x_max = max(one[0],two[0])
    y_min = min(one[1],two[1])
    y_max = max(one[1],two[1])

    crossed = 0
    for i in range(x_min, x_max):
        if i in line_add:
            crossed += 1
    for j in range(y_min, y_max):
        if j in cols_add:
            crossed += 1
    return x_diff + y_diff + crossed*999999

count = 0
for pair in pairs:
    count += get_dist(pair[0], pair[1], cols_added, vert_added)
print(count)
