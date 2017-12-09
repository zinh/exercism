pub fn verse(n: i32) -> String {
    format!("{} of beer on the wall, {} of beer.\n{}, {} of beer on the wall.\n", 
            pluralize(n, true), 
            pluralize(n, false), 
            counter(n),
            pluralize(n - 1, false))
}

pub fn sing(start: i32, end: i32) -> String {
    let mut verses: Vec<String> = Vec::new();
    for number in (end..start + 1).rev() {
        verses.push(verse(number))
    }
    verses.join("\n")
}

fn pluralize(num: i32, capitalize: bool) -> String {
    match num {
        -1 => String::from("99 bottles"),
        0 => if capitalize {
            String::from("No more bottles")
        } else {
            String::from("no more bottles")
        },
        1 => String::from("1 bottle"),
        _ => format!("{} bottles", num),
    }
}

fn counter(num: i32) -> String {
    match num {
        0 => String::from("Go to the store and buy some more"),
        1 => String::from("Take it down and pass it around"),
        _ => String::from("Take one down and pass it around"),
    }
}
