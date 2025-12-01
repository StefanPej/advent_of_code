from aoc_utils import *
from collections import defaultdict

test = read_input(2024, 13, filename='test')
inp_ = read_input(2024, 13)

inp = test
inp = inp_

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
            games[game].extend([x,y])
    return games

games = parse_inp(inp)
BEST = float('inf')
def play_game(game):
    global BEST
    seen = set()
    BEST = float('inf')
    def do_turn(ap, bp):
        global BEST

        if (ap, bp) in seen or ap*3 + bp > BEST or ap > 100 or bp > 100:
            return
        
        ax, ay, bx, by, px, py = game

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
    ans += play_game(game)

print(ans)
