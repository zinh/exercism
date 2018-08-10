def primitive_triplets(number_in_triplet):
    if number_in_triplet % 4 != 0:
        raise(ValueError('Invalid'))
    return {tuple(sorted((m**2 - n**2, 2*m*n, m**2 + n**2)))
            for n in range(1, number_in_triplet + 1) 
            for m in range(n + 1, number_in_triplet + 1) 
            if (m - n) % 2 == 1 and number_in_triplet == 2 * m * n and coprime(n, m)}

def triplets_in_range(range_start, range_end):
    return {(a, b, c) for a in range(range_start, range_end + 1) for b in range(a, range_end + 1) for c  in range(b, range_end + 1) if (a**2 + b**2) == c**2}

def is_triplet(triplet):
    l = list(triplet)
    list.sort(l)
    return l[2]**2 == (l[0]**2 + l[1]**2)

# Assume a <= b
def coprime(a, b):
    for r in range(2, a + 1):
        if a % r == 0 and b % r == 0:
            return False
    return True
