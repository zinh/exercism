from functools import reduce

chars = list(range(ord('a'), ord('z') + 1))

def encode(plain_text):
    return ''.join(reduce(encode_char, plain_text.lower(), []))

def encode_char(memo, c):
    if c >= 'a' and c <= 'z':
        c_encoded = chr(chars[96 - ord(c)])
        memo.append(c_encoded)
        return memo
    else:
        return memo

def decode(ciphered_text):
    return ''.join(reduce(encode_char, ciphered_text.lower(), []))

print(encode('a'))
