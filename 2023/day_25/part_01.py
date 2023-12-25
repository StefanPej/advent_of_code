from aoc_utils import *
from collections import defaultdict

inp = read_input(2023, 25)
# with open('2023/day_25/test.txt') as o:
#     inp = o.readlines()
# inp = [line.strip() for line in inp]


def parse_inp(line):
    source, dests = line.split(":")
    return source, dests.split()

class Graph:
    def __init__(self):
        self.nodes = set()
        self.connections = defaultdict(list)
        self.size = 0
        
    def add_connection(self, node1, node2):
        self.connections[node1].append(node2)
        self.connections[node2].append(node1)
        self.nodes.add(node1)
        self.nodes.add(node2)
        self.size = len(self.nodes)
        
    def find_amt_nodes(self, node):
        seen = set()
        nodes_to_check = [node]
        
        while nodes_to_check:
            checking = nodes_to_check.pop()
            seen.add(checking)
            for child in self.connections[checking]:
                if child not in seen:
                    nodes_to_check.append(child)
                    
        return len(seen)
        
    def __repr__(self) -> str:
        [print(f'{node}: {connections}') for node, connections in self.connections.items()]
        return f"{self.size} nodes"

graph = Graph()
for line in inp:
    source, dests = parse_inp(line)
    for dest in dests:
        graph.add_connection(source, dest)

cypher = "n1,n2\n"
for line in inp:
    source, dests = parse_inp(line)
    for dest in dests:
        cypher += f"{source},{dest}\n"
        
with open('2023/day_25/conns.csv', 'w') as o:
    o.write(cypher)

# LOL IMPORT TO NEO4J

with open('2023/day_25/distinct.csv') as o:
    distinct = o.readlines()
distinct = [line.strip() for line in distinct]


g2 = Graph()
for line in distinct[1:]:
    n1, n2 = line.split(',')
    g2.add_connection(n1, n2)
    
print(g2.find_amt_nodes('hln') * (g2.size - g2.find_amt_nodes('hln')))