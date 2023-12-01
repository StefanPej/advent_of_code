num_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

with open("inputs.txt", "r") as o:
    inputs = o.readlines()

def get_line(line):
    first_nums = {}
    last_nums = {}
    for k in num_dict.keys():
        first_nums[k] = line.find(k)
        last_nums[k] = line.rfind(k)

    first_nums = {k:v for k, v in first_nums.items() if v != -1}
    first_nums = {k: v for k, v in sorted(first_nums.items(), key=lambda item: item[1])}

    first_num = num_dict[list(first_nums.keys())[0]]

    last_nums = {k:v for k, v in last_nums.items() if v != -1}
    last_nums = {k: v for k, v in sorted(last_nums.items(), key=lambda item: item[1])}

    last_num = num_dict[list(last_nums.keys())[-1]]
    
    return int(first_num+last_num)

count = 0
for line in inputs:
    count += get_line(line)
print(count)
