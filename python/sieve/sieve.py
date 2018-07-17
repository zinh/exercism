def sieve(limit):
    if limit == 1:
        return []
    s = [True] * (limit + 1)
    for i in range(2, limit + 1):
        if not s[i]:
            continue
        for j in range(2, (limit // i) + 1):
            s[i * j] = False
    return [i for i in range(2, limit + 1) if s[i]]
