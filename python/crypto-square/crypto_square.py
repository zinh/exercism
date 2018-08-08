from math import ceil

def encode(plain_text):
    if len(plain_text) == 0:
        return ''
    normalized = normalize(plain_text)
    if len(normalized) <= 1:
        return normalized
    col, row = break_line(len(normalized))
    arr = [normalized[c::row] for c in range(0, col)]
    encoded_str = ''.join(arr)
    if (col * row) > len(encoded_str):
        encoded_str += ' ' * (col * row - len(encoded_str))
    return ' '.join([encoded_str[r:(r + col)] for r in range(0, len(encoded_str), col)])

def normalize(plain_text):
    return ''.join([c for c in plain_text.lower() if 'a' <= c <= 'z' or '0' <= c <= '9'])

def break_line(l):
    for col in range(1, l):
        row = ceil(l / col)
        if 0 <= (row - col) <= 1:
            return (col, row)
    return None
