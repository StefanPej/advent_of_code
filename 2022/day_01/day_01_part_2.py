from utils2022 import read_input
from collections import defaultdict

input = read_input("01")

calories = defaultdict(list)

counter = 1
for line in input:
    if line == '\n' or not line:
        counter += 1
        continue
    calories[str(counter)].append(int(line))

cals = [sum(val) for val in calories.values()]
print(sum(sorted(cals)[-3:]))