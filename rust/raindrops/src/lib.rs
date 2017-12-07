pub fn raindrops(n: i32) -> String {
    let mut result: String = String::from("");

    if n % 3 == 0 {
        result.push_str("Pling");
    } 

    if n % 5 == 0 {
        result.push_str("Plang");
    } 

    if n % 7 == 0 {
        result.push_str("Plong");
    }
    if result == "" {
        result = n.to_string();
    }
    result
}
