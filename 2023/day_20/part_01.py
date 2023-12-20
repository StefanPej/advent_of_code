from aoc_utils import *

inp = read_input(2023, 20)

# with open('2023/day_20/test.txt') as o:
#     inp = o.readlines()

modules = {}
for line in inp:
    out = [out.rstrip(',') for out in line.split()[2:]]
    name = line.split()[0][1:]
    
    if line.split()[0] == 'broadcaster':
        modules['broadcaster'] = {'type': 'broadcaster', 
                                  'out': [out.rstrip(',') for out in line.split()[2:]]}
    elif line.startswith('%'):   
        modules[name] = {'type': 'flip',
                         'power': 'off',
                         'out': out}
    elif line.startswith('&'):
        in_ = {}
        for line2 in inp:
            checks = [word.rstrip(',') for word in line2.split()[2:]]
            if name in checks:
                in_[line2.split()[0][1:]] = 'low'
        modules[name] = {'type': 'conj',
                    'out': out,
                    'in': in_}

def process_action(pulse, module_name, sender):
    module = modules.get(module_name, False)
    if not module:
        return []
    out_list = module['out']
    ret = []
    if module['type'] == 'broadcaster':
        for mod in out_list:
            ret.append(('low', mod, module_name))
    
    elif module['type'] == 'flip':
        power = module['power']

        if pulse == 'low':
            if power == 'off':
                module['power'] = 'on'
                for mod in out_list:
                    ret.append(('high', mod, module_name))
            else:
                module['power'] = 'off'
                for mod in out_list:
                    ret.append(('low', mod, module_name))               
    
    elif module['type'] == 'conj':
        module['in'][sender] = pulse

        if all(val == 'high' for val in module['in'].values()):
            for mod in out_list:
                ret.append(('low', mod, module_name))       
        else:
            for mod in out_list:
                ret.append(('high', mod, module_name))

    return ret


counts = {'low':0, 'high':0}
counter = 0
while counter < 1000:
    actions = [('low', 'broadcaster', 'button')]
    while actions:
        pulse, mod, sender = actions.pop(0)
        counts[pulse] += 1
        results = process_action(pulse, mod, sender)
        for result in results:
            actions.append(result)
    counter += 1

print(counts['low']*counts['high'])
