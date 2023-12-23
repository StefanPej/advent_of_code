from utils2022 import read_input

input = read_input('02')

points = {
    'X': 0,
    'Y': 3,
    'Z': 6,
    'R': 1,
    'P': 2,
    'S': 3
}

def get_me(opponent, victory):
    if opponent == 'A':
        if victory == 'X':
            return 'S'
        if victory == 'Y':
            return 'R'
        if victory == 'Z':
            return 'P'
    if opponent == 'B':
        if victory == 'X':
            return 'R'
        if victory == 'Y':
            return 'P'
        if victory == 'Z':
            return 'S'
    if opponent == 'C':
        if victory == 'X':
            return 'P'
        if victory == 'Y':
            return 'S'
        if victory == 'Z':
            return 'R'

def get_game_score(game):
    opponent, me  = game.split()
    return points[me] + points[get_me(opponent, me)]

count = 0
for line in input:
    count += get_game_score(line)

print(count)

