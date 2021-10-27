// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let products : f64 = (speed as f64) * 221.0;
    if speed <= 4 {
        products
    } else if speed <= 8 {
        products * 0.9
    } else {
        products * 0.77
    }
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / 60.0) as u32
}
