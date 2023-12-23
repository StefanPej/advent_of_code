from aoc_utils import *

inp = read_input(2022, 7, filename='input')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
    
    def get_parent(self):
        if self.parent:
            return self.parent
        return self
    
    def add_child(self, child):
        self.children.append(child)

    def find_child(self, child_name):
        return [child for child in self.children if type(child) != tuple and child.name == child_name][0]

    def get_full_filepath(self):
        if self.name == '/':
            return ""
        return self.parent.get_full_filepath() + '/' + self.name

    def get_size(self):
        size = 0
        for child in self.children:
            if type(child) == tuple:
                size += child[1]
            else:
                size += child.get_size()
        return size
    
    def __repr__(self):
        return f"Name: {self.name}, parent: {self.parent}"

def parse_line(line):
    line_s = line.split()
    if line_s[0] == '$':
        if 'cd' in line_s:
            return 'cd', line_s[2]
        elif 'ls' in line_s:
            return 'ls', None
    elif line_s[0] == 'dir':
        return 'dir', line_s[1]
    else:
        return int(line_s[0]), line_s[1]

root = Directory('/', None)

directories = {'/':root}
curr_dir = root

for line in inp:
    cmd, arg = parse_line(line)
    if cmd == 'cd':
        if arg == '..':
            curr_dir = curr_dir.get_parent()
        elif arg == '/':
            curr_dir = root
        else:
            curr_dir = curr_dir.find_child(arg)
    if cmd == 'dir':
        new_dir = Directory(arg, curr_dir)
        curr_dir.add_child(new_dir)
        directories[new_dir.get_full_filepath()] = new_dir
    if type(cmd) == int:
        curr_dir.add_child((arg, cmd))


print(sum([dir.get_size() for dir in directories.values() if dir.get_size() <= 100000]))
