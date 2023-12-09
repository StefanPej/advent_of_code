import os
def read_input(day):
    with open(f'2022/input_{day}.txt') as o:
        out = o.readlines()
    return [line.strip() for line in out]