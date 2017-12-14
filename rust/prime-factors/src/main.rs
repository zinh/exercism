extern crate prime_factors;
use prime_factors::factors;

fn main() {
    for i in factors(93819012551) {
        println!("{}", i);
    }
}
