from functools import reduce

def largest_palindrome(max_factor, min_factor):
    if not valid_range(min_factor, max_factor):
        raise ValueError('Invalid range')
    product_lst = products(min_factor, max_factor)
    lagest = max(product_lst.keys())
    print(lagest)
    return lagest, product_lst[lagest]

def smallest_palindrome(max_factor, min_factor):
    if not valid_range(min_factor, max_factor):
        raise ValueError('Invalid range')
    product_lst = products(min_factor, max_factor)
    smallest = min(product_lst.keys())
    return smallest, product_lst[smallest]

def valid_range(min_factor, max_factor):
    return min_factor < max_factor

def products(min_factor, max_factor):
    r = dict()
    for a in range(min_factor, max_factor + 1):
        for b in range(a, max_factor + 1):
            if palindrome(a * b):
                r.setdefault(a * b, {(a, b)}).add((a, b))
    return r

def palindrome(num):
    s = str(num)
    return s[::-1] == s
