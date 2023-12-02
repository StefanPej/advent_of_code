with open("input.txt", "r") as o:
    inputs = o.readlines()

max_cubes = {'red': 12,
             'green': 13,
             'blue': 14}

def get_game_no(line):
    return int(line.split(':')[0].split(" ")[1])

def get_cube_showing(line):
    showings = line.split(':')[1].split(';')
    game_max = {'red': 0,
             'green': 0,
             'blue': 0}
    for showing in showings:
        dice_shown = showing.split(',')
        for dice in dice_shown:
            num, colour = dice.strip().split(' ')
            game_max[colour] = max(game_max[colour], int(num))

    for k, v in game_max.items():
        if game_max[k] > max_cubes[k]:
            return 0

    return get_game_no(line)
    
total = 0
for line in inputs:
    total += get_cube_showing(line)

print(total)

