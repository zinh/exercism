from functools import reduce
def classify(number):
    if number <= 0:
        raise ValueError("Non positive number")
    aliquot = reduce(lambda s, d: s + d if number % d == 0 else s, range(1, number//2 + 1), 0)
    if aliquot == number:
        return 'perfect'
    elif aliquot < number:
        return 'deficient'
    else:
        return 'abundant'
