with open('input.txt') as f:
    hands = {hand: int(bid) for (hand, bid) in map(lambda x: x.split(), f.readlines())}

typeorder = [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]]
cardorder = {key: val for (val, key) in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}
cardorder_Joker = {key: val for (val, key) in enumerate(['J','2','3','4','5','6','7','8','9','T','Q','K','A'])}

def hand_to_type(h):
    cnt = {}
    for c in h:
        cnt[c] = cnt.get(c, 0) + 1
    return sorted(cnt.values())

def hand_to_type_Joker(h):
    cnt = {}
    jokers = 0
    for c in h:
        if c == 'J':
            jokers += 1
        else:
            cnt[c] = cnt.get(c, 0) + 1
    if jokers == 5:
        return [5]
    else:  
        temp = list(sorted(cnt.values()))
        temp[-1] += jokers
        return temp

def comp_hands(a, b):
    atype = typeorder.index(hand_to_type_Joker(a))
    btype = typeorder.index(hand_to_type_Joker(b))
    if atype != btype:
        return atype - btype
    for i in range(5):
        acard = cardorder_Joker[a[i]]
        bcard = cardorder_Joker[b[i]]
        if acard != bcard:
            return (acard-bcard)
    return 0

import functools
ranked_hands = sorted(list(hands.keys()), key=functools.cmp_to_key(comp_hands))
sum = 0
for i, h in enumerate(ranked_hands):
    sum += (i+1)*hands[h]
print(sum)
