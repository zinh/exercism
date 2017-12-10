pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    let mut results: Vec<u32> = Vec::new();
    for factor in factors {
        for i in 1..limit {
            if i % factor == 0 && !exists(&results, i) {
                results.push(i);
            }
        }
    }
    return results.iter().fold(0, |acc, x| acc + x);
}

fn exists(arr: &Vec<u32>, item: u32) -> bool {
    for &i in arr {
        if item == i {
            return true;
        }
    }
    return false;
}
