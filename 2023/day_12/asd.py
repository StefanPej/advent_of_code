from aoc_utils import *
from itertools import combinations

inp = read_input(2023, 12)

springs = []
for line in inp:
    spring, broken = line.split()
    temp_sp = []
    temp_br = []
    for _ in range(5):
        temp_sp.append(spring)
        temp_br.append(broken)
    spring = "?".join(sp for sp in temp_sp)
    broken = ','.join(br for br in temp_br)
    broken = broken.split(',')
    broken = [int(broke) for broke in broken]
    springs.append((spring, broken))

def check_valid(spring, groups):
    spring = ''.join(char for char in spring)
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return False
    return True


test = springs[0]

print(test)

def check_valid_placement(board, broken_num):
    board = ''.join(char for char in board)
    # board = board.replace('?','')
    # board = board.replace('!','')
    # #print(board)
    # grouped_broken = board.split('.')
    # grouped_broken = [group for group in grouped_broken if group != '']
    # #print(max(grouped_broken, key=len))
    # if len(max(grouped_broken, key=len)) != broken_num:
    #     return False
    if Substring(board) != broken_num:
        return False
    return True

def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

def Substring(s):
 
    ans, temp = 1, 1
 
    # Traverse the string
    for i in range(1, len(s)):
         
        # If character is same as
        # previous increment temp value
        if (s[i] == s[i - 1] == '#'):
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 1
 
    ans = max(ans, temp)
 
    # Return the required answer
    return ans

def get_poss_placements(board, broken_num, start_ind):
    if start_ind > len(board):
        return []

    hash_count = 0
    ind = start_ind
    while hash_count < broken_num:
        if ind >= len(board):
            return []
        char = board[ind]
        if char == '#':
            hash_count += 1
        ind += 1

    board_slice = board[start_ind:ind]

    q_marks = []
    for i, char in enumerate(board_slice):
        if char in ['?', '#']:
            q_marks.append(i)

    all_possibilities = [combo for combo in combinations(q_marks, broken_num) if checkConsecutive(combo)]

    poss_placements = []
    for poss in sorted(all_possibilities):
        temp = [*board_slice]
        for ind_ in poss:
            temp[ind_] = '#'

        preceding_dot = min(poss) - 1
        seceeding_dot = max(poss) + 1
        for i in range(preceding_dot + 1):
            if temp[i] == '?':
                temp[i] = '.'
        if seceeding_dot < len(temp)-1:
            temp[seceeding_dot] = '.'
        

        # for i, char in enumerate(temp):
        #     if char == '?':
        #         temp[i] = '.'
        if check_valid_placement(temp, broken_num):
            if seceeding_dot == len(temp):
                poss_placements.append((board[:start_ind] + ''.join(char for char in temp) + '.' + board[ind_+2:], ind_))
            else:
                poss_placements.append((board[:start_ind] + ''.join(char for char in temp) + board[ind_+1:], ind_))

    return poss_placements

boards = []
start_ind = 0
boards_to_test = [(test[0], 0)]
for broken_num in test[1]:
    #print(broken_num)
    for board in boards_to_test:
        #print(board)
        latest_boards = []
        for new_board in get_poss_placements(board[0], broken_num, board[1]):
            if new_board != []:
                latest_boards.append(new_board)
    if latest_boards == []:
        break
    boards.append(latest_boards)
    boards_to_test = latest_boards
    print('NEW-BOARDS: ', latest_boards)
#print(boards)
