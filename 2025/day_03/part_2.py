from aoc_utils import *

t = """987654321111111
811111111111119
234234234234278
818181911112111"""
t = t.split("\n")

inp = read_input(2025, 3)

count = 0

for line in inp:
    val = ""
    last_ind = -1

    for i in range(12, 0, -1):
        ind = len(line) - i
        current_ind = ind
        while ind > last_ind + 1:
            new_ind = ind - 1

            if line[new_ind] >= line[current_ind]:
                current_ind = new_ind
            ind = new_ind
        last_ind = current_ind
        val += line[current_ind]

    count += int(val)


print(count)