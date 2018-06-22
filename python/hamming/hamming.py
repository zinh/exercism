def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Incompatible length")
    distance = 0
    for idx, nu in enumerate(strand_a):
        distance += 1 if nu != strand_b[idx] else 0
    return distance
