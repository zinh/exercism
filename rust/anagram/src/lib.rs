use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &'a [&str]) -> HashSet<&'a str> {
    let mut h: HashSet<&str> = HashSet::new();
    let lower_word = word.to_lowercase();
    for &possible_anagram in possible_anagrams {
        if is_anagrams(possible_anagram, &lower_word) {
            h.insert(possible_anagram);
        }
    }
    h
}

fn is_anagrams(word: &str, target_word: &str) -> bool {
    let mut word_vec : Vec<char> = word.chars().collect();
    let mut target_word_vec : Vec<char> = target_word.chars().collect();
    word_vec.sort_unstable();
    target_word_vec.sort_unstable();
}
