from functools import reduce

chars = list(range(ord('a'), ord('z') + 1))

def encode(plain_text):
    s = reduce(encode_char, plain_text.lower(), [])
    return ' '.join([''.join(s[i:i + 5]) for i in range(0, len(s), 5)])

def encode_char(memo, c):
    if c >= 'a' and c <= 'z':
        c_encoded = chr(chars[96 - ord(c)])
        memo.append(c_encoded)
    elif c >= '0' and c <= '9':
        memo.append(c)
    return memo

def decode(ciphered_text):
    return ''.join(reduce(encode_char, ciphered_text.lower(), []))
