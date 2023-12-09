from utils2022 import read_input

input = read_input("03")

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
PRIOS = {letter:i for letter, i in zip(letters.split(), range(1,53))}

bags_grouped = []
count = -1
for i, line in enumerate(input):
    if i % 3 == 0:
        bags_grouped.append([])
        count += 1
    bags_grouped[count].append(line)

# bags_grouped = [input[i:i+3] for i in range(len(input))]
# bags_grouped = [bags for bags in bags_grouped if len(bags) == 3]

def get_duped_item(bags):
    first, sec, third = bags
    first = set(first)
    sec = set(sec)
    third = set(third)
    return list(first.intersection(sec).intersection(third))[0]

count = 0
for i, bag in enumerate(bags_grouped):
    print('DONE BAG ', i)
    count += PRIOS[get_duped_item(bag)]

print(count)
