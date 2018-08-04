from math import sqrt
def prime_factors(natural_number):
    if natural_number < 2:
        return []
    for i in range(2, int(sqrt(natural_number)) + 1):
        if natural_number % i == 0:
            return [i] + prime_factors(natural_number // i)
    return [natural_number]
