def hey(phrase):
    phrase = phrase.strip()
    if phrase == '':
        return 'Fine. Be that way!'
    if contain_character(phrase):
        if end_with_question(phrase) and all_capital(phrase):
            return "Calm down, I know what I'm doing!"
        elif all_capital(phrase):
            return 'Whoa, chill out!'
    if end_with_question(phrase):
        return 'Sure.'
    return 'Whatever.'

def end_with_question(phrase):
    return phrase.endswith('?')

def all_capital(phrase):
    for c in phrase:
        if c >= 'a' and c <= 'z':
            return False
    return True

def contain_character(phrase):
    for c in phrase:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            return True
    return False
