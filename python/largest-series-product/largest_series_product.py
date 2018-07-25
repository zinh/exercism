from functools import reduce

def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError('Size is too big')
    if size == 0:
        return 1
    start = 0
    current_product = 0
    while (start + size) <= len(series):
        p = product_of_digits(series[start:start+size])
        if p > current_product:
            current_product = p
        start += 1
    return current_product

def product_of_digits(number):
    return reduce(lambda memo, digit: memo * int(digit), number, 1)
