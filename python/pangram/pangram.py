def is_pangram(sentence):
    if sentence == "":
        return False
    h = {}
    for c in range(ord('a'), ord('z')):
        h[chr(c)] = 0
    for c in sentence.lower():
        if h.get(c) == 0:
            h[c] += 1
    for c, count in h.items():
        if count == 0:
            return False
    return True
