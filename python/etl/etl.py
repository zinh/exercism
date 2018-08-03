from functools import reduce

def transform(legacy_data):
    return reduce(convert ,legacy_data.items(), {})

def convert(memo, element):
    score, chars = element
    for char in chars:
        memo[char.lower()] = score
    return memo
