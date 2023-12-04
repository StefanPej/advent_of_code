with open("./2023/day_04/input.txt", "r") as o:
    input = o.readlines()

def split_line(line):
    games = line.split(':')[1]
    wins, mine = games.split('|')
    wins = wins.split()
    mine = mine.split()
    return (wins, mine)

def get_value(game):
    winners = 0
    for number in game[1]:
        if number in game[0]:
            winners += 1
    if not winners:
        return 0
    return 2**(winners-1)

total = 0
for line in input:
    game = split_line(line)
    total += get_value(game)
print(total)