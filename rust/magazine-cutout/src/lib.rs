// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut cache: HashMap<&str, u32> = HashMap::new();
    for &word in magazine {
        if cache.contains_key(word) {
        } else {
            cache.insert(word, 1);
        }
    }
    for &word in note {
    }
    true
}
