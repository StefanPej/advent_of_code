with open("./2023/day_07/input.txt", "r") as o:
    input = o.readlines()

hands_ = [[line.split()[0], int(line.split()[1])] for line in input]

ordered = []

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
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

hands = []
for hand in hands_:
    val = get_hand_value(hand[0])
    temp = hand
    temp.append(val)
    hands.append(temp)
#print(hands)

def compare_hands(hand1, hand2):
    hand1_val = get_hand_value(hand1)
    hand2_val = get_hand_value(hand2)
    if hand1_val < hand2_val:
        return True
    elif hand1_val == hand2_val:
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


for hand in hands:
    inserted = False
    if not ordered:
        ordered.append(hand)
        continue
    for i, order in enumerate(ordered):
        if compare_hands(hand[0], order[0]):
            ordered.insert(i, hand)
            inserted = True
            break
    if not inserted:
        ordered.append(hand)
    #print(ordered)

    

bets = [(hand[0], hand[1], rank, hand[2]) for hand, rank in zip(ordered, range(len(ordered), 0, -1))]
#print(len(bets))
vals = sum([hand[1]*hand[2] for hand in bets])
print(vals)
counter = 0
# for i, thing in enumerate(bets):
#     print(i)
#     assert thing[3] <= bets[i+1][3]


