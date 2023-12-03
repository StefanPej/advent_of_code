import regex as re

with open("input.txt", "r") as o:
    input = o.readlines()

input = [line.replace('\n','').strip() for line in input]

spec_indices = {}
nums = []

num_indexes = []
for i, line in enumerate(input):
    matches = re.finditer(f'\d+', input[i])
    for match in matches:
        num_indexes.append((match.group(0), i, (match.start()), len(match.group(0))))

    #print(re.findall(r'\d+', line))
    for j, char in enumerate(line):
        if char != '.' and not char.isdigit():
            if not spec_indices.get(char):
                spec_indices[char] = [(i,j)]
            else:
                spec_indices[char].append((i,j))


num_uniq = []
for num in num_indexes:
    if num not in num_uniq:
        num_uniq.append(num)

#print(num_indexes)
#print(spec_indices)


def make_search_grid(num_index):
    search_grid = []
    search_range = [-1, 0, 1]
    for increm in search_range:
        search_grid.append((num_index[1] + increm, num_index[2]-1))
        search_grid.append((num_index[1] + increm, num_index[2]))
        for i in range(num_index[3]):
            search_grid.append((num_index[1] + increm, num_index[2]+1+i))
    
    return search_grid

def is_good_num(search_grid, spec_indices):
    for search in search_grid:
        for char, index in spec_indices.items():
            if search in index:
                return True, search, char

#print(make_search_grid(num_indexes[0]))
gears = {}
for num in num_uniq:
    #print(num)
    search_grid = make_search_grid(num)
    #print(search_grid)
    #print(num[0], num[1], num[2],search_grid)
    good = is_good_num(search_grid, spec_indices)
    if good:
        if good[2] == "*":
            if gears.get(str(good[1])):
                gears.get(str(good[1])).append(int(num[0]))
            else:
                gears[str(good[1])] = [int(num[0])]

total = 0
for v in gears.values():
    if len(v) == 2:
        total += v[0] * v[1]


print(total)

#print(spec_indices)
