from functools import reduce
def square_of_sum(count):
    return sum(range(1, count + 1)) ** 2

def sum_of_squares(count):
    return reduce(lambda s, n: s + n ** 2, range(1, count + 1), 0)


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
