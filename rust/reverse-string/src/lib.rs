pub fn reverse(input: &str) -> String {
    let mut result: String = String::from("");
    for c in input.chars() {
        result = c.to_string() + &result
    }
    result
}
