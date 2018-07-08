def detect_anagrams(word, candidates):
    sorted_word = ''.join(sorted(list(word.lower())))
    return [candidate for candidate in candidates if word.lower() != candidate.lower() and is_anagram(sorted_word, candidate.lower())]

def is_anagram(word, candidate):
    sorted_word = ''.join(sorted(list(candidate)))
    return word == sorted_word
