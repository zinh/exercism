use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &'a [&str]) -> HashSet<&'a str> {
    let mut h: HashSet<&str> = HashSet::new();
    let lower_word = word.to_lowercase();
    for possible_anagram in possible_anagrams {
        if lower_word == possible_anagram.to_lowercase() {
            continue;
        }
        if is_anagrams(possible_anagram, &lower_word) {
            h.insert(possible_anagram);
        }
    }
    h
}

pub fn is_anagrams(word: &str, target_word: &str) -> bool {
    let mut word_vec : Vec<char> = word.to_lowercase().chars().collect();
    let mut target_word_vec : Vec<char> = target_word.chars().collect();
    word_vec.sort_unstable();
    target_word_vec.sort_unstable();
    if word_vec.len() != target_word_vec.len() {
        return false;
    }
    for (idx, c) in word_vec.iter().enumerate() {
        if *c != target_word_vec[idx] {
            return false;
        }
    }
    true
}
