from aoc_utils import *
from queue import PriorityQueue
inp = read_input(2023, 17)

# with open('2023/day_17/test.txt') as o:
#     inp = o.readlines()
inp = [list(map(int, line.strip())) for line in inp]
print(inp)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRS = [UP, DOWN, LEFT, RIGHT]

def check_oob(location, inp):
    if not (0 <= location[0] < len(inp)) or not (0 <= location[1] < len(inp[0])):
        return True
    return False
    
def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])
    
class Traveller:
    def __init__(self, location, direction, moves_same_dir, seen, cost):
        self.location = location
        self.direction = direction
        self.moves_same_dir = moves_same_dir
        self.seen = seen
        self.cost = cost

    def find_good_moves(self):
        ret = []
        if self.moves_same_dir < 4:
            new_loc = (add_tuples(self.location, self.direction), self.direction, self.moves_same_dir+1)
            if not check_oob(new_loc[0], inp) and not new_loc[0] in self.seen:
                return [new_loc]
            return []
        for direc in DIRS:
            if direc == self.direction and self.moves_same_dir < 10:
                new_loc = (add_tuples(self.location, direc), direc, self.moves_same_dir+1)
            elif direc != self.direction:
                new_loc = (add_tuples(self.location, direc), direc, 1)
            else:
                continue
            if not check_oob(new_loc[0], inp) and not new_loc[0] in self.seen:
                ret.append(new_loc)
        return ret
    
    def __repr__(self):
        out = f"""
            LOC: {self.location}
            DIR: {self.direction}
            MOVES: {self.moves_same_dir}
            SEEN: {self.seen}
            COST: {self.cost}
            """
        return out
    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __ne__(self, other):
        return self.cost != other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self.cost >= other.cost



x = Traveller((0,0), DOWN, 0, set([(0,0)]), 0)
y = Traveller((0,0), RIGHT, 0, set([(0,0)]), 0)
travellers = PriorityQueue()
travellers.put(x)
travellers.put(y)

ans = 100000
all_seen = {}
while not travellers.empty():
    traveller = travellers.get()
    # print(traveller)
    # input()
    key = (traveller.location, traveller.direction, traveller.moves_same_dir)
    #print(key)
    #input()
    if all_seen.get(key, 999999) <= traveller.cost:
        continue
    all_seen[key] = traveller.cost
    if traveller.cost >= ans:
        #print(traveller.cost)
        continue
    if traveller.location == (len(inp)-1, len(inp[0])-1):
        ans = min(ans, traveller.cost)
        print(ans)
        continue
    next_moves = traveller.find_good_moves()
    for move in next_moves:
        travellers.put(Traveller(move[0], move[1], move[2], traveller.seen.union(tuple([move[0]])), traveller.cost + inp[move[0][0]][move[0][1]]))

    #print(len(travellers))

print(ans)