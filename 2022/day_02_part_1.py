from utils2022 import read_input

input = read_input('02')

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'w': 6,
    'd': 3,
    'l': 0
}

def is_winner(opponent, me):
    if opponent == 'A':
        if me == 'X':
            return 'd'
        if me == 'Y':
            return 'w'
        if me == 'Z':
            return 'l'
    if opponent == 'B':
        if me == 'X':
            return 'l'
        if me == 'Y':
            return 'd'
        if me == 'Z':
            return 'w'
    if opponent == 'C':
        if me == 'X':
            return 'w'
        if me == 'Y':
            return 'l'
        if me == 'Z':
            return 'd'

def get_game_score(game):
    opponent, me  = game.split()
    return points[me] + points[is_winner(opponent, me)]

count = 0
for line in input:
    count += get_game_score(line)

print(count)

