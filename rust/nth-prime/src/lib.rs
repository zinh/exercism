pub fn nth(n: i32) -> Result<i32, String> {
    if n < 1 {
        return Err(String::from("Less than 1"));
    } else if n == 1 {
        return Ok(2);
    } else {
        let mut start = 3;
        let mut current_prime_count = 1;
        loop {
            if is_prime(start) {
                current_prime_count = current_prime_count + 1;
                if current_prime_count == n {
                    return Ok(start);
                }
            }
            start = start + 1;
        }
    }
}

pub fn is_prime(n: i32) -> bool {
    let mut d = 2;
    let limit = (n as f64).sqrt();
    loop {
        if n % d == 0 {
            return false;
        } else if d > (limit as i32) {
            break;
        }
        d = d + 1;
    }
    true
}
