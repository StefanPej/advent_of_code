with open('2023/day_10/grid.txt') as o:
    grid = o.readlines()

# General logic is to blow everything character from grid into
# a 3x3. This means we can now easily see the parts where the
# little rat boy can slip between pipes

# Blow everything up into a 3x3 cell
exploded_icons = {
    '|': ('.|.','.|.','.|.'),
    '-': ('...', '---', '...'),
    'L': ('.|.','.--','...'),
    'J': ('.|.', '--.', '...'),
    '7': ('...','--.','.|.'),
    'F': ('...', '.--', '.|.'),
    'I': ('III','III','III'),
}

# Make the big boy
big_boy = []
for i, line in enumerate(grid):
    first = []
    second = []
    third = []
    for letter in line:
        if letter != '\n':
            top, mid, bot = exploded_icons[letter]
            f1, f2, f3 = top
            m1, m2, m3 = mid
            b1, b2, b3 = bot
            first.append(f1)
            first.append(f2)
            first.append(f3)
            second.append(m1)
            second.append(m2)
            second.append(m3)
            third.append(b1)
            third.append(b2)
            third.append(b3)
    big_boy.append(first)
    big_boy.append(second)
    big_boy.append(third)

# Get the index of all 'I' and '.'
I = []
for i, line in enumerate(big_boy, start=1):
    for j, letter in enumerate(line, start=1):
        if letter == 'I' or letter == '.':
            I.append((i,j))

# Checks if given coords are adjacent to a safe node
# If yes, append coord to the safe set, since it's now safe too
def is_adjacent(coords, safe_set):
    adjs = [(coords[0]-1, coords[1]), (coords[0]+1, coords[1]),(coords[0], coords[1]-1),(coords[0], coords[1]+1)]
    for adj in adjs:
        if adj in safe_set:
            safe_set.add(coords)
            return True, safe_set
    return False, safe_set

# Basic idea is that we start with one 'safe' node that we KNOW isn't trapped
# We then add all the other nodes around it, since they aren't trapped either
# This proliferates along all 'I's in the grid, and all the '.'s, since
# we know that the rat can scurry along those (they represent the gaps between pipes)
# This shit isn't efficient at all, but it works
safe = {(0,1)}
current_len = len(I)
searching = True
while searching:
    for i in I:
        is_adj, safe = is_adjacent(i, safe)
        if is_adj:
            I.pop(I.index(i))
    new_len = len(I)
    if new_len == current_len:
        searching = False
    current_len = new_len

# Count all the I's left over and divide by 9 since we made them into a 3x3 before
count = 0
for item in I:
    if big_boy[item[0]][item[1]] == 'I':
        count += 1
print(count/9)

