with open("./2023/day_07/input.txt", "r") as o:
    input = o.readlines()

hands = [[line.split()[0], int(line.split()[1])] for line in input]

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
CARD_VALS = {card:i for i, card in enumerate(CARDS)}

def get_hand_value(hand):
    set_hand = set(hand)
    set_len = len(set_hand)
    if set_len == 1:
        return 1
    elif set_len == 5:
        return 7
    elif set_len == 4:
        return 6
    elif set_len == 2:
        if hand.count(hand[0]) in [1,4]:
            return 2 
        else:
            return 3
    else:
        for card in hand:
            if hand.count(card) == 3:
                return 4
        return 5
    
def break_hand(hand):
    inds = []
    for i, char in enumerate(hand):
        if char == 'J':
            inds.append(i)

    return hand.replace('J', ''), inds

def find_most_common_card(hand):
    counts = [(char,hand.count(char)) for char in hand if char != 'J']
    return [count for count in sorted(counts, key=lambda item: item[1], reverse=True)][0][0]

def make_best_hand(hand):
    if hand.find('J') == -1:
        return hand
    
    elif hand == 'JJJJJ':
        return hand
    
    common_card = find_most_common_card(hand)
    return hand.replace('J', common_card)

def compare_hands(hand1, hand2, temp_hand, order2):
    hand1_val = get_hand_value(hand1)
    hand2_val = get_hand_value(hand2)
    temp_hand_val = get_hand_value(temp_hand)
    order2_val = get_hand_value(order2)
    if temp_hand_val < order2_val:
        return True
    elif temp_hand_val == order2_val:
        for hand1_card, hand2_card in zip(hand1, hand2):
            hand1_card_val = CARD_VALS[hand1_card]
            hand2_card_val = CARD_VALS[hand2_card]
            if hand1_card_val < hand2_card_val:
                return True
            elif hand1_card_val > hand2_card_val:
                return False
            else:
                pass
    return False

ordered = []

for hand in hands:
    temp_hand = make_best_hand(hand[0])
    inserted = False
    if not ordered:
        ordered.append((temp_hand, hand[1], hand[0]))
        continue
    
    for i, order in enumerate(ordered):
        #print(ordered)
        if compare_hands(hand[0], order[2], temp_hand, order[0]):
            ordered.insert(i, (temp_hand, hand[1], hand[0]))
            inserted = True
            break
    if not inserted:
        ordered.append((temp_hand, hand[1], hand[0]))
print(ordered)

# for hand in hands[:20]:
#     print(hand, make_best_hand(hand[0]))

#print(make_best_hand(hands[925][0]))
bets = [(hand[1], rank) for hand, rank in zip(ordered, range(len(ordered), 0, -1))]
print(bets)
vals = sum([hand[1]*hand[0] for hand in bets])
print(vals)
counter = 0
# for i, thing in enumerate(bets):
#     print(i)
#     assert thing[3] <= bets[i+1][3]

