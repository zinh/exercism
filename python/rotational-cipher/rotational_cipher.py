def rotate(text, key):
    return ''.join(list(map(lambda char: cipher(char, key), text)))

def cipher(char, key):
    if (char >= 'a' and char <= 'z'):#  or (char >= 'A' and char <= 'Z'):
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    elif char >= 'A' and char <= 'Z':
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    else:
        return char
