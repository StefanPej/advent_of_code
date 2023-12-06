with open("./2023/day_05/input.txt", "r") as o:
    input = o.readlines()

seeds_pairs = input[0].strip().split()[1:]
seeds = []
for i in range(0,len(seeds_pairs), 2):
    seeds.append(range(int(seeds_pairs[i]), int(seeds_pairs[i+1])))

def location_to_seed(location):
    seed_map = {str(location):{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':str(location)}}
    maps_mes = input[2:]
    maps = {}
    for line in maps_mes:
        line = line.strip()
        #print(line)
        if len(line.split() )== 2:
            current_map = line.split()[0]
            maps[current_map] = []
        else:
            if line == '':
                continue
            maps[current_map].append(line)

    def find_mapping(number, map):
        for line in map:
            source, dest, ranges = line.split()
            dest, source, ranges, number = int(dest), int(source), int(ranges), int(number)
            max_source = source + ranges
            if number in range(source, max_source):
                #print(f'SEED {number} is in range {source} - {max_source}. RETURNING  {str(dest + (number - source))}')
                return str(dest + (number - source))
        #print(f'SEED NOT FOUND')
        return str(number)
                
                
    #print(maps['temperature-to-humidity'])
    for seed in seed_map:
        seed_map[seed]['humid'] = find_mapping(seed_map[seed]['loc'], maps['humidity-to-location'])
        seed_map[seed]['temp'] = find_mapping(seed_map[seed]['humid'], maps['temperature-to-humidity'])
        seed_map[seed]['light'] = find_mapping(seed_map[seed]['temp'], maps['light-to-temperature'])
        seed_map[seed]['water'] = find_mapping(seed_map[seed]['light'], maps['water-to-light'])
        seed_map[seed]['fert'] = find_mapping(seed_map[seed]['water'], maps['fertilizer-to-water'])
        seed_map[seed]['soil'] = find_mapping(seed_map[seed]['fert'], maps['soil-to-fertilizer'])
        seed_map[seed]['seed'] = find_mapping(seed_map[seed]['soil'], maps['seed-to-soil'])
        
    return seed_map[seed]['seed']


def check_if_seed(value, seed_ranges):
    for range_ in seed_ranges:
        if value in range_:
            return True
    return False

for i in range(143606042, 300000000):
    seed = location_to_seed(i)
    if check_if_seed(seed, seeds):
        print(f'LOCATION FOUND: {i}')
        break
    else:
        print(f"DON'T HAVE SEED {seed} for LOC {i}")