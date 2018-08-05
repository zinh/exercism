def translate(text):
    return ' '.join([single_word(word) for word in text.split(' ')])

def single_word(text):
    if len(text) == 2 and text[1] == 'y':
        return text[::-1] + 'ay'
    if vowel(text[0]) or text[0:2] == 'xr' or text[0:2] == 'yt':
        return text + 'ay'
    s = ''
    for idx, c in enumerate(text):
        if idx > 0 and c == 'y':
            return text[idx:] + s + 'ay'
        if c == 'q' and text[idx + 1] == 'u':
            return text[idx+2:] + s + 'qu' + 'ay'
        if vowel(c):
            return text[idx:] + s + 'ay'
        s += c
    return text

def vowel(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return True
    return False

def consonant(c):
    return not vowel(c)
