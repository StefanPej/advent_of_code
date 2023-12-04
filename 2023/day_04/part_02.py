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
    return winners

cards = {str(j):1 for j in range(1,199)}
for i, line in enumerate(input, start=1):
    game = split_line(line)
    winners = get_value(game)
    print(winners)
    
    for k in range(i+1, i+winners+1):
        cards[str(k)] += cards[str(i)]

print(cards)
print(sum(list(cards.values())))