from aoc_utils import *
from collections import defaultdict

test = read_input(2024, 13, filename='test')
inp_ = read_input(2024, 13)

inp = test
#inp = inp_

def parse_inp(inp):
    games = defaultdict(list)

    game = 0
    for line in inp:
        if line == "":
            game += 1
            continue
        if not 'Prize' in line:
            button, inst = line.split(":")
            button = button.split(" ")[1]
            x, y = inst.split(",")
            x = int(x.split("+")[1])
            y = int(y.split("+")[1])
            games[game].extend([x, y])
        else:
            _, inst = line.split(":")
            x, y = inst.split(",")
            x = int(x.split("=")[1])
            y = int(y.split("=")[1])
            games[game].extend([1000000000 + x, 1000000000+ y])
    return games

def factor(n):
    return [i for i in range(1, n) if n % i ==0]

games = parse_inp(inp)
BEST = float('inf')
def play_game(ax, ay, bx, by, px, py):
    global BEST
    seen = set()
    BEST = float('inf')
    def do_turn(ap, bp):
        global BEST
        #print(ap, bp)
        
        if (ap, bp) in seen or ap*3 + bp > BEST:
            return
        
        
        #print(ax*ap + bx*bp, ay*ap + by*bp)
        print(factor(px))
        input()

        if ax*ap + bx*bp > px or ay*ap + by*bp > py:
            return
        
        if ax*ap + bx*bp == px and ay*ap + by*bp == py:
            BEST = ap*3 + bp
            return
        
        seen.add((ap, bp))
        do_turn(ap+1, bp)
        do_turn(ap, bp+1)
    do_turn(0, 0)
    return BEST if BEST < float('inf') else 0

ans = 0
for game in games.values():
    ax, ay, bx, by, px, py = game
    ans += play_game(ax, ay, bx, by, px, py)

print(ans)
