from functools import reduce
def on_square(integer_number):
    if integer_number <= 0:
        raise ValueError("Non-positive number")
    if integer_number > 64:
        raise ValueError("Too big number")
    return 2**(integer_number - 1)


def total_after(integer_number):
    if integer_number <= 0:
        raise ValueError("Non-positive number")
    if integer_number > 64:
        raise ValueError("Too big number")
    return reduce(lambda sum, el: sum + on_square(el), range(1, integer_number + 1), 0)
