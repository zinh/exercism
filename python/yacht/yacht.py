# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    counted_dice = count_dice(dice)
    if category == YACHT and is_yatch(counted_dice):
        return 50
    if category == FULL_HOUSE and full_house(counted_dice):
        return sum(dice)
    if category == FOUR_OF_A_KIND and four_kind(counted_dice):
        val = counted_dice[4] if 4 in counted_dice else counted_dice[5]
        return val * 4
    if category == LITTLE_STRAIGHT and little_straight(dice):
        return 30
    if category == BIG_STRAIGHT and big_straight(dice):
        return 30
    if category == CHOICE:
        return sum(dice)
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES] and is_number(dice, category):
        return category * dice.count(category)
    return 0


def count_dice(dice):
    return {dice.count(x): x for x in dice}

def is_yatch(dice):
    return 5 in dice

def is_number(dice, number):
    for val in dice:
        if val == number:
            return True
    return False

def full_house(dice):
    return 2 in dice and 3 in dice

def four_kind(dice):
    return 4 in dice or 5 in dice

def little_straight(dice):
    return set(dice) == {1,2,3,4,5}

def big_straight(dice):
    return set(dice) == {2, 3, 4, 5, 6}
