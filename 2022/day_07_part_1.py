from utils2022 import read_input

input = read_input('07')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
    
    def get_parent(self):
        if self.parent:
            return self.parent
        return self

root = Directory('root', None)
test = Directory('test', root)

cur = test
print(cur.name)
cur = test.get_parent()
print(cur.name)
cur = test.get_parent()
print(cur.name)