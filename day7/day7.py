with open('input.txt') as f:
    hands = {hand: int(bet) for (hand, bet) in map(lambda x: x.split(), f.readlines())}

typeorder = [[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[1,4],[5]]
cardorder = {key: val for (val, key) in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}

def hand_to_type(h):
    cnt = {}
    for c in h:
        cnt[c] = cnt.get(c, 0) + 1
    return sorted(cnt.values())

def comp_hands(a, b):
    atype = typeorder.index(hand_to_type(a))
    btype = typeorder.index(hand_to_type(b))
    if atype != btype:
        return atype - btype
    for i in range(5):
        acard = cardorder[a[i]]
        bcard = cardorder[b[i]]
        if acard != bcard:
            return (acard-bcard)
    return 0

import functools
ranked_hands = sorted(list(hands.keys()), key=functools.cmp_to_key(comp_hands))
sum = 0
for i, h in enumerate(ranked_hands):
    sum += (i+1)*hands[h]
print(sum)
