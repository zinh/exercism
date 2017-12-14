pub fn factors(n: u64) -> Vec<u64> {
    if n < 2 {
        return vec![];
    }
    let mut current_num = n;
    let mut div: u64 = 2;
    let mut result: Vec<u64> = vec![];
    while current_num != 1 {
        if current_num % div == 0 {
            result.push(div);
            current_num = current_num / div;
            div = 2;
        } else {
            div += 1;
        }
    }
    return result;
}
