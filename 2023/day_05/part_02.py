with open("./2023/day_05/input.txt", "r") as o:
    input = o.readlines()

seeds_pairs = input[0].strip().split()[1:]
seeds = []
for i in range(0,len(seeds_pairs), 2):
    seeds.append((int(seeds_pairs[i]), int(seeds_pairs[i])+int(seeds_pairs[i+1])))

   
print(seeds) 
# seed_map = {str(seed):{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':''} for seed in seeds}

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

maps['humidity-to-location'] = [v for v in sorted(maps['humidity-to-location'], key=lambda v: int(v.split()[0]))]

print(maps['humidity-to-location'])

mama_mia = None
counter = 0
while not mama_mia:
    print(maps['humidity-to-location'][counter].split()[0])
    source, ranges = maps['humidity-to-location'][counter].split()[1:]
    source, ranges = int(source), int(ranges)
    source_range = (source, source+ranges)
    def get_range(input, map):
        for line in map:
            dest, source, ranges = line.split()
            dest, source, ranges = int(dest), int(source), int(ranges)
            destmax = dest+ranges
            if (input[0] >= dest and input[0] <= destmax) and (input[1] <= destmax and input[1] >= dest):
                print(f'INPUT {input} IS SUBBSET OF {(dest, destmax)}')
                return (source+(input[0] - dest), source+(input[1] - dest))
            elif (input[0] >= dest and input[0] <= destmax):
                print(f'INPUT {input[0]} IS GREATER THAN {dest} BUT LESS THAN {destmax}')
                return (source+(input[0] - dest),  destmax)
            elif input[1] <= destmax and input[1] >= dest:
                print(f'INPUT {input[1]} IS LESS THAN {destmax} BUT GREATER THAN {dest}')
                return (source, source+(input[1]-dest))
        return 'WEEWOO'


    for map in [maps['temperature-to-humidity'],
                maps['light-to-temperature'],
                maps['water-to-light'],
                maps['fertilizer-to-water'],
                maps['seed-to-soil']]:

        print(source_range)
        source_range = get_range(source_range, map)
    
    print(source_range)

    def find_seed(seeds, input):
        mini = input[0]
        for seed in seeds:
            if mini >= seed[0] and mini <= seed[1]:
                return mini
            
    mama_mia = find_seed(seeds, source_range)
    counter += 1
    

print(mama_mia)
        
        
    

# def find_mapping(number, map):
#     for line in map:

#         max_source = source + ranges
#         if number in range(source, max_source):
#             print(f'SEED {number} is in range {source} - {max_source}. RETURNING  {str(dest + (number - source))}')
#             return str(dest + (number - source))
#     print(f'SEED NOT FOUND')
#     return str(number)

#print(source_range)

def part_one_again_lol(seeds, maps):


    seed_map = {seed:{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':''} for seed in seeds}

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

part_one_again_lol([str(mama_mia)], maps)