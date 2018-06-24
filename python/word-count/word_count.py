import re

def word_count(phrase):
    result = {}
    current_word = ""
    phrase = phrase.lower()
    for i, c in enumerate(phrase):
        if delimiter(c):
            current_word = trim(current_word)
            if current_word != '':
                result[current_word] = result.get(current_word, 0) + 1
            current_word = ''
        else:
            current_word += c
    if current_word != '':
        current_word = trim(current_word)
        result[current_word] = result.get(current_word, 0) + 1
    print(result)
    return result

def delimiter(c):
    return True if c in ' :.,\n_\t' else False

# remove leading puntuation
def trim(s):
    s1 = re.sub(r'[^0-9A-Za-z]+\Z', '', s)
    return re.sub(r'^[^0-9A-Za-z]+', '', s1)
