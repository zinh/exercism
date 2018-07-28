from functools import reduce

def flatten(iterable):
    if iterable == None or iterable == ():
        return []
    if type(iterable) == list:
        return reduce(lambda memo, el: memo + flatten(el), iterable, [])
    else:
        return [iterable]
