with open('./2022/input_06.txt') as o:
    input = o.read()

for j in range(len(input)-1):
    if j < 3:
        continue
    sub = input[j-3:j+1]
    if len(sub) == len(set(sub)):
        print(j+1)
        break
