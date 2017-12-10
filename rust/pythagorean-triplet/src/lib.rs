pub fn find() -> Option<u32> {
    for a in 1..1000 {
        for b in a..1000 {
            if a + b < 1000 {
                let c = 1000 - a - b;
                if (a*a + b*b) == c*c {
                    return Some(a * b * c);
                }
            }
        }
    }
    return None;
}
