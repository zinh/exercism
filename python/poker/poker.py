def best_hands(hands):
    if len(hands) == 1:
        return hands

def rank_to_int(rank):
    if rank == 'K':
        return 12
    if rank == 'Q':
        return 11
    if rank == 'J':
        return 10
    else:
        return int(rank)
# hand: string "4D 5S 6S 8D 3C",
def type_of_hands(hand):
    cards = [(rank_to_int(card[0:-1]), card[-1]) for card in hand.split(' ')]
    cards.sort(key=lambda card: card[0])
    # straight flush
    straight_flush = True
    straight = True
    for current_card in range(len(cards) - 1):
        next_card = current_card + 1
        if cards[current_card][0] != cards[next_card][0] - 1:
            straight_flush = False
            straight = False
            break
        if cards[next_card][1] != cards[current_card][1]:
            straight_flush = False
    if straight_flush:
        return ('straight flush', cards)
    if straight:
        return ('straight', cards)
    # four_kinds
    hand_by_rank = {}
    hand_by_suits = {}
    pair = []
    for rank, suit in cards:
        hand_by_rank.setdefault(rank, []).append(suit)
        hand_by_suits.setdefault(suit, []).append(rank)
    # three cards one rank, 2 cards another rank
    #import pdb; pdb.set_trace()
    if len(hand_by_rank.keys()) == 2 and (len(list(hand_by_rank.values())[0]) == 2 or len(list(hand_by_rank.values())[0]) == 3):
        return ('full house', list(hand_by_rank.keys()))
    for rank, suits in hand_by_rank.items():
        if len(suits) == 4:
            return ('four of a kind', rank)
        if len(suits) == 3:
            return ('three of a kind', rank)
        if len(suits) == 2:
            pair.append(rank)
    # flush: five cards same suit
    for suit, ranks in hand_by_suits.items():
        if len(ranks) == 5:
            return ('flush', ranks)
    if len(pair) == 2:
        return ('two pairs', pair)
    if len(pair) == 1:
        return ('one pairs', pair)
    return ('high cards', cards[-1])

#print(type_of_hands("4S 5H 4D 5D 4H"))
