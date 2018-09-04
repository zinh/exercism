def best_hands(hands):
    ranking = {'straight flush': 8, 'four of a kind': 7, 'full house': 6, 
            'flush': 5, 'straight': 4, 'three of a kind': 3, 'two pairs': 2, 
            'one pair': 1, 'high cards': 0}
    if len(hands) == 1:
        return hands
    sorted_hands = [(hand, type_of_hands(hand)) for hand in hands]
    sorted_hands.sort(key = lambda hand: ranking[hand[1][0]], reverse=True)
    same_type_hands = [hand for hand in sorted_hands if hand[1][0] == sorted_hands[0][1][0]]
    same_type_hands.sort(key = lambda hand: hand[1][1][-1], reverse=True)
    return [hand[0] for hand in same_type_hands if hand[1][1][-1] == same_type_hands[0][1][1][-1]]

def rank_to_int(rank):
    if rank == 'A':
        return 14
    if rank == 'K':
        return 13
    if rank == 'Q':
        return 12
    if rank == 'J':
        return 11
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
        return ('straight flush', [cards[-1][0]])
    if straight:
        return ('straight', [cards[-1][0]])
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
        return ('full house', list(hand_by_rank.keys())[-1:])
    for rank, suits in hand_by_rank.items():
        if len(suits) == 4:
            return ('four of a kind', [rank])
        if len(suits) == 3:
            return ('three of a kind', [rank])
        if len(suits) == 2:
            pair.append(rank)
    # flush: five cards same suit
    for suit, ranks in hand_by_suits.items():
        if len(ranks) == 5:
            return ('flush', ranks)
    if len(pair) == 2:
        return ('two pairs', pair)
    if len(pair) == 1:
        return ('one pair', pair)
    return ('high cards', [cards[-1][0]])
