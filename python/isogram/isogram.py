def is_isogram(string):
    k = {}
    for c in string.lower():
        if c == ' ' or c == '-':
            continue
        if k.get(c):
            return False
        k[c] = True
    return True
