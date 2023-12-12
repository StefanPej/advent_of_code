from aoc_utils import *
from itertools import combinations
import re

inp = read_input(2023, 12)

with open("./2023/day_12/test.txt", "r") as o:
    inp = o.readlines()

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
    spring = spring.replace('?', '.')
    spring = spring.replace('!', '#')
    grouped_broken = spring.split('.')
    grouped_broken = [group for group in grouped_broken if group != '']
    for i, group in enumerate(grouped_broken):
        if len(group) != groups[i]:
            return False
    return True

def find_placements(board):
    ret = []
    finding = False
    for i, char in enumerate(board):
        if char in ['?', '#']:
            if not finding:
                finding = True
                start_ind = i
        else:
            if finding:
                ret.append((start_ind, i-1))
                finding = False
    if finding:
        ret.append((start_ind, len(board)-1))
    return ret

def mark_broken(board, broken_num, need_to_place):
    if board.count('?') + board.count('#') <= need_to_place:
        return None
    placement_locs = [loc for loc in find_placements(board) if (loc[1]+1-loc[0]) >= broken_num]
    og_hashes = [match.start() for match in re.finditer('#', board)]
    #print(placement_locs)
    ret = []
    if not placement_locs: 
        return None
    for loc in placement_locs:
        start_ind = loc[0]
        end_ind = loc[0] + broken_num
        while end_ind <= loc[1]+1:
            temp_board = [*board]
            for i in range(start_ind, end_ind):
                temp_board[i] = '!'
            if start_ind > 0:
                temp_board[start_ind-1] = '.'
            if end_ind < len(temp_board)-1:
                temp_board[end_ind] = '.'

            start_ind += 1
            end_ind += 1
            # dont append board if it deletes an OG hash
            for og_hash in og_hashes:
                if temp_board[og_hash] != '#':
                    continue
            ret.append(''.join(char for char in temp_board))

    return ret

def pre_proc(springs, groups):
    spring_broken = [*springs]
    for i, char in enumerate(spring_broken):
        if char == '.':
            continue
        if char == '?':
            break
        if char == '#':
            hash_count = 1
            ind = i
            while hash_count < groups[0]:
                ind += 1
                spring_broken[ind] = '#'
                hash_count += 1
            spring_broken[ind+1] = '.'
            groups.pop(0)
            break
    
    springs = "".join(char for char in spring_broken)

    spring_broken = [*springs]
    for i, char in enumerate(reversed(spring_broken)):
        if char == '.':
            continue
        if char == '?':
            break
        if char == '#':
            hash_count = 1
            ind = len(spring_broken) -1 -i
            while hash_count < groups[-1]:
                ind -= 1
                spring_broken[ind] = '#'
                hash_count += 1
            spring_broken[ind+1] = '.'
            groups.pop(-1)
            break
    
    springs = "".join(char for char in spring_broken)

    return springs, groups

sp = []
for spr in springs:
    sp.append(pre_proc(spr[0], spr[1]))
springs = sp


test = springs[5]
boards_to_test = [test[0]]
# ttt = '????.!!!!!!..!!!!!.?????.!!!!!!..!!!!!.?????.!!!!!!..!!!!!.?????.!!!!!!..!!!!!.?????.!!!!!!..!!!!!.'
# boards_to_test = [ttt]
print(test[0])
print(mark_broken(test[0], 3, sum(test[1])))
all_boards = []
need_to_place = sum(test[1])
for broken_num in sorted(test[1], reverse=True):
    next_boards_to_test = set()
    for board_to_test in boards_to_test:
        new_boards = mark_broken(board_to_test, broken_num, need_to_place)
        # print('placing', broken_num, 'into', board_to_test)
        # print(new_boards)
        if new_boards is None:
            continue
        for new_board in new_boards:
            if new_board is not None:
                # if broken_num == min(test[1]):
                #     if check_valid(new_board, test[1]):
                #         next_boards_to_test.add(new_board)
                # else:
                #     next_boards_to_test.add(new_board)
                next_boards_to_test.add(new_board)
    boards_to_test = next_boards_to_test
    need_to_place +- broken_num
    print('DONE: ', broken_num, ' NEXT LEN OF BOARDS TO TEST: ', len(boards_to_test))

#print(all_poss)
#print(len([x for xs in all_boards for x in xs]))
print(sum([check_valid(board, test[1]) for board in boards_to_test]))




