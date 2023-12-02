from math import prod


def get_game_no(game):
    return int(game.split(":")[0].split(" ")[1])


def get_game_showings(game):
    return game.split(":")[1].split(";")


def break_down_game(showings):
    game_breakdown = []
    for showing in showings:
        dice_shown = {}
        dice = showing.split(",")
        for die in dice:
            num, colour = die.strip().split(" ")
            dice_shown[colour] = int(num)
        game_breakdown.append(dice_shown)
    return game_breakdown


def solve_part_1(games):
    def check_valid_game(game):
        available_cubes = {"red": 12, "green": 13, "blue": 14}
        showings = get_game_showings(game)
        breakdown = break_down_game(showings)
        for showing in breakdown:
            for colour, num in showing.items():
                if available_cubes[colour] < num:
                    return 0
        return 1

    return sum([get_game_no(game) * check_valid_game(game) for game in games])


def solve_part_2(games):
    answer = 0
    for game in games:
        game_max = {"red": 0, "green": 0, "blue": 0}
        showings = get_game_showings(game)
        breakdown = break_down_game(showings)
        for showing in breakdown:
            for colour, num in showing.items():
                game_max[colour] = max(game_max[colour], num)
        answer += prod(game_max.values())
    return answer


with open("input.txt", "r") as o:
    games = o.readlines()

print(f"Part 1: {solve_part_1(games)}")
print(f"Part 2: {solve_part_2(games)}")
