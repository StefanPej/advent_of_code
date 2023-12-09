from utils2022 import read_input

input = read_input('04')

def check_subset(line):
    one, two = line.split(',')
    one_min, one_max = one.split('-')
    two_min, two_max = two.split('-')

    one = set(list(range(int(one_min), int(one_max)+1)))
    two = set(list(range(int(two_min), int(two_max)+1)))

    if one.issubset(two) or two.issubset(one):
        return 1
    
    return 0

counter = 0
for line in input:
    counter += check_subset(line)

print(counter)