def abbreviate(words):
    return ''.join([abbr(word) for word in words.split(' ')])
def abbr(word):
    return ''.join([w[0].upper() for w in word.split('-')])
