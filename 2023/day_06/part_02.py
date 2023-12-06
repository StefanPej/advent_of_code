with open("./2023/day_06/input.txt", "r") as o:
    input = o.readlines()

times = input[0].split()[1:]
times = int("".join(time for time in times))
dists = input[1].split()[1:]
dists = int("".join(dist for dist in dists))


def how_many_ways_to_win(time, dist):
    ret = 0
    for hold in range(time):
        time_left = time-hold
        if time_left*hold > dist:
            ret += 1
    return ret

print(how_many_ways_to_win(times, dists))