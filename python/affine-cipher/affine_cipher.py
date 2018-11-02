def encode(plain_text, a, b):
    if not coprime(a, 26):
        raise ValueError("a, 26 must be coprime")
    encoded_chars = [encode_char(c, a, b) if is_ascii_char(c) else c for c in plain_text if valid_char(c)]
    return " ".join(["".join(encoded_chars[i:i+5]) for i in range(0, len(encoded_chars), 5)])

def encode_char(c, a, b):
    x = ord(c) - ord('a') if c.islower() else ord(c) - ord('A')
    return chr(ord('a') + (a * x + b) % 26)

def decode(ciphered_text, a, b):
    a1 = mmi(a, 26)
    return "".join([decode_char(c, a1, b) if is_ascii_char(c) else c for c in ciphered_text if valid_char(c)])

def decode_char(c, a1, b):
    if c.isupper():
        raise ValueError("Invalid character")
    y = ord(c) - ord('a')
    return chr(ord('a') + a1 * (y - b) % 26)

def valid_char(c):
    return is_number(c) or is_ascii_char(c)

def is_number(c):
    return ord('0') <= ord(c) <= ord('9')

def is_ascii_char(c):
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')

def coprime(a, b):
    return gcd(a, b) == 1

def gcd(a, b):
    if b <= 0:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(a - b, b)

def mmi(a, m):
    t, newt = 0, 1
    r, newr = m, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError("Not invertible")
    if t < 0:
        t = t + m
    return t
