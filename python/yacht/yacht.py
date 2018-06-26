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
    if category == YACHT and is_yatch(dice):
        return sum(dice)
    if category == FULL_HOUSE and full_house(dice):
        return sum(dice)
    if category == FOUR_OF_A_KIND and four_kind(dice):
        return sum(dice)
    if category == LITTLE_STRAIGHT and little_straight(dice):
        return 30
    if category == BIG_STRAIGHT and big_straight(dice):
        return 30
    if category == CHOICE:
        return sum(dice)
    return 0

def is_yatch(dice):
    for val in dice:
        if val != dice[0]:
            return False
    return True

def is_number(dice, number):
    for val in dice:
        if val == number:
            return True
    return False

def full_house(dice):
    return {dice.count(x) for x in set(dice)} == {2, 3}

def four_kind(dice):
    return {x: dice.count(x) for x in set(dice)} == {4, 1}

def little_straight(dice):
    return set(dice) == {1,2,3,4,5}

def big_straight(dice):
    return set(dice) == {2, 3, 4, 5, 6}
