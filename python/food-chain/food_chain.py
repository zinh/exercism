m = {'bird': 'How absurd to swallow a bird!',
        'cat': 'Imagine that, to swallow a cat!',
        'dog': 'What a hog, to swallow a dog!',
        'goat': 'Just opened her throat and swallowed a goat!',
        'cow': "I don't know how she swallowed a cow!",
        'spider': 'It wriggled and jiggled and tickled inside her.',
        'fly': "I don't know why she swallowed the fly. Perhaps she'll die."}

animals = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow']

def recite(start_verse, end_verse):
    results = []
    for n in range(start_verse - 1, end_verse):
        results += verse(n)
        if n < end_verse - 1:
            results.append("")
    return results

def verse(n):
    if n == 0:
        return [first_sentence('fly'), m['fly']]
    if n >= 7:
        return ["I know an old lady who swallowed a horse.", "She's dead, of course!"]
    previous_animal = None
    results = []
    for i in range(n, -1, -1):
        animal = animals[i]
        if i == n:
            results.append(first_sentence(animal))
            results.append(m[animal])
        else:
            results.append(swallow_to_catch(previous_animal, animal))
        if i == 0:
            results.append(last_setence())
        previous_animal = animal
    return results

def first_sentence(animal):
    return f"I know an old lady who swallowed a {animal}."

def last_setence():
    return m['fly']

def swallow_to_catch(catch, be_catch):
    if be_catch == 'spider':
        return f"She swallowed the {catch} to catch the spider that wriggled and jiggled and tickled inside her."
    else:
        return f"She swallowed the {catch} to catch the {be_catch}."
