from utils2022 import read_input

input = read_input("03")

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
PRIOS = {letter:i for letter, i in zip(letters.split(), range(1,53))}

def get_duped_item(bags):
    first_compart = set(bag[0:len(bag)//2])
    second_compart = set(bag[len(bag)//2:len(bag)])
    return list(first_compart.intersection(second_compart))[0]

count = 0
for bag in input:
    count += PRIOS[get_duped_item(bag)]

print(count)
