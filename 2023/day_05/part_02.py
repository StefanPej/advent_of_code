with open("./2023/day_05/input.txt", "r") as o:
    input = o.readlines()

seeds_pairs = input[0].strip().split()[1:]
seeds = []
for i in range(0,len(seeds_pairs), 2):
    seeds.append((int(seeds_pairs[i]), int(seeds_pairs[i])+int(seeds_pairs[i+1])-1))

   
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
maps['temperature-to-humidity'] = [v for v in sorted(maps['temperature-to-humidity'], key=lambda v: int(v.split()[0]), reverse=True)]
maps['water-to-light'] = [v for v in sorted(maps['water-to-light'], key=lambda v: int(v.split()[0]))]
maps['fertilizer-to-water'] = [v for v in sorted(maps['fertilizer-to-water'], key=lambda v: int(v.split()[0]))]
maps['soil-to-fertilizer'] = [v for v in sorted(maps['soil-to-fertilizer'], key=lambda v: int(v.split()[0]))]
maps['seed-to-soil'] = [v for v in sorted(maps['seed-to-soil'], key=lambda v: int(v.split()[0]))]


#print(maps['humidity-to-location'])

mama_mia = None
counter = 0
while not mama_mia:
    print('SEARCHIN FROM LOC:', maps['humidity-to-location'][counter].split()[0])
    print('TO:', int(maps['humidity-to-location'][counter].split()[0])+int(maps['humidity-to-location'][counter].split()[2])-1)
    source, ranges = maps['humidity-to-location'][counter].split()[1:]
    source, ranges = int(source), int(ranges)
    source_range = [(source, source+ranges-1)]
    def get_range(input_list, map):
        ret = []
        for input in input_list:
            print('CHECKING', input)
            for line in map:
                dest, source, ranges = line.split()
                dest, source, ranges = int(dest), int(source), int(ranges)
                destmax = dest+ranges-1
                
                if (input[0] >= dest and input[0] <= destmax) and (input[1] <= destmax and input[1] >= dest):
                    print(f'INPUT {input} IS SUBBSET OF {(dest, destmax)}')
                    print(f'ADDING {(source+(input[0] - dest), source+(input[1] - dest))} TO RET')
                    ret.append((source+(input[0] - dest), source+(input[1] - dest)))
                    input = ()
                    break
                elif (input[0] >= dest and input[0] <= destmax):
                    print(f'INPUT {input[0]} IS GREATER THAN {dest} BUT LESS THAN {destmax}')
                    ret.append((source+(input[0] - dest),  source+ranges))
                    print(f'ADDING {(source+(input[0] - dest),  source+ranges)} TO RET')
                    input = (destmax+1, input[1])
                elif input[1] <= destmax and input[1] >= dest:
                    print(f'INPUT {input[1]} IS LESS THAN {destmax} BUT GREATER THAN {dest}')
                    ret.append((source, source+(input[1]-dest)))
                    print(f'ADDING {(source, source+(input[1]-dest))} TO RET')
                    input = (input[0], dest-1)
                print("INPUT NOW", input)
        if not ret:
            return 'WEEWOO'
        if input:
            print('WEEWOO INPUT STILL', input)
            ret.append(input)
        return ret


    for map in [maps['temperature-to-humidity'],
                maps['light-to-temperature'],
                maps['water-to-light'],
                maps['fertilizer-to-water'],
                maps['seed-to-soil']]:

        print(source_range)
        source_range = get_range(source_range, map)
    
    print(source_range)

    def find_seed(seeds, inputs):
        ret = []
        for input in inputs:
            for seed in seeds:
                if (input[0] >= seed[0] and input[0] <= seed[1]) and (input[1] <= seed[1] and input[1] >= seed[0]):
                    print(f'RANGE {input} IS SUBBSET OF {seed}')
                    ret.append(input)
                elif (input[0] >= seed[0] and input[0] <= seed[1]):
                    print(f'RANGE {input[0]} IS GREATER THAN {seed[0]} BUT LESS THAN {destmax}')
                    ret.append((input[0], seed[1]))
                elif input[1] <= seed[1] and input[1] >= seed[0]:
                    print(f'RANGE {input[1]} IS LESS THAN {seed[1]} BUT GREATER THAN {seed[0]}')
                    ret.append((seed[0], input[1]))
        return ret
            
    mama_mia = find_seed(seeds, source_range)
    counter += 1
    
print("!@#!#!@#!@#!@#!@#")
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
            max_source = source + ranges -1
            if number in range(source, max_source):
                #print(f'SEED {number} is in range {source} - {max_source}. RETURNING  {str(dest + (number - source))}')
                return str(dest + (number - source))
        #print(f'SEED NOT FOUND')
        return str(number)
                
                
    #print(maps['temperature-to-humidity'])
    #test = {'13548942':{'soil':'', 'fert':'', 'water':'', 'light':'', 'temp':'', 'humid':'', 'loc':''}}
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
    

    return list(seed_loc.values())[0]

    

all_seeds = []

for tups in mama_mia:
    for seed in tups:
        all_seeds.append(str(seed))
print('ASDASDASDASDSAD')
print(all_seeds)
print(part_one_again_lol(all_seeds, maps))

test_seed = ['2866967606']
print(part_one_again_lol(test_seed, maps))

# count = 0
# for seed_pair in mama_mia:
#     min_loc = 99999999999999999999999999999999999
#     print(seed_pair)
#     for seed in range(seed_pair[0], seed_pair[1]):
#         min_loc = min(part_one_again_lol([str(seed)], maps), min_loc)
#         count += 1
#         if count % 1000 == 0:
#             print(f'checked {count} seeds')
#             #print(min_loc)

# print(f'min loc is: {min_loc}')

# total_seeds = 0
# for sp in mama_mia:
#     total_seeds += sp[1] - sp[0]
# print(total_seeds)
