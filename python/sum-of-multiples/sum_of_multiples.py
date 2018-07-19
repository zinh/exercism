from functools import reduce

def sum_of_multiples(limit, multiples):
    return reduce(lambda sum, n: sum + n if multiple_by(n, multiples) else sum, range(1, limit), 0)
def multiple_by(a, lst):
    return any([a % m == 0 for m in lst])
