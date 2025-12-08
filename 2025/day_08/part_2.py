from aoc_utils import *
from collections import defaultdict

inp = read_input(2025, 8)
test = read_input(2025, 8, filename='test')
inp = [tuple(map(int, line.split(","))) for line in inp]

distances = []

for i in range(len(inp)-1):
    for j in range(i+1, len(inp)):
        ix, iy, iz = inp[i]
        jx, jy, jz = inp[j]

        distance = ((ix-jx)**2 + (iy-jy)**2 + (iz-jz)**2)**(1/2)
        distances.append((distance, inp[i], inp[j]))

distances = order_list(distances, 0, True)

count = 0
links = []

while distances:
    do_nothing = False
    _, x, y = distances.pop()

    member_links = []
    for i, link in enumerate(links):
        if x in link and y in link:
            do_nothing = True
            count += 1
            break
        if x in link:
            member_links.append(i)
        if y in link:
            member_links.append(i)

    if not member_links and not do_nothing:
        links.append(set([x, y]))
        count += 1

    if len(member_links) == 1 and not do_nothing:
        links[member_links[0]].add(x)
        links[member_links[0]].add(y)
        count += 1
    
    if len(member_links) == 2 and not do_nothing:
        new_group = links[member_links[0]].union(links[member_links[1]])
        for member in sorted(member_links, reverse=True):
            links.pop(member)
        links.append(new_group)
        count += 1

    if len(links) == 1 and len(links[0]) == 1000:
        print(x[0] * y[0])
        break