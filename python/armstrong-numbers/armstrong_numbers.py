from functools import reduce
def is_armstrong(number):
    n = str(number)
    power = len(n)
    sum = reduce(lambda acc, digit: acc + int(digit) ** power, n, 0)
    return (sum == number)
