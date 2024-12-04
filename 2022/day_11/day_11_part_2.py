from math import floor
from aoc_utils import *
monkey_dict = {}

class Monkey:
    def __init__(self, number, items, test_divisor, test_true_to, test_false_to):
        self.number = number
        self.items = items
        self.inspected = 0
        self.test_divisor = test_divisor
        self.test_true_to = test_true_to
        self.test_false_to = test_false_to
    
    def operation(self, item):
        if self.number == 0:
            return item * 13
        if self.number == 1:
            return item + 3
        if self.number == 2:
            return item * item
        if self.number == 3:
            return item + 5
        if self.number == 4:
            return item + 7
        if self.number == 5:
            return item + 4
        if self.number == 6:
            return item * 19
        if self.number == 7:
            return item + 2
        
    def throw(self, item):
        if item % self.test_divisor == 0:
            return self.test_true_to
        return self.test_false_to
        
    def get_bored(self, item):
        return floor(item/3)
    
    def play(self):
        while len(self.items) > 0:
            self.inspected += 1
            item = self.items.pop(0)
            item = self.operation(item)
            #item = self.get_bored(item)
            monkey_dict[self.throw(item)].items.append(item)

with open("./2022/day_11/test.txt") as f:
    inp = f.read()

inp = inp.split("\n\n")
    
for monkey in inp:
    line = monkey.split('\n')
    line = [inst.strip() for inst in line]
    monkey_num = int(line[0].split()[1].strip(":"))
    starting_items = [int(num.strip(",")) for num in line[1].split()[2:]]
    test_divisor = int(line[3].split()[-1])
    if_true = int(line[4].split()[-1])
    if_false = int(line[5].split()[-1])

    monkey_dict[monkey_num] = Monkey(monkey_num, starting_items, test_divisor, if_true, if_false)

starting_list = [monkey.items.copy() for _, monkey in monkey_dict.items()]

for i in range(10000):
    for _, monkey in monkey_dict.items():
        monkey.play()
    current_items = [monkey.items for _, monkey in monkey_dict.items()]
    if current_items == starting_list:
        print(i)
        input() 

inspected = [monkey.inspected for _, monkey in monkey_dict.items()]
inspected = sorted(inspected)
ans = inspected[-1]*inspected[-2]
print(ans)
