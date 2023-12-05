with open("./2023/day_05/input.txt", "r") as o:
    input = o.readlines()

seeds = input[0].strip().split()[1:]
seed_map = {seed:{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':''} for seed in seeds}

#get maps
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
        dest, source, ranges = line.split()
        dest, source, ranges, number = int(dest), int(source), int(ranges), int(number)
        max_source = source + ranges
        if number in range(source, max_source):
            print(f'SEED {number} is in range {source} - {max_source}. RETURNING  {str(dest + (number - source))}')
            return str(dest + (number - source))
    print(f'SEED NOT FOUND')
    return str(number)
            
            
#print(maps['temperature-to-humidity'])
test = {'13548942':{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':''}}
for seed in seed_map:
    seed_map[seed]['soil'] = find_mapping(seed, maps['seed-to-soil'])
    seed_map[seed]['fert'] = find_mapping(seed_map[seed]['soil'], maps['soil-to-fertilizer'])
    seed_map[seed]['water'] = find_mapping(seed_map[seed]['fert'], maps['fertilizer-to-water'])
    seed_map[seed]['light'] = find_mapping(seed_map[seed]['water'], maps['water-to-light'])
    seed_map[seed]['temp'] = find_mapping(seed_map[seed]['light'], maps['light-to-temperature'])
    seed_map[seed]['humid'] = find_mapping(seed_map[seed]['temp'], maps['temperature-to-humidity'])
    seed_map[seed]['loc'] = find_mapping(seed_map[seed]['humid'], maps['humidity-to-location'])
    
seed_loc = {seed: int(seed_map[seed]['loc']) for seed in seed_map}

seed_loc = {k: v for k, v in sorted(seed_loc.items(), key=lambda item: item[1])}

print(seed_loc)

